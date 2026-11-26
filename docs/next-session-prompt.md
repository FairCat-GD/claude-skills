Read docs/spec/FEATURE-provenance-tracer.md PT 5, 8, and the spec's *Evals*;
docs/spec/FEATURE-eval-engine.md EE 4–6, 9; docs/ARCHITECTURE.md invariants 5–7, *The eval
harness*, *The data layer*, *provenance-tracer*; P2's done-note; `evals/crux-finder/checks.py` as
the pattern; then CLAUDE.md, *The session cycle* in docs/DEVELOPMENT-WORKFLOW.md,
docs/ARCHITECTURE.md's overview, invariants and baseline, docs/spec/SESSIONS.md's header, your
block and P2's done-note, then this file, and do Session P3: provenance-tracer's checks and first
cycle. P3 covers:
- `evals/provenance-tracer/checks.py` and its tests, on the shared code, every check falsified;
- the cycle: thirteen cases, three runs each, four at a time, through `evals/run.py`;
- the owner's reading of every failed verdict and one run per case, recorded in `review.md`.

P3 cuts no version.

## State you need that is not in the specs

- **Round 2 is provenance-tracer, and one eval engine for every skill:** P1, E1, E2, E3 and P2
  are done; P3, P4 and P5 remain.
- **Push status:** `origin/main` holds everything through P2's review commit ("review: each gold
  fact cites the page it rests on, and four doc fixes"), pushed with the owner's yes; nothing in
  P2 changes what installs.
- **What P2 left:**
  - **Thirteen cases** in `evals/provenance-tracer/cases/`, committed with their golds before any
    result. The well-sourced case is `well-sourced-exercise-heart-disease`, the owner's
    replacement for the spec's smoking claim.
  - **The graders `checks.py` maps to bars:** `labels` (six cases), `facts` and `no-verdict`
    (all thirteen), `footer` (the ten forward reports), `no-search` and `no-fetch` (the
    private-person case, together "No search issued") and `manager-not-searched` (the
    personal-chain case). gold.md's fields: `roots`, `grounding`, `modifiers`, `fact_N` with
    `source_N` or `must_N`, `authored`, `approved_by` (*The data layer*).
  - **The trial's cost:** the MMR forward run $1.47 and 334 s (7 searches, 23 fetches, 38
    turns), the private-person refusal $0.10 and 15 s; judging $0.01 to $0.05 a run. A cycle of
    39 runs at four at a time: the eleven cases that trace (33 runs) at about $1.50 each is about
    $50, the refusal and question cases (6 runs) under $1; time about 45 minutes. One forward run
    is a small sample: a trace that runs to the spec's limits may cost more.
  - **The trial's verdicts are a lead, not a result:** the MMR run took a 1996 pilot study as the
    root ahead of Wakefield's paper, so `labels` failed without Origin retracted. Whether that
    root is right is the owner's reading in P3. `facts` and `no-verdict` failed 3/3 under the
    judge's first wording; two clauses were added after, with the owner, and are untried.
  - **The fetch tool refuses** PubMed, PubMed Central, *The Lancet*, *The BMJ*, the BBC, *The New
    York Times* and the Wayback Machine. Runs reach primaries through Europe PMC or Crossref, or
    leave them `(not opened)`; a 403 page comes back as a call that returned, not an error.
- **What the runner needs** is unchanged: `--max-cost-usd` is required; it refuses while
  `plugins/provenance-tracer/` or `evals/provenance-tracer/cases/` has uncommitted changes.
- **Baseline** (ARCHITECTURE's table): `verify` green with 6 stages; 304 unit tests passed, 0
  skipped; 15 Python files; 3 skill folders, 3 plugins, 3 marketplace entries; `claude` 2.1.330;
  crux-finder's `checks.py`: `checks: 10 case(s), 0 problem(s); every pass bar met`, exit 0.
- **Not done:** an API error's shape in the engine's result is unmeasured (`docs/BACKLOG.md`); a
  grader's own error shows only when its case runs. No case's `llm` graders have run as
  committed: the trial ran before the two clauses were added, and its MMR `facts` and
  `no-verdict` failed. Only the trial's `labels`, `footer`, `no-search` and `no-fetch` ran as
  they stand; the other regex and `tool_used` graders were checked in node only.

## Watch for

- **The Ask at the start of P3:** the cycle's cost ceiling, `--max-cost-usd`, from the trial's
  cost per run above.
- **How gold order is reckoned** (crux-finder's `checks.py` reckons only committed results from
  history, and reads paths with `-z`) is P3's to settle with the owner.
- **The judge keeps no reasons:** the owner reads every failed verdict; a reader that gives its
  reasons helps tell a grader's wording from the reply.
- **A real page can hold a word on the term list** (`CLAUDE.md`): ask the owner; never trim a
  quote silently.
- **A cycle spends real model runs and the live web:** one cycle at a time, never in a parallel
  part.
