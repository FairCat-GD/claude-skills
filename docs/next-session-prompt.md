Read everything Session 8's block names: `SPEC.md`, `PDD.md`, `REVIEW-2026-11-17.md` and
`docs/spec/SESSIONS.md` in full; `ARCHITECTURE.md` in full; `CLAUDE.md`; `DEVELOPMENT-WORKFLOW.md`
*Rounds* (*Close*) and *Git*, with *The session cycle*. Then the previous block's done-note
(7c), then this file, and do Session 8: the release and the round's close. 8 covers:
- `plugins/crux-finder/README.md` (decision 19): install per target, one example report taken
  verbatim from the results, the eval results table;
- the root README: crux-finder no longer marked in development;
- crux-finder 1.0.0 (decisions 20, 23): the version fields and the changelog entry, only if
  decision 23's conditions hold;
- the round's close: `ARCHITECTURE.md` read cold against the code, `CLAUDE.md` pointed at the
  plugin READMEs, anything open moved to `docs/BACKLOG.md`, then after the review the separate
  `docs: close round 1` commit;
- asked at the start: the tag `crux-finder--v1.0.0`, and any push, each on its own.

Release crux-finder 1.0.0.

## State you need that is not in the specs

- **Round 1 is a home for many skills**: Sessions 0–7c are done; 8 remains, the round's last.
- **Push status.** `origin/main` holds everything through Session 7b (`b187824`). Session 7c's
  commit and its `review:` commit are local until the owner approves a push; list
  `git log origin/main..HEAD` before any push.
- **Decision 23's conditions, as 7c left them:**
  - **Every pass bar met** by Session 7c's cycle on crux-finder 0.4.0, commit `b187824`:
    crux 20/20, type 18/20, stability 9/10, quotes 20/20, symmetry 18/18, length 18/18,
    people 20/20, gate 2/2, no conflict 2/2, gold order 10/10, as it stands 20/20.
  - **The claude.ai smoke test passed,** 3/3, on the same skill (Fable 5.2 at High effort).
  - **No change to the skill's instructions or references since that run:** check it against
    git (`git log b187824.. -- plugins/crux-finder/skills/crux-finder/`, which should list
    nothing until 1.0.0's version fields move). The version fields are the one change decision
    23 allows, and `metadata.version` sits in `SKILL.md`. `checks.py`'s last row, "Runs on the
    skill as it stands", is `_as_it_stands`, which runs `git diff --quiet <commit> --
    plugins/crux-finder/skills/crux-finder` for each run's commit: any change in the folder,
    the version line included, makes it 0 / 20 and `checks.py` exit 1. How the release reads
    that row after the bump (as decision 23 allows, or with a change to the check) is the
    owner's call: ask, do not guess.
- **`uv run evals/crux-finder/checks.py`** prints `checks: 10 case(s), 0 problem(s); every pass
  bar met`, exit 0, with the smoke test's row 3 / 3.
- **The results** in `evals/crux-finder/results/<id>/`: `run-1.md`, `run-2.md` and `review.md`
  for each case, plus `claude-ai.md` for `empirical-studio-kiln`, `one-sided-games-night` and
  `no-conflict-quiz-team`. The README's example report must be one of them, verbatim (block's
  Watch for), and the results table is 7c's summary table in its done-note.
- **claude.ai:** the upload was deleted after the smoke test and no synced `crux-finder` loads
  in Claude Code. claude.ai now takes uploads on its Plugins page (*Add*, *Upload plugin*),
  which accepts a skill's `.zip`; it listed crux-finder as a plugin with version "v1". The
  READMEs still say "upload the zip as a custom skill", which is still what it does; whether to
  name the page is Session 8's README work.
- **Baseline** (ARCHITECTURE's table): `verify` green with 6 stages, about 25 s; 203 unit tests
  passed, 0 skipped; 13 Python files; 2 skill folders, 2 plugins, 2 marketplace entries;
  `claude` 2.1.330; `checks.py` as above.
- **Not done:** installing from GitHub, for both skills, is not yet checked by a person
  (`docs/BACKLOG.md`).

## Watch for

- **Decision 23 is a gate, not a formality:** any edit under
  `plugins/crux-finder/skills/crux-finder/` besides the version fields needs a new cycle first.
  README and CHANGELOG are outside the skill folder.
- **The tag comes last,** after the review, the close and any approved push (*Git*), and each
  is asked on its own.
- **The real excerpt holds the era's racial terms;** choose the README's example report from a
  synthetic case.
