Read docs/spec/FEATURE-provenance-tracer.md (decisions PT 1–3, 6, 9–12, and the spec's *Scope*,
*Repo placement*, *SKILL.md frontmatter*, *Mode selection*, *Asking the user*, *Forward trace*,
*Reverse trace*, *Labels*, *Output format*, *Guardrails* and *Distribution*); docs/ARCHITECTURE.md
invariants 2–4 and 8, *Context*, *The contract between the layers*, *verify*,
*provenance-tracer*, *Packaging*; plugins/crux-finder/ as the pattern; then CLAUDE.md, *The
session cycle* in docs/DEVELOPMENT-WORKFLOW.md, docs/ARCHITECTURE.md's overview, invariants and
baseline, docs/spec/SESSIONS.md's header and your block, then this file, and do Session P1:
provenance-tracer, the skill. P1 covers:
- the plugin and its skill folder, `SKILL.md` and four references, from the owner's spec;
- its marketplace entry, published name and `LIMITS` row, with their tests;
- its README, CHANGELOG, and the root README;
- three headless traces and an install from this folder, tried by hand.

Release provenance-tracer 0.1.0.

## State you need that is not in the specs

- **Round 2 is provenance-tracer, and one eval engine for every skill:** the intake is done;
  P1, E1, E2, E3, P2, P3, P4 and P5 remain. P1 is the round's first session, so there is no
  previous done-note to read.
- **The intake is committed locally, not pushed.** `origin/main` holds everything through
  `docs: close round 1`.
- **What P1 builds on:**
  - `.claude-plugin/marketplace.json` lists two plugins, each `{"name", "source"}`; the new
    entry follows them.
  - `scripts/check_plugins.py`'s `PUBLISHED` names the two published plugins;
    `scripts/check_skills.py`'s `LIMITS` has crux-finder's row alone,
    `Limits(lines=300, scripts=False)`, and `tests/test_check_skills.py` asserts that row.
  - `plugins/crux-finder/` is the shape to copy: `plugin.json` with `name`, `version`,
    `description`, `author`, `homepage`, `license`; `SKILL.md` naming each reference by its
    path, which the `skills` stage requires.
- **Decisions written down nowhere else:** the intake moved the retirement of crux-finder's old
  eval harness from E3 to E2 while writing the plan, so the real debate case's gold can gain
  its `source:` and `license:` before any new result (E2's block says why). The spec's file is
  copied byte for byte into `FEATURE-provenance-tracer.md`; nothing else holds it.
- **Baseline** (ARCHITECTURE's table, crux-finder 1.0.0 and travel-itinerary-builder 1.1.0):
  `verify` green with 6 stages, about 25 s; 208 unit tests passed, 0 skipped; 13 Python files;
  2 skill folders, 2 plugins, 2 marketplace entries; `claude` 2.1.330; `checks.py`:
  `checks: 10 case(s), 0 problem(s); every pass bar met`, exit 0. P1 moves the skill, plugin
  and marketplace counts to 3 and adds tests.
- **Not done:** nothing was measured of `claude plugin eval`; its facts in the spec files come
  from its docs and are E1's to measure.

## Watch for

- **The skill's description is the spec's, word for word** (184 characters).
- **`SKILL.md` keeps `metadata.version`,** against the spec's frontmatter line (PT 1).
- **The headless runs need the web tools allowed** and start from an empty temporary folder,
  so they load neither this repository's `CLAUDE.md` nor the owner's settings, as round 1's
  Session 4 ran crux-finder (*Context*, Built).
- **The private-person run must make no web search;** record it from the run's own tool calls.
