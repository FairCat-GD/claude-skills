"""Invariant 5: everything under evals/ imports the standard library only, or its shared code."""

import ast
import sys
from pathlib import Path

EVALS = Path(__file__).resolve().parent.parent / "evals"
# The one module of evals/ that the files under it may import: evals/shared.py.
SHARED = {"shared"}


def outside_the_standard_library(folder: Path) -> list[str]:
    """Each import, in each Python file under the folder, of a module neither the standard library
    nor the shared code holds; and each file that would shadow a standard-library module."""
    found = []
    for path in sorted(folder.rglob("*.py")):
        where = path.relative_to(folder).as_posix()
        # A script's own folder comes first on its path, so a json.py beside it would be imported
        # in place of the standard library's.
        if path.stem in sys.stdlib_module_names:
            found.append(f"{where}: shadows the standard library's {path.stem}")
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom):
                # A relative import names a file beside it, which this test reads too.
                names = [] if node.level else [node.module or ""]
            else:
                continue
            found += [
                f"{where}:{node.lineno}: {name}"
                for name in names
                if name.split(".")[0] not in sys.stdlib_module_names | SHARED
            ]
    return found


def test_everything_under_evals_imports_the_standard_library_only() -> None:
    files = sorted(EVALS.rglob("*.py"))
    assert len(files) >= 4
    assert (EVALS / "shared.py").is_file()
    assert outside_the_standard_library(EVALS) == []


def test_an_import_from_outside_the_standard_library_is_found(tmp_path: Path) -> None:
    (tmp_path / "tool").mkdir()
    (tmp_path / "tool" / "fine.py").write_text("import json\nfrom pathlib import Path\n")
    (tmp_path / "tool" / "bad.py").write_text(
        "import os\nimport yaml\n\n\ndef load():\n    from requests.adapters import HTTPAdapter\n"
    )
    assert outside_the_standard_library(tmp_path) == [
        "tool/bad.py:2: yaml",
        "tool/bad.py:6: requests.adapters",
    ]


def test_the_shared_code_may_be_imported_and_nothing_else_of_evals(tmp_path: Path) -> None:
    (tmp_path / "shared.py").write_text("import re\n")
    (tmp_path / "run.py").write_text("import shared\n")
    (tmp_path / "skill").mkdir()
    (tmp_path / "skill" / "checks.py").write_text(
        "import sys\nimport shared\nfrom shared import fields\nimport run\n"
    )
    assert outside_the_standard_library(tmp_path) == ["skill/checks.py:4: run"]


def test_a_file_named_like_a_standard_library_module_is_found(tmp_path: Path) -> None:
    (tmp_path / "skill").mkdir()
    (tmp_path / "json.py").write_text("")
    (tmp_path / "skill" / "json.py").write_text("")
    (tmp_path / "skill" / "checks.py").write_text("import json\n")
    assert outside_the_standard_library(tmp_path) == [
        "json.py: shadows the standard library's json",
        "skill/json.py: shadows the standard library's json",
    ]
