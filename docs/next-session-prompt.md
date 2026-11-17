Read `SPEC.md` decisions 5, 6, 12, 13, 14, 26–29; `REVIEW-2026-11-17.md` F1;
`ARCHITECTURE.md` invariant 9, *Stack and pins*, *Layout and boundaries*, *verify*, *The
hygiene stage*, *Testing strategy*; `DEVELOPMENT-WORKFLOW.md` *Day one* and *A clean
repository*; the port's source in the owner's public repository `FairCat-GD/krita-art-mcp`,
checked out at `~/Documents/GitHub Projects/krita-art-mcp`: `scripts/hygiene.py`,
`tests/test_hygiene.py`, and `scripts/verify.py` for its shape only. Then CLAUDE.md, *The
session cycle* in docs/DEVELOPMENT-WORKFLOW.md, docs/ARCHITECTURE.md's overview, invariants and
baseline, docs/spec/SESSIONS.md's header and your block, then this file, and do Session 1: the
scaffold. 1 covers:
- the toolchain: `pyproject.toml`, `uv.lock`, `.python-version`;
- `verify` with the stages `format`, `lint`, `tests` and `hygiene`;
- the hygiene stage: the ported part, and the rest of the kit's design;
- the itinerary skill's seven example lines replaced (F1), with the owner's approval.

No release: the skill's change is released as 1.0.1 by Session 2 (`SPEC.md` decision 18).

## State you need that is not in the specs

- **Round 1 is a home for many skills**: Session 0 (the intake) is done; Sessions 1–8 remain.
- **Session 0's commit and its review commit are pushed.** `origin/main` holds everything
  through the review commit, `review: rules that contradicted Session 1's scope, …`; no local
  commit waits for a push. The push published documents only: nothing new is installable.
- **What exists:** the docs Session 0 wrote, `CLAUDE.md`, `.gitignore`, the licence, the README
  as first published, and the skill at `travel-itinerary-builder/` at the root. No script, no
  `pyproject.toml`, no test.
- **What the source of the port is, measured at intake:** 239 lines in `scripts/hygiene.py`,
  standard library only, running on Python 3.10; `tests/test_hygiene.py` is pytest. It checks
  terms and attribution only (see the block). Its `scripts/verify.py` imports `tomllib`.
- **F1 is one word on 7 lines,** listed by file and line in `REVIEW-2026-11-17.md`. The same word
  is in the three pushed commits, so the first full scan ends with a count of hits in pushed
  history; that is expected, and the done-note records the count.
- **Decisions written down nowhere else:**
  - Session 0's plan had one adversarial review, on the strongest model; what it changed is in
    Session 0's commit message, and what it rejected is in `docs/BACKLOG.md`'s *Decided
    against*.
  - The workflow file was copied from the kit at `02fb1d99f56ff414ec88cf7b1789328933e355d0`.
  - The owner's attribution settings were confirmed off at intake.
- **Baseline:** none yet; Session 1 writes the first, from its first green `verify`.
- **Not done:** nothing is built; every Built part of `ARCHITECTURE.md` says "Not yet".

## Watch for

- **This machine's own `python3` is 3.9.** Use `uv run`; uv has 3.10 and 3.12 installed.
- **Never print the F1 word.** Name its places by file and line, in chat and in the done-note.
- **Propose the replacement city before writing anything,** each of the seven lines in the
  skill's voice, checked against the term list first.
