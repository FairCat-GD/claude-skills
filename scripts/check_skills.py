"""The skills stage's own checks, run after the Agent Skills validator on each skill folder.

The validator checks each folder's frontmatter and name against the specification. These check
what it leaves to this repository: SKILL.md's length, a skill's own limits, that SKILL.md links
every file under references/ and names no reference that is missing, and that metadata.version
repeats the plugin's version.

Usage: uv run scripts/check_skills.py
"""

import json
import re
import sys
from pathlib import Path
from typing import NamedTuple

from check_plugins import plugin_folders, skill_folders_of

ROOT = Path(__file__).resolve().parent.parent
# The specification's limit for SKILL.md, in lines; a SKILL.md must stay under it.
SPEC_LINES = 500


class Limits(NamedTuple):
    """A skill's own limits; the defaults are what the specification allows."""

    # SKILL.md must stay under this many lines; a row above SPEC_LINES never lifts it.
    lines: int = SPEC_LINES
    # Whether the skill folder may hold a scripts/ folder.
    scripts: bool = True


# The one table of per-skill limits, a row per skill that has its own, by skill name.
LIMITS: dict[str, Limits] = {
    # A short SKILL.md, and instructions and references only (invariant 4).
    "crux-finder": Limits(lines=300, scripts=False),
}
# A path into references/ as SKILL.md names it, in a Markdown link or in backticks: at the start
# of a word or after `./`, never inside a URL or a longer word such as cross-references/.
_REFERENCE = re.compile(r"(?:(?<=\./)|(?<![\w/.:-]))references/[^\s`'\"()<>\[\]]+")


def skill_folders(root: Path) -> list[Path]:
    """Every skill folder, plugins/<plugin>/skills/<skill>/, as the plugins stage finds them."""
    return [skill for plugin in plugin_folders(root) for skill in skill_folders_of(plugin)]


def line_count(text: str) -> int:
    # Counted at newlines only, as editors and git count them; a last line without one counts.
    return text.count("\n") + (0 if text == "" or text.endswith("\n") else 1)


def _unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
        return value[1:-1]
    return value


def metadata(text: str) -> dict[str, str]:
    """The frontmatter's metadata map, as strings; {} where there is none.

    Reads only the block form the skills use (`metadata:`, then indented `key: value` lines), so
    any other form reads as no metadata and fails the check rather than passing it.
    """
    lines = text.split("\n")
    if lines[0].rstrip() != "---":
        return {}
    found: dict[str, str] = {}
    inside = False
    for line in lines[1:]:
        if line.rstrip() == "---":
            break
        if not line.strip():
            # A blank line does not end a block in YAML.
            continue
        if not line[:1].isspace():
            inside = line.rstrip() == "metadata:"
            continue
        key, colon, value = line.strip().partition(":")
        if inside and colon:
            found[key.strip()] = _unquote(value.strip())
    return found


def _named_references(text: str) -> set[str]:
    named = set()
    for match in _REFERENCE.findall(text):
        # A fragment or a sentence's last mark is not part of the path.
        named.add(match.split("#", 1)[0].rstrip(".,;:!?"))
    return named


def _reference_files(folder: Path) -> set[str]:
    # A dotfile such as .DS_Store is the system's, not the skill's, and git ignores it.
    return {
        path.relative_to(folder).as_posix()
        for path in (folder / "references").rglob("*")
        if path.is_file() and not any(p.startswith(".") for p in path.relative_to(folder).parts)
    }


def _plugin_version(manifest: Path) -> tuple[str | None, str | None]:
    """The plugin's version, or None and why it cannot be read."""
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except OSError:
        return None, "missing"
    except ValueError as error:
        return None, f"not valid JSON ({error})"
    version = data.get("version") if isinstance(data, dict) else None
    return (version, None) if isinstance(version, str) else (None, "has no version")


def _check_folder(root: Path, folder: Path) -> list[str]:
    where = folder.relative_to(root).as_posix()
    try:
        text = (folder / "SKILL.md").read_text(encoding="utf-8")
    except OSError:
        return [f"{where}: no SKILL.md"]
    problems = []
    own = LIMITS.get(folder.name, Limits())
    limit = min(own.lines, SPEC_LINES)
    lines = line_count(text)
    if lines >= limit:
        problems.append(f"{where}/SKILL.md: {lines} lines; it must stay under {limit}")
    if not own.scripts and (folder / "scripts").is_dir():
        problems.append(
            f"{where}: has a scripts/ folder; this skill ships instructions and references only"
        )
    named = _named_references(text)
    files = _reference_files(folder)
    problems += [f"{where}/{path}: not linked from SKILL.md" for path in sorted(files - named)]
    problems += [
        f"{where}/SKILL.md: names {path}, which is missing" for path in sorted(named - files)
    ]
    manifest = folder.parent.parent / ".claude-plugin" / "plugin.json"
    plugin_version, why = _plugin_version(manifest)
    version = metadata(text).get("version")
    if version is None:
        problems.append(f"{where}/SKILL.md: no metadata.version")
    elif plugin_version is None:
        problems.append(f"{manifest.relative_to(root).as_posix()}: {why}")
    elif version != plugin_version:
        problems.append(
            f"{where}/SKILL.md: metadata.version {version} is not the plugin's {plugin_version}"
        )
    return problems


def check(root: Path) -> list[str]:
    folders = skill_folders(root)
    if not folders:
        return ["no skill folder: each skill lives in plugins/<plugin>/skills/<skill>/"]
    return [problem for folder in folders for problem in _check_folder(root, folder)]


def main() -> int:
    problems = check(ROOT)
    for problem in problems:
        print(problem)
    print(f"check_skills: {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
