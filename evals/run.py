"""The eval runner every skill shares: `claude plugin eval` on the skill's cases, one file per run.

Given a skill, it runs the engine on `evals/<skill>/cases/` and writes, for each run,
`evals/<skill>/results/<id>/run-N.md` (a header, the run's tool calls, the final reply) and
`verdicts-N.md` beside it (each grader's verdict), every machine path scrubbed. The engine runs on a
temporary copy of the plugin, with the chosen cases under the copy's `evals/` and each case's
`gold.md` left out by name, so neither the runner nor the session under test ever opens it
(invariant 6). It refuses while the plugin or the cases have uncommitted changes, so every result's
`commit` holds what ran.

It spends real model runs: run it only where a session's block names it, one cycle at a time.

Usage: uv run evals/run.py <skill> --runs N --max-cost-usd USD [--case ID ...] [--trial FOLDER]
"""

import argparse
import json
import math
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

import shared

ROOT = Path(__file__).resolve().parent.parent
# Named here and written into every result, so that cycles compare.
MODEL = "claude-opus-5-5"
# The engine's default judge, measured with claude 2.1.330, pinned so a change of judge is a
# visible decision rather than a new release of the alias.
JUDGE_MODEL = "claude-haiku-5-5"
CONCURRENCY = 4
# The tools each skill's cases need beyond the engine's read-only set, granted with --allow-tools.
SKILLS: dict[str, tuple[str, ...]] = {
    "crux-finder": (),
    "provenance-tracer": ("WebSearch", "WebFetch"),
}
# A list, so a test can put a stub in its place.
CLAUDE = ["claude"]
SCHEMA_VERSION = 1
# What an isolated run's start event shows, measured with claude 2.1.330: the engine runs every
# case in this mode, denying whatever the case does not allow.
PERMISSION_MODE = "dontAsk"
# The engine caps each run at 3,600 s at most, so no call outlasts this many seconds per round of
# CONCURRENCY runs; the cap only catches an engine that hangs.
RUN_SECONDS = 3600
GRACE_SECONDS = 600
# Variables of a launching Claude Code session (its model, effort, entry point) would reach the
# engine; none is needed, since the CLI signs in with its own stored login.
_STRIPPED = re.compile(r"(CLAUDE|ANTHROPIC_)")
_AGENT_TOOLS = ("Agent", "Task")
_REFUSED = re.compile(r"denied by your permission settings|has been denied")
# The argument each tool's line shows; any other tool shows its whole input as one-line JSON.
_ARGUMENT = {
    "WebSearch": "query",
    "WebFetch": "url",
    "Skill": "skill",
    "Read": "file_path",
    "Agent": "subagent_type",
    "Task": "subagent_type",
}


class Refusal(Exception):
    """Nothing can run: a bad request, or a state no result should be written from."""


@dataclass(frozen=True)
class Request:
    skill: str
    runs: int
    ceiling: float
    cases: list[str]
    trial: Path | None


def _relative(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def _git(*args: str) -> str:
    try:
        done = subprocess.run(
            ["git", *args], cwd=ROOT, capture_output=True, text=True, stdin=subprocess.DEVNULL
        )
    except OSError as error:
        raise Refusal(f"cannot run git: {error}") from None
    if done.returncode != 0:
        raise Refusal(f"git {' '.join(args)}: {done.stderr.strip()}")
    return done.stdout.strip()


def _plugin(skill: str) -> Path:
    return ROOT / "plugins" / skill


def _cases_folder(skill: str) -> Path:
    return ROOT / "evals" / skill / "cases"


def _case_ids(request: Request) -> list[str]:
    """The chosen cases, each a folder holding a prompt.md, which is never opened here."""
    if request.skill not in SKILLS:
        raise Refusal(f"unknown skill {request.skill}; skills: {', '.join(sorted(SKILLS))}")
    if not _plugin(request.skill).is_dir():
        raise Refusal(f"no plugin: {_relative(_plugin(request.skill))} does not exist")
    folder = _cases_folder(request.skill)
    if not folder.is_dir():
        raise Refusal(f"no cases: {_relative(folder)} does not exist")
    ids = sorted(p.name for p in folder.iterdir() if p.is_dir() and not p.name.startswith("."))
    if not ids:
        raise Refusal(f"no cases in {_relative(folder)}")
    unknown = [case for case in request.cases if case not in ids]
    if unknown:
        raise Refusal(f"unknown case(s) {', '.join(unknown)}; cases: {', '.join(ids)}")
    chosen = sorted(set(request.cases)) or ids
    without = [case for case in chosen if not (folder / case / "prompt.md").is_file()]
    if without:
        raise Refusal(f"no prompt.md in {', '.join(without)}")
    return chosen


def _uncommitted(path: Path) -> bool:
    return bool(_git("status", "--porcelain", "--", _relative(path)))


def _skill_version(skill: str) -> str:
    manifest = _plugin(skill) / ".claude-plugin" / "plugin.json"
    try:
        version = json.loads(manifest.read_text(encoding="utf-8")).get("version")
    except (OSError, ValueError, AttributeError) as error:
        raise Refusal(f"{_relative(manifest)}: cannot be read ({error})") from None
    if not isinstance(version, str) or not version:
        raise Refusal(f"{_relative(manifest)}: no version")
    return version


def _check_state(request: Request) -> tuple[str, str]:
    """The skill's version and HEAD, refusing a state whose results would not name what ran."""
    if _uncommitted(_plugin(request.skill)):
        raise Refusal(
            f"{_relative(_plugin(request.skill))} has uncommitted changes; commit them, "
            "so each result names its skill"
        )
    if request.trial is None and _uncommitted(_cases_folder(request.skill)):
        raise Refusal(
            f"{_relative(_cases_folder(request.skill))} has uncommitted changes; commit them, "
            "so each result names the graders it ran with, or run a --trial"
        )
    if request.trial is not None:
        trial = request.trial.resolve()
        if trial == ROOT.resolve() or ROOT.resolve() in trial.parents:
            raise Refusal(f"--trial {request.trial} is inside the repository")
    return _skill_version(request.skill), _git("rev-parse", "HEAD")


def _results_folder(request: Request) -> Path:
    if request.trial is not None:
        return request.trial
    return ROOT / "evals" / request.skill / "results"


def missing_runs(results: Path, cases: list[str], runs: int) -> dict[str, list[int]]:
    """For each case, the run numbers from 1 to `runs` with no run-N.md yet."""
    missing = {}
    for case in cases:
        numbers = [n for n in range(1, runs + 1) if not (results / case / f"run-{n}.md").exists()]
        if numbers:
            missing[case] = numbers
    return missing


def environment() -> dict[str, str]:
    """The launching environment, without the variables that would change a run."""
    return {key: value for key, value in os.environ.items() if not _STRIPPED.match(key)}


def engine_command(plugin: Path, out: Path, runs: int, ceiling: float, tools: tuple[str, ...]):
    """The engine's command line; the target comes first and --allow-tools, which takes a list,
    last."""
    return [
        *CLAUDE,
        "plugin",
        "eval",
        str(plugin),
        "--model",
        MODEL,
        "--judge-model",
        JUDGE_MODEL,
        "--ablation",
        "none",
        "--no-publish",
        "--trust-plugin",
        # Each run's trace, the only place its reply and tool calls are, is kept only so.
        "--keep-temp",
        # A low score is a result; exit 1 is then a failure to load or to run.
        "--threshold",
        "0",
        "--concurrency",
        str(CONCURRENCY),
        "--runs",
        str(runs),
        "--max-cost-usd",
        f"{ceiling:.2f}",
        "--output-dir",
        str(out),
        *(["--allow-tools", *tools] if tools else []),
    ]


def _copy(skill: str, cases: list[str], folder: Path) -> Path:
    """The plugin under folder/plugin/<skill>, with the cases under its evals/ and no gold.md."""
    plugin = folder / "plugin" / skill
    shutil.copytree(_plugin(skill), plugin)
    for case in cases:
        # Left out by name, so it is never opened; the graders are copied byte for byte.
        shutil.copytree(
            _cases_folder(skill) / case,
            plugin / "evals" / case,
            ignore=shutil.ignore_patterns("gold.md"),
        )
    return plugin


def _run_engine(command: list[str], cwd: Path, runs: int) -> tuple[int | None, str]:
    """The engine's exit code (None when it had to be stopped) and the end of its stderr."""
    seconds = math.ceil(runs / CONCURRENCY) * RUN_SECONDS + GRACE_SECONDS
    try:
        process = subprocess.Popen(
            command,
            cwd=cwd,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=environment(),
        )
    except OSError as error:
        return 1, f"cannot run {CLAUDE[0]}: {error}"
    try:
        _, stderr = process.communicate(timeout=seconds)
        return process.returncode, stderr
    except subprocess.TimeoutExpired:
        # Terminated, the engine still writes what it has as a partial result.
        process.terminate()
        try:
            _, stderr = process.communicate(timeout=60)
        except subprocess.TimeoutExpired:
            process.kill()
            _, stderr = process.communicate()
        return None, f"stopped after {seconds} s\n{stderr}"


class Scrubber:
    """Replaces the machine paths a run's text may hold with placeholders, longest first."""

    def __init__(self, places: list[tuple[Path, str]], home: Path) -> None:
        pairs = {}
        for path, placeholder in places:
            for form in _forms(path):
                pairs.setdefault(form, placeholder)
        self.pairs = sorted(pairs.items(), key=lambda pair: len(pair[0]), reverse=True)
        home_text = str(home)
        self.home_forms = {
            home_text,
            home_text.replace("/", "-"),
            quote(home_text, safe=""),
            home_text.replace("/", "\\/"),
        }

    def __call__(self, text: str) -> str:
        for form, placeholder in self.pairs:
            text = text.replace(form, placeholder)
        return text

    def leftover(self, text: str) -> str | None:
        """A machine path the replacement missed: the home folder in any form, or a temp folder."""
        for form in self.home_forms:
            if form in text:
                return "the home folder"
        if re.search(r"/(?:private/)?var/folders/", text):
            return "a temporary folder"
        return None


def _forms(path: Path) -> set[str]:
    """A path as given and as resolved, with and without macOS's /private."""
    forms = set()
    for text in (str(path), os.path.realpath(path)):
        forms.add(text)
        if text.startswith("/private/"):
            forms.add(text[len("/private") :])
        elif text.startswith(("/var/", "/tmp/", "/etc/")):
            forms.add("/private" + text)
    return {form for form in forms if len(form) > 1}


def _events(trace: Path) -> list[dict]:
    events = []
    for line in trace.read_text(encoding="utf-8").splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if isinstance(event, dict):
            events.append(event)
    return events


def _same(a: object, b: Path) -> bool:
    return os.path.realpath(str(a)) == os.path.realpath(b)


def _inside(path: object, folder: Path) -> bool:
    real = os.path.realpath(str(path))
    root = os.path.realpath(folder)
    return real == root or real.startswith(root + os.sep)


def isolation_breaches(start: dict, plugin: Path, skill: str, sandbox: Path) -> list[str]:
    """What, in a run's start event, shows the run was not isolated."""
    breaches = []
    if start.get("model") != MODEL:
        breaches.append(f"the model is {start.get('model')}, not {MODEL}")
    plugins = [p for p in start.get("plugins") or [] if p.get("path") != "builtin"]
    if not any(_same(p.get("path"), plugin) for p in plugins):
        breaches.append("the plugin under test did not load")
    breaches += [
        f"plugin {p.get('name')} loaded from {p.get('path')}"
        for p in plugins
        if not _same(p.get("path"), plugin)
    ]
    name = f"{skill}:{skill}"
    skills = start.get("skills") or []
    if name not in skills:
        breaches.append(f"{name} is not among the skills")
    # Claude Code's own skills carry no namespace; a plugin's or a synced upload's do.
    breaches += [
        f"skill {other} loaded"
        for other in skills
        if other != name and (":" in other or other == skill)
    ]
    breaches += [f"MCP server {s.get('name')} loaded" for s in start.get("mcp_servers") or []]
    if start.get("permissionMode") != PERMISSION_MODE:
        breaches.append(f"the permission mode is {start.get('permissionMode')}")
    # Each run has a memory folder in its own temporary home, empty; any other is the user's.
    breaches += [
        f"memory at {path}"
        for path in (start.get("memory_paths") or {}).values()
        if not _inside(path, sandbox)
    ]
    breaches += [f"folder {path} opened" for path in start.get("additional_directories") or []]
    return breaches


def _argument(tool: str, given: object) -> str:
    if isinstance(given, dict) and isinstance(given.get(_ARGUMENT.get(tool, "")), str):
        return given[_ARGUMENT[tool]]
    return json.dumps(given, ensure_ascii=False, separators=(",", ":"))


def tool_calls(events: list[dict]) -> list[shared.Call]:
    """Every tool call in a run's trace, in order, a subagent's included, each with its outcome."""
    agents: dict[str, str] = {}
    denied: set[str] = set()
    failed: set[str] = set()
    for event in events:
        if event.get("type") == "system" and event.get("subtype") == "permission_denied":
            denied.add(str(event.get("tool_use_id")))
        if event.get("type") == "result":
            denied |= {str(d.get("tool_use_id")) for d in event.get("permission_denials") or []}
        if event.get("type") == "user":
            for block in _blocks(event):
                if block.get("type") == "tool_result" and block.get("is_error"):
                    failed.add(str(block.get("tool_use_id")))
                    # A read of the eval folder is refused as an error, with no denial event.
                    if _REFUSED.search(str(block.get("content"))):
                        denied.add(str(block.get("tool_use_id")))
    calls = []
    for event in events:
        if event.get("type") != "assistant":
            continue
        parent = event.get("parent_tool_use_id")
        for block in _blocks(event):
            if block.get("type") != "tool_use":
                continue
            tool, given, ident = str(block.get("name")), block.get("input"), str(block.get("id"))
            if tool in _AGENT_TOOLS and isinstance(given, dict):
                agents[ident] = str(given.get("subagent_type") or "subagent")
            outcome = "denied" if ident in denied else "error" if ident in failed else ""
            subagent = agents.get(str(parent), "subagent") if parent else None
            calls.append(shared.Call(tool, _argument(tool, given), subagent, outcome))
    return calls


def _blocks(event: dict) -> list[dict]:
    content = (event.get("message") or {}).get("content")
    return (
        [block for block in content if isinstance(block, dict)] if isinstance(content, list) else []
    )


def _sandbox(run: dict) -> Path | None:
    """The engine's kept folder for a run: the one holding out/trace.jsonl, named as the engine
    names it (e-XXXXXX), since the runner removes it and must never take another folder for it."""
    trace = run.get("tracePath")
    if not isinstance(trace, str):
        return None
    folder = Path(trace).parent.parent
    if Path(trace).parent.name != "out" or not folder.name.startswith("e-"):
        return None
    return folder


def _remove(folder: Path) -> None:
    """A kept folder, which the engine leaves read-only with a part sealed at mode 000."""
    if not folder.exists():
        return
    for path, folders, _ in os.walk(folder):
        os.chmod(path, stat.S_IRWXU)
        for name in folders:
            os.chmod(os.path.join(path, name), stat.S_IRWXU)
    shutil.rmtree(folder)


def _date(started: object) -> str:
    match = re.match(r"(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d)", str(started))
    return f"{match.group(1)}Z" if match else "unknown"


@dataclass
class Written:
    run: str
    verdicts: str


def render(
    case: dict,
    run: dict,
    number: int,
    *,
    skill: str,
    version: str,
    commit: str,
    plugin: Path,
    folder: Path,
) -> Written:
    """One run's two files, or RuntimeError with the reason none is written."""
    if run.get("aborted"):
        raise RuntimeError(f"aborted: {run['aborted']}")
    if run.get("skippedPaidGraders"):
        raise RuntimeError("its judges were skipped at the cost ceiling")
    graders = run.get("graders") or []
    if not graders:
        raise RuntimeError(f"not graded: {run.get('error') or 'no grader results'}")
    sandbox = _sandbox(run)
    trace = Path(run["tracePath"]) if sandbox else None
    if trace is None or not trace.is_file():
        raise RuntimeError("its trace was not kept")
    events = _events(trace)
    start = next(
        (e for e in events if e.get("type") == "system" and e.get("subtype") == "init"), None
    )
    if start is None:
        raise RuntimeError("its trace has no start event")
    breaches = isolation_breaches(start, plugin, skill, sandbox)
    if breaches:
        raise RuntimeError(f"not isolated: {'; '.join(breaches)}")
    result = next((e for e in reversed(events) if e.get("type") == "result"), None)
    reply = result.get("result") if result else None
    places = [(plugin, "<plugin>"), (folder, "<temp>"), (sandbox, "<temp>"), (ROOT, "<repo>")]
    if isinstance(start.get("cwd"), str):
        places.insert(0, (Path(start["cwd"]), "<workspace>"))
    scrub = Scrubber([*places, (Path.home(), "~")], Path.home())
    calls = [
        shared.Call(c.tool, scrub(c.argument), c.subagent, c.outcome) for c in tool_calls(events)
    ]
    header = {
        "case": case["name"],
        "run": str(number),
        "model": str(start.get("model")),
        "claude": str(start.get("claude_code_version")),
        "skill_version": version,
        "commit": commit,
        "date": _date(run.get("startedAt")),
        "cost_usd": f"{float(run.get('costUsd') or 0):.4f}",
        "duration_s": str(run.get("durationSeconds")),
        "turns": str(run.get("turns")),
        "error": shared.one_line(scrub(str(run.get("error")))) if run.get("error") else "none",
    }
    types = {g.get("name"): str(g.get("type")) for g in case.get("graders") or []}
    verdicts = [
        shared.Verdict(
            name=str(g.get("name")),
            type=types.get(g.get("name"), "unknown"),
            passed=bool(g.get("passed")),
            scored=bool(g.get("scored", True)),
            weight=str(g.get("weight")),
            votes=" ".join("pass" if v else "fail" for v in g["judgeVotes"])
            if isinstance(g.get("judgeVotes"), list)
            else "none",
            explanation=scrub(str(g.get("explanation") or "")),
        )
        for g in graders
    ]
    texts = Written(
        shared.format_run(header, calls, scrub(reply) if isinstance(reply, str) else ""),
        shared.format_verdicts(
            {
                "case": case["name"],
                "run": str(number),
                "score": str(run.get("score")),
                "judge_model": JUDGE_MODEL,
                "judge_cost_usd": f"{float(run.get('judgeCostUsd') or 0):.4f}",
            },
            verdicts,
        ),
    )
    for text in (texts.run, texts.verdicts):
        left = scrub.leftover(text)
        if left:
            raise RuntimeError(f"its text still names {left}")
    return texts


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    partial = path.with_name(f".{path.name}.partial")
    partial.write_text(text, encoding="utf-8")
    partial.replace(path)


def _say(message: str) -> None:
    print(f"evals/run.py: {message}", flush=True)


def run_group(
    request: Request,
    missing: dict[str, list[int]],
    count: int,
    ceiling: float,
    version: str,
    commit: str,
) -> tuple[bool, float]:
    """One engine call for the cases missing `count` runs; whether every run was written, and the
    spend the engine reported."""
    with tempfile.TemporaryDirectory(prefix=f"{request.skill}-eval-") as name:
        folder = Path(name)
        plugin = _copy(request.skill, sorted(missing), folder)
        out = folder / "out"
        command = engine_command(plugin, out, count, ceiling, SKILLS[request.skill])
        code, stderr = _run_engine(command, folder, len(missing) * count)
        try:
            data = json.loads((out / "aggregate-result.json").read_text(encoding="utf-8"))
        except (OSError, ValueError):
            _say(f"no result from the engine (exit {code}): {stderr.strip()[-800:]}")
            return False, 0.0
        if not isinstance(data, dict):
            _say("the engine's result is not an object")
            return False, 0.0
        cases = {c.get("name"): c for c in data.get("cases") or [] if isinstance(c, dict)}
        sandboxes = [
            sandbox
            for case in cases.values()
            for arm in ((case.get("arms") or {}).values())
            for sandbox in map(_sandbox, arm if isinstance(arm, list) else [])
            if sandbox is not None
        ]
        try:
            complete = _write_group(
                request, missing, data, cases, stderr, version, commit, plugin, folder
            )
        finally:
            for sandbox in sandboxes:
                _remove(sandbox)
        if code not in (0, 1, 2):
            complete = False
        return complete, float(data.get("costUsd") or 0)


def _write_group(
    request: Request,
    missing: dict[str, list[int]],
    data: dict,
    cases: dict,
    stderr: str,
    version: str,
    commit: str,
    plugin: Path,
    folder: Path,
) -> bool:
    if data.get("schemaVersion") != SCHEMA_VERSION:
        _say(f"a result of schema {data.get('schemaVersion')!r}, not {SCHEMA_VERSION}")
        return False
    extra = sorted(map(str, set(cases) - set(missing)))
    if extra:
        _say(f"the engine ran case(s) it was not given: {', '.join(extra)}")
        return False
    results = _results_folder(request)
    complete = True
    for case_id, numbers in sorted(missing.items()):
        case = cases.get(case_id)
        if case is None:
            _say(f"{case_id}: did not load; nothing written ({stderr.strip()[-800:]})")
            complete = False
            continue
        written = 0
        for run in (case.get("arms") or {}).get("with") or []:
            if written == len(numbers):
                break
            number = numbers[written]
            try:
                texts = render(
                    case,
                    run,
                    number,
                    skill=request.skill,
                    version=version,
                    commit=commit,
                    plugin=plugin,
                    folder=folder,
                )
            except RuntimeError as reason:
                _say(f"{case_id}: a run not written: {reason}")
                continue
            target = results / case_id / f"run-{number}.md"
            # The run file last: it is what a later call skips on.
            _write(target.with_name(f"verdicts-{number}.md"), texts.verdicts)
            _write(target, texts.run)
            _say(f"wrote {_relative(target)}")
            written += 1
        if written < len(numbers):
            complete = False
    if data.get("partial"):
        _say(f"the engine stopped early: {data.get('partialReason')}")
        complete = False
    return complete


def _positive(kind):
    def parse(value: str):
        number = kind(value)
        if not math.isfinite(number) or number <= 0:
            raise argparse.ArgumentTypeError("must be a number more than 0")
        return number

    return parse


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="claude plugin eval on a skill's cases.")
    parser.add_argument("skill", help="the skill whose cases run")
    parser.add_argument("--runs", type=_positive(int), required=True, help="runs per case")
    parser.add_argument(
        "--max-cost-usd", type=_positive(float), required=True, help="the whole command's ceiling"
    )
    parser.add_argument("--case", action="append", default=[], help="only this case (repeatable)")
    parser.add_argument("--trial", type=Path, help="write results here, outside the repository")
    options = parser.parse_args(argv)
    request = Request(
        options.skill, options.runs, options.max_cost_usd, options.case, options.trial
    )
    try:
        cases = _case_ids(request)
        version, commit = _check_state(request)
    except Refusal as refusal:
        _say(str(refusal))
        return 2
    missing = missing_runs(_results_folder(request), cases, request.runs)
    for case in cases:
        if case not in missing:
            _say(f"{case}: every run exists; skipped")
    groups: dict[int, dict[str, list[int]]] = {}
    for case, numbers in missing.items():
        groups.setdefault(len(numbers), {})[case] = numbers
    complete = True
    left = request.ceiling
    for count, group in sorted(groups.items(), reverse=True):
        # The engine reads its ceiling to the cent.
        if left < 0.01:
            _say(f"the ceiling is spent; not run: {', '.join(sorted(group))}")
            complete = False
            continue
        done, spent = run_group(request, group, count, left, version, commit)
        complete = complete and done
        left -= spent
    return 0 if complete else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
