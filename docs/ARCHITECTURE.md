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

**Built.** Not yet: Sessions 1–2. Today the repository holds one skill folder,
`travel-itinerary-builder/`, at its root.

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

**Built.** Not yet: Session 2 (`claude plugin validate`, the validator), Session 4 (`claude -p`,
claude.ai). Measured at intake, 2026-11-17: `claude` 2.1.326; uv 0.12.3; Python 3.10.20
installed through uv.

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

**Built.** Not yet: Session 1 (Python, uv, ruff, pytest), Session 2 (the validator).

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

**Built.** Not yet: Session 1 (`scripts/`, `tests/`), Session 2 (the marketplace and
`plugins/`), Session 5 (`evals/`). *Enforced by:* not yet.

## The invariants

1. **Every skill folder conforms to the Agent Skills specification.** *Why:* every target
   loads the folder as the specification defines it. *Enforced by* the `skills` stage (Session
   2).
2. **A skill's names agree everywhere:** its folder, its `SKILL.md` `name`, its plugin folder,
   its `plugin.json` `name` and its marketplace entry, and every plugin folder is listed.
   *Why:* an entry name unlike its manifest name fails at install. *Enforced by* the `plugins`
   stage (Session 2).
3. **A skill's version is the same in its `plugin.json` and its `metadata.version`.** *Why:* the
   copy and zip targets show only the second. *Enforced by* the `skills` stage (Session 2).
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
   by* the `plugins` stage, against a list of the published names (Session 2).
9. **Nothing private enters the repository.** *Why:* the repository is public, and history
   cannot be cleaned without a rewrite. *Enforced by* the hygiene stage (Session 1; until then,
   Session 0's check of the term list): the owner's term list against every file, path and
   commit message, attribution against every commit message, and secrets by their exact shapes.

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

**Built.** Not yet: Session 2.

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

**Built.** Not yet: Session 1 (`format`, `lint`, `tests`, `hygiene`), Session 2 (`skills`,
`plugins`).

## The hygiene stage

**Decided.** The kit's design, copied into Session 1's block: the owner's term list, attribution
in messages, secrets by their exact shapes, `.env` files, and conflict markers, with routine and
full scans and a stamp. Its terms-and-attribution part is ported from the owner's public
repository `FairCat-GD/krita-art-mcp`, relicensed here under MIT by the owner; the rest is built
here. Every part is falsified here.

**Built.** Not yet: Session 1.

## travel-itinerary-builder

**Decided.** A day-by-day itinerary for one city, from an interview, web research and a PDF.
Its targets are Claude Code, Codex, claude.ai and any agent that loads `SKILL.md`, and where a
capability is missing it says what it does instead; its minimum environment is stated in
`compatibility` (wording settled in Session 3). Version 1.0.1 after the restructure, 1.1.0
after the review's fixes.

**Built.** Version 1.0 in its frontmatter, at the repository root, as first published
(2026-07-22). The audit is `docs/spec/REVIEW-2026-11-17.md`. Packaging and version: not yet,
Session 2; targets: not yet, Session 3.

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
| Hygiene | `verify`, with the drafted commit message; in full when the term list or the stage changes | Private terms in files, paths and messages; attribution in messages; secrets by their exact shapes; conflict markers | Images and binaries; a term joined inside one lowercase run; attribution in files; a home-directory path; a secret of any other shape |
| Evals | Where a block names them | A skill's behaviour on fixed cases, judged by the owner and `checks.py` | Cases outside the set; targets not run |
| By hand | Recorded in done-notes | Installs, claude.ai, a whole interview | Anything not written down; what nobody checked goes to the backlog |

Not yet: Sessions 1, 2 and 5 build these.

## Packaging

**Decided.**
- **Claude Code:** `/plugin marketplace add FairCat-GD/claude-skills`, then
  `/plugin install <skill>@faircat-skills`.
- **Codex:** the skill folder copied to `~/.agents/skills/` or `.agents/skills/`.
- **claude.ai:** a zip with the skill folder at its root, uploaded as a custom skill.
- **Other agents:** the skill folder copied into the agent's skills directory.
- **Releases:** a skill's version moves in its own session; crux-finder 1.0.0 is tagged
  `crux-finder--v1.0.0`. Pushes and tags are each the owner's yes.

**Built.** Not yet: Session 2 (the marketplace), Session 4 (the claude.ai zip).

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

Filled in by Session 1, from its first green `verify`.

## Decision log

None yet.
