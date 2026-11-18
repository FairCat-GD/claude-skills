"""Keeps private terms, AI attribution, secrets and conflict markers out of the repository.

A routine run reads what a commit could still change. A full scan reads everything; it runs with
--all, or by itself when the stamp is missing or older than the term list or this file.
"""

import argparse
import os
import re
import subprocess
import sys
import unicodedata
from collections.abc import Iterable, Iterator, Mapping
from pathlib import Path
from typing import NamedTuple

ROOT = Path(__file__).resolve().parent.parent
# A change to the stage's own source brings one full scan.
SOURCE = Path(__file__).resolve()
# Outside every repository: a hash of a short word is reversed by hashing a dictionary of names.
TERMS_FILE = Path.home() / ".config" / "hygiene" / "terms.txt"
# In the common git directory, so every checkout of the repository shares it. It holds nothing:
# its modification time records the last full scan that passed.
STAMP_NAME = "hygiene-scanned"


def _mark_ranges() -> str:
    ranges: list[list[int]] = []
    for code in range(sys.maxunicode + 1):
        if unicodedata.category(chr(code))[0] != "M":
            continue
        if ranges and ranges[-1][1] == code - 1:
            ranges[-1][1] = code
        else:
            ranges.append([code, code])
    return "".join(f"{re.escape(chr(first))}-{re.escape(chr(last))}" for first, last in ranges)


# Combining marks join a run, so a word in a script with vowel signs stays one token.
_RUN = re.compile(f"(?:[^\\W_]|[{_mark_ranges()}])+")
# Camel-case words and digit groups inside a run, so a term joined to another word is still seen.
_SUBTOKEN = re.compile(r"[A-Z]+(?=[A-Z][a-z])|[A-Z]?[a-z]+|[A-Z]+|[0-9]+")
_GITLINK = "160000"
# A credit line counts only when it names an AI tool, so a codegen script's note passes.
_TOOLS = r"(?:claude|chatgpt|gpt|openai|codex|copilot|gemini|cursor|ai)\b"
_VERBS = r"\b(?:generated|written|created|authored|produced)"
# Within one line: the tool may follow up to three words, as in "with the help of".
_CREDIT = r"[ \t]+(?:with|by|using|via)[ \t]+(?:[^\w\n]*\w+[ \t]+){0,3}?[^\w\n]*"
# Assembled from pieces so that this file never holds what it bans.
_ATTRIBUTION = {
    "co-author trailer": re.compile(r"^[ \t]*co" + "-author" + r"ed-by[ \t]*:", re.I | re.M),
    "generated-with line": re.compile(_VERBS + _CREDIT + _TOOLS, re.I),
    "AI session link": re.compile(
        r"https?://(?:[a-z0-9-]+\.)*(?:clau" + r"de\.ai|chat" + r"gpt\.com)/", re.I
    ),
}


def _bounded(body: str, inside: str) -> re.Pattern[str]:
    # Neither neighbour may be a character the secret is made of, so a longer run is not one.
    return re.compile(f"(?<![{inside}])(?:{body})(?![{inside}])")


_KEY = "A-Za-z0-9_-"
# Exact shapes only: looser ones raise false alarms on hyphenated names and test fixtures. The
# key header is split so that scanners looking for its literal text pass over this file.
_SECRETS = {
    "private-key header": re.compile("-" * 5 + "BEGIN (?:[A-Z0-9]+ )*PRIVATE KEY" + "-" * 5),
    "AWS access key": _bounded("(?:AKIA|ASIA)[A-Z0-9]{16}", "A-Z0-9"),
    "GitHub token": _bounded(
        "gh[pousr]_[A-Za-z0-9]{36}|github_pat_[A-Za-z0-9]{22}_[A-Za-z0-9]{59}", "A-Za-z0-9_"
    ),
    "Slack token": _bounded("xox[bpars]-[0-9]+-[A-Za-z0-9-]+", "A-Za-z0-9-"),
    "Anthropic key": _bounded(f"sk-ant-[a-z]+[0-9]{{2}}-[{_KEY}]{{80,}}", _KEY),
    "OpenAI key": _bounded(f"sk-(?:proj|svcacct|admin)-[{_KEY}]{{40,}}|sk-[A-Za-z0-9]{{48}}", _KEY),
}
# Left by a merge resolved by hand. A line of "=" alone is not one: Markdown underlines with it.
_MARKERS = ("<" * 7 + " ", ">" * 7 + " ")
# Names that hold examples rather than secrets.
_ENV_EXAMPLES = frozenset({".env.example", ".env.sample", ".env.template"})


class TermsError(Exception):
    pass


class Result(NamedTuple):
    problems: list[str]
    # Hits in pushed commit messages: history is never rewritten without the owner, so they are
    # counted for the owner and never fail the stage.
    pushed: list[str]


def _shown(path: Path) -> str:
    # Output may be pasted into a done-note, which never holds a home-directory path.
    try:
        return f"~/{path.relative_to(Path.home())}"
    except ValueError:
        return str(path)


def _fold(text: str) -> str:
    return unicodedata.normalize("NFC", unicodedata.normalize("NFC", text).lower())


def load_terms(path: Path) -> frozenset[str]:
    try:
        # An editor's byte-order mark would otherwise stick to the first word.
        text = path.read_text(encoding="utf-8-sig")
    except FileNotFoundError:
        raise TermsError(
            f"no term list at {_shown(path)}; create it, empty if nothing is private"
        ) from None
    terms = set()
    for number, line in enumerate(text.splitlines(), 1):
        word = _fold(line.strip())
        if not word or word.startswith("#"):
            continue
        # A line that is not one token could never match, so it fails instead of passing silently.
        if not _RUN.fullmatch(word):
            raise TermsError(f"{_shown(path)}:{number}: not one word")
        terms.add(word)
    return frozenset(terms)


def _shape(run: str) -> str:
    # Each letter's case in ASCII, so _SUBTOKEN splits camel case in any script.
    return "".join("A" if c.isupper() else "0" if c.isdecimal() else "a" for c in run)


def _tokens(line: str) -> set[str]:
    tokens = set()
    for run in _RUN.findall(unicodedata.normalize("NFC", line)):
        tokens.add(_fold(run))
        shape = run if run.isascii() else _shape(run)
        tokens.update(_fold(run[m.start() : m.end()]) for m in _SUBTOKEN.finditer(shape))
    return tokens


def _term_lines(text: str, terms: frozenset[str]) -> Iterator[int]:
    if not terms:
        return
    for number, line in enumerate(text.splitlines(), 1):
        if not terms.isdisjoint(_tokens(line)):
            yield number


def _line_hits(text: str, terms: frozenset[str], *, markers: bool) -> Iterator[tuple[int, str]]:
    for number, line in enumerate(text.splitlines(), 1):
        if terms and not terms.isdisjoint(_tokens(line)):
            yield number, "private term"
        yield from ((number, kind) for kind, shape in _SECRETS.items() if shape.search(line))
        if markers and line.startswith(_MARKERS):
            yield number, "conflict marker"


def _is_env(path: str) -> bool:
    name = path.rpartition("/")[2]
    return (name == ".env" or name.startswith(".env.")) and name not in _ENV_EXAMPLES


def _worktree(file: Path) -> bytes | None:
    # A link is read as its target, which is what git records, so nothing outside is read.
    if file.is_symlink():
        return os.fsencode(os.readlink(file))
    return file.read_bytes() if file.is_file() else None


def _content(where: str, data: bytes, terms: frozenset[str]) -> list[str]:
    if b"\0" in data:
        return []
    text = data.decode("utf-8", "replace")
    return [f"{where}:{number}: {kind}" for number, kind in _line_hits(text, terms, markers=True)]


def scan_files(root: Path, paths: Iterable[str], terms: frozenset[str]) -> list[str]:
    problems = []
    for path in paths:
        if any(_term_lines(path, terms)):
            problems.append(f"{path}: private term in the path")
        if _is_env(path):
            problems.append(f"{path}: .env file")
        data = _worktree(root / path)
        if data is not None:
            problems.extend(_content(path, data, terms))
    return problems


def scan_stored(
    root: Path, stored: Mapping[str, bytes], terms: frozenset[str], where: str
) -> list[str]:
    # A version stored in git, read only where it differs from the working tree's.
    problems = []
    for path, data in stored.items():
        if data != _worktree(root / path):
            problems.extend(_content(f"{path} ({where})", data, terms))
    return problems


def _message_hits(message: str, terms: frozenset[str]) -> list[tuple[int, str]]:
    hits = []
    for kind, pattern in _ATTRIBUTION.items():
        for match in pattern.finditer(message):
            hits.append((message.count("\n", 0, match.start()) + 1, kind))
    hits.extend(_line_hits(message, terms, markers=False))
    return hits


def scan_messages(commits: Iterable[tuple[str, str]], terms: frozenset[str]) -> list[str]:
    return [
        f"commit {sha[:12]}, message line {number}: {kind}"
        for sha, message in commits
        for number, kind in _message_hits(message, terms)
    ]


def scan_draft(message: str, terms: frozenset[str]) -> list[str]:
    return [
        f"commit message draft, line {number}: {kind}"
        for number, kind in _message_hits(message, terms)
    ]


def _git(root: Path, *args: str) -> str:
    # stdin is closed, so git never waits on a terminal.
    return subprocess.run(
        ["git", *args], cwd=root, input="", capture_output=True, text=True, check=True
    ).stdout


def _paths(listing: str) -> set[str]:
    return set(filter(None, listing.split("\0")))


def _has_commits(root: Path) -> bool:
    head = ["git", "rev-parse", "--verify", "--quiet", "HEAD"]
    return subprocess.run(head, cwd=root, input=b"", capture_output=True).returncode == 0


def repository_files(root: Path) -> list[str]:
    # Untracked files count too, so a new file is checked before it is staged.
    return sorted(
        _paths(_git(root, "ls-files", "-z", "--cached", "--others", "--exclude-standard"))
    )


def _index(root: Path) -> dict[str, str]:
    # The index is what a commit records, and it can differ from the working tree.
    entries = {}
    for entry in filter(None, _git(root, "ls-files", "-z", "--stage").split("\0")):
        info, _, path = entry.partition("\t")
        mode, sha, _ = info.split(" ")
        if mode != _GITLINK:
            entries[path] = sha
    return entries


def _head_tree(root: Path) -> dict[str, str]:
    entries = {}
    for entry in filter(None, _git(root, "ls-tree", "-r", "-z", "HEAD").split("\0")):
        info, _, path = entry.partition("\t")
        _, kind, sha = info.split(" ")
        if kind == "blob":
            entries[path] = sha
    return entries


def _blobs(root: Path, entries: Mapping[str, str]) -> dict[str, bytes]:
    batch = subprocess.run(
        ["git", "cat-file", "--batch"],
        cwd=root,
        input="".join(f"{sha}\n" for sha in entries.values()).encode(),
        capture_output=True,
        check=True,
    ).stdout
    contents, offset = {}, 0
    for path in entries:
        header_end = batch.index(b"\n", offset)
        size = int(batch[offset:header_end].split()[2])
        contents[path] = batch[header_end + 1 : header_end + 1 + size]
        offset = header_end + 1 + size + 1
    return contents


def _on_no_remote(root: Path, empty_tree: str) -> dict[str, set[str]]:
    # Each commit no remote holds, with the paths it changed against its first parent, so a merge
    # shows what it brought in; a root commit is compared with the empty tree.
    commits = {}
    for line in _git(root, "rev-list", "--parents", "HEAD", "--not", "--remotes").splitlines():
        sha, *parents = line.split()
        base = parents[0] if parents else empty_tree
        commits[sha] = _paths(_git(root, "diff", "--name-only", "-z", "--no-renames", base, sha))
    return commits


def commit_messages(root: Path, *revisions: str) -> list[tuple[str, str]]:
    if not _has_commits(root):
        return []
    log = _git(root, "log", "--format=%H%x00%B%x1e", *(revisions or ("HEAD",)))
    records = (record.strip("\n") for record in log.split("\x1e"))
    return [(sha, message) for sha, _, message in (r.partition("\0") for r in records if r)]


def scan(
    root: Path, terms: frozenset[str], draft: str | None = None, *, full: bool = False
) -> Result:
    has_commits = _has_commits(root)
    empty_tree = _git(root, "hash-object", "-t", "tree", "--stdin").strip()
    unpushed = _on_no_remote(root, empty_tree) if has_commits else {}
    committed = set().union(*unpushed.values())
    base = "HEAD" if has_commits else empty_tree
    # What a commit could still change: the index against HEAD, the working tree against the
    # index, untracked files, and what the commits on no remote changed.
    paths = (
        _paths(_git(root, "diff", "--cached", "--name-only", "-z", "--no-renames", base))
        | _paths(_git(root, "diff", "--name-only", "-z", "--no-renames"))
        | _paths(_git(root, "ls-files", "-z", "--others", "--exclude-standard"))
        | committed
    )
    if full:
        paths.update(repository_files(root))
    index = _index(root)
    tree = _head_tree(root) if has_commits else {}
    present = sorted(
        path
        for path in paths
        if path in index
        or (path in committed and path in tree)
        or _worktree(root / path) is not None
    )
    # An index version equal to HEAD's adds nothing a commit could record. HEAD's own version is
    # read only where a commit on no remote changed it: pushed history never fails.
    staged = {
        path: index[path] for path in present if path in index and index[path] != tree.get(path)
    }
    at_head = {path: tree[path] for path in present if path in committed and path in tree}
    problems = (
        scan_files(root, present, terms)
        + scan_stored(root, _blobs(root, staged), terms, "staged")
        + scan_stored(root, _blobs(root, at_head), terms, "at HEAD")
    )
    messages = (
        commit_messages(root) if full else commit_messages(root, "HEAD", "--not", "--remotes")
    )
    problems += scan_messages([m for m in messages if m[0] in unpushed], terms)
    pushed = scan_messages([m for m in messages if m[0] not in unpushed], terms)
    if draft is not None:
        problems += scan_draft(draft, terms)
    return Result(problems, pushed)


def stamp_path(root: Path) -> Path:
    return (root / _git(root, "rev-parse", "--git-common-dir").strip()).resolve() / STAMP_NAME


def full_scan_reason(stamp: Path, terms_file: Path) -> str | None:
    try:
        scanned = stamp.stat().st_mtime
    except FileNotFoundError:
        return "no full scan is recorded yet"
    if scanned < terms_file.stat().st_mtime:
        return "the term list changed since the last one"
    if scanned < SOURCE.stat().st_mtime:
        return "the stage changed since the last one"
    return None


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--terms", type=Path, help="the term list (default: ~/.config/hygiene/terms.txt)"
    )
    parser.add_argument("--message", type=Path, help="a drafted commit message to check too")
    parser.add_argument("--all", action="store_true", help="a full scan, whatever the stamp says")
    args = parser.parse_args(argv)
    terms_file = args.terms or TERMS_FILE
    try:
        terms = load_terms(terms_file)
    except (TermsError, OSError, UnicodeDecodeError) as error:
        print(f"hygiene: {error}")
        return 1
    try:
        draft = None if args.message is None else args.message.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as error:
        print(f"hygiene: cannot read the message draft: {error}")
        return 1
    stamp = stamp_path(ROOT)
    reason = "asked for with --all" if args.all else full_scan_reason(stamp, terms_file)
    print("hygiene: routine run" if reason is None else f"hygiene: full scan: {reason}")
    result = scan(ROOT, terms, draft, full=reason is not None)
    for problem in result.problems:
        print(problem)
    print(f"hygiene: {len(result.problems)} problem(s)")
    if reason is not None:
        for hit in result.pushed:
            print(f"{hit} (pushed)")
        print(
            f"hygiene: {len(result.pushed)} hit(s) in pushed history, not failing; "
            "record the count for the owner"
        )
        # Only a passing scan with the owner's own list stands for "everything has been read".
        if not result.problems and terms_file == TERMS_FILE:
            stamp.touch()
    return 1 if result.problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
