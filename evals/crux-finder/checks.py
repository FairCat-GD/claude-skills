"""crux-finder's deterministic checks, and the summary table against PDD B's pass bars.

For every case: gold.md names who approved it, and is committed before any of its results and
unchanged since (invariant 7). For every output, run-N.md and claude-ai.md: every quoted span
is in input.md, and a report's steelmen are balanced and its length is within 400 words. Then
review.md, the owner's judgement of each output, is read, and the bars are counted. This script
may read gold.md; only run.py and the session under test may not.

Usage: uv run evals/crux-finder/checks.py
"""

import re
import subprocess
import sys
from dataclasses import dataclass, field
from fractions import Fraction
from math import ceil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
# Relative to the root, as git names them.
EVALS = "evals/crux-finder"
SKILL_FOLDER = "plugins/crux-finder/skills/crux-finder"
LENGTH = 400
# Each steelman within 25% of the other: the longer at most 5/4 of the shorter.
SYMMETRY = Fraction(5, 4)
GOLD_FIELDS = ("crux", "type", "crux_for", "approved_by")
YES_NO = ("yes", "no")
REQUIRED = ("crux_match", "type_match", "people_statement", "note")
OPTIONAL = ("gate_fired", "no_conflict_reported")
STABILITY = "same_crux_as_run_1"
FIELDS = (*REQUIRED, STABILITY, *OPTIONAL)
SMOKE_CASES = 3

_RUN = re.compile(r"run-([1-9][0-9]*)\.md")
# A `version:` key indented under `metadata:`, with any value, quoted or not.
_VERSION = re.compile(r"[ \t]+version:[ \t]*\S.*")
_REPORT = re.compile(r"^## Crux report[ \t]*$", re.MULTILINE)
_STEELMAN = re.compile(r"\*\*([AB])(?: \([^)\n]*\))?, strongest form:\*\*[ \t]*(.*)")
_CRUX_LABEL = re.compile(r"\*\*(?:(?:Double crux|Crux for [AB]) · [^*\n]+|No crux)\*\*")
_HEADING = re.compile(r"#{1,3}\s")
_CLAIM_MAP = re.compile(r"###\s+Claim map\s*")
_FIELD = re.compile(r"- ([a-z0-9_]+):[ \t]*(.*)")
_HEADER_LINE = re.compile(r"[a-z0-9_]+:.*")
_ELLIPSIS = re.compile(r"…|\.\.\.")
# Typographic quotation marks and apostrophes read as their plain forms: the double ones
# (curly, low, reversed, double prime) as ", the single ones as '.
_DOUBLE = "\u201c\u201d\u201e\u201f\u2033"
_SINGLE = "\u2018\u2019\u201a\u201b\u2032"
_FOLD = str.maketrans(dict.fromkeys(_DOUBLE, '"') | dict.fromkeys(_SINGLE, "'"))


def split_frontmatter(text: str) -> tuple[str | None, str]:
    """The frontmatter's lines and the body; no frontmatter gives None and the whole text."""
    lines = text.split("\n")
    if lines[0].rstrip() != "---":
        return None, text
    for index, line in enumerate(lines[1:], start=1):
        if line.rstrip() == "---":
            return "\n".join(lines[1:index]), "\n".join(lines[index + 1 :])
    raise ValueError("its frontmatter has no closing ---")


def fields(frontmatter: str | None) -> dict[str, str]:
    """One `key: value` per line, a quoted value unquoted; the format gold.md and run.py use."""
    found = {}
    for line in (frontmatter or "").split("\n"):
        key, colon, value = line.partition(":")
        if colon and key.strip() and not line[:1].isspace():
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
                value = value[1:-1]
            found[key.strip()] = value
    return found


def words(text: str) -> int:
    """A word is a whitespace-separated token with a letter or digit; markup alone is none."""
    return sum(1 for token in text.split() if any(ch.isalnum() for ch in token))


def is_report(body: str) -> bool:
    """A reply without the report's heading is a question, judged by gate_fired."""
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


def _fold(text: str) -> str:
    return " ".join(text.translate(_FOLD).split())


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
        marks = _fold(" ".join(paragraph)).split('"')
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
                spans.append(_fold(" ".join(block)).strip('"'))
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


def found_verbatim(span: str, source: str) -> bool:
    """Whether the span is in the source, line breaks joined and quotation marks folded; with an
    ellipsis, piece by piece, in order. A mark that ends the sentence inside the closing
    quotation mark is not part of the quote."""
    pieces = [piece.strip() for piece in _ELLIPSIS.split(_fold(span))]
    pieces = [piece for piece in pieces if piece]
    if pieces:
        pieces[-1] = pieces[-1].rstrip(".,;:!?") or pieces[-1]
    text, position = _fold(source), 0
    for piece in pieces:
        index = text.find(piece, position)
        if index < 0:
            return False
        position = index + len(piece)
    return True


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
    review: dict[str, str] | None = None

    @property
    def number(self) -> int | None:
        match = _RUN.fullmatch(f"{self.name}.md")
        return int(match.group(1)) if match else None


@dataclass
class Row:
    check: str
    bar: str
    passed: int
    total: int
    met: bool


@dataclass
class Report:
    problems: list[str] = field(default_factory=list)
    rows: list[Row] = field(default_factory=list)
    smoke: Row | None = None
    cases: int = 0
    results: bool = False

    @property
    def bars_met(self) -> bool:
        return all(row.met for row in self.rows) and (self.smoke is None or self.smoke.met)


def _git(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, stdin=subprocess.DEVNULL
    )


def _unchanged_since(root: Path, commit: str, path: str) -> bool:
    """Whether the path, in the working tree, is as it was in the commit."""
    return _git(root, "diff", "--quiet", commit, "--", path).returncode == 0


def without_version(text: str) -> str:
    """SKILL.md with its frontmatter's metadata.version line left out, the one line of the skill
    folder a release changes; a text with no such line is returned as it is."""
    lines = text.split("\n")
    if lines[0].rstrip() != "---":
        return text
    in_metadata = False
    for index, line in enumerate(lines[1:], start=1):
        bare = line.rstrip("\r")
        if bare.rstrip() == "---":
            break
        if bare[:1] and not bare[:1].isspace():
            in_metadata = bare.rstrip() == "metadata:"
        elif in_metadata and _VERSION.fullmatch(bare):
            return "\n".join(lines[:index] + lines[index + 1 :])
    return text


def _skill_unchanged_since(root: Path, commit: str) -> bool:
    """Whether the skill folder, in the working tree, is as it was in the commit, SKILL.md's
    metadata.version aside: a change to it alone is a release, not a change to the skill, so a
    run on the commit before it ran the skill as it stands."""
    skill = f"{SKILL_FOLDER}/SKILL.md"
    rest = _git(root, "diff", "--quiet", commit, "--", SKILL_FOLDER, f":(exclude){skill}")
    then = _git(root, "show", f"{commit}:{skill}")
    try:
        now = (root / skill).read_text(encoding="utf-8")
    except OSError:
        return False
    return (
        rest.returncode == 0
        and then.returncode == 0
        and without_version(then.stdout) == without_version(now)
    )


def _in_commit(root: Path, commit: str, path: str) -> bool:
    return _git(root, "cat-file", "-e", f"{commit}:{path}").returncode == 0


def gold_order(root: Path, case: str, outputs: list[Output], results_exist: bool) -> list[str]:
    """Invariant 7: gold.md committed before any of its results, and unchanged since."""
    gold = f"{EVALS}/cases/{case}/gold.md"
    if not _git(root, "log", "--format=%H", "--", gold).stdout.split():
        return [f"{gold}: not committed"]
    problems = []
    first = _git(root, "log", "--format=%H", "--", f"{EVALS}/results/{case}").stdout.split()
    if first:
        parent = _git(root, "rev-parse", "--verify", "--quiet", f"{first[-1]}^").stdout.strip()
        if not parent or not _in_commit(root, parent, gold):
            problems.append(f"{gold}: not committed before the first commit of its results")
        elif not _unchanged_since(root, parent, gold):
            problems.append(f"{gold}: changed since its results were first committed")
    # The runs of one cycle share a commit, so each commit is asked about once.
    ran_on: dict[str, list[str]] = {}
    for output in outputs:
        if output.header.get("commit"):
            ran_on.setdefault(output.header["commit"], []).append(output.name)
    for commit, names in ran_on.items():
        which = f"which {', '.join(names)} ran on"
        if not _in_commit(root, commit, gold):
            problems.append(f"{gold}: not in commit {commit[:12]}, {which}")
        elif not _unchanged_since(root, commit, gold):
            problems.append(f"{gold}: changed since commit {commit[:12]}, {which}")
    if results_exist and not _unchanged_since(root, "HEAD", gold):
        problems.append(f"{gold}: uncommitted changes while results exist")
    return problems


def _gold_fields(root: Path, case: str) -> list[str]:
    path = f"{EVALS}/cases/{case}/gold.md"
    try:
        frontmatter, _ = split_frontmatter((root / path).read_text(encoding="utf-8"))
    except OSError:
        return [f"{path}: missing"]
    except ValueError as error:
        return [f"{path}: {error}"]
    found = fields(frontmatter)
    return [f"{path}: no {name}" for name in GOLD_FIELDS if not found.get(name)]


def output_parts(text: str) -> tuple[str | None, str]:
    """An output's header and its reply. A leading block counts as a header only when it closes
    and holds `key: value` lines alone, so a reply that opens with a `---` rule stays whole."""
    try:
        header, body = split_frontmatter(text)
    except ValueError:
        return None, text
    lines = [line for line in (header or "").split("\n") if line.strip()]
    if header is None or not all(_HEADER_LINE.fullmatch(line) for line in lines):
        return None, text
    return header, body


def _read_output(root: Path, case: str, path: Path, source: str) -> tuple[Output, list[str]]:
    where = path.relative_to(root).as_posix()
    problems = []
    try:
        header, body = output_parts(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        header, body = None, ""
        problems.append(f"{where}: cannot be read ({error})")
    spans, unpaired = quoted_spans(body)
    missing = [span for span in spans if not found_verbatim(span, source)]
    problems += [f'{where}: quote not in input.md: "{span}"' for span in missing]
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
    output = Output(
        case=case,
        name=path.stem,
        path=where,
        header=fields(header),
        report=report,
        quotes=not missing and not unpaired,
        symmetry=symmetry,
        length=length,
    )
    if output.number is not None and not output.header.get("commit"):
        problems.append(f"{where}: no commit in its header; run.py writes one")
    return output, problems


def parse_review(text: str, where: str) -> tuple[dict[str, dict[str, str]], list[str]]:
    """review.md: `# Review: <id>`, then a `## run-N` or `## claude-ai` section per output, each
    of `- field: value` lines."""
    sections: dict[str, dict[str, str]] = {}
    problems = []
    current = None
    for number, line in enumerate(text.split("\n"), start=1):
        stripped = line.strip()
        if not stripped or (stripped.startswith("# ") and current is None):
            continue
        if stripped.startswith("## "):
            name = stripped[3:].strip()
            if name in sections:
                problems.append(f"{where}:{number}: a second section for {name}")
            current = sections.setdefault(name, {})
            continue
        match = _FIELD.fullmatch(stripped)
        if current is None or not match:
            problems.append(f"{where}:{number}: not a `- field: value` line in a run's section")
            continue
        key, value = match.groups()
        if key not in FIELDS:
            problems.append(f"{where}:{number}: unknown field {key}")
        elif key in current:
            problems.append(f"{where}:{number}: {key} given twice")
        else:
            current[key] = value.strip()
    return sections, problems


def _review_problems(where: str, output: Output, review: dict[str, str]) -> list[str]:
    problems = []
    needed = [*REQUIRED]
    if output.number is not None and output.number > 1:
        needed.append(STABILITY)
    if not output.report:
        needed.append("gate_fired")
    for key in needed:
        if not review.get(key):
            reason = "; it is a question, not a report" if key == "gate_fired" else ""
            problems.append(f"{where}: {output.name} has no {key}{reason}")
    for key, value in review.items():
        if key != "note" and value not in YES_NO:
            problems.append(f"{where}: {output.name}'s {key} is {value!r}, not yes or no")
    if output.number == 1 and STABILITY in review:
        problems.append(f"{where}: run-1 has {STABILITY}")
    return problems


def _review(root: Path, case: str, outputs: list[Output]) -> list[str]:
    path = root / EVALS / "results" / case / "review.md"
    where = path.relative_to(root).as_posix()
    if not path.exists():
        return [f"{where}: missing"] if outputs else []
    sections, problems = parse_review(path.read_text(encoding="utf-8"), where)
    names = {output.name for output in outputs}
    problems += [
        f"{where}: a section for {name}, which has no output"
        for name in sections
        if name not in names
    ]
    for output in outputs:
        review = sections.get(output.name)
        if review is None:
            problems.append(f"{where}: no section for {output.name}")
            continue
        output.review = review
        problems += _review_problems(where, output, review)
    for key in OPTIONAL:
        recorded = [output.name for output in outputs if output.review and key in output.review]
        if recorded and len(recorded) != len(outputs):
            problems.append(f"{where}: {key} is recorded for some of this case's outputs, not all")
    return problems


def _said(output: Output, key: str, value: str = "yes") -> bool:
    return bool(output.review) and output.review.get(key) == value


def _all(check: str, passed: int, total: int, unit: str) -> Row:
    return Row(check, f"all {unit}", passed, total, passed == total)


def _ratio(check: str, ratio: Fraction, passed: int, total: int, unit: str) -> Row:
    need = ceil(ratio * total)
    return Row(check, f"≥ {need} / {total} {unit}", passed, total, total > 0 and passed >= need)


def _recorded(check: str, runs: list[Output], key: str) -> Row:
    # Counted over the runs whose review records the field, which must be at least one.
    recorded = [run for run in runs if run.review and key in run.review]
    passed = sum(_said(run, key) for run in recorded)
    return Row(check, "all runs that record it", passed, len(recorded), 0 < passed == len(recorded))


def _as_it_stands(root: Path, runs: list[Output]) -> int:
    commits = {run.header.get("commit") for run in runs} - {None, ""}
    current = {commit for commit in commits if _skill_unchanged_since(root, commit)}
    return sum(run.header.get("commit") in current for run in runs)


def bars(root: Path, runs: list[Output], cases: dict[str, bool]) -> list[Row]:
    """PDD B's pass bars over the cycle's run-N outputs, and decision 22's row."""
    by_case: dict[str, list[Output]] = {}
    for run in runs:
        by_case.setdefault(run.case, []).append(run)
    repeated = [outputs for outputs in by_case.values() if len(outputs) > 1]
    stable = sum(
        all(_said(run, STABILITY) for run in outputs if run.number != 1) for outputs in repeated
    )
    reports = [run for run in runs if run.report]
    return [
        _ratio(
            "Crux matches gold",
            Fraction(4, 5),
            sum(_said(r, "crux_match") for r in runs),
            len(runs),
            "runs",
        ),
        _ratio(
            "Type matches gold",
            Fraction(9, 10),
            sum(_said(r, "type_match") for r in runs),
            len(runs),
            "runs",
        ),
        _ratio(
            "Stability: same primary crux in both runs",
            Fraction(4, 5),
            stable,
            len(repeated),
            "cases",
        ),
        _all("Quotes verbatim", sum(r.quotes for r in runs), len(runs), "runs"),
        _all("Steelman symmetry", sum(bool(r.symmetry) for r in reports), len(reports), "reports"),
        _all(
            f"Length ≤ {LENGTH} words",
            sum(bool(r.length) for r in reports),
            len(reports),
            "reports",
        ),
        _all(
            "people_statement no",
            sum(_said(r, "people_statement", "no") for r in runs),
            len(runs),
            "runs",
        ),
        _recorded("One-sided gate fires", runs, "gate_fired"),
        _recorded(
            "No-conflict case reports no conflict or a Framing crux", runs, "no_conflict_reported"
        ),
        _all("Gold order + approved_by", sum(cases.values()), len(cases), "cases"),
        _all(
            "Runs on the skill as it stands (decision 22)",
            _as_it_stands(root, runs),
            len(runs),
            "runs",
        ),
    ]


def smoke(outputs: list[Output]) -> Row:
    """The claude.ai smoke test: three cases, each matching gold and passing every check."""
    passed = sum(
        _said(o, "crux_match")
        and _said(o, "type_match")
        and o.quotes
        and o.symmetry is not False
        and o.length is not False
        for o in outputs
    )
    return Row(
        "claude.ai smoke test",
        f"{SMOKE_CASES} / {SMOKE_CASES} cases",
        passed,
        len(outputs),
        passed == len(outputs) == SMOKE_CASES,
    )


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
    for case in ids:
        source_path = cases_folder / case / "input.md"
        try:
            _, source = split_frontmatter(source_path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            source = ""
            report.problems.append(f"{EVALS}/cases/{case}/input.md: {error}")
        folder = results_folder / case
        files = sorted(folder.iterdir()) if folder.is_dir() else []
        outputs = []
        for path in files:
            if _RUN.fullmatch(path.name) or path.name == "claude-ai.md":
                output, problems = _read_output(root, case, path, source)
                outputs.append(output)
                report.problems += problems
        outputs.sort(key=lambda o: (o.number is None, o.number or 0))
        report.problems += _review(root, case, outputs)
        case_problems = _gold_fields(root, case) + gold_order(root, case, outputs, bool(files))
        report.problems += case_problems
        sound[case] = not case_problems
        runs += [o for o in outputs if o.number is not None]
        claude_ai += [o for o in outputs if o.number is None]
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
    if claude_ai:
        report.smoke = smoke(claude_ai)
    return report


def table(rows: list[Row]) -> str:
    lines = ["| Check | Pass bar | Result | Met |", "|---|---|---|---|"]
    for row in rows:
        met = "yes" if row.met else "**no**"
        lines.append(f"| {row.check} | {row.bar} | {row.passed} / {row.total} | {met} |")
    return "\n".join(lines)


def main() -> int:
    report = check(ROOT)
    for problem in report.problems:
        print(problem)
    if report.rows:
        print()
        print(table(report.rows))
    if report.smoke:
        print()
        print(table([report.smoke]))
    if not report.cases:
        state = "no cases yet"
    elif not report.results:
        state = "no results yet, so the pass bars are not counted"
    else:
        missed = [
            row.check
            for row in report.rows + ([report.smoke] if report.smoke else [])
            if not row.met
        ]
        state = "every pass bar met" if not missed else f"pass bars not met: {', '.join(missed)}"
    print(f"checks: {report.cases} case(s), {len(report.problems)} problem(s); {state}")
    return 1 if report.problems or (report.results and not report.bars_met) else 0


if __name__ == "__main__":
    sys.exit(main())
