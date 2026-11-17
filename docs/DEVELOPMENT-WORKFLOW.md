# Session-based development workflow

A versioned specification, not the conversation, is the source of truth, and AI coding agents
and developers write code against it. Work is divided into fixed-scope **sessions**. Each runs
in a single chat, with no context carried between them. Because no session can rely on
remembering a previous one, the repository holds everything a session needs: the contract, the
scope, the current state and the known pitfalls. The same discipline suits human teams with
turnover or long gaps between working periods.

Use it for any project expected to outlast its author's working memory. It is more process than
a weekend prototype needs.

This file is copied verbatim into every project as `docs/DEVELOPMENT-WORKFLOW.md`, templates
included. The one edit a project makes to it is an **In this repository** paragraph here, under
the introduction, naming where the project deviates and why (see *Adapting the workflow*). The
project's own standing rules live in its `CLAUDE.md`, not here.

**In this repository.** This repository holds many Agent Skills, one Claude Code plugin per
skill in one marketplace, and its products are mostly prose. Copied from the kit at commit
`02fb1d99f56ff414ec88cf7b1789328933e355d0`. It keeps the core (*Adapting the workflow*) and
deviates in these places, decided at the round 1 intake:
- **Versions are per skill.** Each plugin carries its own version in its `plugin.json` and its
  own `CHANGELOG.md`. A session cuts a version only for a skill whose shipped files it changed;
  a session that changes no skill cuts none, and nor does a change to a skill with no
  `plugin.json` yet, which the session that creates its manifest releases. Where this file
  says "the manifest" or
  "`CHANGELOG.md`", read the plugin's.
- **`verify` is tailored to skills:** the stages `skills`, `plugins`, `format`, `lint`,
  `tests` and `hygiene`, with no type-check stage, since the only code is a few small scripts.
  There is no separate docs-only command: `verify` takes seconds, so every commit runs it whole.
- **A skill's harness is its eval set,** under `evals/<skill>/`. It spends real model runs, so
  it runs only where a session's block names it, never inside `verify`.
- **No CI,** as this file says; the validators run inside `verify`.
- **No architecture-review sessions.** The round's last session reads `ARCHITECTURE.md` cold
  against the code, which covers a codebase this small.
- **No `docs/USER-GUIDE.md`.** Each plugin's own README is its user guide, kept true like one.
- **The hygiene stage** was ported in part from another of the owner's projects, which the owner
  relicensed here under MIT, and completed from the kit's design.

## The documents

| Document | Job | Mutability |
|---|---|---|
| `docs/spec/` | **the round in progress**: its spec file(s), any reviews and its `SESSIONS.md`; while a session runs parallel parts, their notes in `parts/` | spec read-only, except dated amendments the human makes; SESSIONS amendable with a logged reason; part notes deleted by the session commit; the folder is emptied when the round closes |
| `docs/next-session-prompt.md` | **state**: what the next session needs that the docs do not say | rewritten by every session as its last act |
| `CHANGELOG.md` | what shipped, per version, written for the person using the product | append-only for content |
| `docs/BACKLOG.md` | work that has been named but belongs to no round, and checks nobody has done by hand | items move out when a round picks them up |
| `CLAUDE.md` | standing rules, loaded into every session automatically | edited as rules change; kept lean |
| `docs/ARCHITECTURE.md` | **how the system is built**, as decided and as built: the external systems it depends on, the stack and its pins, the layers and their boundaries, the data layer, the invariants, the testing strategy, the deliberate decisions, the known debt and the baseline counts | written by Session 0; kept true by every session; its Decided parts change only with the human, each change logged |
| `docs/USER-GUIDE.md` | behaviour from the user's side | written by round 1's documentation pass; kept true by every session after |
| `README.md` | what the thing is, how to run it, where the docs are | written by Session 1; kept true |
| `docs/DEVELOPMENT-WORKFLOW.md` | this file: the method and its templates | copied verbatim at Session 0; only its *In this repository* paragraph is the project's |

**Scope and state are different jobs, and the split is what makes the workflow hold.** Scope
(`SESSIONS.md`) is fixed in advance, so no session can quietly redefine what a later one owes.
State cannot be written in advance, so the last act of every session is writing the next
session's prompt.

**The spec files of a round.**
- **Round 1, the build:** `docs/spec/PDD.md` (the product design draft, frozen as received,
  with private details replaced by roles) and `docs/spec/SPEC.md` (the contract derived from
  it). They are not two copies of one thing. The spec holds what the round delivers: its
  decisions, where it overrides the draft and which session builds each requirement; for the
  detail it points into the draft rather than copying it, so the draft stays until the round
  closes. How the system is built is not in the spec: Session 0 writes it into
  `docs/ARCHITECTURE.md`, which outlasts the round.
- **Every later round:** one `docs/spec/FEATURE-<name>.md` per request, holding the request
  verbatim and a dated list of the decisions resolved at intake.
- **A round that comes from an audit** keeps the audit beside them as
  `docs/spec/REVIEW-<date>.md`, and so does each architecture review a long round places at its
  milestones. A review is evidence and a session block is scope, and neither is the other: a
  finding becomes scope only when the human turns it into a decision or a block, at an intake
  or in the review session's plan mode.
- **Either way,** the spec is read-only once the round's first session opens. When the human
  changes a resolved decision mid-round, the change is added to the spec file, next to what it
  changes, as a dated **Amended <date> by the user** note saying what changed and why. The
  original text stays. A session never amends the spec on its own authority.

**`ARCHITECTURE.md` keeps what is decided apart from what is built.** **Decided** is the
human's: what an intake answered, and what the human settled with a session, in plan mode, at a
stop or when confirming. A session writes into it only what the human decided. Each addition or
change after Session 0 is written straight in, with a dated line in the file's *Decision log*;
it amends every later block it reaches (*The rules*, 3), and the handoff names it. Git keeps the
earlier wording. **Built** is what exists and how: what sessions built within what is decided
(an entity, field or migration within the data layer's rules, a message within the decided
protocol, a test), the decisions a session made on its own within its scope, each with its why
and in the section it belongs to, the debt and the baseline. Every session keeps it true, and
may revise an earlier session's decision there, giving the reason in its done-note. A choice
that spans subsystems is the human's. A session that finds a Decided part wrong stops (*The
rules*, 2).

**A Decided part is confirmed against code by the first session that builds on it.** Once its
`verify` is green, and before it keeps the docs true (the cycle, step 7), that session shows the
human each Decided part its block lists under **Confirms**, against the code as it now stands.
The human confirms it or changes it, and the done-note records the outcome. Code that a change
leaves behind is brought into line before step 7; a change too large for the session is a stop
(step 5). Until then a Decided part is the intake's best judgement, made without code.

## Rounds

Work happens in **rounds**, and every round has the same lifecycle.

**Where a round comes from:**
- a request from the human;
- a walkthrough, where the human uses the build and their corrections are the request;
- an audit run at the human's request and recorded as `REVIEW-<date>.md`, from the
  architecture review's template: its §1–§4, with §5 on what the request will put through the
  code and §6 saying which findings the intake turned into decisions;
- items picked from `docs/BACKLOG.md`.

However it starts, it goes through an intake.

1. **Intake.** The intake is a session of its own, in its own chat, and writes no product code.
   - The request is written down verbatim.
   - A request that asks for judgement ("what is missing before 2.0?") is answered by an audit
     first, of the code, the docs and whatever the product promises. The intake then proposes
     groups of work for the human to pick from.
   - What the request leaves underdetermined is asked in small batches, each question with a
     recommended answer and one line on why. A contradiction is asked about, not resolved by a
     guess.
   - The answers are recorded as numbered, dated *resolved decisions*. An implementing session
     never re-litigates them. What the human declines goes to `docs/BACKLOG.md`, saying which
     intake left it out.
   - An answer about how the system is built goes into a Decided part of
     `docs/ARCHITECTURE.md`, not the spec file. Session 0 writes the file; a later intake
     writes its answers in, each with a *Decision log* line, and gives each new subsystem its
     section, whose Built part names the session that builds it.
   - A question that only the implementing session will have the context to answer can be
     left to it, written into its block as **Ask at the start of <id>**. A proposal the human
     has not confirmed says so.
2. **Plan.** `docs/spec/SESSIONS.md` gets the standard header, a table of sessions with their
   versions, and one block per session, in order (templates at the end of this file). Each
   block has:
   - its **Read** line: exactly what the session reads of the spec files, `ARCHITECTURE.md` and
     any review, by number and by name (decisions, invariants, the draft's parts and items,
     sections, findings), plus any section of this file beyond the cycle that the session
     builds from, such as Session 1's *Day one*. The intake has read everything, so it is the
     one placed to say what each session needs;
   - its **Scope**, pointing at the files and lines it changes where the intake could see them;
   - its **Docs**: which documents it keeps true, and how;
   - its **Gates**: `verify`, the tests it must add, and the harnesses it must run;
   - its **Watch for**: the known traps.

   A session should be finishable in one chat with every gate green, and deliver a vertical
   slice rather than one layer.
   - **A round of more than five build sessions places an architecture review after each
     milestone**, a point where a layer that later sessions build on is finished. A session's
     review sees one diff; an architecture review reads the code of every session so far, cold,
     against `ARCHITECTURE.md` and the spec, and finds the drift between sessions that no diff
     shows, and where `ARCHITECTURE.md` no longer describes the code. It is a session
     with its own block, whose Read line is everything, and it writes
     `docs/spec/REVIEW-<date>.md` (template at the end): findings only, no product code, no
     version. It does correct a Built part of `ARCHITECTURE.md` that fell behind code doing
     what was decided, in its own commit, so no later session builds on it. Code that breaks a
     Decided part is a finding, for the human. In its plan mode the human picks which findings
     become scope. Each becomes an amendment to a later block or part of an inserted fix
     session.
   - **Each block lists under Confirms the Decided parts of `ARCHITECTURE.md` it is the first
     to build on** (*The documents*). Round 1 plans a walking skeleton as early as it can,
     usually Session 1 or 2: a thin slice through every layer and to each external system, so
     most of the architecture is confirmed against code in the round's first sessions.
   - **Session ids.** Round 1 numbers its sessions (0, 1, 2…). Later rounds give each session a
     letter for its theme and a number, for example C1–C4 for a cleanup, D1 for the data
     layer, V1 for a release.
3. **The intake ends like any session.** The items it picked leave `docs/BACKLOG.md`, and the
   handoff is rewritten to open the round's first session. Then comes a local commit
   (`docs: open round <N> — <theme>`) and the human's review. At an intake the review checks
   the plan against the code: the pointers and the Read lines, the feasibility, and where the
   spec, `ARCHITECTURE.md` and the code disagree. Its fixes land in the spec, the architecture
   and the plan before the first session opens.
4. **Sessions**, one per chat (the cycle below). The plan can change on the way, always with a
   logged reason:
   - **A session can be inserted, with the human,** when a review or a session shows the plan
     is missing one. It gets its own block, which says why it exists, in the human's words
     where they gave them, and takes the id before it plus a letter (6a). The table's versions
     shift, and the handoff says so.
   - **Scope the human adds mid-session** is recorded in the block as "added mid-session by
     the user".
5. **Close.** The round's last block closes it.
   - **Anything left open** moves to `docs/BACKLOG.md`: deferred work, and checks nobody has
     done by hand. A Built part of `ARCHITECTURE.md` that still says "Not yet" for this round
     names its backlog item instead of a session.
   - **The round's last session reads, cold, the sections of `ARCHITECTURE.md` the round's
     blocks named**, against the code. It corrects a Built part that drifted, and brings any
     Decided part the code breaks to the human. Round 1's documentation pass reads all of it.
   - **The round's last session is its release.** Where each session is a release, it cuts a
     version even when its own work is documentation, so every round ends on a version a person
     can name and a milestone's tag can mark. A project that releases at milestones cuts one
     only when the round ends on a milestone.
   - **The close comes last, after the review.** The round's last session writes the
     between-rounds handoff as its handoff (the cycle, step 9), so the review covers it. The
     release commit and its `review:` commit come first, with the last done-note complete in
     them. Then a separate `docs: close round <N>` commit deletes `docs/spec/`'s files and fills
     in the handoff's sha of the review commit, where the last done-note can still be read in
     full. Git history keeps the specs.
   - **Round 1 also owes a documentation pass**, planned as a real session, its last:
     - `docs/ARCHITECTURE.md`, read cold against the code: every Built part true, and the
       baseline current;
     - `docs/USER-GUIDE.md`;
     - a truthful README.

     From then on `CLAUDE.md` points at the user guide too, and every session keeps it true.

**Round 1 starts with Session 0 (intake) and Session 1 (scaffold).** Session 0 turns the
product draft into the spec, the architecture, the plan and the rules file, and writes no
product code. Session 1 builds the scaffold and the day-one checklist, and is the first block
of every build plan.

## Day one (Session 1)

Each of these is cheap on day one and expensive to retrofit.

- **One verification command.** `verify` = typecheck + lint + format check + tests + hygiene.
  Formatting is in the gate from the first commit. It also runs named stages alone
  (`verify hygiene --message <draft>`), so the docs-only command (the cycle, step 6) is one
  call, such as `verify format hygiene --message <draft>`.
- **The hygiene stage** (see *A clean repository*), reading the owner's term list.
- **Version and changelog.** Stamp `0.1.0` in the manifest, surface it in the product, and
  start `CHANGELOG.md` from the template, with an empty `[Unreleased]` section.
- **A fixtures directory** (`tests/fixtures/`). Tests never read design assets or prose
  documentation; a test that depends on a mockup makes the mockup undeletable. A README whose
  examples run as doctests is code.
- **Fictional test data only.** No real names, no real content, no author's identity and no
  home-directory paths in fixtures or seeds.
- **Checkout tuning lives in the repo.** Anything set in `.git/config` or an editor does not
  travel to the next clone; put it in scripts or docs.
- **Part checkouts are ignored.** `.gitignore` and every tool `verify` runs skip
  `.claude/worktrees/` at the checkout's root, where Claude Code creates a parallel part's
  checkout (on a branch `claude/<name>`; see *Parallel parts*), so neither `verify` nor the
  hygiene stage reads a part's copy. Anchor the skip to the root: a part's own `verify` runs
  inside such a checkout and must still read its files.
- **A truthful README**: what the thing is, how to run it, and where the docs are.
- **The Commands table in `CLAUDE.md`**, filled in: every script a session runs, one line
  each on what it does, the docs-only command included.
- **The baseline**, in `ARCHITECTURE.md`'s table: the first counts, from the first green
  `verify`. The Built parts of what the scaffold built are filled in.

## The session cycle

The human opens every session, intakes included, in a new chat in plan mode, by pasting the
one-line opener the previous session printed (step 12). It points at the handoff, which is in
the repository.

1. **Entry gate.** The tree is clean, `docs/next-session-prompt.md` names the session you are
   about to do, and, unless this block is the plan's first, the previous session's block in
   `SESSIONS.md` has its done-note. If it does not, that session did not finish; do not stack
   on it. A session the handoff says paused at integration is the exception: it resumes, and
   its open parts, named in the handoff, stay. Then, where the previous done-note has a
   *Parts* section, check that nothing it names was left behind (*Parallel parts*, integration
   step 6). An intake reads that done-note as of the review commit its handoff names
   (`git show <sha>:docs/spec/SESSIONS.md`).
2. **Read in order** (the handoff's first line copies this order, so the rest of the handoff
   comes last):
   - what the block's **Read** line names, in full;
   - `CLAUDE.md`, which carries every invariant;
   - this file's *The session cycle*, and a section it points to when a step needs it;
   - `docs/ARCHITECTURE.md`: its overview, invariants and baseline, plus the sections the Read
     line names;
   - from `SESSIONS.md`, its header, this session's block and the previous block's done-note;
   - then the prompt.

   No session reads the spec files or `ARCHITECTURE.md` whole, except an architecture review and
   round 1's documentation pass, whose Read lines are everything. They grow past what one
   reading holds, and most of each is about ground the session does not touch. The invariants
   are always in view through `CLAUDE.md`, and a long round's milestone reviews read everything
   (see *Rounds*). The Read line is a floor, not a ceiling: where the code leads somewhere it
   does not name, read that too. An intake has no block yet: it reads what the between-rounds
   prompt names.
3. **Plan with the human before any edit.** In plan mode, read the code the block points at, ask
   the block's *Ask at the start* questions, and write a concrete plan. Before showing it, where
   it is among the riskiest and the session is unsure of it, say why in a line and offer an
   adversarial plan review (*Engineering practices*). On a yes, the plan the human sees is the
   reviewed one. Agree here on anything the plan changes about the block. Those changes are
   logged as amendments ("amended at plan time, with the user"). The human approves the plan,
   and only then does the session edit.
4. **Look for independent parts.** Once the plan is approved, check each of its steps against
   the independence test (see *Parallel parts*) and tell the human, in a few lines, which steps
   could run in parallel and why each is independent, which must stay sequential and what ties
   them, where the parts meet (the interfaces the contract would fix), and what the split would
   cost: how many parts, and how many chats they may be asked to answer in. If no step passes,
   say so in one line and go on. Parts start only on the human's clear yes; without one, the
   session runs sequentially.
5. **Work inside the scope.** Stop the moment the spec or a Decided part of `ARCHITECTURE.md`
   turns out wrong, a decision is genuinely underdetermined, or something does not behave as
   specified. Say so, leave the tree clean or clearly marked, and resolve it with the human. A
   session that guesses to avoid stopping is the expensive failure mode, because the guess
   becomes load-bearing for everything after it.
6. **Verification gate.** `verify` is green before the session may commit. Run the harnesses
   the block names (UI, end-to-end, runtime probes), and any other whose ground the change
   covers. Falsify every new check before trusting it. A commit that changes only docs, meaning
   files no test or build reads, runs the docs-only command in `CLAUDE.md` instead: hygiene,
   plus the format check and lint where they cover docs. Anything else, and every merge, runs
   the full `verify`.
7. **Keep the docs true**, in the same commit as the code:
   - `CHANGELOG.md`: an entry for everything user-visible, under the session's version, and
     the version bumped in the manifest (see *Versions and the changelog*);
   - `docs/ARCHITECTURE.md`, after confirming with the human what the block lists under
     **Confirms**: the Built parts the change touches, with the decisions the session made on
     its own and any new known debt; the baseline table for every count that moved; and, under
     Decided, with a *Decision log* line each, what the human settled with the session (*The
     documents*);
   - `docs/USER-GUIDE.md`, for any behaviour a user now sees differently;
   - `README.md`, when what the thing is, how it runs, or a number it states changes;
   - `CLAUDE.md`, when a standing rule, a command, a pin or a standing trap changes;
   - `docs/BACKLOG.md`, for anything the session deferred or could not check by hand.

   The block's **Docs** line names the ones the plan expected; it is a floor, not a ceiling.
8. **Log.** Append a done-note to the session's block in `SESSIONS.md` (template at the end):
   - what was decided with the human at the start;
   - what actually shipped;
   - the **amendments**, where the block's intent held but its letter did not, each with its
     reason and who decided it;
   - what was measured, and what was checked by hand, with the outcome of each;
   - what was falsified;
   - the numbers, with their deltas.
9. **Handoff.** Rewrite `docs/next-session-prompt.md` for the next session (*The handoff*;
   templates at the end). In the round's last session that is an intake, so it is the
   between-rounds handoff (see *Rounds*).
10. **Commit locally**: one commit for the session's work. A session that ran parallel parts
    has its contract, the parts' commits and the merges before it (see *Parallel parts*). The
    last act before each commit is `verify` run with its drafted message (*A clean
    repository*, "When it runs"). Never push without explicit approval for that specific push,
    and never tag without approval for that tag.
11. **Review.** The human runs a code review over the session's commit at high effort, in the
    same chat (in Claude Code, `/code-review high`); after parallel parts it covers the
    contract, the parts' commits and the merges too, because integration bugs show only in the
    combined code. Fix what it finds. A finding that changes behaviour or scope is the human's
    call, and a finding left unfixed is recorded as skipped, with its reason. A review round
    ends when nothing it found would make the product or a session act wrongly: a finding of
    wording or polish may be skipped, with its reason, and the review is not rerun until it
    finds nothing. Falsify the checks the fixes add. Then:
    - add a **Review** section to the done-note: the findings, what was fixed and what was
      skipped, what was falsified, and the numbers after the review;
    - update that version's CHANGELOG entry and the docs the fixes touched (no new version);
    - update the handoff for anything the review changed, including a session it opened;
    - commit the fixes as a separate `review:` commit;
    - in the round's last session, unless the review opened a session, then make the close
      commit (see *Rounds*).

    Expect it to find something; the worst finds are routinely in code the session had just
    called safe.
12. **Print the opener** as the last message of the chat: one line, ready to paste, that points
    at the handoff and never repeats it. Mid-round it is
    `Read docs/next-session-prompt.md and do the session it names: Session <id>, <one line>, release <x.y.z>.`
    A session that cuts no version leaves out the release. Between rounds it is
    `Read docs/next-session-prompt.md: no round is in progress, so the next session is an intake.`
    If the human then approves a push, follow *Git*: the handoff's push note is folded into the
    last commit before it goes, so the push adds no commit. Print the opener again after the
    push. A milestone's tag comes after all of that (*Git*), and the opener is printed once
    more after it. The chat ends there.

The session is the human's review unit. Between sessions they read the diff and try the build,
and work that runs past the boundary arrives unreviewed and too large to judge.

## Parallel parts

**Tried once:** one session has run two parts, and the rules below include what it taught.

A session can run independent pieces of its approved plan in parallel, each in a chat of its
own. It is an option inside the session, never a way around the cycle. The plan agreed before
any edit, the stop rule, decisions not re-litigated, every check falsified, nothing private,
one code review per session and pushes only with approval all still hold. A session that cannot
keep all of that runs the pieces one after another.

- **The coordinator** is the session the human opened. It plans, proposes the split, commits
  the contract, starts the parts, answers what the plan settles and integrates them, and it
  stays the human's one review unit.
- **A part** is one independent piece of the approved plan, run in a chat of its own, in its
  own checkout and on its own branch. Parts are numbered after their session: 8.1, 8.2, C2.1.
  Letters already mark inserted sessions (6a).
- **Integration** is the coordinator's last stretch: merging the parts, running the full gates
  over the combined code, writing the shared documents and cleaning up.

**The independence test.** A step can become a part only if all of these hold:
- **It needs no other step's result**, and no other step needs its result.
- **Where it meets another part, the interface is fixed.** Parts that meet at an interface (one
  calls what another builds, or both build against one type) are independent only when the plan
  fixes the interface and every brief carries it word for word. Changing it is a stop (see
  *A part's questions*).
- **It needs nothing the coordinator changes in this session, beyond the contract.** Parts are
  cut from the contract commit, or from the commit the session started on when they meet at no
  interface, and the coordinator commits nothing else before they start.
- **It touches no file that another part, or the coordinator's own steps, touch.** That
  includes the files every feature tends to touch. Shared registries are the common trap: one
  list of routes, tools, channels, commands or menu entries, a schema or migration sequence, a
  generated file, a lockfile, a translations file. Two steps that each add one entry to the same
  registry are not independent, however separate their modules look: two tools built in
  different modules but registered in one tool map stay sequential, unless the contract
  registers both, pointing at stubs, so neither part touches the map.
- **It does not have to land in one change with another step.** A data migration and the code
  that reads it belong together.
- **Its checks run on their own.** If the only proof that it works is a harness that needs the
  other parts too, it is not a part.
- **Its checks need no exclusive resource.** A harness that drives a live external app, a
  single-instance desktop app, a fixed port or one real device runs once at a time, so no part
  runs it; integration does. A step whose only proof needs one is not a part. Each project
  names its exclusive resources in `CLAUDE.md`.

When in doubt, a step stays sequential. A wrong split costs more than the time it saves.

**The contract.** When parts meet at an interface, the coordinator commits it before any part
starts, and the parts are cut from that commit. It holds the interfaces as code (types,
signatures, stubs that fail if called) and the shared-registry entries each part would
otherwise add, pointing at those stubs, so each part's own checks, a type check above all, pass
on its branch without anyone else's work. Where an existing test already calls every entry of
a registry, the stub returns the smallest valid result instead, so the full `verify` stays
green. It is typed like any work commit, with no version, ending `(<id>, the parts' contract)`,
and the full `verify` runs on its drafted message last.
- **A part takes in nothing from outside its branch but a contract change** (below).
  Cherry-picking the coordinator's work puts the same patch in history twice. What a part lacks
  is a gap in the contract, and a stop.
- **The contract does not change under running parts** without the human (see *A part's
  questions*). On their yes, the coordinator commits the change on a branch of its own, cut
  from the contract commit in a checkout of its own (`git worktree add -b <branch> <path>
  <sha>`, in the ignored path), merges it into its own line, and sends the new wording to
  every part whose brief carries the interface; each of those parts merges that branch in.
  Each of these merges is drafted and checked like any other:
  `merge: the contract change — <what changed>`. The branch holds the change and nothing else,
  so no part takes in the coordinator's other work, and a merge keeps one copy of the patch in
  history.

**A part's questions.** A part that stops asks the coordinator first, through the human or by
messaging the coordinator's chat where the tool allows it.
- **The coordinator answers** what the approved plan already settles, and a gap in the contract
  it can fill without changing behaviour, scope, the fixed interface or which files each part
  owns.
- **Everything else goes to the human,** an interface change included, and the part waits for
  the answer. When the coordinator is unsure which it is, the question is the human's.
- **Every answer is logged:** the part writes the question, who answered and the answer in its
  note, and the done-note's *Parts* section carries them.

**The shared documents are the coordinator's alone.** Parts writing them at once would
conflict at every merge, so only the coordinator writes them, at integration.
- **The coordinator's alone:** `SESSIONS.md`, the handoff, `CHANGELOG.md`, the version in the
  manifest, `ARCHITECTURE.md`'s baseline table, Decided parts and *Decision log*,
  `docs/BACKLOG.md` and `CLAUDE.md`. A part's note carries the human's answer to its stop; the
  coordinator writes it in at integration.
- **A part writes a part note instead,** `docs/spec/parts/<id>.<n>.md`, in its own branch
  (template at the end). It holds what the part built, measured and falsified, its numbers, and
  anything it could not finish. It is a file rather than a chat report because a report may
  reach the coordinator only in part and does not outlive the chat. The coordinator folds the
  notes into the done-note and deletes `parts/` in the session commit.
- **A part may change a doc of its own area,** such as one section of `ARCHITECTURE.md` or
  `USER-GUIDE.md`, when no other part touches that file and its brief names it.

**How a session runs with parts.**
1. **Plan, then look for parts** (the cycle, steps 3 and 4). No split is proposed before the plan
   is approved, and none starts without the human's clear yes. The coordinator never starts
   parts on its own initiative.
2. **Brief each part** from the template at the end. A part starts cold and is not a session:
   its brief replaces the cycle for it, whatever `CLAUDE.md` says every session does, and
   carries everything it needs, the setup a fresh checkout needs before `verify` runs included
   (ignored files do not come with a new checkout). Where parts meet, each brief carries the
   interface word for word, and names the tests that prove the seam only after the merge; the
   coordinator adds those at integration. Its stop rule is any session's: it never guesses to
   keep the parallel run going.
3. **Commit the contract,** when the parts meet at an interface (see *The contract*).
4. **Start each part** in a fresh checkout on its own branch, cut from the contract commit, or
   from the commit the session started on when there is none. The checkout lives outside the
   repository's folder, or in a path the project's tools ignore, so the coordinator's `verify`
   and harnesses never read a part's copy. Any tool that gives a chat its own checkout will do.
   In Claude Code, the coordinator can start each part as a parallel session in its own
   worktree, with the brief as its prompt; Claude Code puts the checkout under
   `.claude/worktrees/`, on a branch `claude/<name>`, which *Day one* has every tool ignore.
5. **While the parts work,** the coordinator edits no file a part owns. It may do a sequential
   step that no part touches, filling in its own stubs from the contract included, and commits
   it before the merges as a work commit, typed, with no version:
   `refactor: <what changed> (<id>, before the merges)`. It answers the parts' questions as
   *A part's questions* says. A part that waits for the human holds only the merge, and the
   other parts keep going.
6. **Each part commits on its branch** like any work commit: typed, with no version, naming the
   part (`feat: the search index for saved notes (part 8.2)`), with `verify` run on the drafted
   message last.

**Integration**, in this order:
1. **Wait for every part.** A part that stopped for the human holds integration until the human
   answers in that part's chat, or drops the part. A dropped part's steps go back into the plan
   as an amendment logged with the human, and with their yes the session commit removes or
   neutralises that part's stubs and registry entries from the contract, so nothing ships
   pointing at a stub. If the chat has to end first, the coordinator writes in the handoff
   which parts are open and on which branches (the mid-round template has the line), commits
   only the handoff as `docs: <id> paused at integration` with the docs-only command, and the
   next chat finishes this session from integration. Its done-note comes then, so rule 5 holds
   when the session ends.
2. **Check each branch against its brief:** `git diff --stat HEAD...<branch>` lists only what
   the part itself changed, even after it merged a contract change. If a part changed a file
   outside its list (its own note is always on it, and a file the human added is logged there),
   stop and show the human before merging anything.
3. **Merge, with the human's yes,** onto a tree with no uncommitted change outside the shared
   documents (no part touches those, and they wait for the session commit), in a stated
   order, one `--no-ff` merge per part, so history keeps each part visible. A merge is a
   commit like any other: `git merge --no-ff --no-commit <branch>`, a typed message drafted
   (`merge: part 8.1 — <what it adds>`), `verify` run with it, then `git commit -F`. A conflict,
   or a red `verify` on the merge, aborts it (`git merge --abort`) and goes to the human; the
   merge is redone only with their resolution, never with a guess.
4. **Prove the seam, then run the full gates once, on the combined code.** First add the
   end-to-end tests the briefs left to integration. Then run `verify`, every harness the block
   names, and the exclusive harnesses the parts could not run. The baseline counts must equal
   the starting counts plus each part's delta, the coordinator's own and integration's.
   Whatever fails here, the coordinator fixes in the session commit and records in the
   done-note's *Parts* section. A fix that changes behaviour or scope is the human's call first.
5. **Write the shared documents:** the done-note with its *Parts* section, the CHANGELOG entry,
   the version, the baseline and the handoff. Then the session commit, with `verify` run on its
   drafted message last, as always.
6. **Clean up,** right after the session commit, so no part leaves anything behind. For each
   part, `git worktree remove <path>`, then `git branch -d <branch>`, and the same for a
   contract-change branch; then `git worktree prune`. It is safe by construction: git refuses
   to remove a checkout that holds uncommitted or untracked work, and `-d` refuses a branch
   that is not merged. A refusal stops the cleanup and goes to the human; never `--force` or
   `-D` without their yes. A dropped part's branch was never merged, so it goes only with the
   human's yes, asked before the session commit; a branch they keep is listed as kept in the
   done-note's *Parts* section. A branch kept after a refusal here is recorded there by the
   review commit, which adds to the done-note anyway. The next session's entry gate checks
   that nothing else is left: the branches the *Parts* section names (the parts' and any
   contract change's) and their checkouts are gone (`git branch`, `git worktree list`). What
   remains goes into the session's plan and is removed the same way once the plan is approved;
   what git refuses goes to the human, and a branch listed as kept stays. A branch or checkout no
   done-note names is not the session's to remove: leave it.

**Limits.**
- **At most three parts per session,** to begin with. Each is another chat the human may need to
  answer and another branch to review. The limit can rise as more sessions run parts.
- **Parts do not split further.** A part never starts parts of its own.
- **Parts live inside one session.** Running whole sessions of a round in parallel touches the
  round plan, the handoff, versions and reviews at once, and is not part of this workflow.

## What each commit touches

Each commit's subject is in *Git*.

| Commit | Adds | Updates | Removes |
|---|---|---|---|
| **Intake** | the round's spec files and `SESSIONS.md`; in round 1, also `docs/ARCHITECTURE.md`, `CLAUDE.md`, this file and `docs/BACKLOG.md` | `docs/ARCHITECTURE.md`, in a later round whose request changes how the system is built; `docs/BACKLOG.md` (what the intake declined); the handoff, which now opens the first session | from `docs/BACKLOG.md`, the items the round picked up |
| **Contract** for a session's parts | the interfaces the parts meet at, as code: types, signatures and stubs that fail if called | the shared registries, with the entries the parts would each add, pointing at the stubs | — |
| **Part** of a session | the code and tests in the files its brief lists; its part note, `docs/spec/parts/<id>.<n>.md` | only the area docs its brief names | code the part retires, inside its own files |
| **Session** | the code and its tests; the version's CHANGELOG entry; the block's done-note | the manifest's version; `ARCHITECTURE.md` and its baseline; `USER-GUIDE.md`; `README.md`; `CLAUDE.md`; `docs/BACKLOG.md`; the handoff | code the session retires, and every doc line that described it; after parallel parts, `docs/spec/parts/` |
| **Before the merges**, the coordinator's own step while parts run | the code and tests of a step no part touches | its own stubs, filled in from the contract | — |
| **Merge** of a part, or of a contract change | the branch's commits, as one `--no-ff` merge, with the human's resolution of any conflict or red `verify`, and nothing else | — | — |
| **Paused at integration** | — | the handoff, naming the open parts and their branches | — |
| **Review** | the fixes and their tests; the done-note's Review section | that version's CHANGELOG entry; the docs the fixes touched; the handoff; `SESSIONS.md`, if the review opened a session | — |
| **Architecture review** | `docs/spec/REVIEW-<date>.md`; the block's done-note | `SESSIONS.md` (the blocks amended from it, a session it inserted, the versions that shift); the spec, where the human amended a decision; `ARCHITECTURE.md`'s Decided parts and *Decision log*, where the human changed one, and its Built parts the review found stale; the handoff | — |
| **Close**, after the round's last review | — | the handoff, with the sha of the review commit | every file in `docs/spec/` |

- **An intake's review** fixes the spec, the architecture and the plan. It has no CHANGELOG
  entry and no version. Neither has an architecture review, whose `/code-review` follows like
  any session's.
- **Before round 1's documentation pass**, `USER-GUIDE.md` does not exist yet. The CHANGELOG
  and the done-notes carry what it will need.
- **Never removed or rewritten:** a CHANGELOG entry's content; a done-note, which the review
  only adds to; a resolved decision in a spec file, which is amended beside itself rather than
  edited; a line of `ARCHITECTURE.md`'s *Decision log*.

## The rules

1. **One chat per session, never two sessions in one chat.** The split exists so no session
   inherits stale context or a half-formed plan. A session's parallel parts run in chats of
   their own, which the session starts and which end with it.
2. **The spec, and the Decided parts of `ARCHITECTURE.md`, are read-only to a session.** A
   session that finds either wrong stops and says so. Agreed divergence is recorded as an
   amendment in the block. A decision the human changes is added to the spec beside the
   original as a dated amendment, and the original text stays true to its moment; in
   `ARCHITECTURE.md` it is written into the Decided part, with a *Decision log* line.
3. **The plan is amendable, but every amendment carries a reason, logged.** An unexplained
   scope change six sessions deep is indistinguishable from a session quietly dropping work
   it could not finish.
4. **Nothing ships past a red gate.** `verify` green, or the docs-only command for a commit
   that changes only docs, is the condition for every commit (the cycle, step 6). No CI
   enforces it; the session does, and the human's review and push approval stand behind it.
5. **Every session ends with a done-note, a handoff and a commit.** No exceptions for short
   sessions. An intake's plan stands in for its done-note.
6. **Pushes and tags are a human decision**, approved one at a time.
7. **When a session goes wrong, stop** (step 5 of the cycle).

## Git

- **Commit locally; push only on explicit approval, each time.** Approval for one push does not
  extend to the next, and approving a plan is not approving a push. The human's review comes
  before the push.
- **Before any push, list `git log --format='%h %s' origin/main..HEAD`.** Parallel sessions may
  share a checkout, and a push carries whatever is on the branch, not only this session's work.
  If a commit is not this session's, stop and say so. A session's contract, its part commits,
  its work commit before the merges and the merges are its own.
- **Stage explicit paths; never `git add -A`.** Same reason.
- **Part branches** are merged only by the coordinator, never with git's own message, and
  never pushed (*Parallel parts*).
- **Never undo with `git checkout <path>`.** It silently discards changes that may not be
  yours. Revert your own edits by editing, and falsify a check by copying the file aside and
  back.
- **A commit subject is typed and names what changed in plain words**, the way a reader of the
  product would put it. The body says what changed and why.
  - `docs: open round <N> — <theme>` for an intake.
  - `feat:`, `fix:` or `refactor:` for a session's work, ending with the version when it cuts
    one: `feat: quiet copies — one a day, kept 7 days, restored from Help (0.41.0)`.
  - The same types for a parallel part's work, ending with the part and no version:
    `feat: the search index for saved notes (part 8.2)`. The coordinator's own step before the
    merges ends `(<id>, before the merges)`, and its contract `(<id>, the parts' contract)`:
    `refactor: the search index's interface, stubbed (8, the parts' contract)`.
  - `merge: part <id>.<n> — <what it adds>` for each part's merge, and
    `merge: the contract change — <what changed>` for each merge of a contract change.
  - `docs: <id> paused at integration` for a session whose chat ends with parts still open.
  - `docs: <what it wrote> (x.y.z)` for the round's last session when its own work is
    documentation.
  - `review: <the findings, in plain words>, and <n> smaller` for the review commit.
  - `docs: architecture review — <milestone>` for an architecture review.
  - `docs: close round <N>` for the close.
- **An approved push carries its own note.** The handoff was written before the push, so before
  pushing, the session rewrites the handoff's push status to say what the remote will hold,
  writes that commit's message into the draft (`git log -1 --format=%B`) and runs the
  docs-only command with it, since the note changes only the handoff. It folds the note into
  the last unpushed commit (`git commit --amend`; it is this session's own and not yet on the
  remote), lists `origin/main..HEAD` again, and pushes once. The note names that commit by its
  subject, since amending changes its sha. No commit follows the push, so the next session
  starts with `origin/main..HEAD` empty. If the push fails, amend the note back before anything
  else.
- **Tags mark milestones only**, such as a first build for testers or 1.0, and the intake names
  them: the session table marks a milestone's version as tagged. The session that cuts it asks
  before tagging, once the human has said whether to push; on a yes it tags locally as the
  chat's last act before its final opener, after the review, the close and any approved push,
  so the tag holds the review's fixes and no amend moves the commit from under it. The tag is
  pushed only with its own approval (`git push origin <tag>`); unlike a push of commits, that
  push adds no commit and carries no note.

## A clean repository

Every repository is written as if its history will be published, because any of them may be,
and the history is the one part that cannot be cleaned afterwards without rewriting it. It
holds nothing private, nothing a script can tell is broken, and nothing a change has left
behind: a gate holds what a script can judge, and a last read of each diff holds the rest.

**Nothing private.** Every file, test, fixture, done-note, handoff and commit message follows
these rules:

- **No personal names, no names of the owner's other projects or games, no agent personas.**
  Write the role: "the owner", "the first game", "the coding agent".
- **No home-directory paths.** Write `~`.
- **No AI attribution:** no co-author trailers, no lines saying a tool generated the work, no
  links to AI sessions, no AI credited as author, co-author or addressee. Naming a tool the
  product supports or the workflow uses is fine.
- **Fixtures are fictional** (see *Day one*).
- **Done-notes and handoffs never name the owner's own data:** their documents, folders,
  presets. Record what was measured, not whose it was.
- **Unsure whether something is public? Ask before writing it.** A session about to write a
  name, a place or a detail it cannot tell is public stops and asks the owner. A "private"
  answer goes on the term list, so the stage catches that word from then on; a "public" answer
  needs nothing. The list grows from real cases instead of a definition written up front.

What is already public is not private. The owner's name and email are on every commit as its
author, so they are private only when the commits use another identity; the same goes for what
the owner publishes on purpose, such as the copyright holder in the licence or a bundle id. The
intake decides what is private, and which git identity the commits use: the stage below reads
files and messages, not author fields.

**The hygiene stage of `verify` is the gate.** It holds only what a script decides with next
to no false alarms, because a check that blocks a session for nothing teaches sessions to route
around the gate. Each check names the failure it catches, and a hit fails the stage, except
one in pushed history (see *The full scan*):
- **Private terms,** from the owner's term list, in the files, paths and messages it reads.
- **AI attribution** in commit messages: a co-author trailer, a line saying an AI tool generated
  the work, a link to an AI session.
- **Secrets:** a private-key header, an access token in the exact shape its issuer gives it
  (AWS, GitHub, Slack, Anthropic, OpenAI), and a `.env` file a commit could record
  (`.env.example` is fine). A key in a pushed commit stays in history after it is revoked. The
  shapes are exact, and there is no generic `key=` pattern, because looser ones raise false
  alarms.
- **Conflict markers:** a line that starts with `<<<<<<< ` or `>>>>>>> `, left by a merge
  resolved by hand. In code they break the build, but in a document nothing else notices them.
  `=======` alone is not one: Markdown underlines headings with it.

Session 1 builds the stage in the project's own language, from the design in the workflow
kit's `KICKOFF.md`, which Session 0 copies into Session 1's block; from then on the stage's
code holds the design, and ARCHITECTURE's testing strategy describes it.
- **The term list lives outside every repository,** in one plain-text file,
  `~/.config/hygiene/terms.txt`: one word per line, shared by all of the owner's projects,
  because a name private in one is private in all. No repository holds the terms, nor hashes
  of them: a short word's hash is reversed by hashing a dictionary of names. A missing file
  fails the stage, so a new machine cannot pass by accident; copying that one file is the whole
  setup. An empty file is a valid answer: nothing is private beyond what is already public.
- **A term is one word.** A two-word or hyphenated name is given as its words, leaving out any
  that is an ordinary word on its own. The owner edits the file, or names a new term in chat
  and the session adds it with their yes. Either way, each project's next run reads everything
  again (below), so a new term needs no further step.
- **A hit never prints the term or the secret.** It names the file and line, or the commit and
  message line; the line itself shows what it is.

**What each run reads.** Rereading what already passed finds nothing new, so a routine run
reads only what a commit could still change: the drafted message, the files the commit could
record (staged, unstaged, and untracked but not ignored), and the commits on no remote yet,
with the files they changed as they stand now, so a commit made without `verify` (by hand, or
by git's own merge) is caught before it is pushed.

**The full scan reads every file and every commit message,** the draft included. It runs by
itself when it can find something new: on a fresh clone, and after the term list or the
stage's own code changes, so a term added in any project brings one full scan in each without
anyone having to remember it. `verify hygiene --all` runs one on demand. A hit in a pushed
message does not fail: history is never rewritten without the owner, so failing would only
hold the gate red. The stage ends instead with a line of its own saying how many hits pushed
history holds, and the session records them for the owner in the done-note and the handoff (a
part, in its part note). A full-scan hit in a file fails like any other and is fixed; when the
session did not change that file, the owner hears of it too, since its earlier versions may
already be pushed.

**When it runs: once, as the last act before each commit, message included.** The session
writes the done-note and the handoff, reads its diff once more for what no script judges
(below), drafts the commit message into the draft file `COMMIT_DRAFT` in the git directory
(`"$(git rev-parse --git-dir)/COMMIT_DRAFT"`: `.git/` in a plain checkout, elsewhere in a
worktree, never committed either way), runs `verify` with it
(`<verify command> --message <draft>`, or the docs-only command for a commit that changes only
docs), and commits with `git commit -F <draft>`. The draft is written fresh for every commit
and deleted after it, so an old message is never committed again. The stage checks the draft
beside the files and the unpushed messages, so nothing is checked after the fact and no commit
is amended for it. The review commit and the push note's amend go the same way.

**What no script judges.** That last read of the diff looks for what needs judgement:
- the message says what changed and why, the way a reader of the product would put it (*Git*);
- no dead code, and no code left commented out;
- comments state the present (*Engineering practices*);
- no file the change made obsolete stays;
- the docs that describe the change are true (the cycle, step 7);
- nothing private the stage cannot see: a home-directory path, attribution in a file, the
  owner's data.

A finding is fixed, or left with its reason, like a review finding: in the done-note, or in the
commit message where there is none (an intake and its review, or the close).

**Watch for:**
- **A commit message that quotes an attribution form,** even to describe this rule, fails the
  stage. Describe it in words.
- **A test that needs a token-shaped string or a conflict marker** builds it from pieces at run
  time, as the stage's own source builds its patterns. A file that holds one fails the stage.
- **A document that describes conflict markers** writes them inside a sentence, never at the
  start of a line.

## Versions and the changelog

- **Each session is a release.** `SESSIONS.md`'s table gives each session its version:
  - a major bump for round 1's last session, which releases the full working product as
    `1.0.0`, and after that only when the human decides at an intake that a round is a new
    major version;
  - a minor bump for a session that adds a feature or capability, or changes behaviour;
  - a fix bump for a session that only fixes defects or does maintenance;
  - no bump for a session that changes no product code, such as an architecture review, except
    the round's last session, which releases the round.

  The version is `major.minor.fix` in the manifest and is shown in the product.
- **One entry per version**, `## [x.y.z] — YYYY-MM-DD`, using only Keep a Changelog's headings
  (Added, Changed, Deprecated, Removed, Fixed, Security). Prose that fits none of them goes in
  the entry's lead paragraph. `[Unreleased]` stays at the top and stays empty, because each
  session writes its own version's entry.
- **Written for the person using the product.** Each line leads with what they will notice, in
  bold, then what it means for them. No file names, no session ids. A maintenance version with
  nothing to notice says so in one line under Changed.
- **Review fixes join the session's entry**, under the same version.
- **Append-only for content.** A shipped entry's substance is never reworded. Normalising a
  heading to the set above is allowed.
- **Every version has a link reference** at the foot of the file once the repo has a remote.
  A tagged version links to its tag, and an untagged one to the commit that bumped the manifest
  to it. `[Unreleased]` compares the newest tag with `HEAD`; until the first tag it has no link.

## The handoff

`docs/next-session-prompt.md`, rewritten by every session (the templates are at the end of this
file). The chat's last message is never the handoff itself, only the one-line opener that
points at it (the cycle, step 12), so the next session reads the handoff from the repository,
as committed. It holds:

- **The opening paragraph:** the read order (the block's Read line, copied), the session to do
  and what it covers, and the version it releases.
- **State you need that is not in the specs:**
  - the round's progress: which sessions are done, which remain;
  - the push status: what the remote holds (`origin/main` holds everything through `<sha>`),
    and which local commits wait for the next approved push;
  - what shipped that this session builds on, specifically: the names, files and mechanisms
    it will touch, as they are now;
  - what deferred work this session now owns;
  - what the spec said that turned out wrong or harder than described (be specific — this is
    the part that saves a session);
  - decisions made that are written down nowhere else;
  - the baseline counts this session must not move, or must move by a stated amount;
  - what was not done, and why.
- **Watch for:** this session's own traps, the block's plus anything newly discovered. The
  standing traps, the environment's gotchas that every session hits (the shell, the toolchain,
  the harnesses, git), live in `CLAUDE.md`'s *Watch for* section instead, which says when one
  goes in and when it comes out.

Two rules govern it:

1. **Report what happened, not what was intended.** If something was skipped, say it was
   skipped and why. A handoff that describes the plan rather than the outcome is worse than
   no handoff, because the next session trusts it.
2. **It adds context; it does not replace the contract.** The next session still reads the
   spec first.

When no round is in progress, the handoff says so in its first line, the opener says so too,
and the next session is an intake.

## Engineering practices

- **Falsify every new check before believing it.** Break the assertion, watch it fail at its
  own step and nowhere else, restore it. A check that cannot fail looks identical to a passing
  one. When two layers guard one promise, break the layer the check is about, or the
  falsification passes for the wrong reason.
- **Keep a baseline of counts** (tests passed and skipped, harness checks, endpoints or
  channels) in `ARCHITECTURE.md`. A refactor or a docs change must not move any of them; if
  one moves, that is the finding.
- **Measure, don't assume.** A claim about how the runtime behaves (a timestamp, a platform
  default, a size) is measured in the real runtime and recorded in the done-note as measured,
  with the version it was measured on.
- **Real-runtime probes for anything version-sensitive.** When the test runner and the shipped
  runtime differ, keep one-command probes that re-answer the load-bearing questions inside
  the real runtime.
- **Record checks by hand too.** When the human tries the build, or a session runs something no
  harness can, the done-note records each outcome. What nobody checked goes to BACKLOG's *Not
  yet checked by hand*, with the automated check that covers most of it.
- **Design for headless drivability.** Automation never opens anything it cannot dismiss
  (native dialogs, OS prompts, modal pickers). Split every dialog-then-write flow into two
  separately drivable steps, so a harness asserts the control and drives the write directly.
- **Harnesses own their state and clean it up structurally.** A harness creates its own data
  directory, never touches one a person owns, and registers its cleanup with the runner
  rather than relying on each caller to remember. Sweep stale leftovers at startup, which
  covers a run that was killed. Measure the leak before and after rather than assuming.
- **Measurements are committed tests.** A performance number that matters lives in a gated
  benchmark with a budget that fails rather than warns, not in a table typed by hand.
- **A test whose outcome depends on the clock pins the clock.** Otherwise it can pass
  vacuously for weeks.
- **One home per shape.** A duplicate that has drifted once will drift again. The second
  copy of a component, hook or rule is the moment to share it, not the fifth.
- **Comments and names state the present.** A comment, a name or a test title says why the
  code is shaped the way it is now. It never carries a session id, "used to", "until v0.x" or
  a review story; git history and the done-notes keep those. Where the story *is* the reason,
  keep one clause.
- **"Watch for" lines.** Every session block ends with its specific traps, because traps are
  what a fresh context misses; a trap every session can hit goes into `CLAUDE.md` instead (*The
  handoff*).
- **Deviations over corrections.** When mockups, spec and build disagree, resolve the conflict
  once, write down which one wins and why, and leave the artifacts as they are.
- **Keep the rules file lean.** `CLAUDE.md` holds what is always true; the done-notes and
  `ARCHITECTURE.md` hold why. A rule keeps its "why" only when the why changes the action.
  Duplicating prose between them guarantees drift.
- **Keep `ARCHITECTURE.md` readable by section.** A session reads its overview, invariants and
  baseline, and only the sections its block names, so each section stands on its own. A
  deliberate decision lives in the section of the subsystem it belongs to; the closing
  *Deliberate decisions* holds only the ones that span subsystems, and a decision about a
  single module is that module's comment. Without this the file grows into one list nobody can
  read in a session: one project's reached 3,200 lines, half of them a single list of
  decisions.
- **Adversarial plan review.** A separate agent attacks a plan before the human sees it. It is
  costly, so it runs only on the human's yes, and asking says so. Session 0 asks at its intake,
  recommending yes. Any other session or intake asks only when its plan warrants it (the cycle,
  step 3): a proposed change to a Decided part, data that cannot be rebuilt or a public
  interface are the usual reasons, and most sessions have none. One run sets no rule for the
  next.
  - **Who:** a read-only subagent in a fresh context, on the strongest model available or one
    the human names (in Claude Code, a subagent with its model set). The fresh context does the
    work, so planning on the strongest model already is no reason not to ask.
  - **What it gets:** the plan file and, by path, what the plan rests on, with `docs/BACKLOG.md`
    once it exists. It is asked what is wrong, what is missing and what will fail. It is not
    told what the session is worried about.
  - **One pass.** It runs once the plan is written, and is not rerun. The session checks every
    finding against the sources and against what the human said, because some are wrong, and
    folds in what holds. A finding that changes a decision or the scope is the human's call.
  - **The plan ends with what it changed and what it rejected, and why.** The plan file is not
    in the repository, so a rejection that could come up again is written down: what the human
    settled is recorded as a decision, and a judgement goes to `docs/BACKLOG.md`'s *Decided
    against*. It does not replace the code review (the cycle, step 11).

## Adapting the workflow

The method was written on a desktop app with a UI, a local database and several harnesses.
Other projects keep its core, adapt the rest, and say which parts they adapted in their *In
this repository* paragraph.

- **The core, which no project drops:**
  - scope and state kept apart: `docs/spec/` and the handoff;
  - one session per chat, planned with the human before any edit;
  - stopping to ask rather than guessing;
  - intake decisions that are not re-litigated, and amendments logged with their reasons;
  - a done-note, a handoff and a local commit at the end of every session, then the human's
    review and a separate review commit;
  - pushes and tags only with approval;
  - every new check falsified;
  - a clean repository: nothing private, no secret and no conflict marker, enforced by the
    hygiene stage.
- **What depends on the project:**
  - what `verify` runs, and which harnesses exist beside it;
  - whether every session cuts a version and a CHANGELOG entry, or the project releases at
    milestones;
  - whether there is a user guide, and what "user-visible" means;
  - headless drivability, which matters only where there is something to drive;
  - the git remote, which decides pushes, tags and changelog links;
  - CI, which this workflow does not use; a project that adds it says so;
  - parallel parts, which are optional (see *Parallel parts*).

## Templates

Each template is generalised from a real round. Fill every `<…>`; the text around it is the
real wording, to be kept unless it is wrong for the project.

### `docs/spec/SESSIONS.md`: the header and the table

In round 1 the spec files are `SPEC.md` and `PDD.md`.

```markdown
# The session plan: round <N>, <theme>

One block per session, in order, each run by *The session cycle* in
`docs/DEVELOPMENT-WORKFLOW.md`. The request and its resolved decisions are in
`<FEATURE-name.md>` beside this file, which is read-only; do not re-litigate them. A session
that finds its block wrong amends it and records the reason in the block and in
`docs/next-session-prompt.md`. <last id> closes the round: it deletes this file and the
feature file(s), and anything left open moves to `docs/BACKLOG.md`.

| Session | Scope | Decisions | Version |
|---|---|---|---|
| <id> | <one line> | <decision numbers; `ARCHITECTURE.md` sections> | **<x.y.z>** |
| <id> | Architecture review: <milestone> | <decision numbers> | — |
| <last id> | Docs, changelog, manual runs; the round's `ARCHITECTURE.md` sections read cold; close the round | <decision numbers> | **<x.y.z>**<, tagged, when the intake made it a milestone> |
```

### A session block

```markdown
---

## <id>: <title>

<Only for a session inserted mid-round: when and why it was added, in the user's words where
they gave them.>

**Read:** `<spec file>` <decisions by number, sections by name>; `PDD.md` <parts and items, in
round 1>; `ARCHITECTURE.md` <invariants by number, sections by name>; `REVIEW-<date>.md`
<findings, where a review amended this block>; `DEVELOPMENT-WORKFLOW.md` <sections beyond the
cycle it builds from>.

- **<Scope item>** (decision <n>, or the `ARCHITECTURE.md` section that decides it).
  - <What changes, with `file:line` pointers to the code as the intake saw it.>
  - <The constraints: which invariant it touches, which layer the new code belongs in.>
- **<Scope item>** (decision <n>).
- **Docs.**
  - `CLAUDE.md`: <the rule that changes>.
  - `USER-GUIDE.md`: <the sections that change>.
  - `ARCHITECTURE.md`: <the sections that change>.
  - README: <what changes>.
- **Confirms** (*The documents*): <the Decided parts of `ARCHITECTURE.md` this session is the
  first to build on, or leave the line out>.
- **Ask at the start of <id>:** <a decision left to this session, because only it will have
  the context>. <For a proposal the user has not confirmed: "Proposed at intake, not yet
  confirmed.">

**Gates:**
- `<verify command>`, with these tests:
  - <each behaviour the session must prove>.
- `<harness>`: <what it must show>.

**Watch for:**
- **<The trap>.** <Why it bites, and what to do instead.>
```

### The done-note

The session appends it to its block before the local commit; the review adds its section
before the review commit. Leave out a line that has nothing in it.

```markdown
**Done (<YYYY-MM-DD>, <x.y.z>).**
- **Decided with the user:**
  - <each *Ask at the start* answer, anything settled in plan mode or at a stop, and each part
    under **Confirms**, confirmed or changed>.
- **<What shipped, one bullet per area>.** <The names, files and mechanisms, as built.>
- **Amendments:**
  - **<What differs from the block>.** <Why, and who decided: "amended at plan time, with the
    user", "added mid-session by the user", or the session's own finding.>
- **Revised:** <each earlier session's decision in a Built part of `ARCHITECTURE.md` that this
  session changed: the section, what changed, and why>.
- **Measured:** <each claim about runtime behaviour, and the version it was measured on>.
- **Checked by hand:** <each manual run, and the user's look at the build, with the outcome.
  What was left unchecked goes to `docs/BACKLOG.md`.>
- **Falsified:**
  - <each new check: what was broken, and that it failed at its own step>.
- **Numbers:** <n> unit tests (<±d>), <n> `<harness>` checks (<±d>), <the other baseline
  counts>.
- **Parts** (<n>, run in parallel with the user's yes; <the contract-change branch, if there
  was one>; cut from <the contract commit, by its
  subject, or the commit the session started on>; merged in the order <id>.<n>, <id>.<n>):
  - **<id>.<n>, <title>,** on `<branch>`. <What it built, measured and falsified, from its
    note; each stop, who answered it and the answer; anything it could not finish.> Wall time
    <hh:mm>–<hh:mm>.
  - **The coordinator, meanwhile:** <the contract, its own steps, and its commits before the
    merges>.
  - **Integration fixes:** <the end-to-end tests that prove the seam, and each failure the
    combined gates found, with its fix>.
  - **The counts add up:** <the starting counts, plus each part's delta, the coordinator's and
    integration's, summing to the baseline>.
  - **Time saved:** <about how much, against an estimate of the same steps one after another;
    what the split did not shorten>.
  - **What the briefs missed:** <each gap a part had to stop on, or "nothing">.
  - **Merge trouble:** <each conflict and how the user resolved it, or "none">.
  - **Kept:** <a part branch the user chose to keep, and why; the cleanup removed the rest>.
- **Review (`/code-review high`), <n> findings: <n> fixed and <n> skipped.**
  - **<The finding, as fixed>.** <One line; "the user chose" where they decided.>
  - **Skipped:** <the finding>, because <the reason>.
  - **Falsified:** <the checks the fixes added>.
  - **Numbers after the review:** <counts>.
```

### A part brief

The coordinator writes one for each parallel part and gives it to the part as its first message
(see *Parallel parts*). Fill every `<…>`.

```markdown
You are part <id>.<n> of Session <id>, in a checkout of your own, on a branch cut from
`<sha>` (<the parts' contract, or the commit the session started on>). The scope below is from
the plan the user approved in Session <id>'s chat; work inside it. Read <the Read line>,
CLAUDE.md, then this brief.

**Background.** <One paragraph: what Session <id> builds and why, what the other parts and the
coordinator build meanwhile, and where this part meets them.>

You are not a session. This brief replaces the session cycle for you, whatever CLAUDE.md says
every session does: no entry gate, no plan mode, no done-note, no handoff, no CHANGELOG entry,
no version and no `/code-review`; the coordinator's review covers your commits.

**Scope**, in the approved plan's words:
- <each plan step this part owns>.

**The interface**, word for word from the plan: <only where this part meets another: the
signatures, types and registry entries, as the contract holds them>. Changing it is a stop.

**Files you may change:** `<path>`, `<path>`, and your note. To touch any other file, stop and
ask.

**Setup:** `<what a fresh checkout needs before verify runs>`.

**Starting counts** at `<sha>`: <n> unit tests, <the other baseline counts>.

**Gates:**
- `<verify command>` green on this branch, with these tests:
  - <each behaviour the part must prove>.
- Each new check falsified once.
- Do not run `<the exclusive harnesses>`; integration runs them.
- **Proved only after the merge:** <the end-to-end tests across the seam>. Do not write them;
  the coordinator adds them at integration.

**Your note:** `docs/spec/parts/<id>.<n>.md`, committed with your work. It holds what you built,
measured and falsified; your numbers, from the starting counts above; your wall time, from
start to commit; what the shared documents need (CHANGELOG lines, ARCHITECTURE sections and
counts, backlog items); each question you asked, who answered it and the answer; and anything
not finished.

**Commit** on this branch: `<type>: <what changed> (part <id>.<n>)`, with no version, and
`verify` run on the drafted message last.

**Never:** write `SESSIONS.md`, the handoff, `CHANGELOG.md`, the version, ARCHITECTURE's
baseline, Decided parts or *Decision log*, `docs/BACKLOG.md` or `CLAUDE.md`; cherry-pick; merge,
except a contract change the coordinator sends you; push; start parts of your own.

**Stop** when the spec or `ARCHITECTURE.md` turns out wrong, a decision is underdetermined or
the interface does not hold, and ask the coordinator: <how this part reaches it: through the
user, or a message to Session <id>'s chat>. The coordinator answers what the approved plan
settles; anything that changes behaviour, scope, the interface or your file list goes to the
user. Wait for the answer, and never guess to keep the parallel run going.

**Watch for:**
- **<A trap of the block's that reaches this part>.** <Why it bites, and what to do instead.>
```

### `docs/spec/parts/<id>.<n>.md`, a part note

The part commits it with its work. The coordinator folds it into the done-note's *Parts* section
and deletes it in the session commit. Leave out a line that has nothing in it.

```markdown
# Part <id>.<n>: <title>

- **Built:** <the names, files and mechanisms, as built>.
- **Measured:** <each claim about runtime behaviour, and the version it was measured on>.
- **Falsified:**
  - <each new check: what was broken, and that it failed at its own step>.
- **Numbers:** from <the brief's starting counts> to <n> unit tests (<±d>), <the other counts
  this part moved>.
- **Wall time:** <hh:mm>–<hh:mm>.
- **For the shared documents:** <the CHANGELOG lines, the ARCHITECTURE sections and baseline
  counts, and the backlog items, for the coordinator to write>.
- **Stopped:** <each question, who answered it (the coordinator or the user), and the answer>.
- **Not finished:** <what, and why>.
```

### `docs/spec/FEATURE-<name>.md`

```markdown
# FEATURE: <name> (round <N>)

## The request, verbatim (<YYYY-MM-DD>)

> <The user's words, exactly as given.>

<One paragraph: what the intake did (an audit, a proposal of groups of work), what the user
took and what they declined, and anything they said about audience or platform.>

## <Optional: the promise or contract the round exists to keep>

## Resolved decisions (<YYYY-MM-DD>, at intake)

An answer about how the system is built is not here: it is in `docs/ARCHITECTURE.md`, in the
section it belongs to.

1. **<The decision, in one sentence>.** <The detail a session needs, and the why where the
   why changes the action.>
2. **<The sessions, in order>:** <ids and versions>, when the intake decided them.
3. <…>
<n>. **Out of this round:** <what was declined or deferred; each item also goes to
   `docs/BACKLOG.md`>.
```

A decision the user changes later is added beside the one it changes, never edited in:

```markdown
**Amended <YYYY-MM-DD> by the user, in <id>.** <Which decision changes, to what, and why.>
```

### `docs/spec/REVIEW-<date>.md`, an architecture review

Two rules make a review worth its session. The read is done twice, the second time cold,
without sight of the first read's notes, and a finding is kept only once it has been verified
on the code path. Every claim points at `file:line` on a named commit, or at a measurement.

```markdown
# Review <id>: the architecture after the <milestone> milestone

Session <id> of round <N>, <YYYY-MM-DD>. The code and tests of sessions <ids> were read cold
against `ARCHITECTURE.md` and `<spec file>` <sections>. This file is evidence, not scope: it
changes no product code and cuts no version. The user chose, in plan mode, which findings
become scope; §6 says where each landed.

**Method.** <What was read in full, and against what; the second, independent read, and how its
findings were verified; what was run and measured, before and after.>

**Severity.** *High*: an invariant is weakened, or a planned session is blocked as written.
*Medium*: a defect or debt that will cost a later session, or a boundary or invariant whose
check was due by now and does not exist. *Low*: drift or untidiness. *Info*: recorded, no
remedy.

## 1. The baseline as found

| Check | Found |
|---|---|
| `<verify command>` | <stages, counts, times> |
| `<harness>` | <counts, wall time> |

## 2. What holds

<Each boundary and invariant that holds, and where it is enforced (`file:line`).>

## 3. Findings

### High

**F1. <The finding, in one sentence>.** <The evidence, at `file:line` or as a measurement;
what it costs, and which session it reaches.> *Remedy:* <the proposed fix>.

### Medium

### Low

### Info

## 4. Duplication and drift

## 5. <The subsystems> against sessions <ids>

<What the sessions ahead will put through the code as it stands, and what has to change first.>

## 6. Where each finding landed

Decided by the user in plan mode, <YYYY-MM-DD>:

| Finding | Where |
|---|---|
| F1 | Block <id>: <the amendment> |
| F<n>, F<n> | Inserted session **<id>a: review fixes — <milestone>**, <x.y.z>; later versions shift |
| F<n> | `ARCHITECTURE.md` <section>: the Built part corrected in this session |
| F<n> | Recorded here; nothing to do |

## 7. Measured

<Each measurement, and the version it was measured on.>
```

### `docs/next-session-prompt.md`, mid-round

```markdown
Read <the block's Read line, copied>, CLAUDE.md, *The session cycle* in
docs/DEVELOPMENT-WORKFLOW.md, docs/ARCHITECTURE.md's overview, invariants and baseline,
docs/spec/SESSIONS.md's header, your block and the previous block's done-note, then this file,
and do Session <id>: <one line>. <id> covers:
- <part>;
- <part>.

Release <x.y.z>.

## State you need that is not in the specs

- **Round <N> is <theme>**: <ids> are done; <ids> remain.
- **<Previous id> and its review fixes are committed locally, not pushed.** `origin/main` holds
  everything through `<sha>`.
- **What <previous id> left that <id> builds on:**
  - <the names, files and mechanisms this session will touch, as they are now>.
- **What the spec said that turned out wrong or harder:** <specifically>.
- **Decided parts of `ARCHITECTURE.md` changed since the plan was written:** <the section, and
  the later blocks amended for it>.
- **Decisions written down nowhere else:** <…>.
- **Baseline** (ARCHITECTURE's table, v<x.y.z>): <the counts>.
- **Not done:** <what was skipped, and why>.
- **<Only when a session ended with a parallel part still open:> <id> is unfinished.** Part
  <id>.<n> is open on `<branch>`, waiting for <the question>; parts <ids> are finished on
  `<branches>` and not merged. The next chat finishes <id> from integration and starts no other
  session first.

## Watch for

- **<A trap specific to this session>.** <Why it bites, and what to do instead.>
```

### `docs/next-session-prompt.md`, between rounds

```markdown
No round is in progress. Read CLAUDE.md, *The session cycle* in docs/DEVELOPMENT-WORKFLOW.md,
docs/ARCHITECTURE.md's overview, invariants and baseline, then this file; then the sections of
docs/ARCHITECTURE.md the request touches, and any a block will point at. The next session is
an **intake**: write the user's request down verbatim, ask what it leaves open,
and plan the round in `docs/spec/`, a Read line in every block (see
`docs/DEVELOPMENT-WORKFLOW.md`, *Rounds*).

## State you need that is not in the docs

- **<Product> <x.y.z> is released.** Round <N> (<theme>: <ids>) is closed. Its spec files are
  deleted; the last done-note is in `docs/spec/SESSIONS.md` as of the review commit before the
  close (`<sha>`, filled in by the close).
- **Push status:** <what the remote holds, and what waits for the next approved push>.
- **Open items live in `docs/BACKLOG.md`**, <including what this round added there>.
- **Baseline** (ARCHITECTURE's table, v<x.y.z>): <the counts>.

## Watch for

- **<A trap the intake should know>.** <Why it bites, and what to do instead.>
```

### `docs/BACKLOG.md`

```markdown
# Backlog

Work that has been named but belongs to no session. Each item goes through an intake before it
runs (a `docs/spec/FEATURE-*.md` with the request verbatim and the decisions resolved, then a
block in `docs/spec/SESSIONS.md`; see `docs/DEVELOPMENT-WORKFLOW.md`). When an item is picked
up, it moves out of this file.

## Deferred

- **<The item>.** <What it is, and where it was left out: "left out at the round <N> intake".>

## Not yet checked by hand

Checks that need a person at the machine. Each has an automated check covering most of it;
these are the parts only a person can see.

- **<What to check>** (<version>): <how to check it, and which automated check covers the rest>.

## Directions

- **<A possible future>.** <What it would be, and what already points towards it.>

## Decided against

- <What, and the reason in a clause.>
```

### `CHANGELOG.md`

```markdown
# Changelog

All notable changes to <Product> are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow
`major.minor.fix`.

## [Unreleased]

## [0.2.0] — <YYYY-MM-DD>

### Added

- **<What the user notices>.** <What it means for them.>

### Fixed

- **<What now works>.** <What went wrong before.>

## [0.1.0] — <YYYY-MM-DD>

### Added

- **<…>.**

[Unreleased]: <repo URL>/compare/<newest tag>...HEAD
[0.2.0]: <repo URL>/commit/<full sha of the commit that bumped the manifest to 0.2.0>
[0.1.0]: <repo URL>/commit/<full sha>
```

### `docs/ARCHITECTURE.md`: the outline

Session 0 writes it from the intake, and every session after keeps it true (*The documents*).
Keep every section, writing "None" where one has nothing: the Read lines point at its sections
by name. It outlasts every round, so it states what it needs and never points into a spec file
or the draft, which the round's close deletes.

````markdown
# <Product> — architecture

How the system is built. **Decided** is the user's: what an intake answered or the user
settled with a session. It changes only with the user, and each change after Session 0 is
logged in the *Decision log*. **Built** is what exists and how, with the decisions a session
made on its own within its scope, each with its why; every session keeps it true. Until
something is built, its Built part says "Not yet: Session <id>", or "Not yet: backlog, <item>"
once the round that planned it closes without it. In the invariants, each rule and its why are
decided and *Enforced by* is built; the debt and the baseline are built only.

## Overview

**Decided.**

```
<The layers, and what crosses between them>
```

<One paragraph: what each layer is for.>

**Built.** <What exists of it so far, or "Not yet: Session <id>.">

## Context

**Decided.** <Each external system the product talks to or runs inside (an app it drives, a
service it calls, an OS facility it relies on), or "None": what crosses the boundary each way
and in what form, which side owns it, the versions supported, how it fails and what the product
does then, and what the product must never assume about it.>

**Built.** <How the product reaches each one, and what was learned about it: quirks, measured
behaviour, the versions tested.>

## Stack and pins

**Decided.** <Each language, framework and runtime with its pin and why it is pinned, dated
<YYYY-MM-DD>; where the test runner's runtime differs from the shipped one, and which check
runs in the shipped one.>

**Built.** <The runtime versions measured on this machine, not assumed, and when.>

## Layout and boundaries

**Decided.**
- **Layout** (Session 1 creates it; the names are fixed, the files inside are each session's):
  `<folder>/`: <what lives there>.
- **Boundaries:** <what each layer may import, call and own, and what it may not; where a
  constant two layers share lives>.

**Built.** <For each boundary, *Enforced by*: the import rule, lint rule or test that fails when
it is crossed, or "Not yet: Session <id>".>

## The invariants

<Numbered. Each rule and its *Why* are decided. *Enforced by* is built: it names what fails when
the rule breaks, and until that check exists, the session that builds it.>

1. **<The rule>.** *Why:* <one line>. *Enforced by* <the lint rule, type, test or harness
   check>.
<n>. **Nothing private enters the repository.** *Why:* any repository may be published, and
   history cannot be cleaned without a rewrite. *Enforced by* the hygiene stage (Session 1
   builds it; until then, Session 0's check of the term list): the owner's term list against
   every file, path and commit message, attribution against every commit message, and secrets
   by their exact shapes.

## <The contract between the layers>

**Decided.** <The protocol, threading and runtime facts, stated here in full.>

**Built.** <The messages, channels or endpoints that exist, each within the decided protocol.>

## <The data layer: storage, migrations, backups, durability>

**Decided.**
- **Entities and storage:** <the shape of the data, where it lives, and each store's lifetime:
  permanent, rotated, swept at start, removed on close>.
- **Evolution:** <migrations or versioned formats, forward-only unless decided otherwise, and
  how a newer version is refused>.
- **Machine identifiers, never renamed:** <package name, storage keys, bundle id, data
  directory, environment variables>, because data lives under them.

**Built.** <The entities, fields, tables and migrations that exist.>

## <One section per subsystem>

<Each section stands on its own, because a session reads only the sections its block names.>

**Decided.** <What the subsystem does and its contracts, as the intake or the user settled
them.>

**Built.** Not yet: Session <id>. <Once built: the names, files and mechanisms, and the
decisions a session made on its own, each with its why. If the round that planned it closes
without building it: "Not yet: backlog, <item>.">

## Testing strategy — <n> layers, and what each cannot see

**Decided.** **`verify`** runs named stages, each failing on its own and runnable alone by name,
then a summary: <the stages>, then hygiene. It is green before every commit, or the docs-only
stages for a commit that changes only docs. The harnesses: <each one, and what it drives>. The
commands themselves are in `CLAUDE.md`.

**Built.**

| Layer | Runs | Covers | Cannot see |
|---|---|---|---|
| Unit | `verify` | <…> | <…> |
| Hygiene | `verify`, with the drafted commit message; in full when the term list or the stage changes | Private terms in files, paths and messages; attribution in messages; secrets by their exact shapes; conflict markers | Images and binaries; a term joined inside one lowercase run; attribution in files; a home-directory path; a secret of any other shape |
| <Harness> | <the sessions that run it> | <…> | <…> |
| Architecture reviews | At the milestones of a round of more than five build sessions | The code against this file and the round's spec | Runtime behaviour |
| By hand | Recorded in done-notes | <…> | Anything not written down; what nobody checked goes to the backlog |

## Packaging

**Decided.** <How it is built, signed, installed and updated, or explicitly not.>

**Built.** <What exists of it, and what has been tried by hand.>

## Deliberate decisions

**Decided.** <Only the choices that span subsystems and look wrong until you know why, each with
its why. Each is the user's; a session that needs one asks. A decision that belongs to one
subsystem lives in that subsystem's section.>

## Known debt, deliberately deferred

<Built only: what was left, why, and what it will cost.>

## Baseline

<Built only. Session 0 writes this line alone: "Filled in by Session 1, from its first green
`verify`." Session 1 replaces it with the table and adds its version to the heading:
`## Baseline (v<x.y.z>)`.>

| Check | Expected |
|---|---|
| `<verify command>` | green — <n> unit tests passed (<n> skipped: <which, and why>) |
| `<harness>` | <n> PASS; <how long it takes, and its quirks> |
| <an interface count: channels, endpoints, commands> | <n> |

A documentation or refactoring change should not move any of these. If one moves, that
is the finding.

## Decision log

<One line for each change the user made to a Decided part after Session 0, a new decision or a
changed one, oldest first, written with the change: <YYYY-MM-DD>, <section>: <what changed>,
instead of <what it was, or the alternative set aside>, because <why>. Session 0's decisions
are not logged; the file starts from them.>
````
