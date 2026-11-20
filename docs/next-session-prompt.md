Read `SPEC.md` decisions 17, 21; `PDD.md` B, *Inputs*, *Guardrails*, *Evals* (*Cases*);
`ARCHITECTURE.md` invariant 7, *The data layer*; `DEVELOPMENT-WORKFLOW.md` *A clean repository*.
Then CLAUDE.md, *The session cycle* in docs/DEVELOPMENT-WORKFLOW.md, docs/ARCHITECTURE.md's
overview, invariants and baseline, docs/spec/SESSIONS.md's header, your block and the previous
block's done-note, then this file, and do Session 6: the eval cases. 6 covers:
- eight synthetic inputs, one per row of PDD B's synthetic set, drafted by the session and
  approved by the owner;
- two real inputs: a public-domain debate excerpt and a dispute the owner writes up;
- ten `gold.md`, each written or approved by the owner, committed before any result exists;
- `ARCHITECTURE.md`'s *The data layer* Built part, the cases as committed.

No version: the session changes no skill.

## State you need that is not in the specs

- **Round 1 is a home for many skills**: Sessions 0–5 are done; Sessions 6–8 remain.
- **Push status.** `origin/main` holds everything through Session 4's `review:` commit. Session
  5's commit (`feat: the eval tooling, …`) and its `review:` commit are pushed with the owner's
  yes, so `origin/main` holds everything through Session 5.
- **What Session 5 left that Session 6 builds on:**
  - **The formats `checks.py` reads** (*The data layer*, Built): a case is
    `evals/crux-finder/cases/<id>/` with `input.md` and `gold.md`. gold.md's frontmatter is read
    as one `key: value` per line, no YAML library, so each of `crux`, `type`, `crux_for` and
    `approved_by` must sit on one line (quote a value only whole). `approved_by` must be
    non-empty; `FairCat-GD` by decision 17.
  - **input.md:** the prompt is its body, frontmatter left out, and quotes are checked against
    that body; so the two real cases' `source:` and `license:` go in frontmatter, and the body
    is exactly the dispute as the model should see it.
  - **`uv run evals/crux-finder/checks.py`** passes on cases with no results once every gold.md
    is committed: it prints `checks: 10 case(s), 0 problem(s); no results yet, …` and exits 0.
    Before the commit it reports each gold.md as `not committed`. Run it after the commit for
    the block's gate.
  - **`run.py` lists case folders by name, sorted;** a case id is a folder name and is never
    renamed once results exist.
- **What the spec said that turned out wrong or harder:** nothing new in Session 5. The report's
  400 words are still not met: the one real run gave 472 (Session 7's cycle).
- **Decisions written down nowhere else:**
  - Session 6's synthetic inputs must not reuse the topics of `crux-types.md`'s examples (a
    boiler, a crossing guard, online choir rehearsals, an export module, a flat running route,
    local news, a bandstand and footpaths, library hours and books, a garden shed, a kitchen
    rota), the thin slice's bakery, or Session 5's measurement input (an allotment society's seed
    swap), so the cases test the skill rather than its own examples.
  - The owner deleted crux-finder's claude.ai upload in Session 5. Session 7's smoke test
    uploads the zip again; the upload then syncs into Claude Code as
    `anthropic-skills:crux-finder`, and `run.py` refuses runs while it loads.
- **Baseline** (ARCHITECTURE's table): `verify` green with 6 stages, about 25 s; 203 unit tests
  passed, 0 skipped; `hygiene --all` green; 13 Python files; 2 skill folders, 2 plugins, 2
  marketplace entries; `claude` 2.1.329. Session 6 adds no Python file.
- **Not done:** installing from GitHub, for both skills, is not yet checked by a person
  (`docs/BACKLOG.md`).

## Watch for

- **The session never writes a `gold.md` the owner has not approved,** and never runs `run.py`:
  no file under `evals/crux-finder/results/` exists at the end.
- **A real transcript may hold a word on the term list.** Ask the owner; never trim a quote
  silently.
- **The inputs are quoted verbatim by the reports,** so their text is final once gold exists.
- **gold.md's values on one line each:** a folded or multi-line YAML value reads as missing.
