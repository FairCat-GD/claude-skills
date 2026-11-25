import importlib.util
import json
import os
import stat
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote

import pytest

import shared

SOURCE = Path(__file__).resolve().parent.parent / "evals" / "run.py"
_spec = importlib.util.spec_from_file_location("evals_run", SOURCE)
assert _spec is not None and _spec.loader is not None
run = importlib.util.module_from_spec(_spec)
sys.modules["evals_run"] = run
_spec.loader.exec_module(run)

# Every path this process opens while _OPENED is a list; an audit hook cannot be removed, so it
# records only inside the tests that ask it to.
_OPENED: list[str] | None = None


def _audit(event: str, args: tuple) -> None:
    if _OPENED is not None and event == "open":
        _OPENED.append(str(args[0]))


sys.addaudithook(_audit)

SKILL = "tidewatch"
PROMPT = "---\nallowed_tools: [Skill, Read]\n---\n\nWhen is the last ferry?\n"
GRADER = "---\ntype: llm\n---\n\nPASS if the reply names a time.\n"
GOLD = "approved_by: Tester\ncrux: When people travel.\n"
# The reply names the run's workspace and the home folder, which the runner must scrub.
REPLY = "## Report\n\nNotes saved to {workspace}/notes.md and {home}/tides.md.\n"

# The stub engine: it logs what it was given, then writes a result and a trace per run in the shapes
# measured on claude 2.1.330, as each case's mode asks.
STUB = r"""
import json, os, signal, sys, time
from pathlib import Path
argv = sys.argv[1:]
flag = lambda name: argv[argv.index(name) + 1]
target = Path(argv[2])
skill = target.name
out = Path(flag("--output-dir"))
runs = int(flag("--runs"))
evals = target / "evals"
files = {str(p.relative_to(evals)): p.read_text() for p in sorted(evals.rglob("*")) if p.is_file()}
seen = {"argv": argv, "cwd": os.getcwd(), "files": files, "stdin": sys.stdin.read(),
        "env": sorted(k for k in os.environ if k.startswith(("CLAUDE", "ANTHROPIC")))}
with open(os.environ["STUB_LOG"], "a", encoding="utf-8") as log:
    log.write(json.dumps(seen) + "\n")
modes = json.loads(os.environ.get("STUB_MODES", "{}"))
home = os.environ["HOME"]
boxes = Path(os.environ["STUB_SANDBOXES"])
cost = float(os.environ.get("STUB_COST", "0.25"))

def sandbox(case, number, mode):
    box = boxes / f"e-{case}-{number}-{len(list(boxes.iterdir())) if boxes.exists() else 0}"
    (box / "out").mkdir(parents=True)
    workspace = f"{box}/home/cwd"
    start = {"type": "system", "subtype": "init", "model": flag("--model"),
             "claude_code_version": "9.9.9", "permissionMode": "dontAsk", "mcp_servers": [],
             "plugins": [{"name": skill, "path": str(target)}, {"name": "cc-x", "path": "builtin"}],
             "skills": [f"{skill}:{skill}", "simplify"], "cwd": workspace,
             "memory_paths": {"auto": f"{box}/config/projects/x/memory/"},
             "additional_directories": []}
    if mode == "breach":
        start["plugins"].append({"name": "kite-weather", "path": f"{home}/kite-weather"})
    reply = os.environ["STUB_REPLY"].format(workspace=workspace, home=home)
    if mode == "leak":
        reply += "Also " + quote_home + "\n"
    use = lambda i, name, given, parent=None: {"type": "assistant", "parent_tool_use_id": parent,
        "message": {"content": [{"type": "tool_use", "id": i, "name": name, "input": given}]}}
    events = [start,
        use("t1", "Skill", {"skill": f"{skill}:{skill}"}),
        use("t2", "Read", {"file_path": f"{target}/skills/{skill}/references/tables.md"}),
        use("t3", "Agent", {"subagent_type": "general-purpose", "prompt": "fetch"}),
        use("t4", "WebFetch", {"url": "https://example.com/tides", "prompt": "times"}, "t3"),
        use("t5", "Read", {"file_path": "/elsewhere/gold.md"}),
        {"type": "system", "subtype": "permission_denied", "tool_use_id": "t5"},
        {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "t6",
            "is_error": True, "content": "No such page"}]}},
        use("t6", "WebFetch", {"url": "https://example.com/gone"}),
        {"type": "result", "subtype": "error_max_turns" if mode == "turncap" else "success",
         "result": "" if mode == "turncap" else reply}]
    (box / "out" / "trace.jsonl").write_text("".join(json.dumps(e) + "\n" for e in events))
    sealed = box / "sealed"
    sealed.mkdir()
    sealed.chmod(0)
    box.chmod(0o500)
    return f"{box}/out/trace.jsonl" if mode != "notrace" else f"{box}/gone/trace.jsonl", workspace

quote_home = os.environ.get("STUB_QUOTED_HOME", "")

def one(case, number, mode):
    trace, workspace = sandbox(case, number, mode)
    passed = mode not in ("low", "turncap")
    graders = [
        {"name": "crux", "passed": passed, "weight": 1, "scored": True, "withOnly": False,
         "explanation": "judge votes: " + ("PASS " * 3 if passed else "FAIL " * 3).strip(),
         "judgeVotes": [passed] * 3, "evidence": "the reply"},
        {"name": "said", "passed": passed, "weight": 1, "scored": True, "withOnly": False,
         "explanation": f"matched in {workspace}/notes.md"}]
    result = {"score": 1 if passed else 0, "passed": passed, "turns": 3, "costUsd": cost,
              "judgeCostUsd": 0.01, "durationSeconds": 12, "startedAt": "2026-11-25T10:00:00.123Z",
              "error": None, "tracePath": trace, "skippedPaidGraders": mode == "skipped",
              "graders": graders}
    if mode == "turncap":
        result["error"] = "exit 1: Reached maximum number of turns (1)"
    if mode == "api":
        result.update(score=0, graders=[], error="API Error: 529 overloaded")
    if mode == "aborted":
        result["aborted"] = {"server": "notes", "tool": "find", "reason": "budget"}
    return result

def write(cases, partial=None):
    data = {"schemaVersion": 2 if "schema" in modes.values() else 1, "claudeVersion": "9.9.9",
            "costUsd": cost, "partial": partial is not None, "cases": cases}
    if partial:
        data["partialReason"] = partial
    out.mkdir(parents=True, exist_ok=True)
    (out / "aggregate-result.json").write_text(json.dumps(data))

names = sorted(p.name for p in evals.iterdir())
if "nostart" in modes.values():
    sys.exit(1)
if "hang" in modes.values():
    def stop(*_):
        write([{"name": names[0], "graders": [{"name": "crux", "type": "llm"}],
                "arms": {"with": [one(names[0], 1, "ok")]}}], "terminated")
        sys.exit(143)
    signal.signal(signal.SIGTERM, stop)
    time.sleep(60)
cases, code = [], 0
for name in names:
    mode = modes.get(name, "ok")
    if mode == "loadfail":
        sys.stderr.write(f"x {evals}/{name}: prompt.md: unknown frontmatter key\n")
        code = 1
        continue
    count = 1 if mode == "partial" else runs
    cases.append({"name": name, "graders": [{"name": "crux", "type": "llm"},
                  {"name": "said", "type": "regex"}],
                  "arms": {"with": [one(name, n, mode) for n in range(1, count + 1)]}})
    code = 1 if mode == "api" else code
if "extra" in modes.values():
    cases.append({"name": "gale", "graders": [], "arms": {"with": []}})
partial = "cost_ceiling" if "partial" in modes.values() else None
write(cases, partial)
sys.exit(2 if partial else code)
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
    # A fictional repository: the plugin, two cases with their graders and gold, all committed.
    repo = tmp_path / "repo"
    plugin = repo / "plugins" / SKILL
    _write(plugin / ".claude-plugin" / "plugin.json", f'{{"name": "{SKILL}", "version": "0.3.0"}}')
    _write(plugin / "skills" / SKILL / "SKILL.md", f"---\nname: {SKILL}\n---\n")
    for case in ("ferry", "harbour"):
        folder = repo / "evals" / SKILL / "cases" / case
        _write(folder / "prompt.md", PROMPT)
        _write(folder / "graders" / "crux.md", GRADER)
        _write(folder / "gold.md", GOLD)
    _git(repo, "init", "-q", "-b", "main")
    _git(repo, "add", ".")
    _git(repo, "commit", "-q", "-m", "fixture")
    stub = tmp_path / "stub.py"
    stub.write_text(STUB, encoding="utf-8")
    home = tmp_path / "home" / "kestrel-keeper"
    home.mkdir(parents=True)
    monkeypatch.setattr(run, "ROOT", repo)
    monkeypatch.setattr(run, "CLAUDE", [sys.executable, str(stub)])
    monkeypatch.setattr(run, "SKILLS", {SKILL: ("WebSearch", "WebFetch"), "plain": ()})
    monkeypatch.setenv("HOME", str(home))
    monkeypatch.setenv("STUB_LOG", str(tmp_path / "stub.log"))
    monkeypatch.setenv("STUB_SANDBOXES", str(tmp_path / "sandboxes"))
    monkeypatch.setenv("STUB_REPLY", REPLY)
    monkeypatch.delenv("STUB_MODES", raising=False)
    # A launching Claude Code session's variables, which must not reach the engine.
    monkeypatch.setenv("CLAUDECODE", "1")
    monkeypatch.setenv("CLAUDE_EFFORT", "high")
    monkeypatch.setenv("ANTHROPIC_MODEL", "some-other-model")
    return repo


def _log(root: Path) -> list[dict]:
    path = root.parent / "stub.log"
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def _results(root: Path) -> Path:
    return root / "evals" / SKILL / "results"


def _main(*args: str) -> int:
    return run.main([SKILL, "--max-cost-usd", "5", *args])


def _modes(monkeypatch: pytest.MonkeyPatch, **modes: str) -> None:
    monkeypatch.setenv("STUB_MODES", json.dumps(modes))


def _flag(argv: list[str], name: str) -> str:
    return argv[argv.index(name) + 1]


def test_each_run_is_written_with_its_header_calls_reply_and_verdicts(root: Path) -> None:
    assert _main("--runs", "2") == 0
    head = _git(root, "rev-parse", "HEAD").strip()
    for case in ("ferry", "harbour"):
        for number in (1, 2):
            written = shared.read_run(
                (_results(root) / case / f"run-{number}.md").read_text(encoding="utf-8")
            )
            assert written.header == {
                "case": case,
                "run": str(number),
                "model": run.MODEL,
                "claude": "9.9.9",
                "skill_version": "0.3.0",
                "commit": head,
                "date": "2026-11-25T10:00:00Z",
                "cost_usd": "0.2500",
                "duration_s": "12",
                "turns": "3",
                "error": "none",
            }
            assert [call.line() for call in written.calls] == [
                f"- Skill: {SKILL}:{SKILL}",
                f"- Read: <plugin>/skills/{SKILL}/references/tables.md",
                "- Agent: general-purpose",
                "- WebFetch (in general-purpose): https://example.com/tides",
                "- Read (denied): /elsewhere/gold.md",
                "- WebFetch (error): https://example.com/gone",
            ]
            assert written.reply == (
                "## Report\n\nNotes saved to <workspace>/notes.md and ~/tides.md.\n"
            )
            header, verdicts = shared.read_verdicts(
                (_results(root) / case / f"verdicts-{number}.md").read_text(encoding="utf-8")
            )
            assert header == {
                "case": case,
                "run": str(number),
                "score": "1",
                "judge_model": run.JUDGE_MODEL,
                "judge_cost_usd": "0.0100",
            }
            assert [(v.name, v.type, v.passed, v.votes) for v in verdicts] == [
                ("crux", "llm", True, "pass pass pass"),
                ("said", "regex", True, "none"),
            ]
            assert verdicts[1].explanation == "matched in <workspace>/notes.md"
    assert len(_log(root)) == 1


def test_the_engine_gets_every_fixed_flag_in_a_clean_environment(root: Path) -> None:
    assert _main("--runs", "2") == 0
    [entry] = _log(root)
    argv = entry["argv"]
    assert argv[:2] == ["plugin", "eval"]
    target = Path(argv[2])
    assert target.name == SKILL
    assert root.resolve() not in target.resolve().parents
    assert _flag(argv, "--model") == run.MODEL
    assert _flag(argv, "--judge-model") == run.JUDGE_MODEL
    assert _flag(argv, "--ablation") == "none"
    assert _flag(argv, "--threshold") == "0"
    assert _flag(argv, "--concurrency") == "4"
    assert _flag(argv, "--runs") == "2"
    assert _flag(argv, "--max-cost-usd") == "5.00"
    assert {"--no-publish", "--trust-plugin", "--keep-temp"} <= set(argv)
    output = Path(_flag(argv, "--output-dir")).resolve()
    assert root.resolve() not in output.parents
    assert target.resolve() not in output.parents
    # --allow-tools takes a list, so it comes last.
    assert argv[-3:] == ["--allow-tools", "WebSearch", "WebFetch"]
    assert entry["stdin"] == ""
    assert entry["env"] == []
    # The temporary folder is gone once the call ends.
    assert not target.exists()


def test_a_skill_that_needs_no_tools_is_granted_none(
    root: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(run, "SKILLS", {SKILL: ()})
    assert _main("--runs", "1") == 0
    assert "--allow-tools" not in _log(root)[0]["argv"]


def test_gold_md_is_never_opened_or_given_to_the_engine(root: Path, tmp_path: Path) -> None:
    global _OPENED
    golds = list((root / "evals" / SKILL / "cases").glob("*/gold.md"))
    for gold in golds:
        gold.chmod(0)
    _OPENED = []
    try:
        # A trial, since git reports a case folder holding an unreadable file as changed.
        assert _main("--runs", "1", "--trial", str(tmp_path / "trial")) == 0
        opened = _OPENED
    finally:
        _OPENED = None
        for gold in golds:
            gold.chmod(0o644)
    assert not [path for path in opened if Path(path).name == "gold.md"]
    # The engine got each case's prompt and graders byte for byte, and no gold.md.
    assert _log(root)[0]["files"] == {
        "ferry/graders/crux.md": GRADER,
        "ferry/prompt.md": PROMPT,
        "harbour/graders/crux.md": GRADER,
        "harbour/prompt.md": PROMPT,
    }


def test_the_engines_kept_folders_are_removed(root: Path) -> None:
    assert _main("--runs", "2") == 0
    assert list((root.parent / "sandboxes").iterdir()) == []


@pytest.mark.parametrize(
    "change",
    [
        lambda repo: (repo / "plugins" / SKILL / "skills" / SKILL / "SKILL.md").write_text("x\n"),
        lambda repo: (
            repo / "evals" / SKILL / "cases" / "ferry" / "graders" / "crux.md"
        ).write_text("changed\n"),
        lambda repo: _write(repo / "evals" / SKILL / "cases" / "ferry" / "graders" / "new.md", "x"),
    ],
    ids=["plugin", "grader", "untracked grader"],
)
def test_uncommitted_changes_refuse_before_any_run(
    root: Path, change, capsys: pytest.CaptureFixture[str]
) -> None:
    change(root)
    assert _main("--runs", "1") == 2
    assert _log(root) == []
    assert "uncommitted changes" in capsys.readouterr().out


def test_a_trial_runs_on_uncommitted_cases_and_writes_only_to_its_folder(
    root: Path, tmp_path: Path
) -> None:
    _write(root / "evals" / SKILL / "cases" / "ferry" / "graders" / "new.md", "x")
    trial = tmp_path / "trial"
    assert _main("--runs", "1", "--trial", str(trial)) == 0
    assert sorted(p.relative_to(trial).as_posix() for p in trial.rglob("*.md")) == [
        "ferry/run-1.md",
        "ferry/verdicts-1.md",
        "harbour/run-1.md",
        "harbour/verdicts-1.md",
    ]
    assert not _results(root).exists()


def test_a_trial_still_refuses_plugin_changes(root: Path, tmp_path: Path) -> None:
    (root / "plugins" / SKILL / "skills" / SKILL / "SKILL.md").write_text("x\n")
    assert _main("--runs", "1", "--trial", str(tmp_path / "trial")) == 2


def test_a_trial_inside_the_repository_is_refused(
    root: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    assert _main("--runs", "1", "--trial", str(root / "scratch")) == 2
    assert "inside the repository" in capsys.readouterr().out
    assert _log(root) == []


@pytest.mark.parametrize("mode", ["low", "turncap"])
def test_a_graded_run_is_written_whatever_its_score(
    root: Path, mode: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    _modes(monkeypatch, ferry=mode)
    assert _main("--runs", "1") == 0
    written = shared.read_run((_results(root) / "ferry" / "run-1.md").read_text(encoding="utf-8"))
    _, verdicts = shared.read_verdicts(
        (_results(root) / "ferry" / "verdicts-1.md").read_text(encoding="utf-8")
    )
    assert [v.passed for v in verdicts] == [False, False]
    if mode == "turncap":
        assert written.header["error"] == "exit 1: Reached maximum number of turns (1)"
        assert written.reply == ""
    else:
        assert written.header["error"] == "none"


@pytest.mark.parametrize(
    ("mode", "why"),
    [
        ("api", "not graded: API Error: 529 overloaded"),
        ("aborted", "aborted"),
        ("skipped", "judges were skipped"),
        ("breach", "not isolated: plugin kite-weather loaded"),
        ("leak", "still names the home folder"),
        ("notrace", "trace was not kept"),
    ],
)
def test_a_run_that_failed_is_not_written(
    root: Path,
    mode: str,
    why: str,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    _modes(monkeypatch, ferry=mode)
    monkeypatch.setenv("STUB_QUOTED_HOME", quote(os.environ["HOME"], safe=""))
    assert _main("--runs", "1") == 1
    assert not (_results(root) / "ferry").exists()
    assert (_results(root) / "harbour" / "run-1.md").exists()
    assert why in capsys.readouterr().out


def test_a_case_that_did_not_load_writes_nothing_for_it(
    root: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    _modes(monkeypatch, ferry="loadfail")
    assert _main("--runs", "1") == 1
    assert not (_results(root) / "ferry").exists()
    assert (_results(root) / "harbour" / "run-1.md").exists()
    assert "ferry: did not load" in capsys.readouterr().out


@pytest.mark.parametrize(("mode", "why"), [("schema", "schema 2"), ("extra", "not given: gale")])
def test_a_result_the_runner_cannot_trust_writes_nothing(
    root: Path, mode: str, why: str, monkeypatch: pytest.MonkeyPatch, capsys
) -> None:
    _modes(monkeypatch, ferry=mode)
    assert _main("--runs", "1") == 1
    assert not _results(root).exists()
    assert why in capsys.readouterr().out
    assert list((root.parent / "sandboxes").iterdir()) == []


def test_no_result_from_the_engine_writes_nothing(
    root: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    _modes(monkeypatch, ferry="nostart")
    assert _main("--runs", "1") == 1
    assert not _results(root).exists()
    assert "no result from the engine" in capsys.readouterr().out


def test_a_partial_call_writes_its_clean_runs(
    root: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    _modes(monkeypatch, ferry="partial")
    assert _main("--runs", "2") == 1
    assert sorted(p.name for p in (_results(root) / "ferry").glob("run-*.md")) == ["run-1.md"]
    assert "stopped early: cost_ceiling" in capsys.readouterr().out


def test_a_hung_engine_is_stopped_and_its_partial_result_read(
    root: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(run, "RUN_SECONDS", 0)
    monkeypatch.setattr(run, "GRACE_SECONDS", 1)
    _modes(monkeypatch, ferry="hang")
    assert _main("--runs", "1") == 1
    assert (_results(root) / "ferry" / "run-1.md").exists()
    assert not (_results(root) / "harbour").exists()


def test_an_existing_run_is_skipped_and_only_missing_runs_are_asked_for(root: Path) -> None:
    kept = _results(root) / "ferry" / "run-1.md"
    _write(kept, "an earlier run\n")
    # A verdicts file with no run beside it is left from a stopped call, and is replaced.
    _write(_results(root) / "ferry" / "verdicts-2.md", "orphan\n")
    assert _main("--runs", "2") == 0
    assert kept.read_text(encoding="utf-8") == "an earlier run\n"
    calls = [
        (_flag(e["argv"], "--runs"), sorted({p.split("/")[0] for p in e["files"]}))
        for e in _log(root)
    ]
    assert calls == [("2", ["harbour"]), ("1", ["ferry"])]
    assert shared.read_run((_results(root) / "ferry" / "run-2.md").read_text()).header["run"] == "2"
    assert "orphan" not in (_results(root) / "ferry" / "verdicts-2.md").read_text()


def test_every_run_present_calls_no_engine(root: Path) -> None:
    for case in ("ferry", "harbour"):
        _write(_results(root) / case / "run-1.md", "done\n")
    assert _main("--runs", "1") == 0
    assert _log(root) == []


def test_the_ceiling_is_shared_across_calls(root: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    _write(_results(root) / "ferry" / "run-1.md", "done\n")
    monkeypatch.setenv("STUB_COST", "3")
    assert run.main([SKILL, "--max-cost-usd", "4", "--runs", "2"]) == 0
    assert [_flag(e["argv"], "--max-cost-usd") for e in _log(root)] == ["4.00", "1.00"]


def test_a_spent_ceiling_runs_no_further_call(
    root: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    _write(_results(root) / "ferry" / "run-1.md", "done\n")
    monkeypatch.setenv("STUB_COST", "3")
    assert run.main([SKILL, "--max-cost-usd", "3", "--runs", "2"]) == 1
    assert len(_log(root)) == 1
    assert not (_results(root) / "ferry" / "run-2.md").exists()
    assert "the ceiling is spent; not run: ferry" in capsys.readouterr().out


def test_case_chooses_the_cases(root: Path) -> None:
    assert _main("--runs", "1", "--case", "harbour") == 0
    assert sorted(p.name for p in _results(root).iterdir()) == ["harbour"]


@pytest.mark.parametrize(
    ("args", "change", "message"),
    [
        (["gale-watch"], None, "unknown skill gale-watch"),
        ([SKILL, "--case", "gale"], None, "unknown case(s) gale"),
        (
            [SKILL],
            lambda repo: (repo / "evals" / SKILL / "cases" / "ferry" / "prompt.md").unlink(),
            "no prompt.md in ferry",
        ),
        (["plain"], None, "no plugin"),
        (
            [SKILL],
            lambda repo: (repo / "plugins" / SKILL / ".claude-plugin" / "plugin.json").write_text(
                '{"name": "tidewatch"}'
            ),
            "plugin.json: no version",
        ),
    ],
)
def test_a_bad_request_refuses_before_any_run(
    root: Path, args: list[str], change, message: str, capsys: pytest.CaptureFixture[str]
) -> None:
    if change:
        change(root)
        _git(root, "commit", "-q", "-am", "change")
    assert run.main([*args, "--runs", "1", "--max-cost-usd", "1"]) == 2
    assert _log(root) == []
    assert message in capsys.readouterr().out


def test_no_cases_refuses(root: Path) -> None:
    _git(root, "rm", "-rq", f"evals/{SKILL}/cases")
    _git(root, "commit", "-qm", "no cases")
    assert _main("--runs", "1") == 2


@pytest.mark.parametrize("bad", [["--runs", "0"], ["--runs", "1", "--max-cost-usd", "0"]])
def test_runs_and_the_ceiling_must_be_more_than_zero(bad: list[str]) -> None:
    with pytest.raises(SystemExit):
        run.main([SKILL, "--max-cost-usd", "1", *bad])


def test_isolation_breaches_reads_the_whole_start_event(tmp_path: Path) -> None:
    plugin, box = tmp_path / "plugin" / SKILL, tmp_path / "e-box"
    start = {
        "model": run.MODEL,
        "plugins": [{"name": SKILL, "path": str(plugin)}, {"name": "cc-x", "path": "builtin"}],
        "skills": [f"{SKILL}:{SKILL}", "simplify"],
        "mcp_servers": [],
        "permissionMode": "dontAsk",
        "memory_paths": {"auto": str(box / "config" / "memory")},
        "additional_directories": [],
    }
    assert run.isolation_breaches(start, plugin, SKILL, box) == []
    leaky = {
        **start,
        "model": "some-other-model",
        "skills": ["simplify", "anthropic-skills:tidewatch", SKILL],
        "plugins": [],
        "mcp_servers": [{"name": "notes"}],
        "permissionMode": "auto",
        "memory_paths": {"auto": "/elsewhere/memory"},
        "additional_directories": ["/elsewhere"],
    }
    assert run.isolation_breaches(leaky, plugin, SKILL, box) == [
        f"the model is some-other-model, not {run.MODEL}",
        "the plugin under test did not load",
        f"{SKILL}:{SKILL} is not among the skills",
        "skill anthropic-skills:tidewatch loaded",
        f"skill {SKILL} loaded",
        "MCP server notes loaded",
        "the permission mode is auto",
        "memory at /elsewhere/memory",
        "folder /elsewhere opened",
    ]


def test_the_scrubber_replaces_longest_first_and_finds_what_it_missed(tmp_path: Path) -> None:
    home = tmp_path / "home" / "kestrel-keeper"
    plugin = tmp_path / "copy" / "plugin" / SKILL
    scrub = run.Scrubber([(plugin, "<plugin>"), (tmp_path, "<temp>"), (home, "~")], home)
    assert scrub(f"{plugin}/SKILL.md {home}/x {tmp_path}/out") == "<plugin>/SKILL.md ~/x <temp>/out"
    text = str(home)
    for form in (text.replace("/", "-"), quote(text, safe=""), text.replace("/", "\\/")):
        assert scrub.leftover(f"a {form} b") == "the home folder"
    assert scrub.leftover("/private/var/folders/xy/T/run") == "a temporary folder"
    assert scrub.leftover("all clean") is None


def test_a_removed_kept_folder_can_be_sealed(tmp_path: Path) -> None:
    box = tmp_path / "e-box"
    (box / "sealed" / "home").mkdir(parents=True)
    (box / "sealed").chmod(0)
    box.chmod(stat.S_IRUSR | stat.S_IXUSR)
    run._remove(box)
    assert not box.exists()


@pytest.mark.parametrize(
    "trace",
    ["/somewhere/out/trace.jsonl", "/tmp/e-ab12cd/gone/trace.jsonl", None],
)
def test_only_a_folder_named_as_the_engine_names_it_is_taken_for_a_kept_one(trace) -> None:
    assert run._sandbox({"tracePath": trace}) is None


def test_a_kept_folder_is_found_from_its_trace() -> None:
    assert run._sandbox({"tracePath": "/tmp/e-ab12cd/out/trace.jsonl"}) == Path("/tmp/e-ab12cd")
