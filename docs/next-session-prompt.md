Read `SPEC.md` decisions 21, 22, 23; `PDD.md` B, *Runner*, *claude.ai smoke test*, *Review*,
*Deterministic checks*, *Pass bars*; `ARCHITECTURE.md` *crux-finder*, *The eval harness*; the
done-notes of Sessions 5 and 6. Then CLAUDE.md, *The session cycle* in
docs/DEVELOPMENT-WORKFLOW.md, docs/ARCHITECTURE.md's overview, invariants and baseline,
docs/spec/SESSIONS.md's header, your block and the previous block's done-note, then this file,
and do Session 7: one eval cycle, then the claude.ai smoke test once the bars are met. 7 covers:
- `run.py --runs 2` over the ten cases, `checks.py`, the owner's review of every run into
  `review.md`, and the summary table against the pass bars;
- a bar missed: the skill changed for what the reviews show, crux-finder 0.2.0, the results
  recorded, and 7a inserted with the owner;
- every bar met on the skill as it stands: the claude.ai smoke test on three cases.

Release 0.2.0 only when the cycle changes the skill.

## State you need that is not in the specs

- **Round 1 is a home for many skills**: Sessions 0–6 are done; Sessions 7–8 remain.
- **Push status.** `origin/main` holds everything through Session 6: its commit, its `review:`
  commit and the docs commit that corrects this note, each pushed with the owner's yes.
- **What Session 6 left that Session 7 builds on:**
  - **Ten cases** in `evals/crux-finder/cases/`, each `input.md` and an owner-approved `gold.md`,
    committed together, before any result: `definitional-vintage-rail`,
    `empirical-orchard-stall`, `empirical-studio-kiln`, `framing-piano-lessons`,
    `no-conflict-quiz-team`, `one-sided-games-night`, `predictive-hall-solar`,
    `real-lincoln-douglas`, `transcript-father-care`, `value-theatre-season` (`run.py`'s
    order). The ids are now permanent once results exist.
  - **Each gold.md's note,** below the frontmatter, is for the owner's review: what else counts
    as a match, and what does not. Show it to the owner beside each run.
  - **How two cases count** (*The data layer*, Decided): `one-sided-games-night`, a run that asks
    for B's own words and writes no report matches on crux and type, and records
    `gate_fired: yes`; a report counts as the gate firing only if it labels B "reconstructed by
    A". `no-conflict-quiz-team`, only a **No crux** report matches; a Framing crux records
    `no_conflict_reported: yes` but `crux_match: no`. `checks.py` wants `gate_fired` and
    `no_conflict_reported` on every output of a case or none, so record each on all of that
    case's outputs.
  - **`uv run evals/crux-finder/checks.py`** prints `checks: 10 case(s), 0 problem(s); no results
    yet, so the pass bars are not counted` and exits 0.
- **The smoke test's three cases** (PDD B: one Empirical, the one-sided, the no-conflict):
  `empirical-orchard-stall` or `empirical-studio-kiln` (`real-lincoln-douglas` is Empirical too,
  but long), `one-sided-games-night`, `no-conflict-quiz-team`. Choose with the owner.
- **What the spec said that turned out wrong or harder:**
  - **The real set holds one case:** the owner had no dispute of their own, so a fictional
    transcript, `transcript-father-care`, took the second real case's place
    (`docs/BACKLOG.md`).
  - **The report's 400 words** are still not met by any run so far: 472 in Session 5's one real
    run, 486 to 564 in Session 4's. `real-lincoln-douglas` is the longest input (about 1,350
    words), so expect its reports to strain the length bar most.
- **Decisions written down nowhere else:**
  - The two cases most likely to miss on type: `framing-piano-lessons` (a run may call it
    Value) and `real-lincoln-douglas` (a run may make the Predictive "can the Union endure"
    point primary, which its gold counts as no).
  - The owner deleted crux-finder's claude.ai upload in Session 5. The smoke test uploads the zip
    again; it then syncs into Claude Code as `anthropic-skills:crux-finder`, and `run.py`
    refuses runs while it loads, so run the cycle first and the smoke test after, and delete the
    upload when done unless the owner keeps it.
- **Baseline** (ARCHITECTURE's table): `verify` green with 6 stages, about 25 s; 203 unit tests
  passed, 0 skipped; `hygiene --all` green; 13 Python files; 2 skill folders, 2 plugins, 2
  marketplace entries; `claude` 2.1.329; `checks.py` 10 cases, 0 problems, no results.
- **Not done:** installing from GitHub, for both skills, is not yet checked by a person
  (`docs/BACKLOG.md`).

## Watch for

- **The owner records every judgement in `review.md`.** The session never fills `crux_match`,
  `type_match` or `people_statement` itself.
- **A gold.md is never edited once results exist:** `checks.py` fails the gold order. A gold
  that turns out wrong is the owner's call, and the case's results start over.
- **The real excerpt holds the era's racial terms,** and reports quote it verbatim into
  committed results; that was known and accepted when the case was chosen.
- **Twenty real runs:** the eval runner is the exclusive resource, run one at a time; the cost
  is the owner's. Record `claude`'s version, since it is not pinned.
