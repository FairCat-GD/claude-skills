Read docs/spec/FEATURE-provenance-tracer.md PT 2, 5, 8; docs/ARCHITECTURE.md *provenance-tracer*
and *The eval harness*; P4's done-note and each case's `review.md`; then CLAUDE.md, *The session
cycle* in docs/DEVELOPMENT-WORKFLOW.md, docs/ARCHITECTURE.md's overview, invariants and baseline,
docs/spec/SESSIONS.md's header, your block and P4's done-note, then this file, and do Session
P4a: the changes P4's cycle calls for, release 0.3.0. P4a covers:
- the skill changed for each miss P4's cycle left, each change general, settled with the owner;
- `0.3.0` in `plugin.json` and `metadata.version`, and its `CHANGELOG.md` entry;
- a cycle only at the owner's word, after P4's results are removed.

## State you need that is not in the specs

- **Round 2 is provenance-tracer, and one eval engine for every skill:** P1, E1, E2, E3, P2, P3
  and P4 are done; P4a (inserted in P4) and P5 remain.
- **Push status:** `origin/main` holds everything through P3's review commit. P4's commits are
  local and unpushed: the 0.2.0 release, its review, two fixes from the trial, and the cycle's
  commit with its review. A push makes 0.2.0 installable; it needs the owner's yes.
- **The owner does not intend to spend on every session.** P4 spent $58.94 (the trial $7.94,
  the cycle $51.00). P4a asks at its start whether to run a cycle at all, and its ceiling.
- **What P4 left:**
  - **`evals/provenance-tracer/checks.py`** on P4's cycle: `checks: 13 case(s), 2 problem(s);
    pass bars not met: Cases passing at 2 of 3 runs (labels and facts), ≤ 1 quote per source,
    < 15 words`, exit 1. Cases 11/13, quotes 38/39; every other bar met.
  - **The misses, with the owner's notes in each `review.md`:**
    - Gandhi (labels 1/3): the 1913 passage not opened in runs 1 and 3 (a scan of the wrong
      volume, a dead link, a non-English edition), so No primary found.
    - MMR (labels 1/3): runs 1 and 2 counted Fudenberg 1996 as root 2, reached through
      Wikipedia's page about him, though 0.2.0's precursor rule says such a page does not make a
      retelling.
    - Quotes: non-interactive goldfish run 2 quoted Microsoft's report twice on one line.
    - Seen, its case passing: echoed goldfish run 3 drew a study that only a cold trail credits
      as a credited text that differs, so Primary differs.
- **The runner and the engine:**
  - **The ceiling:** `--max-cost-usd` is required and covers the whole command.
  - **The refusal:** the runner refuses while `plugins/provenance-tracer/` or
    `evals/provenance-tracer/cases/` has uncommitted changes, so a release is committed before
    any run, and nothing in the plugin folder is edited while a call is pending.
  - **The account's usage limit** refused 21 runs of P4's first call; the second call ran them,
    since the runner skips a run whose file exists.
- **Baseline** (ARCHITECTURE's table):
  - `verify` green, 6 stages;
  - 374 unit tests passed, 0 skipped;
  - 17 Python files;
  - 3 skill folders, 3 plugins, 3 marketplace entries;
  - `claude` 2.1.330;
  - crux-finder's `checks.py`: `checks: 10 case(s), 0 problem(s); every pass bar met`.
- **Not done:** the runner writes a run whose `llm` judges a usage limit refused, as graded
  fails (`docs/BACKLOG.md`).

## Watch for

- **The Ask at the start of P4a:** whether to run a cycle, and if so its ceiling (P4's cost
  about $1.26 a run, $51.00 a cycle with judging).
- **A change fitted to one case** is not general: each change names the rule it serves.
- **`SKILL.md` stays under 300 lines** (219 now): move detail to the references.
- **A usage limit mid-cycle:** check every `verdicts-N.md` for `grader threw` before the
  reading.
- **A cycle spends real model runs and the live web:** one cycle at a time, never in a parallel
  part.
