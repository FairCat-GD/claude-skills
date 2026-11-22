import importlib.util
import os
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path

import pytest

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
GOLD = (
    "---\ncrux: Whether people travel after nine.\ntype: Empirical\ncrux_for: both\n"
    "approved_by: Tester\n---\n"
)


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
    _git(root, "add", *(paths or ["."]))
    _git(root, "commit", "-q", "--allow-empty", "-m", "change")
    return _git(root, "rev-parse", "HEAD").strip()


@pytest.fixture
def root(tmp_path: Path) -> Path:
    # A fictional repository holding the skill folder, committed.
    _git(tmp_path, "init", "-q", "-b", "main")
    _write(tmp_path, f"{checks.SKILL_FOLDER}/SKILL.md", "---\nname: crux-finder\n---\n")
    _commit(tmp_path)
    return tmp_path


def _case(root: Path, case: str, gold: str = GOLD, text: str = INPUT) -> None:
    _write(root, f"{EVALS}/cases/{case}/input.md", text)
    _write(root, f"{EVALS}/cases/{case}/gold.md", gold)


def _output(root: Path, case: str, name: str, body: str, commit: str | None = None) -> None:
    header = "" if commit is None else f"---\ncase: {case}\ncommit: {commit}\n---\n\n"
    _write(root, f"{EVALS}/results/{case}/{name}.md", header + body)


Review = Callable[[str, str], dict[str, str]]


def good(case: str, name: str) -> dict[str, str]:
    review = {"crux_match": "yes", "type_match": "yes", "people_statement": "no", "note": "fine"}
    if name not in ("run-1", "claude-ai"):
        review["same_crux_as_run_1"] = "yes"
    if case == "case-00":
        review["gate_fired"] = "yes"
    if case == "case-01":
        review["no_conflict_reported"] = "yes"
    return review


def _review(root: Path, case: str, names: list[str], review: Review = good) -> None:
    sections = [
        f"## {name}\n" + "".join(f"- {k}: {v}\n" for k, v in review(case, name).items())
        for name in names
    ]
    _write(root, f"{EVALS}/results/{case}/review.md", f"# Review: {case}\n\n" + "\n".join(sections))


def cycle(root: Path, cases: int = 10, review: Review = good, body: str | None = None) -> str:
    """A whole fictional cycle: gold committed, then two runs per case and their reviews."""
    ids = [f"case-{i:02}" for i in range(cases)]
    for case in ids:
        _case(root, case)
    gold = _commit(root)
    for case in ids:
        for name in ("run-1", "run-2"):
            _output(root, case, name, body or reply(), commit=gold)
        _review(root, case, ["run-1", "run-2"], review)
    return gold


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


# --- the outputs, through check() ------------------------------------------------------------


def test_a_report_that_holds_has_no_problems(root: Path) -> None:
    _case(root, "ferry")
    gold = _commit(root)
    _output(root, "ferry", "run-1", reply(more='A: "almost nobody travels after nine"\n'), gold)
    _review(root, "ferry", ["run-1"])
    assert _problems(root) == []


@pytest.mark.parametrize(
    ("body", "problem"),
    [
        (reply(more='"invented words"\n'), 'quote not in input.md: "invented words"'),
        (reply(53, 69), "steelmen of 53 and 69 words: one is over 1.25 times the other"),
        (reply(more=_steelman(235)), "401 words; a report is at most 400"),
    ],
)
def test_a_report_that_breaks_a_check_fails_it(root: Path, body: str, problem: str) -> None:
    _case(root, "ferry")
    gold = _commit(root)
    _output(root, "ferry", "run-1", body, gold)
    _review(root, "ferry", ["run-1"])
    assert [p.split(": ", 1)[1] for p in _problems(root)] == [problem]


def test_a_question_is_not_held_to_symmetry_or_length_but_needs_gate_fired(root: Path) -> None:
    _case(root, "tide")
    gold = _commit(root)
    _output(root, "tide", "run-1", QUESTION, gold)
    _review(root, "tide", ["run-1"])
    assert _problems(root) == [
        f"{EVALS}/results/tide/review.md: run-1 has no gate_fired; it is a question, not a report"
    ]
    _review(root, "tide", ["run-1"], lambda case, name: {**good(case, name), "gate_fired": "yes"})
    assert _problems(root) == []


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


# --- gold order ------------------------------------------------------------------------------


def test_gold_md_not_committed_fails(root: Path) -> None:
    _case(root, "ferry")
    assert _problems(root) == [f"{EVALS}/cases/ferry/gold.md: not committed"]


def test_gold_committed_before_its_results_passes(root: Path) -> None:
    _case(root, "ferry")
    gold = _commit(root)
    _output(root, "ferry", "run-1", reply(), gold)
    _review(root, "ferry", ["run-1"])
    _commit(root)
    assert _problems(root) == []


@pytest.mark.parametrize("results_first", [True, False])
def test_results_committed_with_or_before_gold_fail(root: Path, results_first: bool) -> None:
    _write(root, f"{EVALS}/cases/ferry/input.md", INPUT)
    _output(root, "ferry", "run-1", reply())
    _review(root, "ferry", ["run-1"])
    if results_first:
        _commit(root, f"{EVALS}/results")
    _write(root, f"{EVALS}/cases/ferry/gold.md", GOLD)
    _commit(root)
    assert _problems(root, "gold.md") == [
        f"{EVALS}/cases/ferry/gold.md: not committed before the first commit of its results"
    ]


def test_gold_changed_in_a_commit_after_its_results_fails(root: Path) -> None:
    _case(root, "ferry")
    gold = _commit(root)
    _output(root, "ferry", "run-1", reply(), gold)
    _review(root, "ferry", ["run-1"])
    _commit(root)
    _write(root, f"{EVALS}/cases/ferry/gold.md", GOLD.replace("Empirical", "Value"))
    _commit(root)
    assert _problems(root, "gold.md") == [
        f"{EVALS}/cases/ferry/gold.md: changed since its results were first committed",
        f"{EVALS}/cases/ferry/gold.md: changed since commit {gold[:12]}, which run-1 ran on",
    ]


def test_gold_changed_but_not_committed_while_results_exist_fails(root: Path) -> None:
    _case(root, "ferry")
    gold = _commit(root)
    _output(root, "ferry", "run-1", reply(), gold)
    _review(root, "ferry", ["run-1"])
    _write(root, f"{EVALS}/cases/ferry/gold.md", GOLD.replace("Empirical", "Value"))
    assert _problems(root, "gold.md") == [
        f"{EVALS}/cases/ferry/gold.md: changed since commit {gold[:12]}, which run-1 ran on",
        f"{EVALS}/cases/ferry/gold.md: uncommitted changes while results exist",
    ]


def test_a_run_on_a_commit_without_gold_fails(root: Path) -> None:
    before = _git(root, "rev-parse", "HEAD").strip()
    _case(root, "ferry")
    _commit(root)
    _output(root, "ferry", "run-1", reply(), before)
    _review(root, "ferry", ["run-1"])
    assert _problems(root, "gold.md") == [
        f"{EVALS}/cases/ferry/gold.md: not in commit {before[:12]}, which run-1 ran on"
    ]


def test_a_run_output_needs_its_commit_header(root: Path) -> None:
    _case(root, "ferry")
    _commit(root)
    _output(root, "ferry", "run-1", reply())
    _review(root, "ferry", ["run-1"])
    assert _problems(root) == [
        f"{EVALS}/results/ferry/run-1.md: no commit in its header; run.py writes one"
    ]


# --- review.md -------------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("change", "problem"),
    [
        (lambda r: {**r, "verdict": "yes"}, "unknown field verdict"),
        (lambda r: {**r, "crux_match": "maybe"}, "run-2's crux_match is 'maybe', not yes or no"),
        (lambda r: {k: v for k, v in r.items() if k != "note"}, "run-2 has no note"),
        (
            lambda r: {k: v for k, v in r.items() if k != "same_crux_as_run_1"},
            "run-2 has no same_crux_as_run_1",
        ),
    ],
)
def test_a_review_field_missing_or_wrong_fails(root: Path, change, problem: str) -> None:
    _case(root, "ferry")
    gold = _commit(root)
    for name in ("run-1", "run-2"):
        _output(root, "ferry", name, reply(), gold)

    def review(case: str, name: str) -> dict[str, str]:
        return change(good(case, name)) if name == "run-2" else good(case, name)

    _review(root, "ferry", ["run-1", "run-2"], review)
    assert [p.split(": ", 1)[1] for p in _problems(root, "review.md")] == [problem]


def test_review_sections_match_the_outputs(root: Path) -> None:
    _case(root, "ferry")
    gold = _commit(root)
    _output(root, "ferry", "run-1", reply(), gold)
    _review(root, "ferry", ["run-2"])
    where = f"{EVALS}/results/ferry/review.md"
    assert _problems(root, "review.md") == [
        f"{where}: a section for run-2, which has no output",
        f"{where}: no section for run-1",
    ]
    (root / where).unlink()
    assert _problems(root, "review.md") == [f"{where}: missing"]


def test_review_lines_outside_the_format_fail(root: Path) -> None:
    text = "# Review: ferry\n\nA stray sentence.\n\n## run-1\n- crux_match: yes\nmore words\n"
    _, problems = checks.parse_review(text, "review.md")
    assert problems == [
        "review.md:3: not a `- field: value` line in a run's section",
        "review.md:7: not a `- field: value` line in a run's section",
    ]


def test_run_1_has_no_stability_field_and_a_gate_is_recorded_for_every_run(root: Path) -> None:
    _case(root, "ferry")
    gold = _commit(root)
    for name in ("run-1", "run-2"):
        _output(root, "ferry", name, reply(), gold)

    def review(case: str, name: str) -> dict[str, str]:
        extra = {"same_crux_as_run_1": "yes", "gate_fired": "yes"} if name == "run-1" else {}
        return {**good(case, name), **extra}

    _review(root, "ferry", ["run-1", "run-2"], review)
    where = f"{EVALS}/results/ferry/review.md"
    assert _problems(root, "review.md") == [
        f"{where}: run-1 has same_crux_as_run_1",
        f"{where}: gate_fired is recorded for some of this case's outputs, not all",
    ]


def test_every_case_has_every_run_and_results_name_a_case(root: Path) -> None:
    cycle(root, cases=2)
    (root / EVALS / "results" / "case-01" / "run-2.md").unlink()
    _review(root, "case-01", ["run-1"])
    _write(root, f"{EVALS}/results/gale/run-1.md", reply())
    assert _problems(root, "results/") == [
        f"{EVALS}/results/gale: results for a case that does not exist",
        f"{EVALS}/results/case-01/run-2.md: missing",
    ]


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
    assert report.bars_met


def _missing(field: str, *pairs: tuple[str, str]) -> Review:
    # A review that holds, with "no" for the field on each (case, run) pair named.
    def review(case: str, name: str) -> dict[str, str]:
        found = good(case, name)
        if (case, name) in pairs:
            found[field] = "no"
        return found

    return review


def _both(*cases: str) -> list[tuple[str, str]]:
    return [(case, name) for case in cases for name in ("run-1", "run-2")]


@pytest.mark.parametrize(
    ("review", "check", "passed", "met"),
    [
        (_missing("crux_match", *_both("case-02", "case-03")), "Crux", 16, True),
        (
            _missing("crux_match", *_both("case-02", "case-03"), ("case-04", "run-1")),
            "Crux",
            15,
            False,
        ),
        (_missing("type_match", *_both("case-05")), "Type", 18, True),
        (_missing("type_match", *_both("case-05"), ("case-06", "run-2")), "Type", 17, False),
        (
            _missing("same_crux_as_run_1", ("case-02", "run-2"), ("case-03", "run-2")),
            "Stability",
            8,
            True,
        ),
        (
            _missing("same_crux_as_run_1", *[(f"case-0{i}", "run-2") for i in (2, 3, 4)]),
            "Stability",
            7,
            False,
        ),
        (_missing("gate_fired", ("case-00", "run-2")), "One-sided", 1, False),
    ],
)
def test_a_bar_is_met_at_its_line_and_missed_below_it(
    root: Path, review: Review, check: str, passed: int, met: bool
) -> None:
    cycle(root, review=review)
    row = _row(root, check)
    assert (row.passed, row.met) == (passed, met)


def test_a_bar_that_no_run_records_is_not_met(root: Path) -> None:
    def review(case: str, name: str) -> dict[str, str]:
        return {k: v for k, v in good(case, name).items() if k != "no_conflict_reported"}

    cycle(root, review=review)
    row = _row(root, "No-conflict")
    assert (row.passed, row.total, row.met) == (0, 0, False)


def test_people_statement_yes_on_any_run_misses_its_bar(root: Path) -> None:
    def review(case: str, name: str) -> dict[str, str]:
        found = good(case, name)
        if (case, name) == ("case-09", "run-2"):
            found["people_statement"] = "yes"
        return found

    cycle(root, review=review)
    row = _row(root, "people_statement")
    assert (row.passed, row.met) == (19, False)


def test_one_long_report_misses_the_length_bar(root: Path) -> None:
    cycle(root)
    _output(
        root,
        "case-04",
        "run-2",
        reply(more=_steelman(300)),
        _git(root, "rev-parse", "HEAD").strip(),
    )
    report = checks.check(root)
    row = next(row for row in report.rows if row.check.startswith("Length"))
    assert (row.passed, row.met) == (19, False)
    assert not report.bars_met


def test_runs_on_a_skill_changed_since_are_not_on_the_skill_as_it_stands(root: Path) -> None:
    cycle(root)
    assert _row(root, "Runs on the skill").met
    _write(root, f"{checks.SKILL_FOLDER}/SKILL.md", "---\nname: crux-finder\n---\nChanged.\n")
    _commit(root)
    row = _row(root, "Runs on the skill")
    assert (row.passed, row.met) == (0, False)


_VERSIONED = '---\nname: crux-finder\nmetadata:\n  version: "0.4.0"\n---\nThe procedure.\n'


def _versioned_cycle(root: Path) -> None:
    # A skill with a version line in SKILL.md and a version-shaped line in a reference.
    _write(root, f"{checks.SKILL_FOLDER}/SKILL.md", _VERSIONED)
    _write(root, f"{checks.SKILL_FOLDER}/references/procedure.md", '  version: "0.4.0"\n')
    _commit(root)
    cycle(root)


def test_a_change_to_the_version_line_alone_leaves_the_skill_as_it_stands(root: Path) -> None:
    _versioned_cycle(root)
    _write(root, f"{checks.SKILL_FOLDER}/SKILL.md", _VERSIONED.replace("0.4.0", "1.0.0"))
    _commit(root)
    row = _row(root, "Runs on the skill")
    assert (row.passed, row.met) == (20, True)


def test_the_version_line_with_another_change_is_a_changed_skill(root: Path) -> None:
    _versioned_cycle(root)
    changed = _VERSIONED.replace("0.4.0", "1.0.0").replace("procedure", "procedure, changed")
    _write(root, f"{checks.SKILL_FOLDER}/SKILL.md", changed)
    _commit(root)
    row = _row(root, "Runs on the skill")
    assert (row.passed, row.met) == (0, False)


def test_a_version_shaped_line_outside_skill_md_is_a_changed_skill(root: Path) -> None:
    _versioned_cycle(root)
    _write(root, f"{checks.SKILL_FOLDER}/references/procedure.md", '  version: "1.0.0"\n')
    _commit(root)
    row = _row(root, "Runs on the skill")
    assert (row.passed, row.met) == (0, False)


def test_the_smoke_test_needs_three_of_three(root: Path) -> None:
    cycle(root, cases=3)
    for case in ("case-00", "case-01", "case-02"):
        _output(root, case, "claude-ai", reply())
        _review(root, case, ["run-1", "run-2", "claude-ai"])
    smoke = checks.check(root).smoke
    assert smoke is not None and (smoke.passed, smoke.total, smoke.met) == (3, 3, True)
    _output(root, "case-02", "claude-ai", reply(53, 69))
    smoke = checks.check(root).smoke
    assert smoke is not None and (smoke.passed, smoke.met) == (2, False)


# --- the command -----------------------------------------------------------------------------


def test_main_with_no_cases_passes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(checks, "ROOT", tmp_path)
    assert checks.main() == 0
    assert capsys.readouterr().out == "checks: 0 case(s), 0 problem(s); no cases yet\n"


def test_main_with_cases_and_no_results_passes_without_counting_bars(
    root: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    _case(root, "ferry")
    _commit(root)
    monkeypatch.setattr(checks, "ROOT", root)
    assert checks.main() == 0
    assert capsys.readouterr().out.endswith(
        "checks: 1 case(s), 0 problem(s); no results yet, so the pass bars are not counted\n"
    )


def test_main_prints_the_table_and_fails_on_a_missed_bar(
    root: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    cycle(root, review=_missing("type_match", *_both("case-01", "case-02")))
    monkeypatch.setattr(checks, "ROOT", root)
    assert checks.main() == 1
    out = capsys.readouterr().out
    assert "| Type matches gold | ≥ 18 / 20 runs | 16 / 20 | **no** |" in out
    assert out.endswith("pass bars not met: Type matches gold\n")


def test_a_blank_line_between_the_crux_label_and_its_sentence_keeps_it_exempt() -> None:
    body = reply().replace("**Double crux · Empirical**\n>", "**Double crux · Empirical**\n\n>")
    assert _quotes(body) == ([], 0)


@pytest.mark.parametrize(
    ("text", "header"),
    [
        ("---\ncase: ferry\ncommit: abc\n---\n\n## Crux report\n", "case: ferry\ncommit: abc"),
        ("---\n\n## Crux report\n\nText.\n", None),
        ("---\n\n## Crux report\n\nText.\n\n---\n\nMore.\n", None),
    ],
)
def test_only_a_block_of_fields_is_an_outputs_header(text: str, header: str | None) -> None:
    found, body = checks.output_parts(text)
    assert found == header
    assert body == (text if header is None else "\n## Crux report\n")


def test_an_output_that_opens_with_a_rule_is_still_checked(root: Path) -> None:
    _case(root, "ferry")
    _commit(root)
    _output(root, "ferry", "claude-ai", "---\n\n" + reply(53, 69))
    _review(root, "ferry", ["claude-ai"])
    assert _problems(root, "claude-ai.md") == [
        f"{EVALS}/results/ferry/claude-ai.md: steelmen of 53 and 69 words: "
        "one is over 1.25 times the other"
    ]


def test_an_output_that_cannot_be_read_is_a_problem_not_a_crash(root: Path) -> None:
    _case(root, "ferry")
    _commit(root)
    (root / EVALS / "results" / "ferry" / "claude-ai.md").mkdir(parents=True)
    problems = _problems(root, "claude-ai.md: cannot be read")
    assert len(problems) == 1
