"""What every skill's eval tooling shares: frontmatter, and the two files each run leaves.

`evals/run.py` writes `results/<id>/run-N.md` and `results/<id>/verdicts-N.md` for each run, and
each skill's `checks.py` reads them, so their shape lives here once. Standard library only
(invariant 5).

A script under `evals/<skill>/` imports this module with its own folder's parent on the path:

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    import shared  # noqa: E402

`run-N.md` is a header, the run's tool calls one per line, then the final reply:

    ---
    case: <id>
    ...
    ---

    ## Tool calls

    - WebFetch (in general-purpose): https://example.com
    - Read (denied): <plugin>/skills/<skill>/references/x.md

    ## Reply

    <the reply>

`verdicts-N.md` is a header, then one section per grader of `- field: value` lines.

Below those formats is what every skill's `checks.py` reckons the same way: gold order and the
case as each run had it, from git (invariant 7); the skill as it stands; the owner's `review.md`;
words, quotation marks and the summary table.
"""

import re
import subprocess
from collections.abc import Callable
from dataclasses import dataclass
from math import ceil
from pathlib import Path

CALLS = "## Tool calls"
REPLY = "## Reply"
NO_CALLS = "none"
# `- <Tool>[ (in <subagent>)][ (denied|error)]: <argument>`
_CALL = re.compile(r"- (\S+?)(?: \(in ([^)\n]+)\))?(?: \((denied|error)\))?: (.*)")
_FIELD = re.compile(r"- ([a-z_]+): ?(.*)")
VERDICT_FIELDS = ("type", "verdict", "scored", "weight", "votes", "explanation")


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
    """One `key: value` per line, a quoted value unquoted, read with no YAML library."""
    found = {}
    for line in (frontmatter or "").split("\n"):
        key, colon, value = line.partition(":")
        if colon and key.strip() and not line[:1].isspace():
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
                value = value[1:-1]
            found[key.strip()] = value
    return found


def one_line(text: str) -> str:
    """Text on one line: a line break becomes the two characters `\\n`."""
    return text.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "\\n")


def _header(values: dict[str, str]) -> str:
    for key, value in values.items():
        if not re.fullmatch(r"[a-z_]+", key) or "\n" in str(value):
            raise ValueError(f"header field {key!r} cannot be written on one line")
    return "---\n" + "".join(f"{key}: {value}\n" for key, value in values.items()) + "---\n"


@dataclass(frozen=True)
class Call:
    """One tool call: the tool, its query, URL, path or input, where it ran and how it ended."""

    tool: str
    argument: str
    subagent: str | None = None
    # "" when it ran, "denied" when a permission refused it, "error" when it failed.
    outcome: str = ""

    def line(self) -> str:
        where = f" (in {self.subagent})" if self.subagent else ""
        how = f" ({self.outcome})" if self.outcome else ""
        return f"- {self.tool}{where}{how}: {one_line(self.argument)}"


@dataclass(frozen=True)
class Run:
    """A run-N.md read back: its header, its tool calls and its reply."""

    header: dict[str, str]
    calls: list[Call]
    reply: str


def format_run(header: dict[str, str], calls: list[Call], reply: str) -> str:
    """run-N.md's text; the reply as given, with a last newline added where it has none."""
    listed = "\n".join(call.line() for call in calls) if calls else NO_CALLS
    if reply and not reply.endswith("\n"):
        reply += "\n"
    return f"{_header(header)}\n{CALLS}\n\n{listed}\n\n{REPLY}\n\n{reply}"


def read_run(text: str) -> Run:
    """A run-N.md's parts. Raises ValueError where the file is not in this shape."""
    frontmatter, body = split_frontmatter(text)
    if frontmatter is None:
        raise ValueError("no header")
    lines = body.split("\n")
    if lines[:3] != ["", CALLS, ""]:
        raise ValueError(f"no {CALLS!r} after the header")
    # The first `## Reply` line is the runner's: every line before it is a call or `none`.
    try:
        end = lines.index(REPLY, 3)
    except ValueError:
        raise ValueError(f"no {REPLY!r}") from None
    calls = []
    for line in lines[3:end]:
        if line in ("", NO_CALLS):
            continue
        match = _CALL.fullmatch(line)
        if not match:
            raise ValueError(f"not a tool call: {line!r}")
        tool, subagent, outcome, argument = match.groups()
        calls.append(Call(tool, argument, subagent, outcome or ""))
    if lines[end + 1 : end + 2] != [""]:
        raise ValueError(f"no blank line after {REPLY!r}")
    return Run(fields(frontmatter), calls, "\n".join(lines[end + 2 :]))


@dataclass(frozen=True)
class Verdict:
    """One grader's verdict on one run."""

    name: str
    type: str
    passed: bool
    scored: bool
    weight: str
    # The judge's votes, as "pass pass fail", for an llm grader; "none" for the others.
    votes: str
    explanation: str


def _yes(value: bool) -> str:
    return "yes" if value else "no"


def format_verdicts(header: dict[str, str], verdicts: list[Verdict]) -> str:
    """verdicts-N.md's text: the header, then a section per grader."""
    sections = []
    for verdict in verdicts:
        if not verdict.name or "\n" in verdict.name:
            raise ValueError(f"grader name {verdict.name!r} cannot be a heading")
        values = {
            "type": verdict.type,
            "verdict": "pass" if verdict.passed else "fail",
            "scored": _yes(verdict.scored),
            "weight": verdict.weight,
            "votes": verdict.votes,
            "explanation": verdict.explanation,
        }
        lines = "".join(f"- {key}: {one_line(value)}\n" for key, value in values.items())
        sections.append(f"## {verdict.name}\n\n{lines}")
    return _header(header) + "".join(f"\n{section}" for section in sections)


def read_verdicts(text: str) -> tuple[dict[str, str], list[Verdict]]:
    """A verdicts-N.md's header and verdicts. Raises ValueError where it is not in this shape."""
    frontmatter, body = split_frontmatter(text)
    if frontmatter is None:
        raise ValueError("no header")
    verdicts = []
    for section in re.split(r"^## ", body, flags=re.MULTILINE)[1:]:
        name, _, rest = section.partition("\n")
        values = {}
        for line in rest.split("\n"):
            if not line:
                continue
            match = _FIELD.fullmatch(line)
            if not match:
                raise ValueError(f"{name}: not a field: {line!r}")
            values[match.group(1)] = match.group(2)
        missing = [key for key in VERDICT_FIELDS if key not in values]
        if missing:
            raise ValueError(f"{name}: no {', '.join(missing)}")
        if values["verdict"] not in ("pass", "fail") or values["scored"] not in ("yes", "no"):
            raise ValueError(f"{name}: verdict or scored is not one of its values")
        verdicts.append(
            Verdict(
                name=name,
                type=values["type"],
                passed=values["verdict"] == "pass",
                scored=values["scored"] == "yes",
                weight=values["weight"],
                votes=values["votes"],
                explanation=values["explanation"],
            )
        )
    return fields(frontmatter), verdicts


# --- Gold order and the case as it ran, from git ---------------------------------------------


def git(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, stdin=subprocess.DEVNULL
    )


def names(text: str) -> frozenset[str]:
    """Paths as git prints them with -z: separated by NUL and never quoted, so a name with a
    non-ASCII letter reads as the folder holds it."""
    return frozenset(name for name in text.split("\0") if name)


@dataclass(frozen=True)
class Snapshot:
    """A skill's case folders in one commit, read against the working tree."""

    # Every file the folders held in the commit; None where the commit cannot be read.
    held: frozenset[str] | None
    # The tracked files that differ in the working tree, removed ones included.
    changed: frozenset[str]


def snapshots(root: Path, evals: str) -> Callable[[str], Snapshot]:
    """Every case folder under `<evals>/cases` in a commit, each commit read once, since a
    cycle's runs share theirs. `evals` is the skill's folder relative to the root, as git names
    it."""
    folder = f"{evals}/cases"
    cache: dict[str, Snapshot] = {}

    def snapshot(commit: str) -> Snapshot:
        if commit not in cache:
            listed = git(root, "ls-tree", "-z", "-r", "--name-only", commit, "--", folder)
            if listed.returncode != 0:
                cache[commit] = Snapshot(None, frozenset())
            else:
                changed = git(
                    root, "diff", "-z", "--no-renames", "--name-only", commit, "--", folder
                )
                cache[commit] = Snapshot(names(listed.stdout), names(changed.stdout))
        return cache[commit]

    return snapshot


def added_in(root: Path, evals: str) -> dict[str, str]:
    """Each file ever added under `<evals>/results`, by the latest commit that added it. Without
    `--no-renames` a file renamed there is logged as renamed, never as added. With -z each
    commit's line is `%x01` and its hash, and each name follows a NUL, unquoted."""
    log = git(
        root,
        "log",
        "-z",
        "--no-renames",
        "--diff-filter=A",
        "--format=%x01%H",
        "--name-only",
        "--",
        f"{evals}/results",
    )
    added: dict[str, str] = {}
    commit, first = "", False
    for token in log.stdout.split("\0"):
        if token.startswith("\x01"):
            commit, first = token[1:], True
            continue
        if first:
            # git puts one newline between a commit's line and its first name.
            token, first = token.removeprefix("\n"), False
        if token:
            # The log runs newest first, so the first commit seen is the latest adding.
            added.setdefault(token, commit)
    return added


def committed(root: Path, evals: str) -> frozenset[str]:
    """Every file under `<evals>/results` that HEAD holds."""
    return names(
        git(root, "ls-tree", "-z", "-r", "--name-only", "HEAD", "--", f"{evals}/results").stdout
    )


def gold_order(
    root: Path,
    evals: str,
    case: str,
    by_commit: dict[str, list[str]],
    present: list[str],
    snapshot: Callable[[str], Snapshot],
    added: dict[str, str],
    held: frozenset[str],
) -> list[str]:
    """Invariant 7: gold.md committed before every result present now, and unchanged since.

    `by_commit` names every output by the commit its header names, a claude.ai reply's as well
    as a run's; `present` is every file now under results/<id>/, as git names it; `held` is what
    `committed` gives.

    Each file HEAD holds under results/<id>/ counts from the commit that added it, its latest
    adding for a file removed and added again, so a retired cycle kept in history never counts.
    A file not yet committed has no adding of its own: any adding its path has in history is a
    retired cycle's, so it is not reckoned from history. The commit that adds it will follow
    HEAD, which must hold gold, and gold must have no uncommitted change, both checked here."""
    gold = f"{evals}/cases/{case}/gold.md"
    head = snapshot("HEAD")
    if head.held is None or gold not in head.held:
        return [f"{gold}: not committed"]
    problems: list[str] = []
    by_adding: dict[str, list[str]] = {}
    for path in present:
        if path not in held:
            continue
        if path in added:
            by_adding.setdefault(added[path], []).append(path.rsplit("/", 1)[-1])
        else:
            # Committed, yet no commit adds it: the order cannot be reckoned, so it is no pass.
            problems.append(f"{gold}: no commit adds {path}, so its order cannot be checked")
    for commit, files in by_adding.items():
        which = f"{', '.join(files)}, added in {commit[:12]}"
        before = snapshot(f"{commit}^")
        if before.held is None or gold not in before.held:
            problems.append(f"{gold}: not committed before {which}")
        elif gold in before.changed:
            problems.append(f"{gold}: changed since {which}")
    for commit, outputs in by_commit.items():
        which = f"which {', '.join(outputs)} ran on"
        then = snapshot(commit)
        if then.held is None or gold not in then.held:
            problems.append(f"{gold}: not in commit {commit[:12]}, {which}")
        elif gold in then.changed:
            problems.append(f"{gold}: changed since commit {commit[:12]}, {which}")
    if present and gold in head.changed:
        problems.append(f"{gold}: uncommitted changes while results exist")
    return problems


def grader_files(root: Path, evals: str, case: str) -> list[str]:
    """The case's grader files by name, in order."""
    folder = root / evals / "cases" / case / "graders"
    return sorted(p.name for p in folder.glob("*.md")) if folder.is_dir() else []


def case_as_run(
    root: Path,
    evals: str,
    case: str,
    by_commit: dict[str, list[str]],
    snapshot: Callable[[str], Snapshot],
) -> list[str]:
    """Each run's prompt.md and graders unchanged since the commit it names: the case as it ran.
    `by_commit` names the runs alone; a claude.ai reply is older than every grader."""
    prompt = f"{evals}/cases/{case}/prompt.md"
    graders = f"{evals}/cases/{case}/graders"
    now = grader_files(root, evals, case)
    problems = []
    for commit, runs in by_commit.items():
        which = f"commit {commit[:12]}, which {', '.join(runs)} ran on"
        then = snapshot(commit)
        held = then.held or frozenset()
        if prompt not in held:
            problems.append(f"{prompt}: not in {which}")
        elif prompt in then.changed:
            problems.append(f"{prompt}: changed since {which}")
        inside = [path[len(graders) + 1 :] for path in held if path.startswith(f"{graders}/")]
        before = sorted(name for name in inside if "/" not in name and name.endswith(".md"))
        if not before:
            problems.append(f"{graders}: not in {which}")
        elif before != now:
            problems.append(f"{graders}: graders added or removed since {which}")
        elif any(path.startswith(f"{graders}/") for path in then.changed):
            problems.append(f"{graders}: changed since {which}")
    return problems


# --- The skill as it stands ------------------------------------------------------------------

# A `version:` key indented under `metadata:`, with any value, quoted or not.
_VERSION = re.compile(r"[ \t]+version:[ \t]*\S.*")


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


def skill_unchanged_since(root: Path, skill_folder: str, commit: str) -> bool:
    """Whether the skill folder, in the working tree, is as it was in the commit, SKILL.md's
    metadata.version aside: a change to it alone is a release, not a change to the skill, so a
    run on the commit before it ran the skill as it stands."""
    skill = f"{skill_folder}/SKILL.md"
    rest = git(root, "diff", "--quiet", commit, "--", skill_folder, f":(exclude){skill}")
    # `git diff` does not see a file git does not track, such as a new reference not yet added.
    untracked = git(root, "ls-files", "-z", "--others", "--exclude-standard", "--", skill_folder)
    then = git(root, "show", f"{commit}:{skill}")
    try:
        now = (root / skill).read_text(encoding="utf-8")
    except OSError:
        return False
    return (
        rest.returncode == 0
        and not names(untracked.stdout)
        and then.returncode == 0
        and without_version(then.stdout) == without_version(now)
    )


# --- review.md: the owner's lines ------------------------------------------------------------

# A review line, `- <field or grader>: <value>`; a grader's name may hold a digit or a hyphen.
_REVIEW_LINE = re.compile(r"- ([a-z0-9_-]+):[ \t]*(.*)")


def parse_review(text: str, where: str) -> tuple[dict[str, dict[str, str]], list[str]]:
    """review.md: `# Review: <id>`, then a `## <output>` section per output, each of
    `- field: value` lines."""
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
        match = _REVIEW_LINE.fullmatch(stripped)
        if current is None or not match:
            problems.append(f"{where}:{number}: not a `- field: value` line in an output's section")
            continue
        key, value = match.groups()
        if key in current:
            problems.append(f"{where}:{number}: {key} given twice")
        else:
            current[key] = value.strip()
    return sections, problems


# --- Words, quotation marks and the summary table --------------------------------------------

_ELLIPSIS = re.compile(r"…|\.\.\.")
# Typographic quotation marks and apostrophes read as their plain forms: the double ones
# (curly, low, reversed, double prime) as ", the single ones as '.
_DOUBLE = "\u201c\u201d\u201e\u201f\u2033"
_SINGLE = "\u2018\u2019\u201a\u201b\u2032"
_FOLD = str.maketrans(dict.fromkeys(_DOUBLE, '"') | dict.fromkeys(_SINGLE, "'"))


def words(text: str) -> int:
    """A word is a whitespace-separated token with a letter or digit; markup alone is none."""
    return sum(1 for token in text.split() if any(ch.isalnum() for ch in token))


def fold(text: str) -> str:
    """Typographic quotation marks as plain ones, and every run of whitespace as one space."""
    return " ".join(text.translate(_FOLD).split())


def found_verbatim(span: str, source: str) -> bool:
    """Whether the span is in the source, line breaks joined and quotation marks folded; with an
    ellipsis, piece by piece, in order. A mark that ends the sentence inside the closing
    quotation mark is not part of the quote."""
    pieces = [piece.strip() for piece in _ELLIPSIS.split(fold(span))]
    pieces = [piece for piece in pieces if piece]
    if pieces:
        pieces[-1] = pieces[-1].rstrip(".,;:!?") or pieces[-1]
    text, position = fold(source), 0
    for piece in pieces:
        index = text.find(piece, position)
        if index < 0:
            return False
        position = index + len(piece)
    return True


@dataclass
class Row:
    """One row of a skill's summary table: a check, its pass bar and the result against it."""

    check: str
    bar: str
    passed: int
    total: int
    met: bool


def all_of(check: str, passed: int, total: int, unit: str) -> Row:
    return Row(check, f"all {unit}", passed, total, passed == total)


def at_least(check: str, ratio, passed: int, total: int, unit: str) -> Row:
    """A row met at the ratio's share of the total, rounded up; never met over nothing."""
    need = ceil(ratio * total)
    return Row(check, f"≥ {need} / {total} {unit}", passed, total, total > 0 and passed >= need)


def table(rows: list[Row]) -> str:
    lines = ["| Check | Pass bar | Result | Met |", "|---|---|---|---|"]
    for row in rows:
        met = "yes" if row.met else "**no**"
        lines.append(f"| {row.check} | {row.bar} | {row.passed} / {row.total} | {met} |")
    return "\n".join(lines)
