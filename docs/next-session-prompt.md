Read docs/spec/FEATURE-provenance-tracer.md PT 2, 4 and 8 (each with the owner's amendment of
2026-11-28) and the spec's *Distribution*; docs/spec/FEATURE-eval-engine.md EE 8;
docs/ARCHITECTURE.md every section this round's blocks named, read cold against the code; P4a's
done-note; then CLAUDE.md, *The session cycle* in docs/DEVELOPMENT-WORKFLOW.md,
docs/ARCHITECTURE.md's overview, invariants and baseline, docs/spec/SESSIONS.md's header, your
block and P4a's done-note, then this file, and do Session P5: the release and the round's close,
release 1.0.0.

## State you need that is not in the specs

- **Round 2 is provenance-tracer, and one eval engine for every skill:** P1, E1, E2, E3, P2, P3,
  P4 and P4a are done; P5 closes the round.
- **Push status:** `origin/main` holds everything through P4's last review commit ("review: a
  goldfish overrule decided again from its fact's full text, …"). Nothing of P4a is pushed;
  `git log origin/main..HEAD` lists its commits.
- **The last cycle is P4a's,** on 0.3.0 (the skill as of `bf06fdf`), twelve cases: `checks.py`
  gives 4 problems and two bars missed, cases 11/12 (exercise) and quotes 34/36 (private-person
  replies written without the skill). PT 2, as the owner amended it, counts this cycle for 1.0.0
  with those two misses named; no further full cycle runs. So 1.0.0 is the version fields alone,
  and `checks.py` stays at exit 1 with those problems.
- **The private-person case did not invoke the skill** in any run of P4a's cycle, where P4's all
  did, with the description unchanged since P1. The claude.ai smoke test includes that case.
- **The owner's account has a 5-hour usage window;** the owner asked that runs fit within it.
  Read it with the app's usage tool before any run.
- **Baseline** (ARCHITECTURE's table):
  - `verify` green, 6 stages;
  - 374 unit tests passed, 0 skipped;
  - 17 Python files;
  - 3 skill folders, 3 plugins, 3 marketplace entries;
  - `claude` 2.1.330;
  - provenance-tracer's `checks.py`: `checks: 12 case(s), 4 problem(s); pass bars not met: Cases
    passing at 2 of 3 runs (labels and facts), ≤ 1 quote per source, < 15 words`, exit 1;
  - crux-finder's `checks.py`: `checks: 10 case(s), 0 problem(s); every pass bar met`.
- **For the backlog at the close:** the private-person trigger; exercise's 1978 paper on the live
  web; the dropped misattributed-quote case; and, still open, the runner writing a run whose
  `llm` judges a usage limit refused as graded fails.

## Watch for

- **A 1.0.0 that changes more than its version lines** leaves P4a's cycle no longer on the skill
  as it stands.
- **A skill uploaded to claude.ai syncs into every Claude Code session:** delete the upload after
  the smoke test unless the owner keeps it.
- **The README's *How it was tested*** gives P4a's table with its two misses named, as PT 2 now
  reads.
