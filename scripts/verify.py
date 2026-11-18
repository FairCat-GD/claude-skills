"""The gate: named stages, each failing on its own and runnable alone, then a summary.

Usage: uv run scripts/verify.py [stage ...] [--message DRAFT] [--all]
"""

import argparse
import subprocess
import sys
import time
from collections.abc import Callable
from pathlib import Path

from check_plugins import plugin_folders
from check_skills import skill_folders

ROOT = Path(__file__).resolve().parent.parent
PYTHON = sys.executable
# The Agent Skills validator, pinned to a commit of agentskills/agentskills. It needs Python 3.11
# or newer, so uvx runs it on an interpreter of its own; a cold uv cache needs the network.
VALIDATOR = (
    "git+https://github.com/agentskills/agentskills"
    "@83021e2be457a9b6679148719c1f6074f0ad975e#subdirectory=skills-ref"
)


class Options(argparse.Namespace):
    message: Path | None
    all: bool


Stage = Callable[[Options], list[list[str]]]


def _relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _skills(_: Options) -> list[list[str]]:
    validate = ["uvx", "--python", ">=3.11", "--from", VALIDATOR, "skills-ref", "validate"]
    validator = [[*validate, _relative(folder)] for folder in skill_folders(ROOT)]
    return [*validator, [PYTHON, "scripts/check_skills.py"]]


def _plugins(_: Options) -> list[list[str]]:
    # At the marketplace root the CLI does not open the plugins' skill files, so each plugin is
    # validated too. --strict fails on its warnings as well, such as an unrecognised field. The
    # CLI is not pinned and a new release can add a warning, so the stage prints its version first.
    validate = ["claude", "plugin", "validate", "--strict"]
    plugins = [[*validate, _relative(folder)] for folder in plugin_folders(ROOT)]
    version = ["claude", "--version"]
    return [version, [*validate, "."], *plugins, [PYTHON, "scripts/check_plugins.py"]]


def _hygiene(options: Options) -> list[list[str]]:
    draft = [] if options.message is None else ["--message", str(options.message)]
    full = ["--all"] if options.all else []
    return [[PYTHON, "scripts/hygiene.py", *draft, *full]]


STAGES: dict[str, Stage] = {
    "skills": _skills,
    "plugins": _plugins,
    "format": lambda _: [[PYTHON, "-m", "ruff", "format", "--check", "."]],
    "lint": lambda _: [[PYTHON, "-m", "ruff", "check", "."]],
    "tests": lambda _: [[PYTHON, "-m", "pytest"]],
    "hygiene": _hygiene,
}
# The flags only hygiene reads; a run that names them without it would leave them unchecked.
HYGIENE_FLAGS = {"message": "--message", "all": "--all"}


def _call(command: list[str]) -> bool:
    try:
        # stdin closed: no stage reads it, and a tool left waiting on it would hang the gate.
        return subprocess.run(command, cwd=ROOT, stdin=subprocess.DEVNULL).returncode == 0
    except OSError as error:
        print(f"verify: cannot run {command[0]}: {error}")
        return False


def _run(name: str, options: Options) -> tuple[bool, float]:
    print(f"\n== {name} ==", flush=True)
    start = time.monotonic()
    # Every command runs, even after one fails, so each reports its own errors.
    results = [_call(command) for command in STAGES[name](options)]
    return all(results), time.monotonic() - start


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="The gate: named stages, then a summary.")
    parser.add_argument("stages", nargs="*", metavar="stage")
    parser.add_argument("--message", type=Path, help="the drafted commit message, for hygiene")
    parser.add_argument("--all", action="store_true", help="hygiene's full scan, on demand")
    # Stage names may come before or after the flags.
    options = parser.parse_intermixed_args(argv, namespace=Options())
    unknown = [name for name in options.stages if name not in STAGES]
    if unknown:
        print(f"verify: unknown stage(s) {', '.join(unknown)}; stages: {', '.join(STAGES)}")
        return 2
    names = options.stages or list(STAGES)
    given = [flag for attr, flag in HYGIENE_FLAGS.items() if getattr(options, attr)]
    if given and "hygiene" not in names:
        print(f"verify: the hygiene stage reads {' and '.join(given)}; name it too")
        return 2
    if options.message is not None:
        options.message = options.message.resolve()
    results = {name: _run(name, options) for name in names}
    print("\n== summary ==")
    for name, (passed, seconds) in results.items():
        print(f"{name:<9} {'PASS' if passed else 'FAIL'}  {seconds:6.1f}s")
    failed = [name for name, (passed, _) in results.items() if not passed]
    print(f"verify: {'FAIL (' + ', '.join(failed) + ')' if failed else 'PASS'}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
