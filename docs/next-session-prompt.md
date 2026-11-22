Read `SPEC.md` decisions 21, 22, 23; `PDD.md` B, *Runner*, *claude.ai smoke test*, *Review*,
*Deterministic checks*, *Pass bars*; `ARCHITECTURE.md` *crux-finder*, *The data layer*, *The
eval harness*; the done-notes of Sessions 7a and 7b. Then CLAUDE.md, *The session cycle* in
docs/DEVELOPMENT-WORKFLOW.md, docs/ARCHITECTURE.md's overview, invariants and baseline,
docs/spec/SESSIONS.md's header, your block and the previous block's done-note, then this file,
and do Session 7c: the fourth eval cycle, on crux-finder 0.4.0, then the claude.ai smoke test
once the bars are met. 7c covers:
- Session 7b's result files removed, then `run.py --runs 2` over the ten cases, `checks.py`, the
  owner's review of every run into `review.md`, and the summary table against the pass bars;
- a bar missed: the skill changed for what the reviews show, crux-finder 0.5.0, the results
  recorded, and 7d inserted with the owner;
- every bar met on the skill as it stands: the claude.ai smoke test on `empirical-studio-kiln`,
  `one-sided-games-night` and `no-conflict-quiz-team`, the upload deleted afterwards unless the
  owner decides otherwise.

Release 0.5.0 only when the cycle changes the skill.

## State you need that is not in the specs

- **Round 1 is a home for many skills**: Sessions 0–7b are done; 7c, inserted in Session 7b, and
  8 remain.
- **Push status.** `origin/main` holds everything through Session 7b: its commit (`4d0d798`)
  and its `review:` commit ("review: crux-finder's type tie-breaks yield to a named condition,
  quotations keep either case, and 4 smaller"), pushed with the owner's yes, so crux-finder
  0.4.0 is installable.
- **What Session 7b left that 7c builds on:**
  - **Session 7b's results** in `evals/crux-finder/results/<id>/`: `run-1.md`, `run-2.md` and
    `review.md` for each case, run on 0.3.0 at commit `5a26a12`. A new cycle replaces them:
    remove all three files of every case before running, since `run.py` skips a run file that
    exists and `checks.py` wants a `review.md` section for every output. Git keeps them.
  - **`uv run evals/crux-finder/checks.py`** prints 1 problem (`predictive-hall-solar` run 1's
    quotation) and `pass bars not met: Type matches gold, Quotes verbatim, Runs on the skill as
    it stands (decision 22)`, exit 1, until the old results are removed.
  - **7b's cycle on 0.3.0:** length 18/18 (191 to 348 words), symmetry 18/18, crux 18/20,
    stability 10/10, quotes 19/20, type 16/20, people 20/20, gate 2/2, no conflict 2/2.
  - **crux-finder 0.4.0** changed for type and quotes: a claim a party says outright would
    change their conclusion ranks first among double cruxes, before stated pairs and depth (both
    solar runs had ranked the deeper self-use share first, typed Empirical); each quotation is
    checked letter for letter, its first letter included, capital or lower case. The review
    then had `crux-types.md`'s two tie-breaks (the record under two forecasts, the fact under a
    weighting) yield to a claim a party names, and recorded the departure from PDD B's step 6
    beside `SPEC.md` decision 21. The spot check measured the ranking, before the tie-break fix,
    on a fictional input of the solar case's shape; no run has measured the quotation rule or
    the tie-break fix.
  - **The review's rules for two cases** (*The data layer*): record `gate_fired` on every output
    of `one-sided-games-night` and `no_conflict_reported` on every output of
    `no-conflict-quiz-team`; each gold.md's note, below its frontmatter, says what else counts.
- **How Session 7b's review went:** as 7a's. One fresh general-purpose subagent was given the
  field rules and told to read only each case's `input.md`, `gold.md` and the two run files, not
  git history, `docs/`, the skill or other results; it returned draft rows with a `Borderline:`
  line per case. The session assembled one scratch file (each case's gold, word counts, both
  replies, the draft) and the owner confirmed all twenty rows. Read the draft's rows, not its
  summary: 7b's summary miscounted two rows.
- **What to watch in 0.4.0's runs:** type has no slack (the piano case's two Value runs are the
  bar's two allowed misses, *Known debt*); whether the stated-condition rule moves a primary
  crux that matched before (orchard, kiln, excerpt); quotations opening a line; length and
  symmetry, which 0.3.0's caps held.
- **The smoke test:** no claude.ai upload of crux-finder exists. The smoke test uploads the zip,
  made outside the repository (`zip -r -X <scratchpad>/crux-finder.zip crux-finder -x
  '*.DS_Store'` from `plugins/crux-finder/skills/`, which keeps any Finder file inside the skill
  folder out of the upload); it then syncs into Claude Code as `anthropic-skills:crux-finder`,
  and `run.py` refuses while it loads, so run the cycle first, the smoke test after. claude.ai
  is the owner's by hand: the owner pastes each case's `input.md` body into a fresh chat and
  pastes back the reply from claude.ai's Copy button, with the model used. `claude-ai.md` gets a
  `key: value` header (`case`, `target`, `model`, `skill_version`, `commit`, `date`) and the
  reply verbatim; its `## claude-ai` review section carries `gate_fired` or
  `no_conflict_reported` in those two cases and no `same_crux_as_run_1`. The owner chose, in
  7b, to delete the upload afterwards.
- **Baseline** (ARCHITECTURE's table): `verify` green with 6 stages, about 24 s; 203 unit tests
  passed, 0 skipped; 13 Python files; 2 skill folders, 2 plugins, 2 marketplace entries;
  `claude` 2.1.330; `checks.py` as above.
- **Not done:** installing from GitHub, for both skills, is not yet checked by a person
  (`docs/BACKLOG.md`).

## Watch for

- **`review.md` records the owner's answers.** The session never fills `crux_match`,
  `type_match` or `people_statement` from its own judgement.
- **A gold.md is never edited once results exist:** `checks.py` fails the gold order. A gold
  that turns out wrong is the owner's call, and the case's results start over.
- **The real excerpt holds the era's racial terms,** and reports quote it verbatim into
  committed results; that was known and accepted when the case was chosen.
- **Twenty real runs, about $3.80:** the eval runner is the exclusive resource, run one at a
  time; the cost is the owner's. The CLI updates itself, even mid-cycle; each run's header
  records the version.
