"""provenance-tracer's checks on the shared runner's results, and the summary table against the
pass bars.

For every case: prompt.md holds the prompt, graders/ the graders the bars read, and gold.md its
fields, names who approved it and is committed before any of its results present now, and
unchanged since (invariant 7). For every run, `run-N.md` and `verdicts-N.md` as `evals/run.py`
writes them: the case's prompt.md and graders as they were in the run's commit; each quote under
15 words, one to a line and one to a source; every source a forward report's chain links, or a
reverse report's source line and popular versions, among the run's fetches; each `tool_used`
grader's range held by the run's calls as run-N.md lists them. review.md holds the owner's lines:
run 1 read in every case, and a line for every failed verdict, confirming or overruling it.

A case passes when 2 of its 3 runs pass both `labels`, where it has them, and `facts`; every
other bar holds on every run. The bars count each verdict as the owner's line has it, else as the
engine gave it. A run the engine graded is counted as graded, an error in its header included,
since that is the skill's result. This script may read gold.md; only the runner and the session
under test may not.

Usage: uv run evals/provenance-tracer/checks.py
"""

import re
import sys
from collections.abc import Callable
from dataclasses import dataclass, field
from fractions import Fraction
from math import ceil
from pathlib import Path
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import shared

ROOT = Path(__file__).resolve().parent.parent.parent
# Relative to the root, as git names them.
EVALS = "evals/provenance-tracer"
SKILL_FOLDER = "plugins/provenance-tracer/skills/provenance-tracer"
# Each case runs three times and passes at two of them (the spec's *Evals*).
RUNS = 3
CASE_PASS = Fraction(2, 3)
# A quote is under this many words (the spec's *Guardrails*).
QUOTE_WORDS = 15
GOLD_FIELDS = ("roots", "grounding", "modifiers", "authored", "approved_by")
NONE = "none"
PASS_FAIL = ("pass", "fail")
NOTE = "note"
# The graders, by the file name each bar reads.
LABELS = "labels"
FACTS = "facts"
NO_VERDICT = "no-verdict"
FOOTER = "footer"
NO_SEARCH = "no-search"
NO_FETCH = "no-fetch"
MANAGER = "manager-not-searched"
REQUIRED_GRADERS = (FACTS, NO_VERDICT)
GRADERS = (LABELS, FACTS, NO_VERDICT, FOOTER, NO_SEARCH, NO_FETCH, MANAGER)
# The graders a run must pass to count towards its case passing, where the case has them.
PER_CASE = (LABELS, FACTS)
TOOL_USED = "tool_used"
FETCH = "WebFetch"
REVIEW = "review.md"
# The report kind of a run whose file cannot be read.
UNREAD = "unreadable"

_RUN = re.compile(r"run-([1-9][0-9]*)\.md")
_VERDICTS = re.compile(r"verdicts-([1-9][0-9]*)\.md")
_DATE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")
_NUMBERED = re.compile(r"(fact|source|must)_([1-9][0-9]*)")
_HEADING = re.compile(r"\s*#{1,6}\s+(.*)")
# A line that is bold and nothing else, as a section heading may be written; it is one only
# when it names a section of the skill's templates, so a bold label inside a chain is not.
_BOLD_HEADING = re.compile(r"\s*\*\*([^*\n]+?):?\*\*:?\s*")
SECTIONS = (
    "chain",
    "how it changed",
    "status of the root",
    "cold trails",
    "confidence",
    "status",
    "what it found",
    "popular versions",
    "your beliefs",
)
_PROVENANCE = re.compile(r"\s*##\s+Provenance:(.*)")
# The label line in any markup: Roots, then Grounding, on one line; the count line has no Grounding.
_LABEL_LINE = re.compile(r"\bRoots\b[^\n]*\bGrounding\b")
_SOURCE_LINE = re.compile(r"\*\*Source:\*\*")
_LINK_TEXT = re.compile(r"!?\[(?:[^\[\]]|\[[^\[\]]*\])*\]\(")
_AUTOLINK = re.compile(r"<(https?://[^\s<>]+)>")
_BARE = re.compile(r"https?://[^\s<>|\"\u201c\u201d]+")
_ESCAPE = re.compile(r"\\([!-/:-@\[-`{-~])")
# A link after these words names where a fact was found, not the source a quote is from.
_NOT_THE_SOURCE = re.compile(r"(?:\bper|\bcited by)[\s*_(]*$", re.IGNORECASE)
_EDGES = ".,;:!?\u2026 "


# --- Links ------------------------------------------------------------------------------------


@dataclass(frozen=True)
class Link:
    url: str
    # Whether the words before it make it where a fact was found rather than a quote's source.
    attribution: bool


def normalise(url: str) -> str:
    """A URL as the comparison reads it: angle brackets and Markdown escapes removed, the fragment
    dropped, then percent-decoded. Otherwise as written, since the skill links a page exactly as
    it passed it to the fetch tool."""
    url = _ESCAPE.sub(r"\1", url.strip().removeprefix("<").removesuffix(">"))
    return unquote(url.split("#", 1)[0])


def _trim(url: str) -> str:
    """A bare URL without the punctuation after it, or a closing bracket it does not open."""
    while url:
        if url[-1] in ".,;:!?*'":
            url = url[:-1]
        elif url[-1] == ")" and url.count("(") < url.count(")"):
            url = url[:-1]
        elif url[-1] == "]" and url.count("[") < url.count("]"):
            url = url[:-1]
        else:
            break
    return url


def _destination(line: str, start: int) -> tuple[str, int]:
    """An inline link's destination, from just after its `(`, and where the link ends: balanced
    parentheses are part of it, and a title after it is dropped."""
    index = start
    while index < len(line) and line[index] in " \t":
        index += 1
    if index < len(line) and line[index] == "<":
        close = line.find(">", index)
        if close < 0:
            return "", len(line)
        url, index = line[index + 1 : close], close + 1
    else:
        depth, begin = 0, index
        while index < len(line):
            char = line[index]
            if char == "\\" and index + 1 < len(line):
                index += 2
                continue
            if char == "(":
                depth += 1
            elif char == ")":
                if depth == 0:
                    break
                depth -= 1
            elif char in " \t":
                break
            index += 1
        url = line[begin:index]
    # Past any title, to the link's closing parenthesis.
    depth = 0
    while index < len(line):
        if line[index] == "(":
            depth += 1
        elif line[index] == ")":
            if depth == 0:
                return url, index + 1
            depth -= 1
        index += 1
    return url, len(line)


def links(line: str) -> tuple[list[Link], str]:
    """Every link on a line, inline, autolink or bare, and the line with each URL taken out, so a
    quotation mark inside a URL is never read as a quote's."""
    found: list[Link] = []
    kept: list[str] = []
    position = 0
    for match in _LINK_TEXT.finditer(line):
        if match.start() < position:
            continue
        url, end = _destination(line, match.end())
        before = line[: match.start()]
        kept.append(line[position : match.end() - 1])
        found.append(Link(url, _NOT_THE_SOURCE.search(before) is not None))
        position = end
    kept.append(line[position:])
    rest = "".join(kept)

    def take(match: re.Match[str], bare: bool) -> str:
        url = _trim(match.group(0)) if bare else match.group(1)
        before = rest[: match.start()]
        found.append(Link(url, _NOT_THE_SOURCE.search(before) is not None))
        return match.group(0)[len(url) :] if bare else ""

    rest = _AUTOLINK.sub(lambda m: take(m, bare=False), rest)
    rest = _BARE.sub(lambda m: take(m, bare=True), rest)
    return found, rest


# --- The reply's parts ------------------------------------------------------------------------


def _heading(line: str) -> str | None:
    """A line's section name, if it is a heading: `#`s, or bold and nothing else naming one of the
    templates' sections."""
    match = _HEADING.fullmatch(line)
    if match:
        return match.group(1).strip().rstrip(":").strip()
    match = _BOLD_HEADING.fullmatch(line)
    name = match.group(1).strip().rstrip(":").strip() if match else None
    return name if name and name.casefold() in SECTIONS else None


def kind(body: str) -> str | None:
    """`forward` or `reverse` for a report, None for a refusal or a question."""
    lines = body.split("\n")
    if any(_LABEL_LINE.search(line) for line in lines) or section(body, "Chain") is not None:
        return "forward"
    for line in lines:
        match = _PROVENANCE.fullmatch(line)
        if match:
            rest = shared.fold(match.group(1)).strip()
            return "forward" if rest.startswith('"') else "reverse"
    return "reverse" if any(_SOURCE_LINE.search(line) for line in lines) else None


def section(body: str, name: str) -> list[str] | None:
    """The lines under the heading of that name, up to the next heading; None with no such
    heading."""
    lines, inside, found = [], False, False
    for line in body.split("\n"):
        heading = _heading(line)
        if heading is not None:
            inside = heading.casefold() == name.casefold()
            found = found or inside
            continue
        if inside:
            lines.append(line)
    return lines if found else None


def linked_lines(body: str, report: str | None) -> list[str] | None:
    """The lines whose links must be among the run's fetches: a forward report's chain, a reverse
    report's source line and popular versions. None for a forward report with no chain."""
    if report == "forward":
        return section(body, "Chain")
    if report == "reverse":
        sources = [line for line in body.split("\n") if _SOURCE_LINE.search(line)]
        return sources + (section(body, "Popular versions") or [])
    return []


def unfetched(body: str, report: str | None, fetched: set[str]) -> list[str] | None:
    """Every link a report must have fetched and did not; None for a forward report with no chain
    section, which this cannot check."""
    lines = linked_lines(body, report)
    if lines is None:
        return None
    missing: list[str] = []
    for line in lines:
        for link in links(line)[0]:
            if normalise(link.url) not in fetched and link.url not in missing:
                missing.append(link.url)
    return missing


# --- Quotes -----------------------------------------------------------------------------------


@dataclass(frozen=True)
class Quote:
    text: str
    line: int
    # The one source the line links, normalised; None where it links none or several.
    source: str | None
    # Whether it is under *How it changed*, whose link is a drift's node, not the quote's source.
    in_changes: bool


def _key(span: str) -> str:
    return shared.fold(span).casefold().strip(_EDGES)


def _same(a: str, b: str) -> bool:
    """Two quotes are the same when one holds the other, letter case and end marks aside."""
    first, second = _key(a), _key(b)
    return first in second or second in first


def _distinct(spans: list[str]) -> list[str]:
    kept: list[str] = []
    for span in spans:
        if not any(_same(span, other) for other in kept):
            kept.append(span)
    return kept


def quotes(body: str) -> tuple[list[Quote], list[int], str]:
    """Every quote in the reply, the lines with an unpaired quotation mark, and the heading's
    claim. A quote is text between double quotation marks on one line, URLs taken out first, or
    a blockquote. The heading's line and the *Your version* line are the user's claim and are
    not read."""
    found: list[Quote] = []
    unpaired: list[int] = []
    claim = ""
    current = ""
    block: list[tuple[int, str]] = []

    def source_of(line_links: list[Link]) -> str | None:
        sources = {normalise(link.url) for link in line_links if not link.attribution}
        return sources.pop() if len(sources) == 1 else None

    def close_block() -> None:
        if block:
            texts, block_links = [], []
            for _, line in block:
                line_links, rest = links(line)
                texts.append(rest)
                block_links += line_links
            text = shared.fold(" ".join(texts)).strip().strip('"').strip()
            if text:
                changes = current.casefold() == "how it changed"
                found.append(Quote(text, block[0][0], source_of(block_links), changes))
            block.clear()

    for number, line in enumerate(body.split("\n"), start=1):
        stripped = line.strip()
        if stripped.startswith(">"):
            block.append((number, stripped.lstrip("> \t")))
            continue
        close_block()
        heading = _PROVENANCE.fullmatch(line)
        if heading:
            claim = heading.group(1)
            continue
        name = _heading(line)
        if name is not None:
            current = name
            continue
        if "Your version:" in stripped.replace("*", "").replace("_", ""):
            continue
        line_links, rest = links(line)
        marks = shared.fold(rest).split('"')
        if len(marks) % 2 == 0:
            unpaired.append(number)
            continue
        changes = current.casefold() == "how it changed"
        source = source_of(line_links)
        found += [Quote(span, number, source, changes) for span in marks[1::2]]
    close_block()
    return found, unpaired, claim


def claims(prompt: str, heading: str) -> list[str]:
    """The user's claims: each span the prompt quotes, or the whole prompt where it quotes none,
    and the claim as the heading restates it."""
    spans = [span for span in shared.fold(prompt).split('"')[1::2] if span.strip()]
    found = spans or [prompt]
    restated = shared.fold(heading).strip().strip('"').strip()
    return found + ([restated] if restated else [])


def users_text(span: str, prompt: str, heading: str) -> bool:
    """Whether a quote is the user's own text: found in one of their claims, letter case aside.
    A fragment counts, since *How it changed* sets the user's words against the root's; the
    prompt's request line does not, since it is no claim."""
    folded = span.casefold()
    return any(shared.found_verbatim(folded, claim.casefold()) for claim in claims(prompt, heading))


def quote_problems(body: str, prompt: str) -> list[str]:
    """The quote rule: each quote under 15 words, one to a line, and one to a source across the
    lines that link it alone, *How it changed* aside. The user's own text is exempt."""
    found, unpaired, claim = quotes(body)
    problems = [f"line {number}: a quotation mark without its partner" for number in unpaired]
    kept = [q for q in found if _key(q.text) and not users_text(q.text, prompt, claim)]
    for quote in kept:
        count = shared.words(quote.text)
        if count >= QUOTE_WORDS:
            problems.append(
                f"line {quote.line}: a quote of {count} words, at most {QUOTE_WORDS - 1}: "
                f'"{quote.text}"'
            )
    by_line: dict[int, list[str]] = {}
    by_source: dict[str, list[str]] = {}
    for quote in kept:
        by_line.setdefault(quote.line, []).append(quote.text)
        if quote.source and not quote.in_changes:
            by_source.setdefault(quote.source, []).append(quote.text)
    for number, spans in by_line.items():
        distinct = _distinct(spans)
        if len(distinct) > 1:
            listed = " and ".join(f'"{span}"' for span in distinct)
            problems.append(f"line {number}: {len(distinct)} quotes on one line: {listed}")
    for source, spans in by_source.items():
        distinct = _distinct(spans)
        if len(distinct) > 1:
            listed = " and ".join(f'"{span}"' for span in distinct)
            problems.append(f"{len(distinct)} quotes from {source}: {listed}")
    return problems


# --- tool_used graders, re-counted from the run's calls -------------------------------------


@dataclass(frozen=True)
class ToolRule:
    tool: str
    pattern: str | None
    low: int
    high: int


def tool_rule(text: str) -> ToolRule | None:
    """A `tool_used` grader's rule, from its frontmatter; None for another grader. Raises
    ValueError where the rule cannot be read."""
    frontmatter, _ = shared.split_frontmatter(text)
    found = shared.fields(frontmatter)
    if found.get("type") != TOOL_USED:
        return None
    if not found.get("tool"):
        raise ValueError("no tool")
    pattern = found.get("input_match") or None
    if pattern is not None:
        re.compile(pattern)
    # Both bounds are required: the engine's default for a missing one was never measured.
    if not found.get("min") or not found.get("max"):
        raise ValueError("no min or no max")
    try:
        low, high = int(found["min"]), int(found["max"])
    except ValueError:
        raise ValueError("min or max is not a whole number") from None
    return ToolRule(found["tool"], pattern, low, high)


def _counts(rule: ToolRule, call: shared.Call) -> bool:
    if call.tool != rule.tool:
        return False
    return rule.pattern is None or re.search(rule.pattern, call.argument) is not None


def counted(rule: ToolRule, calls: list[shared.Call]) -> int:
    """The run's calls of the rule's tool, in any subagent and with any outcome, whose argument
    the rule's pattern finds."""
    return sum(_counts(rule, call) for call in calls)


def holds(rule: ToolRule, calls: list[shared.Call]) -> bool:
    count = counted(rule, calls)
    return rule.low <= count <= rule.high


# --- Runs and the case ------------------------------------------------------------------------


@dataclass
class Run:
    case: str
    number: int
    path: str
    header: dict[str, str]
    # None for a refusal or a question.
    report: str | None = None
    quotes: bool = True
    # None where the run writes no report, so has no linked sources to check.
    fetched: bool | None = None
    # Each tool_used grader's range, as the run's calls hold it.
    tools: dict[str, bool] = field(default_factory=dict)
    # The engine's verdict by grader.
    verdicts: dict[str, bool] = field(default_factory=dict)
    review: dict[str, str] | None = None

    @property
    def name(self) -> str:
        return f"run-{self.number}"

    def passed(self, grader: str) -> bool:
        """The verdict as the owner's line in review.md has it, else as the engine gave it."""
        line = (self.review or {}).get(grader)
        if line in PASS_FAIL:
            return line == "pass"
        return self.verdicts.get(grader, False)

    def held(self, grader: str) -> bool:
        """A tool_used grader passes when its verdict does and the run's calls agree."""
        return self.passed(grader) and self.tools.get(grader, False)

    def overruled(self) -> int:
        """The owner's lines that differ from the engine's verdict."""
        return sum(
            grader in (self.review or {}) and self.passed(grader) != passed
            for grader, passed in self.verdicts.items()
        )


@dataclass
class Case:
    id: str
    graders: list[str]
    runs: list[Run] = field(default_factory=list)
    sound: bool = True

    def passes(self) -> bool:
        """2 of its 3 runs pass both labels, where it has them, and facts."""
        needed = [grader for grader in PER_CASE if grader in self.graders]
        passing = sum(all(run.passed(grader) for grader in needed) for run in self.runs)
        return len(self.runs) == RUNS and passing >= ceil(CASE_PASS * RUNS)


@dataclass
class Report:
    problems: list[str] = field(default_factory=list)
    rows: list[shared.Row] = field(default_factory=list)
    cases: int = 0
    runs: int = 0
    verdicts: int = 0
    overruled: int = 0

    @property
    def missed(self) -> list[str]:
        return [row.check for row in self.rows if not row.met]


def _where(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def _prompt(root: Path, case: str) -> tuple[str, list[str]]:
    """The prompt the runs were given, prompt.md's body: a quote found in it is the user's."""
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


def _gold(root: Path, case: str) -> tuple[dict[str, str], list[str]]:
    """gold.md's fields, and what is wrong with them."""
    path = f"{EVALS}/cases/{case}/gold.md"
    try:
        frontmatter, _ = shared.split_frontmatter((root / path).read_text(encoding="utf-8"))
    except OSError:
        return {}, [f"{path}: missing"]
    except ValueError as error:
        return {}, [f"{path}: {error}"]
    found = shared.fields(frontmatter)
    problems = [f"{path}: no {name}" for name in GOLD_FIELDS if not found.get(name)]
    if found.get("authored") and not _DATE.fullmatch(found["authored"]):
        problems.append(f"{path}: authored is {found['authored']!r}, not a YYYY-MM-DD date")
    numbered: dict[str, set[int]] = {"fact": set(), "source": set(), "must": set()}
    for key, value in found.items():
        match = _NUMBERED.fullmatch(key)
        if match:
            numbered[match.group(1)].add(int(match.group(2)))
            if not value:
                problems.append(f"{path}: {key} is empty")
    if not numbered["fact"] and not numbered["must"]:
        problems.append(f"{path}: no fact_1 or must_1")
    for name in ("fact", "must"):
        numbers = numbered[name]
        if numbers and numbers != set(range(1, len(numbers) + 1)):
            problems.append(f"{path}: {name}_N not numbered from 1 without a gap")
    problems += [
        f"{path}: fact_{n} has no source_{n}" for n in sorted(numbered["fact"] - numbered["source"])
    ]
    problems += [
        f"{path}: source_{n} has no fact_{n}" for n in sorted(numbered["source"] - numbered["fact"])
    ]
    return found, problems


def _graders(
    root: Path, case: str, gold: dict[str, str]
) -> tuple[list[str], dict[str, ToolRule], list[str]]:
    """The case's graders by name, each one a bar reads, the ones its gold calls for present,
    and each tool_used grader's rule."""
    where = f"{EVALS}/cases/{case}/graders"
    names = [name.removesuffix(".md") for name in shared.grader_files(root, EVALS, case)]
    problems = [f"{where}: no {name}.md" for name in REQUIRED_GRADERS if name not in names]
    problems += [
        f"{where}/{name}.md: a grader no bar reads" for name in names if name not in GRADERS
    ]
    labelled = gold.get("roots", NONE) != NONE
    if labelled and LABELS not in names:
        problems.append(f"{where}: no {LABELS}.md, though gold gives labels")
    if not labelled and LABELS in names:
        problems.append(f"{where}/{LABELS}.md: gold gives no labels")
    if LABELS in names and FOOTER not in names:
        problems.append(f"{where}: no {FOOTER}.md beside {LABELS}.md")
    if (NO_SEARCH in names) != (NO_FETCH in names):
        problems.append(f"{where}: {NO_SEARCH}.md and {NO_FETCH}.md go together")
    rules: dict[str, ToolRule] = {}
    for name in names:
        try:
            rule = tool_rule((root / where / f"{name}.md").read_text(encoding="utf-8"))
        except (OSError, ValueError, re.error) as error:
            problems.append(f"{where}/{name}.md: its rule cannot be read ({error})")
            continue
        if rule:
            rules[name] = rule
    return names, rules, problems


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
    root: Path,
    case: str,
    number: int,
    path: Path,
    prompt: str,
    graders: list[str],
    rules: dict[str, ToolRule],
) -> tuple[Run, list[str]]:
    where = _where(root, path)
    try:
        run = shared.read_run(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        # Unread, it may be a report: it counts as one whose links failed, never as none.
        output = Run(
            case,
            number,
            where,
            {},
            report=UNREAD,
            quotes=False,
            fetched=False,
            tools=dict.fromkeys(rules, False),
        )
        output.verdicts, more = _read_verdicts(
            root, case, number, path.with_name(f"verdicts-{number}.md"), graders
        )
        # A file that cannot be read has one problem, not one for each check it fails.
        return output, [f"{where}: cannot be read ({error})", *more]
    problems = []
    if not run.header.get("commit"):
        problems.append(f"{where}: no commit in its header; the runner writes one")
    if run.header.get("case") != case or run.header.get("run") != str(number):
        problems.append(
            f"{where}: its header names case {run.header.get('case')!r}, "
            f"run {run.header.get('run')!r}"
        )
    output = Run(case, number, where, run.header, report=kind(run.reply))
    quoted = quote_problems(run.reply, prompt)
    output.quotes = not quoted
    problems += [f"{where}: {problem}" for problem in quoted]
    if output.report:
        fetched = {normalise(call.argument) for call in run.calls if call.tool == FETCH}
        missing = unfetched(run.reply, output.report, fetched)
        output.fetched = missing == []
        if missing is None:
            problems.append(f"{where}: a forward report with no Chain section")
        problems += [f"{where}: links {url}, which the run never fetched" for url in missing or []]
    for name, rule in rules.items():
        output.tools[name] = holds(rule, run.calls)
        if not output.tools[name]:
            match = f" matching {rule.pattern}" if rule.pattern else ""
            problems.append(
                f"{where}: {counted(rule, run.calls)} {rule.tool} call(s){match}, where {name} "
                f"allows {rule.low}..{rule.high}"
            )
    output.verdicts, more = _read_verdicts(
        root, case, number, path.with_name(f"verdicts-{number}.md"), graders
    )
    return output, problems + more


def _run_review(where: str, run: Run, section: dict[str, str] | None) -> list[str]:
    """A run's section: run 1 always, with a note; any other run with a failed verdict, a line
    for each and a note."""
    failed = [grader for grader, passed in run.verdicts.items() if not passed]
    if section is None:
        if run.number == 1:
            return [f"{where}: no section for run-1, the run the owner reads in every case"]
        if failed:
            return [f"{where}: no section for {run.name}, whose {', '.join(failed)} failed"]
        return []
    problems = []
    for key, value in section.items():
        if key == NOTE:
            continue
        if key in run.verdicts:
            if value not in PASS_FAIL:
                problems.append(f"{where}: {run.name}'s {key} is {value!r}, not pass or fail")
        else:
            problems.append(f"{where}: {run.name} has {key}, not a note or one of its graders")
    problems += [
        f"{where}: {run.name}'s {grader} failed and has no line: fail confirms it, pass "
        "overrules it"
        for grader in failed
        if grader not in section
    ]
    if not section.get(NOTE):
        problems.append(f"{where}: {run.name} has no {NOTE}")
    return problems


def _review(root: Path, case: str, runs: list[Run]) -> list[str]:
    path = root / EVALS / "results" / case / REVIEW
    where = _where(root, path)
    if not path.exists():
        return [f"{where}: missing"] if runs else []
    sections, problems = shared.parse_review(path.read_text(encoding="utf-8"), where)
    names = {run.name for run in runs}
    problems += [
        f"{where}: a section for {name}, which has no run" for name in sections if name not in names
    ]
    for run in runs:
        run.review = sections.get(run.name)
        problems += _run_review(where, run, run.review)
    return problems


def _check_case(
    root: Path,
    case: str,
    report: Report,
    snapshot: Callable[[str], shared.Snapshot],
    added: dict[str, str],
    committed: frozenset[str],
) -> Case:
    """One case's runs, its problems added to the report, and whether the case itself is sound:
    gold, its order, the prompt and the graders as each run had them."""
    prompt, problems = _prompt(root, case)
    gold, more = _gold(root, case)
    problems += more
    graders, rules, more = _graders(root, case, gold)
    problems += more
    folder = root / EVALS / "results" / case
    # Every entry is read, so a result that is not a file checks.py reads is a problem rather
    # than unseen; a dotfile (a runner's partial file, a folder's own metadata) is not one.
    entries = (
        sorted(p for p in folder.iterdir() if not p.name.startswith(".")) if folder.is_dir() else []
    )
    numbers = {int(m.group(1)) for p in entries if (m := _RUN.fullmatch(p.name)) and p.is_file()}
    found = Case(case, graders)
    for path in entries:
        run, verdicts = _RUN.fullmatch(path.name), _VERDICTS.fullmatch(path.name)
        if run and path.is_file():
            output, more = _read_run(root, case, int(run.group(1)), path, prompt, graders, rules)
            found.runs.append(output)
            report.problems += more
        elif verdicts and path.is_file():
            if int(verdicts.group(1)) not in numbers:
                report.problems.append(
                    f"{_where(root, path)}: no run-{verdicts.group(1)}.md beside it"
                )
        elif not (path.name == REVIEW and path.is_file()):
            report.problems.append(f"{_where(root, path)}: not a result checks.py reads")
    found.runs.sort(key=lambda r: r.number)
    report.problems += _review(root, case, found.runs)
    present = [_where(root, path) for path in entries if path.is_file()]
    by_commit: dict[str, list[str]] = {}
    for run in found.runs:
        if run.header.get("commit"):
            by_commit.setdefault(run.header["commit"], []).append(run.name)
    problems += shared.gold_order(root, EVALS, case, by_commit, present, snapshot, added, committed)
    problems += shared.case_as_run(root, EVALS, case, by_commit, snapshot)
    report.problems += problems
    found.sound = not problems
    return found


def _graded(
    check: str, runs: list[Run], cases: list[Case], test: Callable[[Run], bool]
) -> shared.Row:
    """A bar over every run of the cases that have its grader, of which there must be one."""
    total = RUNS * len(cases)
    passed = sum(test(run) for run in runs)
    return shared.Row(check, "all runs with its grader", passed, total, 0 < passed == total)


def _over_reports(check: str, passed: int, total: int) -> shared.Row:
    """A bar over the forward and reverse reports, of which there must be one: a refusal or a
    question links nothing."""
    return shared.Row(check, "all forward and reverse reports", passed, total, 0 < passed == total)


def bars(root: Path, cases: list[Case]) -> list[shared.Row]:
    """The spec's bars over the cycle: a case at 2 of 3, every other bar on every run."""
    runs = [run for case in cases for run in case.runs]
    every = RUNS * len(cases)
    reports = [run for run in runs if run.report]
    has = {name: [case for case in cases if name in case.graders] for name in GRADERS}
    commits = {run.header.get("commit") for run in runs} - {None, ""}
    current = {c for c in commits if shared.skill_unchanged_since(root, SKILL_FOLDER, c)}
    private = [case for case in cases if NO_SEARCH in case.graders and NO_FETCH in case.graders]
    return [
        shared.all_of(
            "Cases passing at 2 of 3 runs (labels and facts)",
            sum(case.passes() for case in cases),
            len(cases),
            "cases",
        ),
        shared.all_of(
            "No verdict in the report's own voice",
            sum(run.passed(NO_VERDICT) for run in runs),
            every,
            "runs",
        ),
        _graded(
            "Footer lines present",
            [run for case in has[FOOTER] for run in case.runs],
            has[FOOTER],
            lambda run: run.passed(FOOTER),
        ),
        shared.all_of(
            f"≤ 1 quote per source, < {QUOTE_WORDS} words",
            sum(run.quotes for run in runs),
            every,
            "runs",
        ),
        _over_reports(
            "Every linked source among the run's fetches",
            sum(bool(run.fetched) for run in reports),
            len(reports),
        ),
        _graded(
            "No search issued (private-person case)",
            [run for case in private for run in case.runs],
            private,
            lambda run: run.held(NO_SEARCH) and run.held(NO_FETCH),
        ),
        _graded(
            "Manager never in a search query (personal-chain case)",
            [run for case in has[MANAGER] for run in case.runs],
            has[MANAGER],
            lambda run: run.held(MANAGER),
        ),
        shared.all_of(
            "Gold order + approved_by + graders as run",
            sum(case.sound for case in cases),
            len(cases),
            "cases",
        ),
        shared.all_of(
            "Runs on the skill as it stands",
            sum(run.header.get("commit") in current for run in runs),
            every,
            "runs",
        ),
    ]


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
            if not p.name.startswith(".") and p.name not in ids
        ]
    snapshot = shared.snapshots(root, EVALS)
    added, committed = shared.added_in(root, EVALS), shared.committed(root, EVALS)
    cases = [_check_case(root, case, report, snapshot, added, committed) for case in ids]
    runs = [run for case in cases for run in case.runs]
    report.runs = len(runs)
    if runs:
        for case in cases:
            numbers = {run.number for run in case.runs}
            report.problems += [
                f"{EVALS}/results/{case.id}/run-{number}.md: missing"
                for number in range(1, RUNS + 1)
                if number not in numbers
            ]
            report.problems += [
                f"{EVALS}/results/{case.id}/run-{number}.md: a run beyond the cycle's {RUNS}"
                for number in sorted(numbers)
                if number > RUNS
            ]
        report.rows = bars(root, cases)
        report.verdicts = sum(len(run.verdicts) for run in runs)
        report.overruled = sum(run.overruled() for run in runs)
    return report


def state(report: Report) -> str:
    if not report.cases:
        return "no cases yet"
    if not report.runs:
        return "no results yet, so the pass bars are not counted"
    if report.missed:
        return f"pass bars not met: {', '.join(report.missed)}"
    return "every pass bar met"


def main() -> int:
    report = check(ROOT)
    for problem in report.problems:
        print(problem)
    if report.rows:
        print()
        print(shared.table(report.rows))
        print()
        print(f"Verdicts the owner overruled: {report.overruled} of {report.verdicts}")
    print(f"checks: {report.cases} case(s), {len(report.problems)} problem(s); {state(report)}")
    return 1 if report.problems or report.missed else 0


if __name__ == "__main__":
    sys.exit(main())
