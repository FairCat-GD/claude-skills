import pytest

import shared

HEADER = {"case": "ferry", "run": "1", "model": "claude-opus-5-5", "error": "none"}
CALLS = [
    shared.Call("Skill", "crux-finder:crux-finder"),
    shared.Call("Read", "<plugin>/skills/crux-finder/references/template.md"),
    shared.Call("WebFetch", "https://example.com/tide: tables", "general-purpose"),
    shared.Call("Read", "<repo>/CLAUDE.md", None, "denied"),
    shared.Call("Glob", '{"pattern":"**"}', "web-fetch", "error"),
]


@pytest.mark.parametrize(
    "reply",
    [
        "## Crux report\n\nThe last ferry.\n",
        "no last newline",
        "",
        # A reply that holds the file's own markers is still read back whole.
        "## Reply\n\n## Tool calls\n\n- Read: x\n",
        "---\nkey: value\n---\n\n## Reply\n",
    ],
)
def test_a_run_file_reads_back_as_it_was_written(reply: str) -> None:
    text = shared.format_run(HEADER, CALLS, reply)
    run = shared.read_run(text)
    assert run.header == HEADER
    assert run.calls == CALLS
    assert run.reply == (reply if not reply or reply.endswith("\n") else reply + "\n")


def test_a_run_file_has_its_header_its_calls_then_its_reply() -> None:
    text = shared.format_run(HEADER, CALLS[:1], "Done.")
    assert text == (
        "---\ncase: ferry\nrun: 1\nmodel: claude-opus-5-5\nerror: none\n---\n\n"
        "## Tool calls\n\n- Skill: crux-finder:crux-finder\n\n## Reply\n\nDone.\n"
    )


def test_no_calls_reads_back_as_none() -> None:
    text = shared.format_run(HEADER, [], "Done.\n")
    assert "## Tool calls\n\nnone\n\n## Reply" in text
    assert shared.read_run(text).calls == []


def test_a_call_with_a_line_break_stays_on_one_line() -> None:
    call = shared.Call("Bash", "echo one\necho two")
    text = shared.format_run(HEADER, [call], "Done.\n")
    assert "- Bash: echo one\\necho two\n" in text
    assert shared.read_run(text).calls == [shared.Call("Bash", "echo one\\necho two")]


@pytest.mark.parametrize(
    ("text", "message"),
    [
        ("no header at all\n", "no header"),
        ("---\ncase: x\n---\n\n## Reply\n\nhi\n", "no '## Tool calls'"),
        ("---\ncase: x\n---\n\n## Tool calls\n\n- Read: x\n", "no '## Reply'"),
        ("---\ncase: x\n---\n\n## Tool calls\n\nnot a call\n\n## Reply\n\nhi\n", "not a tool call"),
    ],
)
def test_a_run_file_in_another_shape_is_refused(text: str, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        shared.read_run(text)


def test_a_header_value_with_a_line_break_is_refused() -> None:
    with pytest.raises(ValueError, match="one line"):
        shared.format_run({"case": "a\nb"}, [], "")


VERDICTS = [
    shared.Verdict("crux", "llm", True, True, "1", "pass pass fail", "judge votes: PASS PASS FAIL"),
    shared.Verdict("said-ready", "regex", False, False, "2", "none", "pattern not found\nat all"),
]


def test_verdicts_read_back_as_they_were_written() -> None:
    header = {"case": "ferry", "run": "2", "score": "0.5", "judge_model": "claude-haiku-5-5"}
    text = shared.format_verdicts(header, VERDICTS)
    assert "## crux\n\n- type: llm\n- verdict: pass\n- scored: yes\n" in text
    read_header, verdicts = shared.read_verdicts(text)
    assert read_header == header
    assert verdicts[0] == VERDICTS[0]
    assert verdicts[1].explanation == "pattern not found\\nat all"
    assert (verdicts[1].passed, verdicts[1].scored, verdicts[1].weight) == (False, False, "2")


@pytest.mark.parametrize(
    ("section", "message"),
    [
        ("## crux\n\n- type: llm\n", "no verdict"),
        ("## crux\n\nloose text\n", "not a field"),
        (
            "## crux\n\n- type: llm\n- verdict: maybe\n- scored: yes\n- weight: 1\n- votes: none\n"
            "- explanation: x\n",
            "not one of its values",
        ),
    ],
)
def test_verdicts_in_another_shape_are_refused(section: str, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        shared.read_verdicts(f"---\ncase: ferry\n---\n\n{section}")


def test_fields_reads_one_key_per_line_and_unquotes() -> None:
    assert shared.fields('approved_by: "Tester"\n  nested: no\ntype: Empirical') == {
        "approved_by": "Tester",
        "type": "Empirical",
    }
