Read docs/spec/FEATURE-eval-engine.md EE 5, 7, 9; docs/ARCHITECTURE.md *The eval harness*, *The
data layer*, *crux-finder* (its eval cycles), *Known debt*; E2's done-note; crux-finder's README,
*How it was tested*; then CLAUDE.md, *The session cycle* in docs/DEVELOPMENT-WORKFLOW.md,
docs/ARCHITECTURE.md's overview, invariants and baseline, docs/spec/SESSIONS.md's header, your
block and E2's done-note, then this file, and do Session E3: crux-finder's first cycle on the new
engine. E3 covers:
- the cycle: ten cases, two runs each, through the shared runner, four at a time;
- the owner's reading: every failed verdict, one run per case, and stability, recorded in each
  case's `review.md` as E2 settled;
- the summary table beside Session 7c's, and crux-finder's README, *How it was tested*,
  rewritten from it.

E3 cuts no version unless a shipped file changes.

## State you need that is not in the specs

- **Round 2 is provenance-tracer, and one eval engine for every skill:** P1, E1 and E2 are done;
  E3, P2, P3, P4 and P5 remain.
- **Push status:** `origin/main` holds everything through E1's handoff commit (`a4bca98`). E2's
  commits are local until the owner approves a push; nothing in E2 changes what installs.
- **What E2 left that E3 runs:**
  - **The command:** `uv run evals/run.py crux-finder --runs 2 --max-cost-usd <usd>`. A run's
    file is skipped if it exists, so a stopped cycle resumes by running the same command.
  - **The cases** carry `allowed_tools: [Skill, Read]`, `max_turns: 20`, `timeout_seconds: 900`.
    Each has `crux`, `type` and `no-statement-about-people`; `one-sided-games-night` also `gate`,
    `no-conflict-quiz-team` also `no-conflict`. `type` is a regex in seven cases, an `llm`
    grader in the one-sided, debate and father's-care cases.
  - **The judge** is `claude-sonnet-5-5`, the owner's choice over the engine's default.
  - **The cost, as measured:** one kiln run $0.21 and its judging $0.013, in 32 s. The debate
    excerpt is several times longer. Round 1's cycles cost $3.40 to $3.81 for 20 runs under
    `claude -p`.
  - **`results/`** holds only the three `claude-ai.md` replies and their `review.md`, cut to the
    `## claude-ai` section. A cycle adds `run-N.md` and `verdicts-N.md` beside them, and the
    owner's sections to the same `review.md`.
- **What `review.md` needs from the owner's reading** (`checks.py` holds it, *The data layer*):
  - a `## run-N` section for every run from run 2 on, and for any run with a failed verdict;
  - `same_crux_as_run_1: yes|no` on run 2, the owner's comparison of the two crux sentences;
  - `- <grader>: fail` to confirm each failed verdict, or `- <grader>: pass` to overrule it;
    `- <grader>: fail` also overrules a pass the owner finds wrong in the run they read;
  - a one-line `- note:` in every section.
  Until those lines exist, `checks.py` reports each failed verdict with no line as a problem.
- **How round 1's reviews were made** (*The data layer*, Session 7c): each run's fields drafted
  by a fresh reader that saw no earlier verdict, and every row confirmed or corrected by the
  owner. Under EE 5 the graders decide; E3 asks how the owner's reading is made.
- **The comparison table:** Session 7c's is in crux-finder's README, *How it was tested*, and in
  git (`docs/spec/SESSIONS.md` of round 1, as of the review commit before `docs: close round 1`).
- **Baseline** (ARCHITECTURE's table): `verify` green with 6 stages; 299 unit tests passed, 0
  skipped; 15 Python files; 3 skill folders, 3 plugins, 3 marketplace entries; `claude`
  2.1.330; `checks.py`: `checks: 10 case(s), 0 problem(s); no cycle yet, so the cycle's bars are
  not counted; the claude.ai smoke test met`, exit 0.
- **Not done:** an API error's shape in the engine's result is unmeasured (`docs/BACKLOG.md`);
  the engine does not read a grader at load, so a grader's own error shows only when its case
  runs.

## Watch for

- **The Ask at the start of E3:** the cycle's cost ceiling, `--max-cost-usd`; and how the owner's
  reading is made.
- **A missed bar is a stop** (the block). A grader changed means its case starts over, its
  results removed, since `checks.py` fails a run whose graders changed since its commit.
- **The type bar has no slack:** both piano runs are expected to miss on type (*Known debt*).
- **`checks.py` counts the owner's line over the engine's verdict;** a line that agrees with a
  pass is allowed but changes nothing.
- **A real transcript can hold a word on the term list** (`CLAUDE.md`).
