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
and `tests/`. The evals: the shared runner, `evals/run.py`, with the result formats it writes,
`evals/shared.py` (Session E1); crux-finder's ten cases in `evals/crux-finder/cases/`, each a
`prompt.md`, its graders and `gold.md`, and its `checks.py` (Session E2); and
`evals/crux-finder/results/`, which holds the three claude.ai replies of round 1's smoke test and
no cycle yet: crux-finder's first cycle on the runner is Session E3's.

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
  scored below its threshold. Read from its docs at intake and measured in Session E1 (Built,
  below); a measured behaviour unlike the docs is a stop. Part of the unpinned CLI, so each
  session that runs it records the CLI's version.
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
    reads outside the run's folders as denied; this folder is the run's own output. Under the
    engine, below, a run's own files are in its own temporary home.
- **`claude plugin eval`, measured in Session E1** (2026-11-25, `claude` 2.1.330,
  `claude-opus-5-5`): a fictional plugin and cases in a temporary folder laid out as this
  repository, with a space in its path: 21 runs for $1.35, 16 measuring and 5 through the
  finished runner. Every call was launched from inside a Claude Code desktop session with each
  `CLAUDE*` and `ANTHROPIC_*` variable removed; the CLI signed in with its own claude.ai login.
  - **Isolation:** each run is a `claude -p` child in a temporary home. Its start event listed the
    plugin under test and Claude Code's built-ins only, un-namespaced built-in skills, no MCP
    server, the `dontAsk` permission mode, a memory folder inside its own temporary home (empty),
    and no added folder. None of the owner's user plugins, synced claude.ai skills or memory
    loaded. The same held from a copy of the plugin and in place.
  - **Reads:** the workspace starts empty. The plugin's folder can be read, a skill's references
    included, but only when the case lists `Read` in `allowed_tools`, which the docs call
    pre-approved; `Skill` fires unlisted. The eval folder, `gold.md` and the graders included,
    was denied by absolute and by relative path ("a directory that is denied by your permission
    settings"). Every other path outside the workspace was denied under `dontAsk`: the root
    `CLAUDE.md`, an earlier result, a file elsewhere.
  - **What a run leaves:** `aggregate-result.json` in `--output-dir`, the same document `--json`
    writes, holds no reply. Per run, it holds:
    - its score, turns, cost, judge cost, duration, start time and `error`;
    - `tracePath` and `skippedPaidGraders`;
    - each grader's verdict, explanation and `scored`, and an `llm` grader's three votes and the
      text it was shown.

    The reply, every tool call and the start event are in the run's trace,
    `<kept folder>/out/trace.jsonl`, in `claude -p`'s stream-json shape. A subagent's calls carry
    the `Agent` call's id as `parent_tool_use_id`; a denial is a `permission_denied` event, or an
    error result for the eval folder. The trace is deleted unless `--keep-temp`. A kept folder is
    `/private/tmp/e-*` whatever `TMPDIR` says, read-only, with a part sealed at mode 000.
  - **Cases:** an unknown key in `prompt.md` fails that case alone, named on stderr, and the call
    exits 1. Two keys the docs do not list, `artifact_publish` and `growthbook_overrides`, are
    accepted. A `gold.md` beside `prompt.md` is ignored. `--case` takes no brace glob, and a
    repeated one keeps the last.
  - **In place:** cases under `evals/<skill>/cases/` load with the repository root as target,
    `--eval-dir evals/<skill>/cases` and `plugins: ["../../../../plugins/<skill>"]`. A `plugins:`
    path must stay inside the folder the engine runs against, a "containment root" the docs do
    not describe; any narrower target refuses it.
  - **The judge:** `claude-haiku-5-5` by default, three votes per `llm` grader. It was shown the
    whole of a 1,756-word reply. Its explanation is the votes alone.
  - **The web tools:** `--allow-tools WebSearch WebFetch` grants both. Each is deferred, loaded
    with ToolSearch, and called in the main session, unlike P1's `claude -p` runs, where every
    fetch ran in a `web-fetch` subagent. `tool_used` counts a subagent's call. Listing ToolSearch
    in `allowed_tools` prints "not granted", though the tool is always there.
  - **Failures:**
    - a run that hits `max_turns` or its timeout is still graded, with `error` set; a timed-out
      run has no reply and reports $0, though it spent tokens;
    - a low score has `error` null;
    - under `--threshold 0`, none of these makes the exit code non-zero;
    - an API error was not provoked; the docs give it no grader results and `error` set.
  - **Time:** a short run took 1 to 18 s; four at once, 18 s for the slowest. `runsPerCase` reads
    3 under `--runs 1`, though one run ran.
  - **Side effects:** nothing was written in the mock repository. The owner's `~/.claude.json`
    project table and `~/.claude/` gained no entry, `--trust-plugin` included. `--debug-file` is
    a top-level option, refused after `plugin eval`.
- **`claude plugin eval` on crux-finder's cases, measured in Session E2** (2026-11-25, `claude`
  2.1.330), each call through the runner's own copy and flags, at $0.22 in all:
  - **Loading:** the engine reads every case's `prompt.md` before it filters by `--case`, since
    `--case` matches the `name` frontmatter key; a call naming no case loads all of them and runs
    none, for $0. All ten loaded; a copy with an unknown key in one `prompt.md` named that case
    on stderr. A grader is not read at load: an unknown grader type passed it.
  - **One run** of `empirical-studio-kiln` (`--trial`): the skill fired and read the template and
    the types with `Read`, in 5 turns and 32 s, for $0.21; the `claude-sonnet-5-5` judge cost
    $0.013 for two `llm` graders of three votes each, and the `regex` grader's explanation is the
    pattern it matched.

Measured at intake, 2026-11-17, and again in Session 2, 2026-11-18: `claude` 2.1.326; uv 0.12.3;
Python 3.10.20 installed through uv. In Session 4, 2026-11-20: `claude` 2.1.328. In Session 5,
2026-11-20, Session 7, 2026-11-21, and Session 7a, 2026-11-22: `claude` 2.1.329. In Session 7b,
2026-11-22: 2.1.329 at the start, and 2.1.330 from the cycle's sixteenth run, the CLI having
updated itself mid-cycle. In Session 7c, 2026-11-22: 2.1.330 throughout. In Session 8,
2026-11-22: 2.1.330. In Session P1, 2026-11-25: 2.1.330. In Session E1, 2026-11-25: 2.1.330. In
Session E2, 2026-11-25: 2.1.330.

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
  `test_check_plugins.py`, `test_crux_finder_checks.py`, `test_evals_run.py`,
  `test_evals_shared.py`, `test_evals_stdlib.py` and `fixtures/terms.txt`, a term list of three
  fictional words. The check tests build fictional plugin trees in a temporary folder. The tests
  import the scripts through pytest's `pythonpath`, which holds `scripts/` and `evals/`, and the
  runner and crux-finder's `checks.py` by their paths under names of their own, since a folder
  named `crux-finder` is no package.
- `evals/` holds the shared runner, `run.py`, and the code every skill's eval tooling shares,
  `shared.py`, both standard library only (*The eval harness*). The runner reaches a skill only
  through the CLI: it copies the plugin folder, without reading the skill's files, to where the
  engine can load it.
- `evals/crux-finder/` holds `checks.py`, standard library and `shared` only, and `cases/`, the
  ten cases (*The data layer*), and `results/`, the three claude.ai replies kept from round 1
  (Session E2 retired round 1's runs and the old runner).

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
   read with `ast`, names a module in `sys.stdlib_module_names` or `shared`, the shared code at
   `evals/shared.py`; and no Python file under `evals/` is named like a standard-library module,
   which its script's folder, first on the path, would put in that module's place.
6. **Neither the runner nor the session under test reads `gold.md`.** *Why:* a run that sees the
   answer proves nothing. **Amended at the round 2 intake, with the owner** (2026-11-25), for the
   shared runner: the session under test reads neither `gold.md` nor a case's graders, and the
   runner never opens `gold.md` and copies the graders unopened. Round 1's runner, which Session
   E2 retired, was held to it by its own test and each run's start event. *Enforced by*
   `tests/test_evals_run.py`, which runs `evals/run.py` against a stub engine with an audit hook
   on every file it opens and gold.md made unreadable, and checks that the engine is given each
   case's `prompt.md` and graders byte for byte and no `gold.md`, which the runner leaves out of
   its copy by name; and by each run's isolation, measured in Session E1 (*Context*: the eval
   folder, graders included, is denied to every run) and checked on every run from the start
   event in its trace, before its files are written (*The eval harness*).
7. **Each `gold.md` is committed before any file now under its `results/<id>/`, and names who
   approved it.** *Why:* gold written after the results could be fitted to them. "Now" since the
   round 2 intake (*The data layer*): a retired cycle stays in history, and its files never
   count. *Enforced by* `evals/crux-finder/checks.py`, from git: gold.md committed; in the parent
   of the commit that added each file now under `results/<id>/` (its latest adding, for a file
   removed and added again) and unchanged since; in the commit each output names and unchanged
   since; with no uncommitted change while results exist; and with a non-empty `approved_by`.
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
- **Settled at the start of Session E2, with the owner** (2026-11-25), as the intake left it
  (EE 6): the owner's correction of a verdict is a line in the case's `review.md`, under the
  run's `## run-N` section, `- <grader>: pass` or `- <grader>: fail`, with a one-line note.
  Every verdict that failed gets one, `fail` confirming it and `pass` overruling it, and a pass
  the owner overrules gets one too. `checks.py` counts the owner's line over the engine's
  verdict, and a failed verdict with no line is a problem, so a failure nobody read cannot pass.
  Stability stays the owner's record, `same_crux_as_run_1` from run 2 on.
- **Machine identifiers, never renamed:** the marketplace name `faircat-skills`; the plugin
  and skill names `travel-itinerary-builder`, `crux-finder` and, from Session P1,
  `provenance-tracer`; the case ids once results exist.

**Built** (the formats, the ten cases and the results present).
- **A case's frontmatter** is read as one `key: value` per line, a quoted value unquoted, with
  no YAML library: gold.md's fields each on one line.
- **crux-finder's ten cases** (Session 6), one folder each under `evals/crux-finder/cases/`,
  named for the row it fills and its topic (`<type>-<topic>`, `one-sided-…`, `no-conflict-…`,
  `real-…`, and `transcript-…` for the one case named for its form); the id never reaches a
  run, which sees only the prompt:
  - nine synthetic, fictional, drafted by the session and approved by the owner. Eight are one
    per row of PDD B's synthetic set: `empirical-orchard-stall`, `empirical-studio-kiln`,
    `predictive-hall-solar`, `definitional-vintage-rail`, `value-theatre-season`,
    `framing-piano-lessons`, `one-sided-games-night` and `no-conflict-quiz-team`. The ninth,
    `transcript-father-care`, stands in the second real case's place (Decided, above): a
    message thread between two siblings, a Value crux, the only synthetic case in transcript
    form. Each prompt is a one-line request in the words of the skill's description, then the
    two parties labelled A and B, given as roles, never names (the one-sided case is one voice
    giving both). No topic is one of `crux-types.md`'s examples, so the cases test the skill
    rather than its own examples;
  - `real-lincoln-douglas`: two unbroken passages from the first Lincoln–Douglas debate
    (Ottawa, 1858) on the "house divided", Douglas first, chosen with the owner and copied
    verbatim from the National Park Service's transcript, its typos kept, since quotes are
    checked against it; its gold's `source:` names the page, and `license: public-domain`.
- **`prompt.md`** (Session E2, moved from round 1's `input.md` with `git mv`, its body
  unchanged): frontmatter of `allowed_tools: [Skill, Read]` (*Context*: a skill reads its
  references only when the case lists `Read`), `max_turns: 20` and `timeout_seconds: 900`, then
  the prompt. 20 turns is four times what a run takes (the skill, three references, the reply),
  and 900 s is round 1's cap per run, since the engine writes a run that hits either as the
  skill's result. No `name:`, which defaults to the folder the runner matches on, and no line
  saying no reply is possible.
- **The graders** (Session E2), `graders/<name>.md`, drawn from each gold and its note and
  approved by the owner, after a review of them by a second model at the owner's request, before
  they were committed. `checks.py` maps each name to a bar:
  - `crux` (every case): an `llm` grader that quotes gold's crux and the note's "Any wording …
    is a match" sentence word for word, and its "counts no" sentence where it has one. PASS if
    the primary crux, the blockquote right under `### The crux`'s label, is a match; FAIL on no
    report, a **No crux** report, or any other primary crux, even where a secondary crux
    matches. In the no-conflict case, a `regex` for `**No crux**` under `### The crux`.
  - `type` (every case): a `regex` on the primary crux's label, `### The crux\s+\*\*(?:Double
    crux|Crux for [AB]) · <Type>\*\*`, the template's own shape. An `llm` grader in the three
    cases whose note ties type to more than the label: `one-sided-games-night` (asking for the
    co-host's own words with no report passes), `real-lincoln-douglas` and
    `transcript-father-care` (the crux the note counts no fails, whatever its label). The
    no-conflict case's is the `**No crux**` regex.
  - `no-statement-about-people` (every case): an `llm` grader with the skill's "Claims, not
    people" rule, the case's parties named, and who is not a party (the daughter, the father,
    the founders). A line restating a party's stated position is a claim; a favourable
    statement about a party counts the same as an unfavourable one.
  - `gate` (`one-sided-games-night`): `llm`, from gold's note: no report and a request for the
    co-host's own words or a transcript, or a report labelling B reconstructed by A.
  - `no-conflict` (`no-conflict-quiz-team`): a `regex` for `**No crux**` or a Framing label.

  Every `llm` grader states the reply's shape: a report has a `## Crux report` heading and a
  `### The crux` section, and in the one-sided case a reply with neither writes no report. The
  regexes were checked against round 1's outputs before those were retired: all 22 verdicts
  with an owner's field agreed (*The eval harness*).
- **gold.md** holds `crux` (one sentence), `type` (one of the five, or `none`), `crux_for` (`A`,
  `B`, `both` or `none`) and `approved_by: FairCat-GD`; `real-lincoln-douglas`'s also
  `source:` and `license:`, moved from its input in Session E2. The owner approved or wrote every
  one before it was written, and all ten were committed together, before any result; the debate
  excerpt's was changed with its input in that session's review, still before any result, and
  gained its two lines in Session E2, after round 1's results were retired. Below the
  frontmatter, which is all `checks.py` reads, a short note for the owner's review: the common
  ground that pins the crux, what else counts as a match, and, for the one-sided and
  no-conflict cases, the rules above. The graders quote it.
- **The results present:** no cycle yet. Session E2 retired round 1's twenty `run-N.md` and the
  `review.md` of the seven cases with no claude.ai reply; the cycles of Sessions 7 (0.1.0), 7a
  (0.2.0), 7b (0.3.0) and 7c (0.4.0, which met every bar) are in git and their done-notes, the
  last in crux-finder's README too. Kept: `claude-ai.md` for `empirical-studio-kiln`,
  `one-sided-games-night` and `no-conflict-quiz-team` (Session 7c, from `b187824`), each case's
  `review.md` cut to `# Review: <id>` and its `## claude-ai` section.
- **`claude-ai.md`** is a claude.ai reply as its Copy button gives it, under a header of `case`,
  `target`, `model`, `skill_version`, `commit` (the commit holding the zipped skill) and `date`,
  written by the session; the header is optional and is left out of the checks. An output's
  leading block is its header only when it closes and holds `key: value` lines alone, so a
  reply that opens with a `---` rule is checked whole.
- **The shared runner's formats** (Session E1), the ones crux-finder's results take from Session
  E3 and provenance-tracer's from P3, written by `evals/run.py` and read with `evals/shared.py`:
  - **`run-N.md`:** frontmatter of `case`, `run`, `model`, `claude`, `skill_version`, `commit`,
    `date`, `cost_usd`, `duration_s`, `turns` and `error` (`none`, or the engine's error for a run
    it still graded). Then `## Tool calls`, one `- <Tool>: <argument>` line per call in the
    trace's order, or `none`. The argument is the query, URL, skill, path or subagent type, and
    any other tool's input as one-line JSON. A call inside a subagent adds `(in <type>)`, and a
    refused or failed one adds `(denied)` or `(error)`. Then `## Reply` and the final reply as
    the run gave it, with a last newline added where it has none. The reader takes the first
    `## Reply` line as the runner's, so a reply that holds one reads back whole.
  - **`verdicts-N.md`:** frontmatter of `case`, `run`, `score`, `judge_model` and
    `judge_cost_usd`. Then a `## <grader>` section per grader, each of `- type:`, `- verdict:`
    (`pass` or `fail`), `- scored:` (`yes` or `no`), `- weight:`, `- votes:` (an `llm` judge's
    three, as `pass pass fail`, else `none`) and `- explanation:`. Its name does not start with
    `run-`, so no pattern for runs takes it in.
  - In both, every machine path is a placeholder (*The eval harness*), and a line break inside a
    value is written as `\n`.
- **`review.md`** is `# Review: <id>`, then a `## run-N` or `## claude-ai` section per output,
  each of `- field: value` lines, one per field, values in lower case. A line of any other shape
  is a problem, so a note stays on one line.
  - **A run's section** (Session E2) holds `same_crux_as_run_1: yes|no` from run 2 on, never on
    run 1; a `<grader>: pass|fail` line for each of its failed verdicts and any it overrules,
    naming only a grader in its `verdicts-N.md`; and a `note`. It is required for every run from
    run 2 on and for any run with a failed verdict, so the stability record and the owner's
    reading of each failure are in it.
  - **A claude.ai section** keeps round 1's fields: `crux_match`, `type_match` and
    `people_statement` (yes or no), a `note`, and `gate_fired` for a question, with
    `no_conflict_reported` where it applies.

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

**Amended in Session E1, with the owner** (2026-11-25), the engine measured (*Context*):
- **Cases run from a temporary copy,** not in place: the plugin, and each chosen case under the
  copy's `evals/` without its `gold.md`. In place loaded too, but it rests on a rule the docs do
  not give, and one call cannot select several cases; the copy is the docs' own layout and never
  hands `gold.md` to the engine. A `prompt.md` carries no `plugins:` line.
- **The judge is pinned** to `claude-haiku-5-5`, the measured default, written into every result;
  Session E2 asks again once crux-finder's graders exist.
- **The runner refuses while the cases have uncommitted changes too,** since a run's `commit` must
  hold the graders it ran with; `--trial` writes to a folder outside the repository instead, for a
  gate's trial run, and is not refused on the cases.
- **A run the engine graded is written,** whatever its score, even one that hit its turn cap or
  timed out, with the engine's error in its header: that is the skill's result. A run with no
  grader results, an aborted one, one whose judges were skipped or one that fails the isolation
  check is not written, and a later call runs it again.
- **`--max-cost-usd` is required** and covers the whole command, every engine call in it.
- **The reply as the run gave it, machine paths aside:** a path is replaced by a placeholder, since
  `CLAUDE.md` keeps every home-directory path out of the repository.
- **Isolation is checked on every run,** from the start event in its trace, as `run.py` checks
  crux-finder's today.

**Settled at the start of Session E2, with the owner** (2026-11-25), the three Asks of its block:
- **The judge** is `claude-sonnet-5-5`, over the engine's default `claude-haiku-5-5`, for its
  reading of paraphrase in the crux and people graders; pinned in the runner and written into
  every `verdicts-N.md`.
- **The graders from gold:** `crux`, `no-statement-about-people` and the one-sided `gate` are
  `llm` graders whose criteria quote gold's crux and its note's match rules word for word.
  `type` is a `regex` on the primary crux's label, which the template fixes, as are the
  no-conflict case's three graders; the three cases whose note ties type to more than the label
  get an `llm` type grader.
- **The corrections:** a line per failed verdict in `review.md` (*The data layer*).
- **Four rules gold left open,** settled mid-session after the owner had a second model review
  the drafted graders: a favourable statement about a party is a statement about people; a
  **No crux** report fails crux and type wherever gold gives a crux; in the debate excerpt, a
  crux that sets slavery among the local varieties against division matches even where it also
  mentions the Union's endurance; in the one-sided case, a reply with no `## Crux report`
  heading and no `### The crux` section writes no report.

**Built.** The shared runner, `evals/run.py`, with `evals/shared.py` (below), and crux-finder's
`evals/crux-finder/checks.py`, all standard library only, on Python 3.10. Round 1's
`evals/crux-finder/run.py` and its tests were retired in Session E2, with the results they
wrote; git keeps them.

`checks.py` (rewritten in Session E2 on `shared`) reads every case and every output and prints
one line per problem; then, with runs present, the summary table and the count of verdicts the
owner overruled; then the smoke test's row; then `checks: <n> case(s), <n> problem(s); <state>`.
It exits 0 with no problem and either no results yet, or no cycle yet and the smoke test met, or
every bar met; otherwise 1.
- **Per case:** `prompt.md` with a body after its frontmatter, the text quotes are checked
  against; `graders/` holding `crux`, `type` and `no-statement-about-people`, and otherwise only
  `gate` or `no-conflict`, since each maps to a bar; gold.md's four fields, `approved_by`
  non-empty.
- **Gold order** (invariant 7), from the results present now: gold in HEAD; for each file now
  under `results/<id>/` that git has, the commit that last added it, whose parent holds gold,
  unchanged since; gold in each output's `commit`, unchanged since; no uncommitted change while
  results exist.
- **The case as it ran:** for each `run-N.md`'s `commit`, the case's `prompt.md` and graders in
  that commit, the same grader files as now, and neither changed since. A `claude-ai.md`, older
  than every grader, is not held to it.
- **Per run:** `run-N.md` read with `shared.read_run`, a file that cannot be read a problem, not
  a crash; its header's `commit`, `case` and `run` agreeing with its place; `verdicts-N.md`
  beside it, and none without a run, read with `shared.read_verdicts`, one verdict for each
  grader of the case and none for another. The reply alone is checked, never the calls: the
  quotes against the prompt and, for a report, symmetry, from the text after `**A[ (…)],
  strongest form:**` and `**B[ (…)], strongest form:**` up to the next label, blank line or
  heading, and length. A run with an `error` header counts as the engine graded it.
- **`review.md`:** the sections and lines *The data layer* gives; a section for a missing output,
  a field given twice or out of range, or a line of another shape is a problem. Every case has
  run-1 to the highest run present, every results folder names a case, and every entry in one is
  read, so a result that is not a file is a problem rather than unseen.
- **The summary table:** PDD B's ten bars and an eleventh, over each run's effective verdict, the
  owner's line where there is one, else the engine's. The ratios are exact fractions of the runs
  or cases present: crux at least 4/5 and type 9/10 of the runs, stability 4/5 of the cases with
  two or more runs, from `same_crux_as_run_1`, which over ten cases and two runs are PDD B's
  16/20, 18/20 and 8/10. Quotes, no statement about people and runs on the skill as it stands are
  over all runs, symmetry and length over the reports, the gate and no-conflict over the runs
  whose case has that grader, at least one, and "Gold order + approved_by + graders as run" over
  the cases. The claude.ai smoke test is a row of its own: three replies, each matching gold on
  crux and type in its review and passing every check.

Decisions made here, each with its why:
- **A run's prompt is held as its graders are,** unchanged since its commit, since quotes are
  checked against the prompt as it is now.
- **Each commit's view of the case folders is read once** (`git ls-tree -r` and `git diff
  --name-only` over `cases/`), and every adding commit in one `git log` over `results/`, since a
  cycle's runs share one commit: a check costs a handful of git calls, not several per file.
- **The verdicts are read by grader name,** so a grader's file name is its bar, and a grader no
  bar reads is a problem rather than a verdict counted nowhere.
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

**The shared runner** (Session E1), `uv run evals/run.py <skill> --runs N --max-cost-usd USD
[--case <id> …] [--trial <folder>]`. It ran on a fictional plugin in a temporary folder in Session
E1, and on one of crux-finder's cases as a trial in Session E2; crux-finder's first cycle on it is
Session E3's.
- **Before anything is spent,** it exits 2 on any of these, with no engine call:
  - a skill not in `SKILLS`, a table of each skill's web tools (crux-finder none,
    provenance-tracer `WebSearch` and `WebFetch`);
  - no plugin folder, no cases, an unknown `--case`, or a case folder with no `prompt.md`, whose
    existence alone it checks, never opening a case;
  - uncommitted changes under `plugins/<skill>/`, or under `evals/<skill>/cases/` except in a
    trial;
  - a trial folder inside the repository;
  - a `plugin.json` with no version.
- **Missing runs:** for each case, the numbers 1 to N with no `run-N.md`. Cases missing the same
  count share one engine call; with nothing missing it spends nothing.
- **Each call** runs in a new temporary folder holding the plugin's copy, with each chosen case
  under the copy's `evals/` and `gold.md` left out by name. The command is `claude plugin eval
  <copy> --model claude-opus-5-5 --judge-model claude-sonnet-5-5 --ablation none --no-publish
  --trust-plugin --keep-temp --threshold 0 --concurrency 4 --runs <missing> --max-cost-usd <left>
  --output-dir <temporary> [--allow-tools <the skill's tools>]`. stdin is closed, and the
  environment has no `CLAUDE*` or `ANTHROPIC_*` variable.
- **Reading** `aggregate-result.json`:
  - anything but `schemaVersion` 1 writes nothing;
  - a case it did not send is named and nothing is written for it, while the cases that came
    back under their own names are written: a `prompt.md` whose `name:` differs from its folder
    costs only its own case;
  - a case that did not come back did not load;
  - each run is written or not by the rule above, and a value the runner cannot read (a cost
    that is not a number, a line break in a grader's name) skips that run, never the command.

  The isolation check reads the run's start event:
  - the model;
  - the copy as the only plugin not built in, and `<skill>:<skill>` with no other namespaced
    skill and no bare one;
  - no MCP server, the `dontAsk` mode, no memory folder outside the run's own, and no added
    folder.
- **Writing:** `verdicts-N.md`, then `run-N.md`, each through a hidden `.partial` file and a
  rename, with N the case's next missing number. An orphan verdicts file is replaced.
- **The exit code** is 0 when every missing run was written, else 1, with earlier files kept. The
  temporary folder and every kept run folder are removed.

Decisions made here, each with its why:
- **`--threshold 0`,** so a low score never sets the exit code and exit 1 means a run or a case
  failed; the results are read either way, since a run the engine still graded can carry an
  error under exit 0.
- **`--keep-temp`,** since each run's trace is the only place its reply and tool calls are. The
  runner unlocks and removes each kept folder, found from its `tracePath` and named as the
  engine names it (`e-*`), so no other folder is ever taken for one, once the call's results
  are read. A call that writes no result leaves its kept folders behind, since nothing
  names them (*Known debt*).
- **The environment without `CLAUDE*` or `ANTHROPIC_*`,** since a launching Claude Code session's
  variables (its model, its effort, its entry point) would reach the engine, and the CLI signs in
  with its own login without them.
- **A wall-clock cap per call** of 3,600 s per round of four runs, plus 600, the most the engine's
  own caps allow. It catches only an engine that hangs, which is then terminated and its partial
  result read.
- **The ceiling is the command's:** each call gets what the calls before it left, by their
  reported cost, rounded down to the cent, and a call is not made with less than a cent. A call
  that leaves no result is taken to have spent its whole ceiling, since what it spent is unknown,
  so no later call runs. A timed-out run reports $0 (*Context*), so the ceiling can under-count
  it.
- **The scrubber** replaces, longest first, in each path's given and resolved forms (macOS
  `/private`), a path only where it ends, so `/a/b` is never taken inside `/a/bc` or `/a/b-old`:
  - the run's workspace → `<workspace>`;
  - the plugin's copy → `<plugin>`;
  - the temporary folder and the run's kept folder → `<temp>`;
  - the repository root → `<repo>`;
  - the home folder → `~`.

  It covers the reply, every call's argument, the run's error and each verdict's explanation; a
  verdict's other fields are the engine's names and numbers. A run whose text still
  holds the home folder (plain, dashed as a project-folder name, percent-encoded or
  JSON-escaped) or a `/var/folders` path is not written. `CLAUDE.md` keeps machine paths out of
  the repository, and the hygiene stage cannot see one.
- **A call is `(denied)`** when a `permission_denied` event or the result's denials name it, or
  its error holds the engine's own words, "denied by your permission settings", which is how a
  read of the eval folder is refused. It is `(error)` when it failed otherwise, a page that says
  it denied access included, so a fetch that failed shows as the run saw it.
- **The judge's evidence is not kept:** for a judge of the reply it is the reply, already in
  `run-N.md`, and for a judge of the trace it is raw trace, which no result holds (EE 4).

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
`tests/test_crux_finder_checks.py`, `tests/test_evals_run.py`, `tests/test_evals_shared.py`,
`tests/test_evals_stdlib.py`) and Hygiene. The shared runner's tests run it against a stub engine
whose result file and traces copy the shapes measured in Session E1; the runner itself ran end to
end on a fictional plugin in that session, and on one crux-finder case as a trial in Session E2.
`checks.py`'s tests build a fictional repository whose results the shared code writes. Evals: the
runner, crux-finder's `checks.py` and its ten cases with their graders (Session E2); round 1's four
cycles ran on the retired runner, in Session 7 on crux-finder 0.1.0, 7a on 0.2.0, 7b on 0.3.0 and
7c on 0.4.0, which met every bar and was followed by the claude.ai smoke test on three cases.
crux-finder's first cycle on the engine is Session E3's. provenance-tracer has no eval set yet
(P2, P3); its first version was tried by hand, headless and installed (Session P1).

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
- **The shared runner can leave kept run folders behind.** When the engine writes no result (it
  crashed, or was killed before it could), nothing names the folders it kept, under
  `/private/tmp/e-*`, and the runner leaves them. They hold a run's temporary home and its
  trace. Sweeping every `e-*` folder at the start would remove another session's, so they are
  removed by hand: `chmod -R u+rwx`, then delete.

## Baseline

Measured 2026-11-25 with Python 3.10.20, uv 0.12.3, ruff 0.17.5, pytest 9.2.0, `claude` 2.1.330
and the validator at `83021e2`. The heading carries no version because the repository has none
of its own: each skill has its own version.

| Check | Expected |
|---|---|
| `uv run scripts/verify.py` | green: 6 stages (`skills`, `plugins`, `format`, `lint`, `tests`, `hygiene`), about 27 s with uv's cache warm, most of it the eval tooling's git fixtures |
| Unit tests (`tests`) | 299 passed, 0 skipped: 115 in `test_crux_finder_checks.py`, 51 in `test_evals_run.py`, 45 in `test_hygiene.py`, 36 in `test_check_skills.py`, 20 in `test_check_plugins.py`, 18 in `test_evals_shared.py`, 10 in `test_verify.py`, 4 in `test_evals_stdlib.py` |
| `uv run scripts/verify.py hygiene --all` | green; 0 hits in pushed history |
| Python files (`ruff format --check .`) | 15 |
| Skills and plugins | 3 skill folders, 3 plugins, 3 marketplace entries |
| `uv run evals/crux-finder/checks.py` | No cycle yet; round 1's smoke test on 0.4.0, read on 1.0.0: `checks: 10 case(s), 0 problem(s); no cycle yet, so the cycle's bars are not counted; the claude.ai smoke test met`, exit 0, the smoke test's row 3 / 3 |

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
- 2026-11-25, Session E1: *Context* records the engine as measured, and the owner confirmed it and
  *The eval harness*. *The eval harness* gains:
  - cases run from a temporary copy rather than in place;
  - the judge pinned;
  - the refusal on uncommitted cases, and a trial mode;
  - graded runs written whatever their error;
  - a required ceiling for the whole command;
  - machine paths replaced in the reply;
  - isolation checked on every run.

  The owner settled the copy at a stop, once both were measured, and the judge after the plan's
  adversarial review; the rest came with the plan the owner approved.
- 2026-11-25, Session E2: *The eval harness* gains the judge, `claude-sonnet-5-5` in place of the
  engine's default; the graders drawn from gold, `llm` for crux, people and the gate and a `regex`
  on the label for type, except where gold ties type to more than the label; and four rules gold
  left open (a favourable statement about a party counts, **No crux** fails where gold gives a
  crux, the debate excerpt's match outranks its exclusion, and headings decide what a report
  is). *The data layer* gains how the owner's correction of a verdict is recorded and counted: a
  line in `review.md` for every failed verdict. Invariant 7 reads "now under". The owner settled
  the first three at the start of Session E2, as the block asked, choosing the stronger judge
  over the session's recommendation, and the four rules mid-session, after a second model
  reviewed the drafted graders at the owner's request.
