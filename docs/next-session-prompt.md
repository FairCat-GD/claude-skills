Read docs/spec/FEATURE-provenance-tracer.md PT 2, 5, 8; docs/ARCHITECTURE.md *provenance-tracer*
and *The eval harness*; P4's done-note and each case's `review.md`; then CLAUDE.md, *The session
cycle* in docs/DEVELOPMENT-WORKFLOW.md, docs/ARCHITECTURE.md's overview, invariants and baseline,
docs/spec/SESSIONS.md's header, your block and P4's done-note, then this file, and finish Session
P4a: the changes P4's cycle calls for, release 0.3.0. P4a is in progress: the release and its
review are committed, and what is left is:
- P4's results are retired (their own commit); the full cycle, the round's last, runs in batches
  that fit the 5-hour window, continued after each reset (the trial is done, a first batch was
  discarded with a fix to the copies' search, and the misattributed-quote case was then dropped
  at the owner's word, so twelve cases remain; P4a's block);
- the owner's reading, `checks.py`, the done-note, this handoff for P5 (or an inserted P4b), the
  cycle commit and its review.

## State you need that is not in the specs

- **Round 2 is provenance-tracer, and one eval engine for every skill:** P1, E1, E2, E3, P2, P3
  and P4 are done; P4a (inserted in P4) is in progress, and P5 remains.
- **Push status:** `origin/main` holds everything through P4's last review commit ("review: a
  goldfish overrule decided again from its fact's full text, …"), pushed with the owner's yes, so
  0.2.0 is installable. Nothing of P4a is pushed.
- **Settled at P4a's start, with the owner** (in *provenance-tracer* Decided and P4a's
  amendments): the four changes; the trial, one run each of Gandhi, MMR, both goldfish cases and
  exercise, `--trial` in the scratchpad, `--max-cost-usd 10`; if it holds, the full cycle at
  `--max-cost-usd 75`. A trial miss goes to the owner before anything else is spent.
- **The trial holds** when each run meets gold's labels where it has them and its facts, keeps
  the quote rule as `checks.py` reads it, and neither goldfish run draws a silent work as a
  credited text.
- **The runner and the engine:**
  - **The ceiling:** `--max-cost-usd` is required and covers the whole command; after a usage
    limit, run the same command with what is left of the ceiling.
  - **The refusal:** the runner refuses while `plugins/provenance-tracer/` or
    `evals/provenance-tracer/cases/` has uncommitted changes, so nothing in the plugin folder is
    edited while a call is pending, and the cycle's `review:` commit touches nothing in the skill
    folder.
- **Baseline** (ARCHITECTURE's table):
  - `verify` green, 6 stages;
  - 374 unit tests passed, 0 skipped;
  - 17 Python files;
  - 3 skill folders, 3 plugins, 3 marketplace entries;
  - `claude` 2.1.330;
  - provenance-tracer's `checks.py`: twelve cases; no results yet, 0 problems, exit 0, until
    the third cycle.
- **Not done:** the runner writes a run whose `llm` judges a usage limit refused, as graded
  fails (`docs/BACKLOG.md`).

## Watch for

- **The account's 5-hour window:** the owner asked that runs fit within the window left. Read
  it with the app's usage tool before each runner call, and run the cycle in batches of cases
  (`--case`) that fit, never into a limit, since a judge a limit refuses is written as a graded
  fail (`docs/BACKLOG.md`).
- **A usage limit mid-cycle:** check every `verdicts-N.md` for `grader threw` before the
  reading.
- **A cycle spends real model runs and the live web:** one cycle at a time, never in a parallel
  part.
- **`SKILL.md` stays under 300 lines** (229 now).
