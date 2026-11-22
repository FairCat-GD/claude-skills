Read `SPEC.md` decisions 21, 22, 23; `PDD.md` B, *Runner*, *claude.ai smoke test*, *Review*,
*Deterministic checks*, *Pass bars*; `ARCHITECTURE.md` *crux-finder*, *The data layer*, *The
eval harness*; the done-notes of Sessions 6 and 7. Then CLAUDE.md, *The session cycle* in
docs/DEVELOPMENT-WORKFLOW.md, docs/ARCHITECTURE.md's overview, invariants and baseline,
docs/spec/SESSIONS.md's header, your block and the previous block's done-note, then this file,
and do Session 7a: the second eval cycle, on crux-finder 0.2.0, then the claude.ai smoke test
once the bars are met. 7a covers:
- Session 7's result files removed, then `run.py --runs 2` over the ten cases, `checks.py`, the
  owner's review of every run into `review.md`, and the summary table against the pass bars;
- a bar missed: the skill changed for what the reviews show, crux-finder 0.3.0, the results
  recorded, and 7b inserted with the owner;
- every bar met on the skill as it stands: the claude.ai smoke test on `empirical-studio-kiln`,
  `one-sided-games-night` and `no-conflict-quiz-team`.

Release 0.3.0 only when the cycle changes the skill.

## State you need that is not in the specs

- **Round 1 is a home for many skills**: Sessions 0–7 are done; 7a, inserted in Session 7, and 8
  remain.
- **Push status.** `origin/main` holds everything through Session 7: its commit and its
  `review:` commit, pushed with the owner's yes, so crux-finder 0.2.0 is installable.
- **What Session 7 left that 7a builds on:**
  - **Session 7's results** in `evals/crux-finder/results/<id>/`: `run-1.md`, `run-2.md` and
    `review.md` for each case, run on 0.1.0 at commit `a04f10d`. A new cycle replaces them
    (decided at the start of 7): remove all three files of every case before running, since
    `run.py` skips a run file that exists and `checks.py` wants a `review.md` section for every
    output. Git keeps them.
  - **`uv run evals/crux-finder/checks.py`** prints 21 problems (the old cycle's length and quote
    misses) and `pass bars not met: Type matches gold, Quotes verbatim, Length ≤ 400 words, Runs
    on the skill as it stands (decision 22)`, exit 1, until the old results are removed.
  - **crux-finder 0.2.0** changed for Session 7's misses: a budget per section; conflict pairs of
    claims the parties argue, stated pairs ranked above inferred ones; Empirical or Predictive
    by what would settle it, in `crux-types.md`; quotation marks for verbatim text only; the
    no-conflict test; nothing after Confidence. The Framing-or-Value tie-break is 0.1.0's, so
    `framing-piano-lessons` may miss on type again (*Known debt*).
  - **The review's rules for two cases** (*The data layer*): record `gate_fired` on every output
    of `one-sided-games-night` and `no_conflict_reported` on every output of
    `no-conflict-quiz-team`; each gold.md's note, below its frontmatter, says what else counts.
- **How Session 7's review went:** the owner reviewed the first case in the chat, then asked for
  the rest to be drafted; each run's fields and note were drafted for the owner against gold.md
  and its note in a scratch file, and the owner confirmed all eighteen rows before they were
  recorded. Show the owner each case's gold beside its runs either way.
- **Where 0.1.0 missed, to watch in 0.2.0's runs:** type on `framing-piano-lessons` (Value for
  Framing), `predictive-hall-solar` (Empirical, with an inferred premise as its crux) and
  `real-lincoln-douglas` (Predictive); length everywhere, worst on `real-lincoln-douglas`
  (564 and 591) and `value-theatre-season`; quotes on `no-conflict-quiz-team`.
- **The spot check of 0.2.0:** two runs on a fictional bookshop dispute, 296 and 315 words, every
  quotation verbatim. One short input, so it says nothing about the long excerpt.
- **The smoke test:** the owner deleted crux-finder's claude.ai upload in Session 5 and none was
  made since. The smoke test uploads the zip (`zip -r crux-finder.zip crux-finder` from
  `plugins/crux-finder/skills/`); it then syncs into Claude Code as `anthropic-skills:crux-finder`,
  and `run.py` refuses while it loads, so run the cycle first, the smoke test after, and delete
  the upload when done unless the owner keeps it.
- **Baseline** (ARCHITECTURE's table): `verify` green with 6 stages, about 21 s; 203 unit tests
  passed, 0 skipped; 13 Python files; 2 skill folders, 2 plugins, 2 marketplace entries;
  `claude` 2.1.329; `checks.py` as above.
- **Not done:** installing from GitHub, for both skills, is not yet checked by a person
  (`docs/BACKLOG.md`).

## Watch for

- **`review.md` records the owner's answers.** The session never fills `crux_match`,
  `type_match` or `people_statement` from its own judgement.
- **A gold.md is never edited once results exist:** `checks.py` fails the gold order. A gold
  that turns out wrong is the owner's call, and the case's results start over.
- **The real excerpt holds the era's racial terms,** and reports quote it verbatim into
  committed results; that was known and accepted when the case was chosen.
- **Twenty real runs, about $3.40:** the eval runner is the exclusive resource, run one at a
  time; the cost is the owner's. Record `claude`'s version, since it is not pinned.
