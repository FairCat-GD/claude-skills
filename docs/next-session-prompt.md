Read `SPEC.md` decisions 1, 3, 10, 17, 18, 19, 25, 28, 29; `REVIEW-2026-11-17.md` F2;
`PDD.md` B, *Repo structure* and *Distribution*; `ARCHITECTURE.md` invariants 1–3 and 8,
*Context*, *Layout and boundaries*, *The contract between the layers*, *verify*,
*travel-itinerary-builder*, *Packaging*, *Deliberate decisions*. Then CLAUDE.md, *The session
cycle* in docs/DEVELOPMENT-WORKFLOW.md, docs/ARCHITECTURE.md's overview, invariants and baseline,
docs/spec/SESSIONS.md's header, your block and the previous block's done-note, then this file,
and do Session 2: the restructure. 2 covers:
- the marketplace, `.claude-plugin/marketplace.json`;
- the itinerary plugin: the move, its `plugin.json`, and the frontmatter (F2);
- the `skills` and `plugins` stages;
- the plugin's README and changelog, and the root README.

Release travel-itinerary-builder 1.0.1.

## State you need that is not in the specs

- **Round 1 is a home for many skills**: Sessions 0 and 1 are done; Sessions 2–8 remain.
- **Session 1 and its review fixes are pushed.** `origin/main` holds everything through
  `review: a merge of pushed work no longer fails hygiene, …`; no local commit waits for a
  push. The push published the tooling and the skill's Lisbon examples. There is no marketplace
  yet, so nothing new is installable.
- **What Session 1 left that Session 2 builds on:**
  - `scripts/verify.py`'s `STAGES` maps each stage name to a function that returns the commands
    it runs, each a list of arguments run from the root. `skills` and `plugins` go ahead of
    `format`. `tests/test_verify.py`'s order test lists the stages, so it changes with them.
  - `pyproject.toml` has no runtime dependencies. The Agent Skills validator stays out of it: it
    runs through `uvx`, pinned to a commit, on Python 3.11 or newer.
  - The hygiene stage keeps its stamp at `.git/hygiene-scanned`. A change to
    `scripts/hygiene.py` or to the term list brings one full scan.
  - The move carries Session 1's change to the skill: the seven F1 lines now use Lisbon
    (`SKILL.md:89`, `:138`, `:189`; `references/location-block-template.md:37`, `:55`;
    `references/research-playbook.md:61`, `:68`). The change is unreleased. Per decision 18,
    1.0.1's changelog entry carries it, written for the person using the skill.
- **What the spec said that turned out wrong or harder:**
  - Block 1 expected F1's word to be counted in pushed history. The full scan reads pushed
    messages, and the word is in none of them, so the count is 0 (amended at plan time, with the
    owner). The word remains in file versions stored in 3 pushed commits, which no scan reads.
  - ruff 0.17's default also formats the Python code blocks inside Markdown. `include` limits
    ruff to Python files and `pyproject.toml`, so the skill's Markdown stays as written.
  - uv refuses a `[project]` table without `version`, so `pyproject.toml` has `0.0.0`, which
    nothing reads.
- **Baseline** (ARCHITECTURE's table): `verify` green with 4 stages; 52 unit tests passed, 0
  skipped; `hygiene --all` green, with 0 hits in pushed history. Session 2 adds two stages and
  their tests.
- **Not done:** nothing from block 1.

## Watch for

- **`references/location-block-template.md:49` still writes `UAH` into the snack template.**
  That is F12, which belongs to Session 3. Session 2 changes no line of the skill beyond F2.
- **`references/output-formats.md` holds a Python code block** that ruff would reformat if its
  `include` widened. Keep ruff on Python files.
- **A new check needs its own failing case at its own stage.** For `skills` and `plugins`,
  copy the file aside, break it, watch only that stage fail, then copy it back. Never use
  `git checkout`.
