"""Invariant 5: everything under evals/ imports the standard library only."""

import ast
import sys
from pathlib import Path

EVALS = Path(__file__).resolve().parent.parent / "evals"


def outside_the_standard_library(folder: Path) -> list[str]:
    """Each import, in each Python file under the folder, of a module the standard library lacks."""
    found = []
    for path in sorted(folder.rglob("*.py")):
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
                f"{path.relative_to(folder).as_posix()}:{node.lineno}: {name}"
                for name in names
                if name.split(".")[0] not in sys.stdlib_module_names
            ]
    return found


def test_everything_under_evals_imports_the_standard_library_only() -> None:
    files = sorted(EVALS.rglob("*.py"))
    assert len(files) >= 2
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
