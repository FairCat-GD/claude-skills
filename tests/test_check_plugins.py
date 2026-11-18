import json
from pathlib import Path

import pytest

import check_plugins

NAME = "tide-tables"
SOURCE = f"./plugins/{NAME}"


@pytest.fixture(autouse=True)
def published(monkeypatch: pytest.MonkeyPatch) -> None:
    # The fictional plugin stands in for the published ones.
    monkeypatch.setattr(check_plugins, "PUBLISHED", (NAME,))


def _write(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data), encoding="utf-8")


def _marketplace(root: Path, entries: list[dict], name: str = "faircat-skills") -> None:
    _write(
        root / ".claude-plugin" / "marketplace.json",
        {"name": name, "owner": {"name": "A. Maintainer"}, "plugins": entries},
    )


def _plugin(root: Path, folder: str, *, name: str | None = None, skills: list[str] | None = None):
    name = folder if name is None else name
    _write(root / "plugins" / folder / ".claude-plugin" / "plugin.json", {"name": name})
    for skill in [name] if skills is None else skills:
        (root / "plugins" / folder / "skills" / skill).mkdir(parents=True)


def _sound(root: Path) -> None:
    _plugin(root, NAME)
    _marketplace(root, [{"name": NAME, "source": SOURCE}])


def test_a_sound_marketplace_passes(tmp_path: Path) -> None:
    _sound(tmp_path)
    assert check_plugins.check(tmp_path) == []


def test_a_missing_marketplace_fails(tmp_path: Path) -> None:
    _plugin(tmp_path, NAME)
    assert check_plugins.check(tmp_path) == [".claude-plugin/marketplace.json: missing"]


def test_a_renamed_marketplace_fails(tmp_path: Path) -> None:
    _plugin(tmp_path, NAME)
    _marketplace(tmp_path, [{"name": NAME, "source": SOURCE}], name="faircat-skill")
    assert check_plugins.check(tmp_path) == [
        "the marketplace is named faircat-skill; it is published as faircat-skills"
    ]


def test_a_published_name_missing_fails(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    _sound(tmp_path)
    monkeypatch.setattr(check_plugins, "PUBLISHED", (NAME, "kite-weather"))
    assert check_plugins.check(tmp_path) == [
        "published plugin kite-weather: no marketplace entry; a published name is never removed"
    ]


def test_a_plugin_folder_missing_from_the_marketplace_fails(tmp_path: Path) -> None:
    _sound(tmp_path)
    _plugin(tmp_path, "kite-weather")
    assert check_plugins.check(tmp_path) == ["plugins/kite-weather: not listed in the marketplace"]


def test_an_entry_name_unlike_its_manifest_name_fails(tmp_path: Path) -> None:
    _plugin(tmp_path, NAME)
    _marketplace(tmp_path, [{"name": "tide-table", "source": SOURCE}])
    assert check_plugins.check(tmp_path) == [
        f"marketplace entry tide-table: its plugin.json is named {NAME}; the two must agree",
        f"published plugin {NAME}: no marketplace entry; a published name is never removed",
    ]


def test_a_folder_named_unlike_its_manifest_fails(tmp_path: Path) -> None:
    _plugin(tmp_path, "tides", name=NAME)
    _marketplace(tmp_path, [{"name": NAME, "source": "./plugins/tides"}])
    assert check_plugins.check(tmp_path) == [
        f"plugins/tides: its plugin.json is named {NAME}; the folder must be too"
    ]


def test_an_entry_that_sets_a_version_fails(tmp_path: Path) -> None:
    _plugin(tmp_path, NAME)
    _marketplace(tmp_path, [{"name": NAME, "source": SOURCE, "version": "0.3.0"}])
    assert check_plugins.check(tmp_path) == [
        f"marketplace entry {NAME}: sets a version; plugin.json is the one place a version is set"
    ]


@pytest.mark.parametrize(
    "source", [f"plugins/{NAME}", f"{SOURCE}/", "./plugins/", "https://example.org/tides", None]
)
def test_a_source_that_is_not_a_plugin_folder_fails(tmp_path: Path, source: object) -> None:
    _plugin(tmp_path, NAME)
    _marketplace(tmp_path, [{"name": NAME, "source": source}])
    assert check_plugins.check(tmp_path) == [
        f"marketplace entry {NAME}: source {source!r} is not ./plugins/<plugin>",
        f"plugins/{NAME}: not listed in the marketplace",
    ]


def test_a_plugin_without_a_manifest_fails(tmp_path: Path) -> None:
    (tmp_path / "plugins" / NAME / "skills" / NAME).mkdir(parents=True)
    _marketplace(tmp_path, [{"name": NAME, "source": SOURCE}])
    assert check_plugins.check(tmp_path) == [f"plugins/{NAME}/.claude-plugin/plugin.json: missing"]


@pytest.mark.parametrize("skills", [[], ["tides"], [NAME, "kite-weather"]])
def test_a_plugin_without_exactly_its_own_skill_folder_fails(
    tmp_path: Path, skills: list[str]
) -> None:
    _plugin(tmp_path, NAME, skills=skills)
    _marketplace(tmp_path, [{"name": NAME, "source": SOURCE}])
    assert check_plugins.check(tmp_path) == [
        f"plugins/{NAME}: skill folders {sorted(skills)}; the one expected is skills/{NAME}/"
    ]
