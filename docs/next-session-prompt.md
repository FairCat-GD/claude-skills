Read docs/spec/FEATURE-provenance-tracer.md PT 3, 6–8, and the spec's *Evals*, *Labels*, *Output
format* and *Guardrails*; docs/spec/FEATURE-eval-engine.md EE 2, 3; docs/ARCHITECTURE.md
invariant 7, *The data layer*, *The eval harness*, *provenance-tracer*; E1's and E3's done-notes;
one crux-finder case as the pattern; then CLAUDE.md, *The session cycle* in
docs/DEVELOPMENT-WORKFLOW.md, docs/ARCHITECTURE.md's overview, invariants and baseline,
docs/spec/SESSIONS.md's header, your block and E3's done-note, then this file, and do Session
P2: provenance-tracer's cases. P2 covers:
- thirteen cases under `evals/provenance-tracer/cases/<id>/`, the spec's seven forward and six
  behaviour cases, each a `prompt.md`, graders and a `gold.md` the owner approved;
- one or two cases run once through the runner with `--trial`, to prove the suite loads and to
  measure a run's cost, time, searches and fetches, nothing they write committed.

P2 cuts no version.

## State you need that is not in the specs

- **Round 2 is provenance-tracer, and one eval engine for every skill:** P1, E1, E2 and E3 are
  done; P2, P3, P4 and P5 remain.
- **Push status:** `origin/main` holds everything through E3's review commit ("review: git
  paths read with -z in crux-finder's checks, the handoff's undecided rule, and 3 smaller"),
  pushed with the owner's yes; nothing in E3 changes what installs.
- **What E3 left:**
  - crux-finder's first cycle on the engine, in `evals/crux-finder/results/`: every bar met on
    1.0.0, $4.97 for 20 runs in 3 min 16 s at four at a time, each run $0.13 to $0.30. Its
    table is in crux-finder's README and E3's done-note.
  - **The owner's reading** was made by a fresh reader that saw no verdict, its draft set beside
    the engine's, every line confirmed by the owner (*The data layer*); one run per case is
    run 1. P3 asks again at its start.
  - **The judge keeps no reasons:** a `verdicts-N.md` holds an `llm` grader's votes only
    (`judge votes: FAIL FAIL FAIL`). The owner overruled three `no-statement-about-people` fails
    the reader and owner found wrong (`docs/BACKLOG.md`). A provenance-tracer grader that
    judges prose may do the same; the owner reads every failed verdict.
  - **crux-finder's `checks.py` reckons gold order from history only for committed results,**
    so a cycle reads clean before its commit even where a retired cycle used the same paths,
    and reads every path from git with `-z`, so a name git would quote still matches. Whether
    provenance-tracer's `checks.py` (P3) does the same is P3's to settle with the owner.
- **What the runner needs for provenance-tracer** (E1, `evals/run.py`): `SKILLS` already grants
  it `WebSearch` and `WebFetch`; a case's `prompt.md` takes `allowed_tools`, `max_turns` and
  `timeout_seconds`, and no `name:` or `plugins:` line; the runner refuses while
  `evals/<skill>/cases/` has uncommitted changes, except with `--trial`, which writes outside
  the repository. `--max-cost-usd` is required.
- **Baseline** (ARCHITECTURE's table): `verify` green with 6 stages; 304 unit tests passed, 0
  skipped; 15 Python files; 3 skill folders, 3 plugins, 3 marketplace entries; `claude`
  2.1.330; crux-finder's `checks.py`: `checks: 10 case(s), 0 problem(s); every pass bar met`,
  exit 0.
- **Not done:** an API error's shape in the engine's result is unmeasured (`docs/BACKLOG.md`);
  the engine does not read a grader at load, so a grader's own error shows only when its case
  runs.

## Watch for

- **The Ask at the start of P2:** the true-statistic case and the obscure claim, from two or
  three candidates each, with the reason each fits.
- **No `gold.md` the owner has not approved,** and no fact without a source the session opened.
- **No case is one of the skill's own examples** (P1's references).
- **A trial run spends real model runs and the live web:** name the ceiling before it.
- **A real page can hold a word on the term list** (`CLAUDE.md`): ask the owner; never trim a
  quote silently.
