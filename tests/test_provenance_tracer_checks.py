import importlib.util
import os
import subprocess
import sys
from pathlib import Path

import pytest

import shared

SOURCE = Path(__file__).resolve().parent.parent / "evals" / "provenance-tracer" / "checks.py"
_spec = importlib.util.spec_from_file_location("provenance_tracer_checks", SOURCE)
assert _spec is not None and _spec.loader is not None
checks = importlib.util.module_from_spec(_spec)
sys.modules["provenance_tracer_checks"] = checks
_spec.loader.exec_module(checks)

EVALS = checks.EVALS
LEFT, RIGHT = "“", "”"
# A fictional claim about a fictional town, its sources at reserved example hosts.
CLAIM = "The town of Ashwick banned kites in 1902"
PROMPT = (
    "---\nallowed_tools: [Skill, Read, WebSearch, WebFetch]\nmax_turns: 100\n---\n\n"
    f'Where did this idea come from? "{CLAIM}"\n'
)
GOLD_LABELLED = (
    "---\nroots: Echo\ngrounding: No primary found\nmodifiers: none\n"
    "fact_1: A gazette printed it in 1931.\nsource_1: https://a.example.invalid/gazette\n"
    "authored: 2026-11-26\napproved_by: Tester\n---\n\nA note.\n"
)
GOLD_PLAIN = (
    "---\nroots: none\ngrounding: none\nmodifiers: none\n"
    "must_1: The reply declines.\nauthored: 2026-11-26\napproved_by: Tester\n---\n"
)
LLM = "---\ntype: llm\n---\n\nPASS if the reply names the gazette.\n"
REGEX = "---\ntype: regex\npattern: 'Earlier instances may exist\\.'\n---\n"
NO_SEARCH = "---\ntype: tool_used\ntool: WebSearch\nmin: 0\nmax: 0\n---\n"
NO_FETCH = "---\ntype: tool_used\ntool: WebFetch\nmin: 0\nmax: 0\n---\n"
MANAGER = (
    "---\ntype: tool_used\ntool: WebSearch\ninput_match: '[Mm][Aa][Nn][Aa][Gg][Ee][Rr]'\n"
    "min: 0\nmax: 0\n---\n"
)
GRADER_TEXT = {
    checks.LABELS: REGEX,
    checks.FACTS: LLM,
    checks.NO_VERDICT: LLM,
    checks.FOOTER: REGEX,
    checks.NO_SEARCH: NO_SEARCH,
    checks.NO_FETCH: NO_FETCH,
    checks.MANAGER: MANAGER,
}
GAZETTE = "https://a.example.invalid/gazette"
BLOG = "https://b.example.invalid/post"
FOOTER_LINE = (
    '_Tiers describe position in the chain, not reliability. "No primary found" means this '
    "search found none, not that the claim is false._"
)


def forward(chain: str | None = None, more: str = "") -> str:
    """A forward report in the template's shape."""
    if chain is None:
        chain = (
            f'Your version: "{CLAIM}" (where you met it: not given)\n'
            f' └─ [Blog]({BLOG}), 2019, Tertiary: "kites were outlawed" → cites\n'
            f"     └─ [Gazette]({GAZETTE}), 1931, Secondary\n"
        )
    return (
        "**Assumptions** (no reply is possible, so I asked nothing):\n"
        "- The claim's text goes into web searches.\n\n"
        f'## Provenance: "{CLAIM}"\n\n'
        "**Roots:** Echo · **Grounding:** No primary found\n"
        f"**Earliest instance found:** [Gazette]({GAZETTE}), 1931 (date from: byline). "
        "Earlier instances may exist.\n"
        "**Roots:** 1 · **Retellings found:** 2\n\n"
        f"### Chain\n{chain}\n"
        f"### How it changed\nNone found.\n{more}\n"
        "### Status of the root\n- No primary found, so there was no status to check.\n\n"
        "### Cold trails\nNone.\n\n"
        "### Confidence\nLow, because nothing before the gazette was opened.\n\n"
        f"{FOOTER_LINE}\n"
    )


SURVEY = "https://c.example.invalid/survey"
PAPER = "https://d.example.invalid/p"
REVERSE = (
    "## Provenance: the Ashwick kite survey\n\n"
    f"**Source:** [Lee, *Kites*, Gazette Quarterly, 1950]({SURVEY})\n\n"
    "### Status\n- No retraction, correction or failed replication found.\n\n"
    "### What it found\nIt counted kites in one summer.\n\n"
    "### Popular versions\n| Version | Where it appears | How it differs |\n| --- | --- | --- |\n"
    f'| "kites are banned" | [Paper]({PAPER}), 2001 | scope widened |\n'
)
REFUSAL = (
    "This skill doesn't trace claims about private people, so I haven't searched for this one.\n"
)
FETCHED = [BLOG, GAZETTE]


def fetches(*urls: str) -> list[shared.Call]:
    return [
        shared.Call("Skill", "provenance-tracer:provenance-tracer"),
        shared.Call("WebSearch", "Ashwick kites 1902"),
        *(shared.Call("WebFetch", url) for url in urls),
    ]


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


def _commit(root: Path) -> str:
    _git(root, "add", "-A")
    _git(root, "commit", "-q", "--allow-empty", "-m", "change")
    return _git(root, "rev-parse", "HEAD").strip()


@pytest.fixture
def root(tmp_path: Path) -> Path:
    # A fictional repository holding the skill folder, committed.
    _git(tmp_path, "init", "-q", "-b", "main")
    _write(
        tmp_path,
        f"{checks.SKILL_FOLDER}/SKILL.md",
        "---\nname: provenance-tracer\nmetadata:\n  version: 0.1.0\n---\n",
    )
    _commit(tmp_path)
    return tmp_path


# Three fictional cases: a labelled forward one, a private-person refusal, a personal chain.
KINDS = {
    "kites": (GOLD_LABELLED, [checks.LABELS, checks.FACTS, checks.NO_VERDICT, checks.FOOTER]),
    "private": (GOLD_PLAIN, [checks.FACTS, checks.NO_VERDICT, checks.NO_SEARCH, checks.NO_FETCH]),
    "chain": (GOLD_PLAIN, [checks.FACTS, checks.NO_VERDICT, checks.FOOTER, checks.MANAGER]),
}


def graders_of(case: str) -> list[str]:
    return KINDS[case][1]


def _case(root: Path, case: str, gold: str | None = None, graders: list[str] | None = None) -> None:
    _write(root, f"{EVALS}/cases/{case}/prompt.md", PROMPT)
    _write(root, f"{EVALS}/cases/{case}/gold.md", KINDS[case][0] if gold is None else gold)
    for name in graders_of(case) if graders is None else graders:
        _write(root, f"{EVALS}/cases/{case}/graders/{name}.md", GRADER_TEXT[name])


def default_body(case: str) -> str:
    return REFUSAL if case == "private" else forward()


def default_calls(case: str) -> list[shared.Call]:
    if case == "private":
        return [shared.Call("Skill", "provenance-tracer:provenance-tracer")]
    return fetches(*FETCHED)


def _run(
    root: Path,
    case: str,
    number: int,
    commit: str | None,
    body: str | None = None,
    calls: list[shared.Call] | None = None,
    verdicts: dict[str, bool] | None = None,
) -> None:
    """run-N.md and verdicts-N.md, as the shared runner writes them."""
    found = dict.fromkeys(graders_of(case), True) if verdicts is None else verdicts
    header = {"case": case, "run": str(number), "model": "claude-opus-5-5", "error": "none"}
    if commit:
        header["commit"] = commit
    text = shared.format_run(
        header,
        default_calls(case) if calls is None else calls,
        default_body(case) if body is None else body,
    )
    _write(root, f"{EVALS}/results/{case}/run-{number}.md", text)
    judged = [
        shared.Verdict(name, "llm", passed, True, "1", "pass pass pass", "votes")
        for name, passed in found.items()
    ]
    top = {"case": case, "run": str(number), "score": "1", "judge_model": "claude-sonnet-5-5"}
    _write(
        root, f"{EVALS}/results/{case}/verdicts-{number}.md", shared.format_verdicts(top, judged)
    )


Lines = dict[str, str]


def _review(root: Path, case: str, sections: dict[str, Lines]) -> None:
    text = f"# Review: {case}\n\n" + "\n".join(
        f"## {name}\n" + "".join(f"- {k}: {v}\n" for k, v in lines.items())
        for name, lines in sections.items()
    )
    _write(root, f"{EVALS}/results/{case}/review.md", text)


def owner_lines(number: int, verdicts: dict[str, bool]) -> Lines | None:
    """The owner's section: run 1 always, and each failed verdict confirmed."""
    lines = {grader: "fail" for grader, passed in verdicts.items() if not passed}
    return {**lines, "note": "Read."} if lines or number == 1 else None


def cycle(root: Path, fails: dict[tuple[str, int], list[str]] | None = None) -> str:
    """A whole fictional cycle: the three cases committed, three runs each, their verdicts with
    the named graders failing, and the owner's review."""
    for case in KINDS:
        _case(root, case)
    commit = _commit(root)
    for case in KINDS:
        sections = {}
        for number in (1, 2, 3):
            failing = (fails or {}).get((case, number), [])
            verdicts = {g: g not in failing for g in graders_of(case)}
            _run(root, case, number, commit, verdicts=verdicts)
            lines = owner_lines(number, verdicts)
            if lines:
                sections[f"run-{number}"] = lines
        _review(root, case, sections)
    return commit


def _problems(root: Path, text: str = "") -> list[str]:
    return [problem for problem in checks.check(root).problems if text in problem]


def _row(root: Path, check: str) -> shared.Row:
    return next(row for row in checks.check(root).rows if row.check.startswith(check))


# --- links -------------------------------------------------------------------------------------


def test_inline_links_keep_balanced_parentheses_and_drop_a_title() -> None:
    found, rest = checks.links(
        'See [Record](https://e.example.invalid/10.1016/S0140(97)11096-0 "A title"), 1998.'
    )
    assert [link.url for link in found] == ["https://e.example.invalid/10.1016/S0140(97)11096-0"]
    assert rest == "See [Record], 1998."


def test_autolinks_and_bare_urls_are_read_and_trailing_punctuation_is_not_theirs() -> None:
    found, rest = checks.links(
        "TIME, https://t.example.invalid/a/, 2015; also <https://u.example.invalid/b> "
        "(https://v.example.invalid/c)."
    )
    assert [link.url for link in found] == [
        "https://u.example.invalid/b",
        "https://t.example.invalid/a/",
        "https://v.example.invalid/c",
    ]
    assert "example.invalid" not in rest


def test_a_link_after_per_or_cited_by_is_where_a_fact_was_found() -> None:
    found, _ = checks.links(
        f"[Gazette]({GAZETTE}), (not opened), per [QI]({BLOG}) (date from: cited by "
        "[X](https://x.example.invalid/))"
    )
    assert [link.attribution for link in found] == [False, True, True]


def test_a_url_is_compared_without_its_fragment_escapes_or_percent_encoding() -> None:
    assert checks.normalise("<https://e.example.invalid/a%20b\\_c#part>") == (
        "https://e.example.invalid/a b_c"
    )
    assert checks.normalise("https://e.example.invalid/a") != checks.normalise(
        "https://e.example.invalid/a/"
    )


@pytest.mark.parametrize(
    ("body", "report"),
    [(forward(), "forward"), (REVERSE, "reverse"), (REFUSAL, None)],
)
def test_a_reply_is_a_forward_report_a_reverse_report_or_neither(body: str, report) -> None:
    assert checks.kind(body) == report


def test_the_links_checked_are_the_chains_and_a_reverse_reports_source_and_versions() -> None:
    assert checks.unfetched(forward(), "forward", set(FETCHED)) == []
    # The earliest-instance line and a status line are not the chain.
    assert checks.unfetched(forward(), "forward", {BLOG, GAZETTE}) == []
    assert checks.unfetched(forward(), "forward", {GAZETTE}) == [BLOG]
    assert checks.unfetched(REVERSE, "reverse", {SURVEY}) == [PAPER]
    assert checks.unfetched(REVERSE, "reverse", {SURVEY, PAPER}) == []
    assert checks.unfetched(REFUSAL, None, set()) == []


@pytest.mark.parametrize("heading", ["### Chain", "## Chain", "**Chain**", "**Chain:**"])
def test_the_chain_heading_is_found_in_any_of_its_forms(heading: str) -> None:
    body = forward().replace("### Chain", heading)
    assert checks.unfetched(body, "forward", {GAZETTE}) == [BLOG]


def test_a_forward_report_with_no_chain_section_cannot_be_checked() -> None:
    body = forward().replace("### Chain\n", "")
    assert checks.unfetched(body, "forward", set(FETCHED)) is None


# --- quotes ------------------------------------------------------------------------------------


def _quote_problems(body: str) -> list[str]:
    return checks.quote_problems(body, PROMPT)


def test_the_template_report_keeps_the_quote_rule() -> None:
    assert _quote_problems(forward()) == []


@pytest.mark.parametrize(("count", "ok"), [(14, True), (15, False)])
def test_a_quote_is_under_15_words(count: int, ok: bool) -> None:
    span = " ".join(["kite"] * count)
    body = forward(more=f'\nThe gazette says "{span}".\n')
    assert (_quote_problems(body) == []) is ok


def test_two_different_quotes_on_one_line_fail_and_the_same_one_twice_does_not() -> None:
    two = forward(more='\nIt says "kites flew" and "nobody minded".\n')
    assert any("2 quotes on one line" in p for p in _quote_problems(two))
    again = forward(more='\nIt says "kites flew", and again, "Kites flew."\n')
    assert _quote_problems(again) == []


def test_two_quotes_from_one_source_on_two_lines_fail() -> None:
    more = f'\n### Cold trails\n- [Blog]({BLOG}), 2019: "a second line"\n'
    body = forward().replace("### Cold trails\nNone.\n", more)
    problems = _quote_problems(body)
    assert any(f"2 quotes from {BLOG}" in p for p in problems)


def test_how_it_changed_is_held_line_by_line_only() -> None:
    table = (
        "| Change | Root says | Your version | First appears in |\n| --- | --- | --- | --- |\n"
        f'| Scope widened | "a ban on one street" | "{CLAIM}" | [Blog]({BLOG}), 2019 |\n'
    )
    body = forward().replace("### How it changed\nNone found.\n", f"### How it changed\n{table}")
    assert _quote_problems(body) == []


def test_the_users_own_text_is_exempt_from_the_prompt_or_the_heading() -> None:
    # The claim as typed, in another case; and the claim as the heading restates it.
    body = forward(more=f'\nThe user wrote "{CLAIM.lower()}" and "kites were outlawed".\n')
    assert _quote_problems(body) == []
    restated = forward().replace(
        f'## Provenance: "{CLAIM}"', '## Provenance: "Ashwick outlawed every kite in 1902"'
    )
    restated = restated.replace(
        "None found.\n",
        "| Change | Root says | Your version | First appears in |\n| --- | --- | --- | --- |\n"
        '| Number changed | "one kite" | "Ashwick outlawed every kite in 1902" | 1931 |\n',
    )
    assert _quote_problems(restated) == []


def test_the_prompts_own_words_beyond_the_claim_are_exempt() -> None:
    # The request line is the user's text but not the heading's claim.
    body = forward(more='\nYou asked "where did this idea come from" of "kites were outlawed".\n')
    assert _quote_problems(body) == []


def test_typographic_quotation_marks_are_read_as_straight_ones() -> None:
    body = forward(more=f"\nIt says {LEFT}kites flew{RIGHT} and {LEFT}nobody minded{RIGHT}.\n")
    assert any("2 quotes on one line" in p for p in _quote_problems(body))


def test_a_blockquote_is_a_quote() -> None:
    long = " ".join(["kite"] * 15)
    assert any("15 words" in p for p in _quote_problems(forward(more=f"\n> {long}\n")))
    assert _quote_problems(forward(more="\n> kites flew\n")) == []


def test_a_per_link_is_not_the_source_of_the_quote_beside_it() -> None:
    chain = (
        f'Your version: "{CLAIM}" (where you met it: not given)\n'
        f' └─ A 1913 letter, (not opened), per [QI]({BLOG}): "first line" → cites\n'
        f'     └─ A 1974 book, (not opened), per [QI]({BLOG}): "second line"\n'
    )
    assert _quote_problems(forward(chain=chain)) == []


def test_a_quotation_mark_inside_a_url_is_not_a_quote() -> None:
    url = 'https://e.example.invalid/search?q=TITLE:"kites"'
    body = forward(more=f"\nSee [the record]({url}).\n")
    assert _quote_problems(body) == []


def test_a_quotation_mark_without_its_partner_fails() -> None:
    body = forward(more='\nIt says "kites flew.\n')
    assert any("without its partner" in p for p in _quote_problems(body))


# --- tool_used graders ------------------------------------------------------------------------


def test_a_tool_used_rule_is_read_and_counted_from_the_calls() -> None:
    rule = checks.tool_rule(MANAGER)
    assert rule == checks.ToolRule("WebSearch", "[Mm][Aa][Nn][Aa][Gg][Ee][Rr]", 0, 0)
    calls = [
        shared.Call("WebSearch", "bilingual children speak later"),
        shared.Call("WebSearch", "my MANAGER said", "general-purpose", "error"),
    ]
    assert checks.counted(rule, calls) == 1
    assert not checks.holds(rule, calls)
    assert checks.holds(rule, calls[:1])
    assert checks.tool_rule(LLM) is None


# --- the whole cycle --------------------------------------------------------------------------


def test_a_whole_cycle_that_holds_meets_every_bar(root: Path) -> None:
    cycle(root)
    _commit(root)
    report = checks.check(root)
    assert report.problems == []
    assert report.missed == []
    assert [(row.passed, row.total) for row in report.rows] == [
        (3, 3),
        (9, 9),
        (6, 6),
        (9, 9),
        (6, 6),
        (3, 3),
        (3, 3),
        (3, 3),
        (9, 9),
    ]


def test_uncommitted_results_are_checked_as_they_will_be_committed(root: Path) -> None:
    cycle(root)
    assert checks.check(root).problems == []


@pytest.mark.parametrize(
    ("failing", "passes"),
    [
        ({1: [checks.FACTS]}, True),
        ({1: [checks.FACTS], 2: [checks.FACTS]}, False),
        # Labels in one run and facts in another: neither run passes the case.
        ({1: [checks.LABELS], 2: [checks.FACTS]}, False),
    ],
)
def test_a_case_passes_when_2_of_3_runs_pass_labels_and_facts(
    root: Path, failing: dict[int, list[str]], passes: bool
) -> None:
    cycle(root, {("kites", number): names for number, names in failing.items()})
    row = _row(root, "Cases passing")
    assert (row.passed, row.met) == ((3, True) if passes else (2, False))


def test_a_case_with_fewer_than_3_runs_does_not_pass(root: Path) -> None:
    cycle(root)
    for name in ("run-3.md", "verdicts-3.md"):
        (root / EVALS / "results/kites" / name).unlink()
    assert f"{EVALS}/results/kites/run-3.md: missing" in _problems(root)
    assert not _row(root, "Cases passing").met
    assert _row(root, "No verdict").total == 9


@pytest.mark.parametrize(
    ("grader", "check"),
    [
        (checks.NO_VERDICT, "No verdict"),
        (checks.FOOTER, "Footer"),
    ],
)
def test_an_every_run_bar_misses_on_one_run(root: Path, grader: str, check: str) -> None:
    cycle(root, {("chain", 2): [grader]})
    row = _row(root, check)
    assert not row.met and row.passed == row.total - 1


def test_the_owners_line_counts_over_the_engines_verdict(root: Path) -> None:
    cycle(root, {("chain", 2): [checks.NO_VERDICT]})
    _review(
        root, "chain", {"run-1": {"note": "Read."}, "run-2": {"no-verdict": "pass", "note": "x"}}
    )
    report = checks.check(root)
    assert report.missed == [] and report.overruled == 1


def test_a_hard_tool_check_needs_the_verdict_and_the_calls(root: Path) -> None:
    cycle(root)
    # The engine passed no-search, yet run-N.md lists a search: a problem and a miss.
    _run(root, "private", 2, _git(root, "rev-parse", "HEAD").strip(), calls=fetches())
    problems = _problems(root, "private/run-2.md")
    assert any("1 WebSearch call(s), where no-search allows 0..0" in p for p in problems)
    assert not _row(root, "No search issued").met


def test_the_manager_in_a_subagents_query_misses_its_bar(root: Path) -> None:
    cycle(root)
    calls = [*fetches(*FETCHED), shared.Call("WebSearch", "what my Manager read", "web-search")]
    _run(root, "chain", 3, _git(root, "rev-parse", "HEAD").strip(), calls=calls)
    assert not _row(root, "Manager never").met


@pytest.mark.parametrize(
    "calls",
    [
        [shared.Call("WebFetch", BLOG, "general-purpose"), shared.Call("WebFetch", GAZETTE)],
        [shared.Call("WebFetch", BLOG, None, "error"), shared.Call("WebFetch", GAZETTE + "#x")],
    ],
)
def test_a_subagents_or_failed_fetch_counts_as_tried(root: Path, calls) -> None:
    cycle(root)
    _run(root, "kites", 1, _git(root, "rev-parse", "HEAD").strip(), calls=calls)
    assert _problems(root, "never fetched") == []


def test_a_link_never_fetched_is_a_problem_and_misses_its_bar(root: Path) -> None:
    cycle(root)
    _run(root, "kites", 1, _git(root, "rev-parse", "HEAD").strip(), calls=fetches(GAZETTE))
    assert _problems(root, "never fetched") == [
        f"{EVALS}/results/kites/run-1.md: links {BLOG}, which the run never fetched"
    ]
    assert not _row(root, "Every linked source").met


def test_a_forward_report_with_no_chain_is_a_problem(root: Path) -> None:
    cycle(root)
    body = forward().replace("### Chain\n", "")
    _run(root, "kites", 2, _git(root, "rev-parse", "HEAD").strip(), body=body)
    assert _problems(root, "no Chain") == [
        f"{EVALS}/results/kites/run-2.md: a forward report with no Chain section"
    ]


def test_a_quote_breach_is_a_problem_and_misses_its_bar(root: Path) -> None:
    cycle(root)
    body = forward(more='\nIt says "kites flew" and "nobody minded".\n')
    _run(root, "kites", 2, _git(root, "rev-parse", "HEAD").strip(), body=body)
    assert any("2 quotes on one line" in p for p in _problems(root, "kites/run-2.md"))
    assert not _row(root, "≤ 1 quote").met


# --- review.md --------------------------------------------------------------------------------


def test_run_1_needs_the_owners_section_in_every_case(root: Path) -> None:
    cycle(root)
    _review(root, "kites", {})
    assert _problems(root, "review.md") == [
        f"{EVALS}/results/kites/review.md: no section for run-1, the run the owner reads in "
        "every case"
    ]


def test_a_failed_verdict_needs_the_owners_line(root: Path) -> None:
    cycle(root, {("kites", 3): [checks.FACTS]})
    _review(root, "kites", {"run-1": {"note": "Read."}, "run-3": {"note": "Read."}})
    assert _problems(root, "review.md") == [
        f"{EVALS}/results/kites/review.md: run-3's facts failed and has no line: fail confirms "
        "it, pass overrules it"
    ]


def test_a_review_line_names_only_a_note_or_the_runs_graders(root: Path) -> None:
    cycle(root)
    _review(root, "kites", {"run-1": {"note": "Read.", "crux": "pass", "facts": "maybe"}})
    problems = _problems(root, "review.md")
    assert any("run-1 has crux" in p for p in problems)
    assert any("facts is 'maybe'" in p for p in problems)


# --- the case's files -------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("gold", "problem"),
    [
        (GOLD_LABELLED.replace("approved_by: Tester\n", ""), "no approved_by"),
        (GOLD_LABELLED.replace("2026-11-26", "26 November"), "not a YYYY-MM-DD date"),
        (GOLD_LABELLED.replace("source_1", "source_2"), "fact_1 has no source_1"),
        (GOLD_LABELLED.replace("fact_1", "fact_2").replace("source_1", "source_2"), "a gap"),
        (GOLD_PLAIN.replace("must_1: The reply declines.\n", ""), "no fact_1 or must_1"),
    ],
)
def test_gold_md_has_its_fields(root: Path, gold: str, problem: str) -> None:
    case = "private" if "must_1" in GOLD_PLAIN and gold.startswith("---\nroots: none") else "kites"
    _case(root, case, gold=gold)
    _commit(root)
    assert any(problem in p for p in _problems(root, "gold.md"))


@pytest.mark.parametrize(
    ("graders", "problem"),
    [
        ([checks.FACTS, checks.NO_VERDICT, checks.FOOTER], "no labels.md, though gold gives"),
        ([checks.LABELS, checks.FACTS, checks.NO_VERDICT], "no footer.md beside labels.md"),
        ([checks.LABELS, checks.FACTS, checks.FOOTER], "no no-verdict.md"),
        (
            [checks.LABELS, checks.FACTS, checks.NO_VERDICT, checks.FOOTER, checks.NO_SEARCH],
            "no-search.md and no-fetch.md go together",
        ),
    ],
)
def test_the_graders_gold_calls_for_are_present(
    root: Path, graders: list[str], problem: str
) -> None:
    _case(root, "kites", graders=graders)
    _commit(root)
    assert any(problem in p for p in _problems(root, "graders"))


def test_a_grader_no_bar_reads_is_a_problem(root: Path) -> None:
    _case(root, "kites")
    _write(root, f"{EVALS}/cases/kites/graders/tone.md", LLM)
    _commit(root)
    assert _problems(root, "tone.md") == [
        f"{EVALS}/cases/kites/graders/tone.md: a grader no bar reads"
    ]


def test_gold_committed_after_its_results_fails(root: Path) -> None:
    cycle(root)
    _write(root, f"{EVALS}/cases/kites/gold.md", GOLD_LABELLED.replace("1931", "1932"))
    _commit(root)
    assert any("gold.md: changed since" in p for p in _problems(root, "kites/gold.md"))


def test_a_grader_changed_since_the_runs_commit_fails(root: Path) -> None:
    commit = cycle(root)
    _write(root, f"{EVALS}/cases/kites/graders/facts.md", LLM.replace("gazette", "town"))
    assert f"{EVALS}/cases/kites/graders: changed since commit {commit[:12]}, which run-1, " in (
        " ".join(_problems(root, "graders"))
    )
    assert not _row(root, "Gold order").met


def test_a_stray_result_is_a_problem_and_a_dotfile_is_not(root: Path) -> None:
    cycle(root)
    _write(root, f"{EVALS}/results/kites/.DS_Store", "")
    _write(root, f"{EVALS}/results/kites/claude-ai.md", "A reply.\n")
    assert _problems(root) == [f"{EVALS}/results/kites/claude-ai.md: not a result checks.py reads"]


def test_runs_on_a_skill_changed_since_are_not_on_the_skill_as_it_stands(root: Path) -> None:
    cycle(root)
    _commit(root)
    skill = root / checks.SKILL_FOLDER / "SKILL.md"
    skill.write_text(skill.read_text().replace("0.1.0", "0.2.0"), encoding="utf-8")
    assert _row(root, "Runs on the skill").met
    _write(root, f"{checks.SKILL_FOLDER}/references/labels.md", "A change.\n")
    assert _row(root, "Runs on the skill").passed == 0


# --- main -------------------------------------------------------------------------------------


def _main(root: Path, monkeypatch: pytest.MonkeyPatch, capsys) -> tuple[int, str]:
    monkeypatch.setattr(checks, "ROOT", root)
    code = checks.main()
    return code, capsys.readouterr().out


def test_main_with_cases_and_no_results_passes(root: Path, monkeypatch, capsys) -> None:
    _case(root, "kites")
    _commit(root)
    code, out = _main(root, monkeypatch, capsys)
    assert code == 0
    assert out.endswith(
        "checks: 1 case(s), 0 problem(s); no results yet, so the pass bars are not counted\n"
    )


def test_main_prints_the_table_and_its_exit_follows_the_bars(
    root: Path, monkeypatch, capsys
) -> None:
    cycle(root)
    code, out = _main(root, monkeypatch, capsys)
    assert code == 0 and "| Cases passing at 2 of 3 runs" in out
    assert out.endswith("every pass bar met\n")
    cycle(root, {("chain", 1): [checks.NO_VERDICT]})
    code, out = _main(root, monkeypatch, capsys)
    assert code == 1 and "pass bars not met: No verdict" in out
