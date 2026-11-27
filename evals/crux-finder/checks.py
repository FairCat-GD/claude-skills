"""crux-finder's checks on the shared runner's results, and the summary table against the pass bars.

For every case: prompt.md holds the prompt, graders/ the graders the bars read, and gold.md names
who approved it and is committed before any of its results present now, and unchanged since
(invariant 7). For every run, `run-N.md` and `verdicts-N.md` as `evals/run.py` writes them: the
case's prompt.md and graders are as they were in the run's commit; every quoted span of the reply
is in the prompt; a report's steelmen are balanced and its length within 400 words. review.md
holds the owner's lines: one for every failed verdict, confirming or overruling it, stability
from run 2 on, and the judgement of each claude.ai reply. The bars count each verdict as the
owner's line has it, else as the engine gave it. A run the engine graded is counted as graded,
an error in its header included, since that is the skill's result. This script may read gold.md;
only the runner and the session under test may not.

Usage: uv run evals/crux-finder/checks.py
"""

import re
import sys
from collections.abc import Callable
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import shared

ROOT = Path(__file__).resolve().parent.parent.parent
# Relative to the root, as git names them.
EVALS = "evals/crux-finder"
SKILL_FOLDER = "plugins/crux-finder/skills/crux-finder"
LENGTH = 400
# Each steelman within 25% of the other: the longer at most 5/4 of the shorter.
SYMMETRY = Fraction(5, 4)
GOLD_FIELDS = ("crux", "type", "crux_for", "approved_by")
YES_NO = ("yes", "no")
PASS_FAIL = ("pass", "fail")
# The graders, by the file name each bar reads: every case has the first three.
CRUX = "crux"
TYPE = "type"
PEOPLE = "no-statement-about-people"
GATE = "gate"
NO_CONFLICT = "no-conflict"
REQUIRED_GRADERS = (CRUX, TYPE, PEOPLE)
GRADERS = (*REQUIRED_GRADERS, GATE, NO_CONFLICT)
STABILITY = "same_crux_as_run_1"
NOTE = "note"
# A claude.ai reply is judged by the owner alone, with round 1's fields.
CLAUDE_AI = "claude-ai"
CLAUDE_AI_REQUIRED = ("crux_match", "type_match", "people_statement", NOTE)
CLAUDE_AI_FIELDS = (*CLAUDE_AI_REQUIRED, "gate_fired", "no_conflict_reported")
SMOKE_CASES = 3

_RUN = re.compile(r"run-([1-9][0-9]*)\.md")
_VERDICTS = re.compile(r"verdicts-([1-9][0-9]*)\.md")
_REPORT = re.compile(r"^## Crux report[ \t]*$", re.MULTILINE)
_STEELMAN = re.compile(r"\*\*([AB])(?: \([^)\n]*\))?, strongest form:\*\*[ \t]*(.*)")
_CRUX_LABEL = re.compile(r"\*\*(?:(?:Double crux|Crux for [AB]) · [^*\n]+|No crux)\*\*")
_HEADING = re.compile(r"#{1,3}\s")
_CLAIM_MAP = re.compile(r"###\s+Claim map\s*")
_HEADER_LINE = re.compile(r"[a-z0-9_]+:.*")

words = shared.words
found_verbatim = shared.found_verbatim


def is_report(body: str) -> bool:
    """A reply without the report's heading is a question, held to neither symmetry nor length."""
    return _REPORT.search(body) is not None


def report_words(body: str) -> int:
    """The output's words, a claim map left out: it is appended on request and not counted."""
    kept, skipping = [], False
    for line in body.split("\n"):
        stripped = line.strip()
        if _HEADING.match(stripped):
            skipping = _CLAIM_MAP.fullmatch(stripped) is not None
        if not skipping:
            kept.append(line)
    return words("\n".join(kept))


def steelmen(body: str) -> dict[str, int]:
    """Each steelman's words, by party, the label left out. A steelman runs to the next label,
    blank line or heading."""
    texts: dict[str, list[str]] = {}
    current = None
    for line in body.split("\n"):
        stripped = line.strip()
        match = _STEELMAN.fullmatch(stripped)
        if match:
            current = match.group(1)
            texts.setdefault(current, []).append(match.group(2))
        elif not stripped or stripped.startswith("#"):
            current = None
        elif current is not None:
            texts[current].append(stripped)
    return {party: words(" ".join(lines)) for party, lines in texts.items()}


def symmetry_problem(body: str) -> str | None:
    counts = steelmen(body)
    missing = [party for party in "AB" if party not in counts]
    if missing:
        return f"no steelman for {' or '.join(missing)}"
    shorter, longer = sorted((counts["A"], counts["B"]))
    if shorter == 0 or longer > SYMMETRY * shorter:
        return (
            f"steelmen of {counts['A']} and {counts['B']} words: one is over 1.25 times the other"
        )
    return None


def quoted_spans(body: str) -> tuple[list[str], int]:
    """Every quoted span and the count of quotation marks without a partner.

    A span is text between double quotation marks, straight or curly, within a paragraph, or a
    blockquote other than the crux sentence, which is the skill's own words.
    """
    spans, unpaired = [], 0
    paragraph: list[str] = []
    block: list[str] = []
    previous = ""

    def close_paragraph() -> None:
        nonlocal unpaired
        marks = shared.fold(" ".join(paragraph)).split('"')
        spans.extend(marks[1::2])
        unpaired += 0 if len(marks) % 2 else 1
        paragraph.clear()

    def close_block() -> None:
        nonlocal previous
        if block:
            # The crux sentence follows its label, a blank line between or not; any other
            # blockquote quotes the input.
            if _CRUX_LABEL.fullmatch(previous):
                paragraph.extend(block)
            else:
                spans.append(shared.fold(" ".join(block)).strip('"'))
            block.clear()
            previous = ""

    for line in body.split("\n"):
        stripped = line.strip()
        if stripped.startswith(">"):
            block.append(stripped.lstrip("> \t"))
            continue
        close_block()
        if stripped:
            paragraph.append(stripped)
            previous = stripped
        else:
            close_paragraph()
    close_block()
    close_paragraph()
    return spans, unpaired


@dataclass
class Output:
    case: str
    name: str  # run-N or claude-ai
    path: str
    header: dict[str, str]
    report: bool
    quotes: bool
    symmetry: bool | None  # None for a question
    length: bool | None
    # The engine's verdict by grader, for a run; a claude.ai reply has none.
    verdicts: dict[str, bool] = field(default_factory=dict)
    review: dict[str, str] | None = None

    @property
    def number(self) -> int | None:
        match = _RUN.fullmatch(f"{self.name}.md")
        return int(match.group(1)) if match else None

    def passed(self, grader: str) -> bool:
        """The verdict as the owner's line in review.md has it, else as the engine gave it."""
        line = (self.review or {}).get(grader)
        if line in PASS_FAIL:
            return line == "pass"
        return self.verdicts.get(grader, False)

    def overruled(self) -> int:
        """The owner's lines that differ from the engine's verdict."""
        return sum(
            grader in (self.review or {}) and self.passed(grader) != passed
            for grader, passed in self.verdicts.items()
        )


@dataclass
class Report:
    problems: list[str] = field(default_factory=list)
    rows: list[shared.Row] = field(default_factory=list)
    smoke: shared.Row | None = None
    cases: int = 0
    runs: int = 0
    results: bool = False
    verdicts: int = 0
    overruled: int = 0

    @property
    def missed(self) -> list[str]:
        return [
            row.check for row in [*self.rows, *([self.smoke] if self.smoke else [])] if not row.met
        ]


def _by_commit(outputs: list["Output"]) -> dict[str, list[str]]:
    """The outputs' names by the commit each names; the runs of one cycle share one."""
    found: dict[str, list[str]] = {}
    for output in outputs:
        if output.header.get("commit"):
            found.setdefault(output.header["commit"], []).append(output.name)
    return found


def _snapshots(root: Path) -> Callable[[str], shared.Snapshot]:
    return shared.snapshots(root, EVALS)


def _added_in(root: Path) -> dict[str, str]:
    return shared.added_in(root, EVALS)


def _committed(root: Path) -> frozenset[str]:
    return shared.committed(root, EVALS)


def gold_order(
    root: Path,
    case: str,
    outputs: list[Output],
    present: list[str],
    snapshot: Callable[[str], shared.Snapshot],
    added: dict[str, str],
    committed: frozenset[str],
) -> list[str]:
    """Invariant 7, as `shared.gold_order` reckons it, over every output: the runs and the
    claude.ai reply."""
    return shared.gold_order(
        root, EVALS, case, _by_commit(outputs), present, snapshot, added, committed
    )


def case_as_run(
    root: Path, case: str, runs: list[Output], snapshot: Callable[[str], shared.Snapshot]
) -> list[str]:
    """Each run's prompt.md and graders unchanged since the commit it names. A claude.ai reply
    is older than every grader and not held to this."""
    return shared.case_as_run(root, EVALS, case, _by_commit(runs), snapshot)


def _gold_fields(root: Path, case: str) -> list[str]:
    path = f"{EVALS}/cases/{case}/gold.md"
    try:
        frontmatter, _ = shared.split_frontmatter((root / path).read_text(encoding="utf-8"))
    except OSError:
        return [f"{path}: missing"]
    except ValueError as error:
        return [f"{path}: {error}"]
    found = shared.fields(frontmatter)
    return [f"{path}: no {name}" for name in GOLD_FIELDS if not found.get(name)]


def _prompt(root: Path, case: str) -> tuple[str, list[str]]:
    """The prompt the runs were given, prompt.md's body: what quotes are checked against."""
    path = f"{EVALS}/cases/{case}/prompt.md"
    try:
        _, body = shared.split_frontmatter((root / path).read_text(encoding="utf-8"))
    except OSError:
        return "", [f"{path}: missing"]
    except ValueError as error:
        return "", [f"{path}: {error}"]
    if not body.strip():
        return "", [f"{path}: no prompt after its frontmatter"]
    return body, []


def _graders(root: Path, case: str) -> tuple[list[str], list[str]]:
    """The case's graders by name, each one a bar reads, and every case's three present."""
    where = f"{EVALS}/cases/{case}/graders"
    names = [name.removesuffix(".md") for name in shared.grader_files(root, EVALS, case)]
    problems = [f"{where}: no {name}.md" for name in REQUIRED_GRADERS if name not in names]
    problems += [
        f"{where}/{name}.md: a grader no bar reads" for name in names if name not in GRADERS
    ]
    return names, problems


def output_parts(text: str) -> tuple[str | None, str]:
    """A claude.ai reply's header and its reply. A leading block counts as a header only when it
    closes and holds `key: value` lines alone, so a reply that opens with a `---` rule stays
    whole."""
    try:
        header, body = shared.split_frontmatter(text)
    except ValueError:
        return None, text
    lines = [line for line in (header or "").split("\n") if line.strip()]
    if header is None or not all(_HEADER_LINE.fullmatch(line) for line in lines):
        return None, text
    return header, body


def _judge_reply(where: str, body: str, source: str) -> tuple[dict, list[str]]:
    """The deterministic checks on a reply: its quotes, and a report's symmetry and length."""
    problems = []
    spans, unpaired = quoted_spans(body)
    missing = [span for span in spans if not found_verbatim(span, source)]
    problems += [f'{where}: quote not in prompt.md: "{span}"' for span in missing]
    if unpaired:
        problems.append(f"{where}: a quotation mark without its partner")
    report = is_report(body)
    symmetry = length = None
    if report:
        why = symmetry_problem(body)
        symmetry = why is None
        if why:
            problems.append(f"{where}: {why}")
        count = report_words(body)
        length = count <= LENGTH
        if not length:
            problems.append(f"{where}: {count} words; a report is at most {LENGTH}")
    found = {
        "report": report,
        "quotes": not missing and not unpaired,
        "symmetry": symmetry,
        "length": length,
    }
    return found, problems


def _where(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def _read_claude_ai(root: Path, case: str, path: Path, source: str) -> tuple[Output, list[str]]:
    where = _where(root, path)
    problems = []
    try:
        header, body = output_parts(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        header, body = None, ""
        problems.append(f"{where}: cannot be read ({error})")
    found, judged = _judge_reply(where, body, source)
    output = Output(case, CLAUDE_AI, where, shared.fields(header), **found)
    return output, problems + judged


def _read_verdicts(
    root: Path, case: str, number: int, path: Path, graders: list[str]
) -> tuple[dict[str, bool], list[str]]:
    where = _where(root, path)
    if not path.exists():
        return {}, [f"{where}: missing; the runner writes it beside run-{number}.md"]
    try:
        header, verdicts = shared.read_verdicts(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        return {}, [f"{where}: cannot be read ({error})"]
    problems = []
    if header.get("case") != case or header.get("run") != str(number):
        problems.append(
            f"{where}: its header names case {header.get('case')!r}, run {header.get('run')!r}"
        )
    found: dict[str, bool] = {}
    for verdict in verdicts:
        if verdict.name in found:
            problems.append(f"{where}: a second verdict for {verdict.name}")
        found[verdict.name] = verdict.passed
    problems += [f"{where}: no verdict for {name}" for name in graders if name not in found]
    problems += [
        f"{where}: a verdict for {name}, which is not one of the case's graders"
        for name in found
        if name not in graders
    ]
    return found, problems


def _read_run(
    root: Path, case: str, number: int, path: Path, source: str, graders: list[str]
) -> tuple[Output, list[str]]:
    where = _where(root, path)
    problems = []
    try:
        run = shared.read_run(path.read_text(encoding="utf-8"))
        header, reply, read = run.header, run.reply, True
    except (OSError, ValueError) as error:
        header, reply, read = {}, "", False
        problems.append(f"{where}: cannot be read ({error})")
    found, judged = _judge_reply(where, reply, source)
    output = Output(case, f"run-{number}", where, header, **found)
    # A file that cannot be read has one problem, not one for each header field it lacks.
    if read and not header.get("commit"):
        problems.append(f"{where}: no commit in its header; the runner writes one")
    if read and (header.get("case") != case or header.get("run") != str(number)):
        problems.append(
            f"{where}: its header names case {header.get('case')!r}, run {header.get('run')!r}"
        )
    output.verdicts, more = _read_verdicts(
        root, case, number, path.with_name(f"verdicts-{number}.md"), graders
    )
    return output, problems + judged + more


def _run_review(where: str, output: Output, section: dict[str, str] | None) -> list[str]:
    """A run's section: stability from run 2 on, a line for every failed verdict, a note."""
    failed = [grader for grader, passed in output.verdicts.items() if not passed]
    number = output.number or 0
    if section is None:
        if number > 1:
            return [f"{where}: no section for {output.name}; it needs {STABILITY}"]
        if failed:
            return [f"{where}: no section for {output.name}, whose {', '.join(failed)} failed"]
        return []
    problems = []
    for key, value in section.items():
        if key == NOTE:
            continue
        if key == STABILITY:
            if number == 1:
                problems.append(f"{where}: run-1 has {STABILITY}")
            elif value not in YES_NO:
                problems.append(f"{where}: {output.name}'s {key} is {value!r}, not yes or no")
        elif key in output.verdicts:
            if value not in PASS_FAIL:
                problems.append(f"{where}: {output.name}'s {key} is {value!r}, not pass or fail")
        else:
            problems.append(f"{where}: {output.name} has {key}, not a field or one of its graders")
    if number > 1 and STABILITY not in section:
        problems.append(f"{where}: {output.name} has no {STABILITY}")
    problems += [
        f"{where}: {output.name}'s {grader} failed and has no line: fail confirms it, pass "
        "overrules it"
        for grader in failed
        if grader not in section
    ]
    if not section.get(NOTE):
        problems.append(f"{where}: {output.name} has no {NOTE}")
    return problems


def _claude_ai_review(where: str, output: Output, section: dict[str, str] | None) -> list[str]:
    """A claude.ai reply's section, the owner's judgement with round 1's fields."""
    if section is None:
        return [f"{where}: no section for {output.name}"]
    problems = []
    needed = [*CLAUDE_AI_REQUIRED, *([] if output.report else ["gate_fired"])]
    for key in needed:
        if not section.get(key):
            reason = "; it is a question, not a report" if key == "gate_fired" else ""
            problems.append(f"{where}: {output.name} has no {key}{reason}")
    for key, value in section.items():
        if key not in CLAUDE_AI_FIELDS:
            problems.append(f"{where}: {output.name} has {key}, not one of its fields")
        elif key != NOTE and value not in YES_NO:
            problems.append(f"{where}: {output.name}'s {key} is {value!r}, not yes or no")
    return problems


def _review(root: Path, case: str, outputs: list[Output]) -> list[str]:
    path = root / EVALS / "results" / case / "review.md"
    where = _where(root, path)
    if not path.exists():
        needs = [
            o for o in outputs if o.number is None or o.number > 1 or not all(o.verdicts.values())
        ]
        return [f"{where}: missing"] if needs else []
    sections, problems = shared.parse_review(path.read_text(encoding="utf-8"), where)
    names = {output.name for output in outputs}
    problems += [
        f"{where}: a section for {name}, which has no output"
        for name in sections
        if name not in names
    ]
    for output in outputs:
        section = sections.get(output.name)
        output.review = section
        if output.number is None:
            problems += _claude_ai_review(where, output, section)
        else:
            problems += _run_review(where, output, section)
    return problems


def _said(output: Output, key: str, value: str = "yes") -> bool:
    return bool(output.review) and output.review.get(key) == value


def _graded(check: str, runs: list[Output], grader: str) -> shared.Row:
    # Counted over the runs of the cases that have this grader, which must be at least one.
    graded = [run for run in runs if grader in run.verdicts]
    passed = sum(run.passed(grader) for run in graded)
    return shared.Row(
        check, "all runs with its grader", passed, len(graded), 0 < passed == len(graded)
    )


def _as_it_stands(root: Path, runs: list[Output]) -> int:
    commits = {run.header.get("commit") for run in runs} - {None, ""}
    current = {
        commit for commit in commits if shared.skill_unchanged_since(root, SKILL_FOLDER, commit)
    }
    return sum(run.header.get("commit") in current for run in runs)


def bars(root: Path, runs: list[Output], cases: dict[str, bool]) -> list[shared.Row]:
    """PDD B's pass bars over the cycle's runs, and decision 22's row."""
    by_case: dict[str, list[Output]] = {}
    for run in runs:
        by_case.setdefault(run.case, []).append(run)
    repeated = [outputs for outputs in by_case.values() if len(outputs) > 1]
    stable = sum(
        all(_said(run, STABILITY) for run in outputs if run.number != 1) for outputs in repeated
    )
    reports = [run for run in runs if run.report]
    return [
        shared.at_least(
            "Crux matches gold",
            Fraction(4, 5),
            sum(run.passed(CRUX) for run in runs),
            len(runs),
            "runs",
        ),
        shared.at_least(
            "Type matches gold",
            Fraction(9, 10),
            sum(run.passed(TYPE) for run in runs),
            len(runs),
            "runs",
        ),
        shared.at_least(
            "Stability: same primary crux in both runs",
            Fraction(4, 5),
            stable,
            len(repeated),
            "cases",
        ),
        shared.all_of("Quotes verbatim", sum(r.quotes for r in runs), len(runs), "runs"),
        shared.all_of(
            "Steelman symmetry", sum(bool(r.symmetry) for r in reports), len(reports), "reports"
        ),
        shared.all_of(
            f"Length ≤ {LENGTH} words",
            sum(bool(r.length) for r in reports),
            len(reports),
            "reports",
        ),
        shared.all_of(
            "No statement about people",
            sum(run.passed(PEOPLE) for run in runs),
            len(runs),
            "runs",
        ),
        _graded("One-sided gate fires", runs, GATE),
        _graded("No-conflict case reports no conflict or a Framing crux", runs, NO_CONFLICT),
        shared.all_of(
            "Gold order + approved_by + graders as run", sum(cases.values()), len(cases), "cases"
        ),
        shared.all_of(
            "Runs on the skill as it stands (decision 22)",
            _as_it_stands(root, runs),
            len(runs),
            "runs",
        ),
    ]


def smoke(outputs: list[Output]) -> shared.Row:
    """The claude.ai smoke test: three cases, each matching gold and passing every check."""
    passed = sum(
        _said(o, "crux_match")
        and _said(o, "type_match")
        and o.quotes
        and o.symmetry is not False
        and o.length is not False
        for o in outputs
    )
    return shared.Row(
        "claude.ai smoke test",
        f"{SMOKE_CASES} / {SMOKE_CASES} cases",
        passed,
        len(outputs),
        passed == len(outputs) == SMOKE_CASES,
    )


def _check_case(
    root: Path,
    case: str,
    report: Report,
    snapshot: Callable[[str], shared.Snapshot],
    added: dict[str, str],
    committed: frozenset[str],
) -> tuple[list[Output], list[Output], bool]:
    """One case's runs and claude.ai reply, its problems added to the report, and whether the
    case itself is sound: gold, its order, the prompt and the graders as each run had them."""
    source, problems = _prompt(root, case)
    graders, more = _graders(root, case)
    problems += more
    folder = root / EVALS / "results" / case
    # Every entry is read, so a result that is not a file is a problem rather than unseen.
    files = (
        sorted(p for p in folder.iterdir() if not p.name.startswith(".")) if folder.is_dir() else []
    )
    outputs = []
    numbers = {int(m.group(1)) for p in files if (m := _RUN.fullmatch(p.name))}
    for path in files:
        run, verdicts = _RUN.fullmatch(path.name), _VERDICTS.fullmatch(path.name)
        if run:
            output, found = _read_run(root, case, int(run.group(1)), path, source, graders)
            outputs.append(output)
            report.problems += found
        elif verdicts and int(verdicts.group(1)) not in numbers:
            report.problems.append(f"{_where(root, path)}: no run-{verdicts.group(1)}.md beside it")
        elif path.name == "claude-ai.md":
            output, found = _read_claude_ai(root, case, path, source)
            outputs.append(output)
            report.problems += found
    outputs.sort(key=lambda o: (o.number is None, o.number or 0))
    report.problems += _review(root, case, outputs)
    runs = [o for o in outputs if o.number is not None]
    present = [_where(root, path) for path in files if path.is_file()]
    problems += _gold_fields(root, case)
    problems += gold_order(root, case, outputs, present, snapshot, added, committed)
    problems += case_as_run(root, case, runs, snapshot)
    report.problems += problems
    return runs, [o for o in outputs if o.number is None], not problems


def check(root: Path) -> Report:
    report = Report()
    cases_folder, results_folder = root / EVALS / "cases", root / EVALS / "results"
    ids = (
        sorted(p.name for p in cases_folder.iterdir() if p.is_dir() and not p.name.startswith("."))
        if cases_folder.is_dir()
        else []
    )
    report.cases = len(ids)
    if results_folder.is_dir():
        report.problems += [
            f"{EVALS}/results/{p.name}: results for a case that does not exist"
            for p in sorted(results_folder.iterdir())
            if p.is_dir() and not p.name.startswith(".") and p.name not in ids
        ]
    runs: list[Output] = []
    claude_ai: list[Output] = []
    sound: dict[str, bool] = {}
    snapshot, added, committed = _snapshots(root), _added_in(root), _committed(root)
    for case in ids:
        case_runs, case_claude_ai, sound[case] = _check_case(
            root, case, report, snapshot, added, committed
        )
        runs += case_runs
        claude_ai += case_claude_ai
    report.runs = len(runs)
    report.results = bool(runs or claude_ai)
    if runs:
        highest = max(run.number or 0 for run in runs)
        present = {(run.case, run.number) for run in runs}
        report.problems += [
            f"{EVALS}/results/{case}/run-{number}.md: missing"
            for case in ids
            for number in range(1, highest + 1)
            if (case, number) not in present
        ]
        report.rows = bars(root, runs, sound)
        report.verdicts = sum(len(run.verdicts) for run in runs)
        report.overruled = sum(run.overruled() for run in runs)
    if claude_ai:
        report.smoke = smoke(claude_ai)
    return report


def state(report: Report) -> str:
    if not report.cases:
        return "no cases yet"
    if not report.results:
        return "no results yet, so the pass bars are not counted"
    if report.missed:
        met = f"pass bars not met: {', '.join(report.missed)}"
    elif report.runs:
        met = "every pass bar met"
    else:
        met = "the claude.ai smoke test met"
    if not report.runs:
        return f"no cycle yet, so the cycle's bars are not counted; {met}"
    return met


def main() -> int:
    report = check(ROOT)
    for problem in report.problems:
        print(problem)
    if report.rows:
        print()
        print(shared.table(report.rows))
        print()
        print(f"Verdicts the owner overruled: {report.overruled} of {report.verdicts}")
    if report.smoke:
        print()
        print(shared.table([report.smoke]))
    print(f"checks: {report.cases} case(s), {len(report.problems)} problem(s); {state(report)}")
    return 1 if report.problems or report.missed else 0


if __name__ == "__main__":
    sys.exit(main())
