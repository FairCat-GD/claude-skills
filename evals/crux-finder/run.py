"""crux-finder's eval runner: one fresh, isolated `claude -p` session per case per run.

Each run starts in an empty temporary folder, with a copy of the plugin beside it and none of
the user's settings, MCP servers or memory, so it loads the plugin under test and Claude Code's
built-ins only, and it can read nothing outside those two folders. The prompt is the body of
cases/<id>/input.md, its frontmatter left out. The reply goes to results/<id>/run-<n>.md, after
a header naming the model, the CLI, the skill's version and the commit it ran on. The runner
never names or opens gold.md (invariant 6).

It spends real model runs: run it only where a session's block names it, one at a time.

Usage: uv run evals/crux-finder/run.py --runs N [--case ID ...]
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from shutil import copytree

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
CASES = HERE / "cases"
RESULTS = HERE / "results"
PLUGIN = ROOT / "plugins" / "crux-finder"
# Named here and written into every result, so that cycles compare.
MODEL = "claude-opus-5-5"
# The plugin's skill, as the Skill tool and the run's start event name it.
SKILL = "crux-finder:crux-finder"
# A list, so a test can put a stub in its place.
CLAUDE = ["claude"]
TIMEOUT_SECONDS = 900
BUDGET_USD = "2"
# Measured with claude 2.1.329: with these, the start event lists the copy and
# Claude Code's built-ins only, no MCP server, the default permission mode and no memory paths,
# and a read outside the run's two folders is denied, by Read and by Bash alike.
ISOLATION = [
    "--setting-sources",
    "",
    "--strict-mcp-config",
    "--no-session-persistence",
    "--permission-prompts",
    "none",
]
ENVIRONMENT = {"CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1"}


class Refusal(Exception):
    """Nothing can run: a bad request, or a state no result should be written from."""


class RunFailed(Exception):
    """A run went wrong; nothing was written for it."""


def split_frontmatter(text: str) -> tuple[str | None, str]:
    """The frontmatter's lines and the body; no frontmatter gives None and the whole text."""
    lines = text.split("\n")
    if lines[0].rstrip() != "---":
        return None, text
    for index, line in enumerate(lines[1:], start=1):
        if line.rstrip() == "---":
            return "\n".join(lines[1:index]), "\n".join(lines[index + 1 :])
    raise ValueError("its frontmatter has no closing ---")


def _relative(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def _prompts(chosen: list[str]) -> dict[str, str]:
    """Each case's prompt, by id, read from its input.md alone."""
    if not CASES.is_dir():
        raise Refusal(f"no cases: {_relative(CASES)} does not exist")
    ids = sorted(p.name for p in CASES.iterdir() if p.is_dir() and not p.name.startswith("."))
    if not ids:
        raise Refusal(f"no cases in {_relative(CASES)}")
    unknown = [case for case in chosen if case not in ids]
    if unknown:
        raise Refusal(f"unknown case(s) {', '.join(unknown)}; cases: {', '.join(ids)}")
    prompts = {}
    for case in chosen or ids:
        source = CASES / case / "input.md"
        try:
            _, body = split_frontmatter(source.read_text(encoding="utf-8"))
        except OSError:
            raise Refusal(f"{_relative(source)}: missing") from None
        except ValueError as error:
            raise Refusal(f"{_relative(source)}: {error}") from None
        if not body.strip():
            raise Refusal(f"{_relative(source)}: no text after its frontmatter")
        prompts[case] = body.strip()
    return prompts


def _git(*args: str) -> str:
    try:
        done = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            stdin=subprocess.DEVNULL,
        )
    except OSError as error:
        raise Refusal(f"cannot run git: {error}") from None
    if done.returncode != 0:
        raise Refusal(f"git {' '.join(args)}: {done.stderr.strip()}")
    return done.stdout.strip()


def _skill_version() -> str:
    """The plugin's version, read before any run is spent."""
    manifest = PLUGIN / ".claude-plugin" / "plugin.json"
    try:
        version = json.loads(manifest.read_text(encoding="utf-8")).get("version")
    except (OSError, ValueError, AttributeError) as error:
        raise Refusal(f"{_relative(manifest)}: cannot be read ({error})") from None
    if not isinstance(version, str) or not version:
        raise Refusal(f"{_relative(manifest)}: no version")
    return version


def _commit() -> str:
    """HEAD, refusing while the plugin has changes no commit holds."""
    plugin = _relative(PLUGIN)
    if _git("status", "--porcelain", "--", plugin):
        raise Refusal(
            f"{plugin} has uncommitted changes; commit them, so each result names its skill"
        )
    return _git("rev-parse", "HEAD")


def _events(stdout: str) -> list[dict]:
    events = []
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if isinstance(event, dict):
            events.append(event)
    return events


def _same(a: str, b: Path) -> bool:
    return os.path.realpath(a) == os.path.realpath(b)


def isolation_breaches(start: dict, plugin: Path) -> list[str]:
    """What, in the run's start event, shows the run was not isolated."""
    breaches = []
    if start.get("model") != MODEL:
        breaches.append(f"the model is {start.get('model')}, not {MODEL}")
    plugins = [p for p in start.get("plugins") or [] if p.get("path") != "builtin"]
    if not any(_same(str(p.get("path")), plugin) for p in plugins):
        breaches.append("the plugin under test did not load")
    breaches += [
        f"plugin {p.get('name')} loaded from {p.get('path')}"
        for p in plugins
        if not _same(str(p.get("path")), plugin)
    ]
    skills = start.get("skills") or []
    if SKILL not in skills:
        breaches.append(f"{SKILL} is not among the skills")
    # Claude Code's own skills carry no namespace; a plugin's or a synced upload's do.
    breaches += [
        f"skill {skill} loaded"
        for skill in skills
        if skill != SKILL and (":" in skill or skill == SKILL.split(":")[1])
    ]
    breaches += [
        f"MCP server {server.get('name')} loaded" for server in start.get("mcp_servers") or []
    ]
    if start.get("permissionMode") != "default":
        breaches.append(f"the permission mode is {start.get('permissionMode')}")
    if start.get("memory_paths"):
        breaches.append("memory is on")
    return breaches


def _skill_calls(events: list[dict]) -> list[str]:
    calls = []
    for event in events:
        if event.get("type") != "assistant":
            continue
        for block in event.get("message", {}).get("content") or []:
            if block.get("type") == "tool_use" and block.get("name") == "Skill":
                calls.append(str(block.get("input", {}).get("skill")))
    return calls


def run_once(case: str, number: int, prompt: str, commit: str, version: str) -> str:
    """One isolated session; the result file's text."""
    with tempfile.TemporaryDirectory(prefix="crux-finder-run-") as folder:
        work = Path(folder) / "work"
        work.mkdir()
        plugin = Path(folder) / "plugin" / PLUGIN.name
        copytree(PLUGIN, plugin)
        command = [
            *CLAUDE,
            "-p",
            "--model",
            MODEL,
            "--output-format",
            "stream-json",
            "--verbose",
            "--plugin-dir",
            str(plugin),
            # The skill reads its references from the copy; nothing else outside work/ is open.
            "--add-dir",
            str(plugin),
            *ISOLATION,
            "--max-budget-usd",
            BUDGET_USD,
        ]
        try:
            # The prompt goes in on stdin, so a body that starts with "-" is never a flag.
            done = subprocess.run(
                command,
                cwd=work,
                input=prompt,
                capture_output=True,
                text=True,
                timeout=TIMEOUT_SECONDS,
                env={**os.environ, **ENVIRONMENT},
            )
        except subprocess.TimeoutExpired:
            raise RunFailed(f"no reply within {TIMEOUT_SECONDS} s") from None
        except OSError as error:
            raise RunFailed(f"cannot run {CLAUDE[0]}: {error}") from None
        events = _events(done.stdout)
        start = next(
            (e for e in events if e.get("type") == "system" and e.get("subtype") == "init"), None
        )
        if start is None:
            raise RunFailed(f"no start event; exit {done.returncode}: {done.stderr.strip()[-500:]}")
        breaches = isolation_breaches(start, plugin)
        if breaches:
            raise RunFailed(f"not isolated: {'; '.join(breaches)}")
        result = next((e for e in reversed(events) if e.get("type") == "result"), None)
        reply = result.get("result") if result else None
        if done.returncode != 0 or result is None or result.get("is_error"):
            raise RunFailed(f"exit {done.returncode}: {done.stderr.strip()[-500:] or reply}")
        if not isinstance(reply, str) or not reply.strip():
            raise RunFailed("an empty reply")
        calls = _skill_calls(events)
        header = {
            "case": case,
            "run": str(number),
            "model": str(start.get("model")),
            "claude": str(start.get("claude_code_version")),
            "skill_version": version,
            "commit": commit,
            "date": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "skill_calls": ", ".join(calls) or "none",
            "denials": str(len(result.get("permission_denials") or [])),
            "cost_usd": str(result.get("total_cost_usd")),
        }
    lines = "".join(f"{key}: {value}\n" for key, value in header.items())
    # The reply as returned, with a last newline added where it has none.
    return f"---\n{lines}---\n\n{reply}" + ("" if reply.endswith("\n") else "\n")


def _positive(value: str) -> int:
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("must be 1 or more")
    return number


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="One isolated claude -p run per case per run.")
    parser.add_argument("--runs", type=_positive, required=True, help="runs per case")
    parser.add_argument("--case", action="append", default=[], help="only this case (repeatable)")
    options = parser.parse_args(argv)
    try:
        prompts = _prompts(options.case)
        commit = _commit()
        version = _skill_version()
    except Refusal as refusal:
        print(f"run.py: {refusal}")
        return 2
    # One run at a time: the eval runner is an exclusive resource.
    for case, prompt in prompts.items():
        for number in range(1, options.runs + 1):
            target = RESULTS / case / f"run-{number}.md"
            if target.exists():
                print(f"run.py: {_relative(target)} exists; skipped")
                continue
            try:
                text = run_once(case, number, prompt, commit, version)
            except RunFailed as failure:
                print(f"run.py: {case} run {number}: {failure}; nothing written")
                return 1
            target.parent.mkdir(parents=True, exist_ok=True)
            partial = target.with_name(f".{target.name}.partial")
            partial.write_text(text, encoding="utf-8")
            partial.replace(target)
            print(f"run.py: wrote {_relative(target)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
