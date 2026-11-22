No round is in progress. Read CLAUDE.md, *The session cycle* in docs/DEVELOPMENT-WORKFLOW.md,
docs/ARCHITECTURE.md's overview, invariants and baseline, then this file; then the sections of
docs/ARCHITECTURE.md the request touches, and any a block will point at. The next session is
an **intake**: write the user's request down verbatim, ask what it leaves open,
and plan the round in `docs/spec/`, a Read line in every block (see
`docs/DEVELOPMENT-WORKFLOW.md`, *Rounds*).

## State you need that is not in the docs

- **crux-finder 1.0.0 is released,** tagged `crux-finder--v1.0.0` as the round's last act;
  travel-itinerary-builder stays at 1.1.0, untagged. Round 1 (a home for many skills: Sessions
  0–8, with 7a, 7b and 7c inserted for the eval cycles) is closed. Its spec files are deleted;
  the last done-note is in `docs/spec/SESSIONS.md` as of the review commit before the close
  (`<sha>`, filled in by the close).
- **Push status:** `origin/main` holds everything through Session 7c. Session 8's release
  commit, its `review:` commit and the close wait for the push the owner approved at the start
  of Session 8; the tag and its own push come after it.
- **Open items live in `docs/BACKLOG.md`**, including what this round added there: a second
  real eval case, the Framing-or-Value line between two golds, a case with the agent as a party,
  running either skill on Codex or another agent, installing from GitHub by hand, the itinerary
  skill on its other targets and its fallbacks, and the direction on crux-finder's *what would
  move it* and common ground.
- **Baseline** (ARCHITECTURE's table, crux-finder 1.0.0 and travel-itinerary-builder 1.1.0):
  `verify` green with 6 stages, about 25 s; 208 unit tests passed, 0 skipped; 13 Python files;
  2 skill folders, 2 plugins, 2 marketplace entries; `claude` 2.1.330; `checks.py` on Session
  7c's results, read on 1.0.0: `checks: 10 case(s), 0 problem(s); every pass bar met`, exit 0.

## Watch for

- **`checks.py` sets aside `SKILL.md`'s version line, and nothing else.** A release that only
  moves the version keeps "Runs on the skill as it stands" met; any other change in the skill
  folder turns it red until a new cycle runs on the skill as it stands, starting with the old
  results removed, since `run.py` skips a file that exists.
- **crux-finder's README carries the fourth cycle's table.** A new cycle on a changed skill
  replaces `results/`, so the README's *How it was tested* and its table move with it.
- **The type bar has no slack:** the piano case's two Value runs use both of its misses
  (ARCHITECTURE's *Known debt*), so any skill change must keep every other case on type.
