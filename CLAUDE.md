# claude-skills

A public collection of Agent Skills, one Claude Code plugin per skill, in one marketplace,
`faircat-skills`. `.claude-plugin/marketplace.json` lists each plugin; `plugins/<skill>/` holds
its `.claude-plugin/plugin.json`, `README.md` and `CHANGELOG.md`; and
`plugins/<skill>/skills/<skill>/` is the skill folder that ships, `SKILL.md` and `references/`.
Each skill also works as a plain skill folder in Codex, claude.ai and any agent that loads
`SKILL.md`. The marketplace name and each plugin's and skill's name
(`travel-itinerary-builder`, `crux-finder`) never change once published, because people install
by them.

**Each plugin's `README.md` is its skill's user guide;** there is no `docs/USER-GUIDE.md`. It
says what the skill does, what it needs on each target and how to install it, and crux-finder's
holds its eval results. A session that changes what a user sees, how a skill installs, or a
number a README states keeps that README true.

**Read `docs/ARCHITECTURE.md`'s overview, invariants and baseline, and the sections your
session's block names, before changing anything.** It describes how the repository is built:
the layout, the contract between marketplace, plugin and skill, the stack and its pins, the
invariants, `verify`, the eval harness, and the deliberate decisions that look wrong until you
know why. It keeps what is **Decided**, which changes only with the owner, apart from what is
**Built**, which every session keeps true (*The documents* in `docs/DEVELOPMENT-WORKFLOW.md`).
**The round's spec files in `docs/spec/` are the contract for what the round delivers**: read
the parts your block names. `docs/DEVELOPMENT-WORKFLOW.md` is the session-based workflow this
repo follows; its *In this repository* paragraph says where this repo deviates.
`docs/BACKLOG.md` lists what has been named but not planned.

## Working protocol

Every session runs *The session cycle* in `docs/DEVELOPMENT-WORKFLOW.md`. One session per
chat. A push or tag needs explicit approval, each time.

**Scope lives in `docs/spec/SESSIONS.md`** (one block per session, in order) and the round's
spec files (`SPEC.md` in round 1; after it, one `FEATURE-*.md` per request, holding the request
verbatim plus the decisions resolved at intake — read-only, not re-litigated). `docs/spec/`
holds only the round in progress: when a round closes its files are deleted (git history keeps
them) and anything still open moves to `docs/BACKLOG.md`. **State lives in
`docs/next-session-prompt.md`**, rewritten by every session as its last act.

1. `uv run scripts/verify.py` (skills + plugins + format + lint + tests + hygiene) must be green
   before you commit, docs-only commits included. `skills` needs the network while uv's cache
   is cold, and `plugins` needs the `claude` CLI. Run a skill's evals only when your block names
   them; expected results are in ARCHITECTURE.md's baseline table.
2. Falsify any new check before trusting it: break the assertion, watch it fail at its own
   step, restore it.
3. A change to a skill's shipped files gets a line in that plugin's `CHANGELOG.md` and a version
   bump, `major.minor.fix`, in its `plugin.json` and its `SKILL.md` `metadata.version`. A
   session that changes no skill cuts no version. A skill with no `plugin.json` yet cuts none
   either: the session that creates its manifest releases the change.
4. If a decision is genuinely underdetermined, stop and ask rather than guessing — a guess
   becomes load-bearing for everything after it.
5. Comments state the present: why the code is shaped this way now. No session ids, no
   "until v0.x", no review stories — git history keeps those.

## Invariants — these are rules, not preferences

1. Every skill folder conforms to the Agent Skills specification (the `skills` stage).
2. A skill's names agree everywhere, and every plugin is listed in the marketplace (the
   `plugins` stage).
3. A skill's version is the same in `plugin.json` and `metadata.version` (the `skills` stage).
4. crux-finder ships no scripts and needs no network or dependencies (the `skills` stage).
5. Everything under `evals/` imports the standard library only (a test).
6. Neither the eval runner nor the session under test reads `gold.md` (a test; the run's
   isolation).
7. Each `gold.md` is committed before any of its results, and names who approved it
   (`checks.py`).
8. Published names are never renamed (the `plugins` stage).
9. Nothing private enters the repository (the hygiene stage).

Each is enforced from the session named in `ARCHITECTURE.md`; until then, by reading the diff.

## Python 3.10, through uv only

Every script and test runs on Python 3.10, the eval tooling's floor, through `uv run`; the
machine's own `python3` is another version. Code that needs 3.11 or newer (`tomllib`, `Self`,
`except*`) fails here. The one exception is the Agent Skills validator, which needs 3.11 or
newer and runs through `uvx` on its own interpreter, pinned to a commit.

## Nothing private goes in

The repository is public, so every file, test, fixture, done-note, handoff and commit message
follows these rules:
- **No personal names, no names of the owner's other projects or games, no agent personas.**
  Write the role: "the owner", "the maintainer". A public repository the docs cite by name is
  the exception.
- **No home-directory paths.** Write `~`.
- **No AI attribution:** no co-author trailers, no lines saying a tool generated the work, no
  AI session links, no AI credited as author, co-author or addressee. Naming Claude Code,
  Codex, claude.ai or the `claude` CLI as targets or tools is fine.
- **Fixtures are fictional.** Eval inputs are fictional, public domain, written and
  anonymized by the owner, or a public claim about a public figure. A public figure such a
  case names may be named in its results and in a README's test table; a private person never.
- **Done-notes and handoffs never name the owner's own data.**
- **Unsure whether something is public? Ask the owner before writing it.** A word they call
  private goes on the term list.

The owner publishes on purpose the handle `FairCat-GD` (licence, marketplace owner,
`approved_by`) and their name as commit author and as each plugin's `author` in its
`plugin.json`. The hygiene stage of `verify`
(`uv run scripts/verify.py hygiene`) checks the term list in `~/.config/hygiene/terms.txt`,
attribution in messages, secrets and conflict markers; the last read of each diff covers the
rest of this list.

## Commands

| Command | Does |
|---|---|
| `uv run scripts/verify.py [stage …] [--message <draft>] [--all]` | The gate: the named stages (`skills`, `plugins`, `format`, `lint`, `tests`, `hygiene`), or all of them in that order, each run even after one fails, then a summary. `--message` and `--all` go to `hygiene`, which must be among the stages run |
| `uv run scripts/verify.py --message "$(git rev-parse --git-dir)/COMMIT_DRAFT"` | The last act before each commit: every stage, with the drafted message checked by `hygiene` |
| `uv run scripts/verify.py hygiene --all` | Hygiene's full scan, on demand; it also runs by itself when the term list or the stage changes, or in a checkout with no stamp |
| `uv run ruff format .` and `uv run ruff check --fix .` | Apply what `format` checks, and the fixable part of what `lint` checks |
| `uv run pytest tests/test_hygiene.py -k <name>` | One test file, or the tests whose names match |
| `uv run scripts/check_skills.py` and `uv run scripts/check_plugins.py` | The `skills` and `plugins` stages' own checks alone, without the validators |
| `claude plugin validate --strict <path>` | The CLI's check of the marketplace (`.`) or of one plugin (`plugins/<skill>`), as the `plugins` stage runs it |
| `uv run evals/crux-finder/run.py --runs N [--case <id> …]` | The eval runner: one isolated `claude -p` session per case per run, into `results/<id>/run-N.md`. Skips a run whose file exists; refuses while `plugins/crux-finder/` has uncommitted changes. Spends real model runs: only where a block names it |
| `uv run evals/crux-finder/checks.py` | crux-finder's deterministic checks (gold order, `approved_by`, quotes, symmetry, length, `review.md`) and the summary table against the pass bars |

No test reads the owner's term list or touches the real hygiene stamp, `results/` or `cases/`.

**Exclusive resources:** the eval runner (it writes `results/` and spends real model runs, one
at a time) and the owner's claude.ai account. A parallel part never runs them; the session's
integration does.

## Git

- Commits use this machine's git identity.
- Commit locally; a push or tag needs explicit approval, each time. Before any push, list
  `git log origin/main..HEAD`; parallel sessions may share this checkout. `origin` is public:
  a push makes the marketplace's current state installable.
- Stage explicit paths, never `git add -A`. Never undo with `git checkout <path>`.
- As the last act before each commit, after the done-note, the handoff and a last read of the
  diff for what no script judges (the workflow's *A clean repository*): draft the message into
  `"$(git rev-parse --git-dir)/COMMIT_DRAFT"`, run `uv run scripts/verify.py --message` with
  it, commit with `git commit -F` from it, then delete it. The message is checked before it
  exists in history.

## Watch for

The standing traps and forbidden moves, a line or two each: the trap, then what to do instead.
One goes in when the intake knows it or once it has cost a session time, and comes out once a
check, a script or a pin makes it impossible.

- **A shell command that reads stdin hangs.** Give it `< /dev/null`.
- **Renaming a published name** (the marketplace, a plugin, a skill, a case id with results) is
  forbidden without the owner.
- **A commit message that describes eval output** in the words of the attribution rule (a tool
  "generated" a report) fails the hygiene stage. Say what changed in the skill instead.
- **A real transcript can hold a word on the term list.** Ask the owner; never trim a quote
  silently.
- **`claude plugin marketplace add ./` registers this folder in the owner's user settings.**
  Remove it with `claude plugin marketplace remove faircat-skills` before the session ends; that
  also uninstalls the plugins installed from it, and nothing else.
- **A `claude` update can turn the `plugins` stage red** with no change here, since
  `claude plugin validate --strict` fails on every warning and the CLI is not pinned. The stage
  prints the CLI's version first: compare it with the baseline's, fix what the warning names,
  and ask the owner before dropping `--strict`.
- **A skill uploaded to claude.ai syncs into every Claude Code session** as
  `anthropic-skills:<skill>`, beside the plugin's copy. `run.py` refuses a run where it loads;
  after a smoke test, delete the upload unless the owner keeps it.
- Do not finish with `verify` red, or with a skill's change missing from its plugin's
  `CHANGELOG.md`.
