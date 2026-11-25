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
  - `CLAUDE.md`: the skill's name beside the others; invariant 4 as `ARCHITECTURE.md` now
    states it.
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

---

## E2: crux-finder's cases on the new engine

**Read:** `FEATURE-eval-engine.md` EE 3, 5–8; `ARCHITECTURE.md` invariants 6 and 7, *The data
layer*, *The eval harness*, *crux-finder* (Decided), *Known debt*; E1's done-note;
`evals/crux-finder/cases/` (each `input.md` and `gold.md`, its note included),
`evals/crux-finder/checks.py`, `tests/test_crux_finder_checks.py`.

- **The ten cases** (EE 7): for each, a `prompt.md` holding the input's body unchanged, with
  the frontmatter E1 measured to be needed (`allowed_tools`, the no-reply line); and graders
  drawn from its `gold.md` and its note: crux, type and *no statement about people*, plus the
  gate and no-conflict rules where gold has them. The session drafts each grader; the owner
  approves every one before it is committed.
- **The golds:** unchanged, except `real-lincoln-douglas/gold.md`, which gains the `source:`
  and `license:` lines of its `input.md`. That case has no claude.ai reply, and its old results
  go in this commit, so its gold precedes every result it will have.
- **The new checks** (EE 3–8), in `evals/crux-finder/checks.py`, rewritten on the shared code E1
  left: gold's fields and `approved_by`; the gold order, and graders unchanged since each run's
  commit; the pass bars from the verdicts and the owner's corrections; quotes, symmetry and
  length from each `run-N.md`; stability from the owner's record; the claude.ai rows from
  `claude-ai.md` and its `review.md`; *Runs on the skill as it stands*. Its tests rewritten
  with it.
- **Retired in this commit,** so no checks ever read results they were not written for:
  `evals/crux-finder/run.py` and its tests; each `input.md`; every `run-N.md` and `review.md`
  of round 1's cycle, kept in git. The three `claude-ai.md` replies and their `review.md` stay
  (EE 7, 8). `checks.py` then reports no cycle yet.
- **Amended at intake, while writing this plan:** the approved plan retired the old harness in
  E3, with the new results. Moving the real case's `source:` and `license:` into its gold
  needs the old results gone before that gold changes, or the gold order fails; so the old
  results, and the checks that read them, go here.
- **Docs.**
  - crux-finder's README: *How it was tested* keeps the fourth cycle's table, and says the
    reports and reviews are in the repository's history; E3 replaces it.
  - `CLAUDE.md`: *Commands* (the old runner's line removed, `checks.py`'s line as it now is);
    invariants 6 and 7 as `ARCHITECTURE.md` now states them.
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
  including a gold changed after its results, a grader changed after a run's commit, a
  correction counted over a verdict, and a quote not in the prompt.
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

**Gates:**
- `uv run scripts/verify.py`, green.
- `uv run evals/provenance-tracer/checks.py` on the new cycle; a bar still missed opens an
  inserted P4a, with the owner.

**Watch for:**
- **`SKILL.md` stays under 300 lines** as rules are added: move detail to the references.

---

## P5: The release and the round's close

**Read:** `FEATURE-provenance-tracer.md` PT 2, 4, and the spec's *Distribution*;
`FEATURE-eval-engine.md` EE 8; `ARCHITECTURE.md` every section this round's blocks named,
read cold against the code; the last cycle's done-note.

- **1.0.0:** the version fields alone, once the last cycle met every bar on the skill as it
  stands; its `CHANGELOG.md` entry; the root README's *(in development)* removed.
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
- `uv run evals/provenance-tracer/checks.py` and `uv run evals/crux-finder/checks.py`: every
  bar met, the smoke test's row 3 / 3.

**Watch for:**
- **A skill uploaded to claude.ai syncs into every Claude Code session** (`CLAUDE.md`): the
  runner must refuse while it loads; delete the upload afterwards unless the owner keeps it.
- **A 1.0.0 that changes more than its version lines** leaves the last cycle no longer on the
  skill as it stands.
