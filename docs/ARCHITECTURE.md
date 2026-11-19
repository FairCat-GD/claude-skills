# claude-skills — architecture

How the system is built. **Decided** is the user's: what an intake answered or the user
settled with a session. It changes only with the user, and each change after Session 0 is
logged in the *Decision log*. **Built** is what exists and how, with the decisions a session
made on its own within its scope, each with its why; every session keeps it true. Until
something is built, its Built part says "Not yet: Session <id>", or "Not yet: backlog, <item>"
once the round that planned it closes without it. In the invariants, each rule and its why are
decided and *Enforced by* is built; the debt and the baseline are built only.

## Overview

**Decided.**

```
marketplace  .claude-plugin/marketplace.json      one entry per plugin, relative sources
   │
plugins      plugins/<skill>/                     plugin.json, README.md, CHANGELOG.md
   │
skills       plugins/<skill>/skills/<skill>/      SKILL.md + references/ — what ships
                         ▲
evals        evals/<skill>/                       cases, results, run.py, checks.py
                         (drives a skill only through the claude CLI)

tooling      scripts/verify.py, scripts/hygiene.py, tests/     never shipped
```

The repository is a Claude Code plugin marketplace that holds many Agent Skills, one plugin per
skill. A skill folder is the product: it is what Claude Code loads from the plugin, what Codex
and other agents copy, and what claude.ai receives as a zip. The plugin wraps it with a
manifest, a README that is its user guide, and a changelog. The evals are a skill's harness,
outside the shipped folders. The tooling proves the repository is sound and ships nowhere.

**Built.** The marketplace, `.claude-plugin/marketplace.json`, lists one plugin,
`plugins/travel-itinerary-builder/`, whose skill folder is
`plugins/travel-itinerary-builder/skills/travel-itinerary-builder/`. The tooling:
`scripts/verify.py`, `scripts/hygiene.py`, `scripts/check_skills.py`, `scripts/check_plugins.py`
and `tests/`. The evals: not yet, Session 5.

## Context

**Decided.**
- **The `claude` CLI** (Claude Code). `claude plugin validate` checks the marketplace and each
  plugin; at the marketplace root it does not open the skill files of plugins it lists, so each
  plugin is validated too. `claude plugin marketplace add`, `install`, `details` and
  `marketplace remove` are used by hand. `claude -p` runs a skill headless for the evals. It
  needs the owner's sign-in for `-p`; it is not pinned, so each session that uses it records
  its version.
- **uv and uvx.** uv runs every script and test on the pinned Python; uvx runs the Agent Skills
  validator on its own interpreter. A cold cache needs the network.
- **The Agent Skills validator** (`skills-ref`, from the `agentskills/agentskills` repository),
  pinned to a commit. It checks a skill folder's frontmatter and naming against the
  specification at agentskills.io. Its own README calls it a demonstration; where it and the
  specification disagree, the specification wins and the session stops.
- **claude.ai.** A skill folder zipped with the folder at its root, uploaded by the owner as a
  custom skill. Nothing drives it automatically; every claude.ai run is the owner's, by hand.
- **Codex and other agents.** They load a copied skill folder. No session runs them this round;
  their install steps are documented only.
- **The owner's term list,** `~/.config/hygiene/terms.txt`, outside every repository, shared by
  all the owner's projects. The hygiene stage reads it; nothing in the repository holds it.
- **GitHub.** `origin` is the public `FairCat-GD/claude-skills`. People add the marketplace from
  it and receive a skill's change only when that skill's version moves.

**Built.**
- **`claude plugin validate --strict`** runs in the `plugins` stage, on the marketplace root and
  on each plugin. `--strict` fails on its warnings too, such as an unrecognised field. Its advice
  and its plugin-directory warnings (a missing icon) do not change its verdict, so they print
  without failing. At the root it passed an entry whose name differs from its plugin's
  manifest, so that agreement is the stage's own check. `marketplace add`, `install`, `details`
  and `marketplace remove` were run by hand in Session 2, on this folder.
- **The Agent Skills validator** runs in the `skills` stage on each skill folder, through `uvx`
  on uv's Python 3.12.13, pinned as *Stack and pins* says. At its pinned commit it allows exactly
  the specification's frontmatter fields and checks the name against the folder, so it and the
  specification agree. With uv's cache warm it runs offline; on a cold cache with no network the
  stage fails, with uv's error naming the fetch.
- **GitHub:** `origin` is `https://github.com/FairCat-GD/claude-skills.git`. Adding the
  marketplace from it waits for a push (`docs/BACKLOG.md`).
- Not yet: Session 4 (`claude -p`, claude.ai).

Measured at intake, 2026-11-17, and again in Session 2, 2026-11-18: `claude` 2.1.326; uv 0.12.3;
Python 3.10.20 installed through uv.

## Stack and pins

**Decided** (2026-11-17).
- **Python 3.10** for every script and test, pinned in `.python-version`, because PDD B makes
  3.10 the eval tooling's floor and running on the floor is what proves it. 3.10 left upstream
  support in October 2026; moving the floor is the owner's call.
- **uv** runs everything, with `pyproject.toml` and `uv.lock`. The repository is not a Python
  package.
- **ruff** (format and lint) and **pytest**, development only, pinned in a development group.
- **The standard library only** for everything under `evals/` (invariant 5).
- **The Agent Skills validator** through `uvx`, on Python 3.11 or newer (it requires it),
  pinned to a commit of its repository.

**Built.** Python 3.10.20 through uv 0.12.3: `.python-version` holds `3.10`, and
`pyproject.toml` says `requires-python = ">=3.10"`. The repository is not a package
(`tool.uv.package = false`): uv installs the tools and never builds it. Its `version = "0.0.0"`
is there only because uv refuses a `[project]` table without one; nothing reads it. ruff 0.17.5
and pytest 9.2.0 are pinned exactly in the `dev` group and locked in `uv.lock`. ruff's `include`
is Python files and `pyproject.toml` only, because its default also formats the Python code
blocks inside Markdown, and a skill's Markdown ships as written. ruff selects `E`, `F`, `W`, `I`,
`UP`, `B` and `RUF`, with lines of 100. The validator is pinned to commit
`83021e2be457a9b6679148719c1f6074f0ad975e` of `agentskills/agentskills` (its `main` on
2026-11-18), in `scripts/verify.py`'s `VALIDATOR`. `uvx` runs it on Python 3.11 or newer
(`--python ">=3.11"`), so it is in neither `pyproject.toml` nor `uv.lock`.

## Layout and boundaries

**Decided.**
- **Layout** (Sessions 1, 2, 4 and 5 create it; the names are fixed, the files inside are each
  session's):
  - `.claude-plugin/marketplace.json`: the marketplace.
  - `plugins/<skill>/`: one plugin per skill, holding `.claude-plugin/plugin.json`, `README.md`,
    `CHANGELOG.md` and `skills/<skill>/`.
  - `plugins/<skill>/skills/<skill>/`: the skill folder, `SKILL.md` and `references/`.
  - `evals/<skill>/`: `cases/<id>/` (`input.md`, `gold.md`), `results/<id>/` (`run-N.md`,
    `claude-ai.md`, `review.md`), `run.py`, `checks.py`.
  - `scripts/`: `verify.py`, `hygiene.py`.
  - `tests/`: tests of the scripts and of each skill's eval tooling; `tests/fixtures/`.
  - `docs/`: the workflow's documents.
- **Boundaries:**
  - A skill folder holds only what ships, and refers only to files inside itself, one level
    deep from `SKILL.md`.
  - Nothing under `plugins/` refers to `evals/`, `scripts/` or `tests/`.
  - `evals/` reaches a skill only through the `claude` CLI or a zip, never by importing or
    reading it as code.
  - `verify` never runs the evals.

**Built.**
- `.claude-plugin/marketplace.json`, and `plugins/travel-itinerary-builder/` with
  `.claude-plugin/plugin.json`, `README.md`, `CHANGELOG.md` and `skills/travel-itinerary-builder/`
  (`SKILL.md` and four files under `references/`).
- `scripts/` holds `verify.py`, `hygiene.py`, `check_skills.py` and `check_plugins.py`, all
  standard library only. The two checks are named for their stages with a `check_` prefix, so
  neither reads as the `plugins/` folder on the import path.
- `tests/` holds `test_verify.py`, `test_hygiene.py`, `test_check_skills.py`,
  `test_check_plugins.py` and `fixtures/terms.txt`, a term list of three fictional words. The
  check tests build fictional plugin trees in a temporary folder. The tests import the scripts
  through pytest's `pythonpath`.
- Not yet: Session 5 (`evals/`).

*Enforced by,* in part:
- The `skills` stage holds a skill folder's references one level deep from `SKILL.md`: every file
  under `references/` is linked from `SKILL.md`, and every `references/` path it names exists.
- The `plugins` stage holds the shape of `plugins/`: every folder listed, each holding one skill
  folder of its plugin's name.
- The last read of each diff covers the rest: that nothing under `plugins/` refers to `evals/`,
  `scripts/` or `tests/`, and that `evals/` reaches a skill only through the CLI or a zip.

## The invariants

1. **Every skill folder conforms to the Agent Skills specification.** *Why:* every target
   loads the folder as the specification defines it. *Enforced by* the `skills` stage: the Agent
   Skills validator on every skill folder.
2. **A skill's names agree everywhere:** its folder, its `SKILL.md` `name`, its plugin folder,
   its `plugin.json` `name` and its marketplace entry, and every plugin folder is listed.
   *Why:* an entry name unlike its manifest name fails at install. *Enforced by* the `plugins`
   stage (`scripts/check_plugins.py`): each entry's name equals its manifest's and its folder's,
   the plugin holds one skill folder of that name, and every plugin folder is listed. The
   validator in the `skills` stage holds `SKILL.md`'s `name` equal to its folder.
3. **A skill's version is the same in its `plugin.json` and its `metadata.version`.** *Why:* the
   copy and zip targets show only the second. *Enforced by* the `skills` stage
   (`scripts/check_skills.py`).
4. **crux-finder ships no scripts and needs no network or dependencies.** *Why:* PDD B,
   *Scope*. *Enforced by* the `skills` stage, which fails on a `scripts/` folder (Session 4).
5. **Everything under `evals/` imports the standard library only.** *Why:* PDD B, *Scope*.
   *Enforced by* a test (Session 5).
6. **Neither the runner nor the session under test reads `gold.md`.** *Why:* a run that sees the
   answer proves nothing. *Enforced by* a test that `run.py` never opens it, and by each run's
   isolation, measured (Session 5).
7. **Each `gold.md` is committed before any file under its `results/<id>/`, and names who
   approved it.** *Why:* gold written after the results could be fitted to them. *Enforced by*
   `checks.py`, from `git log` (Session 5).
8. **Published names are never renamed:** the marketplace `faircat-skills`, and each plugin's and
   skill's name. *Why:* people install by them, and a rename strands their install. *Enforced
   by* the `plugins` stage, against the published names in `scripts/check_plugins.py`
   (`MARKETPLACE` and `PUBLISHED`); a plugin's skill folder takes its name, so the same check
   holds the skill's.
9. **Nothing private enters the repository.** *Why:* the repository is public, and history
   cannot be cleaned without a rewrite. *Enforced by* the hygiene stage of `verify`
   (`scripts/hygiene.py`): the owner's term list against every file, path and commit message,
   attribution against every commit message, secrets by their exact shapes, `.env` files and
   conflict markers; the last read of each diff covers what it cannot see.

## The contract between the layers

**Decided.**
- **Marketplace to plugin:** each entry has `name` and a relative `source`
  (`./plugins/<skill>`), and no `version`, so the plugin's own `plugin.json` is the one place a
  version is set. Install is `<skill>@faircat-skills`.
- **Plugin to skill:** one skill per plugin, in `skills/<skill>/`; the plugin and the skill have
  the same name, so the skill runs as `/<skill>:<skill>` or by its description.
- **A version** lives in `plugin.json` and is repeated as `metadata.version` in `SKILL.md`. A
  session that changes a skill's shipped files bumps both, and adds the plugin's changelog
  entry.
- **Licence:** `license: MIT` in every `SKILL.md` and `plugin.json`.
- **Display fields** (settled 2026-11-18): each `plugin.json` also carries `author`, the owner's
  name, and `homepage`, the plugin's README on GitHub; no keywords.

**Built.**
- The marketplace's one entry is `{"name": "travel-itinerary-builder", "source":
  "./plugins/travel-itinerary-builder"}`. It carries no description, so a plugin's description
  is set once, in its `plugin.json`, and `claude plugin validate --strict` accepts it so.
- The marketplace's own description, under `metadata`, is the root README's first sentence. The
  plugin's is the first sentence of its `SKILL.md` description. Both were the owner's choice.
- `plugin.json` holds `name`, `version`, `description`, `author`, `homepage` and `license`.
  `SKILL.md` holds `name`, `description`, `license` and `metadata.version`.
- The `plugins` stage fails an entry that sets a version or a source other than
  `./plugins/<plugin>`. The `skills` stage fails a `metadata.version` unlike its plugin's.

## The data layer

**Decided.**
- **Entities and storage:** plain Markdown files in git. A case is `evals/<skill>/cases/<id>/`
  with `input.md` (real cases carry `source:` and `license:` frontmatter) and `gold.md`
  (frontmatter `crux`, `type`, `crux_for`, `approved_by`). A result is
  `evals/<skill>/results/<id>/` with `run-N.md`, `claude-ai.md` and `review.md`. Cases are
  permanent; results are rewritten by each cycle as Session 7 settles, with git keeping the
  earlier ones.
- **Evolution:** the formats are PDD B's; a change to one is an amendment with the owner.
- **Machine identifiers, never renamed:** the marketplace name `faircat-skills`; the plugin
  and skill names `travel-itinerary-builder` and `crux-finder`; the case ids once results exist.

**Built.** Not yet: Sessions 5 and 6.

## verify

**Decided.** `uv run scripts/verify.py` runs named stages, each failing on its own and runnable
alone by name, then a summary; `--message <draft>` gives `hygiene` the drafted commit message.
One command serves every commit, docs only or not.
- **`skills`:** the Agent Skills validator on every skill folder; `SKILL.md` under 500 lines,
  and under each skill's own lower limit where it has one (crux-finder: 300); every file under
  `references/` linked from `SKILL.md`; `metadata.version` equal to the plugin's version;
  crux-finder has no `scripts/` folder. The per-skill limits are one table in the stage.
- **`plugins`:** `claude plugin validate` on the marketplace root and on each plugin; every
  plugin folder listed; each entry name equal to its manifest name; every published name
  present.
- **`format`** and **`lint`:** ruff, on every Python file.
- **`tests`:** pytest.
- **`hygiene`:** *The hygiene stage*, below.

**Built.** `scripts/verify.py`. Its `STAGES` maps each name to the commands it runs, in this
order:
- `skills`: the validator (*Stack and pins*) on each skill folder, `plugins/*/skills/*/`, then
  `scripts/check_skills.py`. That checks:
  - that there is at least one skill folder;
  - that `SKILL.md` is under its limit: the specification's, `SPEC_LINES` (500), or the skill's
    own row in `LINE_LIMITS`, the one table of per-skill limits, empty today, where that row is
    lower; a higher row never lifts the specification's. Lines are counted at newlines, as
    hygiene counts them;
  - that every file under `references/` is linked from `SKILL.md`, and every `references/` path
    `SKILL.md` names exists;
  - that `metadata.version` equals `plugin.json`'s `version`.
- `plugins`: `claude --version`, then `claude plugin validate --strict` on `.` and on each
  `plugins/<plugin>/`, then `scripts/check_plugins.py`. That checks:
  - that the marketplace is named `faircat-skills`, and no two entries share a name or a source;
  - that each entry's source is `./plugins/<plugin>` and it sets no version;
  - that its name, its manifest's and its folder's agree, and the plugin holds one skill folder,
    of that name;
  - that every folder under `plugins/` is listed, and every name in `PUBLISHED` has an entry.
- `format`: `ruff format --check .`
- `lint`: `ruff check .`
- `tests`: `pytest`, which reads `testpaths` and its flags from `pyproject.toml`
- `hygiene`: `scripts/hygiene.py`

Each command runs from the root with stdin closed, so no tool, `claude` included, waits on it.
The Python ones run through the interpreter `uv run` gives `verify`; `uvx` and `claude` are found
on `PATH`, and a missing one fails its stage with `verify: cannot run <tool>`. Every stage runs
even after one fails. Then the summary prints PASS or FAIL and the time for each stage, followed
by `verify: PASS` or `verify: FAIL (<stages>)`, and the exit code is 1 on any failure.
`--message <draft>` and `--all` are passed to `hygiene`. A run that gives either without
`hygiene` among its stages exits 2, since the flag would go unchecked. So does an unknown stage.

Every tool skips `.claude/worktrees/` at the root:
- ruff by `extend-exclude`, which is anchored at the project root, and by `.gitignore`;
- pytest by `testpaths` and `--ignore=.claude/worktrees`, since it does not read `.gitignore`;
- hygiene by skipping every path under it, and by git's ignore rules from the root
  `.gitignore`;
- `skills` and `plugins` by reading only `.claude-plugin/` and `plugins/` at the root, and the
  README that `claude plugin validate` reads for its advice: a plugin's own, or for the
  marketplace the one at the root. That advice never changes its verdict.

Decisions made here, each with its why:
- **"Linked" means named by its path,** in a Markdown link or in backticks, because the
  itinerary skill names its references in backticks and a skill's text does not change to suit a
  check. A fragment or a sentence's last mark is not part of the path. A path counts only at the
  start of a word or after `./`, so a URL or a longer word that contains `references/` names
  nothing.
- **A reference `SKILL.md` names but that is missing fails too:** it is a broken link in what
  ships, found by the same comparison.
- **Dotfiles under `references/` are skipped:** the system's `.DS_Store` is no part of the
  skill, and git ignores it.
- **The frontmatter is read without a YAML library,** so the scripts stay standard library only.
  Only `metadata`'s block form is read, blank lines within it included; any other form reads as
  no `metadata.version` and fails rather than passes. The validator parses the whole
  frontmatter, with strictyaml.
- **Folder discovery lives in `check_plugins.py`;** `check_skills.py` and `verify` import it, so
  the stages and their checks never disagree on what a skill or plugin folder is. A dot folder
  is neither.
- **No two entries share a name or a source,** since install would then pick one.
- **An entry that sets a version fails,** which holds *Deliberate decisions*' third bullet.
- **`claude plugin validate` runs with `--strict`,** so an unrecognised or misspelt field fails
  instead of printing a warning. The CLI is not pinned, so a release that adds a warning can
  fail the stage with no change here; the stage prints the CLI's version first, to tell that
  case apart.

## The hygiene stage

**Decided.** The kit's design, copied into Session 1's block: the owner's term list, attribution
in messages, secrets by their exact shapes, `.env` files, and conflict markers, with routine and
full scans and a stamp. Its terms-and-attribution part is ported from the owner's public
repository `FairCat-GD/krita-art-mcp`, relicensed here under MIT by the owner; the rest is built
here. Every part is falsified here.

**Built.** `scripts/hygiene.py` is run by `verify` or alone, as
`uv run scripts/hygiene.py [--terms <list>] [--message <draft>] [--all]`. The terms-and-attribution
part is the port as it was written: the token splitting, the loading of the term list and the
attribution patterns. The rest is built here.
- **Secrets** (`_SECRETS`): the design's shapes, each bounded so that a longer run of its own
  characters is not one. The AWS key is also bounded by base64's alphabet, so a run inside an
  encoded blob or a hash is not one. They are checked in file contents and in commit messages.
- **`.env` files:** any path the run reads named `.env` or `.env.*`, except the three example
  names.
- **Conflict markers:** a line of file contents that starts with seven `<` or `>` and a space.
- **The routine run** reads these paths:
  - those that differ between the index and HEAD, or between the working tree and the index;
  - untracked files that are not ignored;
  - those changed by each commit on no remote (`HEAD --not --remotes`), listed with the
    messages in one `git log` call. A merge lists only the paths that differ from every parent
    (`--diff-merges=combined`): the content it made itself, as in a conflict's resolution. A
    path equal to a parent's came with that parent's history, which is either pushed or read in
    its own commit, so merging pushed work never fails on it.

  Paths under `.claude/worktrees/` at the root are skipped, so a part's checkout is never read.

  For each path it reads its name, its working-tree version, its index version where that
  differs from both the working tree's and HEAD's, and HEAD's version where a commit on no
  remote changed it. It also reads the messages of the commits on no remote, and the draft.
- **The full scan** reads all of that, plus every tracked and untracked-not-ignored path and every
  message reachable from HEAD. It runs with `--all`, or when the stamp
  `$(git rev-parse --git-common-dir)/hygiene-scanned` is missing, or is older than the term list in
  use or than `scripts/hygiene.py`; its first line says why. A hit in a pushed message does not
  fail: it is listed with `(pushed)` and counted on the last line,
  `hygiene: <n> hit(s) in pushed history, not failing; …`.
- **A hit names only its place**, as `<path>:<line>`, `<path> (staged):<line>`,
  `<path> (at HEAD):<line>`, `commit <sha>, message line <n>` or
  `commit message draft, line <n>`, followed by the kind.

Decisions made here, each with its why:
- **The full scan reads everything a routine run reads**, so it is never the weaker of the two.
- **Only a passing full scan with the owner's own list renews the stamp**, so a run with
  `--terms` never stands in for it.
- **Secrets are checked in messages too:** a token pasted into a message is as public as one in a
  file.
- **A symlink is read as its target string**, which is what git records, so nothing outside the
  repository is read.
- **A repository with no commits is compared with the empty tree**, so its staged and untracked
  files are still read. An empty one passes.
- **An index version equal to HEAD's is not read**, because no commit would record it anew. A
  term in pushed history that is fixed in the working tree therefore passes before the fix is
  staged, while one in a commit on no remote is still read, as HEAD's version.
- **Lines are counted at newlines only**, as editors and git count them, so a form feed or a
  Unicode separator never shifts a reported line.
- **git runs with stdin closed**, so it never waits on a terminal.

## travel-itinerary-builder

**Decided.** A day-by-day itinerary for one city, from an interview, web research and a PDF.
Its targets are Claude Code, Codex, claude.ai and any agent that loads `SKILL.md`, and where a
capability is missing it says what it does instead. Version 1.0.1 after the restructure, 1.1.0
after the review's fixes. Settled 2026-11-19:
- **The minimum environment,** in `SKILL.md`'s `compatibility`: "Needs web search. Builds the
  PDF with Python, WeasyPrint and its Pango library where it can run code; delivers the plan in
  chat otherwise. Fonts load from Google Fonts when online."
- **The PDF is A4,** in one column, so it reads on a laptop at fit-to-width and on paper, and on
  a phone by zooming into the column. A phone-sized page was rendered and set aside: it reads
  without zooming on a phone, but as a narrow column on a laptop.
- **The PDF is built with WeasyPrint, else the plan goes to chat** with the reason; there is no
  second PDF library.

**Built.** Version 1.1.0 (2026-11-19), in `plugins/travel-itinerary-builder/`: the skill as
first published (2026-07-22, `1.0.0` in its changelog), with F1's examples on Lisbon, F2's
frontmatter, and F3–F21 of `docs/spec/REVIEW-2026-11-17.md` fixed. The audit's `SKILL.md` line
numbers predate F2, which added two lines, so a line it cites as `:N` was `:N+2` before 1.1.0.
Each missing capability has a stated fallback:
- no question tool: the choice steps asked in chat as numbered options, with "Other" last;
- no WeasyPrint or Pango: `references/output-formats.md`'s *Building the PDF* order (already
  importable, then a virtual environment, then Pango asked for), then chat with the reason;
- no `pdftoppm`: PyMuPDF from pip; neither, or no way to view images: the visual check is
  reported as skipped;
- no network: the fonts fall back to Georgia and Helvetica Neue (measured on macOS), found by
  the font check the skill now runs and reported;
- the weekday: a Python one-liner, or a calendar found by search, instead of GNU `date -d`;
- delivery: the file's path in the working folder, or the environment's own link, instead of
  `computer://` alone.

Decisions made here, each with its why:
- **The Wikipedia link sits on the place's name,** as four of the five places that described it
  already said, and as restaurant names carry their links.
- **A restaurant keeps its Booking line when walk-in,** since the template offers "Walk-in OK"
  as a value and not being able to reserve is worth knowing.
- **One spelling, `(verify)`,** the one used seven times against one.
- **The save-and-hand-over rule lives in `SKILL.md` Phase 5;** `output-formats.md` points at it.
- **On macOS with Homebrew, WeasyPrint finds Pango only with `DYLD_FALLBACK_LIBRARY_PATH` set to
  Homebrew's `lib`,** measured with WeasyPrint 70.0 from uv and 66.0 in a venv on the system's
  Python 3.9; the reference says so.

Its README is its user guide: what it does, what it needs on each target, and its install.

## crux-finder

**Decided.** PDD B, carried into this round by `SPEC.md` with the amendments of its §3: two
positions in, the smallest claim the rest hinges on out, as a report of at most 400 words; no
verdict, no statement about either party; instructions and references only. `SKILL.md` under
300 lines, with `references/procedure.md`, `crux-types.md` and `output-template.md`.

**Built.** Not yet: Session 4.

## The eval harness

**Decided.** PDD B, *Evals*, under `evals/crux-finder/`: ten cases, two runs each through
`run.py` in a fresh session, the owner's review of every run, `checks.py`'s deterministic
checks and summary against the pass bars, and a claude.ai smoke test on three cases. It spends
real model runs, so it runs only where a session's block names it, never in `verify`, one run
at a time. How runs are isolated, and the gaps in the checks, are settled at the start of
Session 5.

**Built.** Not yet: Sessions 5–7.

## Testing strategy — five layers, and what each cannot see

**Decided.** **`verify`** runs named stages, each failing on its own and runnable alone by name,
then a summary: `skills`, `plugins`, `format`, `lint`, `tests`, then `hygiene`. It is green
before every commit. The harness is each skill's eval set. The commands are in `CLAUDE.md`.

**Built.**

| Layer | Runs | Covers | Cannot see |
|---|---|---|---|
| Validators | `verify` (`skills`, `plugins`) | The specification's frontmatter and naming; the manifests; the limits and names in *verify* | Whether a skill behaves well |
| Unit | `verify` (`tests`) | The scripts: hygiene, verify's own checks, the eval tooling | The skills themselves |
| Hygiene | `verify`, with the drafted commit message; in full when the term list or the stage changes | Private terms in files, paths and messages; attribution in messages; secrets by their exact shapes; `.env` files; conflict markers | Images and binaries; a term joined inside one lowercase run; attribution in files; a home-directory path; a secret of any other shape; a file's earlier versions in history |
| Evals | Where a block names them | A skill's behaviour on fixed cases, judged by the owner and `checks.py` | Cases outside the set; targets not run |
| By hand | Recorded in done-notes | Installs, claude.ai, a whole interview | Anything not written down; what nobody checked goes to the backlog |

Built: Validators (the `skills` and `plugins` stages), Unit (`tests/test_verify.py`,
`tests/test_hygiene.py`, `tests/test_check_skills.py`, `tests/test_check_plugins.py`) and
Hygiene. Not yet: Evals, Session 5.

## Packaging

**Decided.**
- **Claude Code:** `/plugin marketplace add FairCat-GD/claude-skills`, then
  `/plugin install <skill>@faircat-skills`.
- **Codex:** the skill folder copied to `~/.agents/skills/` or `.agents/skills/`.
- **claude.ai:** a zip with the skill folder at its root, uploaded as a custom skill.
- **Other agents:** the skill folder copied into the agent's skills directory.
- **Releases:** a skill's version moves in its own session; crux-finder 1.0.0 is tagged
  `crux-finder--v1.0.0`. Pushes and tags are each the owner's yes.

**Built.** The marketplace, checked locally: `claude plugin marketplace add ./` and
`claude plugin install travel-itinerary-builder@faircat-skills` installed it, and
`claude plugin details` listed its one skill at 1.0.1. Adding it from GitHub waits for a push
(`docs/BACKLOG.md`). The itinerary plugin's README gives each target's install, the claude.ai
zip included. travel-itinerary-builder 1.1.0 is untagged. Not yet: Session 4 (a claude.ai
upload, run).

## Deliberate decisions

**Decided.**
- **No type-check stage.** The only code is a few small scripts; ruff and the tests cover them.
- **One command for every commit,** with no docs-only command: `verify` takes seconds here.
- **A version per skill, set only in `plugin.json` and repeated in `SKILL.md`;** the marketplace
  entries carry none, so a skill that did not change is not offered as an update.
- **The evals sit outside `verify`.** They cost real model runs and the owner's review, so a
  block names when they run.

## Known debt, deliberately deferred

None yet.

## Baseline

Measured 2026-11-19 with Python 3.10.20, uv 0.12.3, ruff 0.17.5, pytest 9.2.0, `claude` 2.1.326
and the validator at `83021e2`. The heading carries no version because the repository has none
of its own: each skill has its own version.

| Check | Expected |
|---|---|
| `uv run scripts/verify.py` | green: 6 stages (`skills`, `plugins`, `format`, `lint`, `tests`, `hygiene`), about 6 s with uv's cache warm |
| Unit tests (`tests`) | 102 passed, 0 skipped: 45 in `test_hygiene.py`, 28 in `test_check_skills.py`, 19 in `test_check_plugins.py`, 10 in `test_verify.py` |
| `uv run scripts/verify.py hygiene --all` | green; 0 hits in pushed history |
| Python files (`ruff format --check .`) | 8 |
| Skills and plugins | 1 skill folder, 1 plugin, 1 marketplace entry |

A documentation or refactoring change should not move any of these. If one moves, that is the
finding.

## Decision log

- 2026-11-18, Session 2: *The contract between the layers* gains the plugins' display fields:
  `author`, the owner's name, and `homepage`, the plugin's README on GitHub; no keywords. The
  owner settled it at the start of Session 2.
- 2026-11-19, Session 3: *travel-itinerary-builder* gains its minimum environment (the
  `compatibility` wording), the A4 page in one column, and the WeasyPrint-else-chat order. The
  owner settled them with the session, the page from rendered samples.
