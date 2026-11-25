Read docs/spec/FEATURE-eval-engine.md in full; docs/ARCHITECTURE.md invariants 5 and 6, *Context*,
*Layout and boundaries*, *The eval harness*, *The data layer*, *Testing strategy*; the engine's
docs, `https://code.claude.com/docs/en/plugin-evals.md`, and `claude plugin eval --help`;
`evals/crux-finder/run.py`, `tests/test_crux_finder_run.py`, `tests/test_evals_stdlib.py`; then
CLAUDE.md, *The session cycle* in docs/DEVELOPMENT-WORKFLOW.md, docs/ARCHITECTURE.md's overview,
invariants and baseline, docs/spec/SESSIONS.md's header, your block and P1's done-note, then this
file, and do Session E1: the eval engine, measured, and the shared runner. E1 covers:
- the engine measured first, each measurement a stop if it fails;
- the shared runner under `evals/`, standard library only, and its tests against a stub;
- invariant 5's test allowing shared code under `evals/`;
- crux-finder's tooling untouched.

E1 cuts no version.

## State you need that is not in the specs

- **Round 2 is provenance-tracer, and one eval engine for every skill:** P1 is done; E1, E2,
  E3, P2, P3, P4 and P5 remain.
- **Push status:** `origin/main` holds everything through P1's review commit ("review: page
  fetch found in any form before the skill stops, no search note on a refusal, and 5 smaller"),
  pushed with the owner's yes, so provenance-tracer 0.1.0 is installable from GitHub;
  `docs/BACKLOG.md`'s *Installing from GitHub* names it. Nothing waits.
- **What P1 left that E1 builds on:**
  - `plugins/provenance-tracer/` at 0.1.0, the third marketplace entry, in `PUBLISHED` and
    `LIMITS`. No case or result exists for it; P2 writes them.
  - **The web tools in a headless run** (*Context*, Built, measured with `claude` 2.1.330):
    - WebSearch is a deferred tool, loaded with ToolSearch before the first search;
    - WebFetch is not among the main session's tools: every fetch ran inside a built-in
      `web-fetch` subagent, as a WebFetch call in that subagent's events.

    E1's measurement of `--allow-tools WebSearch WebFetch` and of what a run calls its tools
    should check whether the engine's run behaves the same. If it does, a trace's fetches are
    found among subagent events, which P3's "every chain URL in one of the run's fetches" needs.
  - **What a run should not do:** under `--permission-prompts none`, one Bash call, a local PDF
    text extraction, was denied, and no web call was.
  - **A read outside the run's folders was allowed:** one run read its own session's tool-results
    files under `~/.claude/projects/`, where the CLI saved a long fetch, despite
    `--no-session-persistence` (*Context*, Built). E1's isolation measurement checks whether an
    engine run can read beyond that folder.
- **Decisions written down nowhere else, for P2 and P3:**
  - **The no-reply line** the P1 runs used, for P2's `append_system_prompt` to reuse word for
    word: `No reply is possible in this run: the user cannot answer questions.`
  - **The label line** is the first line under `## Provenance:`. A regex anchors on
    `**Roots:** <value> · **Grounding:**`, since the template's third line, the count line, also
    starts with `**Roots:**`.
  - **The footer** closes forward reports only. The reverse report, the refusal and a question
    carry none, so the spec's "footer lines present, every run" grader means every forward
    report.
- **Decided parts of `ARCHITECTURE.md` changed since the plan was written** (each logged):
  - *provenance-tracer*: how the skill tells no reply is possible, the roots rule, and two rules
    from P1's runs (nothing after the report; all 6 opening queries);
  - *verify*: provenance-tracer's limits beside crux-finder's.

  None changes a later block.
- **Baseline** (ARCHITECTURE's table, provenance-tracer 0.1.0, crux-finder 1.0.0,
  travel-itinerary-builder 1.1.0):
  - `verify` green with 6 stages, about 27 s;
  - 210 unit tests passed, 0 skipped;
  - 13 Python files;
  - 3 skill folders, 3 plugins, 3 marketplace entries;
  - `claude` 2.1.330;
  - `checks.py`: `checks: 10 case(s), 0 problem(s); every pass bar met`, exit 0.
- **Not done:** nothing of `claude plugin eval` has been measured yet; that is E1's first step.

## Watch for

- **The measurements' spend is the block's Ask:** ask before the first engine call, with
  `--max-cost-usd` on each.
- **`--no-publish` on every engine call,** measurements included: the engine publishes its
  report to claude.ai by default.
- **The engine writes `results/` inside the plugin unless `--output-dir` is given,** which would
  also make the runner refuse on uncommitted plugin changes.
- **A throwaway case lives in a temporary folder, never in the repository,** and is fictional.
