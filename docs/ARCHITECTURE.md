# claude-skills — architecture

How the system is built. **Decided** is the user's: what an intake answered or the user
settled with a session. It changes only with the user, and each change after Session 0 is
logged in the *Decision log*. **Built** is what exists and how, with the decisions a session
made on its own within its scope, each with its why; every session keeps it true. Until
something is built, its Built part says "Not yet: Session <id>", or "Not yet: backlog, <item>"
once the round that planned it closes without it. In the invariants, each rule and its why are
decided and *Enforced by* is built; the debt and the baseline are built only.

Round 1's spec files, cited throughout (`SPEC.md` and its numbered decisions, `PDD.md` as PDD B,
the audit `REVIEW-2026-11-17.md`, and `SESSIONS.md`'s blocks and done-notes), were deleted from
`docs/spec/` when the round closed; git history keeps them, as of the review commit before
`docs: close round 1`. Round 2's, `FEATURE-provenance-tracer.md` and `FEATURE-eval-engine.md`
with their `SESSIONS.md`, are in `docs/spec/` while the round runs; what they decided about how
the repository is built is stated here in full.

## Overview

**Decided.**

```
marketplace  .claude-plugin/marketplace.json      one entry per plugin, relative sources
   │
plugins      plugins/<skill>/                     plugin.json, README.md, CHANGELOG.md
   │
skills       plugins/<skill>/skills/<skill>/      SKILL.md + references/ — what ships
                         ▲
evals        evals/<skill>/                       cases, results, checks.py
             evals/                               one shared runner over `claude plugin eval`
                         (drives a skill only through the claude CLI)

tooling      scripts/verify.py, scripts/hygiene.py, tests/     never shipped
```

The repository is a Claude Code plugin marketplace that holds many Agent Skills, one plugin per
skill. A skill folder is the product: it is what Claude Code loads from the plugin, what Codex
and other agents copy, and what claude.ai receives as a zip. The plugin wraps it with a
manifest, a README that is its user guide, and a changelog. The evals are a skill's harness,
outside the shipped folders; from round 2 every skill's run on one engine, `claude plugin
eval`, through one runner (*The eval harness*). The tooling proves the repository is sound and
ships nowhere.

**Built.** The marketplace, `.claude-plugin/marketplace.json`, lists three plugins,
`plugins/travel-itinerary-builder/`, `plugins/crux-finder/` and `plugins/provenance-tracer/`,
each with its skill folder at `plugins/<skill>/skills/<skill>/`. The tooling:
`scripts/verify.py`, `scripts/hygiene.py`, `scripts/check_skills.py`, `scripts/check_plugins.py`
and `tests/`. The evals: `evals/crux-finder/run.py` and `checks.py`, and crux-finder's ten cases
in `evals/crux-finder/cases/`, with the latest cycle's results in `evals/crux-finder/results/`.

## Context

**Decided.**
- **The `claude` CLI** (Claude Code). `claude plugin validate` checks the marketplace and each
  plugin; at the marketplace root it does not open the skill files of plugins it lists, so each
  plugin is validated too. `claude plugin marketplace add`, `install`, `details` and
  `marketplace remove` are used by hand. `claude -p` runs a skill headless for the evals. It
  needs the owner's sign-in for `-p`; it is not pinned, so each session that uses it records
  its version.
- **`claude plugin eval`** (settled at the round 2 intake, 2026-11-25), the eval engine for
  every skill from round 2: it runs a plugin's cases, each a `prompt.md` and its graders, in
  isolated non-interactive sessions and scores them with its own graders (`regex`, `tool_used`,
  `tool_order`, `file_exists`, `llm`, `baseline`). It reads cases only from a folder inside the
  plugin, it publishes its report to claude.ai unless told not to, and exit 1 means any case
  scored below its threshold. Read from its docs at intake and not yet measured; Session E1
  measures it before anything is built on it, and a measured behaviour unlike the docs is a
  stop. Part of the unpinned CLI, so each session that runs it records the CLI's version.
- **The web,** for provenance-tracer's runs: web search and page fetch, live, so a cycle's
  replies differ for reasons outside the skill, and a case's expected facts carry the date they
  were checked.
- **uv and uvx.** uv runs every script and test on the pinned Python; uvx runs the Agent Skills
  validator on its own interpreter. A cold cache needs the network.
- **The Agent Skills validator** (`skills-ref`, from the `agentskills/agentskills` repository),
  pinned to a commit. It checks a skill folder's frontmatter and naming against the
  specification at agentskills.io. Its own README calls it a demonstration; where it and the
  specification disagree, the specification wins and the session stops.
- **claude.ai.** A skill folder zipped with the folder at its root, uploaded by the owner as a
  custom skill. Nothing drives it automatically; every claude.ai run is the owner's, by hand.
  **Amended mid-Session 7c, with the owner** (2026-11-22): at the owner's word, the session
  itself may run claude.ai in the owner's Chrome, through Claude in Chrome: the upload, each case
  in a fresh chat, the reply taken from claude.ai's own Copy button, and the upload's deletion
  once the owner confirms it. The owner's review of each reply is unchanged.
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
  marketplace from it is not yet checked by hand (`docs/BACKLOG.md`).
- **`claude -p`** ran crux-finder in Session 4, from an empty folder in a temporary directory,
  with no `CLAUDE.md` above it: first with `--plugin-dir` and the plugin's absolute path, then
  with the plugin installed instead, each with `--output-format stream-json --verbose` to show
  which skill ran. It ran under the owner's sign-in and the owner's user settings, so the
  owner's user-level plugins and skills synced from claude.ai loaded beside the plugin under
  test, auto memory was on, and the permission mode was the user's `auto`. The skill read its
  references with the shell, outside the run's folder, and nothing was denied. A marketplace
  added from a local folder loads the plugin in place, not from a copy.
- **`claude -p` isolated,** measured in Session 5 from the run's start event (the stream's
  `system`/`init`, printed before any model call). With `--setting-sources ""`,
  `--strict-mcp-config`, `--no-session-persistence`, `--permission-prompts none` and
  `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`, and the plugin copied to a temporary folder outside the
  repository, a run lists only that copy and Claude Code's built-in plugins and skills, no MCP
  server, the `default` permission mode and no memory paths. Without them, it also listed the
  owner's two user-level plugins, a plugin and twelve skills synced from claude.ai, a claude.ai
  MCP server and the `auto` mode. Under those flags, a read outside the run's folder and the
  copy (given by `--add-dir`) was denied, by Read and by Bash alike, while the skill's references
  in the copy were read. Skills in `~/.claude/skills/` carry no namespace in the start event, so
  they cannot be told from the built-ins there; none loaded under those flags.
- **claude.ai** accepted crux-finder's zip as a custom skill after its security scan, and read
  `license` and `metadata.version` from the frontmatter (it shows License MIT and Version
  0.1.0). An uploaded skill is then synced into the owner's Claude Code sessions as
  `anthropic-skills:<skill>`, beside any plugin of the same name. Session 5 removed the upload
  (claude.ai deletes it with its version history), and the next `claude` start dropped its
  synced copy.
- **claude.ai in Session 7c:** uploads are made on the Plugins page (*Add*, *Upload plugin*),
  which takes a plugin archive or a skill's `.zip`, `.skill` or `SKILL.md`. crux-finder's zip was
  listed as a plugin, "Crux finder", made by the owner, with its one skill, and its version shown as
  "v1", not the `metadata.version`. Each chat read the skill's files before replying. The Copy
  button under a reply gives its Markdown as `text/plain`, which the session read by wrapping
  the page's clipboard calls. *Delete* in the plugin's menu removed it after a "can't be
  undone" prompt, and a `claude` start after that listed no `crux-finder` skill.
- **`claude -p` with the web tools,** measured in Session P1 on provenance-tracer: Session 5's
  isolation flags and `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`, plus `--allowedTools WebSearch
  WebFetch`, the plugin given in place by `--plugin-dir` and `--add-dir`, from an empty folder in
  a temporary directory. The start event listed the plugin and Claude Code's built-ins only, no
  MCP server, the `default` mode and no memory paths.
  - **WebSearch** is among the session's tools, deferred: each run loaded it with ToolSearch
    (`select:WebSearch`) before its first search.
  - **WebFetch** is not among the main session's tools. Every fetch ran inside a built-in
    `web-fetch` subagent (the Agent tool), as a WebFetch call in the subagent's events.
  - **Permissions:** no web call was denied. One Bash call, a local PDF text extraction, was
    denied under `--permission-prompts none`.
  - **The references** were read with Read, or with one shell `cat`, inside the `--add-dir`
    folder.
  - **One read went outside both folders, and was not denied.** A run whose fetch returned a long
    PDF read two files from its own session's tool-results folder, under `~/.claude/projects/`,
    where the CLI had saved that output, even with `--no-session-persistence`. Session 5 recorded
    reads outside the run's folders as denied; this folder is the run's own output, but E1's
    isolation measurement must check it.

Measured at intake, 2026-11-17, and again in Session 2, 2026-11-18: `claude` 2.1.326; uv 0.12.3;
Python 3.10.20 installed through uv. In Session 4, 2026-11-20: `claude` 2.1.328. In Session 5,
2026-11-20, Session 7, 2026-11-21, and Session 7a, 2026-11-22: `claude` 2.1.329. In Session 7b,
2026-11-22: 2.1.329 at the start, and 2.1.330 from the cycle's sixteenth run, the CLI having
updated itself mid-cycle. In Session 7c, 2026-11-22: 2.1.330 throughout. In Session 8,
2026-11-22: 2.1.330. In Session P1, 2026-11-25: 2.1.330.

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
    **Amended at the round 2 intake, with the owner** (2026-11-25), from Session E2 on:
    `cases/<id>/` holds `prompt.md`, its graders and `gold.md`; `results/<id>/` holds
    `run-N.md`, each run's grader verdicts, and `claude-ai.md` and `review.md` where they
    apply; `checks.py`, one per skill. One runner under `evals/`, shared by every skill,
    replaces each skill's `run.py`; its file name and the shared code's are Session E1's.
    Nothing under `plugins/` holds a case.
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
- `.claude-plugin/marketplace.json`, and three plugins, each with `.claude-plugin/plugin.json`,
  `README.md`, `CHANGELOG.md` and its skill folder: `plugins/travel-itinerary-builder/`
  (`SKILL.md` and four files under `references/`), `plugins/crux-finder/` (`SKILL.md` and
  three) and `plugins/provenance-tracer/` (`SKILL.md` and four).
- `scripts/` holds `verify.py`, `hygiene.py`, `check_skills.py` and `check_plugins.py`, all
  standard library only. The two checks are named for their stages with a `check_` prefix, so
  neither reads as the `plugins/` folder on the import path.
- `tests/` holds `test_verify.py`, `test_hygiene.py`, `test_check_skills.py`,
  `test_check_plugins.py`, `test_crux_finder_run.py`, `test_crux_finder_checks.py`,
  `test_evals_stdlib.py` and `fixtures/terms.txt`, a term list of three fictional words. The
  check tests build fictional plugin trees in a temporary folder. The tests import the scripts
  through pytest's `pythonpath`, and the eval scripts by their paths, since a folder named
  `crux-finder` is no package and each skill's evals will have a `run.py` of its own.
- `evals/crux-finder/` holds `run.py` and `checks.py`, standard library only, and `cases/`, the
  ten cases (*The data layer*), and `results/`, the latest cycle's. `run.py` reaches the skill only
  through the CLI: it copies the plugin folder, without reading the skill's files, to where the
  run can load it.

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
4. **crux-finder and provenance-tracer ship no scripts, and crux-finder needs no network or
   dependencies.** *Why:* PDD B, *Scope*, and provenance-tracer's spec, *Scope* (it needs web
   search and page fetch, and nothing else). Amended at the round 2 intake, with the owner
   (2026-11-25), adding provenance-tracer. *Enforced by* the `skills` stage
   (`scripts/check_skills.py`): crux-finder's row in `LIMITS`
   forbids a `scripts/` folder and any file but `SKILL.md` and Markdown under `references/`, and
   provenance-tracer's row the same, each `Limits(lines=300, scripts=False)`, held by
   `tests/test_check_skills.py`. crux-finder needing no network or dependencies is held by the
   last read of each diff.
5. **Everything under `evals/` imports the standard library only.** *Why:* PDD B, *Scope*.
   *Enforced by* `tests/test_evals_stdlib.py`: every import in every Python file under `evals/`,
   read with `ast`, names a module in `sys.stdlib_module_names`.
6. **Neither the runner nor the session under test reads `gold.md`.** *Why:* a run that sees the
   answer proves nothing. *Enforced by* `tests/test_crux_finder_run.py`, which runs `run.py`
   against a stub with an audit hook on every file it opens and gold.md made unreadable; and by
   each run's isolation, measured in Session 5 (*Context*) and checked on every run from its
   start event, before anything is written (*The eval harness*). **Amended at the round 2
   intake, with the owner** (2026-11-25), for the shared runner: the session under test reads
   neither `gold.md` nor a case's graders, and the runner never opens `gold.md` and copies the
   graders unopened. *Enforced by,* for the shared runner: not yet, Session E1; whether each
   run's isolation can still be checked on every run is measured there.
7. **Each `gold.md` is committed before any file under its `results/<id>/`, and names who
   approved it.** *Why:* gold written after the results could be fitted to them. *Enforced by*
   `evals/crux-finder/checks.py`, from git: gold.md committed, in the parent of the first commit
   under `results/<id>/` and unchanged since, in the commit each run names and unchanged since,
   with no uncommitted change while results exist, and with a non-empty `approved_by`.
8. **Published names are never renamed:** the marketplace `faircat-skills`, and each plugin's and
   skill's name. *Why:* people install by them, and a rename strands their install. *Enforced
   by* the `plugins` stage, against the published names in `scripts/check_plugins.py`
   (`MARKETPLACE` and `PUBLISHED`); a plugin's skill folder takes its name, so the same check
   holds the skill's. `tests/test_check_plugins.py` holds `PUBLISHED` to the three names.
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
- The marketplace's three entries are `{"name": "<skill>", "source": "./plugins/<skill>"}`, for
  `travel-itinerary-builder`, `crux-finder` and `provenance-tracer`. They carry no description, so a plugin's
  description is set once, in its `plugin.json`, and `claude plugin validate --strict` accepts
  it so.
- The marketplace's own description, under `metadata`, is the root README's first sentence. The
  plugin's is the first sentence of its `SKILL.md` description. Both were the owner's choice.
- `plugin.json` holds `name`, `version`, `description`, `author`, `homepage` and `license`.
  `SKILL.md` holds `name`, `description`, `license` and `metadata.version`, and the itinerary
  skill's also `compatibility`.
- The `plugins` stage fails an entry that sets a version or a source other than
  `./plugins/<plugin>`. The `skills` stage fails a `metadata.version` unlike its plugin's.

## The data layer

**Decided.**
- **Entities and storage:** plain Markdown files in git. A case is `evals/<skill>/cases/<id>/`
  with `input.md` (real cases carry `source:` and `license:` frontmatter) and `gold.md`
  (frontmatter `crux`, `type`, `crux_for`, `approved_by`). A result is
  `evals/<skill>/results/<id>/` with `run-N.md`, `claude-ai.md` and `review.md`. Cases are
  permanent; each cycle replaces the results, with git keeping the earlier ones and each
  done-note its summary table (settled with the owner at the start of Session 7).
- **Evolution:** the formats are PDD B's; a change to one is an amendment with the owner.
- **Amended at the start of Session 5, with the owner** (2026-11-20):
  - `review.md` records, per output, `crux_match`, `type_match` and `people_statement` (yes or
    no) and a one-line `note`, as PDD B has it, plus `same_crux_as_run_1` from run 2 on, and
    `gate_fired` and `no_conflict_reported` where they apply: the three bars that had no field.
  - The prompt is input.md's body, its frontmatter left out, and quotes are checked against the
    same body.
- **Amended at the start of Session 6, with the owner** (2026-11-20), where PDD B left open how
  two cases are judged:
  - **The one-sided case's gold** is the crux and type expected had B's own words been given,
    and the gate must fire. A run that asks for B's words and writes no report matches on crux
    and type; a run that reports instead is judged against the crux.
  - **The no-conflict case's gold** is no crux, with `type: none` and `crux_for: none`. Only a
    **No crux** report matches; a Framing crux meets PDD B's no-conflict bar but not crux or
    type.
- **Amended mid-Session 6, with the owner** (2026-11-20): the real set holds one case, the
  public-domain debate excerpt, where PDD B has two. The owner had no dispute of their own to
  write up and asked the session to write a serious one; being fictional, it is a synthetic
  case, with no `license:`. A second real case is in `docs/BACKLOG.md`.
- **Amended mid-Session 7, with the owner** (2026-11-22): how one cycle's review was made. The
  owner reviewed the first case in the chat; for the other nine, at the owner's request, each
  run's fields and note were drafted for the owner against gold.md and its note, and the owner
  confirmed every row before `review.md` recorded it. `review.md` holds the owner's answers either way. Each
  cycle's session asks at its start how its review is made.
- **Settled at the start of Session 7a, with the owner** (2026-11-22): its review was made as
  Session 7's ended, each run's fields and note drafted against gold.md and its note by a fresh
  reader that saw no earlier verdict, and every row confirmed or corrected by the owner before
  `review.md` recorded it.
- **Settled at the start of Session 7b, with the owner** (2026-11-22): its review was made as
  Session 7a's, for the cycle's runs and for any claude.ai replies alike.
- **Settled at the start of Session 7c, with the owner** (2026-11-22): its review was made as
  Session 7b's, for the cycle's runs and the claude.ai replies alike.
- **Amended at the round 2 intake, with the owner** (2026-11-25), for both skills, from Session
  E2 on (crux-finder) and P2 on (provenance-tracer); until E2, crux-finder's formats are as
  above:
  - **A case** is `prompt.md` (the engine's frontmatter, then the prompt: for crux-finder, the
    input's body unchanged), its graders, and `gold.md`. `gold.md` is the answer the owner
    approved, in flat `key: value` lines read with no YAML library: crux-finder's four fields;
    for provenance-tracer, the expected labels, the authoring date and the facts it must
    report, each checked on the web at authoring; `approved_by` in both; `source:` and
    `license:` where the input has them. The graders are drawn from it and approved by the
    owner before they are committed. Every provenance-tracer case but the one that tests a
    question tells the run no reply is possible; crux-finder's prompts carry no such line, as
    round 1's runs had none and its one-sided case must be free to ask.
  - **A result** is `results/<id>/run-N.md`: a header (the case, the run, the model, the CLI's
    version, the skill's version, the commit, the date, the cost), the run's tool calls one per
    line (the tool and its query or URL), then the final reply as the run gave it; beside it,
    the run's grader verdicts, every machine path removed. Never a raw trace, the engine's
    HTML report or its JSON. `claude-ai.md` stays as it is, judged by the owner in `review.md`.
  - **The review:** the graders and the skill's `checks.py` decide; each cycle, the owner reads
    every failed verdict and one run per case, and crux-finder's stability; how a correction is
    recorded is asked at the start of Session E2.
  - **crux-finder's ten case ids stay.** Its `real-lincoln-douglas` gold gains its input's
    `source:` and `license:` in E2, after round 1's results are retired and before any new
    one; its three claude.ai replies stay, their cases' `review.md` cut to the `## claude-ai`
    section.
  - **Gold order** is reckoned from the first commit of the results present now, never from a
    results folder's whole history, which keeps retired cycles; a case's graders are unchanged
    since each `run-N.md`'s commit, a check that does not apply to `claude-ai.md`.
- **Machine identifiers, never renamed:** the marketplace name `faircat-skills`; the plugin
  and skill names `travel-itinerary-builder`, `crux-finder` and, from Session P1,
  `provenance-tracer`; the case ids once results exist.

**Built** (the formats, the ten cases and the latest cycle's results).
- **A case's frontmatter** is read as one `key: value` per line, a quoted value unquoted, with
  no YAML library: gold.md's `crux`, `type`, `crux_for` and `approved_by` each on one line.
- **crux-finder's ten cases** (Session 6), one folder each under `evals/crux-finder/cases/`,
  named for the row it fills and its topic (`<type>-<topic>`, `one-sided-…`, `no-conflict-…`,
  `real-…`, and `transcript-…` for the one case named for its form); the id never reaches a
  run, which sees only the body:
  - nine synthetic, fictional, drafted by the session and approved by the owner. Eight are one
    per row of PDD B's synthetic set: `empirical-orchard-stall`, `empirical-studio-kiln`,
    `predictive-hall-solar`, `definitional-vintage-rail`, `value-theatre-season`,
    `framing-piano-lessons`, `one-sided-games-night` and `no-conflict-quiz-team`. The ninth,
    `transcript-father-care`, stands in the second real case's place (Decided, above): a
    message thread between two siblings, a Value crux, the only synthetic case in transcript
    form. Each input has no frontmatter: a one-line request in the words of the skill's
    description, then the two parties labelled A and B, given as roles, never names (the
    one-sided case is one voice giving both). No topic is one of `crux-types.md`'s examples,
    so the cases test the skill rather than its own examples;
  - `real-lincoln-douglas`: two unbroken passages from the first Lincoln–Douglas debate
    (Ottawa, 1858) on the "house divided", Douglas first, chosen with the owner and copied
    verbatim from the National Park Service's transcript, its typos kept, since quotes are
    checked against it; `source:` names the page and `license: public-domain`.
- **gold.md** holds `crux` (one sentence), `type` (one of the five, or `none`), `crux_for` (`A`,
  `B`, `both` or `none`) and `approved_by: FairCat-GD`. The owner approved or wrote every one
  before it was written, and all ten were committed together, before any result; the debate
  excerpt's was changed with its input in that session's review, still before any result.
  Below the frontmatter, which is all `checks.py` reads, a short note for the owner's review:
  the common ground that pins the crux, what else counts as a match, and, for the one-sided
  and no-conflict cases, the rules above.
- **The latest cycle** (Session 7c, crux-finder 0.4.0, commit `b187824`): `run-1.md` and
  `run-2.md` for each of the ten cases, `claude-ai.md` for `empirical-studio-kiln`,
  `one-sided-games-night` and `no-conflict-quiz-team`, and each case's `review.md`. It met every
  bar and the smoke test on the skill as it stands; its summary table is in Session 7c's
  done-note and in crux-finder's README. The cycles of Sessions 7 (0.1.0), 7a (0.2.0) and 7b
  (0.3.0) are in git and their done-notes.
- **`run-N.md`** is written by `run.py`: frontmatter of `case`, `run`, `model`, `claude` (the
  CLI's version), `skill_version` (the plugin's `plugin.json`), `commit` (HEAD, which holds the
  plugin as it ran), `date` (UTC), `skill_calls` (the Skill tool's calls, or `none`), `denials`
  (permission denials) and `cost_usd`; then a blank line and the reply as returned, with a last
  newline added where it has none.
- **`claude-ai.md`** is a claude.ai reply as its Copy button gives it, under a header of `case`,
  `target`, `model`, `skill_version`, `commit` (the commit holding the zipped skill) and `date`,
  written by the session; the header is optional and is left out of the checks. An output's
  leading block is its header only when it closes and holds `key: value` lines alone, so a
  reply that opens with a `---` rule is checked whole.
- **`review.md`** is `# Review: <id>`, then a `## run-N` or `## claude-ai` section per output,
  each of `- field: value` lines, one per field, values in lower case. A line of any other shape
  is a problem, so a note stays on one line.

## verify

**Decided.** `uv run scripts/verify.py` runs named stages, each failing on its own and runnable
alone by name, then a summary; `--message <draft>` gives `hygiene` the drafted commit message.
One command serves every commit, docs only or not.
- **`skills`:** the Agent Skills validator on every skill folder; `SKILL.md` under 500 lines,
  and under each skill's own lower limit where it has one (crux-finder and provenance-tracer:
  300); every file under `references/` linked from `SKILL.md`; `metadata.version` equal to the
  plugin's version; crux-finder and provenance-tracer have no `scripts/` folder. The per-skill limits are one table in the stage.
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
    own row in `LIMITS` where that row's `lines` is lower; a higher row never lifts the
    specification's. Lines are counted at newlines, as hygiene counts them;
  - that a skill whose row says `scripts=False` ships instructions and references only: no
    `scripts/` folder, and no file but `SKILL.md` and Markdown under `references/`;
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
on `PATH`, and a missing one fails its stage with `verify: cannot run <tool>: <error>`. Every
stage runs even after one fails. Then the summary prints PASS or FAIL and the time for each
stage, followed by `verify: PASS` or `verify: FAIL (<stages>)`, and the exit code is 1 on any
failure.
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
- **`LIMITS` is one table, a row per skill,** each row a `Limits` of `lines` and `scripts`,
  whose defaults are what the specification allows. A skill's own limits then read in one
  place, as the per-skill limits are one table in the Decided part. Its two rows, crux-finder's
  and provenance-tracer's, are each `Limits(lines=300, scripts=False)`.
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
frontmatter, and F3–F21 of round 1's audit, `REVIEW-2026-11-17.md`, fixed. The audit's
`SKILL.md` line numbers predate F2, which added two lines, so a line it cites as `:N` was `:N+2`
before 1.1.0.
Each missing capability has a stated fallback:
- no question tool: the choice steps asked in chat as numbered options, with "Other" last;
- no WeasyPrint or Pango: `references/output-formats.md`'s *Building the PDF* order (already
  importable; then a virtual environment in a temporary folder, never the user's project; then
  Pango looked for where it is installed but not found, and only then asked for), then chat
  with the reason;
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
  Python 3.9. The reference has the agent try that before asking to install Pango.
- **The skeleton imports the italic styles the design uses** (Playfair Display italic 400,
  Inter italic 400 and 600), so its italics are true italics rather than synthesized obliques.

Its README is its user guide: what it does, what it needs on each target, and its install.

## crux-finder

**Decided.** PDD B, carried into this round by `SPEC.md` with the amendments of its §3: two
positions in, the smallest claim the rest hinges on out, as a report of at most 400 words; no
verdict, no statement about either party; instructions and references only. `SKILL.md` under
300 lines, with `references/procedure.md`, `crux-types.md` and `output-template.md`. Settled
2026-11-20, where PDD B's template left it open:
- **Party labels:** the report says A and B throughout; where the input names its parties (a
  transcript's speakers, or positions given under names), the two steelman lines add the name or
  role in brackets, `**A (<name or role>), strongest form:**`.
- **No conflict:** the report keeps every heading; *The crux* reads `**No crux**` with one
  neutral sentence on why both positions can hold at once, and an empty section says `None.`
- **The report's length:** a check before sending (the steelmen's balance, the 400 words, the
  quotations), each field of a crux one sentence, and nothing after Confidence.

Settled 2026-11-22, with the owner, for 0.2.0, from what Session 7's cycle showed (each change
general, none fitted to one case):
- **A budget per section,** aiming at about 350 words (replaced in 0.3.0 by caps in words,
  below): each steelman at most 50 words (still 2
  to 4 sentences), Common ground at most three lines, each crux field one sentence of about 25
  words, a secondary crux only where each party states a side, *Not actually in dispute* at most
  two lines and never a repeat of Common ground, Confidence one sentence.
- **A conflict pair is two claims the parties argue:** each stated by its party, or an inferred
  premise the other party's words contradict directly; a point one party never touches is in no
  pair. A pair of stated claims ranks above one holding an inferred premise, after double cruxes
  and before depth.
- **Empirical or Predictive by what would settle it,** in the order of questions and in the
  tie-break alike: a dispute over a record both read differently is Empirical even when each
  draws a forecast from it or words it in the future tense. The Framing-or-Value tie-break stays
  as 0.1.0 had it: no general wording separated the piano case's gold from the theatre case's
  (*Known debt*).
- **Quotation marks** only around text copied verbatim from the input, capitals included: never
  the skill's own words, a question it poses or a label.
- **The no-conflict exit** reports a Framing crux only where taking up the other's question would
  change a conclusion, else **No crux**; and the report is the whole answer, with nothing after
  Confidence.

Settled 2026-11-22, with the owner, for 0.3.0, from what Session 7a's cycle showed (its one
missed bar, length, on the long excerpt alone):
- **A cap in words for each section, adding up to under 400** with the headings and labels:
  each steelman 45; Common ground 40; The crux 130, its sentence at most 25 and each field at
  most 22; Secondary cruxes 50 in all; Not actually in dispute 30; Confidence 25. A report inside
  every cap is inside 400 however long the input (386 words with every section at its cap, by
  `checks.py`'s count; 390 with a three-word name in each steelman's brackets, the most the
  label allows; 368 with the note on the agent as a party, whose report has no secondary
  cruxes), so length no longer rests on the model counting its whole report.
- **A steelman keeps to the reasons the conclusion most rests on,** not every reason the input
  gives; a list of further reasons is the first thing cut. Added after the first spot check of
  the caps broke symmetry (below).

Settled 2026-11-22, with the owner, for 0.4.0, from what Session 7b's cycle showed (type and
quotes missed):
- **A claim a party says outright would change their conclusion ranks first among double
  cruxes,** before stated pairs and depth, since the input then names its own crux; a deeper
  claim under it can be a secondary crux, and the type tie-breaks that send a forecast or a
  weighting down to the record or fact under it yield to it. PDD B's "deepest double crux"
  still orders the rest (`SPEC.md` decision 21, amended).
- **A quotation is checked letter for letter, its first letter included:** it keeps the input's
  capital or lower case wherever it falls, and the line is reworded around it. The harness's
  quoted-span rule stays as it is.

**Built.** Version 1.0.0 (2026-11-22), in `plugins/crux-finder/`: 0.4.0 with its version fields
alone changed, released once 0.4.0 met every pass bar and the claude.ai smoke test. `SKILL.md`
(166 lines) holds PDD B's frontmatter, its description word for word, plus `metadata.version`;
the Inputs table, steps 1–9 in brief, the report's rules and the check before sending, and the
seven guardrails.
`references/procedure.md` defines each step in full; `crux-types.md` gives the five types, the
order to test them in, tie-breaks, and two fictional examples each, with roles for parties;
`output-template.md` gives PDD B's template verbatim, the section caps, and every variant
(labels, `None.`, the one-sided form, **No crux**, you as a party, the claim map on request, a
gate's question).
Decisions made here, each with its why:
- **A is the party named first** (in a transcript, the first to speak) unless the user says
  otherwise, so labelling is never a guess.
- **A Framing crux is labelled by the crux test run on the question itself** (would A's
  conclusion change if A took up B's question?), so it fits the template's labels.
- **The references are read when needed:** the template before any report, the types at step 7,
  the procedure where the brief rules leave a case open, as PDD B has the procedure "loaded on
  demand".

Its runs on one fictional input (Session 4): three headless and one installed run in Claude
Code, each seen to trigger the skill by its description, and one on claude.ai, seen only by its
output; every run gave the template's shape. None met the 400 words (486 to 564); the primary
crux's label differed between runs (double crux, or a crux for A).

**The first eval cycle** (Session 7, 0.1.0, `claude` 2.1.329, $3.40 for 20 runs): crux 17/20,
stability 9/10, symmetry 18/18, no statement about people, the one-sided gate 2/2 and the
no-conflict case 2/2, all met; type 13/20 (each miss repeated in both runs of a case: Framing
read as Value, Predictive as Empirical, Empirical as Predictive), quotes 16/20 (the skill's own
words and labels in quotation marks) and length 2/18 (416 to 591 words, about 470 on average)
missed. 0.2.0 is the change for those three. Two spot-check runs of 0.2.0 on a fictional input
outside the set gave 296 and 315 words, with every quotation verbatim.

**The second eval cycle** (Session 7a, 0.2.0, `claude` 2.1.329, $3.56 for 20 runs): crux 20/20,
type 18/20 (the two piano runs read as Value, the *Known debt*), stability 10/10, quotes 20/20,
symmetry 18/18, no statement about people, the gate 2/2 and the no-conflict case 2/2, all met;
length 16/18 missed: the sixteen other reports ran 283 to 393 words, and both reports on the
debate excerpt ran over, at 488 and 463, a full secondary crux of 92 to 95 words and a crux
section of 151 to 162. 0.3.0 is the change for it. Its spot check, on a fictional two-speaker
debate of 1,208 words outside the set: with the caps alone, 336 and 318 words, but one run's
steelmen at 43 and 54, outside the 25%; with the steelman rule added, 326 and 300 words,
steelmen 48/48 and 43/43, the same crux in both, every quotation verbatim.

**The third eval cycle** (Session 7b, 0.3.0, `claude` 2.1.329 for fifteen runs and 2.1.330 for
the last five, $3.81 for 20 runs): length 18/18 (191 to 348 words; the debate excerpt at 336 and
348), symmetry 18/18, crux 18/20, stability 10/10, no statement about people, the gate 2/2 and
the no-conflict case 2/2, all met; type 16/20 and quotes 19/20 missed. Both
`predictive-hall-solar` runs took the hall's share of its own output, a premise under the
ten-year payback both parties argue and B names as what would change their vote, as the
primary crux, typed Empirical, by step 6's depth rule (crux and type missed); both piano runs
read as Value again (*Known debt*). One solar run quoted the input with a capital the input does
not have, at the start of a line. Most crux fields ran a few words over their cap of 22 while
every report kept inside 400. 0.4.0 is the change for both misses. Its spot check, on a
fictional input outside the set with the same shape (a stated condition with a deeper premise
under it): 277 and 323 words, steelmen 43/40 and 40/48, the stated condition as the primary
crux in both, typed Predictive, the deeper claim a secondary crux in one; neither quoted the
input, so the quotation rule was left to the fourth cycle.

**The fourth eval cycle** (Session 7c, 0.4.0, `claude` 2.1.330, $3.73 for 20 runs): every bar
met on the skill as it stands. Crux 20/20, type 18/20 (the two piano runs read as Value, the
*Known debt*), stability 9/10 (the debate excerpt's runs took the two cruxes gold allows, one
each), quotes 20/20, symmetry 18/18, length 18/18 (194 to 358 words), no statement about people,
the gate 2/2 and the no-conflict case 2/2. Both `predictive-hall-solar` runs took the ten-year
payback B names as the crux, typed Predictive, the self-use share a secondary crux; the orchard,
kiln and excerpt cases kept the cruxes they matched before. Only one run quoted the input, so the
quotation rule's first letter had little to catch. The owner's review notes, below any bar:
what would move it left out a record gold names (the pitch fee invoices, the supplier's
readings) or gave a calculation; common-ground lines that widened what a party said.

**The claude.ai smoke test** (Session 7c, 0.4.0 from `b187824`, Fable 5.2 at High effort, run by
the session in the owner's Chrome): `empirical-studio-kiln` gave gold's Empirical crux in 280
words, with a meter on the kiln's circuit as what would move it; `one-sided-games-night` asked
for the co-host's own words and wrote no report; `no-conflict-quiz-team` reported **No crux** in
186 words. All three matched gold on crux and type and passed every check: 3/3.

## provenance-tracer

**Decided** (the round 2 intake, 2026-11-25, from the owner's spec, `provenance-tracer-spec.md`
v2). A claim the user types is traced through its retellings to the earliest instance found,
and the report shows how it changed on the way; a reverse mode starts from one named source and
reports what it found, its status, and what it supports. It reports where a claim came from,
never whether it is true.
- **Targets:** Claude Code and claude.ai with web search on; Codex and other agents documented
  only. Needs web search and page fetch; no file or notes access, no scripts (invariant 4).
- **The skill folder:** `SKILL.md` under 300 lines (the trigger, mode selection, asking the
  user, both procedures in brief, the labels' axes, the guardrails) and four references:
  `labels.md` (both label axes, modifiers and tiers), `mutation-types.md` (the kinds of drift),
  `search-playbook.md` (query patterns, stop rules, status checks), `output-template.md`.
- **Frontmatter:** `name`, the spec's `description` word for word (184 characters, under
  claude.ai's 200), `license: MIT` and `metadata.version`, which overrides the spec's three
  fields because invariant 3 needs it and claude.ai accepted it in round 1.
- **The contract the spec fixes,** carried as written: the mode table; at most one question
  message per trace, none in a non-interactive run, whose assumptions head the report; the
  forward trace's eleven steps, with 6 queries to start and at most 14 more, at most 6 hops per
  branch and 25 fetches per trace, every page used opened, never a snippet; tiers (Primary only
  if opened); the two label axes, Roots and Grounding, one value each, and the five modifiers;
  the report's template and its two footer lines; a saved report only when asked, in Claude
  Code, never naming hearsay; the guardrails (no verdict in the report's own voice, opened
  sources only, honest nulls, the claim text in searches said once, no private person's name in
  a search, at most one quote per source, under 15 words).
- **Asking the user** (settled at the start of Session P1, with the owner, 2026-11-25): the skill
  assumes a person is there to answer, unless the prompt or the system prompt says no reply is
  possible, or it runs as a subagent or a scheduled task; then it never asks, proceeds web-only,
  takes each question's default and lists its assumptions at the top. Every eval case but the one
  that tests a question says so in its system prompt.
- **Roots** (settled at the start of Session P1, with the owner, 2026-11-25, where the spec's step
  7 and its *Cold trails* disagree): a root cites nothing earlier and originates the claim, its
  own data, study, document, speech or text, or, where no chain reaches such an origin, it is the
  earliest instance found. Any other node that states the claim and cites nothing is a cold trail:
  counted as a retelling, never a root. Independent means two or more such origins. Read so, the
  spec's six labelled cases give the labels it expects.
- **Two rules added mid-Session P1, with the owner** (2026-11-25), after the first three
  hand-tries: the report is the whole answer, with nothing after its last line (both reports had
  added a closing summary); and all 6 opening queries are run before judging whether to add more
  (the forward run had stopped at 3).
- **Versions:** 0.1.0 when built (P1), a minor bump per change an eval cycle calls for, 1.0.0
  once a cycle meets every bar on the skill as it stands, tagged
  `provenance-tracer--v1.0.0`.
- **Out of scope:** the notes-vault mode, truth verdicts, more than one claim per run, claims
  about private individuals (`docs/BACKLOG.md`, the last by design).

**Built.** Version 0.1.0 (2026-11-25), in `plugins/provenance-tracer/`, in crux-finder's shape.

- **`SKILL.md`** (185 lines). Its frontmatter: `name`, the spec's description word for word in
  double quotes (it holds a colon), `license: MIT` and `metadata.version`. Its body:
  - what to read and when;
  - the need for web tools;
  - the spec's mode table, its private-person row checked first;
  - asking the user;
  - the forward trace's eleven steps and the reverse trace's five, with the spec's numbers;
  - the labels table;
  - the report's rules;
  - the guardrails;
  - a check before sending.
- **`references/labels.md`:** tiers, the roots rule, counting retellings, both axes, the
  modifiers and the label line.
- **`references/mutation-types.md`:** the six drifts and "other", and where a drift first
  appears.
- **`references/search-playbook.md`:**
  - what never goes into a query;
  - the six query families;
  - the budgets and stop rules;
  - opening, following and dating a page (the Wayback Machine's capture index for an archive
    date);
  - the status checks;
  - reverse mode.
- **`references/output-template.md`:**
  - the spec's forward template verbatim;
  - how to fill it in;
  - the search note, the assumptions block, the question, the refusal;
  - the reverse report;
  - saving a report.

Every example in the references is invented and marked so. None is a spec eval case.

Decisions made here, each with its why:
- **No web search or no page fetch: say so and stop.** A trace from memory would break *opened
  sources only*, and search without fetch leaves nothing that can be opened. Each may come as a
  tool, a deferred tool or a subagent, and the skill looks for every form first, since a headless
  Claude Code run has WebFetch only through a subagent (*Context*).
- **A private-person claim gets no tool call of any kind,** and the refusal does not repeat the
  name: the spec's "do not search", read so that nothing about the person leaves the
  conversation. The refusal carries no search note, since nothing is searched.
- **Several claims share one question message** with the personal-chain questions for the claim
  picked. That keeps the spec's "at most one question message per trace" when both apply.
- **The report's grammar, fixed for P2's graders and P3's checks:**
  - modifiers after the Grounding value, each after ` · `, in the spec's order;
  - every node linked to the URL exactly as passed to the fetch tool, and a `(not opened)` node
    linked only if its fetch was tried;
  - the tier on every node, not only the root as the template shows;
  - titles in italics, so quotation marks hold only quotes;
  - the assumptions block above the heading, so the template's lines keep their order;
  - untraced claims listed in the assumptions without quotation marks, so quotation marks hold
    only the heading's claim, the *Your version* line and sources' quotes;
  - every status finding under *Status of the root*, the root's Primary first and any other
    Primary's finding naming its source, since the template has no other place for status.

  The template's two `**Roots:**` lines stay as the spec wrote them: a label regex anchors on
  `**Roots:** <value> · **Grounding:**`.
- **The reverse report is as the spec lists it:** the source and status first, then *What it
  found*, *Popular versions* and the beliefs table if asked, with no labels, Confidence or footer.
  The footer speaks of tiers and labels, which a reverse report does not carry.
- **Confidence is in the trace, not the claim:** High, Medium or Low by what was opened and how
  each date is known.

**Tried by hand** (Session P1, `claude` 2.1.330, `claude-opus-5-5`, as *Context* describes,
each run with a system-prompt line saying no reply is possible). Three inputs: a quote
misattributed to a famous scientist, a 1999 psychology paper named for a reverse trace, and a
claim about an invented coworker.
- **The first three runs:**
  - the forward and reverse runs triggered the skill and gave reports in the template's shapes,
    each followed by a closing summary;
  - the forward run made 3 searches;
  - the private-person prompt, worded "Where did this come from?", did not trigger the skill. The
    model declined to search on its own.
- **After the two rules above and a reworded prompt,** all three triggered the skill:
  - **forward:** 6 searches and 7 fetches; Echo · No primary found · Mutated · Misattributed; the
    count and earliest-instance lines; ended at the footer;
  - **reverse:** 3 searches and 13 fetches; the status checks; ended at *Popular versions*;
  - **private person:** no tool call but the Skill tool; the refusal, without the name.
- **In every run:** nothing asked, the assumptions block where a report was written, and no web
  call denied.
- **Spend:** six runs, $2.67.

**Not yet:** the cases (P2) and the first cycle (P3).

## The eval harness

**Decided.** PDD B, *Evals*, under `evals/crux-finder/`: ten cases, two runs each through
`run.py` in a fresh session, the owner's review of every run, `checks.py`'s deterministic
checks and summary against the pass bars, and a claude.ai smoke test on three cases. It spends
real model runs, so it runs only where a session's block names it, never in `verify`, one run
at a time. Settled at the start of Session 5, with the owner (2026-11-20), where PDD B left a
gap:
- **Isolation:** `run.py` as PDD B has it, each run isolated from the user's settings, plugins,
  synced skills, MCP servers and memory, and from every file outside its own folder and the
  plugin; measured first.
- **The model:** `claude-opus-5-5`, named in `run.py` and written at the head of every result,
  with the CLI's version, the skill's version and the commit, so cycles compare.
- **A quoted span** is text between double quotation marks, straight or curly, and any
  blockquote but the crux sentence's, which is the skill's own words; the template's fixed
  labels are never quoted. It must be in the input after line breaks are joined and curly and
  straight quotation marks and apostrophes are folded; with an ellipsis, piece by piece, in
  order. Single quotes mark no span, since they are apostrophes too.
- **A question is not a report:** an output without `## Crux report` is held to neither
  symmetry nor length, and is judged by `gate_fired`.
- **A word** is a whitespace-separated token with a letter or digit, so markup alone (`##`,
  `**`, `-`, `·`, `>`) is none. Length counts the output after its header, a claim map left out,
  at most 400. Symmetry: each steelman within 25% of the other, the longer at most 1.25 times
  the shorter.
- **Gold order** fails a gold.md that is not committed, whose first commit does not precede the
  first commit of its results, or that changed after results existed, committed or not.
- **Settled at the start of Session 8, with the owner** (2026-11-22): a run is on the skill as it
  stands when the skill folder is as it was in the run's commit, a change to `SKILL.md`'s
  `metadata.version` line alone aside, since that is the one change decision 23 allows a
  release.

**Amended at the round 2 intake, with the owner** (2026-11-25): one engine for every skill,
`claude plugin eval` (*Context*), from Session E2 on for crux-finder; what is above about
quotes, words, symmetry, length, a question and the skill as it stands still holds for
crux-finder, read from the new results, and gold order too, reckoned from the results present
now (*The data layer*).
- **One runner, shared,** under `evals/`, standard library only (invariant 5, whose test lets
  a file under `evals/` import shared code there). Given a skill, it refuses while the plugin
  has uncommitted changes, records the commit, the skill's and the CLI's versions, runs the
  engine on that skill's cases, and writes the results (*The data layer*). It skips a run whose
  file exists. It runs cases in place, or, if Session E1 measures that the engine cannot, from
  a temporary copy of the plugin and the cases; either way no case is under `plugins/`.
- **Its fixed choices:** the model `claude-opus-5-5`; no baseline arm (`--ablation none`);
  never published (`--no-publish`); `--trust-plugin` for this repository's own plugin only;
  results written outside the plugin (`--output-dir`); the web tools a skill's cases need,
  granted with `--allow-tools`; up to four runs at once (`--concurrency 4`), and still one
  cycle at a time. A run's failure is read from the results, not the exit code.
- **Isolation,** as before: none of the owner's settings, plugins, synced skills, MCP servers
  or memory, and no read of `gold.md` or the graders. Session E1 measures it, and whether it
  can be checked on every run; losing that per-run check is the owner's call.
- **Graders and checks:** the engine's graders judge what they can express; each skill's
  `checks.py` judges the rest from the committed results and git: gold's fields and order,
  the graders unchanged since each run's commit, the owner's corrections, and the pass bars.
  crux-finder: two runs per case, round 1's bars, stability judged by the owner.
  provenance-tracer: three runs per case, a case passing at 2 of 3, the spec's hard checks on
  every run, and every chain URL among the run's fetches.
- **A claude.ai reply** is judged by the owner in `review.md`, for both skills.

**Built.** `evals/crux-finder/run.py` and `evals/crux-finder/checks.py`, both standard library
only, on Python 3.10.

`run.py --runs N [--case <id> …]`:
- **Before anything is spent,** it reads every chosen case's input.md (missing, an unclosed
  frontmatter or an empty body exits 2, as do an unknown case and no cases), and it refuses,
  exiting 2, while `plugins/crux-finder/` has uncommitted changes, so every result's `commit`
  holds the skill it ran, or while its `plugin.json` gives no version.
- **Each run** gets a new temporary folder holding an empty `work/`, its working directory, and
  a copy of `plugins/crux-finder`. The command is `claude -p --model claude-opus-5-5
  --output-format stream-json --verbose --plugin-dir <copy> --add-dir <copy>` with the isolation
  flags *Context* names, `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`, a 900-second timeout and
  `--max-budget-usd 2`. The prompt goes in on stdin. The folder is removed when the run ends.
- **The start event is checked** before anything is written: the model is `MODEL`; the only
  plugin not built in is the copy; `crux-finder:crux-finder` is listed and no other namespaced
  skill or other `crux-finder`; no MCP server; the `default` permission mode; no memory paths.
  A breach, a non-zero exit, a timeout, an error result or an empty reply writes nothing for
  that run and stops with exit 1; earlier files stay.
- **An existing `run-N.md` is skipped,** never overwritten, so a stopped cycle resumes by
  running the same command and a new cycle starts by removing the old files.
- **It never names gold.md:** it lists the case folders and opens only each `input.md`.

`checks.py` reads every case and every output and prints one line per problem, then the summary
table, then `checks: <n> case(s), <n> problem(s); <state>`. It exits 0 with no problem and either
no results yet or every bar met; otherwise 1.
- **Per case:** gold.md's four fields, `approved_by` non-empty; the gold order (invariant 7).
- **Per output:** an output that cannot be read is a problem, not a crash; the quotes; for a
  report, symmetry, from the text after
  `**A[ (…)], strongest form:**` and `**B[ (…)], strongest form:**` up to the next label, blank
  line or heading; and length. A `run-N.md` must carry the `commit` `run.py` writes.
- **`review.md`:** a section for every output and none for a missing one; the three yes-or-no
  fields and the note; `same_crux_as_run_1` from run 2 on and not on run 1; `gate_fired` for a
  question; `gate_fired` and `no_conflict_reported` on every output of a case or none. Every case
  has run-1 to the highest run present, and every results folder names a case.
- **The summary table:** PDD B's ten bars over the `run-N` outputs, each with its bar, its count
  and whether it is met. The ratios are exact fractions of the runs or cases present: crux at
  least 4/5, type 9/10, stability 4/5 of the cases with two or more runs, which over ten cases
  and two runs are PDD B's 16/20, 18/20 and 8/10. Gate and no-conflict count the runs whose
  review records the field, at least one. The claude.ai smoke test is a row of its own: three
  outputs, each matching gold on crux and type and passing every check.

Decisions made here, each with its why:
- **The isolation guard reads the start event of every run,** not only the session's
  measurement, because a CLI release or a new upload can change what loads with no change here.
- **The plugin is copied out of the repository,** so the run's only open folder outside its own
  holds the plugin and nothing that leads to gold.md; `--add-dir` opens it because the skill
  reads its references with the file tools.
- **The prompt goes on stdin,** because a body that starts with `-` would be read as a flag.
- **A sentence's last mark just inside the closing quotation mark is not part of the quote,**
  since English punctuation puts it there whether or not the input had it.
- **An unpaired quotation mark is a problem,** since the span it opens cannot be checked.
- **An eleventh row, beyond PDD B's ten bars,** "Runs on the skill as it stands": every run's
  `commit` has the skill folder as it is now, `SKILL.md`'s `metadata.version` line aside. That is
  decision 22's condition with decision 23's one allowed change, so a release that moves only the
  version keeps the row met. The rest of the folder is compared by `git diff --quiet`, and
  `SKILL.md` as the commit holds it (`git show`) against the working tree's, each with
  `without_version` leaving out the one `version:` line inside the frontmatter's `metadata:`
  block, in any form the `skills` stage reads (quoted or not, any indent, any value). A
  version-shaped line anywhere else, in `SKILL.md`'s body or in a reference, still counts as a
  change. It needs no git option newer than `show` and `diff`. The row came with the plan the
  owner approved.

## Testing strategy — five layers, and what each cannot see

**Decided.** **`verify`** runs named stages, each failing on its own and runnable alone by name,
then a summary: `skills`, `plugins`, `format`, `lint`, `tests`, then `hygiene`. It is green
before every commit. The harness is each skill's eval set. The commands are in `CLAUDE.md`.
From round 2 (amended at its intake, 2026-11-25), every skill's eval set runs on `claude plugin
eval` through one shared runner, judged by its graders and the skill's `checks.py`, with the
owner reading every failed verdict and one run per case (*The eval harness*).

**Built.**

| Layer | Runs | Covers | Cannot see |
|---|---|---|---|
| Validators | `verify` (`skills`, `plugins`) | The specification's frontmatter and naming; the manifests; the limits and names in *verify* | Whether a skill behaves well |
| Unit | `verify` (`tests`) | The scripts: hygiene, verify's own checks, the eval tooling | The skills themselves |
| Hygiene | `verify`, with the drafted commit message; in full when the term list or the stage changes | Private terms in files, paths and messages; attribution in messages; secrets by their exact shapes; `.env` files; conflict markers | Images and binaries; a term joined inside one lowercase run; attribution in files; a home-directory path; a secret of any other shape; a file's earlier versions in history |
| Evals | Where a block names them | A skill's behaviour on fixed cases, judged by the owner and `checks.py` | Cases outside the set; targets not run |
| By hand | Recorded in done-notes | Installs, claude.ai (run by the owner, or at their word by the session in their browser), a whole interview | Anything not written down; what nobody checked goes to the backlog |

Built: Validators (the `skills` and `plugins` stages), Unit (`tests/test_verify.py`,
`tests/test_hygiene.py`, `tests/test_check_skills.py`, `tests/test_check_plugins.py`,
`tests/test_crux_finder_run.py`, `tests/test_crux_finder_checks.py`, `tests/test_evals_stdlib.py`)
and Hygiene. Evals: the tooling (`run.py`, `checks.py`) and crux-finder's ten cases; the first
cycle ran in Session 7, on crux-finder 0.1.0, the second in Session 7a, on 0.2.0, the third
in Session 7b, on 0.3.0, and the fourth in Session 7c, on 0.4.0, which met every bar and was
followed by the claude.ai smoke test on three cases. provenance-tracer has no eval set yet (P2,
P3); its first version was tried by hand, headless and installed (Session P1).

## Packaging

**Decided.**
- **Claude Code:** `/plugin marketplace add FairCat-GD/claude-skills`, then
  `/plugin install <skill>@faircat-skills`.
- **Codex:** the skill folder copied to `~/.agents/skills/` or `.agents/skills/`.
- **claude.ai:** a zip with the skill folder at its root, uploaded as a custom skill.
- **Other agents:** the skill folder copied into the agent's skills directory.
- **Releases:** a skill's version moves in its own session; crux-finder 1.0.0 is tagged
  `crux-finder--v1.0.0`, and provenance-tracer's 1.0.0 will be tagged
  `provenance-tracer--v1.0.0` (settled at the round 2 intake, 2026-11-25). Pushes and tags are
  each the owner's yes.

**Built.** The marketplace, checked locally: `claude plugin marketplace add ./` and
`claude plugin install travel-itinerary-builder@faircat-skills` installed it, and
`claude plugin details` listed its one skill at 1.0.1. Adding it from GitHub is not yet checked
by hand (`docs/BACKLOG.md`). Each plugin's README gives each target's install, the claude.ai zip
and the Plugins page it is uploaded on included. crux-finder 1.0.0 is tagged
`crux-finder--v1.0.0`, made with `claude plugin tag`, which checks that `plugin.json` and the
marketplace entry agree; travel-itinerary-builder 1.1.0 is untagged. crux-finder was
installed the same way in Session 4 (`claude plugin details crux-finder` listed its one skill at
0.1.0, about 94 tokens always on), and its zip, `zip -r crux-finder.zip crux-finder` from
`plugins/crux-finder/skills/`, was uploaded to claude.ai as a custom skill and run once. In
Session 7c the 0.4.0 zip (`zip -r -X crux-finder.zip crux-finder -x '*.DS_Store'`, made
outside the repository: `SKILL.md` and the three references) was uploaded on claude.ai's Plugins
page, run on the smoke test's three cases, and deleted (*Context*).

provenance-tracer, the third plugin, in Session P1:
- **Installed from this folder:**
  - `claude plugin marketplace add ./`;
  - `claude plugin install provenance-tracer@faircat-skills`;
  - `claude plugin details provenance-tracer` listed its one skill at 0.1.0, about 78 tokens
    always on and 3.6k on invoke;
  - `claude plugin marketplace remove faircat-skills` removed both; neither list shows them.
- **Its claude.ai zip** (`zip -r -X provenance-tracer.zip provenance-tracer -x '*.DS_Store'`, made
  outside the repository) holds the folder at its root: `SKILL.md` and the four references. It
  is not uploaded until P5.
- **Untagged.** It joins the install from GitHub once pushed.

## Deliberate decisions

**Decided.**
- **No type-check stage.** The only code is a few small scripts; ruff and the tests cover them.
- **One command for every commit,** with no docs-only command: `verify` takes seconds here.
- **A version per skill, set only in `plugin.json` and repeated in `SKILL.md`;** the marketplace
  entries carry none, so a skill that did not change is not offered as an update.
- **The evals sit outside `verify`.** They cost real model runs and the owner's review, so a
  block names when they run.

## Known debt, deliberately deferred

- **crux-finder's Framing-or-Value line.** `framing-piano-lessons` (gold Framing) and
  `value-theatre-season` (gold Value) have the same shape: each side states what the decision
  is for and grants the other's facts. A rule that sent the first to Framing would send the
  second there too, so the tie-break stays as 0.1.0 had it and both piano runs may miss on type,
  which the type bar's 18/20 allows. They did in Sessions 7a, 7b and 7c, so every other case
  must match on type for the bar to hold; in 7c every other case did. The owner's call whether
  either gold should change (`docs/BACKLOG.md`).

## Baseline

Measured 2026-11-25 with Python 3.10.20, uv 0.12.3, ruff 0.17.5, pytest 9.2.0, `claude` 2.1.330
and the validator at `83021e2`. The heading carries no version because the repository has none
of its own: each skill has its own version.

| Check | Expected |
|---|---|
| `uv run scripts/verify.py` | green: 6 stages (`skills`, `plugins`, `format`, `lint`, `tests`, `hygiene`), about 25 s with uv's cache warm, most of it the eval tooling's git fixtures |
| Unit tests (`tests`) | 210 passed, 0 skipped: 75 in `test_crux_finder_checks.py`, 45 in `test_hygiene.py`, 36 in `test_check_skills.py`, 22 in `test_crux_finder_run.py`, 20 in `test_check_plugins.py`, 10 in `test_verify.py`, 2 in `test_evals_stdlib.py` |
| `uv run scripts/verify.py hygiene --all` | green; 0 hits in pushed history |
| Python files (`ruff format --check .`) | 13 |
| Skills and plugins | 3 skill folders, 3 plugins, 3 marketplace entries |
| `uv run evals/crux-finder/checks.py` | Session 7c's cycle and smoke test on 0.4.0, read on 1.0.0, whose skill differs only in its version line: `checks: 10 case(s), 0 problem(s); every pass bar met`, exit 0, the "as it stands" row 20 / 20 and the smoke test's row 3 / 3 |

A documentation or refactoring change should not move any of these. If one moves, that is the
finding.

## Decision log

- 2026-11-18, Session 2: *The contract between the layers* gains the plugins' display fields:
  `author`, the owner's name, and `homepage`, the plugin's README on GitHub; no keywords. The
  owner settled it at the start of Session 2.
- 2026-11-19, Session 3: *travel-itinerary-builder* gains its minimum environment (the
  `compatibility` wording), the A4 page in one column, and the WeasyPrint-else-chat order. The
  owner settled them with the session, the page from rendered samples.
- 2026-11-20, Session 4: *crux-finder* gains the party labels, the **No crux** report's shape
  and the check before sending, with one sentence per crux field and nothing after Confidence.
  The owner settled the first two at the start of Session 4, where PDD B's template left them
  open, and the third after the first headless runs ran over the 400 words.
- 2026-11-20, Session 5: *The data layer* gains `review.md`'s three fields and the prompt
  without its frontmatter, and *The eval harness* the isolation, the model, the quoted span, a
  question judged by `gate_fired`, the word rules and the strict gold order. The owner settled
  them at the start of Session 5, each as the session recommended (decision 21).
- 2026-11-20, Session 6: *The data layer* gains how the one-sided and no-conflict cases are
  judged against their gold. The owner settled both at the start of Session 6, as the session
  recommended (decision 21), with the debate excerpt. Mid-session, with no dispute of their own
  to write up, the owner asked for a serious fictional one, so the real set holds one case.
- 2026-11-22, Session 7: *The data layer* gains that each cycle replaces the results, and how
  Session 7's review was made, a draft confirmed row by row by the owner; *crux-finder*
  gains 0.2.0's section budget, conflict pairs and their ranking, the Empirical-or-Predictive rule, quotation
  marks and the no-conflict exit. The owner settled the first at the start of Session 7, the
  second mid-session, and the rest from the cycle's results, each as the session proposed.
- 2026-11-22, Session 7a: *The data layer* gains how Session 7a's review was made, a draft by a
  fresh reader that saw no earlier verdict, confirmed row by row by the owner; *crux-finder*
  gains 0.3.0's caps in words that add up to under 400, and the steelman kept to its main
  reasons. The owner settled the first at the start of Session 7a, and the rest from the
  cycle's results and the spot check, each as the session proposed.
- 2026-11-22, Session 7b: *The data layer* gains how Session 7b's review was made, as 7a's;
  *crux-finder* gains 0.4.0's ranking of a party's stated condition first among double cruxes,
  and quotations checked letter for letter, the first letter included. The owner settled the
  first at the start of Session 7b, and the rest from the cycle's results, each as the session
  recommended. In the session's review the owner had the type tie-breaks yield to the new
  ranking and recorded the departure from PDD B's step 6 beside `SPEC.md` decision 21.
- 2026-11-22, Session 7c: *The data layer* gains how Session 7c's review was made, as 7b's;
  *Context* gains that the session may run claude.ai in the owner's Chrome at the owner's word. The owner settled the first at the start of Session 7c, and the
  second mid-session, asking the session to run the smoke test itself.
- 2026-11-22, Session 8: *The eval harness* gains that a change to `SKILL.md`'s
  `metadata.version` line alone leaves a run on the skill as it stands. The owner settled it at
  the start of Session 8, as the session recommended.
- 2026-11-25, round 2 intake: a new section, *provenance-tracer*, from the owner's spec, with
  `metadata.version` kept against the spec's three fields; invariant 4 extended to it;
  *Context* gains `claude plugin eval` and the live web; *Layout and boundaries*, *The data
  layer*, *The eval harness* and *Testing strategy* move every skill's evals onto that engine
  through one shared runner at the root, instead of crux-finder's own `run.py` and the owner's
  review of every run, with `gold.md` kept, each run's reply and tool calls committed, the
  owner reading failed verdicts and one run per case, and four runs at once instead of one;
  invariant 6 covers the graders; *Packaging* names provenance-tracer's tag. The owner settled
  each at the intake: the engine for crux-finder too, asking for one layout for every skill;
  what a cycle commits, after the plan review showed the engine's JSON holds no whole reply.
- 2026-11-25, Session P1: *provenance-tracer* gains how the skill tells that no reply is
  possible, and the roots rule, where the spec's step 7 and its *Cold trails* disagree. The owner
  settled both at the start of Session P1, as the session recommended, the second after the plan's
  adversarial review found the disagreement.
- 2026-11-25, Session P1: *verify*'s Decided limits name provenance-tracer beside crux-finder
  (under 300 lines, no `scripts/` folder), as decision PT 10 settled at the round 2 intake. Amended
  at plan time, with the owner, since the block named only *verify*'s Built part.
- 2026-11-25, Session P1: *provenance-tracer* gains two rules: nothing follows the report, and all
  6 opening queries run before judging whether to add more. The owner settled both mid-session,
  after the first three hand-tries ended in a closing summary and stopped at 3 searches.
