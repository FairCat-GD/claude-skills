Read docs/spec/FEATURE-provenance-tracer.md PT 2, 5, 8; docs/ARCHITECTURE.md *provenance-tracer*
and *The eval harness*; P3's done-note; then CLAUDE.md, *The session cycle* in
docs/DEVELOPMENT-WORKFLOW.md, docs/ARCHITECTURE.md's overview, invariants and baseline,
docs/spec/SESSIONS.md's header, your block and P3's done-note, then this file, and do Session P4:
the changes P3's cycle calls for, release 0.2.0. P4 covers:
- the skill changed for each bar P3's cycle missed, each change general, settled with the owner
  (done: 0.2.0 is committed, below);
- `0.2.0` in `plugin.json` and `metadata.version`, and its `CHANGELOG.md` entry (done);
- the next cycle on the skill as it stands, after P3's results are removed (not yet run).

## State you need that is not in the specs

- **P4 is under way; this handoff records where it stands until its last commit rewrites it.**
  - **Committed** (local, not pushed): the 0.2.0 release (`feat: provenance-tracer 0.2.0, …`)
    and its review's fixes (`review: …`), then the trial's fix (`fix: …`: Grounding on a study's
    own data, one quote per row of *How it changed*). The skill's changes, the ten-percent gold's change and
    the owner's decisions are in `docs/ARCHITECTURE.md` (*provenance-tracer*, Decided and Built;
    the *Decision log*). P3's results are retired: `checks.py` prints `no results yet`.
  - **Settled with the owner:** the trial, 5 single runs with `--max-cost-usd 10` on
    `misattributed-quote-gandhi`, `popular-myth-ten-percent-brain`,
    `retracted-origin-mmr-autism`, `well-sourced-exercise-heart-disease` and
    `echoed-statistic-goldfish-attention`, into a folder outside the repository; then the cycle,
    `--max-cost-usd 75`. The owner intends this cycle to be the last: if a bar still misses,
    nothing more runs without the owner's word.
  - **The trial** (5 runs, $6.74): Gandhi, ten-percent, MMR and goldfish passed every grader with
    clean quotes; exercise had Independent right but Primary differs for Grounded, and three
    quotes on one row, which the fix answers; one more exercise run checks it.
  - **Left:** the exercise re-check; the cycle; the owner's reading as in P3; `checks.py`'s
    table; the docs, P4's done-note (with the release review's seven findings, all fixed) and
    this handoff; the cycle's commit; its review.
  - **Amendments to the block:** two commits, since the runner refuses an uncommitted plugin;
    the owner's review of the release before any spend; the trial.
- **Round 2 is provenance-tracer, and one eval engine for every skill:** P1, E1, E2, E3, P2 and
  P3 are done; P4 is under way and P5 remains.
- **Push status:** `origin/main` holds everything through P3's review commit ("review: a bold
  label keeps the chain open, the user's text is a claim, and 5 smaller"), pushed with the
  owner's yes. P4's commits are local.
- **What P3 left** (its results now retired, in git as of `c82907f`):
  - **`evals/provenance-tracer/checks.py`** on the cycle: `checks: 13 case(s), 59 problem(s);
    pass bars not met: Cases passing at 2 of 3 runs (labels and facts), ≤ 1 quote per source,
    < 15 words`, exit 1. Cases 9/13; quotes 14/39; every other bar met.
  - **The four cases that miss, with the owner's notes in each `review.md`:**
    - Gandhi (labels 0/3): the 1913 passage did not open, so No primary found; one run made it
      a second root.
    - Ten-percent (labels 0/3): James's essay taken as a Primary that differs; gold says No
      primary found. The owner chose the gold: it is now Primary differs.
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
  - **Skipped runs:** it skips a run whose file exists; P3's results are already removed.
- **Baseline** (ARCHITECTURE's table):
  - `verify` green, 6 stages;
  - 374 unit tests passed, 0 skipped;
  - 17 Python files;
  - 3 skill folders, 3 plugins, 3 marketplace entries;
  - `claude` 2.1.330;
  - crux-finder's `checks.py`: `checks: 10 case(s), 0 problem(s); every pass bar met`;
  - provenance-tracer's `checks.py`: `no results yet`, exit 0, until the cycle runs.
- **Not done:** the runner writes a run whose `llm` judges a usage limit refused, as graded
  fails (`docs/BACKLOG.md`).

## Watch for

- **The Ask at the start of P4:** answered (above): $10 for the trial, $75 for the cycle.
- **A change fitted to one case** is not general: each change names the rule it serves.
- **`SKILL.md` stays under 300 lines:** move detail to the references.
- **A usage limit mid-cycle:** check every `verdicts-N.md` for `grader threw` before the
  reading.
- **A cycle spends real model runs and the live web:** one cycle at a time, never in a parallel
  part.
