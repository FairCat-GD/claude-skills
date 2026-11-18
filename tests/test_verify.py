from pathlib import Path

import pytest

import verify


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
    if "scripts/hygiene.py" in command:
        return "hygiene"
    if "pytest" in command:
        return "tests"
    return "format" if "format" in command else "lint"


def test_a_named_stage_runs_alone(calls: list[list[str]]) -> None:
    assert verify.main(["lint"]) == 0
    assert [_stage_of(command) for command in calls] == ["lint"]


def test_every_stage_runs_in_order_when_none_is_named(calls: list[list[str]]) -> None:
    assert verify.main([]) == 0
    assert [_stage_of(command) for command in calls] == ["format", "lint", "tests", "hygiene"]


def test_a_failing_stage_leaves_the_others_running(
    calls: list[list[str]], monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setitem(verify.STAGES, "lint", lambda _: [["fail"]])
    assert verify.main([]) == 1
    assert [_stage_of(command) for command in calls] == ["format", "lint", "tests", "hygiene"]
    assert capsys.readouterr().out.splitlines()[-1] == "verify: FAIL (lint)"


def test_an_unknown_stage_exits_2(calls: list[list[str]]) -> None:
    assert verify.main(["format", "typecheck"]) == 2
    assert calls == []


@pytest.mark.parametrize("flags", [["--message", "draft"], ["--all"]])
def test_a_hygiene_flag_without_hygiene_exits_2(calls: list[list[str]], flags: list[str]) -> None:
    assert verify.main(["lint", *flags]) == 2
    assert calls == []


def test_the_hygiene_flags_reach_the_stage(calls: list[list[str]], tmp_path: Path) -> None:
    draft = tmp_path / "COMMIT_DRAFT"
    assert verify.main(["--message", str(draft), "hygiene", "--all"]) == 0
    assert calls == [[verify.PYTHON, "scripts/hygiene.py", "--message", str(draft), "--all"]]
