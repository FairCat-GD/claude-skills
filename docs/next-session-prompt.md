Read docs/spec/FEATURE-provenance-tracer.md PT 2, 5, 8; docs/ARCHITECTURE.md *provenance-tracer*
and *The eval harness*; P3's done-note; then CLAUDE.md, *The session cycle* in
docs/DEVELOPMENT-WORKFLOW.md, docs/ARCHITECTURE.md's overview, invariants and baseline,
docs/spec/SESSIONS.md's header, your block and P3's done-note, then this file, and do Session P4:
the changes P3's cycle calls for, release 0.2.0. P4 covers:
- the skill changed for each bar P3's cycle missed, each change general, settled with the owner;
- `0.2.0` in `plugin.json` and `metadata.version`, and its `CHANGELOG.md` entry;
- the next cycle on the skill as it stands, after P3's results are removed.

## State you need that is not in the specs

- **Round 2 is provenance-tracer, and one eval engine for every skill:** P1, E1, E2, E3, P2 and
  P3 are done; P4 and P5 remain.
- **Push status:** `origin/main` holds everything through P2's review commit; P3's commits are
  local until the owner approves a push.
- **What P3 left:**
  - **`evals/provenance-tracer/checks.py`** on the cycle: `checks: 13 case(s), 59 problem(s);
    pass bars not met: Cases passing at 2 of 3 runs (labels and facts), ≤ 1 quote per source,
    < 15 words`, exit 1. Cases 9/13; quotes 14/39; every other bar met.
  - **The four cases that miss, with the owner's notes in each `review.md`:**
    - Gandhi (labels 0/3): the 1913 passage did not open, so No primary found; one run made it
      a second root.
    - Ten-percent (labels 0/3): James's essay taken as a Primary that differs; gold says No
      primary found, which the spec's tier definition may not support. Gold or skill is the
      owner's call; a gold change starts that case over.
    - MMR (1/3): Fudenberg 1996, not opened, taken as the root; the owner judged it wrong.
    - Exercise (1/3): Morris 1953 alone, not opened, in two runs.
  - **The quote rule,** kept strict by the owner mid-session: 25 runs quote one source twice,
    often a phrase and a cited word or year. The skill's own text already says one quote per
    source.
  - **The shared reckoning** in `evals/shared.py`, which both skills' checks call.
- **The runner and the engine:**
  - **The ceiling:** `--max-cost-usd` is required. P3's 39 runs cost $46.71, judging included,
    plus $2.88 for two runs removed.
  - **The refusal:** the runner refuses while `plugins/provenance-tracer/` or
    `evals/provenance-tracer/cases/` has uncommitted changes.
  - **Skipped runs:** it skips a run whose file exists, so the next cycle starts by removing
    P3's results.
- **Baseline** (ARCHITECTURE's table):
  - `verify` green, 6 stages;
  - 367 unit tests passed, 0 skipped;
  - 17 Python files;
  - 3 skill folders, 3 plugins, 3 marketplace entries;
  - `claude` 2.1.330;
  - crux-finder's `checks.py`: `checks: 10 case(s), 0 problem(s); every pass bar met`.
- **Not done:** the runner writes a run whose `llm` judges a usage limit refused, as graded
  fails (`docs/BACKLOG.md`).

## Watch for

- **The Ask at the start of P4:** the next cycle's ceiling, `--max-cost-usd`, from P3's cost per
  run (about $1.20 a tracing run).
- **A change fitted to one case** is not general: each change names the rule it serves.
- **`SKILL.md` stays under 300 lines:** move detail to the references.
- **A usage limit mid-cycle:** check every `verdicts-N.md` for `grader threw` before the
  reading.
- **A cycle spends real model runs and the live web:** one cycle at a time, never in a parallel
  part.
