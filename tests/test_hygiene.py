import os
import shutil
import subprocess
import unicodedata
from collections.abc import Callable
from pathlib import Path

import pytest

import hygiene

OWNERS_LIST = hygiene.TERMS_FILE
REPOSITORY = hygiene.ROOT
FIXTURE = Path(__file__).parent / "fixtures" / "terms.txt"
PROBE, CYRILLIC, DEVANAGARI = (
    line
    for line in FIXTURE.read_text(encoding="utf-8").splitlines()
    if line and not line.startswith("#")
)
# Assembled from pieces so that this file never holds what the stage bans.
TRAILER = "Co" + "-authored-by: Someone <someone@example.invalid>"
GENERATED = "Gener" + "ated with [Clau" + "de Code](https://example.invalid)"
SESSION_LINK = "https://clau" + "de.ai/code/session_0123"
SECRETS = {
    "private-key": ("private-key header", "-" * 5 + "BEGIN OPENSSH " + "PRIVATE KEY" + "-" * 5),
    "aws": ("AWS access key", "AS" + "IA" + "Q7" * 8),
    "github": ("GitHub token", "gh" + "p_" + "aB3" * 12),
    "github-pat": ("GitHub token", "github" + "_pat_" + "a1" * 11 + "_" + "b2c" * 19 + "d4"),
    "slack": ("Slack token", "xo" + "xb-" + "1234567890" + "-" + "aBcD1234"),
    "anthropic": ("Anthropic key", "sk-" + "ant-" + "api03-" + "aB1_-" * 16),
    "openai-project": ("OpenAI key", "sk-" + "proj-" + "aB1_-" * 8),
    "openai-legacy": ("OpenAI key", "sk-" + "Ab1" * 16),
}
# Times for the stamp tests, so no outcome depends on the clock.
T_SOURCE, T_LIST, T_STAMP, T_LATER = 1_600_000_000, 1_700_000_000, 1_700_000_100, 1_700_000_200

Terms = Callable[..., frozenset[str]]


@pytest.fixture(autouse=True)
def _never_the_owners_list_or_stamp(
    tmp_path_factory: pytest.TempPathFactory, monkeypatch: pytest.MonkeyPatch
) -> None:
    # The owner's list is never read, and the real repository's stamp is out of reach: a run
    # that forgot to choose a repository fails in a folder that is not one.
    stage = tmp_path_factory.mktemp("stage")
    source = stage / "hygiene.py"
    source.write_text("")
    os.utime(source, (T_SOURCE, T_SOURCE))
    monkeypatch.setattr(hygiene, "TERMS_FILE", stage / "missing.txt")
    monkeypatch.setattr(hygiene, "ROOT", tmp_path_factory.mktemp("not-a-repository"))
    monkeypatch.setattr(hygiene, "SOURCE", source)


@pytest.fixture
def terms(tmp_path_factory: pytest.TempPathFactory) -> Terms:
    # A list of fictional words, kept outside every repository a test scans.
    def load(*words: str) -> frozenset[str]:
        path = tmp_path_factory.mktemp("terms") / "terms.txt"
        path.write_text("".join(f"{word}\n" for word in words), encoding="utf-8")
        return hygiene.load_terms(path)

    return load


@pytest.fixture
def owners_list(tmp_path_factory: pytest.TempPathFactory, monkeypatch: pytest.MonkeyPatch) -> Path:
    # A copy of the fixture standing in for the owner's list, so its time can be set.
    listed = tmp_path_factory.mktemp("owner") / "terms.txt"
    shutil.copyfile(FIXTURE, listed)
    os.utime(listed, (T_LIST, T_LIST))
    monkeypatch.setattr(hygiene, "TERMS_FILE", listed)
    return listed


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    # Its origin is a bare repository beside it, so a push makes a commit pushed.
    origin, repo = tmp_path / "origin.git", tmp_path / "repo"
    repo.mkdir()
    _git(tmp_path, "init", "-q", "--bare", "-b", "main", str(origin))
    _git(repo, "init", "-q", "-b", "main")
    _git(repo, "remote", "add", "origin", str(origin))
    return repo


def _git(repo: Path, *args: str) -> str:
    env = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}
    identity = ["-c", "user.name=Test", "-c", "user.email=test@example.invalid"]
    return subprocess.run(
        ["git", *identity, *args], cwd=repo, env=env, check=True, capture_output=True, text=True
    ).stdout


def _commit(repo: Path, message: str, files: dict[str, str] | None = None) -> str:
    for name, text in (files or {}).items():
        (repo / name).write_text(text, encoding="utf-8")
        _git(repo, "add", name)
    _git(repo, "commit", "-q", "--allow-empty", "-m", message)
    return _git(repo, "rev-parse", "HEAD").strip()


def _push(repo: Path) -> None:
    _git(repo, "push", "-q", "origin", "main")


def _set_time(path: Path, seconds: int) -> None:
    os.utime(path, (seconds, seconds))


def _stamp(repo: Path) -> Path:
    return repo / ".git" / hygiene.STAMP_NAME


def test_the_list_is_read_from_outside_the_repository() -> None:
    assert OWNERS_LIST == Path.home() / ".config" / "hygiene" / "terms.txt"
    assert REPOSITORY not in OWNERS_LIST.parents


def test_a_missing_list_fails(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(hygiene.TermsError, match="no term list"):
        hygiene.load_terms(tmp_path / "absent.txt")
    assert hygiene.main([]) == 1
    assert f"no term list at {hygiene.TERMS_FILE}" in capsys.readouterr().out


def test_an_empty_list_passes(terms: Terms) -> None:
    assert terms() == frozenset()
    assert terms("", "  ") == frozenset()


def test_a_byte_order_mark_and_comment_lines_are_not_terms(tmp_path: Path) -> None:
    path = tmp_path / "terms.txt"
    path.write_text(f"﻿{PROBE}\n# a note on this list\n{CYRILLIC}\n", encoding="utf-8")
    assert hygiene.load_terms(path) == frozenset({PROBE, CYRILLIC})


def test_the_fixture_list_loads_as_its_three_words() -> None:
    assert hygiene.load_terms(FIXTURE) == frozenset({PROBE, CYRILLIC, DEVANAGARI})


def test_a_path_under_home_is_shown_with_a_tilde() -> None:
    absent = Path.home() / ".config" / "hygiene-absent-zqx" / "terms.txt"
    with pytest.raises(hygiene.TermsError) as error:
        hygiene.load_terms(absent)
    assert str(error.value).startswith("no term list at ~/.config/hygiene-absent-zqx/terms.txt;")
    assert str(Path.home()) not in str(error.value)


def test_a_line_that_is_not_one_word_fails_without_printing_it(tmp_path: Path) -> None:
    path = tmp_path / "terms.txt"
    path.write_text(f"{PROBE}\n{PROBE}-{PROBE}\n", encoding="utf-8")
    with pytest.raises(hygiene.TermsError) as error:
        hygiene.load_terms(path)
    assert str(error.value) == f"{path}:2: not one word"


def test_a_term_in_a_file_is_reported_by_file_and_line_never_by_name(
    tmp_path: Path, terms: Terms
) -> None:
    (tmp_path / "notes.txt").write_text(f"first line\nsecond line, {PROBE.upper()}!\n")
    (tmp_path / "clean.txt").write_text("nothing to see\n")
    problems = hygiene.scan_files(tmp_path, ["notes.txt", "clean.txt"], terms(PROBE))
    assert problems == ["notes.txt:2: private term"]
    assert PROBE not in "".join(problems).lower()


def test_a_term_joined_to_a_word_or_number_is_reported(tmp_path: Path, terms: Terms) -> None:
    text = f"my{PROBE.capitalize()}Notes\n{PROBE}2026\nmy{CYRILLIC.capitalize()}\n"
    (tmp_path / "joined.txt").write_text(text, encoding="utf-8")
    problems = hygiene.scan_files(tmp_path, ["joined.txt"], terms(PROBE, CYRILLIC))
    assert problems == [f"joined.txt:{n}: private term" for n in (1, 2, 3)]


def test_a_cyrillic_term_is_found_however_it_is_encoded(tmp_path: Path, terms: Terms) -> None:
    decomposed = unicodedata.normalize("NFD", CYRILLIC)
    assert decomposed != CYRILLIC
    text = f"x {decomposed} y\nx {CYRILLIC.upper()} y\n"
    (tmp_path / "notes.txt").write_text(text, encoding="utf-8")
    for term in (CYRILLIC, decomposed):
        problems = hygiene.scan_files(tmp_path, ["notes.txt"], terms(term))
        assert problems == ["notes.txt:1: private term", "notes.txt:2: private term"]


def test_a_word_with_combining_marks_is_one_token(tmp_path: Path, terms: Terms) -> None:
    assert any(unicodedata.category(c).startswith("M") for c in DEVANAGARI)
    (tmp_path / "notes.txt").write_text(f"क {DEVANAGARI} ख\n", encoding="utf-8")
    problems = hygiene.scan_files(tmp_path, ["notes.txt"], terms(DEVANAGARI))
    assert problems == ["notes.txt:1: private term"]


def test_a_term_in_a_path_is_reported(tmp_path: Path, terms: Terms) -> None:
    name = f"{PROBE}-notes.txt"
    (tmp_path / name).write_text("nothing to see\n")
    problems = hygiene.scan_files(tmp_path, [name], terms(PROBE))
    assert problems == [f"{name}: private term in the path"]


def test_binary_files_are_skipped(tmp_path: Path, terms: Terms) -> None:
    (tmp_path / "image.bin").write_bytes(b"\0" + PROBE.encode())
    assert hygiene.scan_files(tmp_path, ["image.bin"], terms(PROBE)) == []


def test_a_link_is_read_as_its_target_never_followed(tmp_path: Path, terms: Terms) -> None:
    outside = tmp_path / "outside"
    outside.mkdir()
    (outside / "notes.txt").write_text(f"about {PROBE}\n")
    (tmp_path / "repo").mkdir()
    (tmp_path / "repo" / "link").symlink_to(outside / "notes.txt")
    (tmp_path / "repo" / "named").symlink_to(outside / f"{PROBE}.txt")
    problems = hygiene.scan_files(tmp_path / "repo", ["link", "named"], terms(PROBE))
    assert problems == ["named:1: private term"]


@pytest.mark.parametrize(("kind", "secret"), SECRETS.values(), ids=SECRETS.keys())
def test_each_secret_shape_fails(tmp_path: Path, kind: str, secret: str) -> None:
    (tmp_path / "config.txt").write_text(f"first line\nkey = {secret}\n")
    problems = hygiene.scan_files(tmp_path, ["config.txt"], frozenset())
    assert problems == [f"config.txt:2: {kind}"]
    assert secret not in "".join(problems)


def test_a_secret_in_the_draft_fails() -> None:
    draft = f"fix: one\n\nThe key was {SECRETS['github'][1]}."
    assert hygiene.scan_draft(draft, frozenset()) == ["commit message draft, line 3: GitHub token"]


def test_lookalikes_of_a_secret_pass(tmp_path: Path) -> None:
    lookalikes = [
        "risk-" + "Ab1" * 16,
        "github" + "_pat_TEST",
        "AKIA" + "Q7" * 8 + "X",
        "data:image/png;base64,iVBOR" + "ASIA" + "Q7" * 8 + "wgAAA",
        "sha512-" + "AKIA" + "Q7" * 8 + "/x+Y==",
        "sk-" + "Ab1" * 16 + "c",
    ]
    (tmp_path / "notes.txt").write_text("".join(f"{line}\n" for line in lookalikes))
    assert hygiene.scan_files(tmp_path, ["notes.txt"], frozenset()) == []


def test_line_numbers_count_newlines_only(tmp_path: Path, terms: Terms) -> None:
    # A form feed or a Unicode line separator does not start a line for an editor or for git.
    (tmp_path / "notes.txt").write_text(f"one\fstill one\u2028and still\nabout {PROBE}\n")
    assert hygiene.scan_files(tmp_path, ["notes.txt"], terms(PROBE)) == [
        "notes.txt:2: private term"
    ]
    # A term and an attribution on one line get one line number.
    draft = f"fix: one\n\nx\u2028About {PROBE}, {GENERATED}"
    assert hygiene.scan_draft(draft, terms(PROBE)) == [
        "commit message draft, line 3: generated-with line",
        "commit message draft, line 3: private term",
    ]


def test_a_part_checkout_at_the_root_is_skipped(tmp_path: Path, terms: Terms) -> None:
    _git(tmp_path, "init", "-q", "-b", "main")
    for folder in (".claude/worktrees/part", "docs/.claude/worktrees/part"):
        (tmp_path / folder).mkdir(parents=True)
        (tmp_path / folder / "notes.txt").write_text(f"about {PROBE}\n")
    for full in (False, True):
        assert hygiene.scan(tmp_path, terms(PROBE), full=full).problems == [
            "docs/.claude/worktrees/part/notes.txt:1: private term"
        ]


def test_a_tracked_env_file_fails_and_an_example_passes(tmp_path: Path) -> None:
    _git(tmp_path, "init", "-q", "-b", "main")
    (tmp_path / "app").mkdir()
    for name in (".env", ".env.example", "app/.env.local"):
        (tmp_path / name).write_text("SETTING=1\n")
    _git(tmp_path, "add", "-f", ".")
    assert hygiene.scan(tmp_path, frozenset()).problems == [
        ".env: .env file",
        "app/.env.local: .env file",
    ]


def test_a_conflict_marker_fails_and_a_heading_underline_passes(tmp_path: Path) -> None:
    merged = "<" * 7 + " HEAD\nours\n" + "=" * 7 + "\ntheirs\n" + ">" * 7 + " topic\n"
    (tmp_path / "merged.md").write_text(merged)
    (tmp_path / "heading.md").write_text("Title\n" + "=" * 7 + "\n\nText " + "<" * 7 + " too.\n")
    assert hygiene.scan_files(tmp_path, ["heading.md", "merged.md"], frozenset()) == [
        "merged.md:1: conflict marker",
        "merged.md:5: conflict marker",
    ]


def test_attribution_and_terms_in_commit_messages_are_reported(
    tmp_path: Path, terms: Terms
) -> None:
    _git(tmp_path, "init", "-q", "-b", "main")
    _git(tmp_path, "commit", "-q", "--allow-empty", "-m", "feat: clean\n\nA plain body.")
    _git(tmp_path, "commit", "-q", "--allow-empty", "-m", f"fix: one\n\n{TRAILER}")
    _git(tmp_path, "commit", "-q", "--allow-empty", "-m", f"fix: two\n\n{GENERATED}")
    _git(tmp_path, "commit", "-q", "--allow-empty", "-m", f"fix: three\n\nSee {SESSION_LINK}")
    _git(tmp_path, "commit", "-q", "--allow-empty", "-m", f"fix: four\n\nAbout {PROBE}.")
    problems = hygiene.scan_messages(hygiene.commit_messages(tmp_path), terms(PROBE))
    kinds = sorted(problem.split(": ", 1)[1] for problem in problems)
    assert kinds == ["AI session link", "co-author trailer", "generated-with line", "private term"]
    assert all(", message line 3: " in problem for problem in problems)


def test_a_generated_line_counts_only_when_it_names_an_ai_tool() -> None:
    plain = [
        "The tables are " + "gener" + "ated with the codegen script.",
        "Tables re" + "gener" + "ated with\n- AI-free fixtures.",
        "Files " + "gener" + "ated with\n- Codex notes.",
        "The config writ" + "ten by doctor now works with Codex.",
    ]
    for body in plain:
        assert hygiene.scan_draft(f"fix: one\n\n{body}", frozenset()) == []
    credits = [
        GENERATED,
        "Writ" + "ten by Codex.",
        "Gener" + "ated with the help of Claude.",
        "Creat" + "ed using an AI.",
    ]
    for body in credits:
        assert hygiene.scan_draft(f"fix: one\n\n{body}", frozenset()) == [
            "commit message draft, line 3: generated-with line"
        ]


def test_a_term_or_a_trailer_in_the_draft_fails(tmp_path: Path, terms: Terms) -> None:
    listed = terms(PROBE)
    _git(tmp_path, "init", "-q", "-b", "main")
    assert hygiene.scan(tmp_path, listed, f"fix: one\n\nAbout {PROBE}.").problems == [
        "commit message draft, line 3: private term"
    ]
    assert hygiene.scan(tmp_path, listed, f"fix: one\n\n{TRAILER}").problems == [
        "commit message draft, line 3: co-author trailer"
    ]
    assert hygiene.scan(tmp_path, listed, "fix: one\n\nA plain body.").problems == []


def test_main_checks_the_draft(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    repo, listed = tmp_path / "repo", tmp_path / "terms.txt"
    repo.mkdir()
    listed.write_text("")
    _git(repo, "init", "-q", "-b", "main")
    monkeypatch.setattr(hygiene, "ROOT", repo)
    draft = tmp_path / "COMMIT_DRAFT"
    draft.write_text(f"fix: one\n\n{TRAILER}\n")
    assert hygiene.main(["--terms", str(listed), "--message", str(draft)]) == 1
    assert "commit message draft, line 3: co-author trailer" in capsys.readouterr().out
    draft.write_text("fix: one\n\nA plain body.\n")
    assert hygiene.main(["--terms", str(listed), "--message", str(draft)]) == 0


def test_an_unreadable_draft_fails(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    (tmp_path / "terms.txt").write_text("")
    argv = ["--terms", str(tmp_path / "terms.txt"), "--message", str(tmp_path / "absent")]
    assert hygiene.main(argv) == 1
    assert "cannot read the message draft" in capsys.readouterr().out


def test_a_term_staged_but_gone_from_the_working_tree_is_reported(
    tmp_path: Path, terms: Terms
) -> None:
    _git(tmp_path, "init", "-q", "-b", "main")
    (tmp_path / "notes.txt").write_text(f"a {PROBE}\n")
    _git(tmp_path, "add", "notes.txt")
    (tmp_path / "notes.txt").write_text("clean again\n")
    assert hygiene.scan(tmp_path, terms(PROBE)).problems == ["notes.txt (staged):1: private term"]


def test_a_clean_repository_passes(tmp_path: Path, terms: Terms) -> None:
    (tmp_path / "README.md").write_text("A fictional project.\n")
    _git(tmp_path, "init", "-q", "-b", "main")
    _git(tmp_path, "add", "README.md")
    _git(tmp_path, "commit", "-q", "-m", "docs: a readme\n\nA plain body.")
    (tmp_path / "untracked.txt").write_text(f"{PROBE}\n")
    assert hygiene.scan(tmp_path, frozenset()).problems == []
    assert hygiene.scan(tmp_path, terms(PROBE)).problems == ["untracked.txt:1: private term"]


def test_a_repository_with_no_commits_yet_passes(tmp_path: Path, terms: Terms) -> None:
    _git(tmp_path, "init", "-q", "-b", "main")
    for full in (False, True):
        assert hygiene.scan(tmp_path, terms(PROBE), full=full) == hygiene.Result([], [])


def test_a_change_left_unstaged_is_read(repo: Path, terms: Terms) -> None:
    _commit(repo, "docs: notes", {"notes.txt": "clean\n"})
    _push(repo)
    listed = terms(PROBE)
    assert hygiene.scan(repo, listed).problems == []
    (repo / "notes.txt").write_text(f"clean\nnow about {PROBE}\n")
    assert hygiene.scan(repo, listed).problems == ["notes.txt:2: private term"]


def test_a_fix_left_unstaged_passes_while_pushed_history_keeps_the_term(
    repo: Path, terms: Terms
) -> None:
    # The index still holds the pushed version, which no commit would record anew.
    _commit(repo, "docs: notes", {"notes.txt": f"about {PROBE}\n"})
    _push(repo)
    (repo / "notes.txt").write_text("clean again\n")
    assert hygiene.scan(repo, terms(PROBE)).problems == []


def test_a_routine_run_reads_a_commit_on_no_remote_and_skips_a_pushed_one(
    repo: Path, terms: Terms
) -> None:
    _commit(repo, f"docs: one\n\nAbout {PROBE}.")
    _push(repo)
    unpushed = _commit(repo, f"docs: two\n\nAbout {PROBE}.")
    assert hygiene.scan(repo, terms(PROBE)) == hygiene.Result(
        [f"commit {unpushed[:12]}, message line 3: private term"], []
    )


def test_a_merge_of_pushed_work_reads_only_what_the_merge_made(repo: Path, terms: Terms) -> None:
    _commit(repo, "docs: a readme", {"README.md": "A fictional project.\n"})
    _push(repo)
    _git(repo, "checkout", "-q", "-b", "upstream")
    _commit(repo, "docs: notes", {"notes.txt": f"about {PROBE}\n"})
    _git(repo, "push", "-q", "origin", "upstream")
    _git(repo, "checkout", "-q", "main")
    _commit(repo, "docs: local", {"local.txt": "clean\n"})
    _git(repo, "merge", "-q", "--no-edit", "upstream")
    listed = terms(PROBE)
    # The pushed term came with the merge's second parent, already pushed: it never fails.
    assert hygiene.scan(repo, listed).problems == []
    # Content the merge itself made, as when resolving a conflict, is read.
    (repo / "resolved.txt").write_text(f"about {PROBE}\n")
    _git(repo, "add", "resolved.txt")
    _git(repo, "commit", "-q", "--amend", "--no-edit")
    _git(repo, "reset", "-q")
    assert hygiene.scan(repo, listed).problems == ["resolved.txt:1: private term"]


def test_a_file_committed_without_the_stage_is_read_as_it_stands_at_head(
    repo: Path, terms: Terms
) -> None:
    _commit(repo, "docs: a readme", {"README.md": "A fictional project.\n"})
    _push(repo)
    _commit(repo, "docs: notes", {"notes.txt": f"about {PROBE}\n"})
    listed = terms(PROBE)
    assert hygiene.scan(repo, listed).problems == ["notes.txt:1: private term"]
    # Fixed and staged but not committed: the commit on no remote still holds the term.
    (repo / "notes.txt").write_text("clean again\n")
    _git(repo, "add", "notes.txt")
    assert hygiene.scan(repo, listed).problems == ["notes.txt (at HEAD):1: private term"]
    _commit(repo, "docs: clean notes")
    assert hygiene.scan(repo, listed).problems == []


def test_a_missing_stamp_or_a_newer_list_or_stage_brings_a_full_scan_that_reads_the_draft(
    repo: Path,
    owners_list: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    _commit(repo, f"docs: one\n\nAbout {PROBE}.")
    _push(repo)
    monkeypatch.setattr(hygiene, "ROOT", repo)
    draft = tmp_path / "COMMIT_DRAFT"
    draft.write_text(f"fix: two\n\nAbout {PROBE}.\n")
    argv = ["--message", str(draft)]
    _stamp(repo).touch()
    _set_time(_stamp(repo), T_STAMP)
    assert hygiene.main(argv) == 1
    assert capsys.readouterr().out.splitlines() == [
        "hygiene: routine run",
        "commit message draft, line 3: private term",
        "hygiene: 1 problem(s)",
    ]

    def full_scan() -> str:
        assert hygiene.main(argv) == 1
        out = capsys.readouterr().out.splitlines()
        assert "commit message draft, line 3: private term" in out
        assert out[-1].startswith("hygiene: 1 hit(s) in pushed history, not failing")
        return out[0]

    _set_time(owners_list, T_LATER)
    assert full_scan() == "hygiene: full scan: the term list changed since the last one"
    _set_time(owners_list, T_LIST)
    _set_time(hygiene.SOURCE, T_LATER)
    assert full_scan() == "hygiene: full scan: the stage changed since the last one"
    _set_time(hygiene.SOURCE, T_SOURCE)
    _stamp(repo).unlink()
    assert full_scan() == "hygiene: full scan: no full scan is recorded yet"


def test_a_full_scan_counts_a_hit_in_a_pushed_message_and_renews_the_stamp(
    repo: Path,
    owners_list: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    pushed = _commit(repo, f"docs: one\n\nAbout {PROBE}.")
    _push(repo)
    monkeypatch.setattr(hygiene, "ROOT", repo)
    assert hygiene.main([]) == 0
    assert capsys.readouterr().out.splitlines()[-2:] == [
        f"commit {pushed[:12]}, message line 3: private term (pushed)",
        "hygiene: 1 hit(s) in pushed history, not failing; record the count for the owner",
    ]
    assert _stamp(repo).exists()
    # The renewed stamp stands for that scan, so the next run is routine.
    assert hygiene.main([]) == 0
    assert capsys.readouterr().out.splitlines() == ["hygiene: routine run", "hygiene: 0 problem(s)"]


def test_a_full_scan_fails_on_a_file_and_leaves_the_stamp_as_it_was(
    repo: Path,
    owners_list: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    _commit(repo, "docs: notes", {"notes.txt": f"about {PROBE}\n"})
    _push(repo)
    monkeypatch.setattr(hygiene, "ROOT", repo)
    _stamp(repo).touch()
    _set_time(_stamp(repo), T_STAMP)
    # A routine run reads only what a commit could still change; the pushed file is not that.
    assert hygiene.main([]) == 0
    for argv, listed_at in ((["--all"], T_LIST), ([], T_LATER)):
        _set_time(owners_list, listed_at)
        assert hygiene.main(argv) == 1
        assert "notes.txt:1: private term" in capsys.readouterr().out.splitlines()
        assert _stamp(repo).stat().st_mtime == T_STAMP


def test_a_scan_with_another_list_never_renews_the_stamp(
    repo: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    other = tmp_path / "other.txt"
    other.write_text("")
    monkeypatch.setattr(hygiene, "ROOT", repo)
    assert hygiene.main(["--terms", str(other)]) == 0
    assert not _stamp(repo).exists()
