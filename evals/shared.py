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
"""

import re
from dataclasses import dataclass

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
