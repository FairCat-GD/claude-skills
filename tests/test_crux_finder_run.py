import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

SOURCE = Path(__file__).resolve().parent.parent / "evals" / "crux-finder" / "run.py"
_spec = importlib.util.spec_from_file_location("crux_finder_run", SOURCE)
assert _spec is not None and _spec.loader is not None
run = importlib.util.module_from_spec(_spec)
sys.modules["crux_finder_run"] = run
_spec.loader.exec_module(run)

# Every path this process opens while _OPENED is a list; an audit hook cannot be removed, so it
# records only inside the tests that ask it to.
_OPENED: list[str] | None = None


def _audit(event: str, args: tuple) -> None:
    if _OPENED is not None and event == "open":
        _OPENED.append(str(args[0]))


sys.addaudithook(_audit)

# Fictional cases: two neighbours on a ferry timetable, and a one-sided note on a tide gauge.
FERRY = "A: The last ferry should leave at ten.\n\nB: The last ferry should leave at eleven.\n"
TIDE = "---\nsource: written for this test\nlicense: maintainer-authored\n---\n\nA: Move it.\n"
GOLD = "---\ncrux: When people travel.\ntype: Empirical\ncrux_for: both\napproved_by: Tester\n---\n"
REPLY = "## Crux report\n\n**A, strongest form:** Ten.\n**B, strongest form:** Eleven.\n"

# The stub claude: it logs what it was given, then prints the events its mode asks for.
STUB = r"""
import json, os, sys
argv = sys.argv[1:]
prompt = sys.stdin.read()
with open(os.environ["STUB_LOG"], "a", encoding="utf-8") as log:
    memory = os.environ.get("CLAUDE_CODE_DISABLE_AUTO_MEMORY")
    seen = {"argv": argv, "cwd": os.getcwd(), "listing": sorted(os.listdir(".")),
            "stdin": prompt, "memory": memory}
    log.write(json.dumps(seen) + "\n")
mode = os.environ.get("STUB_MODE", "ok")
plugin = argv[argv.index("--plugin-dir") + 1]
plugins = [{"name": "crux-finder", "path": plugin}, {"name": "cc-plugin-x", "path": "builtin"}]
skills = ["crux-finder:crux-finder", "simplify"]
start = {"type": "system", "subtype": "init", "model": argv[argv.index("--model") + 1],
         "claude_code_version": "9.9.9", "permissionMode": "default", "mcp_servers": [],
         "plugins": plugins, "skills": skills}
if mode == "breach-plugin":
    plugins.append({"name": "kite-weather", "path": "/elsewhere/kite-weather"})
if mode == "breach-skill":
    skills.append("anthropic-skills:crux-finder")
if mode == "breach-model":
    start["model"] = "some-other-model"
print(json.dumps(start))
print(json.dumps({"type": "assistant", "message": {"content": [
    {"type": "tool_use", "name": "Skill", "input": {"skill": "crux-finder:crux-finder"}}]}}))
if mode == "fail":
    sys.stderr.write("the stub failed\n")
    sys.exit(3)
print(json.dumps({"type": "result", "is_error": mode == "error", "result": os.environ["STUB_REPLY"],
                  "total_cost_usd": 0.25, "permission_denials": [{"tool_name": "Bash"}]}))
"""


def _git(repo: Path, *args: str) -> str:
    env = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}
    identity = ["-c", "user.name=Test", "-c", "user.email=test@example.invalid"]
    return subprocess.run(
        ["git", *identity, *args], cwd=repo, env=env, check=True, capture_output=True, text=True
    ).stdout


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


@pytest.fixture
def root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    # A fictional repository: the plugin, two cases with their gold, all committed.
    repo = tmp_path / "repo"
    plugin = repo / "plugins" / "crux-finder"
    _write(plugin / ".claude-plugin" / "plugin.json", '{"name": "crux-finder", "version": "0.4.0"}')
    _write(plugin / "skills" / "crux-finder" / "SKILL.md", "---\nname: crux-finder\n---\n")
    evals = repo / "evals" / "crux-finder"
    for case, text in {"ferry": FERRY, "tide": TIDE}.items():
        _write(evals / "cases" / case / "input.md", text)
        _write(evals / "cases" / case / "gold.md", GOLD)
    _git(repo, "init", "-q", "-b", "main")
    _git(repo, "add", ".")
    _git(repo, "commit", "-q", "-m", "fixture")
    stub = tmp_path / "stub.py"
    stub.write_text(STUB, encoding="utf-8")
    monkeypatch.setattr(run, "ROOT", repo)
    monkeypatch.setattr(run, "CASES", evals / "cases")
    monkeypatch.setattr(run, "RESULTS", evals / "results")
    monkeypatch.setattr(run, "PLUGIN", plugin)
    monkeypatch.setattr(run, "CLAUDE", [sys.executable, str(stub)])
    monkeypatch.setenv("STUB_LOG", str(tmp_path / "stub.log"))
    monkeypatch.setenv("STUB_REPLY", REPLY)
    monkeypatch.delenv("STUB_MODE", raising=False)
    return repo


def _log(root: Path) -> list[dict]:
    path = root.parent / "stub.log"
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def _results(root: Path) -> Path:
    return root / "evals" / "crux-finder" / "results"


def _flag(argv: list[str], name: str) -> str:
    return argv[argv.index(name) + 1]


def test_each_run_is_written_with_its_header_and_the_reply_as_returned(root: Path) -> None:
    assert run.main(["--runs", "2"]) == 0
    head = _git(root, "rev-parse", "HEAD").strip()
    for case in ("ferry", "tide"):
        for number in (1, 2):
            text = (_results(root) / case / f"run-{number}.md").read_text(encoding="utf-8")
            header, body = run.split_frontmatter(text)
            assert header is not None
            fields = dict(line.split(": ", 1) for line in header.splitlines())
            assert fields["case"] == case
            assert fields["run"] == str(number)
            assert fields["model"] == run.MODEL
            assert fields["claude"] == "9.9.9"
            assert fields["skill_version"] == "0.4.0"
            assert fields["commit"] == head
            assert fields["skill_calls"] == run.SKILL
            assert fields["denials"] == "1"
            assert fields["cost_usd"] == "0.25"
            assert body == "\n" + REPLY
    assert len(_log(root)) == 4


def test_the_prompt_is_the_body_of_input_md_on_stdin(root: Path) -> None:
    assert run.main(["--runs", "1"]) == 0
    prompts = {Path(entry["cwd"]).parent.name: entry["stdin"] for entry in _log(root)}
    assert sorted(prompts.values()) == sorted([FERRY.strip(), "A: Move it."])
    # On stdin, never as an argument, so a body that starts with "-" is never read as a flag.
    assert all(entry["stdin"] not in entry["argv"] for entry in _log(root))


def test_each_run_is_a_fresh_isolated_session(root: Path) -> None:
    assert run.main(["--runs", "2"]) == 0
    entries = _log(root)
    folders = {entry["cwd"] for entry in entries}
    assert len(folders) == len(entries) == 4
    for entry in entries:
        argv, cwd = entry["argv"], Path(entry["cwd"]).resolve()
        assert entry["listing"] == []
        assert root.resolve() not in cwd.parents
        plugin = Path(_flag(argv, "--plugin-dir")).resolve()
        assert root.resolve() not in plugin.parents
        assert plugin.parent.parent == cwd.parent
        assert _flag(argv, "--add-dir") == _flag(argv, "--plugin-dir")
        assert _flag(argv, "--model") == run.MODEL
        assert _flag(argv, "--setting-sources") == ""
        assert _flag(argv, "--permission-prompts") == "none"
        assert {"-p", "--strict-mcp-config", "--no-session-persistence"} <= set(argv)
        assert not {"--continue", "-c", "--resume", "-r"} & set(argv)
        assert entry["memory"] == "1"
    # The temporary folders are gone once each run ends.
    assert not any(Path(folder).exists() for folder in folders)


def test_the_runner_never_opens_gold_md(root: Path) -> None:
    global _OPENED
    golds = list((root / "evals" / "crux-finder" / "cases").glob("*/gold.md"))
    for gold in golds:
        gold.chmod(0)
    _OPENED = []
    try:
        assert run.main(["--runs", "2"]) == 0
        opened = _OPENED
    finally:
        _OPENED = None
        for gold in golds:
            gold.chmod(0o644)
    assert any(path.endswith("input.md") for path in opened)
    assert not [path for path in opened if "gold" in Path(path).name]


def test_an_existing_result_is_skipped_never_overwritten(root: Path) -> None:
    kept = _results(root) / "ferry" / "run-1.md"
    _write(kept, "an earlier run\n")
    assert run.main(["--runs", "1"]) == 0
    assert kept.read_text(encoding="utf-8") == "an earlier run\n"
    assert len(_log(root)) == 1


def test_case_chooses_the_cases(root: Path) -> None:
    assert run.main(["--runs", "1", "--case", "tide"]) == 0
    assert sorted(p.name for p in _results(root).iterdir()) == ["tide"]


@pytest.mark.parametrize("mode", ["fail", "error"])
def test_a_failed_run_writes_nothing_and_stops(
    root: Path, mode: str, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setenv("STUB_MODE", mode)
    assert run.main(["--runs", "2"]) == 1
    assert not _results(root).exists() or not list(_results(root).rglob("*.md"))
    assert len(_log(root)) == 1
    assert "nothing written" in capsys.readouterr().out


@pytest.mark.parametrize(
    ("mode", "why"),
    [
        ("breach-plugin", "plugin kite-weather loaded"),
        ("breach-skill", "skill anthropic-skills:crux-finder loaded"),
        ("breach-model", "the model is some-other-model"),
    ],
)
def test_a_run_that_was_not_isolated_writes_nothing(
    root: Path,
    mode: str,
    why: str,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setenv("STUB_MODE", mode)
    assert run.main(["--runs", "1"]) == 1
    assert not _results(root).exists()
    assert why in capsys.readouterr().out


def test_an_empty_reply_writes_nothing(root: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("STUB_REPLY", "  \n")
    assert run.main(["--runs", "1"]) == 1
    assert not _results(root).exists()


def test_isolation_breaches_reads_the_whole_start_event(tmp_path: Path) -> None:
    plugin = tmp_path / "plugin" / "crux-finder"
    start = {
        "model": run.MODEL,
        "plugins": [{"name": "crux-finder", "path": str(plugin)}],
        "skills": [run.SKILL, "simplify"],
        "mcp_servers": [],
        "permissionMode": "default",
    }
    assert run.isolation_breaches(start, plugin) == []
    leaky = {
        **start,
        "skills": ["simplify"],
        "plugins": [],
        "mcp_servers": [{"name": "notes"}],
        "permissionMode": "auto",
        "memory_paths": {"auto": "/somewhere"},
    }
    assert run.isolation_breaches(leaky, plugin) == [
        "the plugin under test did not load",
        f"{run.SKILL} is not among the skills",
        "MCP server notes loaded",
        "the permission mode is auto",
        "memory is on",
    ]
    bare = {**start, "skills": [run.SKILL, "crux-finder"]}
    assert run.isolation_breaches(bare, plugin) == ["skill crux-finder loaded"]


def test_uncommitted_changes_to_the_plugin_refuse_every_run(
    root: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    skill = root / "plugins" / "crux-finder" / "skills" / "crux-finder" / "SKILL.md"
    skill.write_text("changed\n", encoding="utf-8")
    assert run.main(["--runs", "1"]) == 2
    assert _log(root) == []
    assert "uncommitted changes" in capsys.readouterr().out


@pytest.mark.parametrize(
    ("change", "message"),
    [
        (lambda cases: None, "unknown case(s) gale"),
        (lambda cases: (cases / "ferry" / "input.md").unlink(), "input.md: missing"),
        (
            lambda cases: (cases / "ferry" / "input.md").write_text("---\nsource: x\n"),
            "no closing ---",
        ),
        (
            lambda cases: (cases / "ferry" / "input.md").write_text("---\nsource: x\n---\n\n"),
            "no text after its frontmatter",
        ),
    ],
)
def test_a_bad_case_refuses_before_any_run(
    root: Path, change, message: str, capsys: pytest.CaptureFixture[str]
) -> None:
    change(root / "evals" / "crux-finder" / "cases")
    case = ["--case", "gale"] if "gale" in message else []
    assert run.main(["--runs", "1", *case]) == 2
    assert _log(root) == []
    assert message in capsys.readouterr().out


def test_no_cases_refuses(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(run, "CASES", tmp_path / "cases")
    assert run.main(["--runs", "1"]) == 2
    (tmp_path / "cases").mkdir()
    assert run.main(["--runs", "1"]) == 2


def test_runs_must_be_one_or_more() -> None:
    with pytest.raises(SystemExit):
        run.main(["--runs", "0"])


@pytest.mark.parametrize(
    ("manifest", "message"),
    [
        ("{not json", "plugin.json: cannot be read"),
        ('{"name": "crux-finder"}', "plugin.json: no version"),
    ],
)
def test_a_plugin_without_a_readable_version_refuses_before_any_run(
    root: Path, manifest: str, message: str, capsys: pytest.CaptureFixture[str]
) -> None:
    path = root / "plugins" / "crux-finder" / ".claude-plugin" / "plugin.json"
    path.write_text(manifest, encoding="utf-8")
    _git(root, "commit", "-q", "-am", "manifest")
    assert run.main(["--runs", "1"]) == 2
    assert _log(root) == []
    assert message in capsys.readouterr().out
