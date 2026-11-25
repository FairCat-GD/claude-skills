Read docs/spec/FEATURE-eval-engine.md EE 3, 5–8; docs/ARCHITECTURE.md invariants 6 and 7, *The
data layer*, *The eval harness*, *crux-finder* (Decided), *Known debt*; E1's done-note;
`evals/crux-finder/cases/` (each `input.md` and `gold.md`, its note included),
`evals/crux-finder/checks.py`, `tests/test_crux_finder_checks.py`; then CLAUDE.md, *The session
cycle* in docs/DEVELOPMENT-WORKFLOW.md, docs/ARCHITECTURE.md's overview, invariants and baseline,
docs/spec/SESSIONS.md's header, your block and E1's done-note, then this file, and do Session E2:
crux-finder's cases on the new engine. E2 covers:
- the ten cases as `prompt.md` and graders, each grader approved by the owner before it is
  committed;
- `real-lincoln-douglas/gold.md` gaining its input's `source:` and `license:`;
- the new `checks.py` on `evals/shared.py`, and its tests;
- the old runner, its tests, the `input.md` files and round 1's results retired in the same commit.

E2 cuts no version unless a shipped file changes.

## State you need that is not in the specs

- **Round 2 is provenance-tracer, and one eval engine for every skill:** P1 and E1 are done; E2,
  E3, P2, P3, P4 and P5 remain.
- **Push status:** `origin/main` holds everything through P1's review commit. E1's commits are
  local and wait for the next approved push; nothing in them changes what installs.
- **What E1 left that E2 builds on:**
  - **The shared runner,** `uv run evals/run.py crux-finder --runs 2 --max-cost-usd <usd>
    [--case <id> …] [--trial <folder>]`. crux-finder's row in `SKILLS` grants no tools.
    - **The copy:** it runs the engine on a temporary copy of `plugins/crux-finder`, each case
      copied under the copy's `evals/` without `gold.md`, so a `prompt.md` needs no `plugins:`
      line.
    - **The refusals:** it refuses while `plugins/crux-finder/` or
      `evals/crux-finder/cases/` has uncommitted changes. `--trial <folder>`, outside the
      repository, relaxes the second and writes there; it is how E2's gate run ("one cheap run of
      one case, nothing committed") is made. Delete the trial folder afterwards.
  - **`evals/shared.py`,** for the new `checks.py`:
    - `split_frontmatter` and `fields`, as crux-finder's `checks.py` has them now;
    - `read_run`, which gives a `run-N.md`'s header, calls and reply apart, so the quote, symmetry
      and length checks read the reply alone;
    - `read_verdicts`, which gives each grader's verdict.

    A script under `evals/crux-finder/` imports it as its docstring says (its folder's parent on
    `sys.path`, then `import shared  # noqa: E402`). Invariant 5's test allows `shared` and
    nothing else of `evals/`.
  - **The result formats** are in *The data layer*'s Built part:
    - `run-N.md`'s header no longer has `skill_calls` or `denials`: the calls are listed, a
      Skill call as `- Skill: crux-finder:crux-finder`;
    - `verdicts-N.md` holds each grader's `verdict`, `scored`, `weight`, `votes` and
      `explanation`;
    - a run the engine graded is written even with a turn-cap or timeout error, its `error`
      header set, so the checks must decide how such a run counts.
- **What the engine needs from a case** (measured with `claude` 2.1.330, *Context*):
  - **`allowed_tools: [Skill, Read]`:** a skill reads its own references only when the case lists
    `Read`, though the docs call it pre-approved; `Skill` fires unlisted. Listing ToolSearch
    prints "not granted".
  - **Frontmatter keys:** an unknown key fails that case alone. The allowed keys are
    `schema_version`, `name`, `description`, `tags`, `plugins`, `runs`, `expected_outcome`,
    `model`, `max_turns`, `timeout_seconds`, `allowed_tools`, `disallowed_tools`,
    `artifact_publish`, `growthbook_overrides`, `append_system_prompt` and `env`. So `source:`
    and `license:` go in `gold.md`, never in `prompt.md`.
  - **Overrides:** a case's `name` must stay its folder's name, since the runner matches results
    by it. `runs:` and `model:` are overridden by the runner.
  - **Graders:** `graders/<name>.md`, frontmatter `type:` and its options; an `llm` grader's body
    is its criteria. `regex` is a JavaScript pattern, with `flags: i` rather than an inline
    `(?i)`, and `match: not_contains` for an absence.
  - **Defaults:** `max_turns` is 10 and `timeout_seconds` 300. A turn-cap or timeout run is
    written as the skill's result, so size both with room.
- **The judge:** `claude-haiku-5-5`, pinned in the runner, three votes per `llm` grader. It was
  shown the whole of a 1,756-word reply, and its explanation is the votes alone, with no reason.
  The owner reading a failed verdict reads the reply in `run-N.md`.
- **Decisions written down nowhere else, for P2 and P3** (carried from P1):
  - **The no-reply line** the P1 runs used, for P2's `append_system_prompt` to reuse word for
    word: `No reply is possible in this run: the user cannot answer questions.`
  - **The label line** is the first line under `## Provenance:`. A regex anchors on
    `**Roots:** <value> · **Grounding:**`, since the template's third line, the count line, also
    starts with `**Roots:**`.
  - **The footer** closes forward reports only. The reverse report, the refusal and a question
    carry none, so the spec's "footer lines present, every run" grader means every forward
    report.
  - **The web tools under the engine** (E1): WebSearch and WebFetch are deferred, loaded with
    ToolSearch, and called in the main session, not in a `web-fetch` subagent as under
    `claude -p`. A subagent's calls are in the trace and listed `(in <type>)` in `run-N.md`, so
    P3's "every chain URL in one of the run's fetches" reads the `WebFetch` lines, wherever they
    ran.
- **Baseline** (ARCHITECTURE's table):
  - `verify` green with 6 stages, about 32 s;
  - 281 unit tests passed, 0 skipped;
  - 17 Python files;
  - 3 skill folders, 3 plugins, 3 marketplace entries;
  - `claude` 2.1.330;
  - `checks.py`: `checks: 10 case(s), 0 problem(s); every pass bar met`, exit 0.

  E2 moves the tests and files by what it retires and adds; the block's gate says what
  `checks.py` reports after.
- **Not done:** no real skill has run through the shared runner, and an API error's shape in
  the engine's result is unmeasured (`docs/BACKLOG.md`).

## Watch for

- **The Asks at the start of E2:**
  - the block's two: how a corrected verdict is recorded, and how each gold's note becomes
    graders;
  - E1's: the judge model, now that real graders exist to see it misjudge.
- **A grader or `prompt.md` must be committed before a real run;** the runner refuses otherwise.
  A trial before the commit uses `--trial`.
- **The engine's `tool_used` grader on `Skill` is scored** under `--ablation none`, which the
  runner always passes.
- **The session never commits a grader the owner has not approved,** and three gold files must
  not change (the block's *Watch for*).
