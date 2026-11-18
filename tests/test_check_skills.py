import json
from pathlib import Path

import pytest

import check_skills

NAME = "tide-tables"


def _skill(
    root: Path,
    *,
    body: str = "Read `references/notes.md` before the first answer.\n",
    version: str | None = '"0.3.0"',
    plugin_version: str = "0.3.0",
) -> Path:
    # A fictional skill in its plugin, sound unless a test changes it.
    folder = root / "plugins" / NAME / "skills" / NAME
    (folder / "references").mkdir(parents=True)
    meta = "" if version is None else f"metadata:\n  version: {version}\n"
    frontmatter = f"---\nname: {NAME}\ndescription: Reads tide tables.\nlicense: MIT\n{meta}---\n"
    (folder / "SKILL.md").write_text(f"{frontmatter}\n{body}", encoding="utf-8")
    (folder / "references" / "notes.md").write_text("Notes.\n", encoding="utf-8")
    manifest = root / "plugins" / NAME / ".claude-plugin" / "plugin.json"
    manifest.parent.mkdir(parents=True)
    manifest.write_text(json.dumps({"name": NAME, "version": plugin_version}), encoding="utf-8")
    return folder


def test_a_sound_skill_passes(tmp_path: Path) -> None:
    _skill(tmp_path)
    assert check_skills.check(tmp_path) == []


def test_no_skill_folder_fails(tmp_path: Path) -> None:
    (tmp_path / "plugins").mkdir()
    assert check_skills.check(tmp_path) == [
        "no skill folder: each skill lives in plugins/<plugin>/skills/<skill>/"
    ]


def test_a_skill_folder_without_skill_md_fails(tmp_path: Path) -> None:
    (_skill(tmp_path) / "SKILL.md").unlink()
    assert check_skills.check(tmp_path) == [f"plugins/{NAME}/skills/{NAME}: no SKILL.md"]


def test_a_reference_skill_md_does_not_link_fails(tmp_path: Path) -> None:
    folder = _skill(tmp_path)
    (folder / "references" / "extra.md").write_text("More.\n", encoding="utf-8")
    assert check_skills.check(tmp_path) == [
        f"plugins/{NAME}/skills/{NAME}/references/extra.md: not linked from SKILL.md"
    ]


@pytest.mark.parametrize(
    "body",
    [
        "See [the notes](references/notes.md).\n",
        "See references/notes.md.\n",
        "See `references/notes.md#tides`.\n",
        "See [the notes](./references/notes.md).\n",
    ],
)
def test_a_reference_named_by_its_path_is_linked(tmp_path: Path, body: str) -> None:
    _skill(tmp_path, body=body)
    assert check_skills.check(tmp_path) == []


def test_references_inside_a_url_or_a_longer_word_are_not_named(tmp_path: Path) -> None:
    body = (
        "Read `references/notes.md`. Sources: https://example.org/references/tips, "
        "docs/references/old.md and the cross-references/index.\n"
    )
    _skill(tmp_path, body=body)
    assert check_skills.check(tmp_path) == []


def test_a_named_reference_that_is_missing_fails(tmp_path: Path) -> None:
    _skill(tmp_path, body="Read `references/notes.md`, then `references/gone.md`.\n")
    assert check_skills.check(tmp_path) == [
        f"plugins/{NAME}/skills/{NAME}/SKILL.md: names references/gone.md, which is missing"
    ]


def test_a_dotfile_under_references_is_skipped(tmp_path: Path) -> None:
    folder = _skill(tmp_path)
    (folder / "references" / ".DS_Store").write_bytes(b"\0")
    assert check_skills.check(tmp_path) == []


def test_a_dot_folder_is_no_plugin_or_skill(tmp_path: Path) -> None:
    folder = _skill(tmp_path)
    (tmp_path / "plugins" / ".trash" / "skills" / "old").mkdir(parents=True)
    (folder.parent / ".cache").mkdir()
    assert check_skills.skill_folders(tmp_path) == [folder]
    assert check_skills.check(tmp_path) == []


def test_skill_md_at_its_own_limit_fails(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    folder = _skill(tmp_path)
    lines = check_skills.line_count((folder / "SKILL.md").read_text(encoding="utf-8"))
    monkeypatch.setitem(check_skills.LINE_LIMITS, NAME, lines + 1)
    assert check_skills.check(tmp_path) == []
    monkeypatch.setitem(check_skills.LINE_LIMITS, NAME, lines)
    assert check_skills.check(tmp_path) == [
        f"plugins/{NAME}/skills/{NAME}/SKILL.md: {lines} lines; it must stay under {lines}"
    ]


@pytest.mark.parametrize("own", [None, check_skills.SPEC_LINES + 100])
def test_the_specification_limit_holds_without_a_lower_row(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, own: int | None
) -> None:
    # A skill with no row, or with a row above the specification's, still stops at 500.
    if own is not None:
        monkeypatch.setitem(check_skills.LINE_LIMITS, NAME, own)
    padding = "line\n" * check_skills.SPEC_LINES
    folder = _skill(tmp_path, body=f"Read `references/notes.md`.\n{padding}")
    lines = check_skills.line_count((folder / "SKILL.md").read_text(encoding="utf-8"))
    assert check_skills.check(tmp_path) == [
        f"plugins/{NAME}/skills/{NAME}/SKILL.md: {lines} lines; "
        f"it must stay under {check_skills.SPEC_LINES}"
    ]


def test_a_metadata_version_unlike_the_plugins_fails(tmp_path: Path) -> None:
    _skill(tmp_path, plugin_version="0.3.1")
    assert check_skills.check(tmp_path) == [
        f"plugins/{NAME}/skills/{NAME}/SKILL.md: metadata.version 0.3.0 is not the plugin's 0.3.1"
    ]


def test_no_metadata_version_fails(tmp_path: Path) -> None:
    _skill(tmp_path, version=None)
    assert check_skills.check(tmp_path) == [
        f"plugins/{NAME}/skills/{NAME}/SKILL.md: no metadata.version"
    ]


def test_a_plugin_without_a_manifest_fails(tmp_path: Path) -> None:
    _skill(tmp_path)
    (tmp_path / "plugins" / NAME / ".claude-plugin" / "plugin.json").unlink()
    assert check_skills.check(tmp_path) == [f"plugins/{NAME}/.claude-plugin/plugin.json: missing"]


@pytest.mark.parametrize("version", ['"0.3.0"', "'0.3.0'", "0.3.0"])
def test_metadata_reads_the_block_form_quoted_or_not(version: str) -> None:
    text = f"---\nname: x\nmetadata:\n  version: {version}\n  stage: draft\n---\nversion: 9\n"
    assert check_skills.metadata(text) == {"version": "0.3.0", "stage": "draft"}


def test_metadata_reads_past_a_blank_line_in_its_block() -> None:
    text = '---\nname: x\nmetadata:\n\n  version: "0.3.0"\nlicense: MIT\n---\n'
    assert check_skills.metadata(text) == {"version": "0.3.0"}


def test_metadata_reads_no_other_field_as_its_own() -> None:
    # Another field's map is not metadata, and the flow form reads as none, so it fails the check.
    text = "---\nname: x\nnotes:\n  version: 9.9.9\nmetadata: {version: 0.3.0}\n---\n"
    assert check_skills.metadata(text) == {}


@pytest.mark.parametrize(
    ("text", "lines"), [("", 0), ("a", 1), ("a\n", 1), ("a\nb", 2), ("a\fb\u2028c\n", 1)]
)
def test_lines_are_counted_at_newlines_only(text: str, lines: int) -> None:
    assert check_skills.line_count(text) == lines
