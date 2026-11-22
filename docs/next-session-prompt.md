Read `SPEC.md` decisions 21, 22, 23; `PDD.md` B, *Runner*, *claude.ai smoke test*, *Review*,
*Deterministic checks*, *Pass bars*; `ARCHITECTURE.md` *crux-finder*, *The data layer*, *The
eval harness*; the done-notes of Sessions 7 and 7a. Then CLAUDE.md, *The session cycle* in
docs/DEVELOPMENT-WORKFLOW.md, docs/ARCHITECTURE.md's overview, invariants and baseline,
docs/spec/SESSIONS.md's header, your block and the previous block's done-note, then this file,
and do Session 7b: the third eval cycle, on crux-finder 0.3.0, then the claude.ai smoke test
once the bars are met. 7b covers:
- Session 7a's result files removed, then `run.py --runs 2` over the ten cases, `checks.py`, the
  owner's review of every run into `review.md`, and the summary table against the pass bars;
- a bar missed: the skill changed for what the reviews show, crux-finder 0.4.0, the results
  recorded, and 7c inserted with the owner;
- every bar met on the skill as it stands: the claude.ai smoke test on `empirical-studio-kiln`,
  `one-sided-games-night` and `no-conflict-quiz-team`.

Release 0.4.0 only when the cycle changes the skill.

## State you need that is not in the specs

- **Round 1 is a home for many skills**: Sessions 0–7a are done; 7b, inserted in Session 7a, and
  8 remain.
- **Push status.** `origin/main` holds everything through Session 7a: its commit and its
  `review:` commit ("review: crux-finder's caps hold with a three-word party label and the party
  note, the 0.3.0 link, and 4 smaller"), pushed with the owner's yes, so crux-finder 0.3.0 is
  installable.
- **What Session 7a left that 7b builds on:**
  - **Session 7a's results** in `evals/crux-finder/results/<id>/`: `run-1.md`, `run-2.md` and
    `review.md` for each case, run on 0.2.0 at commit `9cae03b`. A new cycle replaces them:
    remove all three files of every case before running, since `run.py` skips a run file that
    exists and `checks.py` wants a `review.md` section for every output. Git keeps them.
  - **`uv run evals/crux-finder/checks.py`** prints 2 problems (the excerpt's two reports over
    400 words) and `pass bars not met: Length ≤ 400 words, Runs on the skill as it stands
    (decision 22)`, exit 1, until the old results are removed.
  - **7a's cycle on 0.2.0 met every bar but length:** crux 20/20, type 18/20, stability 10/10,
    quotes 20/20, symmetry 18/18, length 16/18 (`real-lincoln-douglas` at 488 and 463; the rest
    283 to 393), people 20/20, gate 2/2, no conflict 2/2.
  - **crux-finder 0.3.0** changed for length alone: a cap in words for every section, adding up
    to under 400 with the headings and labels (each steelman 45, Common ground 40, The crux 130
    with its sentence 25 and each field 22, Secondary cruxes 50 in all, Not actually in dispute
    30, Confidence 25), a name or role in a steelman's brackets of at most three words, no
    secondary cruxes in a report that opens with the note on the agent as a party, and the
    steelman kept to the reasons the conclusion most rests on. The last two came after the spot
    check, from Session 7a's review, and no run has measured the label rule or the note rule.
  - **The review's rules for two cases** (*The data layer*): record `gate_fired` on every output
    of `one-sided-games-night` and `no_conflict_reported` on every output of
    `no-conflict-quiz-team`; each gold.md's note, below its frontmatter, says what else counts.
- **How Session 7a's review went:** a fresh general-purpose subagent was given the field rules
  and told to read only each case's `input.md`, `gold.md` and the two run files, not git history,
  `docs/` or other results; it returned draft rows with a reason for each borderline call. The
  session assembled one scratch file per cycle, each case's gold beside its two replies, the
  word counts and the draft, and the owner confirmed all twenty rows. `review.md` holds only the
  rows the owner confirmed or corrected.
- **What to watch in 0.3.0's runs:** length on `real-lincoln-douglas`; symmetry, which the first
  spot check of the caps broke once (43/54) before the steelman line; crux and type with shorter
  fields; `framing-piano-lessons` may still read as Value (*Known debt*), which uses both of the
  type bar's two allowed misses.
- **The spot check of 0.3.0:** a fictional two-speaker debate of 1,208 words, run twice: 326 and
  300 words, steelmen 48/48 and 43/43, every quotation verbatim, the same crux in both.
- **The smoke test:** no claude.ai upload of crux-finder exists. The smoke test uploads the zip,
  made outside the repository (`zip -r -X <scratchpad>/crux-finder.zip crux-finder -x
  '*.DS_Store'` from `plugins/crux-finder/skills/`, which keeps any Finder file inside the skill
  folder out of the upload); it then syncs into Claude Code as `anthropic-skills:crux-finder`,
  and `run.py` refuses while it loads, so run the cycle first, the smoke test after, and delete
  the upload when done unless the owner keeps it. claude.ai is the owner's by hand: the owner pastes each case's `input.md` body into a
  fresh chat and pastes back the reply from claude.ai's Copy button, with the model used.
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
- **Twenty real runs, about $3.60:** the eval runner is the exclusive resource, run one at a
  time; the cost is the owner's. Record `claude`'s version, since it is not pinned.
