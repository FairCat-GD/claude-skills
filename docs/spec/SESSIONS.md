# The session plan: round 2, provenance-tracer and one eval engine

One block per session, in order, each run by *The session cycle* in
`docs/DEVELOPMENT-WORKFLOW.md`. The requests and their resolved decisions are in
`FEATURE-provenance-tracer.md` (cited as PT 1, PT 2…) and `FEATURE-eval-engine.md` (EE 1, EE 2…)
beside this file, both read-only; do not re-litigate them. A session that finds its block wrong
amends it and records the reason in the block and in `docs/next-session-prompt.md`. P5 closes
the round: it deletes this file and the feature files, and anything left open moves to
`docs/BACKLOG.md`.

Versions are per skill: the column names the skill a session releases.

| Session | Scope | Decisions | Version |
|---|---|---|---|
| P1 | provenance-tracer, the skill: plugin, skill folder, marketplace entry, limits, READMEs; tried by hand in Claude Code | PT 1–3, 6, 9–12; *provenance-tracer*, *Packaging* | provenance-tracer **0.1.0** |
| E1 | The engine measured; the shared runner built and tested; today's crux-finder tooling untouched | EE 1, 2, 4, 9–12; *Context*, *The eval harness* | — |
| E2 | crux-finder's cases in the new format and its new checks; the old runner, checks and results retired | EE 3, 5–8; *The data layer*, *The eval harness* | — |
| E3 | crux-finder's first cycle on the new engine; its README's test section rewritten | EE 5, 7, 9 | — |
| P2 | provenance-tracer's thirteen cases: prompts, golds and graders | PT 3, 6–8; EE 2, 3 | — |
| P3 | provenance-tracer's `checks.py`, its first cycle and the owner's spot check | PT 5, 8; EE 4–6, 9 | — |
| P4 | The changes P3's cycle calls for, and the next cycle (dropped, with its reason logged, if P3's cycle meets every bar) | PT 2, 5, 8 | provenance-tracer **0.2.0** |
| P4a | The changes P4's cycle calls for, and a cycle only at the owner's word (inserted in Session P4) | PT 2, 5, 8 | provenance-tracer **0.3.0** |
| P5 | 1.0.0, the claude.ai smoke test, the round's `ARCHITECTURE.md` sections read cold, close the round | PT 2, 4; EE 8 | provenance-tracer **1.0.0**, tagged `provenance-tracer--v1.0.0` |

As in round 1, a session is inserted (P4a, E3a…) for each further cycle a changed skill needs,
and the versions after it shift.

**The owner at the keyboard**, by session: three traces of the new skill read, and the install
check (P1); the measurements' spend approved (E1); every crux-finder grader approved before it
is committed (E2); failed verdicts, one run per case and stability read (E3); the two open
cases chosen and every gold approved (P2); the cycle's cost ceiling, failed verdicts and one
run per case (P3, P4); the claude.ai replies judged, the tag and any push (P5).

---

## P1: provenance-tracer, the skill

**Read:** `FEATURE-provenance-tracer.md` PT 1–3, 6, 9–12, and the spec's *Scope*, *Repo
placement*, *SKILL.md frontmatter*, *Mode selection*, *Asking the user*, *Forward trace*,
*Reverse trace*, *Labels*, *Output format*, *Guardrails* and *Distribution*; `ARCHITECTURE.md`
invariants 2–4 and 8, *Context*, *The contract between the layers*, *verify*,
*provenance-tracer*, *Packaging*; crux-finder's plugin as the pattern
(`plugins/crux-finder/`).

- **The skill** (the spec's *Repo placement* to *Guardrails*; PT 1, 6, 10):
  `plugins/provenance-tracer/skills/provenance-tracer/SKILL.md`, with `name`, the spec's
  `description` word for word, `license: MIT` and `metadata.version: "0.1.0"`, under 300 lines:
  the trigger, mode selection, asking the user, both procedures in brief, the labels' axes and
  the guardrails. `references/labels.md`, `mutation-types.md`, `search-playbook.md` and
  `output-template.md` hold the detail, each linked from `SKILL.md`. Instructions and
  references only.
- **The plugin** (PT 11): `plugins/provenance-tracer/.claude-plugin/plugin.json` at `0.1.0`,
  with `name`, `version`, `description` (the first sentence of the skill's), `author`,
  `homepage` and `license`, as crux-finder's; `CHANGELOG.md` with `[0.1.0]`; `README.md`, its
  user guide: what it does and never does, what it needs on each target (web search and page
  fetch; on claude.ai, web search and code execution on), installing on each target. No test
  results yet.
- **The marketplace and the checks** (invariants 2, 4, 8): its entry in
  `.claude-plugin/marketplace.json`; `provenance-tracer` in `PUBLISHED`
  (`scripts/check_plugins.py`); its row in `LIMITS` (`scripts/check_skills.py`),
  `Limits(lines=300, scripts=False)`; their tests, beside crux-finder's
  (`tests/test_check_skills.py`, `tests/test_check_plugins.py`).
- **The root README:** the skill under a new heading, **Research**, marked as in development.
- **Tried by hand,** as round 1's Session 4 tried crux-finder:
  - headless, `claude -p` with `--plugin-dir` and the plugin's absolute path, from an empty
    temporary folder, the web tools allowed, on three inputs: a forward claim the spec's cases
    do not use, a reverse source, and a claim about an invented private person;
  - then `claude plugin marketplace add ./`, `claude plugin install
    provenance-tracer@faircat-skills`, `claude plugin details provenance-tracer`, and
    `claude plugin marketplace remove faircat-skills` at the end.

  Nothing a run writes is committed; the done-note records, per run, whether the skill
  triggered, the web tools' names as the run used them, the number of searches and fetches,
  the labels and footer, and whether it asked a question.
- **Docs.**
  - `CLAUDE.md`: the skill's name beside the others (invariant 4 already names it, from the
    intake).
  - `ARCHITECTURE.md`: *provenance-tracer*'s Built part; *Overview*, *Layout and boundaries*,
    *The contract between the layers* and *Packaging*'s Built parts; invariant 4's *Enforced
    by*; *verify*'s `LIMITS`; the baseline.
  - README: the root README's list; the plugin's own.
- **Confirms:** *provenance-tracer*; *Packaging* (the third plugin, and its zip for claude.ai).
- **Ask at the start of P1:** how the skill tells that no reply is possible (the spec's
  *Asking the user*). *Recommended:* it assumes a person is there, unless the prompt or the
  system prompt says no reply is possible, or it runs as a subagent or a scheduled task; the
  eval cases say so through `append_system_prompt` (PT 6).

**Gates:**
- `uv run scripts/verify.py`, green, with these tests: provenance-tracer's `LIMITS` row is
  `Limits(lines=300, scripts=False)`; `provenance-tracer` is in `PUBLISHED`. Falsified: a
  `SKILL.md` of 300 lines fails, a file under `scripts/` fails, the marketplace entry removed
  fails, a `metadata.version` unlike `plugin.json`'s fails.
- The three headless runs trigger the skill; the private-person run makes no web search.
- `claude plugin details provenance-tracer` lists the skill; `claude plugin marketplace list`
  no longer shows `faircat-skills` at the end.

**Watch for:**
- **The description is the spec's, word for word,** and stays under claude.ai's 200
  characters (184).
- **The examples in the references follow the guardrails:** no verdict in the skill's own
  voice, no private person, at most one short quote per source, and no example that is one of
  the spec's eval cases, so the cases test the skill rather than its examples.
- **The spec's report rules are instructions here, not checks.** The checks are P3's.
- **`SKILL.md` under 300 lines with two procedures** leaves the step detail to the references;
  each reference is named in `SKILL.md` by its path, or the `skills` stage fails.
- **A reply can hold a word on the owner's term list.** Nothing from these runs is committed;
  the done-note records what was seen, not quoted.
- **`claude plugin marketplace add ./` registers this folder in the owner's user settings**
  (`CLAUDE.md`'s *Watch for*): remove it before the session ends.

**Done (2026-11-25, provenance-tracer 0.1.0).**
- **Decided with the user:**
  - **No reply possible** (the block's Ask), as recommended: the skill assumes a person is there
    unless the prompt or the system prompt says no reply is possible, or it runs as a subagent or
    a scheduled task; then it asks nothing, proceeds web-only and lists its assumptions at the top.
  - **At plan time, after an adversarial review of the plan at the owner's request:**
    - **The roots rule**, where the spec's step 7 and its *Cold trails* disagree: a root cites
      nothing earlier and originates the claim, or, where no chain reaches an origin, it is the
      earliest instance found; any other uncited node is a cold trail, counted as a retelling.
      Read so, the spec's six labelled cases give the labels it expects.
    - **The hand-tries:** three inputs (a quote misattributed to a famous scientist, a 1999
      psychology paper for a reverse trace, a claim about an invented coworker), each with a
      system-prompt line saying no reply is possible, and at most $30, $8 and 900 s a run.
  - **Mid-session, after the first three runs:**
    - two general rules: nothing follows the report, and all 6 opening queries are run before
      judging whether to add more;
    - the private-person prompt reworded;
    - all three rerun.
  - **Confirms:** *provenance-tracer* and *Packaging*, each confirmed as built.
- **The skill,** `plugins/provenance-tracer/skills/provenance-tracer/`:
  - **`SKILL.md`** (181 lines): the spec's description word for word (184 characters), `license:
    MIT` and `metadata.version: "0.1.0"`; the mode table, asking the user, both traces in brief,
    the labels, the report's rules, the guardrails and a check before sending.
  - **Four references:** `labels.md` (tiers, roots, both axes, modifiers), `mutation-types.md`
    (the six drifts), `search-playbook.md` (queries, budgets, dating, status checks) and
    `output-template.md` (the spec's forward template verbatim, its grammar, the variants, the
    reverse report).
  - **Examples:** every one invented and marked so; none is a spec eval case.
- **The plugin:**
  - **`plugin.json`** at 0.1.0, its description the first sentence of the skill's.
  - **`CHANGELOG.md`** `[0.1.0]`. Its link reference waits for this commit's sha, added in the
    review commit.
  - **`README.md`,** its user guide: what it does and never does, what it needs on each target,
    and each target's install. No test results yet.
- **The marketplace and the checks:**
  - the third marketplace entry;
  - `provenance-tracer` in `PUBLISHED`;
  - its `LIMITS` row, `Limits(lines=300, scripts=False)`;
  - two tests: the row, and the real `PUBLISHED`, read at import before the autouse fixture
    patches it, equal to the three names.
- **Docs:**
  - the root README's **Research** heading, the skill *(in development)*;
  - `CLAUDE.md`'s published names;
  - `ARCHITECTURE.md`:
    - *Overview*, *Context*, *Layout*, invariants 4 and 8, *The contract* and *verify*;
    - *provenance-tracer* Decided and Built;
    - *Packaging*, *Testing strategy* and the baseline;
    - three *Decision log* lines;
  - `docs/BACKLOG.md`: "either skill" on Codex is now "a skill".
- **Amendments:**
  - ***verify*'s Decided limits line** names provenance-tracer beside crux-finder, as PT 10 settled
    at intake. Amended at plan time, with the owner: the block named only *verify*'s Built part.
  - **The skill changed after its first runs,** with the owner (above).
  - **`docs/BACKLOG.md`'s *Installing from GitHub*** gains provenance-tracer only when a push is
    approved, folded in then, so it never states a push that has not happened.
- **Measured** (`claude` 2.1.330; each run's model claude-opus-5-5):
  - **Setup:** headless, from an empty folder in a temporary directory, with Session 5's
    isolation flags plus `--allowedTools WebSearch WebFetch` and the plugin in place.
  - **Start event:** the plugin and the built-ins only, no MCP server, the `default` mode, no
    memory.
  - **Web tools:** WebSearch is deferred and was loaded with ToolSearch before the first search.
    WebFetch is not a main-session tool: every fetch ran in a built-in `web-fetch` subagent, as a
    WebFetch call among the subagent's events.
  - **Denials:** no web call was denied. One Bash call, a local PDF text extraction, was.
  - **References:** read with Read, or one shell `cat`, inside the `--add-dir` folder.
- **Checked by hand:**
  - **The first three runs:**
    - forward: triggered; Echo · No primary found · Mutated · Misattributed; 3 searches, 8
      fetches; a closing summary after the footer;
    - reverse: triggered; the spec's reverse shape; 4 searches, 16 fetches; a closing summary;
    - private person, worded "Where did this come from? …": the skill did not trigger, and the
      model declined to search on its own.
  - **After the fixes:**

    | Run | Skill | Searches / fetches | Asked | Last line | Cost |
    |---|---|---|---|---|---|
    | Forward | triggered | 6 / 7 | no, assumptions listed | the footer | $0.59 |
    | Reverse | triggered | 3 / 13 | no, assumptions listed | *Popular versions* | $0.71 |
    | Private person | triggered | 0 / 0, no tool call but Skill | no | the refusal, without the name | $0.10 |

    - The forward run's labels: Echo · No primary found · Mutated · Misattributed, 11 retellings,
      the earliest-instance and footer lines present.
    - A few drift cells in the reverse report quoted a word or two from a source that already had
      its one quote: P3's quote check is the judge.
  - **Spend:** six runs, $2.67. Nothing a run wrote is committed.
  - **Installed:**
    - `claude plugin marketplace add ./` and `install provenance-tracer@faircat-skills` (scope
      user);
    - `details`: 0.1.0, Skills (1) `provenance-tracer`, about 78 tokens always on and 3.6k on
      invoke;
    - `marketplace remove faircat-skills` uninstalled it; neither `marketplace list` nor
      `plugin list` shows either.
  - **The claude.ai zip,** made outside the repository: the folder at its root, `SKILL.md` and the
    four references. Not uploaded (P5).
- **Falsified,** each through the whole `verify`, the file copied aside and back:
  - `SKILL.md` padded to 300 lines failed `skills` alone, at `check_skills.py`;
  - `scripts/probe.sh` in the skill folder failed `skills` alone;
  - the marketplace entry removed failed `plugins` alone: not listed, and the published name with
    no entry;
  - `metadata.version` "0.1.1" failed `skills` alone;
  - the row at `lines=301` failed `tests` alone, at its test;
  - the name dropped from `PUBLISHED` failed `tests` alone, at its test.
- **Numbers:**
  - 210 unit tests (+2), 0 skipped;
  - 6 `verify` stages;
  - 13 Python files (±0);
  - 3 skill folders, 3 plugins, 3 marketplace entries (+1 each);
  - crux-finder's `checks.py` unchanged: 10 cases, every bar met.
- **Review (`/code-review high`), 7 findings: 7 fixed and 0 skipped.** The owner chose to fix
  all seven. The skill's fixes join 0.1.0, which is not yet published.
  - **A headless run has WebFetch only through a subagent,** so the rule to stop without page
    fetch could fire wrongly. `SKILL.md` now names the forms fetch may take (a tool, a deferred
    tool, a subagent) and has the skill look for each first.
  - **The search note was the first line of every reply,** the refusal included. It now leads only
    a reply that leads to a search; the refusal says nothing about searches.
  - **Status checks of a non-root Primary had nowhere to go.** The root's Primary is checked first,
    and every finding goes under *Status of the root*, one about another Primary naming it.
  - **Untraced claims were quoted in the assumptions block,** where P3's quote rule would count
    them. They are listed without quotation marks.
  - **`ARCHITECTURE.md`'s *Context* left out a read outside the run's folders:** one run read its
    own tool-results files under `~/.claude/projects/`, not denied. Recorded, and named in the
    handoff for E1's isolation measurement.
  - **The changelog had no link references;** `[0.1.0]` now links the session commit.
  - **claude.ai's page fetch was assumed.** The README says it is not yet checked, and
    `docs/BACKLOG.md` names it for P5's smoke test.
  - **Not rerun:** the three hand-tries ran on the skill before these wording fixes. The first
    two fixes change no behaviour the runs showed (each run found its fetch tool, and the refusal
    carried no note); P3's cycle runs on the skill as it now stands.
  - **Numbers after the review:** 210 unit tests, 0 skipped; `SKILL.md` 185 lines; the other
    counts unchanged.
  - **Pushed** with the owner's yes, with this commit; `docs/BACKLOG.md`'s *Installing from
    GitHub* gained provenance-tracer in it.

---

## E1: The eval engine, measured, and the shared runner

**Read:** `FEATURE-eval-engine.md` in full; `ARCHITECTURE.md` invariants 5 and 6, *Context*,
*Layout and boundaries*, *The eval harness*, *The data layer*, *Testing strategy*; the engine's
docs, `https://code.claude.com/docs/en/plugin-evals.md`, and `claude plugin eval --help`;
`evals/crux-finder/run.py`, `tests/test_crux_finder_run.py`, `tests/test_evals_stdlib.py`.

- **Measure first** (EE 2, 4, 11), each with a fictional throwaway case in a temporary folder,
  never in the repository, and each a stop if it fails:
  - whether cases under `evals/<skill>/cases/` run in place through a case's `plugins:` field,
    or only from a temporary plugin copy;
  - that a run loads none of the owner's plugins, synced skills, MCP servers or memory, cannot
    read its graders, and can read the skill's `references/`; and whether what a run loaded can
    be checked on every run, as `run.py` checks each start event now;
  - where each run's whole reply and tool calls can be read (`--json`, `--keep-temp`, the
    trace), and which machine paths the results hold;
  - that `--allow-tools WebSearch WebFetch` reaches the web, and what the tools are called in
    a run;
  - whether an extra file in a case folder (`gold.md`) or an unknown key breaks loading;
  - how much of a long reply an `llm` judge is shown; the judge model; the cost fields; the
    time one run takes at `--concurrency 4`.
- **The shared runner** (EE 2, 4, 9, 10), under `evals/`, standard library only: given a
  skill, it reads the plugin's version and HEAD and refuses while the plugin has uncommitted
  changes; runs the engine on that skill's cases with the fixed flags; writes
  `results/<id>/run-N.md` and the verdicts beside it, machine paths removed; skips a run whose
  file exists; never opens `gold.md`; and tells a low score from a load failure or an API error
  by the results, not the exit code. Its tests run it against a stub, as
  `tests/test_crux_finder_run.py` runs `run.py`, gold.md made unreadable.
- **Invariant 5's test** (EE 12): `tests/test_evals_stdlib.py` lets a file under `evals/`
  import shared code under `evals/`, and still fails any other import outside the standard
  library.
- **crux-finder's tooling is untouched:** its `run.py`, `checks.py`, cases and results stay as
  they are, and its checks still meet every bar.
- **Docs.**
  - `CLAUDE.md`: the shared runner in *Commands*; *Exclusive resources* names it.
  - `ARCHITECTURE.md`: *Context*'s Built part (the engine as measured, the CLI's version);
    *The eval harness*'s Built part (the runner, and the decisions it made, each with its
    why); invariant 6's *Enforced by* for the new runner; *Testing strategy*; the baseline.
- **Confirms:** *Context* (`claude plugin eval`); *The eval harness* (the runner's fixed
  choices, isolation, and running in place or from a copy).
- **Ask at the start of E1:** the most the measurements may spend. *Recommended:* $5, every
  throwaway case a few lines long, with `--max-cost-usd` set on each call.

**Gates:**
- `uv run scripts/verify.py`, green, with these tests: the runner's flags; its refusal on
  uncommitted plugin changes; that it never opens `gold.md`; that a run's failure is told from
  a low score; that an existing `run-N.md` is skipped; invariant 5's test with a shared import.
  Each falsified.
- `uv run evals/crux-finder/checks.py`: `checks: 10 case(s), 0 problem(s); every pass bar met`,
  exit 0, unchanged.

**Watch for:**
- **The engine publishes its report to claude.ai by default.** Pass `--no-publish` on every
  call, measurements included.
- **A temporary plugin copy is an untrusted folder;** without a terminal the run is refused.
  `--trust-plugin` is for this repository's own plugin only.
- **The engine writes `results/` inside the plugin unless told otherwise.** Use
  `--output-dir`, so nothing lands under `plugins/`, where it would also make the runner refuse.
- **`claude plugin eval init` writes files and runs an interview.** Do not use it here.
- **Exit 1 is expected** whenever a case scores below 1 (`--threshold` defaults to 1.0).
- **Measured facts change with the CLI,** which is not pinned: record its version with every
  measurement.

**Done (2026-11-25, no release).**
- **Decided with the user:**
  - **The spend (the block's Ask):** at most $5 for the measurements; $1.35 was spent, on 21 runs.
  - **At plan time:** after an adversarial review of the plan at the owner's request, the judge
    is pinned to the measured default's full id, written into every result, and E2 asks again.
    The amendments below came with the plan.
  - **At a stop after M2,** both measured: cases run from a temporary copy, not in place.
  - **At a stop after M6:** five behaviours unlike the engine's docs, each recorded in *Context*,
    and the session went on.
  - **Confirms:** *Context* and *The eval harness*, both confirmed.
- **The engine, measured** (`claude` 2.1.330, `claude-opus-5-5`), on a fictional plugin and cases
  in a temporary folder laid out as this repository; *Context* has every finding.
  - **Isolation:** the eval folder (gold, graders) was denied to every run, and every path outside
    the workspace too. The skill's references can be read when a case lists `Read`. None of the
    owner's plugins, synced skills, MCP servers or memory loaded.
  - **What a run leaves:** each run's whole reply, every tool call (a subagent's included) and its
    start event are in its trace, kept only with `--keep-temp`. The result file joins it by
    `tracePath` and holds no reply.
  - **The judge** is `claude-haiku-5-5`, shown the whole of a 1,756-word reply.
  - **The web tools:** WebSearch and WebFetch were called in the main session.
  - **Failures:** a turn-cap or timeout run is still graded.
- **The shared runner,** `evals/run.py`:
  - **the command:** `uv run evals/run.py <skill> --runs N --max-cost-usd USD [--case <id> …]
    [--trial <folder>]`;
  - **before anything is spent,** the refusals, on the plugin and on the cases;
  - **the missing runs,** grouped into one engine call per count;
  - **the copy,** without `gold.md`, with the fixed flags and a clean environment;
  - **the per-run isolation check** from the trace's start event;
  - **the write rule;**
  - **the scrubber;**
  - **`run-N.md` and `verdicts-N.md`;**
  - **the cleanup** of the engine's kept folders.

  *The eval harness* has each decision with its why.
- **The shared code,** `evals/shared.py`: the frontmatter reader, and the writers and readers of
  both result files (*The data layer*).
- **Invariant 5's test:** `shared` may be imported, nothing else of `evals/` may be, and a file
  under `evals/` named like a standard-library module is a finding.
- **Tests:** `tests/test_evals_run.py`, against a stub engine in the measured shapes, and
  `tests/test_evals_shared.py`. `pyproject.toml`'s pytest path and ruff's sources gain `evals`.
- **Docs:**
  - `CLAUDE.md`: the shared runner's command, the exclusive resources, the trap of calling the
    engine directly, and the synced-upload line;
  - `ARCHITECTURE.md`:
    - *Overview*, *Context* and *Layout*;
    - invariants 5 and 6;
    - *The data layer*'s new formats;
    - *The eval harness* (Decided amendments, and the runner as Built);
    - *Testing strategy*, *Known debt* and the baseline;
    - a *Decision log* line;
  - `docs/BACKLOG.md`: an API error's shape, unmeasured.
- **Amendments:**
  - **Five, at plan time, with the owner,** by approving the plan:
    - the judge pinned;
    - the reply as the run gave it, machine paths aside;
    - the runner refuses on uncommitted cases too, and has a trial mode for gate runs;
    - a run the engine graded is written even with a turn-cap or timeout error;
    - `--max-cost-usd` is required and covers the whole command.
  - **E3 and P4 gain an Ask** for the cycle's ceiling, which the runner now requires; P3 had one.
  - **E2's and P2's gate runs** use `--trial`, so nothing a trial writes lands where a cycle would
    skip it.
- **Measured:** as above, with `claude` 2.1.330. Every call was launched from inside a Claude Code
  desktop session, with each `CLAUDE*` and `ANTHROPIC_*` variable removed; `claude auth status`
  showed the CLI's own claude.ai login without them.
- **Checked by hand:** the runner end to end with the real engine, on the fictional plugin.
  - **The run:** 2 cases × 2 runs, four at once in under 6 s, $0.24. Each `run-N.md` holds its
    header, the Skill call, the Read of `<plugin>/skills/…/token.md` and the reply; each
    `verdicts-N.md` holds the judge's three votes.
  - **The rerun:** the same command again made no engine call.
  - **Refusal and trial:** with an uncommitted grader, the runner refused, and a trial ran into
    its own folder with the new grader.
  - **Clean results:** a grep found no home folder, `/var/folders` or temporary path in the
    results.
  - **Nothing left behind:** no kept folder was left, and the owner's config gained no entry.
- **Falsified,** each break through the runner's tests, each failing at its own test, each file
  restored:
  - **the runner's flags:** `--no-publish`, `--keep-temp` or `--threshold 0` dropped; the
    environment not stripped;
  - **gold.md and the refusals:** `gold.md` copied; the refusal on the plugin, on the cases, or on
    a trial inside the repository removed;
  - **writing:** an ungraded run written; existing runs overwritten;
  - **paths and isolation:** the scrubber, its leftover check, or the isolation check removed;
  - **the results:** the shared ceiling, the partial flag, the schema check or the extra-case
    check ignored; kept folders not removed; the hung engine not stopped;
  - **the trace:** denials or subagents not marked; any folder above a `tracePath` taken for a
    kept one;
  - **the formats:** the reply split at the last `## Reply`;
  - **invariant 5:** `shared` refused, any import accepted, shadowing allowed.

  One break, `--no-publish` dropped, also ran through the whole `verify`: `tests` alone failed.
- **Numbers:**
  - 275 unit tests (+65), 0 skipped;
  - 6 `verify` stages, about 32 s;
  - 17 Python files (+4);
  - 3 skill folders, 3 plugins, 3 marketplace entries;
  - crux-finder's `checks.py` unchanged: 10 cases, every bar met.
- **Review (`/code-review high`), 7 findings: 7 fixed and 0 skipped.** The owner chose to fix
  all seven.
  - **A page that says it denied access is a failed call, not a refused one.** Only the engine's
    own words, "denied by your permission settings", mark an error result `(denied)`; a site's
    block page had been read as a permission refusal.
  - **A case the runner did not send costs only itself.** The cases that came back under their
    own names are written. The stray name is reported, with a `prompt.md` whose `name:` differs
    from its folder as the likely cause. Before, one renamed case discarded a whole paid call.
  - **A value the runner cannot read skips that run,** never the command: a cost that is not a
    number, or a line break in a grader's name, had ended it with a traceback.
  - **A path is replaced only where it ends,** so `…/claude-skills` is never taken inside
    `…/claude-skills-old`; the home folder's leftover check keeps the same boundary.
  - **The ceiling is rounded down to the cent,** never up past what is left.
  - **A call that leaves no result is taken to have spent its whole ceiling,** so no later call
    in the command runs on money that may already be gone.
  - **`ARCHITECTURE.md` said every verdict field is scrubbed;** it is the explanation, with the
    reply, the calls and the run's error.
  - **Falsified:** each of the six code fixes undone in turn failed its own new test: the denial
    wording, a stray or renamed case, a cost that is not a number, a sibling path, a ceiling of
    4.996, a call with no result.
  - **Numbers after the review:** 281 unit tests (+6), 0 skipped; the other counts unchanged.

---

## E2: crux-finder's cases on the new engine

**Read:** `FEATURE-eval-engine.md` EE 3, 5–8; `ARCHITECTURE.md` invariants 6 and 7, *The data
layer*, *The eval harness*, *crux-finder* (Decided), *Known debt*; E1's done-note;
`evals/crux-finder/cases/` (each `input.md` and `gold.md`, its note included),
`evals/crux-finder/checks.py`, `tests/test_crux_finder_checks.py`.

- **The ten cases** (EE 7): for each, a `prompt.md` holding the input's body unchanged, with
  the frontmatter E1 measured to be needed (`allowed_tools`), and no line saying no reply is
  possible: round 1's runs had none, and the one-sided case's gold needs the skill free to ask
  for the other side's own words; and graders
  drawn from its `gold.md` and its note: crux, type and *no statement about people*, plus the
  gate and no-conflict rules where gold has them. The session drafts each grader; the owner
  approves every one before it is committed.
- **The golds:** unchanged, except `real-lincoln-douglas/gold.md`, which gains the `source:`
  and `license:` lines of its `input.md`. That case has no claude.ai reply, and its old results
  go in this commit, so its gold precedes every result it will have.
- **The new checks** (EE 3–8), in `evals/crux-finder/checks.py`, rewritten on the shared code E1
  left: gold's fields and `approved_by`; the gold order, reckoned from the first commit of the
  results present now (each file's adding commit, the earliest of them), never from the
  folder's whole history, which still holds round 1's retired results; graders unchanged since
  each `run-N.md`'s commit, which does not apply to `claude-ai.md`, older than every grader;
  the pass bars from the verdicts and the owner's corrections; quotes, symmetry and
  length from each `run-N.md`; stability from the owner's record; the claude.ai rows from
  `claude-ai.md` and its `review.md`; *Runs on the skill as it stands*. Its tests rewritten
  with it.
- **Retired in this commit,** so no checks ever read results they were not written for:
  `evals/crux-finder/run.py` and its tests; each `input.md`; every `run-N.md` of round 1's
  cycle, and the `review.md` of each case with no claude.ai reply, kept in git. The three
  `claude-ai.md` replies stay (EE 7, 8), and their cases' `review.md` is cut to its
  `## claude-ai` section, since it also holds sections for the retired runs. `checks.py` then
  reports no cycle yet.
- **Amended at intake, while writing this plan:** the approved plan retired the old harness in
  E3, with the new results. Moving the real case's `source:` and `license:` into its gold
  needs the old results gone before that gold changes, or the gold order fails; so the old
  results, and the checks that read them, go here.
- **Docs.**
  - crux-finder's README: *How it was tested* keeps the fourth cycle's table, and says the
    reports and reviews are in the repository's history; E3 replaces it.
  - `CLAUDE.md`: *Commands* (the old runner's line removed, `checks.py`'s line as it now is);
    invariant 7's wording if the gold order's reckoning needs it (invariant 6 is reworded from
    the intake).
  - `ARCHITECTURE.md`: *The data layer*'s and *The eval harness*'s Built parts; invariants 6
    and 7's *Enforced by*; *Testing strategy*; the baseline, whose `checks.py` row now reads no
    cycle yet.
- **Confirms:** *The data layer* (the case and result formats, gold.md's fields); *The eval
  harness* (the review method).
- **Ask at the start of E2:**
  - How the owner's correction of a verdict is recorded and counted (EE 6). *Recommended:* one
    line per correction in the case's `review.md`, which `checks.py` counts over the grader's.
  - How each gold's note becomes graders. *Recommended:* one `llm` grader each for crux and
    type, whose criteria quote gold's fields and the note's "what else counts as a match"; a
    regex or `llm` grader for statements about the people, the session's proposal per case.

**Gates:**
- `uv run scripts/verify.py`, green, with these tests: every check above, each falsified,
  including a gold changed after its results, a gold changed after retired results and before
  the present ones (which passes), a grader changed after a run's commit, a grader newer than a
  `claude-ai.md` (which passes), a correction counted over a verdict, and a quote not in the
  prompt.
- `uv run evals/crux-finder/checks.py` reports ten cases, no cycle yet, the claude.ai rows
  3 / 3, and exit 0.
- The engine loads all ten cases (one cheap run of one case, nothing committed).

**Watch for:**
- **The type bar has no slack** (*Known debt*): write the type grader from gold and its note,
  not to the piano case's known miss.
- **The session never commits a grader the owner has not approved.**
- **A prompt's text is final once its gold exists:** quotes are checked against it.
- **Three gold files must not change** (`empirical-studio-kiln`, `one-sided-games-night`,
  `no-conflict-quiz-team`): their claude.ai replies are results.

**Done (2026-11-25, no release).**
- **Decided with the user:**
  - **The block's three Asks, at the start:**
    - **Corrections:** a line per failed verdict in `review.md`, `fail` confirming and `pass`
      overruling, counted over the engine's verdict; a failed verdict with no line is a problem.
    - **Graders:** type by its label (a regex), except where gold ties type to more than the
      label; crux, people and the gate as `llm` graders quoting gold.
    - **The judge:** `claude-sonnet-5-5`. The session recommended keeping `claude-haiku-5-5`; the
      owner chose the stronger reader.
  - **Mid-session, the graders:** the owner had a second model (Fable) review the 32 drafts
    before approving them. It found nothing misquoted and twelve points: seven wording fixes the
    session applied, and four rules gold left open, which the owner settled as the session
    recommended:
    - a favourable statement about a party counts as a statement about people;
    - a **No crux** report fails crux where gold gives a crux;
    - in the debate excerpt, a match outranks the excluded "endure half slave and half free"
      crux when one sentence holds both;
    - in the one-sided case, a reply with no `## Crux report` heading and no `### The crux`
      section writes no report.

    The owner approved all 32 after the fixes.
  - **Confirms:** *The data layer* and *The eval harness*, confirmed with the plan.
- **The ten cases** in the engine's format:
  - each `input.md` moved to `prompt.md` with `git mv`, body unchanged, frontmatter
    `allowed_tools: [Skill, Read]`, `max_turns: 20`, `timeout_seconds: 900`;
  - 32 graders: `crux`, `type` and `no-statement-about-people` in every case, `gate` in the
    one-sided case and `no-conflict` in the no-conflict case; 9 regex and 23 `llm`;
  - `real-lincoln-douglas/gold.md` gained its input's `source:` and `license:`, byte for byte.
    No other gold changed.
- **The judge pin** in `evals/run.py`: `claude-sonnet-5-5`.
- **`evals/crux-finder/checks.py`,** rewritten on `evals/shared.py`:
  - per case, the prompt, the grader set and gold's fields;
  - gold order from the results present now, each file counted from its latest adding;
  - the case as each run had it, prompt and graders;
  - each run and its verdicts;
  - `review.md`'s run sections and the owner's lines;
  - the bars over each run's effective verdict;
  - the claude.ai smoke row;
  - "no cycle yet" when only claude.ai replies are present.
- **Retired,** in this commit: `evals/crux-finder/run.py`, `tests/test_crux_finder_run.py`, round
  1's twenty `run-N.md`, and the `review.md` of the seven cases with no claude.ai reply. The three
  `claude-ai.md` stay, their `review.md` cut to `## claude-ai`.
- **Tests:** `tests/test_crux_finder_checks.py` rewritten: the pure functions' tests carried
  over, and the new checks on a fictional repository whose results `shared` writes.
- **Docs:**
  - crux-finder's README: the last sentence of *How it was tested* says where the reports are.
  - `CLAUDE.md`: invariants 6 and 7, *Commands*, *Exclusive resources*, the synced-upload line.
  - `ARCHITECTURE.md`:
    - *Overview*, *Context* (E2's measurements), *Layout*;
    - invariants 6 and 7;
    - *The data layer* (Decided: the corrections; Built: the cases, prompts, graders, gold and
      `review.md`);
    - *The eval harness* (Decided: the three Asks and the four rules; Built: `checks.py`);
    - *Testing strategy*, the baseline, a *Decision log* line.
- **Amendments:**
  - **The case as it ran includes `prompt.md`,** not only the graders, since quotes are checked
    against the prompt as it is now. It came with the plan the owner approved.
  - **The per-case row is "Gold order + approved_by + graders as run",** since it now counts a
    case whose graders changed since a run as unsound. It came with the plan.
- **Measured** (`claude` 2.1.330, $0.22 in all):
  - **Loading, $0:** the engine reads every `prompt.md` before it filters by `--case`. A call
    naming no case loaded all ten with no error. A copy with an unknown key in one prompt named
    that case. A grader is not read at load: an unknown grader type passed it.
  - **One trial run** of `empirical-studio-kiln` through the runner (`--trial`, outside the
    repository): $0.21 for the run and $0.013 for the judge, 5 turns, 32 s. The skill fired and
    read the template and the types. `crux` and `no-statement-about-people` passed 3/3 votes and
    the `type` regex matched. No kept folder was left, and the trial folder was deleted.
- **Checked by hand:**
  - **The regexes against round 1:** every `regex` grader compiled by JavaScript and run on round
    1's 23 outputs before they were retired. All 22 verdicts with an owner's field agreed, both
    piano runs failing as Value. The no-conflict patterns failed on other labels and passed a
    Framing label.
  - **`checks.py` on round 1's results before retiring them:** every old `run-N.md` reported
    unreadable in the new format, and the debate gold's change was caught against its present
    results.
  - **The three golds** with claude.ai replies are unchanged against HEAD.
- **Falsified:** each of `checks.py`'s new checks broken in turn, the whole test file run each
  time, and each break failing at its own test (30 breaks, the file restored after):
  - **the case:** quotes against the prompt's body, not the whole file; the three graders
    present; no grader that no bar reads;
  - **gold order:** a file counted from its latest adding (the retired-results tests); gold
    before each adding; gold unchanged since; no uncommitted gold; gold in each output's commit;
  - **the case as it ran:** the prompt unchanged; graders added or removed; graders changed;
    graders in the commit; a claude.ai reply not held to the graders;
  - **verdicts:** `verdicts-N.md` present; none without a run; one for each grader; none for
    another;
  - **review.md:** a line for each failed verdict; the owner's line counted over the verdict;
    stability from run 2; none on run 1; a note; pass or fail; no unknown field;
  - **runs and bars:** a run's header names its place; "no cycle yet" on the smoke test; the
    people, crux and type bars from the effective verdict; every results entry read.

  `tests/test_evals_stdlib.py`'s guard now names the runner, the shared code and `checks.py`
  instead of counting four files, since the old runner is gone; with `checks.py` moved away it
  failed.
- **Numbers:**
  - 299 unit tests (+18: −75 and −22 retired, +115 new), 0 skipped;
  - 6 `verify` stages, about 27 s, down from 32: each `check()` reads the case folders once per
    commit, seven git calls for a cycle in place of about 130;
  - 15 Python files (−2);
  - 3 skill folders, 3 plugins, 3 marketplace entries;
  - `checks.py`: `checks: 10 case(s), 0 problem(s); no cycle yet, so the cycle's bars are not
    counted; the claude.ai smoke test met`, exit 0, the smoke row 3 / 3.
- **Review (`/code-review high`), 2 findings: 2 fixed and 0 skipped.** The owner chose to fix
  both.
  - **A result file renamed under `results/` escaped the gold order:** git logs a rename as a
    rename, never as an adding, so the renamed file had no commit to reckon from and was skipped.
    Reproduced in a scratch repository. The log and the diff now take `--no-renames`, and a
    committed result that no commit adds is a problem rather than a pass.
  - **A run file that could not be read was reported twice,** as unreadable and as lacking its
    commit. The header is checked only once the file is read.
  - **Falsified:** `--no-renames` dropped from the log, the unattributed-result problem removed,
    and the read guard dropped, each failing at its own new or tightened test.
  - **Numbers after the review:** 301 unit tests (+2: three added, one that proved nothing
    dropped), 0 skipped; the other counts unchanged.

---

## E3: crux-finder's first cycle on the new engine

**Read:** `FEATURE-eval-engine.md` EE 5, 7, 9; `ARCHITECTURE.md` *The eval harness*, *The data
layer*, *crux-finder* (its eval cycles), *Known debt*; E2's done-note; crux-finder's README,
*How it was tested*.

- **The cycle** (EE 7, 9): ten cases, two runs each, through the shared runner at four at a
  time; `checks.py` on the results.
- **The owner's reading** (EE 5, 6): every failed verdict, one run per case, and stability
  (the two crux sentences of each case side by side), recorded as E2 settled.
- **The comparison:** the summary table beside Session 7c's, in the done-note.
- **A missed bar is a stop.** The owner decides whether a grader or the skill is at fault. A
  grader changed means its case starts over; a skill changed means a version and another cycle
  (an inserted E3a).
- **Ask at the start of E3:** the cycle's cost ceiling, `--max-cost-usd`, which the shared runner
  requires. Amended in Session E1.
- **Docs.**
  - crux-finder's README: *How it was tested* and its table, rewritten for the new engine and
    method.
  - `ARCHITECTURE.md`: *crux-finder*'s eval cycles; *The data layer*'s latest cycle; the
    baseline.

**Gates:**
- `uv run scripts/verify.py`, green.
- `uv run evals/crux-finder/checks.py`: every pass bar met, exit 0.

**Watch for:**
- **A real transcript can hold a word on the term list** (`CLAUDE.md`): ask the owner; never
  trim a quote silently.
- **A commit message that describes the cycle's output** in the attribution rule's words fails
  hygiene. Say what changed.
- **`run.py`'s successor skips a run whose file exists:** a cycle on a changed skill starts by
  removing the old results.

**Done (2026-11-25, no release).**
- **Decided with the user:**
  - **The ceiling** (the block's Ask): `--max-cost-usd 10`, as recommended, against an estimate
    of about $6.
  - **How the owner's reading is made** (the handoff's Ask), as recommended: a fresh reader that
    sees each case's prompt, gold.md and its note, the graders and each run's reply, never a
    verdict, drafts a verdict for every grader of every run, the stability call and a note; the
    session sets it beside the engine's verdicts and names every disagreement; the owner
    confirms or corrects every line. The one run per case is run 1, fixed before any result.
  - **At a stop, mid-session:** fix `checks.py`'s gold order here rather than leave it to the
    backlog (Amendments).
- **The cycle** (1.0.0 from `3a97160`, `claude` 2.1.330, `claude-opus-5-5`, judge
  `claude-sonnet-5-5`): `uv run evals/run.py crux-finder --runs 2 --max-cost-usd 10` wrote all
  20 runs in one engine call, exit 0, in 3 min 16 s, for $4.97 ($4.39 for the runs, $0.13 to
  $0.30 each; $0.58 for the judging). Every run called `crux-finder:crux-finder` and read the
  references (37 reads), with no denied or failed call, 3 to 6 turns, no error. No machine path
  in any result, and no kept folder left under `/private/tmp`.
- **The owner's reading:** the reader, reading no verdict, agreed with the engine on 61 of 64
  verdicts. The three it disputed were `no-statement-about-people` on run 1 of the kiln, piano
  and solar cases, which the judge failed by 2, 3 and 3 votes of 3 with no reason recorded (the
  engine keeps only the votes). The owner confirmed every drafted line: a `pass` overruling
  each of the three, a `fail` confirming both piano type verdicts, `same_crux_as_run_1: yes` in
  all ten cases, and a note on every run. Ten `review.md`, seven new and three after their
  `## claude-ai` section.
- **The summary table** (`checks.py`, 0 problems, exit 0, 3 of 64 verdicts overruled), beside
  Session 7c's (0.4.0, the retired runner, the owner's review of every run):

  | Check | Pass bar | 7c | E3 | Met |
  |---|---|---|---|---|
  | Crux matches gold | ≥ 16 / 20 runs | 20 / 20 | 20 / 20 | yes |
  | Type matches gold | ≥ 18 / 20 runs | 18 / 20 | 18 / 20 | yes |
  | Stability: same primary crux in both runs | ≥ 8 / 10 cases | 9 / 10 | 10 / 10 | yes |
  | Quotes verbatim | all runs | 20 / 20 | 20 / 20 | yes |
  | Steelman symmetry | all reports | 18 / 18 | 18 / 18 | yes |
  | Length ≤ 400 words | all reports | 18 / 18 | 18 / 18 | yes |
  | No statement about people (7c: people_statement no) | all runs | 20 / 20 | 20 / 20 | yes |
  | One-sided gate fires | all runs with its grader | 2 / 2 | 2 / 2 | yes |
  | No-conflict case reports no conflict or a Framing crux | all runs with its grader | 2 / 2 | 2 / 2 | yes |
  | Gold order + approved_by + graders as run (7c: without graders) | all cases | 10 / 10 | 10 / 10 | yes |
  | Runs on the skill as it stands (decision 22) | all runs | 20 / 20 | 20 / 20 | yes |
  | claude.ai smoke test | 3 / 3 cases | 3 / 3 | 3 / 3 | yes |

- **What the results showed:**
  - **Type and crux:** every case but the piano lessons matched gold on both; both piano runs
    read as Value again, the *Known debt*, the bar's two allowed misses. Solar took the ten-year
    payback in both runs, the kiln and orchard their record cruxes, the father's care the wish
    set against the risk, not the excluded carers question.
  - **Stability:** 10/10, where 7c's was 9/10: both debate runs took the founders' policy, one
    of the two cruxes gold accepts, with the local-variety-or-division question a secondary crux.
  - **Length and symmetry:** 194 to 354 words (7c: 194 to 358), the excerpt at 354 and 351;
    every steelman pair within 25%, the widest 46/39.
  - **Quotes:** two runs quoted the input (vintage run 2, solar run 1), every span verbatim.
  - **The owner's notes, below any bar,** as 7c's: what would move it leaving out a record gold
    names (the pitch fee invoices in both orchard runs, the supplier's readings in both kiln
    runs) or setting its own figure for a dated check (both solar runs); common-ground lines
    that widen what a party said (quiz, excerpt), and a not-in-dispute line that does (kiln).
- **No version:** no shipped file changed.
- **Docs:**
  - crux-finder's README: *How it was tested* rewritten for the engine and the reading, with
    this cycle's table.
  - `ARCHITECTURE.md`:
    - *Overview* Built;
    - invariant 7's *Enforced by*;
    - *The data layer* (Decided: the reading; Built: the results present);
    - *crux-finder* Built: the first cycle on the engine;
    - *The eval harness* Built: gold order, a decision on uncommitted results, the runner's
      first cycle;
    - *Testing strategy*, *Known debt*, the baseline, a *Decision log* line.
  - `docs/BACKLOG.md`: the people grader's false fails and the judge's missing reasons; the
    review notes' direction extended to this cycle.
- **Amendments:**
  - **`checks.py` changed, where the plan had no code:** before the reading, it reported the
    debate case's gold as changed since its new, uncommitted `run-1.md` and `run-2.md`, which it
    reckoned from round 1's adding of the same paths (`c52b303`), before Session E2 gave that
    gold its `source:` and `license:`. It now reckons from history only the files HEAD holds;
    an uncommitted one follows HEAD, whose gold and its lack of uncommitted change were already
    checked. It never gave a false pass. Decided with the user at a stop, with one test added.
- **Measured:** the cycle's cost, time and calls (above); `claude` 2.1.330 before and after.
- **Checked by hand:** the reader's report lists only the case files and `run-N.md` it read; no
  `/Users/`, `/var/folders` or `/private/` path in `results/`.
- **Falsified:** the new reckoning put back as it was (an uncommitted file reckoned from the
  latest adding of its path): only the new test failed, in both its forms (uncommitted, and
  staged), and all 119 passed once restored. A coarser break, dropping the guard alone, failed
  44 tests, since every uncommitted file then read as committed with no adding.
- **Numbers:**
  - 303 unit tests (+2, the new test's two forms), 0 skipped; 119 in
    `test_crux_finder_checks.py`;
  - 6 `verify` stages; 15 Python files (±0);
  - 3 skill folders, 3 plugins, 3 marketplace entries (±0);
  - `results/`: +40 run and verdicts files, +7 `review.md`, 3 extended;
  - `checks.py`: `checks: 10 case(s), 0 problem(s); every pass bar met`, exit 0.
- **Review (`/code-review high`), 5 findings: 5 fixed and 0 skipped.** The user asked for
  every finding fixed.
  - **A result path git would quote skipped the gold order** (older than this session, which
    copied the pattern into one more call): `git ls-tree`, `git diff --name-only` and `git log
    --name-only` print a name with a non-ASCII letter quoted and escaped, so it matched no
    folder, and its gold read as uncommitted and its results as never added. All four calls in
    `checks.py` now take `-z` and split on NUL; the log's one newline after each commit line is
    the only one stripped. One test, a case whose id has a non-ASCII letter.
  - **The handoff set a rule nobody decided,** that P3's `checks.py` reckon gold order as
    crux-finder's now does. It now says what crux-finder's does and leaves P3's to P3 and the
    owner.
  - **The README said "report" where the one-sided case writes none:** each reply was graded,
    and one full reply per case read.
  - ***The eval harness* misdated the false problem:** the decision now says the gold changed
    in E2 and the false problem showed in E3's uncommitted cycle.
  - **This done-note put the kiln's widening under common ground;** it was in its
    *Not actually in dispute* line.
  - **Falsified:** each of the four git calls put back in its old form, without `-z` and split
    on newlines, one at a time: each failed only the new test, and all 120 passed once restored.
    Dropping `-z` alone, keeping the NUL split, failed 5 to 54 tests, since the names then ran
    together, so it was not taken as the falsification.
  - **Numbers after the review:** 304 unit tests (+1), 0 skipped, 120 in
    `test_crux_finder_checks.py`; the other counts unchanged; `checks.py` 0 problems, exit 0.

---

## P2: provenance-tracer's cases

**Read:** `FEATURE-provenance-tracer.md` PT 3, 6–8, and the spec's *Evals*, *Labels*, *Output
format* and *Guardrails*; `FEATURE-eval-engine.md` EE 2, 3; `ARCHITECTURE.md` invariant 7, *The
data layer*, *The eval harness*, *provenance-tracer*; E1's and E3's done-notes; one crux-finder
case as the pattern.

- **Thirteen cases** under `evals/provenance-tracer/cases/<id>/`, the spec's seven forward and
  six behaviour cases, each with:
  - `prompt.md`: the input, `allowed_tools` with the web tools, `max_turns` and
    `timeout_seconds` sized for 20 searches and 25 fetches, and the no-reply line except in the
    several-claims case (PT 6, 7);
  - graders per the spec's *Graders* table, as far as the engine expresses them (PT 8);
  - `gold.md`: `approved_by`, the authoring date, the expected labels and the required facts,
    each fact checked on the web at authoring, with its source.
- **Ids** name the row and the topic, as crux-finder's do (`misattributed-quote-…`,
  `private-person-…`); an id is never renamed once it has results.
- **Docs.** `ARCHITECTURE.md`: *The data layer*'s Built part (the cases as committed).
- **Ask at the start of P2:** the true-statistic case and the obscure claim, from two or three
  candidates each, with the reason each fits.

**Gates:**
- `uv run scripts/verify.py`, green.
- One or two cases run once through the runner, to prove the suite loads and to measure one
  run's cost, time, and number of searches and fetches. Nothing they write is committed.

**Watch for:**
- **The session never writes a `gold.md` the owner has not approved,** and never a fact it did
  not open a source for (the skill's own *Honest nulls* rule applies to its cases).
- **No case is one of the skill's own examples** (P1's references).
- **Live facts go stale:** the authoring date is in each gold, and re-authoring re-verifies.

**Done (2026-11-26, no release).**
- **Decided with the user:**
  - **The block's Ask, as recommended:** the true statistic is the ONS's "In the 2021 census, one
    in six people in England and Wales were born outside the UK", the office's own words; the
    obscure claim is Elbert Hubbard's "damn fool … five minutes every day", which Quote
    Investigator traced on 20 November 2026, after the model's training cutoff. Each was chosen
    from candidates whose sources the session had opened: the 2020 US census count for the first,
    a copier-market forecast and a gambling quip credited to Wilson Mizner for the second.
  - **Two more at the start, as recommended:** each modifier a row lists is required and any
    other is allowed in the skill's fixed order, since the spec's MMR row leaves out the Mutated
    its Primary differs implies; the trial is the MMR and private-person cases, at most $5.
  - **With the plan:** the non-interactive case reuses the echoed-statistic prompt; `footer`
    checks both fixed lines and runs in the ten forward-report cases; `no-verdict` runs in all
    thirteen; the personal chain is one message; `no-search`, `no-fetch` and
    `manager-not-searched` are `tool_used` graders.
  - **Mid-session:** the owner approved the behaviour batch as drafted and asked for the smoking
    case to be replaced "with something happier"; from three candidates, they chose "Regular
    exercise lowers the risk of heart disease", with the same labels, and approved the forward
    batch with it. After the trial, they approved two clauses added to every `facts` and
    `no-verdict` grader (Amendments).
- **The thirteen cases,** `evals/provenance-tracer/cases/`, each a `prompt.md`, its graders and a
  `gold.md` the owner approved, all committed together before any result:
  - six labelled forward cases (`misattributed-quote-gandhi`, `popular-myth-ten-percent-brain`,
    `echoed-statistic-goldfish-attention`, `retracted-origin-mmr-autism`,
    `well-sourced-exercise-heart-disease`, `true-statistic-born-outside-uk`), the facts-only
    `obscure-claim-hubbard-fool`, and six behaviour cases (`reverse-mode-stanford-prison`,
    `personal-chain-bilingual-speech`, `no-memory-bilingual-speech`,
    `non-interactive-goldfish-attention`, `private-person-neighbour-theft`,
    `multiple-claims-lightning-bulls`);
  - 45 graders: `facts` and `no-verdict` in all 13 (26 `llm`), `labels` in 6 and `footer` in 10
    (16 `regex`), and 3 `tool_used`;
  - every web fact with the page opened for it at authoring; the behaviour cases' musts are the
    spec's.
- **Docs:** `ARCHITECTURE.md`'s *Overview* and *Layout* Built (and *Layout*'s line on
  crux-finder's results, which still named only round 1's replies), *Context* (P2's
  measurements, the CLI's version for E3 and P2), *The data layer* (provenance-tracer's cases),
  *provenance-tracer* (Decided: the cases; Built: the cases and the trial), *The eval harness*
  Built (the trial), a *Decision log* line; P3's block names the graders it maps to bars.
- **Amendments:**
  - **The well-sourced case's claim** is exercise and heart disease, not the spec's smoking
    claim: the owner's request, mid-session. `FEATURE-provenance-tracer.md` is unchanged, as
    read-only; *provenance-tracer*'s Decided part records it.
  - **`footer` reads the spec's "every run" as every forward report,** since the reverse report,
    the refusal and the question carry no footer in the spec's own formats. Amended at plan time,
    with the owner.
  - **Two clauses in every `facts` and `no-verdict` grader,** after the trial: a fact's
    bibliographic detail is not required, and a source's title or headline and a named study's or
    fact-check's conclusion credited to it are not verdicts. The engine's judge failed the MMR
    run's `facts` and `no-verdict` 3/3; a fresh reader that gave its reasons drafted FAIL on both,
    for those two readings, then PASS on checking each sentence. The owner approved the clauses;
    no gold changed, and the run was not repeated.
- **Measured** (`claude` 2.1.330, `claude-opus-5-5`, judge `claude-sonnet-5-5`, skill 0.1.0):
  - **Loading, $0:** all thirteen cases loaded from a copy without `gold.md`; one unknown key in a
    copied `prompt.md` failed the load, named.
  - **The trial,** `uv run evals/run.py provenance-tracer --runs 1 --max-cost-usd 5 --case
    retracted-origin-mmr-autism --case private-person-neighbour-theft --trial <scratchpad>`, exit
    0, 5 min 35 s, $1.63:

    | Case | Cost | Time | Turns | Searches / fetches | Judge | Verdicts |
    |---|---|---|---|---|---|---|
    | `retracted-origin-mmr-autism` | $1.47 | 334 s | 38 | 7 / 23 (2 errors) | $0.047 | `footer` pass; `labels`, `facts`, `no-verdict` fail |
    | `private-person-neighbour-theft` | $0.10 | 15 s | 3 | 0 / 0 | $0.011 | all four pass |

    The MMR run read the four references, took a 1996 pilot study (through Wikipedia and Crossref)
    as the root and Wakefield's paper as a Primary node, and reported both retraction notices from
    their index records; *The Lancet* and *The BMJ* returned 403. The private-person run called
    the Skill alone and refused. No kept folder was left; the trial folder was deleted; no machine
    path in either result.
  - **Pages the fetch tool refuses,** at authoring: PubMed and PubMed Central, *The Lancet*, *The
    BMJ*, the BBC, *The New York Times*, the Wayback Machine. Europe PMC's and Crossref's APIs
    open.
- **Checked by hand:** in node, every `regex` grader compiles and passes template-shaped replies
  (CRLF included), and each fails its near misses: a wrong value, a missing or out-of-order
  modifier, an extra word after the modifiers, the count line, the footer or the earliest-instance
  line altered or missing; `input_match` matches "Manager" and "MANAGER" in a JSON query and not a
  query without it. The written cases are byte for byte the drafts the owner approved, apart from
  the two clauses.
- **Falsified:** the MMR `labels` pattern with Origin retracted made optional, and the
  `input_match` narrowed to a lower-case m, each failed the node check (3 failures), and the
  regenerated cases passed it; the load check with an unknown key (above).
- **Numbers:** 304 unit tests (±0), 0 skipped; 6 `verify` stages; 15 Python files (±0); 3 skill
  folders, 3 plugins, 3 marketplace entries; 13 cases, 45 graders; crux-finder's `checks.py`
  unchanged.
- **Review (`/code-review high`), 5 findings: 5 fixed and 0 skipped.** The owner chose to fix
  all five.
  - **Gold facts stated details their cited page did not hold.** Each fact now cites the page
    it rests on, a fact split where its clauses came from two pages, with no fact changed in
    substance, still before any result: exercise's four facts (the 1953 paper by its Europe PMC
    record, the bus finding by Wikipedia, each Paffenbarger study by its own record); MMR's fact 2
    split, "eight of the 12" cited to its Europe PMC record and "did not claim to prove" to
    Wikipedia; goldfish's report named by its Scribd copy, as a fact not required; and the
    ten-percent case's fact 1 narrowed to what James's essay says. Their `facts` graders quote
    the new golds. The owner approved the changed golds by choosing this fix.
  - **The handoff said eleven cases' graders had not run:** no case's `llm` graders have run as
    committed.
  - ***The data layer*'s grader list was split** by the paragraph on the two clauses, with one
    over-long line; it now follows the list.
  - ***The data layer* misstated two prompts' request lines** (the private-person "claim", the
    several-claims "these").
  - ***The data layer* called the inputs "claims in public circulation",** a category
    `CLAUDE.md`'s fixtures rule does not list; it now says each was written by the session and
    approved by the owner, as crux-finder's synthetic cases were.
  - **Checked:** the node check passes on the regenerated cases (no `regex` or `tool_used` grader
    changed); only the four cases' `gold.md` and `facts.md` changed. Each new source is a page
    opened at authoring.
  - **Numbers after the review:** unchanged.

---

## P3: provenance-tracer's checks and first cycle

**Read:** `FEATURE-provenance-tracer.md` PT 5, 8, and the spec's *Evals*; `FEATURE-eval-engine.md`
EE 4–6, 9; `ARCHITECTURE.md` invariants 5–7, *The eval harness*, *The data layer*,
*provenance-tracer*; P2's done-note; `evals/crux-finder/checks.py` as the pattern.

- **`evals/provenance-tracer/checks.py`** and its tests, on the shared code: gold's fields and
  order; graders unchanged since each run's commit; a case passes at 2 of 3 runs; the spec's
  hard checks on every run (no verdict, footer lines, the quote rule, no search in the
  private-person case, the manager never in a query); every chain URL in one of the run's
  fetches; the summary table; *Runs on the skill as it stands*.
  - **The graders P2 left,** each a bar's input (amended in Session P2): `labels` (six cases),
    `facts` and `no-verdict` (all thirteen), `footer` (the ten forward reports), `no-search` and
    `no-fetch` (the private-person case, together the spec's "No search issued") and
    `manager-not-searched` (the personal-chain case). gold.md's fields are in *The data layer*.
- **The cycle:** thirteen cases, three runs each, four at a time.
- **The owner's reading** (PT 5): every failed verdict and one run per case.
- **Docs.**
  - `CLAUDE.md`: provenance-tracer's checks in *Commands*.
  - `ARCHITECTURE.md`: *provenance-tracer*'s first cycle; *The eval harness*'s Built part; the
    baseline.
- **Ask at the start of P3:** the cycle's cost ceiling, `--max-cost-usd`, from P2's measured
  cost per run.

**Gates:**
- `uv run scripts/verify.py`, green, with each check above falsified.
- `uv run evals/provenance-tracer/checks.py` run on the cycle; its table in the done-note,
  met or not.

**Watch for:**
- **A missed bar is not fixed here.** P4 changes the skill, each change general, never fitted to
  one case.
- **Live-web runs differ between cycles** for reasons outside the skill: record a fetch that
  failed as the run saw it.
- **A reply can hold a word on the owner's term list,** or a researcher's name: names of public
  figures are allowed (PT 3); a listed term is asked about.

**Done (2026-11-27, no release).**
- **Decided with the user:**
  - **The block's Ask:** `--max-cost-usd 75`, as recommended, against an estimate of about $52.
  - **The handoff's Ask, gold order:** as crux-finder's, with that code moved into
    `evals/shared.py` so both skills run one copy, as recommended.
  - **With the plan:**
    - a case passes when 2 of its 3 runs pass `labels` and `facts` together;
    - the quote rule per line and per linked source, *How it changed* per line only, the user's
      text exempt;
    - a reverse report's source and popular-version links held to the fetches;
    - after the plan's adversarial review, five readings: the heading's claim exempt, a
      blockquote a quote, a `per`/`cited by` link not a quote's source, a forward report with
      no chain a problem, `footer` wherever `labels` is.
  - **Mid-session, on the cycle's replies:** the quote rule stays strict, a quoted word or year
    a quote; the remaining $65 of the ceiling spent on the runs a usage limit had refused.
  - **The reading:** four verdicts overruled to pass (personal-chain runs 1 and 3 `facts`, Gandhi
    run 3 and MMR run 1 `no-verdict`); MMR's Fudenberg root judged wrong, its run 1 `facts`
    confirmed fail; every `labels` fail and exercise's two `facts` fails confirmed, with notes
    for P4.
- **Shipped:**
  - `evals/provenance-tracer/checks.py` and `tests/test_provenance_tracer_checks.py` (62
    tests);
  - `evals/shared.py` gains the reckoning crux-finder's `checks.py` had built: gold order,
    graders as run, the skill as it stands, `review.md`, words and quotation marks, the table.
    crux-finder's `checks.py` calls it through thin wrappers, its output byte for byte the same.
    An untracked file in the skill folder now counts as a change to the skill;
  - one crux-finder test, a claude.ai reply's commit checked for gold;
  - the cycle: 39 `run-N.md` and `verdicts-N.md`, and 13 `review.md`.
- **The cycle** (0.1.0 from `641ce2a`, `claude` 2.1.330 throughout, `claude-opus-5-5`, judge
  `claude-sonnet-5-5`):
  - **First call** (`--max-cost-usd 75`): 9 runs before the account's usage limit refused the
    rest. Two of the 9, Gandhi runs 2 and 3, came back with their `llm` judges refused and
    written as fails. The session removed them, uncommitted (*Context*; `docs/BACKLOG.md`).
  - **Second call** (`--max-cost-usd 65`, the rest of the ceiling): the other 32, exit 0, 23 min
    31 s.
  - **Spend:** $46.71 for the 39 kept ($45.16 runs, $0.12 to $1.75 each; $1.55 judging), $2.88
    for the two removed. 253 searches, 553 fetches (57 errors), 12 to 357 s a run, no error
    header, no kept folder, no machine path.
- **The owner's reading,** made as E3's: four fresh readers, each given a bundle of its cases'
  prompts, golds, graders and runs and no verdict, drafted every verdict and run 1's note. They
  agreed with the engine on 130 of 135; the five disputes and every failed verdict went to the
  owner, who confirmed or corrected each line (above).
- **`checks.py` on the cycle:** `checks: 13 case(s), 59 problem(s); pass bars not met: Cases
  passing at 2 of 3 runs (labels and facts), ≤ 1 quote per source, < 15 words`, exit 1. Every
  problem is a quote-rule line.

  | Check | Pass bar | Result | Met |
  |---|---|---|---|
  | Cases passing at 2 of 3 runs (labels and facts) | all cases | 9 / 13 | **no** |
  | No verdict in the report's own voice | all runs | 39 / 39 | yes |
  | Footer lines present | all runs with its grader | 30 / 30 | yes |
  | ≤ 1 quote per source, < 15 words | all runs | 14 / 39 | **no** |
  | Every linked source among the run's fetches | all forward and reverse reports | 33 / 33 | yes |
  | No search issued (private-person case) | all runs with its grader | 3 / 3 | yes |
  | Manager never in a search query (personal-chain case) | all runs with its grader | 3 / 3 | yes |
  | Gold order + approved_by + graders as run | all cases | 13 / 13 | yes |
  | Runs on the skill as it stands | all runs | 39 / 39 | yes |

  Verdicts the owner overruled: 4 of 135.
- **What the results showed:**
  - **The cases that miss:**
    - Gandhi, labels 0/3: the 1913 passage did not open in two runs, so No primary found; the
      third opened it and made it a second root.
    - Ten-percent, labels 0/3: James's essay, opened, taken as a Primary that differs, where gold
      has No primary found. The spec's tier definition allows the runs' reading.
    - MMR, 1/3: Fudenberg 1996 as the root in two runs, so no Origin retracted.
    - Exercise, 1/3: Morris alone, not opened, in two runs.
  - **Quotes:** 25 runs quote a source twice: a phrase beside a cited word, two years, a rating
    beside its sentence.
  - **Every other bar is met:** no-verdict 39/39 after the reading, footer 30/30, links 33/33,
    no search 3/3, the manager in no query 3/3.
  - **Behaviour:** one private-person run called Grep, not in its `allowed_tools`, and it ran.
- **No version:** no shipped file changed.
- **Docs:**
  - `CLAUDE.md`: *Commands*.
  - `ARCHITECTURE.md`:
    - *Overview* Built;
    - *Context* (the cycle's limit and calls, the CLI);
    - invariant 7's *Enforced by*;
    - *The data layer* (Decided and Built);
    - *provenance-tracer* Built (the first cycle);
    - *The eval harness* (Decided: the readings; Built: the shared reckoning, provenance-tracer's
      `checks.py` and its decisions);
    - *Testing strategy*, the baseline, a *Decision log* line.
  - `docs/BACKLOG.md`: the judge refusal written as a graded run.
- **Amendments:**
  - **The plan's ceiling ran in two calls,** since a usage limit stopped the first; the second
    spent what was left, at the owner's word.
  - **`skill_unchanged_since` changed with the move:** its test found that an untracked file
    in the skill folder was not counted as a change.
- **Checked by hand:** the readers' bundles held no verdicts file; no `/Users/`, `/var/folders`
  or `/private/` path in `results/`; hygiene green over the results; every run's `claude:`
  header 2.1.330.
- **Falsified:** each check broken in turn, its own test failing, then restored:
  - the case pass at 1 of 3, and without `labels`;
  - a failed fetch, and a subagent's, left out;
  - a missing chain passed;
  - the quote limit at 16;
  - the per-line count, and the per-source count;
  - the prompt exemption (no test failed at first, so one was added), and the heading's;
  - a `per` link taken as the source;
  - blockquotes ignored;
  - the `tool_used` re-count;
  - run 1's required section;
  - the gold-order call;
  - a stray results file allowed;
  - the version-line rule;
  - the untracked-file check;
  - crux-finder's new test, by building gold order from runs alone.
- **Numbers:**
  - 367 unit tests (+63), 0 skipped: 62 in `test_provenance_tracer_checks.py`, 121 in
    `test_crux_finder_checks.py`;
  - 6 `verify` stages; 17 Python files (+2);
  - 3 skill folders, 3 plugins, 3 marketplace entries;
  - `results/`: +78 run and verdicts files, +13 `review.md`;
  - crux-finder's `checks.py` unchanged: 0 problems, every bar met.
- **Review (`/code-review high`), 7 findings: 7 fixed and 0 skipped.** The owner chose to fix all
  seven.
  - **A bold-only line ended a section:** a bold branch label inside a chain left the links after
    it unchecked. A bold line is a heading now only when it names a template section.
  - **The user's-text exemption took any span in the prompt.** The owner was shown the first
    fix, a span needing half the claim's words: on the cycle it flagged the user's own words in
    *How it changed* (quotes 14/39 to 11/39). The owner chose any fragment of a claim instead:
    the prompt's quoted claims and the heading's, never its request line. A source quote that
    repeats the claim's words stays exempt, the stated gap.
  - **A forward report could be read as reverse,** its chain unchecked, where its label line was
    in other markup and its heading unquoted: a label line in any markup, or a chain section,
    now makes it forward.
  - **A bare URL ran on through a table's `|`;** it now ends there.
  - **A `tool_used` grader without `min` was re-counted as `min: 1`,** a default never
    measured; both bounds are now required.
  - **An unreadable run left the linked-sources row,** which could then read met; it now counts
    as a report whose links failed.
  - ***The data layer* called the `review.md` shape settled at the start;** it came with the plan.
  - **Falsified:** each fix reverted in turn, only its own new test failing: any bold line a
    heading; any prompt fragment exempt (the half-claim rule, then the whole prompt for the
    request line); a chain alone not making a report forward; a bare URL through a pipe;
    missing bounds read; an unreadable run not a report.
  - **On the cycle:** `checks.py` prints the same 59 problems and table as before the review.
  - **Numbers after the review:** 374 unit tests (+7), 69 in
    `test_provenance_tracer_checks.py`; the other counts unchanged.

---

## P4: The changes the cycle calls for

**Read:** `FEATURE-provenance-tracer.md` PT 2, 5, 8; `ARCHITECTURE.md` *provenance-tracer*,
*The eval harness*; P3's done-note.

- **The skill changed** for each bar P3's cycle missed, each change general and settled with
  the owner; `0.2.0` in `plugin.json` and `metadata.version`; its `CHANGELOG.md` entry.
- **The next cycle,** on the skill as it stands, after the old results are removed.
- **If P3's cycle met every bar,** this session is dropped, with the reason logged in
  `SESSIONS.md` and the handoff, and the versions after it shift.
- **Docs.** `ARCHITECTURE.md`: *provenance-tracer*, Decided for what the owner settled and
  Built for the cycle; the baseline. The plugin's README where what it does changed.
- **Ask at the start of P4:** the cycle's cost ceiling, `--max-cost-usd`, which the shared runner
  requires. Amended in Session E1.

**Gates:**
- `uv run scripts/verify.py`, green.
- `uv run evals/provenance-tracer/checks.py` on the new cycle; a bar still missed opens an
  inserted P4a, with the owner.

**Watch for:**
- **`SKILL.md` stays under 300 lines** as rules are added: move detail to the references.

**Done (2026-11-27, provenance-tracer 0.2.0).**
- **Decided with the owner:**
  - **At the start:** the ten-percent gold to Primary differs, over a narrower Grounding rule; a
    5-run trial at `--max-cost-usd 10`, then the cycle at `--max-cost-usd 75`; an adversarial
    review of the plan. The owner intends this cycle to be the last: nothing more runs without
    the owner's word.
  - **With the plan, after its adversarial review:** the roots refinements (citing defined, a
    work passing the claim on with a source is a node, precursors, a misattribution adds no root,
    two teams' studies two roots), opening a Primary in other copies, and the quote rule made
    concrete. The review's findings were folded in: goldfish in the trial in place of the
    reverse case, the precursor rule, the footer's quotation marks left alone, nothing in the
    plugin folder edited while a runner call was pending.
  - **After the trial:** Grounding on a study's own data, an association included, with
    correlation stated as causation only where the study stops short of a cause; one quote per
    row of *How it changed*; each root marked in the chain.
  - **The reading:** 7 engine fails overruled to pass; 5 `labels` fails confirmed; the true
    statistic's run 3 `no-verdict` kept a pass, decided by the session at the owner's word. In
    the cycle commit's review, the owner asked the session to decide echoed goldfish run 2's
    `facts` again from fact 1's full text: kept a pass, since fact 1 is the provenance the run
    gives, and run 1, which the engine passed, lacks the same figures.
  - **After the cycle:** commit it and open P4a for a later session.
- **Shipped:**
  - `plugins/provenance-tracer/` 0.2.0: `SKILL.md` (219 lines), the four references, the
    version in `plugin.json` and `metadata.version`, `CHANGELOG.md`, `README.md`;
  - `popular-myth-ten-percent-brain`'s `gold.md` and `labels` grader, re-authored (its three
    pages opened again, unchanged);
  - P3's cycle retired; the second cycle: 39 `run-N.md` and `verdicts-N.md`, 13 `review.md`.
- **The commits:** the release (`fa3326f`), its review (`72e2b04`), two fixes the trial called
  for (`09e4c25`, `429b407`), then the cycle's.
- **The trial** ($6.74, then $1.20, and $0.26 of judging: $8.20): four of five passed every grader with clean quotes;
  exercise read an association as a drift and packed three quotes in a row; its re-check, after
  the fix, gave Independent · Grounded with clean quotes, and a `facts` fail on a report that
  named no root.
- **The cycle** (0.2.0 from `429b407`, `claude` 2.1.330, `claude-opus-5-5`, judge
  `claude-sonnet-5-5`): two runner calls, since the account's usage limit refused 21 runs of the
  first; $49.30 for the runs and $1.70 for judging, $51.00 of $75; no refused judge, no error.
  With the trials, P4 spent $59.20.
- **The owner's reading,** made as P3's: four fresh readers with bundles of prompts, golds,
  graders and runs and no verdicts; they agreed with the engine on 127 of 135.
- **`checks.py` on the cycle:** `checks: 13 case(s), 2 problem(s); pass bars not met: Cases
  passing at 2 of 3 runs (labels and facts), ≤ 1 quote per source, < 15 words`, exit 1.

  | Check | Pass bar | Result | Met |
  |---|---|---|---|
  | Cases passing at 2 of 3 runs (labels and facts) | all cases | 11 / 13 | **no** |
  | No verdict in the report's own voice | all runs | 39 / 39 | yes |
  | Footer lines present | all runs with its grader | 30 / 30 | yes |
  | ≤ 1 quote per source, < 15 words | all runs | 38 / 39 | **no** |
  | Every linked source among the run's fetches | all forward and reverse reports | 33 / 33 | yes |
  | No search issued (private-person case) | all runs with its grader | 3 / 3 | yes |
  | Manager never in a search query (personal-chain case) | all runs with its grader | 3 / 3 | yes |
  | Gold order + approved_by + graders as run | all cases | 13 / 13 | yes |
  | Runs on the skill as it stands | all runs | 39 / 39 | yes |

  Verdicts the owner overruled: 7 of 135.
- **What the results showed:**
  - **Fixed:** quotes 14/39 to 38/39; exercise 1/3 to 3/3; ten-percent 0/3 to 3/3 on its new gold.
  - **Missed:** Gandhi 1/3 (the 1913 text not opened in runs 1 and 3); MMR 1/3 (Fudenberg as
    root 2 through a page about him, runs 1 and 2); one quote run (non-interactive goldfish run
    2, Microsoft's report quoted twice on one line).
  - **Seen, its case still passing:** echoed goldfish run 3 drew a study a cold trail credits as a
    credited text that differs, so Primary differs.
- **Docs:** `ARCHITECTURE.md` (*Overview* Built; *The data layer*; *provenance-tracer* Decided,
  Built, the trial and the second cycle; the baseline; a *Decision log* line); the plugin's
  README and CHANGELOG; this block and P4a's; the handoff.
- **Amendments:**
  - **Two commits and more,** since the runner refuses an uncommitted plugin: the release before
    any run, the cycle after; with the owner.
  - **The owner's review of the release before any spend,** so no later review could leave the
    cycle stale; with the owner.
  - **A trial, and two fixes from it,** each committed before the cycle; with the owner.
  - **P4a inserted,** since two bars are still missed; the owner chose to open it for later.
- **Checked by hand:** the readers' bundles held no verdicts file; every run's header `claude`
  2.1.330 and `commit` `429b407`; no `grader threw`; hygiene green over the results.
- **Falsified:** the new ten-percent `labels` pattern, against P3's three real label lines (match)
  and Grounded, No primary found, Independent and the count line (no match). No other check is
  new.
- **Numbers:** 374 unit tests, 0 skipped, unchanged; 6 `verify` stages; 17 Python files;
  3 skill folders, 3 plugins, 3 marketplace entries; `results/`: 39 runs, 39 verdicts, 13
  reviews, as P3's.
- **The release's review (`/code-review high`), 7 findings: 7 fixed and 0 skipped,** the owner
  choosing to fix all seven, before any run:
  - a precursor does not count as something earlier the root cites;
  - every quote linked, as the spec asks;
  - a credited text counted under the rule for several Primaries;
  - the heading a fixed line;
  - a credited text and a precursor not counted as retellings;
  - the precursor note out of the status checks' list;
  - the handoff kept true between the commits.
- **The cycle commit's review (`/code-review high`), 4 findings: 4 fixed and 0 skipped,** the
  owner choosing to fix all four; none touched the skill folder, so the cycle stays on the skill
  as it stands:
  - echoed goldfish run 2's `facts` overrule had rested on a misstated rule; decided again from
    fact 1's full text, it stays a pass, its `review.md` line giving the reason;
  - the root marking, which the owner settled, added to *provenance-tracer* Decided and the
    *Decision log*;
  - P4's spend given with the trials' judging, $59.20;
  - the handoff names the review commits as they are.
- **After the review:** `checks.py` prints the same 2 problems and table; the other numbers are
  unchanged.

---

## P4a: The changes P4's cycle calls for

Inserted in Session P4, with the owner, since its cycle left two bars unmet. The owner decides at
its start whether it runs a cycle at all.

**Read:** `FEATURE-provenance-tracer.md` PT 2, 5, 8; `ARCHITECTURE.md` *provenance-tracer*,
*The eval harness*; P4's done-note and the cases' `review.md`.

- **The skill changed** for each miss, each change general and settled with the owner:
  - **a precursor reached through a page about its author** taken as a second root (MMR runs 1
    and 2), against the rule 0.2.0 already states;
  - **a credited text not opened** within its retries (Gandhi runs 1 and 3): the wrong volume,
    a dead link, a non-English edition;
  - **two quotes from one page on one line** (non-interactive goldfish run 2);
  - and, its case still passing, **a credited text that only a cold trail credits** drawn as
    differing (echoed goldfish run 3).
- **`0.3.0`** in `plugin.json` and `metadata.version`, and its `CHANGELOG.md` entry.
- **The next cycle,** only at the owner's word, after P4's results are removed.
- **Ask at the start of P4a:** whether to run a cycle, and its ceiling.

**Gates:**
- `uv run scripts/verify.py`, green.
- `uv run evals/provenance-tracer/checks.py` on a new cycle, if the owner runs one.

**Watch for:**
- **The owner does not intend to spend on every session:** a cycle costs about $51.

**Amended at plan time, with the owner (2026-11-27):**
- **A trial before the cycle:** one run each of the four cases the changes target and of
  exercise, the case the roots change most risks, outside the repository at
  `--max-cost-usd 10`; the cycle only if it holds. The owner asked why not re-run only the four
  cases: the changes touch rules every forward case shares, and 1.0.0 needs a cycle on the skill
  as it stands.
- **The owner's review of the release before any spend,** as in P4, so no later review leaves
  the cycle stale.
- **P4's results retired in a commit of their own,** after the trial holds, so 0.2.0's results
  stay in HEAD until the cycle is sure to run.

**The release's review (`/code-review high`, before any spend), 6 findings: 6 fixed and 0
skipped,** the owner choosing to fix all six:
- *another subject* in what speaks to the claim let a study of a different question count;
- *a root beyond the first* left which root is first open, so an earliest instance tied to the
  claim only by a biography could stay root 1;
- the precursor a root names as background had been limited to roots that retellings credit;
- a fetch's *not found* on a text cut short could be read as silence;
- the quote guardrail in `SKILL.md` lacked the *per*, *cited by* and *Root says* exceptions;
- *Decided* said the archive record costs no fetch, where it costs no extra one.

**The trial** (five runs, $7.67 and $0.23 of judging, from `a03e7f1`): both goldfish runs Echo ·
No primary found, exercise Independent · Grounded, MMR Echo · Primary differs · Origin retracted
with Fudenberg a `Background:` bullet, every quote and link clean; Gandhi No primary found, its
one English copy an access-restricted item (403). At the owner's word, the playbook skips such an
item, committed before the cycle without another trial.

**The cycle's first batch, discarded** (12 runs: Gandhi, MMR, private person, several claims;
$9.34 and $0.31 of judging): Gandhi 0/3, each run sent by the catalogue to a mislabelled scan;
at the owner's word the copies' search puts a web search for the passage's words first, and the
cycle starts again on the skill as it then stands. The batch's files are kept outside the
repository; MMR was Echo in 3/3, and two private-person runs did not invoke the skill.

**The cycle restarted on `bf06fdf`:** batch A (Gandhi, MMR, private person, several claims; $9.86
and $0.36 of judging) gave Gandhi 0/3 again, its runs searching the passage's words first and
then reaching the same mislabelled scans. At the owner's word, the misattributed-quote case is
dropped (PT 8 amended by the owner) and its runs set aside outside the repository; the copies'
search stays, decided by the session, so batch A's other nine runs stand and the cycle goes on
with the eight cases not yet run, none run again. Batch B was stopped before it wrote a run.

**The account's window,** said by the owner after the review: the runs fit within the 5-hour
window left (40%), so the cycle runs in batches of cases read against the usage tool.

**Done (2026-11-28, provenance-tracer 0.3.0).**
- **Decided with the owner:**
  - **At the start:** the silent-work rule over a credit-must-travel rule; the copies found by
    their passage and checked, the budget unchanged; an adversarial review of the plan, which
    scoped the roots rule to two or more roots, made silence need a full reading, and added
    exercise to the trial; the spend, a trial then the full cycle. The owner asked why passing
    cases run again: rules every forward case shares changed, and PT 2 needed the skill as it
    stands.
  - **Mid-session:** all six of the release review's findings fixed; runs fitted to the account's
    5-hour window; after the trial, the access-restricted skip; after the first batch, the
    copies' search web-first and the cycle restarted; after batch A, the misattributed-quote case
    dropped (PT 8 amended by the owner), the copies' search kept as it was by the session so no
    run was made again.
  - **The reading:** 9 engine fails overruled to pass, 4 kept, at the owner's word.
  - **After the reading:** PT 2 amended by the owner: this cycle counts for 1.0.0 with its two
    misses named, and no further full cycle runs.
- **Shipped:**
  - `plugins/provenance-tracer/` 0.3.0: `SKILL.md` (231 lines), `labels.md`,
    `search-playbook.md`, `output-template.md`, the version in `plugin.json` and
    `metadata.version`, `CHANGELOG.md`, the README's version line;
  - `misattributed-quote-gandhi` deleted; P4's cycle retired; the third cycle: 36 `run-N.md` and
    `verdicts-N.md`, 12 `review.md`.
- **The commits:** the release (`504be85`), its review (`a03e7f1`), two fixes (`89fb485`,
  `bf06fdf`), the retirement (`5ea77ee`), the dropped case (`5d9abd7`), then the cycle's.
- **The trial** ($7.67 and $0.23 of judging, from `a03e7f1`): both goldfish runs No primary found,
  exercise Independent · Grounded, MMR Echo with Fudenberg a `Background:` bullet, every quote and
  link clean; Gandhi's one copy access-restricted.
- **The cycle** (0.3.0, the skill as of `bf06fdf`, `claude` 2.1.330, `claude-opus-5-5`, judge
  `claude-sonnet-5-5`), in batches within the window: a first batch discarded ($9.65); batch A's
  Gandhi runs set aside ($5.32); a batch stopped before it wrote a run; kept, $46.41 for the runs
  and $1.28 for judging, $47.69. With the trial, P4a spent about $70.56, and the stopped call's
  share is unknown.
- **The owner's reading:** two fresh readers with the cases and runs and no verdicts; they agreed
  with the engine but for nine fails, all overruled.
- **`checks.py` on the cycle:** `checks: 12 case(s), 4 problem(s); pass bars not met: Cases passing
  at 2 of 3 runs (labels and facts), ≤ 1 quote per source, < 15 words`, exit 1.

  | Check | Pass bar | Result | Met |
  |---|---|---|---|
  | Cases passing at 2 of 3 runs (labels and facts) | all cases | 11 / 12 | **no** |
  | No verdict in the report's own voice | all runs | 36 / 36 | yes |
  | Footer lines present | all runs with its grader | 27 / 27 | yes |
  | ≤ 1 quote per source, < 15 words | all runs | 34 / 36 | **no** |
  | Every linked source among the run's fetches | all forward and reverse reports | 30 / 30 | yes |
  | No search issued (private-person case) | all runs with its grader | 3 / 3 | yes |
  | Manager never in a search query (personal-chain case) | all runs with its grader | 3 / 3 | yes |
  | Gold order + approved_by + graders as run | all cases | 12 / 12 | yes |
  | Runs on the skill as it stands | all runs | 36 / 36 | yes |

  Verdicts the owner overruled: 9 of 123.
- **What the results showed:**
  - **Fixed:** MMR 1/3 to 3/3; both goldfish cases 3/3, no credited text drawn; every quote the
    skill wrote clean.
  - **Missed:** exercise 1/3 (runs 2 and 3 opened no copy of either root); the quote bar, in two
    private-person replies written without the skill, which no run of that case invoked.
  - **Dropped:** Gandhi, its 1913 passage opened in none of six runs on 0.3.0.
- **Docs:** `ARCHITECTURE.md` (*Overview*, *Layout*, *The data layer*, *provenance-tracer* Decided
  and Built, the baseline, four *Decision log* lines); PT 2 and PT 8 amended by the owner; the
  plugin's CHANGELOG and README; this block, P5's and the handoff.
- **Amendments:** the trial with a fifth case, the release's review before any spend, and P4's
  results retired in a commit of their own (at plan time); the case dropped and the cycle run in
  batches (mid-session); each with the owner.
- **Checked by hand:** the archive's direct file address (200 where `download` gave 302); every
  run's header `claude` 2.1.330 and its commit's skill folder as `bf06fdf`'s; no `grader threw`;
  hygiene green over the results.
- **Falsified:** nothing new; no check was added.
- **Numbers:** 374 unit tests, 0 skipped, unchanged; 6 `verify` stages; 17 Python files; 3 skill
  folders, 3 plugins, 3 marketplace entries; provenance-tracer's cases 13 to 12; `results/`: 36
  runs, 36 verdicts, 12 reviews.

**The cycle commit's review (`/code-review high`), 5 findings: 5 fixed and 0 skipped,** the owner
choosing to fix all five; none touched the skill folder, so the cycle stays on the skill as it
stands:
- P5's 1.0.0 bullet and Gates still asked for every bar met, against PT 2 as amended;
- the 0.3.0 changelog said passages are found more reliably, and left out the web-first search
  and the access-restricted skip;
- those two rules, which the owner settled, added to *provenance-tracer* Decided and the
  *Decision log*;
- the handoff's Read line no longer says PT 4 was amended;
- *Layout and boundaries* names the results as P4a's cycle.
- **After the review:** `checks.py` prints the same 4 problems and table; the other numbers are
  unchanged.

---

## P5: The release and the round's close

**Read:** `FEATURE-provenance-tracer.md` PT 2, 4, and the spec's *Distribution*;
`FEATURE-eval-engine.md` EE 8; `ARCHITECTURE.md` every section this round's blocks named,
read cold against the code; the last cycle's done-note.

- **1.0.0:** the version fields alone, on P4a's cycle, which PT 2 as the owner amended it counts
  for 1.0.0 with its two misses named; its `CHANGELOG.md` entry; the root README's *(in
  development)* removed.
- **The claude.ai smoke test** (PT 4): the skill zipped as its README says, uploaded on
  claude.ai's Plugins page, three cases each in a fresh chat with web search on (one forward,
  the reverse case, the private-person case), run by the session in the owner's Chrome at the
  owner's word; each reply saved as `claude-ai.md` and judged by the owner in `review.md`; the
  upload deleted once the owner confirms.
- **The plugin's README:** *How it was tested*, with the last cycle's table and the smoke test.
- **`ARCHITECTURE.md` read cold:** every Built part this round touched true; the baseline.
- **The close:** the between-rounds handoff; `docs/BACKLOG.md` gains what is left; after the
  review commit, `docs: close round 2` deletes `docs/spec/`'s files.
- **The tag** `provenance-tracer--v1.0.0`, with `claude plugin tag`, on the owner's yes, after
  any approved push.

**Gates:**
- `uv run scripts/verify.py`, green.
- `uv run evals/provenance-tracer/checks.py`: as the baseline gives it, 4 problems and exit 1,
  only the two misses PT 2 names (cases 11/12, quotes 34/36), every other bar met.
- `uv run evals/crux-finder/checks.py`: every bar met, the smoke test's row 3 / 3.

**Amended in Session P4a, by the owner (PT 2):** the last cycle is P4a's, on 0.3.0, counted for
1.0.0 with its two misses named; no further full cycle runs, so 1.0.0 is the version fields
alone on that cycle. The 1.0.0 bullet and the Gates above read so.

**Watch for:**
- **A skill uploaded to claude.ai syncs into every Claude Code session** (`CLAUDE.md`): the
  runner must refuse while it loads; delete the upload afterwards unless the owner keeps it.
- **A 1.0.0 that changes more than its version lines** leaves the last cycle no longer on the
  skill as it stands.

**Done (2026-11-28, provenance-tracer 1.0.0).**
- **Decided with the owner:**
  - **The smoke test dropped** at the owner's word (PT 4 amended by the owner); the
    `checks.py` support for claude.ai replies built for it was reverted unused.
  - **After the cold read,** three Decided parts the code already followed: a plugin README may
    say in prose where its cases are kept (*Layout and boundaries*); one line after a saved
    report says where it was saved; the silent-work rule drops *subject*, as the owner's review
    of 0.3.0 had it (*provenance-tracer*).
  - **The spend:** none; the account's window was read before any run.
- **Shipped:**
  - `plugins/provenance-tracer/` 1.0.0: the version in `plugin.json` and `metadata.version`
    alone, so the third cycle stays on the skill as it stands; `CHANGELOG.md`'s 1.0.0 entry,
    linked to its tag; the README's *How it was tested*, with the third cycle's table and its two
    misses named, and its version line.
  - The root README no longer marks provenance-tracer in development; `CLAUDE.md` names both
    READMEs that hold eval results.
- **Amendments:** none beyond the drop above.
- **Revised** (`ARCHITECTURE.md`, read cold by three fresh readers, each finding checked against
  the code): the tests list and the by-path imports; the data layer's grader counts (five
  labelled, nine with a footer), a claude.ai reply's `commit` held to gold order, which header
  values may hold a line break, and which review values are lower case; folder discovery;
  provenance-tracer's `SKILL.md` lines (231), 0.2.0's examples and 0.3.0's precursor rule; the
  eval harness's checks list, results entries, reply kinds, the runner's history and its
  unguarded total cost; *Testing strategy*'s provenance-tracer cycles; *Packaging*'s install
  line; the CLI versions of P4 to P5; the baseline's date; and the intro's round 2 spec files,
  as closed.
- **Checked by hand:** `checks.py` for both skills after the bump, unchanged.
- **Falsified:** nothing new is kept; no check was added.
- **Numbers:** 374 unit tests, 0 skipped, unchanged; 6 `verify` stages; 17 Python files; 3 skill
  folders, 3 plugins, 3 marketplace entries; provenance-tracer's `checks.py` 4 problems, exit 1,
  as the baseline gives it.
- **Backlog:** the private-person case's trigger, the 1978 paper on the live web, a
  misattributed-quote case, and the runner's write of a run whose judges were refused, moved to
  *Deferred*.
