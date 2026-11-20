Read `SPEC.md` decisions 21, 22, 23; `PDD.md` B, *Evals* in full; `ARCHITECTURE.md` invariants
5–7, *Context* (the `claude` CLI), *The data layer*, *The eval harness*. Then CLAUDE.md, *The
session cycle* in docs/DEVELOPMENT-WORKFLOW.md, docs/ARCHITECTURE.md's overview, invariants and
baseline, docs/spec/SESSIONS.md's header, your block and the previous block's done-note, then this
file, and do Session 5: the eval tooling. 5 covers:
- `evals/crux-finder/run.py --runs N`: one fresh session per case per run, the prompt the
  contents of `input.md`, output to `results/<id>/run-N.md`, never opening `gold.md`, isolated
  as settled at the start;
- `evals/crux-finder/checks.py`: quotes, symmetry, length, gold order, `approved_by`, and the
  summary table of `review.md` against the pass bars;
- tests of both in `tests/`, on fictional fixtures, and the standard-library-only test
  (invariant 5);
- `CLAUDE.md`'s commands and the eval runner as the exclusive resource; `ARCHITECTURE.md`'s
  Built parts and the baseline.

No version: the session changes no skill.

## State you need that is not in the specs

- **Round 1 is a home for many skills**: Sessions 0–4 are done; Sessions 5–8 remain.
- **Push status.** `origin/main` holds everything through Session 4's `review:` commit
  (`review: one label rule for A and B, …`); no local commit waits for a push. People who install
  from GitHub now get travel-itinerary-builder 1.1.0 and crux-finder 0.1.0.
- **What Session 4 left that Session 5 builds on:**
  - **crux-finder 0.1.0** in `plugins/crux-finder/`, with `skills/crux-finder/SKILL.md` and
    `references/{procedure,crux-types,output-template}.md`. The report's fixed parts are in
    `output-template.md`: `## Crux report`, the steelman lines `**A, strongest form:**` and
    `**B, strongest form:**` (with a name or role in brackets after A or B where the input names
    its parties, and `**B (reconstructed by A), strongest form:**` after a one-sided input), the
    headings *Common ground*, *The crux*, *Secondary cruxes*, *Not actually in dispute* and
    *Confidence*, a label `**Double crux · <Type>**`, `**Crux for A · <Type>**`, `**Crux for B ·
    <Type>**` or `**No crux**`, then a blockquoted crux sentence that is the skill's own words,
    not a quote. A first line above `## Crux report` appears only when the agent is a party. The
    claim map, `### Claim map`, follows Confidence only on request. These shape the "quoted span"
    and "a question, not a report" questions at your start.
  - **What the skill did on the thin slice** (one fictional input, not an eval case): every run
    triggered it by its description and gave the template's shape, but none met the 400 words:
    547, 564, 515 headless, 486 installed, 558 on claude.ai, counted as tokens with a letter or
    digit. Your length check needs a stated rule for what a word is, and whether markup counts.
    The primary crux's label varied between runs (double crux, or a crux for A).
  - **What a `claude -p` run loads,** measured with 2.1.328 from an empty folder with
    `--plugin-dir`: the plugin under test, but also the owner's user-level plugins, the skills
    synced from the owner's claude.ai uploads, auto memory, and the user's permission mode
    (`auto`). The skill read its references with a shell `cat` outside the run's folder, with no
    denial. `--output-format stream-json --verbose` shows the Skill call and every tool call, which
    is how to tell which copy ran. This is the measurement your isolation question starts from.
  - **The claude.ai upload:** the owner chose to delete crux-finder's upload after its one run.
    While it exists, it appears in Claude Code sessions as `anthropic-skills:crux-finder`, beside
    the plugin's `crux-finder:crux-finder`; check that it is gone before measuring isolation.
- **`LIMITS` in `scripts/check_skills.py`** replaced `LINE_LIMITS`: one table of
  `Limits(lines, scripts)` rows, crux-finder's the only one. Its `scripts=False` fails a
  `scripts/` folder and any file but `SKILL.md` and Markdown under `references/`.
- **What the spec said that turned out wrong or harder:** the report's 400 words is not met by
  instruction alone; the owner left further tuning to Session 7's cycle.
- **Decisions written down nowhere else:** Session 6's synthetic inputs must not reuse the topics
  of `crux-types.md`'s examples (a boiler, a crossing guard, online choir rehearsals, an export
  module, a flat running route, local news, a bandstand and footpaths, library hours and books, a
  garden shed, a kitchen rota) or the thin slice's bakery, so the cases test the skill rather than
  its own examples.
- **Baseline** (ARCHITECTURE's table): `verify` green with 6 stages; 109 unit tests passed, 0
  skipped (35 in `test_check_skills.py`); `hygiene --all` green; 8 Python files; 2 skill folders,
  2 plugins, 2 marketplace entries; `claude` 2.1.328. Session 5 adds Python files under `evals/`
  and tests.
- **Not done:** installing from GitHub, for both skills, is not yet checked by a person
  (`docs/BACKLOG.md`).

## Watch for

- **Python 3.10 and the standard library only** under `evals/` (invariant 5).
- **Tests never touch the real `cases/` or `results/`,** which do not exist yet.
- **The eval runner is the exclusive resource:** one real run at a time, recorded in the
  done-note, nothing written to `results/`.
- **A `claude -p` run from inside this repository reads its `CLAUDE.md`,** and could read
  `gold.md` once cases exist: measure from an empty temporary folder.
- **`claude plugin marketplace add ./` registers this folder in the owner's user settings,** if
  the isolation measurement uses an install: remove it with `claude plugin marketplace remove
  faircat-skills` before the session ends.
