Read `SPEC.md` decisions 8, 9, 18; `REVIEW-2026-11-17.md` in full; `ARCHITECTURE.md` *Context*,
*travel-itinerary-builder*; the skill's five files. Then CLAUDE.md, *The session cycle* in
docs/DEVELOPMENT-WORKFLOW.md, docs/ARCHITECTURE.md's overview, invariants and baseline,
docs/spec/SESSIONS.md's header, your block and the previous block's done-note, then this file,
and do Session 3: the itinerary fixes. 3 covers:
- the contradictions and small bugs: F3, F12–F15, F18–F21;
- the open behaviours, settled at the start: F4, F16, F17;
- the environment assumptions, F5–F10, and the minimum environment in `compatibility`;
- phone readability, F11, from rendered samples;
- the plugin's `CHANGELOG.md` `[1.1.0]` and its README's targets and minimum environment.

Release travel-itinerary-builder 1.1.0.

## State you need that is not in the specs

- **Round 1 is a home for many skills**: Sessions 0, 1 and 2 are done; Sessions 3–8 remain.
- **Session 2 and its review fixes are pushed.** `origin/main` holds everything through
  `review: references inside URLs, duplicate marketplace entries, …`; no local commit waits for
  a push. The push published the `faircat-skills` marketplace: travel-itinerary-builder 1.0.1 is
  installable from GitHub, and people who install it receive 1.1.0 once its version moves.
- **What Session 2 left that Session 3 builds on:**
  - **The skill moved.** Its five files are under
    `plugins/travel-itinerary-builder/skills/travel-itinerary-builder/`. The review's paths are
    relative to the old `travel-itinerary-builder/`, so prefix them.
  - **`SKILL.md`'s lines moved down 2** since the review: F2 replaced one frontmatter line with
    three. A `SKILL.md` line the review cites as `:N` is now `:N+2` (its F2 citation, `:3`,
    excepted). The files under `references/` did not move a line. `SKILL.md` has 280 lines.
  - **The frontmatter** is `name`, `description`, `license: MIT` and `metadata.version: "1.0.1"`.
    `compatibility` is an allowed field; the validator caps it at 500 characters.
  - **The version is set in two places:** `plugins/travel-itinerary-builder/.claude-plugin/plugin.json`
    and `metadata.version`. The `skills` stage fails when they differ, so 1.1.0 goes into both.
  - **The `skills` stage** also fails a file under `references/` that `SKILL.md` does not name
    by its path, a `references/` path it names that is missing, and a `SKILL.md` of 500 lines
    or more. A path counts at the start of a word or after `./`; inside a URL it names nothing.
    `LINE_LIMITS` in `scripts/check_skills.py` holds no row for this skill.
  - **The plugin's README** (`plugins/travel-itinerary-builder/README.md`) has *What it does*,
    *Using it*, install per target and the version; it says nothing yet of what each target
    needs. Its *What it does* describes the PDF as made for a phone and the chat plan as on
    request, so F5–F11's outcome may change those lines.
  - **The changelog** has `[1.0.1]` and `[1.0.0]`; `[1.1.0]` goes above `[1.0.1]`, with an
    empty `[Unreleased]` kept at the top.
- **What the spec said that turned out wrong or harder:** nothing in Session 3's ground.
  `claude plugin validate .` at the root does not compare an entry's name with its manifest, so
  `scripts/check_plugins.py` does; that touches no itinerary work.
- **Baseline** (ARCHITECTURE's table): `verify` green with 6 stages, about 6 s with uv's cache
  warm; 102 unit tests passed, 0 skipped; `hygiene --all` green, with 0 hits in pushed history; 8
  Python files; 1 skill folder, 1 plugin.
- **Not done:** installing from GitHub, now possible after the push, is not yet checked by hand
  (`docs/BACKLOG.md`).

## Watch for

- **`references/location-block-template.md:49` still writes `UAH` into the snack template.**
  That is F12, this session's.
- **`references/output-formats.md` holds a Python code block** that ruff would reformat if its
  `include` widened. Keep ruff on Python files.
- **A new reference file must be named by its path in `SKILL.md`,** or the `skills` stage fails.
- **The `skills` stage needs the network while uv's cache is cold;** it fails with uv's fetch
  error, never passes.
- **A new check needs its own failing case at its own stage.** Copy the file aside, break it,
  watch only that stage fail, then copy it back. Never use `git checkout`.
