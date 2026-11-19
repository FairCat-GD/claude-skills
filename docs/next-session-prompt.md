Read `SPEC.md` decisions 1, 3, 10, 19, 21, 25, 28; `PDD.md` B, *Scope*, *Inputs*,
*Repo structure*, *Procedure*, *Output format*, *Guardrails*, *Distribution*, *Build order*;
`ARCHITECTURE.md` invariants 2–4, *Context*, *The contract between the layers*, *crux-finder*,
*Packaging*. Then CLAUDE.md, *The session cycle* in docs/DEVELOPMENT-WORKFLOW.md,
docs/ARCHITECTURE.md's overview, invariants and baseline, docs/spec/SESSIONS.md's header, your
block and the previous block's done-note, then this file, and do Session 4: crux-finder, the
skill. 4 covers:
- the skill, `plugins/crux-finder/skills/crux-finder/`, with PDD B's frontmatter plus
  `metadata.version: "0.1.0"`, under 300 lines, and its three references;
- the plugin: `plugin.json` at `0.1.0`, its marketplace entry, its `CHANGELOG.md` `[0.1.0]`;
- the `skills` stage's crux-finder row (under 300 lines, no `scripts/` folder) and
  `crux-finder` among the published names;
- the thin slice: one headless `claude -p` run, one installed run, and the owner's claude.ai
  upload and run;
- the root README listing crux-finder as in development.

Release crux-finder 0.1.0.

## State you need that is not in the specs

- **Round 1 is a home for many skills**: Sessions 0–3 are done; Sessions 4–8 remain.
- **Push status.** `origin/main` holds everything through `review: references inside URLs,
  duplicate marketplace entries, …`. Session 3's commit (travel-itinerary-builder 1.1.0) is
  local and waits for an approved push. Until that push, people who
  install from GitHub still get 1.0.1.
- **What Session 3 left that Session 4 builds on:**
  - **The marketplace has one entry,** `travel-itinerary-builder`, at 1.1.0. crux-finder is
    the second; `PUBLISHED` in `scripts/check_plugins.py` lists only the itinerary skill today.
  - **`LINE_LIMITS` in `scripts/check_skills.py` is still empty.** crux-finder's 300 is its first
    row. The `scripts/` rule (invariant 4) is not built yet.
  - **`compatibility` passes both validators.** The Agent Skills validator at `83021e2` and
    `claude plugin validate --strict` (2.1.326) accepted the itinerary skill's
    `compatibility` field. Whether claude.ai's upload accepts it is unchecked
    (`docs/BACKLOG.md`).
  - **The plugin pattern to copy** is `plugins/travel-itinerary-builder/`:
    - `plugin.json` with `name`, `version`, `description`, `author` (the owner's name),
      `homepage` and `license`;
    - a README with *What it does*, *What it needs*, *Installing* and *Version*;
    - a changelog with an empty `[Unreleased]` and a link reference per version.
- **On this machine:** Homebrew's `pango` and `poppler` are installed from Session 3 (the owner
  approved them, and removing them is the owner's call). crux-finder needs neither.
- **What the spec said that turned out wrong or harder:** nothing in Session 4's ground.
  Session 3's F11 rule could not decide the page size (no page passes the old phone check), so
  the owner chose A4; that touches only the itinerary skill.
- **An older copy of the itinerary skill** appears in the desktop app's skill list as
  `anthropic-skills:travel-itinerary-builder`, likely the owner's earlier claude.ai upload.
  A plugin's own skill must be started by its namespaced command to be sure it is the one that
  runs. The same will hold for crux-finder if a copy is ever uploaded before it is installed.
- **Baseline** (ARCHITECTURE's table): `verify` green with 6 stages, about 6 s with uv's cache
  warm; 102 unit tests passed, 0 skipped; `hygiene --all` green, with 0 hits in pushed history; 8
  Python files; 1 skill folder, 1 plugin. Session 4 adds a skill folder, a plugin and tests.
- **Not done:** installing from GitHub is still not checked by hand, and travel-itinerary-builder
  1.1.0 has run only in Claude Code (`docs/BACKLOG.md`).

## Watch for

- **The headless run must load only the plugin under test:** `claude -p` from an empty
  temporary folder with `--plugin-dir` and the plugin's absolute path, before anything is
  installed, so this repository's `CLAUDE.md` is not read.
- **`claude plugin marketplace add ./` registers this folder in the owner's user settings.**
  Remove it with `claude plugin marketplace remove faircat-skills` at the end. One call removes
  it and prints its result first; a second call reports "not found".
- **A new check needs its own failing case at its own stage:** 300 lines fails `skills`, a
  `scripts/` folder fails `skills`. Copy the file aside, break it, and copy it back; never use
  `git checkout`.
- **The description is PDD B's, word for word.**
