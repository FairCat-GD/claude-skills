import importlib.util
import os
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path

import pytest

import shared

SOURCE = Path(__file__).resolve().parent.parent / "evals" / "crux-finder" / "checks.py"
_spec = importlib.util.spec_from_file_location("crux_finder_checks", SOURCE)
assert _spec is not None and _spec.loader is not None
checks = importlib.util.module_from_spec(_spec)
sys.modules["crux_finder_checks"] = checks
_spec.loader.exec_module(checks)

EVALS = checks.EVALS
# Typographic marks, written as escapes so the file reads plainly.
LEFT, RIGHT, APOSTROPHE = "\u201c", "\u201d", "\u2019"
# A fictional dispute over a ferry timetable.
INPUT = (
    "A: The last ferry should leave at ten, because almost nobody travels after nine.\n\n"
    "B: The last ferry should leave at eleven; the cannery's late shift ends at half past ten.\n"
)
PROMPT = "---\nallowed_tools: [Skill, Read]\nmax_turns: 20\n---\n\n" + INPUT
GOLD = (
    "---\ncrux: Whether people travel after nine.\ntype: Empirical\ncrux_for: both\n"
    "approved_by: Tester\n---\n"
)
GRADER = "---\ntype: llm\n---\n\nPASS if the reply names the last ferry.\n"


def _steelman(count: int) -> str:
    return " ".join(["ferry"] * count)


def reply(
    a: int = 40, b: int = 40, crux: str = "Whether people travel late.", more: str = ""
) -> str:
    # A report in the template's shape: 40/40 steelmen and 166 words in all.
    return (
        "## Crux report\n\n"
        f"**A, strongest form:** {_steelman(a)}\n"
        f"**B, strongest form:** {_steelman(b)}\n\n"
        "### Common ground\n- Both want the ferry to run.\n\n"
        "### The crux\n**Double crux · Empirical**\n"
        f"> {crux}\n\n"
        "- A holds: few travel after nine.\n- B holds: a shift ends at half past ten.\n"
        "- If A accepted B's view here: A would move the last ferry; "
        "if B accepted A's: B would too.\n"
        "- What would move it: a count of passengers after nine.\n\n"
        "### Secondary cruxes\nNone.\n\n"
        "### Not actually in dispute\nNone.\n\n"
        f"### Confidence\nMedium, because both sides give one reason each.\n{more}"
    )


QUESTION = "Could you share B's own words, or the conversation itself?\n"


def _git(repo: Path, *args: str) -> str:
    env = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}
    identity = ["-c", "user.name=Test", "-c", "user.email=test@example.invalid"]
    return subprocess.run(
        ["git", *identity, *args], cwd=repo, env=env, check=True, capture_output=True, text=True
    ).stdout


def _write(root: Path, path: str, text: str) -> None:
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def _commit(root: Path, *paths: str) -> str:
    _git(root, "add", "-A", *(paths or ["."]))
    _git(root, "commit", "-q", "--allow-empty", "-m", "change")
    return _git(root, "rev-parse", "HEAD").strip()


@pytest.fixture
def root(tmp_path: Path) -> Path:
    # A fictional repository holding the skill folder, committed.
    _git(tmp_path, "init", "-q", "-b", "main")
    _write(tmp_path, f"{checks.SKILL_FOLDER}/SKILL.md", "---\nname: crux-finder\n---\n")
    _commit(tmp_path)
    return tmp_path


def graders_of(case: str) -> list[str]:
    """The three every case has; case-00 is the one-sided case and case-01 the no-conflict."""
    names = [checks.CRUX, checks.TYPE, checks.PEOPLE]
    if case == "case-00":
        names.append(checks.GATE)
    if case == "case-01":
        names.append(checks.NO_CONFLICT)
    return names


def _case(
    root: Path,
    case: str,
    gold: str | None = GOLD,
    prompt: str = PROMPT,
    graders: list[str] | None = None,
) -> None:
    _write(root, f"{EVALS}/cases/{case}/prompt.md", prompt)
    if gold is not None:
        _write(root, f"{EVALS}/cases/{case}/gold.md", gold)
    for name in graders_of(case) if graders is None else graders:
        _write(root, f"{EVALS}/cases/{case}/graders/{name}.md", GRADER)


def _run(
    root: Path,
    case: str,
    number: int,
    body: str,
    commit: str | None,
    verdicts: dict[str, bool] | None = None,
    header: dict[str, str] | None = None,
) -> None:
    """run-N.md and verdicts-N.md, as the shared runner writes them."""
    found = {name: True for name in graders_of(case)} if verdicts is None else verdicts
    values = {"case": case, "run": str(number), "model": "claude-opus-5-5", "commit": commit}
    values = {k: v for k, v in (values | {"error": "none"} | (header or {})).items() if v}
    calls = [shared.Call("Skill", "crux-finder:crux-finder")]
    _write(root, f"{EVALS}/results/{case}/run-{number}.md", shared.format_run(values, calls, body))
    judged = [
        shared.Verdict(name, "llm", passed, True, "1", "pass pass pass", "votes")
        for name, passed in found.items()
    ]
    top = {"case": case, "run": str(number), "score": "1", "judge_model": "claude-sonnet-5-5"}
    _write(
        root, f"{EVALS}/results/{case}/verdicts-{number}.md", shared.format_verdicts(top, judged)
    )


def _claude_ai(root: Path, case: str, body: str, commit: str | None = None) -> None:
    header = "" if commit is None else f"---\ncase: {case}\ncommit: {commit}\n---\n\n"
    _write(root, f"{EVALS}/results/{case}/claude-ai.md", header + body)


Lines = dict[str, str]
CLAUDE_AI_GOOD = {"crux_match": "yes", "type_match": "yes", "people_statement": "no", "note": "ok"}


def _review(root: Path, case: str, sections: dict[str, Lines]) -> None:
    text = f"# Review: {case}\n\n" + "\n".join(
        f"## {name}\n" + "".join(f"- {k}: {v}\n" for k, v in lines.items())
        for name, lines in sections.items()
    )
    _write(root, f"{EVALS}/results/{case}/review.md", text)


def run_lines(number: int, verdicts: dict[str, bool]) -> Lines | None:
    """The owner's section for a run: stability from run 2 on, each failed verdict confirmed."""
    lines = {checks.STABILITY: "yes"} if number > 1 else {}
    lines |= {grader: "fail" for grader, passed in verdicts.items() if not passed}
    return {**lines, "note": "Read."} if lines else None


Judge = Callable[[str, int, str], bool]
Owner = Callable[[str, int, Lines | None], Lines | None]


def everything_passes(case: str, number: int, grader: str) -> bool:
    return True


def cycle(
    root: Path,
    cases: int = 10,
    judge: Judge = everything_passes,
    owner: Owner | None = None,
    body: str | None = None,
) -> str:
    """A whole fictional cycle: the cases committed, then two runs each, their verdicts as the
    judge gives them, and the owner's review."""
    ids = [f"case-{i:02}" for i in range(cases)]
    for case in ids:
        _case(root, case)
    commit = _commit(root)
    for case in ids:
        sections = {}
        for number in (1, 2):
            verdicts = {grader: judge(case, number, grader) for grader in graders_of(case)}
            _run(root, case, number, body or reply(), commit, verdicts)
            lines = run_lines(number, verdicts)
            if owner:
                lines = owner(case, number, lines)
            if lines:
                sections[f"run-{number}"] = lines
        _review(root, case, sections)
    return commit


def _one(root: Path, body: str | None = None, verdicts: dict[str, bool] | None = None) -> str:
    # One case, committed, with one run on that commit.
    _case(root, "ferry")
    commit = _commit(root)
    found = {g: True for g in graders_of("ferry")} if verdicts is None else verdicts
    _run(root, "ferry", 1, reply() if body is None else body, commit, found)
    return commit


def _problems(root: Path, text: str = "") -> list[str]:
    return [problem for problem in checks.check(root).problems if text in problem]


def _row(root: Path, check: str):
    return next(row for row in checks.check(root).rows if row.check.startswith(check))


# --- words, length and symmetry -------------------------------------------------------------


def test_a_word_has_a_letter_or_digit_so_markup_alone_is_none() -> None:
    assert checks.words("## Crux report") == 2
    assert checks.words("**A, strongest form:** · - > — [inferred] A1") == 5


def test_the_template_report_is_counted_as_its_words() -> None:
    assert checks.report_words(reply()) == 166


@pytest.mark.parametrize(("extra", "fits"), [(234, True), (235, False)])
def test_a_report_of_400_words_fits_and_401_does_not(extra: int, fits: bool) -> None:
    body = reply(more=_steelman(extra))
    assert (checks.report_words(body) <= checks.LENGTH) is fits
    assert checks.report_words(body) == 166 + extra


def test_the_claim_map_is_left_out_and_text_after_confidence_counts() -> None:
    claim_map = "\n### Claim map\n- **A1** (stated · conclusion) " + _steelman(500) + "\n"
    assert checks.report_words(reply(more=claim_map)) == 166
    assert checks.report_words(reply(more="In short, " + _steelman(8))) == 176


@pytest.mark.parametrize(
    ("a", "b", "ok"), [(40, 50, True), (50, 40, True), (40, 51, False), (53, 69, False)]
)
def test_the_longer_steelman_is_at_most_a_quarter_longer(a: int, b: int, ok: bool) -> None:
    assert (checks.symmetry_problem(reply(a, b)) is None) is ok


def test_steelmen_with_names_or_reconstructed_by_a_are_read() -> None:
    body = reply().replace("**A, ", "**A (the harbour master), ")
    body = body.replace("**B, ", "**B (reconstructed by A), ")
    assert checks.steelmen(body) == {"A": 40, "B": 40}


def test_a_steelman_runs_on_over_its_next_lines() -> None:
    body = reply(40, 30).replace("**B, strongest form:** ", "**B, strongest form:** one two\n")
    assert checks.steelmen(body) == {"A": 40, "B": 32}


def test_a_missing_steelman_fails() -> None:
    body = reply().replace("**B, strongest form:**", "**B:**")
    assert checks.symmetry_problem(body) == "no steelman for B"


# --- quotes ----------------------------------------------------------------------------------


def _quotes(body: str) -> tuple[list[str], int]:
    spans, unpaired = checks.quoted_spans(body)
    return [span for span in spans if not checks.found_verbatim(span, INPUT)], unpaired


@pytest.mark.parametrize(
    "line",
    [
        'A says "almost nobody travels after nine".',
        f"A says {LEFT}almost nobody\ntravels after nine.{RIGHT}",
        f"B cites {LEFT}the cannery{APOSTROPHE}s late shift{RIGHT}.",
        f"A: {LEFT}The last ferry … after nine.{RIGHT}",
        'A: "The last ferry ... after nine"',
        "B calls it 'the night run', which is not in the input: single quotes are no span.",
    ],
)
def test_a_quote_found_in_the_input_passes(line: str) -> None:
    assert _quotes(reply(more=line + "\n")) == ([], 0)


@pytest.mark.parametrize(
    "line",
    [
        'A says "hardly anyone travels after nine".',
        'A: "after nine ... should leave at ten"',
        "> almost nobody travels after nine, and the boats run empty",
    ],
)
def test_a_quote_not_in_the_input_fails(line: str) -> None:
    missing, _ = _quotes(reply(more="\n" + line + "\n"))
    assert len(missing) == 1


def test_the_crux_sentence_is_the_skills_own_words_but_another_blockquote_quotes() -> None:
    assert _quotes(reply(crux="Whether the late shift needs the ferry.")) == ([], 0)
    assert _quotes(reply(more="\n> almost nobody travels after nine\n")) == ([], 0)


def test_a_quote_inside_the_crux_sentence_is_checked() -> None:
    missing, _ = _quotes(reply(crux='Whether "everyone" travels late.'))
    assert missing == ["everyone"]


def test_a_quotation_mark_without_its_partner_fails() -> None:
    assert _quotes(reply(more='A says "almost nobody travels.\n')) == ([], 1)


def test_a_blank_line_between_the_crux_label_and_its_sentence_keeps_it_exempt() -> None:
    body = reply().replace("**Double crux · Empirical**\n>", "**Double crux · Empirical**\n\n>")
    assert _quotes(body) == ([], 0)


# --- a run, through check() ------------------------------------------------------------------


def test_a_run_that_holds_has_no_problems(root: Path) -> None:
    _one(root, reply(more='A: "almost nobody travels after nine"\n'))
    report = checks.check(root)
    assert report.problems == []
    assert report.runs == 1


@pytest.mark.parametrize(
    ("body", "problem"),
    [
        (reply(more='"invented words"\n'), 'quote not in prompt.md: "invented words"'),
        # The frontmatter is the engine's, not the prompt: a quote of it is not in the prompt.
        (reply(more='"allowed_tools: [Skill, Read]"\n'), "quote not in prompt.md"),
        (reply(more='A says "almost\n'), "a quotation mark without its partner"),
        (reply(53, 69), "steelmen of 53 and 69 words: one is over 1.25 times the other"),
        (reply(more=_steelman(235)), "401 words; a report is at most 400"),
    ],
)
def test_a_run_that_breaks_a_check_fails_it(root: Path, body: str, problem: str) -> None:
    _one(root, body)
    problems = _problems(root)
    assert len(problems) == 1
    assert problem in problems[0]
    assert problems[0].startswith(f"{EVALS}/results/ferry/run-1.md: ")


def test_a_question_is_not_held_to_symmetry_or_length(root: Path) -> None:
    _one(root, QUESTION)
    assert _problems(root) == []


def test_the_reply_is_read_apart_from_the_header_and_the_calls(root: Path) -> None:
    # A quote-shaped call argument is not the reply's: only the reply is checked.
    commit = _one(root)
    text = (root / EVALS / "results/ferry/run-1.md").read_text(encoding="utf-8")
    text = text.replace("- Skill: crux-finder:crux-finder", '- Read: "invented words"')
    _write(root, f"{EVALS}/results/ferry/run-1.md", text)
    assert _problems(root) == []
    assert commit in text


@pytest.mark.parametrize(
    ("header", "problem"),
    [
        ({"commit": ""}, "run-1.md: no commit in its header; the runner writes one"),
        ({"case": "harbour"}, "run-1.md: its header names case 'harbour', run '1'"),
        ({"run": "2"}, "run-1.md: its header names case 'ferry', run '2'"),
    ],
)
def test_a_runs_header_names_its_commit_and_its_place(
    root: Path, header: dict[str, str], problem: str
) -> None:
    _case(root, "ferry")
    commit = _commit(root)
    _run(root, "ferry", 1, reply(), commit, header=header)
    assert any(p.endswith(problem) for p in _problems(root)), _problems(root)


def test_a_run_that_cannot_be_read_is_a_problem_not_a_crash(root: Path) -> None:
    _one(root)
    _write(root, f"{EVALS}/results/ferry/run-1.md", "---\ncase: ferry\n---\n\nJust text.\n")
    # One problem for one cause: not also its missing commit or its header's fields.
    problems = _problems(root, "run-1.md")
    assert problems == [
        f"{EVALS}/results/ferry/run-1.md: cannot be read (no '## Tool calls' after the header)"
    ]


def test_a_run_with_an_error_is_counted_as_the_engine_graded_it(root: Path) -> None:
    cycle(root)
    commit = _git(root, "rev-parse", "HEAD").strip()
    failed = {g: g == checks.PEOPLE for g in graders_of("case-03")}
    _run(root, "case-03", 2, "", commit, failed, header={"error": "reached max_turns"})
    _review(
        root,
        "case-03",
        {"run-2": {checks.STABILITY: "no", "crux": "fail", "type": "fail", "note": "No reply."}},
    )
    report = checks.check(root)
    assert report.problems == []
    assert (_row(root, "Crux").passed, _row(root, "Type").passed) == (19, 19)


# --- verdicts --------------------------------------------------------------------------------


def test_a_run_without_its_verdicts_or_verdicts_without_a_run_fail(root: Path) -> None:
    _one(root)
    (root / EVALS / "results/ferry/verdicts-1.md").rename(
        root / EVALS / "results/ferry/verdicts-2.md"
    )
    assert _problems(root, "verdicts") == [
        f"{EVALS}/results/ferry/verdicts-1.md: missing; the runner writes it beside run-1.md",
        f"{EVALS}/results/ferry/verdicts-2.md: no run-2.md beside it",
    ]


@pytest.mark.parametrize(
    ("verdicts", "problem"),
    [
        ({"crux": True, "type": True}, "no verdict for no-statement-about-people"),
        (
            {"crux": True, "type": True, checks.PEOPLE: True, "tone": True},
            "a verdict for tone, which is not one of the case's graders",
        ),
    ],
)
def test_each_grader_of_the_case_has_one_verdict(
    root: Path, verdicts: dict[str, bool], problem: str
) -> None:
    _one(root, verdicts=verdicts)
    assert _problems(root, "verdicts-1.md") == [f"{EVALS}/results/ferry/verdicts-1.md: {problem}"]


def test_verdicts_that_cannot_be_read_or_name_another_run_fail(root: Path) -> None:
    _one(root)
    path = f"{EVALS}/results/ferry/verdicts-1.md"
    text = (root / path).read_text(encoding="utf-8")
    _write(root, path, text.replace("run: 1", "run: 3"))
    assert _problems(root, "verdicts-1.md") == [f"{path}: its header names case 'ferry', run '3'"]
    _write(root, path, text.replace("- verdict: pass", "- verdict: maybe", 1))
    assert _problems(root, "verdicts-1.md")[0].startswith(f"{path}: cannot be read (")


# --- the case: prompt, graders, gold ---------------------------------------------------------


@pytest.mark.parametrize(
    ("prompt", "problem"),
    [
        (None, "prompt.md: missing"),
        ("---\nmax_turns: 20\n---\n\n  \n", "prompt.md: no prompt after its frontmatter"),
        ("---\nmax_turns: 20\n", "prompt.md: its frontmatter has no closing ---"),
    ],
)
def test_the_prompt_is_prompt_mds_body(root: Path, prompt: str | None, problem: str) -> None:
    _case(root, "ferry")
    if prompt is None:
        (root / EVALS / "cases/ferry/prompt.md").unlink()
    else:
        _write(root, f"{EVALS}/cases/ferry/prompt.md", prompt)
    _commit(root)
    assert _problems(root) == [f"{EVALS}/cases/ferry/{problem}"]


@pytest.mark.parametrize(
    ("graders", "problem"),
    [
        (["crux", "type"], "graders: no no-statement-about-people.md"),
        ([*graders_of("ferry"), "tone"], "graders/tone.md: a grader no bar reads"),
    ],
)
def test_every_case_has_the_three_graders_and_none_no_bar_reads(
    root: Path, graders: list[str], problem: str
) -> None:
    _case(root, "ferry", graders=graders)
    _commit(root)
    assert _problems(root) == [f"{EVALS}/cases/ferry/{problem}"]


@pytest.mark.parametrize(
    ("gold", "problem"),
    [
        (GOLD.replace("approved_by: Tester\n", ""), "no approved_by"),
        (GOLD.replace("approved_by: Tester", "approved_by:"), "no approved_by"),
        (GOLD.replace("crux_for: both\n", ""), "no crux_for"),
    ],
)
def test_gold_md_names_who_approved_it_and_its_fields(root: Path, gold: str, problem: str) -> None:
    _case(root, "ferry", gold=gold)
    _commit(root)
    assert _problems(root) == [f"{EVALS}/cases/ferry/gold.md: {problem}"]


def test_a_gold_with_source_and_license_lines_is_read(root: Path) -> None:
    _case(
        root,
        "ferry",
        gold=GOLD.replace("---\n\n", "").replace(
            "approved_by: Tester\n", 'approved_by: Tester\nsource: "A: b"\nlicense: public-domain\n'
        ),
    )
    _commit(root)
    assert _problems(root) == []


# --- gold order (invariant 7) ----------------------------------------------------------------


def test_gold_md_not_committed_fails(root: Path) -> None:
    _case(root, "ferry")
    assert _problems(root) == [f"{EVALS}/cases/ferry/gold.md: not committed"]


def test_gold_committed_before_its_results_passes(root: Path) -> None:
    _one(root)
    _commit(root)
    assert _problems(root) == []


@pytest.mark.parametrize("results_first", [True, False])
def test_results_committed_with_or_before_gold_fail(root: Path, results_first: bool) -> None:
    _case(root, "ferry", gold=None)
    commit = _commit(root)
    _run(root, "ferry", 1, reply(), commit)
    if results_first:
        _commit(root)
    _write(root, f"{EVALS}/cases/ferry/gold.md", GOLD)
    added = _commit(root) if not results_first else None
    if results_first:
        _commit(root)
    problems = _problems(root, "gold.md: not committed before")
    assert len(problems) == 1
    assert "run-1.md, verdicts-1.md, added in" in problems[0]
    if added:
        assert added[:12] in problems[0]


def test_gold_changed_after_its_present_results_fails(root: Path) -> None:
    _one(root)
    added = _commit(root)
    _write(root, f"{EVALS}/cases/ferry/gold.md", GOLD.replace("nine", "ten"))
    _commit(root)
    assert f"{EVALS}/cases/ferry/gold.md: changed since run-1.md, verdicts-1.md, added in " + (
        added[:12]
    ) in _problems(root, "gold.md")


def test_gold_changed_after_retired_results_and_before_the_present_ones_passes(
    root: Path,
) -> None:
    # A cycle committed, then retired; the gold changes; a new cycle runs on the new gold.
    _one(root)
    _commit(root)
    for name in ("run-1.md", "verdicts-1.md"):
        (root / EVALS / "results/ferry" / name).unlink()
    _commit(root)
    _write(root, f"{EVALS}/cases/ferry/gold.md", GOLD.replace("nine", "ten"))
    commit = _commit(root)
    _run(root, "ferry", 1, reply(), commit)
    _commit(root)
    assert _problems(root) == []


def test_a_retired_result_never_counts_however_old(root: Path) -> None:
    # A file added before the gold and removed since leaves no mark on the order.
    _write(root, f"{EVALS}/results/ferry/run-1.md", "an early result\n")
    _commit(root)
    (root / EVALS / "results/ferry/run-1.md").unlink()
    _commit(root)
    _one(root)
    _commit(root)
    assert _problems(root) == []


def test_a_committed_result_that_no_commit_adds_is_a_problem(root: Path) -> None:
    _one(root)
    _commit(root)
    added = checks._added_in(root)
    present = [f"{EVALS}/results/ferry/run-1.md"]
    snapshot = checks._snapshots(root)
    tracked = checks._tracked(root)
    problems = checks.gold_order(root, "ferry", [], present, snapshot, {}, tracked)
    assert problems == [
        f"{EVALS}/cases/ferry/gold.md: no commit adds {present[0]}, so its order cannot be checked"
    ]
    assert checks.gold_order(root, "ferry", [], present, snapshot, added, tracked) == []


def test_a_renamed_result_is_logged_as_added_under_its_new_name(root: Path) -> None:
    _one(root)
    _commit(root)
    _git(root, "mv", f"{EVALS}/results/ferry/run-1.md", f"{EVALS}/results/ferry/run-2.md")
    renamed = _commit(root)
    assert checks._added_in(root)[f"{EVALS}/results/ferry/run-2.md"] == renamed


def test_gold_with_uncommitted_changes_while_results_exist_fails(root: Path) -> None:
    _one(root)
    _write(root, f"{EVALS}/cases/ferry/gold.md", GOLD.replace("nine", "ten"))
    problems = _problems(root, "gold.md")
    assert f"{EVALS}/cases/ferry/gold.md: uncommitted changes while results exist" in problems


def test_a_run_on_a_commit_without_gold_fails(root: Path) -> None:
    first = _git(root, "rev-parse", "HEAD").strip()
    _case(root, "ferry")
    _commit(root)
    _run(root, "ferry", 1, reply(), first)
    assert (
        f"{EVALS}/cases/ferry/gold.md: not in commit {first[:12]}, which run-1 ran on"
        in _problems(root, "gold.md")
    )


# --- the case as it ran ----------------------------------------------------------------------


def _graders_path(case: str = "ferry") -> str:
    return f"{EVALS}/cases/{case}/graders"


@pytest.mark.parametrize("commit_it", [False, True])
def test_a_grader_changed_after_a_runs_commit_fails(root: Path, commit_it: bool) -> None:
    commit = _one(root)
    _write(root, f"{_graders_path()}/crux.md", GRADER.replace("ferry", "boat"))
    if commit_it:
        _commit(root)
    assert _problems(root, "graders") == [
        f"{_graders_path()}: changed since commit {commit[:12]}, which run-1 ran on"
    ]


@pytest.mark.parametrize("change", ["added", "removed"])
def test_a_grader_added_or_removed_after_a_runs_commit_fails(root: Path, change: str) -> None:
    commit = _one(root)
    if change == "added":
        _write(root, f"{_graders_path()}/gate.md", GRADER)
    else:
        (root / _graders_path() / "type.md").unlink()
    assert (
        f"{_graders_path()}: graders added or removed since commit {commit[:12]}, "
        "which run-1 ran on"
    ) in _problems(root, "graders")


def test_a_prompt_changed_after_a_runs_commit_fails(root: Path) -> None:
    commit = _one(root)
    _write(root, f"{EVALS}/cases/ferry/prompt.md", PROMPT + "\nOne more line.\n")
    assert _problems(root, "prompt.md") == [
        f"{EVALS}/cases/ferry/prompt.md: changed since commit {commit[:12]}, which run-1 ran on"
    ]


def test_a_run_on_a_commit_without_its_graders_fails(root: Path) -> None:
    _case(root, "ferry", graders=[])
    commit = _commit(root)
    _case(root, "ferry")
    _commit(root)
    _run(root, "ferry", 1, reply(), commit)
    assert _problems(root, "graders") == [
        f"{_graders_path()}: not in commit {commit[:12]}, which run-1 ran on"
    ]


def test_a_grader_newer_than_a_claude_ai_reply_passes(root: Path) -> None:
    # The claude.ai reply ran before any grader existed, so the graders are not held to it.
    _case(root, "ferry", graders=[])
    commit = _commit(root)
    _claude_ai(root, "ferry", reply(), commit)
    _review(root, "ferry", {"claude-ai": CLAUDE_AI_GOOD})
    _commit(root)
    _case(root, "ferry")
    _commit(root)
    assert _problems(root) == []


# --- review.md: the owner's lines ------------------------------------------------------------


def test_a_failed_verdict_needs_the_owners_line(root: Path) -> None:
    _one(root, verdicts={"crux": False, "type": True, checks.PEOPLE: True})
    where = f"{EVALS}/results/ferry/review.md"
    assert _problems(root) == [f"{where}: missing"]
    _review(root, "ferry", {"run-1": {"note": "Read."}})
    assert _problems(root) == [
        f"{where}: run-1's crux failed and has no line: fail confirms it, pass overrules it"
    ]
    _review(root, "ferry", {"run-1": {"crux": "fail", "note": "The crux is another."}})
    assert _problems(root) == []


def test_a_run_with_a_failed_verdict_and_no_section_is_named(root: Path) -> None:
    _one(root, verdicts={"crux": True, "type": False, checks.PEOPLE: True})
    _review(root, "ferry", {})
    assert _problems(root) == [
        f"{EVALS}/results/ferry/review.md: no section for run-1, whose type failed"
    ]


@pytest.mark.parametrize(
    ("line", "counted", "overruled"),
    [
        # The owner overrules a failed verdict: it counts as a pass.
        ("pass", 20, 1),
        # The owner confirms it: it counts as the fail it was.
        ("fail", 19, 0),
    ],
)
def test_the_owners_line_on_a_failed_verdict_is_counted_over_it(
    root: Path, line: str, counted: int, overruled: int
) -> None:
    def judge(case: str, number: int, grader: str) -> bool:
        return (case, number, grader) != ("case-04", 2, "crux")

    def owner(case: str, number: int, lines: Lines | None) -> Lines | None:
        if (case, number) == ("case-04", 2) and lines is not None:
            return {**lines, "crux": line}
        return lines

    cycle(root, judge=judge, owner=owner)
    report = checks.check(root)
    assert report.problems == []
    assert _row(root, "Crux").passed == counted
    assert (report.overruled, report.verdicts) == (overruled, 64)


def test_the_owners_fail_on_a_passed_verdict_is_counted_over_it(root: Path) -> None:
    def owner(case: str, number: int, lines: Lines | None) -> Lines | None:
        if (case, number) == ("case-06", 1):
            return {checks.PEOPLE: "fail", "note": "The report calls A stubborn."}
        return lines

    cycle(root, owner=owner)
    report = checks.check(root)
    assert report.problems == []
    row = _row(root, "No statement about people")
    assert (row.passed, row.met, report.overruled) == (19, False, 1)


@pytest.mark.parametrize(
    ("lines", "problem"),
    [
        ({"note": "Read."}, "run-2 has no same_crux_as_run_1"),
        ({checks.STABILITY: "maybe", "note": "Read."}, "run-2's same_crux_as_run_1 is 'maybe'"),
        ({checks.STABILITY: "yes", "crux": "yes", "note": "x"}, "run-2's crux is 'yes', not pass"),
        ({checks.STABILITY: "yes", "gate": "pass", "note": "x"}, "run-2 has gate, not a field"),
        ({checks.STABILITY: "yes", "crux_match": "yes", "note": "x"}, "run-2 has crux_match"),
        ({checks.STABILITY: "yes"}, "run-2 has no note"),
    ],
)
def test_a_runs_section_holds_stability_its_graders_and_a_note(
    root: Path, lines: Lines, problem: str
) -> None:
    _one(root)
    commit = _git(root, "rev-parse", "HEAD").strip()
    _run(root, "ferry", 2, reply(), commit)
    _review(root, "ferry", {"run-2": lines})
    problems = _problems(root, "review.md")
    assert len(problems) == 1 and problem in problems[0], problems


def test_run_2_needs_a_section_and_run_1_has_no_stability(root: Path) -> None:
    _one(root)
    commit = _git(root, "rev-parse", "HEAD").strip()
    _run(root, "ferry", 2, reply(), commit)
    where = f"{EVALS}/results/ferry/review.md"
    _review(root, "ferry", {"run-1": {checks.STABILITY: "yes", "note": "x"}})
    assert _problems(root, "review.md") == [
        f"{where}: run-1 has same_crux_as_run_1",
        f"{where}: no section for run-2; it needs same_crux_as_run_1",
    ]


def test_review_sections_match_the_outputs_and_keep_their_format(root: Path) -> None:
    _one(root)
    where = f"{EVALS}/results/ferry/review.md"
    _write(
        root,
        where,
        "# Review: ferry\n\n## run-3\n- note: x\n\n## run-1\n- note: x\n- note: y\nloose text\n",
    )
    assert _problems(root, "review.md") == [
        f"{where}:8: note given twice",
        f"{where}:9: not a `- field: value` line in an output's section",
        f"{where}: a section for run-3, which has no output",
    ]


@pytest.mark.parametrize(
    ("body", "lines", "problem"),
    [
        (reply(), {**CLAUDE_AI_GOOD, "crux_match": "maybe"}, "crux_match is 'maybe'"),
        (reply(), {k: v for k, v in CLAUDE_AI_GOOD.items() if k != "note"}, "has no note"),
        (reply(), {**CLAUDE_AI_GOOD, "crux": "pass"}, "has crux, not one of its fields"),
        (QUESTION, CLAUDE_AI_GOOD, "no gate_fired; it is a question, not a report"),
    ],
)
def test_a_claude_ai_section_keeps_round_1s_fields(
    root: Path, body: str, lines: Lines, problem: str
) -> None:
    _case(root, "ferry")
    _commit(root)
    _claude_ai(root, "ferry", body)
    _review(root, "ferry", {"claude-ai": lines})
    problems = _problems(root, "review.md")
    assert len(problems) == 1 and problem in problems[0], problems


def test_every_case_has_every_run_and_results_name_a_case(root: Path) -> None:
    cycle(root, cases=2)
    (root / EVALS / "results/case-01/run-2.md").unlink()
    (root / EVALS / "results/case-01/verdicts-2.md").unlink()
    _write(root, f"{EVALS}/results/stray/run-1.md", "x")
    problems = _problems(root)
    assert f"{EVALS}/results/case-01/run-2.md: missing" in problems
    assert f"{EVALS}/results/stray: results for a case that does not exist" in problems


# --- the pass bars ---------------------------------------------------------------------------


def test_a_whole_cycle_that_holds_meets_every_bar(root: Path) -> None:
    cycle(root)
    report = checks.check(root)
    assert report.problems == []
    assert [(row.passed, row.total, row.met) for row in report.rows] == [
        (20, 20, True),
        (20, 20, True),
        (10, 10, True),
        (20, 20, True),
        (20, 20, True),
        (20, 20, True),
        (20, 20, True),
        (2, 2, True),
        (2, 2, True),
        (10, 10, True),
        (20, 20, True),
    ]
    assert [row.bar for row in report.rows[:3]] == [
        "≥ 16 / 20 runs",
        "≥ 18 / 20 runs",
        "≥ 8 / 10 cases",
    ]
    assert report.missed == []
    assert (report.overruled, report.verdicts) == (0, 64)


def _fails(grader: str, *runs: tuple[str, int]) -> Judge:
    def judge(case: str, number: int, name: str) -> bool:
        return not (name == grader and (case, number) in runs)

    return judge


def _both(*cases: str) -> list[tuple[str, int]]:
    return [(case, number) for case in cases for number in (1, 2)]


@pytest.mark.parametrize(
    ("judge", "check", "passed", "met"),
    [
        (_fails("crux", *_both("case-02", "case-03")), "Crux", 16, True),
        (_fails("crux", *_both("case-02", "case-03"), ("case-04", 1)), "Crux", 15, False),
        (_fails("type", *_both("case-05")), "Type", 18, True),
        (_fails("type", *_both("case-05"), ("case-06", 2)), "Type", 17, False),
        (_fails("gate", ("case-00", 2)), "One-sided", 1, False),
        (_fails("no-conflict", ("case-01", 1)), "No-conflict", 1, False),
        (_fails(checks.PEOPLE, ("case-09", 2)), "No statement", 19, False),
    ],
)
def test_a_bar_is_met_at_its_line_and_missed_below_it(
    root: Path, judge: Judge, check: str, passed: int, met: bool
) -> None:
    cycle(root, judge=judge)
    assert _problems(root) == []
    row = _row(root, check)
    assert (row.passed, row.met) == (passed, met)


@pytest.mark.parametrize(("unstable", "passed", "met"), [(2, 8, True), (3, 7, False)])
def test_stability_is_the_owners_record(root: Path, unstable: int, passed: int, met: bool) -> None:
    def owner(case: str, number: int, lines: Lines | None) -> Lines | None:
        if number == 2 and case in [f"case-0{i}" for i in range(2, 2 + unstable)]:
            return {**(lines or {}), checks.STABILITY: "no"}
        return lines

    cycle(root, owner=owner)
    row = _row(root, "Stability")
    assert (row.passed, row.met) == (passed, met)


def test_a_bar_whose_grader_no_case_has_is_not_met(root: Path) -> None:
    cycle(root, cases=1)
    row = _row(root, "No-conflict")
    assert (row.passed, row.total, row.met) == (0, 0, False)


def test_one_long_report_misses_the_length_bar(root: Path) -> None:
    commit = cycle(root)
    _run(root, "case-04", 2, reply(more=_steelman(300)), commit)
    report = checks.check(root)
    row = next(row for row in report.rows if row.check.startswith("Length"))
    assert (row.passed, row.met) == (19, False)
    assert "Length ≤ 400 words" in report.missed


def test_an_unsound_case_misses_its_row(root: Path) -> None:
    cycle(root)
    _write(root, f"{_graders_path('case-07')}/crux.md", GRADER.replace("ferry", "boat"))
    row = _row(root, "Gold order")
    assert (row.passed, row.met) == (9, False)


def test_runs_on_a_skill_changed_since_are_not_on_the_skill_as_it_stands(root: Path) -> None:
    cycle(root)
    assert _row(root, "Runs on the skill").met
    _write(root, f"{checks.SKILL_FOLDER}/SKILL.md", "---\nname: crux-finder\n---\nChanged.\n")
    _commit(root, checks.SKILL_FOLDER)
    row = _row(root, "Runs on the skill")
    assert (row.passed, row.met) == (0, False)


_VERSIONED = '---\nname: crux-finder\nmetadata:\n  version: "0.4.0"\n---\nThe procedure.\n'


def _versioned_cycle(root: Path) -> None:
    # A skill with a version line in SKILL.md and a version-shaped line in a reference.
    _write(root, f"{checks.SKILL_FOLDER}/SKILL.md", _VERSIONED)
    _write(root, f"{checks.SKILL_FOLDER}/references/procedure.md", '  version: "0.4.0"\n')
    _commit(root)
    cycle(root)


def _release(root: Path, skill_md: str | None = None, procedure: str | None = None) -> None:
    if skill_md is not None:
        _write(root, f"{checks.SKILL_FOLDER}/SKILL.md", skill_md)
    if procedure is not None:
        _write(root, f"{checks.SKILL_FOLDER}/references/procedure.md", procedure)
    _commit(root, checks.SKILL_FOLDER)


def test_a_change_to_the_version_line_alone_leaves_the_skill_as_it_stands(root: Path) -> None:
    _versioned_cycle(root)
    _release(root, _VERSIONED.replace("0.4.0", "1.0.0"))
    row = _row(root, "Runs on the skill")
    assert (row.passed, row.met) == (20, True)


def test_the_version_line_with_another_change_is_a_changed_skill(root: Path) -> None:
    _versioned_cycle(root)
    _release(root, _VERSIONED.replace("0.4.0", "1.0.0").replace("procedure", "procedure, changed"))
    row = _row(root, "Runs on the skill")
    assert (row.passed, row.met) == (0, False)


def test_the_version_line_in_any_form_the_skills_stage_reads_is_set_aside(root: Path) -> None:
    _versioned_cycle(root)
    _release(root, _VERSIONED.replace('  version: "0.4.0"', "    version: 1.1.0-rc.1"))
    row = _row(root, "Runs on the skill")
    assert (row.passed, row.met) == (20, True)


def test_a_version_shaped_line_in_skill_md_s_body_is_a_changed_skill(root: Path) -> None:
    _write(root, f"{checks.SKILL_FOLDER}/SKILL.md", _VERSIONED + '  version: "0.4.0"\n')
    _commit(root)
    cycle(root)
    _release(root, _VERSIONED + '  version: "1.0.0"\n')
    row = _row(root, "Runs on the skill")
    assert (row.passed, row.met) == (0, False)


def test_a_version_shaped_line_outside_skill_md_is_a_changed_skill(root: Path) -> None:
    _versioned_cycle(root)
    _release(root, procedure='  version: "1.0.0"\n')
    row = _row(root, "Runs on the skill")
    assert (row.passed, row.met) == (0, False)


# --- the claude.ai replies -------------------------------------------------------------------


def _smoke_cases(root: Path, bodies: list[str]) -> None:
    for index in range(len(bodies)):
        _case(root, f"case-{index:02}")
    _commit(root)
    for index, body in enumerate(bodies):
        case = f"case-{index:02}"
        _claude_ai(root, case, body)
        _review(root, case, {"claude-ai": CLAUDE_AI_GOOD})
    _commit(root)


def test_the_smoke_test_needs_three_of_three(root: Path) -> None:
    _smoke_cases(root, [reply(), reply(), reply()])
    smoke = checks.check(root).smoke
    assert smoke is not None and (smoke.passed, smoke.total, smoke.met) == (3, 3, True)
    _claude_ai(root, "case-02", reply(53, 69))
    smoke = checks.check(root).smoke
    assert smoke is not None and (smoke.passed, smoke.met) == (2, False)


@pytest.mark.parametrize(
    ("text", "header"),
    [
        ("---\ncase: ferry\ncommit: abc\n---\n\n## Crux report\n", "case: ferry\ncommit: abc"),
        ("---\n\n## Crux report\n\nText.\n", None),
        ("---\n\n## Crux report\n\nText.\n\n---\n\nMore.\n", None),
    ],
)
def test_only_a_block_of_fields_is_a_claude_ai_replys_header(text: str, header: str | None) -> None:
    found, body = checks.output_parts(text)
    assert found == header
    assert body == (text if header is None else "\n## Crux report\n")


def test_a_claude_ai_reply_that_opens_with_a_rule_is_still_checked(root: Path) -> None:
    _case(root, "ferry")
    _commit(root)
    _claude_ai(root, "ferry", "---\n\n" + reply(53, 69))
    _review(root, "ferry", {"claude-ai": CLAUDE_AI_GOOD})
    assert _problems(root, "claude-ai.md") == [
        f"{EVALS}/results/ferry/claude-ai.md: steelmen of 53 and 69 words: "
        "one is over 1.25 times the other"
    ]


def test_a_claude_ai_reply_that_cannot_be_read_is_a_problem_not_a_crash(root: Path) -> None:
    _case(root, "ferry")
    _commit(root)
    (root / EVALS / "results" / "ferry" / "claude-ai.md").mkdir(parents=True)
    problems = _problems(root, "claude-ai.md: cannot be read")
    assert len(problems) == 1


# --- the command -----------------------------------------------------------------------------


def _main(root: Path, monkeypatch: pytest.MonkeyPatch, capsys) -> tuple[int, str]:
    monkeypatch.setattr(checks, "ROOT", root)
    code = checks.main()
    return code, capsys.readouterr().out


def test_main_with_no_cases_passes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    assert _main(tmp_path, monkeypatch, capsys) == (
        0,
        "checks: 0 case(s), 0 problem(s); no cases yet\n",
    )


def test_main_with_cases_and_no_results_passes_without_counting_bars(
    root: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    _case(root, "ferry")
    _commit(root)
    code, out = _main(root, monkeypatch, capsys)
    assert code == 0
    assert out == (
        "checks: 1 case(s), 0 problem(s); no results yet, so the pass bars are not counted\n"
    )


def test_main_with_claude_ai_replies_and_no_cycle_passes_on_the_smoke_test(
    root: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    _smoke_cases(root, [reply(), QUESTION, reply()])
    _review(root, "case-01", {"claude-ai": {**CLAUDE_AI_GOOD, "gate_fired": "yes"}})
    code, out = _main(root, monkeypatch, capsys)
    assert code == 0
    assert "| claude.ai smoke test | 3 / 3 cases | 3 / 3 | yes |" in out
    assert "Crux matches gold" not in out
    assert out.endswith(
        "checks: 3 case(s), 0 problem(s); no cycle yet, so the cycle's bars are not counted; "
        "the claude.ai smoke test met\n"
    )


def test_main_prints_the_table_and_fails_on_a_missed_bar(
    root: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    cycle(root, judge=_fails("type", *_both("case-01", "case-02")))
    code, out = _main(root, monkeypatch, capsys)
    assert code == 1
    assert "| Type matches gold | ≥ 18 / 20 runs | 16 / 20 | **no** |" in out
    assert "Verdicts the owner overruled: 0 of 64\n" in out
    assert out.endswith("pass bars not met: Type matches gold\n")


def test_main_fails_on_any_problem(
    root: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    cycle(root)
    _write(root, f"{EVALS}/cases/case-03/gold.md", GOLD.replace("nine", "ten"))
    code, out = _main(root, monkeypatch, capsys)
    assert code == 1
    assert "uncommitted changes while results exist" in out
