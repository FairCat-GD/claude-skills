import re
import subprocess
from pathlib import Path

import pytest

import verify

ALL = ["skills", "plugins", "format", "lint", "tests", "hygiene"]


@pytest.fixture
def calls(monkeypatch: pytest.MonkeyPatch) -> list[list[str]]:
    # Records each command instead of running it; a command naming "fail" fails.
    recorded: list[list[str]] = []

    def call(command: list[str]) -> bool:
        recorded.append(command)
        return "fail" not in command

    monkeypatch.setattr(verify, "_call", call)
    return recorded


def _stage_of(command: list[str]) -> str:
    if "skills-ref" in command or "scripts/check_skills.py" in command:
        return "skills"
    if command[0] == "claude" or "scripts/check_plugins.py" in command:
        return "plugins"
    if "scripts/hygiene.py" in command:
        return "hygiene"
    if "pytest" in command:
        return "tests"
    return "format" if "format" in command else "lint"


def _stages(calls: list[list[str]]) -> list[str]:
    # A stage may run several commands; consecutive ones of one stage count once.
    names = [_stage_of(command) for command in calls]
    return [name for i, name in enumerate(names) if i == 0 or names[i - 1] != name]


def test_a_named_stage_runs_alone(calls: list[list[str]]) -> None:
    assert verify.main(["lint"]) == 0
    assert _stages(calls) == ["lint"]


def test_every_stage_runs_in_order_when_none_is_named(calls: list[list[str]]) -> None:
    assert verify.main([]) == 0
    assert _stages(calls) == ALL


def test_a_failing_stage_leaves_the_others_running(
    calls: list[list[str]], monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setitem(verify.STAGES, "lint", lambda _: [["fail"]])
    assert verify.main([]) == 1
    assert _stages(calls) == ALL
    assert capsys.readouterr().out.splitlines()[-1] == "verify: FAIL (lint)"


def _tree(root: Path, *names: str) -> None:
    for name in names:
        (root / "plugins" / name / "skills" / name).mkdir(parents=True)


def test_the_skills_stage_runs_the_pinned_validator_on_each_skill_folder(
    calls: list[list[str]], monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    _tree(tmp_path, "kite-weather", "tide-tables")
    monkeypatch.setattr(verify, "ROOT", tmp_path)
    assert verify.main(["skills"]) == 0
    validate = ["uvx", "--python", ">=3.11", "--from", verify.VALIDATOR, "skills-ref", "validate"]
    assert calls == [
        [*validate, "plugins/kite-weather/skills/kite-weather"],
        [*validate, "plugins/tide-tables/skills/tide-tables"],
        [verify.PYTHON, "scripts/check_skills.py"],
    ]
    # Pinned to a whole commit, never a branch that moves.
    assert re.fullmatch(r"git\+https://\S+@[0-9a-f]{40}#subdirectory=skills-ref", verify.VALIDATOR)


def test_the_plugins_stage_validates_the_marketplace_and_each_plugin(
    calls: list[list[str]], monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    _tree(tmp_path, "kite-weather", "tide-tables")
    monkeypatch.setattr(verify, "ROOT", tmp_path)
    assert verify.main(["plugins"]) == 0
    validate = ["claude", "plugin", "validate", "--strict"]
    assert calls == [
        [*validate, "."],
        [*validate, "plugins/kite-weather"],
        [*validate, "plugins/tide-tables"],
        [verify.PYTHON, "scripts/check_plugins.py"],
    ]


def test_a_command_runs_with_stdin_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    seen: dict[str, object] = {}

    def run(command: list[str], **options: object) -> subprocess.CompletedProcess[bytes]:
        seen.update(options)
        return subprocess.CompletedProcess(command, 0)

    monkeypatch.setattr(verify.subprocess, "run", run)
    assert verify._call(["probe"])
    assert seen["stdin"] is subprocess.DEVNULL


def test_an_unknown_stage_exits_2(calls: list[list[str]]) -> None:
    assert verify.main(["format", "typecheck"]) == 2
    assert calls == []


@pytest.mark.parametrize("flags", [["--message", "draft"], ["--all"]])
def test_a_hygiene_flag_without_hygiene_exits_2(
    calls: list[list[str]], flags: list[str], capsys: pytest.CaptureFixture[str]
) -> None:
    assert verify.main(["lint", *flags]) == 2
    assert calls == []
    assert capsys.readouterr().out == f"verify: the hygiene stage reads {flags[0]}; name it too\n"


def test_the_hygiene_flags_reach_the_stage(calls: list[list[str]], tmp_path: Path) -> None:
    draft = tmp_path / "COMMIT_DRAFT"
    assert verify.main(["--message", str(draft), "hygiene", "--all"]) == 0
    assert calls == [[verify.PYTHON, "scripts/hygiene.py", "--message", str(draft), "--all"]]
