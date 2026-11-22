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
| 7a | The second eval cycle, on 0.2.0, then the claude.ai smoke test once the bars are met (inserted in Session 7) | 21, 22, 23 | crux-finder **0.3.0**, when the cycle changes the skill |
| 7b | The third eval cycle, on 0.3.0, then the claude.ai smoke test once the bars are met (inserted in Session 7a) | 21, 22, 23 | crux-finder **0.4.0**, when the cycle changes the skill |
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

**Done (2026-11-19, travel-itinerary-builder 1.1.0).**
- **Decided with the user:**
  - **The PDF tooling:** Homebrew's `pango` and `poppler`, and WeasyPrint only in throwaway uv
    environments, with nothing added to `pyproject.toml` or `uv.lock`. Both stay installed;
    removing them is the owner's call.
  - **F4, food declined:** Appendix A stays, against the block's recommendation. A No means no
    meals on the route (steps 15 and 16 skipped), and Appendix A lists 10–15 picks across every
    tier, each labelled, none flagged on-route.
  - **F16:** the embassy line is dropped, replaced by one line saying to look up one's own
    embassy or consulate. **F17:** letters are fixed, and an omitted appendix is skipped.
  - **F5–F10:** the fallbacks as recommended, with WeasyPrint, else chat; ReportLab leaves.
  - **`compatibility`:** the owner chose a fuller wording than the block's, naming WeasyPrint,
    Pango and the fonts' network.
  - **F11, the page:** **A4, in one column.** The owner first picked a 100 × 178 mm phone page
    from rendered samples, then asked that the PDF read as well on a laptop. Laptop renders of
    both showed the phone page as a narrow column and A4 small at fit-to-page but fine at
    fit-to-width, and the owner chose A4 only over two PDFs or a middle size. The reading check
    is reworded to what A4 gives: a laptop at fit-to-width, paper, and a phone by zooming into
    the single column.
  - **The by-hand run:** in Claude Code, from this folder's marketplace.
  - **Confirms:** *travel-itinerary-builder* (its targets and minimum environment), confirmed as
    built, with the `compatibility` wording, the A4 page and the fallback order added to its
    Decided part.
- **F3–F21,** in `plugins/travel-itinerary-builder/skills/travel-itinerary-builder/`:
  - F3: `@import` first in the skeleton, with a comment saying why. F10: font stacks with
    Georgia and Helvetica fallbacks, and a font check after rendering.
  - F4: one rule in `SKILL.md` steps 14, the research list and Appendix A, `output-formats.md`'s
    Appendix A and the playbook's Food heading.
  - F5: one home for saving and handing over, `SKILL.md` Phase 5 (the path, or the
    environment's own link, `computer://` in the desktop app); `output-formats.md` points at it.
    claude.ai's output location could not be confirmed on the web, so it is not named.
  - F6: `output-formats.md`'s *Building the PDF* order: already importable, a virtual
    environment, `--break-system-packages` only in a disposable sandbox, Pango asked for first
    (with the measured macOS library path), then chat with the reason.
  - F7: a Python one-liner, or a calendar found by search. F8: `pdftoppm`, else PyMuPDF, else
    the visual check reported as skipped. F9: the question tool named generically, the choice
    steps marked as such, and numbered options in chat without one.
  - F11: the reading check reworded for A4; the page and sizes unchanged.
  - F12: the snack template in local and home currency, and its worked example gains
    `(~$1.60)`, one of Session 1's approved lines. F13: Ramiro links to
    `https://www.cervejariaramiro.com/`, where both its domains redirect. F14: `(verify)`.
    F15: six appendices. F16: the embassy pointer under *Must include*. F17: the fixed-letters
    rule in `SKILL.md` and `output-formats.md`. F18: no emoji in the PDF. F19: the Wikipedia link
    on the name. F20: Booking kept for a walk-in. F21: no "Other" in the generic shopping set.
  - The frontmatter gains `compatibility`; `metadata.version` and `plugin.json` are `1.1.0`. The
    description is unchanged. `SKILL.md` has 286 lines (+6).
- **Docs.** The plugin's `CHANGELOG.md` `[1.1.0]` (its link reference waits for this commit's
  sha) and README (*What it does*, a new *What it needs* per target, the version);
  `ARCHITECTURE.md` (*travel-itinerary-builder* Decided and Built, *Packaging*, the baseline's
  date, a *Decision log* line); `docs/BACKLOG.md` (1.1.0 on the other targets, and the two
  fallbacks no run reached).
- **Amendments:**
  - **F4 keeps Appendix A,** and **`compatibility` has the owner's wording,** and **ReportLab
    leaves the fallback order:** amended at plan time, with the user.
  - **F11 is A4 with a reworded check,** not a phone page. The block's rule ("whichever passes
    the reference's own reading check") could not decide it: arithmetic and samples showed no
    page passes "≈11 pt effective" on a phone, which is larger than the phone's own text
    (about 8 pt). Decided mid-session by the user, from phone and laptop renders.
- **Measured** (2026-11-19, macOS, Homebrew `pango` 1.58.2 and `poppler` 26.11.0):
  - The skeleton as it was embedded Times New Roman and Verdana, with no warning; with `@import`
    first, Playfair Display and Inter. The final skeleton offline (fetch blocked by a dead
    proxy) built in 0.5 s with Georgia and Helvetica Neue, silently.
  - WeasyPrint 70.0 (uv, Python 3.12) and 66.0 (a venv on the system's Python 3.9) both failed
    to import without `DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib`, and imported with it.
  - `pdftoppm` and PyMuPDF both wrote page images; PyMuPDF also listed the fonts. `date -d`
    fails on macOS (`illegal option -- d`); the Python one-liner gives Monday for 2026-05-18.
  - On a 1179 px-wide (about 65 mm) phone screen at full width, A4's 10 pt body shows at about
    3 pt; a 100 × 178 mm page's 12 pt body at about 7.8 pt.
- **Checked by hand:**
  - `claude plugin marketplace add ./`, `claude plugin install
    travel-itinerary-builder@faircat-skills` and `claude plugin details`:
    `travel-itinerary-builder 1.1.0`, Skills (1). Then `claude plugin marketplace remove
    faircat-skills`; neither list shows it afterwards.
  - **The owner's run,** in a fresh Claude Code session in an empty folder, started as
    `/travel-itinerary-builder:travel-itinerary-builder`: a six-day plan for a city without
    exact dates, delivered as a 30-page A4 PDF by WeasyPrint 66.0. Inter and Playfair Display
    embedded; no missing glyphs; the winter accent; days headed by their best weekdays; seasonal
    averages labelled as such; all six appendices; the embassy pointer; `(verify)` the one
    spelling. The owner reviewed it and approved shipping. Blocks kept whole leave some pages
    part-empty, one holding a single spilled line; left as it is.
  - Not run: Codex, claude.ai, other agents, and the two chat fallbacks
    (`docs/BACKLOG.md`).
- **Falsified:** F3, the block's gate: the skeleton as it was rendered without its fonts, and
  the corrected one with them, shown by `pdffonts`. No check was added to `verify`.
- **Numbers:** 102 unit tests (±0), 0 skipped; 6 `verify` stages; 8 Python files; 1 skill
  folder, 1 plugin; 0 hits in pushed history at the last full scan.
- **Review (`/code-review high`), 7 findings: 7 fixed and 0 skipped.** The user chose to fix
  all seven, then commit and push. They join 1.1.0's changelog entry.
  - **The build order asked to install Pango before trying the macOS library path,** so a Mac
    that already had it would be asked again. The path is now tried first.
  - **The virtual environment went in the user's working folder,** often their own repository.
    It now goes in a temporary folder, or uv's cache.
  - **`[1.1.0]` had no link reference.** It now links the session commit.
  - **The skeleton loaded no italic styles,** so the design's italics were synthesized
    obliques. The `@import` now adds Playfair Display italic 400 and Inter italic 400 and 600.
  - **After a No to food picks, no day pointed to Appendix A.** Each day now ends with a one-line
    pointer to it.
  - **Two lines still promised the PDF lived well on a phone,** against the A4 reading check.
    Both now say laptop, paper, and a phone by zooming. The description, which says
    "mobile-friendly", is unchanged: it changes only with the owner's yes.
  - **The README told Codex users to turn on web search,** which is on by default with cached
    results. It now says `"live"` gives current hours and forecasts.
  - **Falsified:** the skeleton before the fix, rendered with italic text, embedded
    `Inter-Oblique` and `Playfair-Display-Bold-Oblique`; after it, `Inter-Italic`,
    `Inter-Semi-Bold-Italic` and `Playfair-Display-Italic`. No check was added to `verify`.
  - **Numbers after the review:** unchanged: 102 unit tests, 0 skipped; 6 stages; 8 Python
    files.

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

**Done (2026-11-20, crux-finder 0.1.0).**
- **Decided with the user:**
  - **The hand-written input:** the session's draft, approved as written: two co-owners of a
    bakery on opening on Sundays, labelled A and B. It stayed in a temporary folder; nothing of
    it is in the repository.
  - **Party labels** (PDD B's template left it open): A and B throughout; named parties get their
    name or role in brackets on the two steelman lines.
  - **No conflict** (step 9's shape): every heading stays; *The crux* reads **No crux** with one
    neutral sentence; an empty section says `None.`
  - **The root README:** a **Reasoning** heading, crux-finder marked *(in development)*.
  - **Mid-session, after the first headless run ran 547 words with unbalanced steelmen:** a check
    before sending (steelmen, length, quotations); after the second ran 564, one sentence per
    crux field and nothing after Confidence; then one last run, with further length tuning left
    to Session 7.
  - **Confirms:** *crux-finder*, *Context* (`claude -p`, claude.ai) and *Packaging* (the claude.ai
    zip), each confirmed as built, with the three settlements above added to *crux-finder*'s
    Decided part.
- **The skill,** `plugins/crux-finder/skills/crux-finder/`: `SKILL.md` (135 lines) with PDD B's
  frontmatter, description word for word, `license: MIT` and `metadata.version: "0.1.0"`; the
  Inputs table and labels, steps 1–9 in brief, the report's rules and the check before sending,
  the seven guardrails. `references/procedure.md` (each step in full), `crux-types.md` (the five
  types, the order to test them, tie-breaks, two fictional examples each, parties as roles) and
  `output-template.md` (PDD B's template verbatim and its variants).
- **The plugin:** `plugin.json` at 0.1.0 in the itinerary plugin's pattern, its description the
  first sentence of the skill's; the marketplace's second entry; `CHANGELOG.md` `[0.1.0]` (its
  link reference waits for this commit's sha); a `README.md` with *What it does*, *Using it*,
  *What it needs*, *Installing* and *Version*, which Session 8 completes with the example report
  and the eval table.
- **The checks:** `scripts/check_skills.py`'s `LINE_LIMITS` became `LIMITS`, one table of
  `Limits(lines, scripts)` rows, whose one row, crux-finder's, is `Limits(lines=300,
  scripts=False)`; a `scripts/` folder fails where a row forbids it. `crux-finder` is in
  `PUBLISHED`. Three new tests, two moved to `LIMITS`.
- **Docs:** the root README; `ARCHITECTURE.md` (*Overview*, *Context*, *Layout*, invariant 4's
  *Enforced by*, *The contract*, *verify*, *crux-finder* Decided and Built, *Packaging*, the
  baseline, a *Decision log* line); `docs/BACKLOG.md` (crux-finder in the install from GitHub).
- **Amendments:**
  - **The plugin has a README now,** not only in Session 8: the layout requires one, and its
    `homepage` and the root README link to it. The block's intent held; it named no README.
  - **The skill changed after the thin slice's first run,** with the user, for the report's
    length and balance (above).
- **Measured** (`claude` 2.1.328; the model each run reported was claude-opus-5-5):
  - **Headless,** from an empty folder in a temporary directory with no `CLAUDE.md` above it,
    `claude -p` with `--plugin-dir` and `--output-format stream-json --verbose`, stdin closed:
    each run called the Skill tool as `crux-finder:crux-finder` from the description alone, then
    read `output-template.md` and `crux-types.md` with one shell `cat` outside its folder, with
    no denial (the user's permission mode, `auto`); `procedure.md` was never read. The owner's
    user-level plugins and synced skills loaded too, and auto memory was on: Session 5's
    isolation question.
  - **The three headless runs,** in words (tokens with a letter or digit), steelmen A/B, label:
    547, 53/69, double crux · Predictive; 564 with a 60-word summary after Confidence, 56/61,
    double crux · Predictive; 515, 55/61, crux for A · Predictive, ending at Confidence. About
    $0.23 each.
  - **Installed:** `claude plugin marketplace add ./` ("declared in user settings"), `claude
    plugin install crux-finder@faircat-skills` (scope: user), `claude plugin details
    crux-finder`: `crux-finder 0.1.0`, Skills (1) `crux-finder`, about 94 tokens always on and
    2.3k on invoke. A run from another empty folder, without `--plugin-dir`, triggered
    `crux-finder:crux-finder`, loaded in place from this folder: 486 words, 53/65, crux for A ·
    Predictive, the template's six headings.
  - **Removed:** `claude plugin marketplace remove faircat-skills` removed it and uninstalled
    crux-finder; neither `marketplace list` nor `plugin list` shows either.
- **Checked by hand:** the owner asked the session to upload the zip; it was uploaded through
  the owner's browser to claude.ai's *Customize → Skills*, passed its security scan, and showed
  License MIT and Version 0.1.0. The owner ran the input in a fresh chat: the template's shape,
  **Double crux · Predictive**, 558 words, steelmen 58/66, nothing after Confidence. The upload
  then appeared in this Claude Code session as `anthropic-skills:crux-finder`; the owner chose to
  delete it after the run. Not run: Codex and other agents (`docs/BACKLOG.md`, *Deferred*).
- **Falsified,** each through the whole `verify`, the file copied aside and back:
  - `SKILL.md` padded to 300 lines failed `skills` alone, at `check_skills.py` ("300 lines; it
    must stay under 300"), with the validator still passing the folder;
  - a `scripts/probe.sh` in the skill folder failed `skills` alone, at `check_skills.py`.
- **Numbers:** 105 unit tests (+3), 0 skipped; 6 `verify` stages; 8 Python files (±0); 2 skill
  folders, 2 plugins, 2 marketplace entries (+1 each).
- **Review (`/code-review high`), 6 findings: 6 fixed and 0 skipped.** The user chose to fix all
  six, then commit and push. The skill's fixes join 0.1.0, which was not yet published.
  - **`SKILL.md` made A the party named first, even in a one-sided input,** where only
    `procedure.md` said A is the party whose own words you have; `SKILL.md` now says so too.
  - **`procedure.md` said to keep the input's own labels,** against "always A and B"; it now
    maps any labels to A and B.
  - **The README promised at most 400 words,** which no run met; it now says the report is meant
    to stay within 400 and often runs to about 500 in 0.1.0.
  - **`[0.1.0]` had no link reference;** it now links the session commit.
  - **`ARCHITECTURE.md` said the claude.ai run was seen to trigger by its description;** only its
    output was seen, and it now says so.
  - **The no-scripts rule caught only a folder named `scripts/`;** a `scripts=False` row now also
    fails any file but `SKILL.md` and Markdown under `references/`, so a script anywhere fails.
  - **Falsified:** a `run.sh` beside `SKILL.md` failed `skills` alone, at `check_skills.py`, through
    the whole `verify`. Four new tests (three cases of one, and a sound skill with a dotfile).
  - **Numbers after the review:** 109 unit tests (+4), 0 skipped; 6 stages; 8 Python files.
  - **Pushed** with the user's yes, with this commit.

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

**Done (2026-11-20, no version).**
- **Decided with the user** (each as recommended):
  - **Isolation:** `run.py` as PDD B has it, isolated, measured first.
  - **The synced claude.ai copy:** still synced at the start (`anthropic-skills:crux-finder`,
    0.1.0); the user asked the session to delete it and anything it left.
  - **The model:** `claude-opus-5-5`, named in `run.py` and written at the head of every result
    with the CLI's version, the skill's version and the commit.
  - **A quoted span:** text between double quotation marks, straight or curly, and any
    blockquote but the crux sentence's; matched with line breaks joined, curly and straight
    marks folded, an ellipsis piece by piece in order; single quotes are no span.
  - **The three bars' fields:** `same_crux_as_run_1`, `gate_fired`, `no_conflict_reported` in
    `review.md`; an output without `## Crux report` is a question, held to neither symmetry nor
    length and judged by `gate_fired`.
  - **Word rules:** a word is a token with a letter or digit; length at most 400, header and
    claim map left out; symmetry: the longer steelman at most 1.25 times the shorter.
  - **Gold order, strict:** fails a gold.md uncommitted, not committed before its results, or
    changed after results existed, committed or not.
  - **The prompt:** input.md's body, its frontmatter left out; quotes checked against it.
  - **Confirms:** *The eval harness*, *The data layer* and *Deliberate decisions*' fourth bullet,
    each confirmed as built, with the answers above in their Decided parts.
- **The runner,** `evals/crux-finder/run.py`: `--runs N [--case <id> …]`; every case read and
  the plugin's tree checked clean before anything is spent; each run a new temporary folder
  with an empty working directory and a copy of the plugin, `claude -p` with the measured flags
  and the prompt on stdin; the start event checked before anything is written; an existing
  result skipped; a failure writes nothing and stops. Never names gold.md.
- **The checks,** `evals/crux-finder/checks.py`: gold.md's fields and `approved_by`, the gold
  order from git, quotes, symmetry and length per output, `review.md`'s format and fields,
  completeness, then the summary table: PDD B's ten bars, the extra row below, and the smoke
  test apart. Exits 0 with no problem and no results yet or every bar met.
- **Tests:** `tests/test_crux_finder_run.py` (20; a stub `claude`, an audit hook on `open`,
  gold.md made unreadable), `tests/test_crux_finder_checks.py` (64; fictional outputs and temp
  git repositories), `tests/test_evals_stdlib.py` (2; invariant 5).
- **Docs:** `CLAUDE.md` (the two commands, the runner one run at a time, a *Watch for* line on
  claude.ai uploads syncing into Claude Code); `ARCHITECTURE.md` (*Overview*, *Context*,
  *Layout*, invariants 5–7's *Enforced by*, *The data layer* and *The eval harness* Decided and
  Built, *Testing strategy*, the baseline, a *Decision log* line).
- **Amendments:**
  - **PDD B, *Review*, gains three fields,** and **the prompt leaves out input.md's
    frontmatter,** where PDD B says the prompt is the file's contents: both settled at the start
    with the user.
  - **An eleventh row in the summary table,** "Runs on the skill as it stands" (decision 22),
    beyond PDD B's six checks: in the plan the user approved.
  - **`run.py` refuses while the plugin has uncommitted changes:** in the approved plan, so each
    result's `commit` holds the skill it ran.
- **Measured** (`claude` 2.1.329, up from the baseline's 2.1.328):
  - **The deletion:** claude.ai's *Customize → Skills → Yours* still listed crux-finder; the
    session removed it (claude.ai deletes it with its version history), and the next `claude`
    start dropped `anthropic-skills:crux-finder` and its folder under
    `~/.claude/skills/synced/`. No `faircat-skills` marketplace was registered and no zip was
    left from Session 4.
  - **What a run loads,** from the start event, ended before any model call. As Session 4 ran
    it: the plugin, the owner's two user-level plugins, a synced plugin, twelve synced skills, a
    claude.ai MCP server, the `auto` mode and memory paths. With `--setting-sources ""`,
    `--strict-mcp-config`, `--no-session-persistence`, `--permission-prompts none`,
    `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` and the plugin copied out: the copy and Claude Code's
    built-ins only, no MCP server, `default`, no memory paths. `--restricted`, `--safe-mode` and
    `--bare` were not needed.
  - **The canary** (one call, $0.10): with those flags and `--add-dir <copy>`, a fictional file
    beside the run's folder was denied to Read and to Bash alike, as needing approval no one can
    give; the skill's `output-template.md` in the copy was read.
  - **One real run** through `run.py`'s own code, on a fictional input (an allotment society's
    seed swap) in a temporary folder, nothing written under `evals/`: the header as designed,
    `skill_calls: crux-finder:crux-finder`, 0 denials, $0.17, 29 s; the template's shape,
    **Double crux · Value**, steelmen 66/64, no quotes, 472 words, so it fails the length bar as
    Session 4's runs did. The temporary folders were removed.
- **Falsified,** each through the whole `verify`, the file copied aside and back:
  - `run.py` made to read gold.md failed `tests` at `test_the_runner_never_opens_gold_md`;
  - an `import yaml` in a new file under `evals/` failed `tests` at the standard-library test;
    put into `checks.py` itself it failed lint and stopped the checks' tests at collection;
  - the quote matcher made to accept everything failed the five quote tests;
  - the symmetry ratio loosened to 1.5 failed four tests, the 53/69 cases among them;
  - the gold-order condition reversed failed the four gold-order tests on committed results.
- **Numbers:** 195 unit tests (+86), 0 skipped; 6 `verify` stages, about 25 s (from about 6 s);
  13 Python files (+5); 2 skill folders, 2 plugins, 2 marketplace entries (±0).
- **Review (`/code-review high`), 6 findings: 6 fixed and 0 skipped.** The user asked for every
  finding fixed, then a commit and a push.
  - **A blank line between the crux label and its sentence made the sentence a quote:** the label
    is now remembered across blank lines, and forgotten once a blockquote closes.
  - **A reply opening with a `---` rule was read as frontmatter,** emptied or cut: an output's
    leading block is a header only when it closes and holds `key: value` lines alone.
  - **`run.py` read the skill's version after the run was paid for,** and a bad `plugin.json`
    crashed it: it is read first, and a missing or unreadable version refuses with exit 2.
  - **An unreadable output crashed `checks.py`:** it is now a problem line.
  - **A comment in `run.py` named a session:** it now names only the CLI version measured.
  - **`gold_order` asked git about the same commit once per output:** once per commit now.
  - **Falsified,** each through the whole `verify`, the file copied aside and back: the label
    forgotten at a blank line again failed the blank-line test; `split_frontmatter` back in place
    of `output_parts` failed the leading-rule test; `_skill_version` returning a fixed value
    failed the header test and both refusal tests.
  - **Numbers after the review:** 203 unit tests (+8), 0 skipped; 6 stages; 13 Python files.
  - **Pushed** with the user's yes, with this commit.

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

**Done (2026-11-20, no version).**
- **Decided with the user** (each *Ask at the start* as recommended):
  - **The public-domain excerpt:** the first Lincoln–Douglas debate (Ottawa, 1858) on the
    "house divided": one unbroken passage per speaker, Douglas first.
  - **The owner's dispute:** each side as it was put, labelled A and B. Superseded mid-session
    (Amendments).
  - **The one-sided case's gold:** the crux and type expected had B's own words been given; the
    gate must fire, and a run that asks for B's words matches on crux and type.
  - **The no-conflict case's gold:** no crux, `type: none`, `crux_for: none`; only a **No crux**
    report matches, and a Framing crux meets PDD B's no-conflict bar but not crux or type.
  - **Every input** was approved by the user as drafted, and **every gold** as proposed: nine
    in one table, the tenth with its input.
- **The ten cases,** in `evals/crux-finder/cases/<id>/`, each `input.md` and `gold.md`:
  - eight synthetic, one per row of PDD B's synthetic set: `empirical-orchard-stall`,
    `empirical-studio-kiln`, `predictive-hall-solar`, `definitional-vintage-rail`,
    `value-theatre-season`, `framing-piano-lessons`, `one-sided-games-night`,
    `no-conflict-quiz-team`; about 150 to 210 words each, a one-line request, then A and B as
    roles;
  - `transcript-father-care`: a fictional message thread between two siblings, a Value crux
    (Amendments);
  - `real-lincoln-douglas`: Douglas's 591 words and Lincoln's 722, with `source:` and
    `license: public-domain`.
  - Each gold.md: the four fields on one line each, `approved_by: FairCat-GD`, and a short note
    for the review: the common ground that pins the crux, what else counts as a match, and the
    counting rules for the one-sided and no-conflict cases.
- **Docs:** `ARCHITECTURE.md` (*The data layer* Decided, two amendments, and Built, the cases as
  committed; *Overview*, *Layout* and *Testing strategy* lines; the baseline's `checks.py` row;
  a *Decision log* line); `docs/BACKLOG.md` (a second real case).
- **Amendments:**
  - **The real set holds one case, where the block and PDD B have two:** the user had no dispute
    of their own to write up and asked the session to write a serious one. Being fictional, it
    is a synthetic case, `transcript-father-care`, with no `license:`, rather than one labelled
    `maintainer-authored`; it is the set's only transcript. Added mid-session by the user; a
    second real case is in `docs/BACKLOG.md`.
  - **The excerpt is longer than planned** (591 and 722 words, against about 300 to 450 each):
    the page runs Douglas's paragraphs together and Lincoln's answer is one paragraph, so a
    shorter cut would start or stop mid-argument. Approved by the user with the input.
- **Measured:**
  - **The excerpt's source:** the National Park Service's Ottawa transcript, read with the
    standard library's HTML parser and cut by a script, so the text is the page's character for
    character, its typos ("The knew", "shall became") kept. Douglas's cut ends just before the
    paragraph-run that turns to citizenship, so his most openly racist passage is left out; the
    era's terms in what remains stay as published.
  - **The ids reach no run:** `run.py` sends the body alone, from a temporary folder of a fixed
    name, so an id that names its type biases nothing.
  - **gold.md as `checks.py` reads it:** every gold's four fields through its own `fields()`.
    A value quoted whole in single quotes keeps a doubled apostrophe, since nothing unescapes
    it, so the vintage case's crux, holding both kinds of quotation mark, is left unquoted.
- **Falsified:** no new check. `checks.py`'s gold order on the real cases: before the commit it
  reported each of the ten gold.md `not committed` and exited 1; in a scratch clone with the
  cases committed it reported `10 case(s), 0 problem(s); no results yet` and exited 0.
- **Numbers:** 203 unit tests (±0), 0 skipped; 6 `verify` stages; 13 Python files (±0); 2 skill
  folders, 2 plugins, 2 marketplace entries (±0); 10 cases (+10); no `results/`.
- **Review (`/code-review high`), 3 findings: 3 fixed and 0 skipped.** Each fixed before any
  result exists, so the gold order still holds; the user chose the first two.
  - **`real-lincoln-douglas`'s gold named a premise, not the deepest crux:** it is now whether
    slavery is one of the local differences that bind the Union or a cause of division, the
    point Lincoln's reply turns on, Empirical, both; the founders' policy, the old crux, still
    counts as a match.
  - **The excerpt's request line named the "house divided" speech,** steering a run toward
    whether the Union can endure divided, which the gold counts as a miss: it now names only
    the debate, the date, and who spoke first. The passages are unchanged.
  - **`ARCHITECTURE.md` named the ids `<set or type>-<topic>`,** which `transcript-father-care`
    is not: it now lists each pattern.
  - **Falsified:** no new check.
  - **Numbers after the review:** unchanged; `checks.py` 10 cases, 0 problems, no results.

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

**Done (2026-11-22, 0.2.0).**
- **Decided with the user:**
  - **A new cycle replaces the result files** (the block's Ask), as recommended: git keeps each
    earlier cycle, and each done-note its summary table.
  - **The review:** case by case in chat, the owner answering every field and the session
    writing the answers verbatim; changed mid-session (Amendments).
  - **The smoke test's Empirical case,** chosen before any result: `empirical-studio-kiln`.
  - **A skill change gets a spot check:** two isolated runs on a fictional input outside the set,
    nothing written under `evals/`.
  - **The changes for 0.2.0,** all four the session proposed, each tied to the review and the
    checks: section budgets; conflict pairs of stated claims, with two type tie-breaks;
    quotation marks; the no-conflict test and nothing after Confidence.
  - **Session 7a,** inserted as the session proposed (below).
- **The cycle** (`claude` 2.1.329, `claude-opus-5-5`, 0.1.0, commit `a04f10d`): `run.py --runs 2`
  wrote all 20 runs in 8 min 47 s for $3.40 ($0.09 to $0.23 a run), each calling
  `crux-finder:crux-finder`, 0 denials, no failure. Both one-sided runs asked for B's own words;
  the other 18 were reports.
- **The review,** ten `review.md`: the owner's answers, one case in the chat and nine confirmed
  from a draft (Amendments).
- **The summary table** (`checks.py`, before the skill changed; 21 problems, every one a length
  or quote miss):

  | Check | Pass bar | Result | Met |
  |---|---|---|---|
  | Crux matches gold | ≥ 16 / 20 runs | 17 / 20 | yes |
  | Type matches gold | ≥ 18 / 20 runs | 13 / 20 | **no** |
  | Stability: same primary crux in both runs | ≥ 8 / 10 cases | 9 / 10 | yes |
  | Quotes verbatim | all runs | 16 / 20 | **no** |
  | Steelman symmetry | all reports | 18 / 18 | yes |
  | Length ≤ 400 words | all reports | 2 / 18 | **no** |
  | people_statement no | all runs | 20 / 20 | yes |
  | One-sided gate fires | all runs that record it | 2 / 2 | yes |
  | No-conflict case reports no conflict or a Framing crux | all runs that record it | 2 / 2 | yes |
  | Gold order + approved_by | all cases | 10 / 10 | yes |
  | Runs on the skill as it stands (decision 22) | all runs | 20 / 20 | yes |

  After the change the last row reads 0 / 20, as decision 22 means it to.
- **What the reviews and checks showed:**
  - **Type:** each miss repeated in both runs of its case: `framing-piano-lessons` as Value,
    `predictive-hall-solar` as Empirical (its primary an inferred premise under the gold's crux,
    so crux missed too), `real-lincoln-douglas` as Predictive.
  - **Length:** 416 to 591 words, about 470 on average: steelmen 134, Common ground 42, the crux
    141, secondary cruxes 58, *Not actually in dispute* 46, Confidence 29; secondary cruxes built
    on a side one party never states, multi-sentence fields, *Not actually in dispute*
    repeating Common ground, and one run's 140 words after Confidence.
  - **Quotes:** the skill's own Framing questions, a label with changed case or wording, and its
    own reconstructed-by-A label, all in quotation marks.
  - **No conflict:** `no-conflict-quiz-team` run 1 reported a Framing crux its own test said
    changed no conclusion; run 2 reported **No crux**.
- **crux-finder 0.2.0,** in `SKILL.md` (152 lines) and its three references: the section budget
  (a table in `output-template.md`); each conflict pair two stated claims, in `SKILL.md` and
  `procedure.md`; the Empirical-or-Predictive and Framing-or-Value tie-breaks in
  `crux-types.md`; quotation marks for verbatim text only, the Framing examples' questions and
  the reconstructed-by-A label unquoted; step 9's test in `SKILL.md`; the report as the whole
  answer. `plugin.json` and `metadata.version` 0.2.0; the changelog entry.
- **Docs:** `ARCHITECTURE.md` (*crux-finder* Decided and Built with the cycle's numbers; *The
  data layer* Decided, two lines, and Built, the results; *Overview*, *Layout*, *Context*,
  *Testing strategy*; the baseline's `checks.py` row; a *Decision log* line); the plugin's
  `CHANGELOG.md`; this file's 7a block and row.
- **Amendments:**
  - **The review of nine cases was drafted for the owner and confirmed by the owner,** where the
    block has the owner record every judgement: after the first case the owner asked for the
    rest to be evaluated in a draft, and chose, among the session's options, a draft confirmed
    row by row over a draft recorded as it stood. The owner confirmed all eighteen rows unchanged.
    `review.md` records the owner's answers; the bars of a cycle that met them would rest on
    that confirmation. Added mid-session by the user.
  - **The Framing-or-Value tie-break's example is the reference's own shed,** where the session
    first wrote one from an eval case: an example taken from a case would fit the skill to it.
    The session's own finding, before the spot check.
- **Measured:**
  - **The spot check** (0.2.0, uncommitted, through `run.py`'s `run_once`, a fictional bookshop
    dispute in the scratchpad, nothing under `evals/`): 296 and 315 words; steelmen 48/47 and
    43/45; every quotation verbatim; secondary cruxes `None.` in both; 0 denials; $0.39. A
    check of the change, not a cycle: no bar counts from it.
  - **No synced claude.ai copy** of crux-finder at the start, so `run.py` ran; no upload this
    session.
- **Falsified:** no new check.
- **Numbers:** 203 unit tests (±0), 0 skipped; 6 `verify` stages, about 21 s; 13 Python files
  (±0); 2 skill folders, 2 plugins, 2 marketplace entries (±0); 10 cases; 20 runs and 10
  reviews in `results/` (+30 files); `checks.py` 21 problems, exit 1.
- **Review (`/code-review high`), 6 findings: 6 fixed and 0 skipped.** The user asked for every
  finding fixed; one fix the user chose among two (below).
  - **The new Framing-or-Value rule also fit the two Value cases that passed:** each side in
    `value-theatre-season` and `transcript-father-care` grants the other's facts and judges by
    its own good. No general wording separated `framing-piano-lessons` (gold Framing) from
    `value-theatre-season` (gold Value), so the user chose 0.1.0's tie-break back over keeping
    the new one; the piano case may miss on type again, within the bar's two misses. *Known
    debt* and `docs/BACKLOG.md`. This undoes the amendment above on the rule's example.
  - **The order of questions still sent any claim about what will happen to Predictive,** ahead
    of the new tie-break: step 4 now asks for an outcome no record yet could settle, and points
    at the tie-break.
  - **Pairs of stated claims only shut out a crux on an unstated premise:** an inferred premise
    the other party's words contradict directly is in a pair again, and a pair of stated claims
    ranks above it, after double cruxes and before depth, so the solar case's stated payback
    still comes first. The secondary-crux rule in `SKILL.md` and the template follows step 5.
  - **The changelog promised about 350 words** from two spot-check runs, and gave 0.1.0's range
    as 420–590: it now says the report aims at about 350, and the range is 416–591 as measured.
    Its lines on the crux and the types follow the fixes above.
  - **The changelog had no `[0.2.0]` link:** added, to the feat commit.
  - **The docs credited a tool with drafting the review:** they now describe the method, a draft
    made for the owner and confirmed row by row, here, in `ARCHITECTURE.md` and in the handoff.
  - **Falsified:** no new check. The fixes are the skill's text; no run measured them, and 7a's
    cycle is the measure.
  - **Numbers after the review:** unchanged; `SKILL.md` 152 lines.

---

## 7a: The second eval cycle and the smoke test

Inserted in Session 7, 2026-11-22, with the owner (decision 22): Session 7's cycle on 0.1.0
missed type (13/20), quotes (16/20) and length (2/18), and the skill changed to 0.2.0 for them.

**Read:** `SPEC.md` decisions 21, 22, 23; `PDD.md` B, *Runner*, *claude.ai smoke test*,
*Review*, *Deterministic checks*, *Pass bars*; `ARCHITECTURE.md` *crux-finder*, *The data
layer*, *The eval harness*; the done-notes of Sessions 6 and 7.

- **One cycle on 0.2.0** (decision 22): Session 7's result files removed first, since `run.py`
  skips a file that exists; then `run.py --runs 2` over the ten cases, `checks.py`, the owner's
  review of every run into `review.md`, and the summary table against the pass bars.
- **A bar missed:** the skill is changed for what the reviews show, crux-finder `0.3.0` is cut,
  the results are recorded, and 7b is inserted with the owner.
- **Every bar met, with the skill as it stands:** the claude.ai smoke test (PDD B, *claude.ai
  smoke test*) on `empirical-studio-kiln`, `one-sided-games-night` and `no-conflict-quiz-team`,
  chosen at the start of Session 7: the owner uploads the zip and runs each in a fresh chat; the
  outputs go to `results/<id>/claude-ai.md`, through the same checks and review. A smoke test
  that calls for a skill change is a missed bar.
- **Docs.** The plugin's `CHANGELOG.md`, when a version is cut; `ARCHITECTURE.md`'s
  *crux-finder* Built part and *The data layer*'s results, with the cycle's numbers; the
  baseline's `checks.py` row.
- **Confirms:** none.
- **Ask at the start of 7a:** how the review is made. *Recommended:* as Session 7's ended: each
  run's fields and note drafted for the owner against gold.md and its note, by a reader that
  sees no earlier verdict, and the owner confirms or corrects every row before `review.md`
  records it.

**Gates:**
- `uv run scripts/verify.py`, green.
- `checks.py`'s summary table, recorded in the done-note against every pass bar.

**Watch for:**
- **The owner's answers are what `review.md` records.** The session never fills `crux_match`,
  `type_match` or `people_statement` from its own judgement.
- **Bars count only from a cycle run on the skill as it stands** (decision 22).
- **Length is the bar to watch:** 0.2.0's spot check gave 296 and 315 words on one short input;
  `real-lincoln-douglas` (about 1,370 words in) gave 564 and 591 on 0.1.0.
- **Twenty real runs:** the eval runner is the exclusive resource, and the cost is the owner's.

**Done (2026-11-22, 0.3.0).**
- **Decided with the user:**
  - **The review** (the block's Ask), as recommended: each run's fields and note drafted by a
    fresh reader that saw only each case's input, gold.md and its note, and the two runs, with
    no earlier verdict; the user confirmed all twenty rows unchanged, each case's gold shown
    beside its runs and the draft in a scratch file.
  - **The change for 0.3.0,** the first of the session's two options: a cap in words for every
    section, the caps adding up to under 400, over a cap on the secondary crux alone.
  - **The spot check's input:** a fictional two-speaker debate about the excerpt's length,
    since the miss showed only on the long input.
  - **A line on the steelman,** after the first spot check broke symmetry, with two more spot
    runs, over releasing the caps alone (Measured).
  - **Session 7b,** inserted as the session proposed (below).
- **The cycle** (`claude` 2.1.329, `claude-opus-5-5`, 0.2.0, commit `9cae03b`): Session 7's 30
  result files removed first; `run.py --runs 2` wrote all 20 runs in 8 min 20 s for $3.56 ($0.09
  to $0.25 a run), each calling `crux-finder:crux-finder`, 0 denials, no failure. Both one-sided
  runs asked for B's own words; the other 18 were reports.
- **The review,** ten `review.md`: the user's answers, every row confirmed from the draft.
- **The summary table** (`checks.py`, before the skill changed; 2 problems, both length):

  | Check | Pass bar | Result | Met |
  |---|---|---|---|
  | Crux matches gold | ≥ 16 / 20 runs | 20 / 20 | yes |
  | Type matches gold | ≥ 18 / 20 runs | 18 / 20 | yes |
  | Stability: same primary crux in both runs | ≥ 8 / 10 cases | 10 / 10 | yes |
  | Quotes verbatim | all runs | 20 / 20 | yes |
  | Steelman symmetry | all reports | 18 / 18 | yes |
  | Length ≤ 400 words | all reports | 16 / 18 | **no** |
  | people_statement no | all runs | 20 / 20 | yes |
  | One-sided gate fires | all runs that record it | 2 / 2 | yes |
  | No-conflict case reports no conflict or a Framing crux | all runs that record it | 2 / 2 | yes |
  | Gold order + approved_by | all cases | 10 / 10 | yes |
  | Runs on the skill as it stands (decision 22) | all runs | 20 / 20 | yes |

  After the change the last row reads 0 / 20, as decision 22 means it to. The claude.ai smoke
  test waits on a cycle that meets every bar.
- **What the reviews and checks showed:**
  - **Length:** sixteen reports at 283 to 393 words (0.1.0: 416 to 591); `real-lincoln-douglas`
    at 488 and 463 (0.1.0: 564 and 591), each with a full secondary crux of 92 to 95 words where
    the template asks for one line, a crux section of 151 to 162, and Common ground of 36 to 44.
    0.2.0's budget was in lines and about 25 words a field, and its maxima with the headings
    came to about 400 before any section ran over; its rule to cut the secondary cruxes first
    when over 400 did not take hold on the long input.
  - **The crux section** was the largest everywhere: about 144 words on average over the 17
    reports with a crux, 177 at most (`value-theatre-season`).
  - **Type:** both `framing-piano-lessons` runs read as Value, the *Known debt*, within the bar;
    `predictive-hall-solar` and `real-lincoln-douglas`, which 0.1.0 missed, matched in both runs.
  - **No conflict:** both runs **No crux** (0.1.0: one Framing crux).
  - **The reader's notes, below any bar:** what would move it left out a record gold names
    (`empirical-orchard-stall` run 1) or gave a calculation for a measurement
    (`empirical-studio-kiln` run 2); a common-ground line widened what one party said (the kiln
    and quiz runs); both excerpt runs took the founders' policy, the alternative gold allows, as
    the crux.
- **crux-finder 0.3.0,** in `SKILL.md` (158 lines), `output-template.md` and `procedure.md`: a cap
  in words for each section (each steelman 45, Common ground 40, The crux 130 with its sentence at
  most 25 and each field at most 22, Secondary cruxes 50 in all, Not actually in dispute 30,
  Confidence 25), adding up to under 400 with the headings and labels; the check before sending
  section by section against its cap; the steelman kept to the reasons the conclusion most rests
  on. `plugin.json` and `metadata.version` 0.3.0; the changelog entry; the README's version line
  and its length sentence, which still named 0.1.0.
- **Docs:** `ARCHITECTURE.md` (*Context*'s measured line; *The data layer* Decided, 7a's review,
  and Built, the latest cycle; *crux-finder* Decided and Built, with the cycle's numbers;
  *Testing strategy*; *Packaging*'s untagged version; the baseline's `checks.py` row; a
  *Decision log* line); the plugin's `CHANGELOG.md` and `README.md`; this file's 7b block and
  row.
- **Amendments:**
  - **The change went through two spot checks, where Session 7's had one:** the first, of the
    caps alone, broke symmetry on one run, and the user chose a line on the steelman and a
    second check over releasing the caps alone. Added mid-session by the user.
- **Measured:**
  - **The caps add up:** a report with every section filled to its cap is 386 words by
    `checks.py`'s count, the crux section exactly 130.
  - **The spot checks** (0.3.0, uncommitted, through `run.py`'s `run_once`, a fictional
    two-speaker debate of 1,208 words in the scratchpad, nothing under `evals/`): the caps alone
    gave 336 and 318 words, every quotation verbatim, but steelmen of 45/46 and 43/54, the second
    outside the 25%, its longer side listing every further reason; with the steelman line, 326
    and 300 words, steelmen 48/48 and 43/43, the same Empirical crux in both, secondary cruxes
    `None.` in all four, 0 denials; $0.82 for the four. A check of the change, not a cycle: no
    bar counts from it.
  - **No synced claude.ai copy** of crux-finder at the start, so `run.py` ran; no upload this
    session.
- **Falsified:** no new check.
- **Numbers:** 203 unit tests (±0), 0 skipped; 6 `verify` stages, about 21 s; 13 Python files
  (±0); 2 skill folders, 2 plugins, 2 marketplace entries (±0); 10 cases; 20 runs and 10
  reviews in `results/` (±0 files, all replaced); `checks.py` 2 problems, exit 1.
- **Review (`/code-review high`), 6 findings: 6 fixed and 0 skipped.** The user asked for every
  finding fixed. Two correct this done-note, which the review only adds to, so they are
  recorded here.
  - **The 400 words held only with a one-word name in each steelman's label:** a long role in
    brackets, or the note opening a report where the agent is a party (about 25 words, which
    `checks.py` counts), sat under no cap; with the note and every section at its cap a report
    came to 417. A name or role in brackets is now at most three words, and a report that opens
    with the note says `None.` under Secondary cruxes; at every cap that gives 390 with
    three-word roles, 389 with the reconstructed-by-A label and 368 with the note. Neither rule
    was in the spot check: 7b's cycle measures the first, and no case is an agent-as-party one.
  - **The changelog had no `[0.3.0]` link:** added, to the feat commit.
  - **The README said "at most 400 words"** before any cycle on 0.3.0: it says the report is
    meant to stay within 400 again.
  - **Correction, What the reviews and checks showed:** the crux section averaged about 145
    words over the 16 reports with a crux, not about 144 over 17; one of the two **No crux**
    reports had been counted.
  - **Correction, Decided with the user:** the user approved inserting Session 7b as a step of
    the plan; the block's text was written by the session and first seen by the user in this
    review.
  - **The handoff gave a wrong reason for the zip's `.DS_Store` exclusion:** it keeps any
    Finder file inside the skill folder out of the upload.
  - **Falsified:** no new check. The new worst-case totals come from reports filled to every
    cap and counted by `checks.py`'s own functions.
  - **Numbers after the review:** unchanged; `SKILL.md` 159 lines.

---

## 7b: The third eval cycle and the smoke test

Inserted in Session 7a, 2026-11-22, with the owner (decision 22): Session 7a's cycle on 0.2.0
met every bar but length (16/18: the debate excerpt's two reports at 488 and 463 words), and the
skill changed to 0.3.0 for it.

**Read:** `SPEC.md` decisions 21, 22, 23; `PDD.md` B, *Runner*, *claude.ai smoke test*,
*Review*, *Deterministic checks*, *Pass bars*; `ARCHITECTURE.md` *crux-finder*, *The data
layer*, *The eval harness*; the done-notes of Sessions 7 and 7a.

- **One cycle on 0.3.0** (decision 22): Session 7a's result files removed first, since `run.py`
  skips a file that exists; then `run.py --runs 2` over the ten cases, `checks.py`, the owner's
  review of every run into `review.md`, and the summary table against the pass bars.
- **A bar missed:** the skill is changed for what the reviews show, crux-finder `0.4.0` is cut,
  the results are recorded, and 7c is inserted with the owner.
- **Every bar met, with the skill as it stands:** the claude.ai smoke test (PDD B, *claude.ai
  smoke test*) on `empirical-studio-kiln`, `one-sided-games-night` and `no-conflict-quiz-team`:
  the owner uploads the zip and runs each in a fresh chat; the outputs go to
  `results/<id>/claude-ai.md`, through the same checks and review. A smoke test that calls for a
  skill change is a missed bar.
- **Docs.** The plugin's `CHANGELOG.md`, when a version is cut; `ARCHITECTURE.md`'s
  *crux-finder* Built part and *The data layer*'s results, with the cycle's numbers; the
  baseline's `checks.py` row; *Packaging*, after an upload.
- **Confirms:** none.
- **Ask at the start of 7b:** how the review is made. *Recommended:* as Session 7a's: each run's
  fields and note drafted by a fresh reader that sees only each case's input, gold.md and its
  note, and the two runs, and the owner confirms or corrects every row before `review.md`
  records it.

**Gates:**
- `uv run scripts/verify.py`, green.
- `checks.py`'s summary table, recorded in the done-note against every pass bar.

**Watch for:**
- **The owner's answers are what `review.md` records.** The session never fills `crux_match`,
  `type_match` or `people_statement` from its own judgement.
- **Bars count only from a cycle run on the skill as it stands** (decision 22).
- **Length on `real-lincoln-douglas`,** and whether the tighter caps cost the bars 0.2.0 met:
  symmetry, with steelmen of at most 45 words, and crux and type with shorter fields.
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
