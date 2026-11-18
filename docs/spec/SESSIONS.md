# The session plan: round 1, a home for many skills

One block per session, in order, each run by *The session cycle* in
`docs/DEVELOPMENT-WORKFLOW.md`. The request and its resolved decisions are in `SPEC.md` beside
this file, with the draft in `PDD.md` and the itinerary audit in `REVIEW-2026-11-17.md`, all
read-only; do not re-litigate them. A session that finds its block wrong amends it and records
the reason in the block and in `docs/next-session-prompt.md`. Session 8 closes the round: it
deletes this file and the others in `docs/spec/`, and anything left open moves to
`docs/BACKLOG.md`.

Versions are per skill (`SPEC.md` decision 3): the column names the skill a session releases.

| Session | Scope | Decisions | Version |
|---|---|---|---|
| 1 | The scaffold: `verify` with `format`, `lint`, `tests` and `hygiene`; the hygiene stage; the itinerary skill's examples replaced (F1) | 5, 6, 12, 13, 14, 26–29; *Stack and pins*, *verify*, *The hygiene stage* | — |
| 2 | The restructure: the marketplace, the itinerary plugin, the `skills` and `plugins` stages (F2) | 1, 3, 10, 17, 18, 19, 28; *Layout and boundaries*, *The contract between the layers*, *Packaging* | travel-itinerary-builder **1.0.1** |
| 3 | The itinerary fixes: F3–F21 | 8, 9, 18 | travel-itinerary-builder **1.1.0** |
| 4 | crux-finder, the skill, with a thin slice to Claude Code and claude.ai (build order 1–2) | 1, 3, 10, 19, 21, 25; *crux-finder* | crux-finder **0.1.0** |
| 5 | The eval tooling: `run.py`, `checks.py` and their tests (build order 3) | 21, 22, 23; *The eval harness*, *The data layer* | — |
| 6 | The eval cases: ten inputs and the owner's ten gold files (build order 4–5) | 17, 21 | — |
| 7 | One eval cycle, then the claude.ai smoke test once the bars are met (build order 6–7) | 21, 22, 23 | crux-finder **0.2.0**, when the cycle changes the skill |
| 8 | READMEs, `ARCHITECTURE.md` read cold, the release, close the round (build order 8) | 11, 19, 20, 23, 29 | crux-finder **1.0.0**, tagged `crux-finder--v1.0.0` |

**The owner at the keyboard**, by session: approving the replacement examples (1); a by-hand
install check (2); choosing between rendered samples, and a by-hand run of the itinerary skill
(3); the claude.ai upload (4); writing or approving ten `gold.md` (6); reviewing 20 runs, then
three claude.ai chats (7); the tag and any push (8).

---

## 1: The scaffold

**Read:** `SPEC.md` decisions 5, 6, 12, 13, 14, 26–29; `REVIEW-2026-11-17.md` F1;
`ARCHITECTURE.md` invariant 9, *Stack and pins*, *Layout and boundaries*, *verify*, *The
hygiene stage*, *Testing strategy*; `DEVELOPMENT-WORKFLOW.md` *Day one* and *A clean
repository*; the port's source in the owner's public repository `FairCat-GD/krita-art-mcp`,
checked out at `~/Documents/GitHub Projects/krita-art-mcp`: `scripts/hygiene.py`,
`tests/test_hygiene.py`, and `scripts/verify.py` for its shape only.

- **The toolchain** (`ARCHITECTURE.md`, *Stack and pins*).
  - `pyproject.toml` for a repository that is not a Python package, with ruff and pytest in a
    development group, pinned; `uv.lock`; `.python-version` holding 3.10.
- **`verify`** (`ARCHITECTURE.md`, *verify*): `scripts/verify.py` with the stages `format`,
  `lint`, `tests` and `hygiene`, each failing on its own and runnable alone by name, then a
  summary; `--message <draft>` passes the draft to `hygiene`. The `skills` and `plugins` stages
  are Session 2's. Every tool a stage runs skips `.claude/worktrees/` at the root (*Day one*);
  pytest does not read `.gitignore`, so it is told.
- **The hygiene stage** (decision 13; `ARCHITECTURE.md`, *The hygiene stage*), from the design
  below.
  - **What the port covers:** the source checks the term list against files, paths and messages,
    and attribution in messages, with tokens split as the design says. It does not check secrets,
    conflict markers or `.env` files, has no routine scan, no full scan, no stamp and no `--all`,
    and fails on a hit in a pushed message, which the design forbids. Those parts are built here.
  - **Licence:** the owner, as the source's author, relicenses the ported file and its tests
    here under MIT (decision 13); no other licence header comes along.
- **The fixtures directory,** `tests/fixtures/`, with a term file of fictional words.
- **The itinerary skill's examples** (decision 14; F1): the seven lines replaced in place, in
  `travel-itinerary-builder/`, with the examples the owner approves. Nothing else in the skill
  changes, and no version is cut (decision 18).
- **Docs.**
  - `CLAUDE.md`: the Commands table, filled in.
  - `ARCHITECTURE.md`: the Built parts of *Stack and pins*, *Layout and boundaries*, *verify*,
    *The hygiene stage* and *Testing strategy*; invariant 9's *Enforced by*; the baseline.
  - README: a short *Developing* section saying how to run `verify` and where the docs are.
    Session 2 rewrites the rest.
- **Confirms** (*The documents*): *Stack and pins*; *verify*; *The hygiene stage*; *Testing
  strategy*; the first two bullets of *Deliberate decisions*.
- **Ask at the start of 1:** the city and the seven replacement lines. The session proposes a
  city and each line in the skill's voice, checked against the term list first, and writes
  nothing until the owner approves. *Recommended:* a city the skill already uses elsewhere in
  its examples, so the examples stay consistent.

### The hygiene stage's design

Copied verbatim from the kit's `KICKOFF.md`. What the stage checks and why is
`DEVELOPMENT-WORKFLOW.md`'s *A clean repository*; this is how it is built.

- **The terms come from `~/.config/hygiene/terms.txt`,** never from the repository, not even
  as hashes. A missing file fails the stage; an empty one passes. Tests point the stage at a
  fixture file of fictional terms, through a path argument or an environment variable, and
  never read the owner's file.
- **Each line is split into tokens:** runs of letters and digits in any script (an ASCII-only
  `[a-z0-9]+` misses a name written in Cyrillic), plus the camel-case words and digit groups
  inside each run, read before lowercasing, so a term in `myTermNotes` or `term2026` is still
  found. Terms and tokens alike are normalised to NFC and lowercased before they are compared,
  so a letter such as й matches however it was encoded.
- **A routine run reads what a commit could still change:** the path and contents of each path
  that differs from `HEAD` in the index or the working tree, both versions, since they can
  differ; untracked files that are not ignored, so a new file is checked before it is staged;
  the drafted commit message (`--message <file>`); the commits on no remote
  (`git log HEAD --not --remotes`, which is every commit when there is no remote): their
  messages, and the paths they changed as they stand at `HEAD`. Files containing NUL are
  skipped as binary, a path no longer in the tree is skipped, and submodule entries are
  skipped. A repository with no commits yet passes.
- **A full scan reads everything:** every tracked file and every untracked one that is not
  ignored, the staged contents of every path, every message reachable from `HEAD`, and the
  draft. It runs when `--all` is given, or when the stamp
  `"$(git rev-parse --git-common-dir)/hygiene-scanned"` is missing or older than the term list
  or the stage's own source. A new checkout writes the source anew, so the first run in a
  part's checkout may scan in full; the shared stamp then serves the rest. The stamp holds
  nothing: its modification time is the record. A hit in a file, in the draft or in a commit on
  no remote fails. A hit in a pushed commit does not fail, and the stage's output ends with a
  line of its own counting them. The stamp is renewed after a full scan that does not fail.
  Tests build scratch repositories and never read or touch the real stamp.
- **Attribution is checked in messages,** in the forms the workflow lists. The patterns name
  the tools, so "generated with the codegen script" passes.
- **Secrets have exact shapes,** each bounded by characters that cannot belong to it:
  - a private-key header: `-----BEGIN `, any words, then `PRIVATE KEY-----`;
  - an AWS access key id: `AKIA` or `ASIA`, then 16 capital letters or digits;
  - a GitHub token: `ghp_`, `gho_`, `ghu_`, `ghs_` or `ghr_`, then 36 letters or digits; or
    `github_pat_`, 22 letters or digits, `_`, then 59 more;
  - a Slack token: `xoxb-`, `xoxp-`, `xoxa-`, `xoxr-` or `xoxs-`, a group of digits, `-`, then
    more;
  - an Anthropic key: `sk-ant-`, a kind and two digits, `-`, then 80 or more letters, digits,
    `_` or `-`;
  - an OpenAI key: `sk-proj-`, `sk-svcacct-` or `sk-admin-`, then 40 or more letters, digits,
    `_` or `-`; or `sk-` and exactly 48 letters or digits;
  - a file named `.env` or `.env.<anything>` that a commit could record (tracked, staged, or
    untracked and not ignored), except `.env.example`, `.env.sample` and `.env.template`.

  A dry run over real repositories found two families of false alarms in looser shapes and none
  in these: a bare `sk-` inside hyphenated names, and a `github_pat_` prefix in test fixtures.
- **Conflict markers** are matched at the start of a line only, in the shapes the workflow
  gives.
- **It never holds what it bans.** The attribution patterns are assembled from pieces, so the
  stage's own source does not match them. Tests build their token-shaped strings and conflict
  markers from pieces at run time, so no file in the repository holds one.
- **A hit never prints the term or the secret.** It names the file and line, or the commit and
  message line.
- **What it cannot see** goes into `ARCHITECTURE.md`'s testing strategy: images and other
  binaries, their metadata included; a term joined to another word inside one lowercase run
  (matching every substring instead would flag ordinary words that contain a short term);
  attribution in files, which is checked only in messages, because a document stating this
  rule would match it; a home-directory path; and a secret of any shape not listed.
- **Each part is falsified once:**
  - a missing term file fails and an empty one passes;
  - a Cyrillic term is found, and so is the same term in NFD; `myTermNotes` and `term2026` are
    found;
  - a term or a co-author trailer in the drafted message fails; "generated with the codegen
    script" passes;
  - each secret shape and a tracked `.env` fail; `.env.example`, a hyphenated name containing
    `sk-` and a `github_pat_TEST` fixture pass;
  - a conflict marker fails; a heading underline passes;
  - a change left unstaged is read; a routine run reads a commit on no remote and skips a
    pushed one; a file committed without the stage, in a commit on no remote, is read;
  - a missing stamp, or a term list touched after it, turns a routine run into a full scan,
    and that scan still reads the draft; in a full scan, a hit in a pushed message passes and
    is counted on the last line, and a hit in a file fails and leaves the stamp as it was.

**Gates:**
- `uv run scripts/verify.py`, green, with these tests:
  - every item of the design's last bullet, *Each part is falsified once*;
  - the ported tests, passing against the completed stage.
- `uv run scripts/verify.py hygiene --all`, green once F1's lines are replaced, and red before
  (that is its falsification against the real list, printed as file and line only).
- Each stage falsified once: a formatting slip fails `format`, an unused import fails `lint`, a
  broken assertion fails `tests`, each at its own step and nowhere else.

**Watch for:**
- **Tests never read the owner's term list or the real stamp.** They point the stage at the
  fixture file and build scratch repositories, as the design says.
- **Nothing prints a term.** F1's lines are named by file and line in the done-note too.
- **The source's `verify.py` imports `tomllib`,** which needs Python 3.11; this repository runs
  on 3.10. Take its shape, not that import.
- **The candidate city's words** are checked against the term list before they are shown.
- **The first full scan reads the pushed commits too.** F1's word is in them; that is a counted
  hit on the last line, not a failure, and the done-note records the count for the owner.

**Done (2026-11-18; no version cut).**
- **Decided with the user:**
  - **The city and the seven lines** (*Ask at the start*): Lisbon, already the city of the
    skill's sightseeing and restaurant worked examples, with the seven lines as proposed. Every
    word was checked against the term list before it was shown, and every fact was checked on the
    web.
  - **The count of pushed hits:** the design as written (see *Amendments*).
  - **Confirms:** *Stack and pins*, *verify*, *The hygiene stage*, *Testing strategy* and the
    first two bullets of *Deliberate decisions*, each confirmed as built.
- **The toolchain.**
  - `.python-version` holds `3.10`, and `uv.lock` is committed.
  - `pyproject.toml` describes a repository that is not a package. ruff 0.17.5 and pytest 9.2.0
    are pinned exactly in `dev`. ruff checks only Python files and `pyproject.toml`. pytest
    reads `testpaths`, `pythonpath = ["scripts"]` and `--ignore=.claude/worktrees` from it.
- **`verify`.** `scripts/verify.py` runs the stages `format`, `lint`, `tests` and `hygiene`,
  each runnable alone and each run even after one fails, then a summary. `--message` and `--all`
  are passed to `hygiene`, and exit 2 without it. `tests/test_verify.py` covers this with
  `_call` replaced, so the tests run nothing real.
- **The hygiene stage.** `scripts/hygiene.py` is the port, completed from the design:
  - secrets, `.env` files and conflict markers;
  - the routine run and the full scan, with its stamp in the git common directory;
  - the pushed-history count on the full scan's last line.

  The choices made within the design are in ARCHITECTURE's *The hygiene stage*.
  `tests/test_hygiene.py` holds the 19 ported tests, changed only where the API changed
  (`check` became `scan(...).problems`), and 23 new ones. `tests/fixtures/terms.txt` holds the
  three fictional words the tests use.
- **F1.** The seven lines were replaced in place: `travel-itinerary-builder/SKILL.md:89`, `:138`
  and `:189`; `references/location-block-template.md:37` and `:55`;
  `references/research-playbook.md:61` and `:68`. A script found the listed word through the term
  list, so it was never written or printed. Nothing else in the skill changed, and no version was
  cut (decision 18).
- **Docs.**
  - `CLAUDE.md`: the Commands table, and rule 1 in the present tense.
  - `ARCHITECTURE.md`:
    - the Built parts of *Overview*, *Stack and pins*, *Layout and boundaries*, *verify*, *The
      hygiene stage*, *Testing strategy* and *travel-itinerary-builder*;
    - invariant 9's *Enforced by*;
    - the baseline.
  - The README's *Developing* section.
- **Amendments:**
  - **The first full scan counts 0 hits in pushed history.** The block's last *Watch for*
    expected F1's word to be a counted hit. But the design's full scan reads the messages of pushed
    commits, and the word is in none of the 5. It is only in file versions stored in 3 pushed
    commits, which no scan reads. Amended at plan time, with the user: the design is built as
    written, and "a file's earlier versions in history" joins the Hygiene row's *Cannot see*.
  - **ruff checks Python files only.** ruff 0.17's default `include` also formats the Python
    code blocks inside Markdown, and it would have rewritten one in the skill's
    `references/output-formats.md`. `include` is now `*.py` and `pyproject.toml`, so the skill
    ships as written. This was the session's own finding; the owner confirmed it with *Stack and
    pins*.
  - **`pyproject.toml` has `version = "0.0.0"`.** The plan preferred leaving the field out, but
    uv refuses a `[project]` table without one. Nothing reads it. This was the session's own
    finding.
- **Measured** (2026-11-18): uv 0.12.3, Python 3.10.20, ruff 0.17.5, pytest 9.2.0, git 2.50.1.
  A whole `verify` run takes 4.7 s, 4.4 s of it in `tests`. On this repository, `hygiene --all`
  was red with 7 hits before F1 (the 7 places above, each printed as file and line only). After
  F1 it was green, with 0 hits in pushed history, and wrote the stamp.
- **Falsified:**
  - Each stage at its own step: a formatting slip in `scripts/verify.py` failed `format` alone;
    an unused import in `tests/test_verify.py` failed `lint` alone; a broken assertion failed
    `tests` alone. The files were copied aside and back.
  - `hygiene --all` against the owner's list: red before F1's lines were replaced, green after.
  - The skip of `.claude/worktrees/`: a badly formatted file, a failing test and a conflict
    marker under `.claude/worktrees/probe/` left all four stages green. The same marker at the
    root failed `hygiene` alone. The probes were then deleted.
  - Eight mutations of the stage, one at a time, each caught by its own test:
    - secrets without bounds;
    - markers matched anywhere on a line;
    - no `.env` rule;
    - a stored version read even when it equals the working tree's;
    - a full scan that is not a superset;
    - an index version equal to HEAD's read;
    - a routine run reading pushed messages;
    - the stamp renewed with any list.

    Each item of the design's *Each part is falsified once* is a test that fails without its
    part.
- **Numbers:** 49 unit tests (+49): 42 in `test_hygiene.py` (19 ported, 23 new) and 7 in
  `test_verify.py`, with 0 skipped. 4 `verify` stages; 0 hits in pushed history; 4 Python files.
- **Review (`/code-review high`), 9 findings: 9 fixed and 0 skipped.** The user chose to fix all
  nine.
  - **A merge of pushed work failed the routine run on pushed content.** Each commit on no remote
    was compared with its first parent, so a local merge of pushed upstream work (a `git pull`
    with an unpushed commit) read the upstream files as unpushed. A merge now lists only the
    paths that differ from every parent (`--diff-merges=combined`), the content it made itself.
  - **One `git diff` per commit on no remote**, which meant every commit in a repository with no
    remote. One `git log` call now gives each such commit's message and paths.
  - **Line numbers came from `str.splitlines()`**, which also breaks on form feeds and Unicode
    separators, while attribution counted newlines. Every line is now counted at newlines
    only.
  - **The AWS key could match inside base64**, since its bound let lowercase letters, `+` and `/`
    sit beside it. It is now bounded by base64's alphabet too. This amends the design's letter
    ("bounded by characters that cannot belong to it") on the user's go-ahead, because a false
    alarm would block the gate for nothing.
  - **Working-tree files were read up to three times in one scan.** They are now read once, and
    `scan_stored` compares against that read.
  - **The routine run listed the unpushed commits twice and checked for commits twice.** Both
    now come from the one `git log` call, and `commit_messages` reads only the full history.
  - **Hygiene's skip of `.claude/worktrees/` rested on `.gitignore` alone.** The stage now skips
    paths under it at the root itself, and a test holds that.
  - **The baseline's "4 Python files under ruff" was ambiguous**, since ruff also lists
    `pyproject.toml`. The row now names `ruff format --check .`.
  - **`verify`'s message said "--message and --all is read".** It now reads "the hygiene stage
    reads …", and a test pins the exact output.
  - **Falsified:** four mutations each failed only their new test: a merge compared with its first
    parent; lines split by `splitlines()`; the AWS bound without base64; part checkouts read. A
    changed `verify` message failed its test.
  - **Numbers after the review:** 52 unit tests (+3): 45 in `test_hygiene.py`, 7 in
    `test_verify.py`, with 0 skipped. 4 stages; 0 hits in pushed history; 4 Python files.

---

## 2: The restructure

**Read:** `SPEC.md` decisions 1, 3, 10, 17, 18, 19, 25, 28, 29; `REVIEW-2026-11-17.md` F2;
`PDD.md` B, *Repo structure* and *Distribution*; `ARCHITECTURE.md` invariants 1–3 and 8,
*Context*, *Layout and boundaries*, *The contract between the layers*, *verify*,
*travel-itinerary-builder*, *Packaging*, *Deliberate decisions*.

- **The marketplace** (decisions 10, 17; *The contract between the layers*):
  `.claude-plugin/marketplace.json` named `faircat-skills`, owner `FairCat-GD`, a description,
  and one entry for `travel-itinerary-builder` with a relative source and no version.
- **The itinerary plugin** (decisions 1, 18, 28; F2).
  - `git mv travel-itinerary-builder plugins/travel-itinerary-builder/skills/travel-itinerary-builder`.
  - `plugins/travel-itinerary-builder/.claude-plugin/plugin.json`: name, version `1.0.1`,
    description, licence.
  - `SKILL.md` frontmatter: `version` removed; `license: MIT` and `metadata.version: "1.0.1"`
    added. The description does not change.
- **The `skills` and `plugins` stages** (`ARCHITECTURE.md`, *verify*), with the per-skill
  limits held in one table in the stage, which Session 4 extends.
- **The plugin's README and changelog:** `plugins/travel-itinerary-builder/README.md` (what it
  does, install per target) and `CHANGELOG.md` with `[1.0.0]` (as first published, 2026-07-22)
  and `[1.0.1]` (the packaging, the frontmatter and Session 1's examples).
- **The root README:** what the repository is, the skills with a line each and a link to their
  READMEs, installing from the marketplace, and the *Developing* section.
- **Docs.**
  - `CLAUDE.md`: the Commands table; the plugin layout in its opening paragraph.
  - `ARCHITECTURE.md`: the Built parts of every section in the Read line; invariants 1–3 and 8's
    *Enforced by*; the baseline.
- **Confirms:** *Overview*; *Context* (the `claude` CLI's `plugin validate`, the Agent Skills
  validator, GitHub); *Layout and boundaries*; *The contract between the layers*; *travel-itinerary-builder*
  (packaging and version); *Packaging*; the third bullet of *Deliberate decisions*.
- **Ask at the start of 2:** the display fields of `plugin.json` beyond the required ones.
  *Recommended:* `author` `FairCat-GD`, `homepage` the plugin's README on GitHub, no keywords.

**Gates:**
- `uv run scripts/verify.py`, green with all six stages, with each new check falsified once:
  - a top-level frontmatter field the specification does not allow fails `skills`;
  - a file under `references/` that `SKILL.md` does not link fails `skills`;
  - `metadata.version` unlike the plugin's version fails `skills`;
  - a plugin folder missing from the marketplace fails `plugins`;
  - an entry name unlike its manifest name fails `plugins`;
  - a published name missing (invariant 8) fails `plugins`.
- `claude plugin validate .` and `claude plugin validate plugins/travel-itinerary-builder` pass
  inside the `plugins` stage.
- **By hand:** `claude plugin marketplace add ./`, `claude plugin install
  travel-itinerary-builder@faircat-skills`, and `claude plugin details travel-itinerary-builder`
  lists the skill; then `claude plugin marketplace remove faircat-skills`, and the done-note
  records each output.

**Watch for:**
- **`claude plugin validate .` at the root does not open a plugin's skill files.** Validate each
  plugin directory too.
- **The Agent Skills validator needs Python 3.11 or newer,** and network when uv's cache is
  cold. It runs through `uvx`, pinned to a commit; the stage says plainly when it cannot fetch
  it, rather than passing.
- **The validator's own README calls it a demonstration.** Where it and the specification
  disagree, the specification wins: stop and ask.
- **Removing the local marketplace uninstalls its plugins.** It only removes this folder's
  registration; the owner's other installs are untouched.
- **Move with `git mv`,** so history follows the files.

**Done (2026-11-18, travel-itinerary-builder 1.0.1).**
- **Decided with the user:**
  - **The display fields of `plugin.json`** (*Ask at the start*): `author` and `homepage`, no
    keywords, as recommended, except that `author` is the owner's name rather than the handle.
    The name is not on the term list (checked by count only). This amends decision 27 (see
    *Amendments*).
  - **The descriptions:** the plugin's is the first sentence of its `SKILL.md` description; the
    marketplace's is the root README's first sentence.
  - **The by-hand install check:** run by the session, its outputs recorded below.
  - **Confirms:** *Overview*, *Context* (`claude plugin validate`, the validator, GitHub),
    *Layout and boundaries*, *The contract between the layers*, *travel-itinerary-builder*
    (packaging and version), *Packaging* and the third bullet of *Deliberate decisions*, each
    confirmed as built.
- **The marketplace.** `.claude-plugin/marketplace.json`: `faircat-skills`, owner `FairCat-GD`,
  its description under `metadata`, and one entry, `travel-itinerary-builder` with source
  `./plugins/travel-itinerary-builder`, no version and no description.
- **The itinerary plugin.**
  - The skill folder moved with `git mv` to
    `plugins/travel-itinerary-builder/skills/travel-itinerary-builder/`.
  - `plugins/travel-itinerary-builder/.claude-plugin/plugin.json`: `name`, `version` `1.0.1`,
    `description`, `author`, `homepage` and `license` `MIT`.
  - F2: `SKILL.md`'s frontmatter lost `version` and gained `license: MIT` and
    `metadata.version: "1.0.1"`; the description and every other line are unchanged. The
    frontmatter grew by two lines, so a `SKILL.md` line the review cites as `:N` is now `:N+2`.
- **The `skills` and `plugins` stages,** ahead of `format` in `STAGES`.
  - `skills`: the Agent Skills validator through `uvx --python ">=3.11"`, pinned to commit
    `83021e2be457a9b6679148719c1f6074f0ad975e`, on each skill folder, then
    `scripts/check_skills.py`: a skill folder exists; `SKILL.md` under `SPEC_LINES` or its row in
    `LINE_LIMITS` (empty); every file under `references/` linked from `SKILL.md`, and every path
    it names present; `metadata.version` equal to the plugin's.
  - `plugins`: `claude plugin validate --strict` on `.` and on each plugin, then
    `scripts/check_plugins.py`: the marketplace's name; each entry's source, absent version, and
    name agreeing with its manifest and folder; one skill folder per plugin, of its name; every
    plugin folder listed; every name in `PUBLISHED` present.
  - Every command `verify` runs now has stdin closed.
  - The choices made within the design are in ARCHITECTURE's *verify*.
- **Tests:** `tests/test_check_skills.py` (23) and `tests/test_check_plugins.py` (17), on
  fictional plugin trees in a temporary folder; `tests/test_verify.py` (+3): the two stages'
  commands, the validator's pin, and stdin closed. Its order test lists six stages.
- **Docs.**
  - The plugin's `README.md` (what it does, how it starts, install per target) and
    `CHANGELOG.md` (`[1.0.1]` and `[1.0.0]`, as first published; the `[1.0.1]` link waits for
    the commit's sha).
  - The root README: the skill linked to its plugin README, an *Installing* section, and
    *Developing* for six stages.
  - `CLAUDE.md`: the plugin layout, rule 1 in the present, the published name, the Commands
    table.
  - `ARCHITECTURE.md`: the Built parts of the sections in the Read line, *Stack and pins* and
    *Testing strategy*; invariants 1–3 and 8's *Enforced by*; the display fields under Decided,
    with a *Decision log* line; the baseline.
  - `SPEC.md`: decision 27's amendment. `docs/BACKLOG.md`: installing from GitHub.
- **Amendments:**
  - **`author` is the owner's name, not the handle.** The owner's answer at the start; recorded
    as an **Amended 2026-11-18 by the user** note on decision 27, and in `CLAUDE.md`.
  - **The stages check more than the block lists:** a reference `SKILL.md` names but that is
    missing; an entry's source and that it sets no version; a plugin's folder name and its one
    skill folder. Each holds a Decided rule (*Layout and boundaries*, *The contract between the
    layers*, invariant 2). Amended at plan time, with the user.
  - **`claude plugin validate` runs with `--strict`,** so its warnings fail too. Amended at plan
    time, with the user.
  - **The marketplace's description sits under `metadata`,** where the CLI's schema puts it;
    `--strict` accepts it there. The session's own finding.
- **Measured** (2026-11-18, `claude` 2.1.326, uv 0.12.3, the validator at `83021e2` on Python
  3.12.13):
  - `verify` whole takes about 6 s with uv's cache warm: `skills` 0.2 s, `plugins` 1.2 s,
    `tests` 4.3 s. The first `skills` run fetched and built the validator in 3.1 s.
  - With uv's cache warm, `skills` passes offline (`UV_OFFLINE=1`).
  - `claude plugin validate --strict` passes both manifests. On the plugin it prints a
    plugin-directory warning (no icon) and, before the root README had an install line, advice
    to add one; neither changes its verdict. At the root it passed an entry named unlike its
    manifest; only `check_plugins.py` caught that.
- **Checked by hand** (stdin closed, from the root):
  - `claude plugin marketplace add ./`: "Successfully added marketplace: faircat-skills
    (declared in user settings)".
  - `claude plugin install travel-itinerary-builder@faircat-skills`: "Successfully installed
    plugin: travel-itinerary-builder@faircat-skills (scope: user)".
  - `claude plugin details travel-itinerary-builder`: `travel-itinerary-builder 1.0.1`, the
    description, and Skills (1) `travel-itinerary-builder`, with no agents, hooks, MCP or LSP
    servers; about 227 tokens always on and 7.2k when invoked.
  - `claude plugin marketplace remove faircat-skills`: removed, and "Also uninstalled 1 plugin
    from this marketplace". Afterwards neither `claude plugin marketplace list` nor
    `claude plugin list` shows either.
  - Installing from GitHub waits for the push: in `docs/BACKLOG.md`.
- **Falsified:**
  - Each break at its own stage, run through the whole `verify`, with the file copied aside and
    back:
    - a `version` field in the frontmatter failed `skills` alone, from the validator;
    - a new file under `references/` failed `skills` alone;
    - `plugin.json` at `1.0.2` failed `skills` alone;
    - an empty `plugins/probe/` failed `plugins` alone, from the CLI and the check;
    - the entry named `travel-itinerary` failed `plugins` alone, as a name mismatch and a
      published name missing;
    - the marketplace named `faircat-skill` failed `plugins` alone.
  - The validator on an empty uv cache with no network (`UV_OFFLINE=1`, a scratch
    `UV_CACHE_DIR`) failed `skills`, with uv's error naming the fetch it could not make.
  - Eighteen mutations of the new code, one at a time, each failing its own unit test: every
    check in the two scripts turned off or loosened, the line count by `splitlines()`, the
    fragment kept on a path, stdin left open, and the stages' order swapped. The first run
    missed one, a mutant the metadata test could not tell apart; the test now holds another
    field's map, and a sharper mutant fails it.
- **Numbers:** 95 unit tests (+43): 45 in `test_hygiene.py`, 23 in `test_check_skills.py`, 17
  in `test_check_plugins.py`, 10 in `test_verify.py`, with 0 skipped. 6 `verify` stages (+2); 8
  Python files (+4); 1 skill folder, 1 plugin; 0 hits in pushed history.
- **Review (`/code-review high`), 9 findings: 9 fixed and 0 skipped.** The user chose to fix all
  nine. None touched the skill's shipped files, so 1.0.1's changelog entry is unchanged.
  - **A `references/` inside a URL or a longer word counted as a named reference,** and failed
    as missing. A path now counts only at the start of a word or after `./`.
  - **Two marketplace entries with one name or one source passed.** `check_plugins.py` now fails
    them.
  - **A blank line inside the `metadata:` block ended it,** so a valid version read as missing.
    Blank lines are now skipped.
  - **The two stages disagreed on dot folders:** `skills` found them, `plugins` did not.
    Discovery now lives in `check_plugins.py` alone, and `check_skills.py` imports it.
  - **A `LINE_LIMITS` row above 500 lifted the specification's limit.** The limit is now the
    lower of the two.
  - **`[1.0.1]` had no link reference** in the plugin's changelog. It now links this session's
    commit.
  - **`--strict` ties the gate to the unpinned CLI's warnings.** `--strict` stays; the `plugins`
    stage now prints `claude --version` first, so a failure a CLI release brings is told apart,
    and `CLAUDE.md`'s *Watch for* says what to do.
  - **ARCHITECTURE said the two stages read only `.claude-plugin/` and `plugins/`.** It now
    names the README the CLI reads for its advice.
  - **The 500-line test hard-coded the fixture's line count.** It now counts the fixture, and
    also covers a row above 500.
  - **Falsified:** seven mutations, each undoing one fix, each failed its own new test: the
    reference pattern without its boundary, and without its `./` case; blank lines ending the
    block; discovery by glob again; the limit without `min`; duplicates allowed; the stage
    without `claude --version`.
  - **Numbers after the review:** 102 unit tests (+7): 45 in `test_hygiene.py`, 28 in
    `test_check_skills.py`, 19 in `test_check_plugins.py`, 10 in `test_verify.py`, with 0
    skipped. 6 stages; 8 Python files; 0 hits in pushed history.

---

## 3: The itinerary fixes

**Read:** `SPEC.md` decisions 8, 9, 18; `REVIEW-2026-11-17.md` in full; `ARCHITECTURE.md`
*Context*, *travel-itinerary-builder*; the skill's five files.

- **Contradictions and small bugs** (decision 8): F3, F12–F15, F18–F21, each as its *Remedy*
  says or as the owner settles at the start.
- **The open behaviours,** settled at the start: F4 (food picks declined), F16 (the embassy
  line), F17 (appendix letters).
- **Environment assumptions** (decision 9): F5–F10, each with what the skill does where the
  capability is missing; the minimum environment in the `compatibility` field.
- **Phone readability** (F11), from rendered samples.
- **Docs.**
  - The plugin's `CHANGELOG.md` `[1.1.0]`; its README: the targets and the minimum environment.
  - `ARCHITECTURE.md`: *travel-itinerary-builder*'s Built part; the baseline if a count moved.
  - `docs/BACKLOG.md`: under *Not yet checked by hand*, each target the session could not run.
- **Confirms:** *travel-itinerary-builder* (its targets and minimum environment).
- **Ask at the start of 3:**
  - **The PDF tooling on this machine.** WeasyPrint, Pango and `pdftoppm` are absent, so
    nothing renders. *Recommended:* the owner approves installing Pango and Poppler with
    Homebrew and WeasyPrint in an isolated uv environment, for this session's samples only.
  - **A4 or a phone-sized page** (F11), from samples of each. *Recommended:* whichever passes the
    reference's own reading check; A4 if both do, since it also prints.
  - **Food picks declined** (F4). *Recommended:* no Appendix A and no restaurant research.
  - **The embassy line** (F16). *Recommended:* drop it, and say in one line to look up one's
    own embassy.
  - **Appendix letters** (F17). *Recommended:* fixed letters, an omitted one skipped, so
    cross-references hold.
  - **The fallbacks** (F5–F10). *Recommended:* the interview's options asked in plain chat,
    numbered, where the question tool is absent; the chat format where the PDF cannot be
    built; the file saved in the working folder and its path given; the weekday checked with a
    portable command or by counting.
  - **The minimum environment** for `compatibility` (the skill needs web search, and code
    execution for the PDF). *Recommended:* "Needs web search; builds the PDF where it can run
    Python, and delivers in chat otherwise."

**Gates:**
- `uv run scripts/verify.py`, green; `SKILL.md` still under 500 lines.
- A sample PDF rendered from the corrected skeleton, its pages looked at, and its fonts shown to
  load (F3's falsification is the uncorrected skeleton, which does not).
- **By hand:** the owner runs the skill once end to end in a fresh chat, and the done-note
  records the outcome; a target not run goes to the backlog.

**Watch for:**
- **One rule, three places** (`REVIEW-2026-11-17.md` §4): F4 and F5 each touch three.
- **Installing the PDF tooling changes the owner's system.** Only with their yes, and only what
  they approve.
- **The description changes only with the owner's yes;** it decides when the skill triggers.
- **No scripts are added to the skill** without the owner's yes.

---

## 4: crux-finder, the skill

**Read:** `SPEC.md` decisions 1, 3, 10, 19, 21, 25, 28; `PDD.md` B, *Scope*, *Inputs*,
*Repo structure*, *Procedure*, *Output format*, *Guardrails*, *Distribution*, *Build order*;
`ARCHITECTURE.md` invariants 2–4, *Context*, *The contract between the layers*, *crux-finder*,
*Packaging*.

- **The skill** (PDD B, *Repo structure*, *Procedure*, *Output format*, *Guardrails*):
  `plugins/crux-finder/skills/crux-finder/SKILL.md` with PDD B's frontmatter plus
  `metadata.version: "0.1.0"`, under 300 lines; `references/procedure.md`, `crux-types.md` (two
  fictional examples per type) and `output-template.md`.
- **The plugin:** `plugins/crux-finder/.claude-plugin/plugin.json` at `0.1.0`, its entry in the
  marketplace, its `CHANGELOG.md` `[0.1.0]`.
- **The `skills` stage's crux-finder row:** under 300 lines, and no `scripts/` folder
  (invariant 4).
- **The published names** (invariant 8): `crux-finder` added to the `plugins` stage's list.
- **The thin slice** (PDD B, *Build order* 2; decision 25):
  - first, one headless run, `claude -p` with `--plugin-dir` and the plugin's absolute path,
    started from an empty temporary folder before anything is installed, so it loads only that
    copy and not this repository's `CLAUDE.md`;
  - then `claude plugin marketplace add ./`, `claude plugin install crux-finder@faircat-skills`,
    and one run on the same hand-written input in a fresh session;
  - the owner zips `plugins/crux-finder/skills/crux-finder/`, uploads it to claude.ai as a
    custom skill and runs it once on the same input.

  No output is committed; the done-note records what each run showed. The marketplace
  registration is removed at the end.
- **The root README:** crux-finder listed, marked as in development.
- **Docs.**
  - `ARCHITECTURE.md`: *crux-finder*'s Built part, *Packaging*'s claude.ai zip, invariant 4's
    *Enforced by*, the baseline.
- **Confirms:** *crux-finder*; *Context* (`claude -p`, claude.ai); *Packaging* (the claude.ai
  zip).
- **Ask at the start of 4:** the hand-written input. *Recommended:* the session drafts a short
  fictional two-position text and the owner approves it. It is not an eval case and goes nowhere
  under `evals/`.

**Gates:**
- `uv run scripts/verify.py`, green, with the crux-finder row falsified: 300 lines fail, and a
  `scripts/` folder fails.
- `claude plugin details crux-finder` lists the skill; the headless run returns a report in the
  template's shape; the owner's claude.ai run triggers the skill.
- `claude plugin marketplace list` no longer shows `faircat-skills` at the end.

**Watch for:**
- **The description is PDD B's, word for word.**
- **The examples in `crux-types.md` follow the guardrails too:** no verdict, nothing about
  either party as a person, and fictional.
- **The report's rules are instructions here, not checks.** `checks.py` is Session 5's.

---

## 5: The eval tooling

**Read:** `SPEC.md` decisions 21, 22, 23; `PDD.md` B, *Evals* in full; `ARCHITECTURE.md`
invariants 5–7, *Context* (the `claude` CLI), *The data layer*, *The eval harness*.

- **The runner** (PDD B, *Runner*): `evals/crux-finder/run.py --runs N`, one fresh session per
  case per run, prompt the contents of `input.md`, output to `results/<id>/run-N.md`, never
  opening `gold.md`, isolated as settled at the start.
- **The checks** (PDD B, *Deterministic checks*): `evals/crux-finder/checks.py`, with quotes,
  symmetry, length, gold order, `approved_by`, and the summary table of `review.md` against the
  pass bars, as settled at the start.
- **Tests** of both, in `tests/`, on fictional fixtures.
- **Docs.**
  - `CLAUDE.md`: the two commands; the eval runner as the exclusive resource.
  - `ARCHITECTURE.md`: *The eval harness* and *The data layer*'s Built parts, invariants 5–7's
    *Enforced by*, the baseline.
- **Confirms:** *The eval harness*; *The data layer*; the fourth bullet of *Deliberate
  decisions*.
- **Ask at the start of 5:**
  - **How runs are isolated.** A session started in this repository loads its `CLAUDE.md`, the
    owner's settings, plugins and memory, and could read `gold.md`. The session first measures
    what a run loads under each option: `run.py` started from an empty temporary folder with the
    plugin's absolute path and no project or user settings, or the CLI's own
    `claude plugin eval`, which uses its own case format. *Recommended:* `run.py` as PDD B has
    it, isolated, if the measurement shows nothing else loads.
  - **The model.** *Recommended:* named in `run.py` and written at the head of every result, so
    the cycles compare.
  - **What a "quoted span" is.** The template's blockquoted crux sentence and the label
    "reconstructed by A" are not in any input. *Recommended:* text in quotation marks, with the
    crux blockquote and the template's fixed labels exempt.
  - **Where three bars are recorded.** Stability, "gate fires" and "no conflict" have no field
    in `review.md`. *Recommended:* add `same_crux_as_run_1`, `gate_fired` and
    `no_conflict_reported`, which amends PDD B, *Review*.
  - **An output that is a question, not a report.** *Recommended:* symmetry and length apply
    only to a report; a question is judged by `gate_fired`.

**Gates:**
- `uv run scripts/verify.py`, green, with these tests:
  - each deterministic check fails on a fixture built to break it, and passes on one that holds;
  - `run.py`, with a stub in place of `claude`, writes each `run-N.md` and never opens
    `gold.md`;
  - nothing under `evals/` imports outside the standard library (invariant 5).
- The isolation measured with one real run, recorded in the done-note; nothing written to
  `results/`.

**Watch for:**
- **Python 3.10 and the standard library only** under `evals/`.
- **Tests never touch the real `cases/` or `results/`.**
- **The eval runner is the exclusive resource:** one run at a time.

---

## 6: The eval cases

**Read:** `SPEC.md` decisions 17, 21; `PDD.md` B, *Inputs*, *Guardrails*, *Evals* (*Cases*);
`ARCHITECTURE.md` invariant 7, *The data layer*; `DEVELOPMENT-WORKFLOW.md` *A clean repository*.

- **Eight synthetic inputs** (PDD B, *Cases*): drafted by the session, fictional, one per row of
  the synthetic set, each approved by the owner.
- **Two real inputs:** a public-domain debate excerpt with `source:` and
  `license: public-domain`; a dispute the owner writes up, anonymized, with
  `license: maintainer-authored`.
- **Ten `gold.md`,** each written or approved by the owner, with `crux`, `type`, `crux_for` and
  `approved_by: FairCat-GD`, all committed before any file under `results/` exists.
- **Docs.** `ARCHITECTURE.md`: *The data layer*'s Built part (the cases as committed).
- **Confirms:** none.
- **Ask at the start of 6:**
  - **The public-domain excerpt.** *Recommended:* a passage from the 1858 Lincoln–Douglas
    debates where both speakers argue one point, chosen with the owner.
  - **The owner's dispute.** Written by the owner alone, it is one party's account of both,
    which PDD B, *Inputs* treats as one-sided. *Recommended:* the owner writes each side as that
    side put it, labelled A and B, with every name and place removed.
  - **The one-sided case's gold, and how it counts.** A single-turn run returns a question, not a
    report. *Recommended:* its gold records the expected crux had B's words been given and that
    the gate must fire; a run whose gate fires counts as a match for crux and type.

**Gates:**
- `uv run scripts/verify.py`, green; `checks.py`'s gold-order and `approved_by` checks pass on the
  commit; no file under `evals/crux-finder/results/`.

**Watch for:**
- **The session never writes a `gold.md` the owner has not approved.**
- **A real transcript may contain a word on the term list.** The hygiene stage catches it; ask
  the owner, never trim the quote silently.
- **The inputs are quoted verbatim by the reports,** so their text is final once gold exists.

---

## 7: The eval cycle and the smoke test

**Read:** `SPEC.md` decisions 21, 22, 23; `PDD.md` B, *Runner*, *claude.ai smoke test*,
*Review*, *Deterministic checks*, *Pass bars*; `ARCHITECTURE.md` *crux-finder*, *The eval
harness*; the done-notes of Sessions 5 and 6.

- **One cycle** (decision 22): `run.py --runs 2` over the ten cases; `checks.py`; the owner
  reviews every run into `review.md`; the summary table against the pass bars.
- **A bar missed:** the skill is changed for what the reviews show, crux-finder `0.2.0` is cut,
  the results are recorded, and the next cycle is inserted as 7a with the owner.
- **Every bar met, with the skill as it stands:** the claude.ai smoke test (PDD B, *claude.ai
  smoke test*): the owner uploads the zip and runs the three cases, a fresh chat each; the
  outputs go to `results/<id>/claude-ai.md`, through the same checks and review. A smoke test
  that calls for a skill change is a missed bar.
- **Docs.** The plugin's `CHANGELOG.md`, when a version is cut; `ARCHITECTURE.md`'s
  *crux-finder* Built part, with the cycle's numbers.
- **Confirms:** none.
- **Ask at the start of 7:** whether a new cycle replaces the result files. *Recommended:* yes;
  git keeps each earlier cycle, and each done-note records its summary.

**Gates:**
- `uv run scripts/verify.py`, green.
- `checks.py`'s summary table, recorded in the done-note against every pass bar.

**Watch for:**
- **The owner records every judgement in `review.md`.** The session never fills `crux_match`,
  `type_match` or `people_statement` itself.
- **Bars count only from a cycle run on the skill as it stands** (decision 22).
- **Twenty real runs:** the eval runner is the exclusive resource, and the cost is the owner's.

---

## 8: The release and the round's close

**Read:** everything: `SPEC.md`, `PDD.md`, `REVIEW-2026-11-17.md` and this file;
`ARCHITECTURE.md` in full; `CLAUDE.md`; `DEVELOPMENT-WORKFLOW.md` *Rounds* (*Close*) and *Git*.

- **`plugins/crux-finder/README.md`** (decision 19): install per target, one example report
  taken verbatim from the results, the eval results table.
- **The root README:** crux-finder no longer marked in development.
- **crux-finder 1.0.0** (decisions 20, 23): the version fields and the changelog entry, only if
  decision 23's conditions hold.
- **The round's close:**
  - `docs/ARCHITECTURE.md`, read cold against the code: every Built part true, what the round
    did not build pointing at its backlog item, and the baseline current;
  - `CLAUDE.md` pointed at the plugin READMEs;
  - anything still open moved to `docs/BACKLOG.md`;
  - then, after its review, the separate `docs: close round 1` commit.
- **Confirms:** none.
- **Ask at the start of 8:** the tag `crux-finder--v1.0.0`, and any push, each on its own.

**Gates:**
- `uv run scripts/verify.py`, green.
- Decision 23's conditions, checked against git: no change to the skill's instructions or
  references since the last full cycle.

**Watch for:**
- **The example report's input** must be one of the committed cases, so nothing new is
  published.
- **The tag comes last,** after the review, the close and any approved push (*Git*).
