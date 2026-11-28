No round is in progress. Read CLAUDE.md, *The session cycle* in docs/DEVELOPMENT-WORKFLOW.md,
docs/ARCHITECTURE.md's overview, invariants and baseline, then this file; then the sections of
docs/ARCHITECTURE.md the request touches, and any a block will point at. The next session is
an **intake**: write the user's request down verbatim, ask what it leaves open,
and plan the round in `docs/spec/`, a Read line in every block (see
`docs/DEVELOPMENT-WORKFLOW.md`, *Rounds*).

## State you need that is not in the docs

- **provenance-tracer 1.0.0 is released.** Round 2 (provenance-tracer, and one eval engine for
  every skill: P1, E1, E2, E3, P2, P3, P4, P4a, P5) is closed. Its spec files are deleted; the
  last done-note is in `docs/spec/SESSIONS.md` as of the review commit before the close
  (`a6b85f2`).
- **Push status:** `origin/main` holds everything through the close commit ("docs: close round
  2"), pushed with the owner's yes, so provenance-tracer 1.0.0 is installable. The tag
  `provenance-tracer--v1.0.0` is not made; it waits for the owner's yes after the push.
- **Open items live in `docs/BACKLOG.md`**, including what this round added there:
  provenance-tracer's private-person case no longer starting the skill, the 1978 paper on the
  live web, a misattributed-quote case, and the runner writing a run whose judges were refused.
- **Baseline** (ARCHITECTURE's table): `verify` green, 6 stages; 374 unit tests, 0 skipped; 17
  Python files; 3 skill folders, 3 plugins, 3 marketplace entries; `claude` 2.1.330;
  provenance-tracer's `checks.py` 4 problems and exit 1, the two misses its 1.0.0 counts;
  crux-finder's `checks.py` every bar met.

## Watch for

- **provenance-tracer's `checks.py` exits 1 by design.** PT 2, as the owner amended it, counted
  a cycle with two misses for 1.0.0, so a later session that sees exit 1 should compare its
  output with the baseline rather than fix it.
