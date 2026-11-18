"""The plugins stage's own checks, run after `claude plugin validate` on the marketplace and on
each plugin.

The CLI checks each manifest's shape. These check what it leaves to this repository: every
published name is still there, every plugin folder is listed, a skill's names agree from its
marketplace entry to its skill folder, and no entry sets a version, so plugin.json is the one
place a version is set.

Usage: uv run scripts/check_plugins.py
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# People install by these names, so none is ever renamed or removed.
MARKETPLACE = "faircat-skills"
PUBLISHED = ("travel-itinerary-builder",)
_SOURCE = "./plugins/"


def plugin_folders(root: Path) -> list[Path]:
    """Every plugin folder, plugins/<plugin>/."""
    plugins = root / "plugins"
    if not plugins.is_dir():
        return []
    return sorted(p for p in plugins.iterdir() if p.is_dir() and not p.name.startswith("."))


def _json(path: Path) -> tuple[dict | None, str | None]:
    """The file's JSON object, or None and why it cannot be read."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except OSError:
        return None, "missing"
    except ValueError as error:
        return None, f"not valid JSON ({error})"
    return (data, None) if isinstance(data, dict) else (None, "not a JSON object")


def _check_entry(root: Path, entry: dict, listed: set[str]) -> list[str]:
    name = entry.get("name")
    source = entry.get("source")
    label = f"marketplace entry {name}"
    problems = []
    if "version" in entry:
        problems.append(f"{label}: sets a version; plugin.json is the one place a version is set")
    relative = isinstance(source, str) and source.startswith(_SOURCE)
    folder_name = source[len(_SOURCE) :] if relative else ""
    if not folder_name or "/" in folder_name:
        return [*problems, f"{label}: source {source!r} is not {_SOURCE}<plugin>"]
    listed.add(folder_name)
    where = f"plugins/{folder_name}"
    manifest, why = _json(root / where / ".claude-plugin" / "plugin.json")
    if manifest is None:
        return [*problems, f"{where}/.claude-plugin/plugin.json: {why}"]
    manifest_name = manifest.get("name")
    if name != manifest_name:
        problems.append(f"{label}: its plugin.json is named {manifest_name}; the two must agree")
    if folder_name != manifest_name:
        problems.append(
            f"{where}: its plugin.json is named {manifest_name}; the folder must be too"
        )
    skills = root / where / "skills"
    found = (
        sorted(p.name for p in skills.iterdir() if p.is_dir() and not p.name.startswith("."))
        if skills.is_dir()
        else []
    )
    if found != [manifest_name]:
        problems.append(
            f"{where}: skill folders {found}; the one expected is skills/{manifest_name}/"
        )
    return problems


def check(root: Path) -> list[str]:
    marketplace, why = _json(root / ".claude-plugin" / "marketplace.json")
    if marketplace is None:
        return [f".claude-plugin/marketplace.json: {why}"]
    problems = []
    if marketplace.get("name") != MARKETPLACE:
        problems.append(
            f"the marketplace is named {marketplace.get('name')}; it is published as {MARKETPLACE}"
        )
    entries = marketplace.get("plugins")
    if not isinstance(entries, list) or not all(isinstance(e, dict) for e in entries):
        return [*problems, ".claude-plugin/marketplace.json: plugins is not a list of entries"]
    listed: set[str] = set()
    for entry in entries:
        problems += _check_entry(root, entry, listed)
    problems += [
        f"plugins/{folder.name}: not listed in the marketplace"
        for folder in plugin_folders(root)
        if folder.name not in listed
    ]
    names = {entry.get("name") for entry in entries}
    problems += [
        f"published plugin {name}: no marketplace entry; a published name is never removed"
        for name in PUBLISHED
        if name not in names
    ]
    return problems


def main() -> int:
    problems = check(ROOT)
    for problem in problems:
        print(problem)
    print(f"check_plugins: {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
