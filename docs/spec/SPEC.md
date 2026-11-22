# claude-skills — the round 1 contract

Read-only from the first line of Session 1. Session 0 derived it on 2026-11-17 from
`docs/spec/PDD.md` (Part A, the owner's request; Part B, the crux-finder draft v1.2; both
frozen). The PDD states intent and this file is the contract for what the round delivers: where
they differ, this file wins, and §3 lists every place they do. How the system is built is in
`docs/ARCHITECTURE.md`, which Session 0 wrote beside it and which outlasts the round. The
itinerary skill's audit is `docs/spec/REVIEW-2026-11-17.md`, which is evidence; it became scope
only through decision 8.

## 1. Resolved decisions (2026-11-17, at intake)

Decisions 1–14 were answered by the user at intake. Decisions 15–23 were proposed by the intake
from the PDD and approved with the Session 0 plan. Decisions 24–30 are the ones every project
records. The last collects what round 1 leaves out. None is re-litigated by an implementing
session; a change is added beside the decision as an **Amended <YYYY-MM-DD> by the user** note.
An answer about how the system is built is not here: it is in `ARCHITECTURE.md`, in the section
it belongs to.

1. **Every skill is its own Claude Code plugin, in this repository, in one marketplace.**
   crux-finder lives here, not in a repository of its own as PDD B, *Repo structure* has it, and
   the itinerary skill moves into the same shape. The layout is `ARCHITECTURE.md`, *Layout and
   boundaries*.
2. **One round for everything:** the scaffold, the restructure, the itinerary fixes and
   crux-finder through its 1.0.0.
3. **Each skill has its own version and its own changelog.** The version is in the plugin's
   `plugin.json`; the changelog is the plugin's `CHANGELOG.md`.
4. **No CI.** PDD B, *CI* is dropped. Both validators it names run inside `verify` instead
   (`ARCHITECTURE.md`, *verify*), and `verify` is green before every commit.
5. **Commits use this machine's git identity.** The three commits already pushed show the
   owner's GitHub handle as author; the commits from here on show the owner's name. The owner
   chose this knowing it.
6. **Nothing new is private.** The owner's term list in `~/.config/hygiene/terms.txt` is
   unchanged by this intake.
7. **Session 0's plan had an adversarial review**, one pass, before the owner saw it; its
   outcome is recorded in the Session 0 commit's message.
8. **Every finding of the itinerary audit is scope this round**, in the four groups of
   `REVIEW-2026-11-17.md` §6: spec compliance, contradictions and small bugs, environment
   assumptions, and phone readability.
9. **The itinerary skill targets what crux-finder targets:** Claude Code, Codex, claude.ai, and
   any agent that loads `SKILL.md` (PDD B, *Scope*). Where the skill needs a capability an agent
   may lack, the skill says what it needs and what it does without it; the wording of its
   minimum environment is asked at the start of Session 3.
10. **The owner is `FairCat-GD`, and the marketplace is named `faircat-skills`.** No account
    rename. Install is `/plugin marketplace add FairCat-GD/claude-skills`, then
    `/plugin install <skill>@faircat-skills`.
11. **Each plugin's README is its user guide.** There is no `docs/USER-GUIDE.md`. The only tag
    this round is crux-finder's 1.0.0.
12. **The workflow is tailored for a repository of skills,** keeping the kit's core whole. The
    deviations are the *In this repository* paragraph of `docs/DEVELOPMENT-WORKFLOW.md`: a
    version only for a skill whose shipped files change, `verify` with the stages `skills`,
    `plugins`, `format`, `lint`, `tests` and `hygiene` and no type-check stage, one command for
    every commit, evals as each skill's harness outside `verify`, and no architecture-review
    sessions.
13. **The hygiene stage is ported in part from another of the owner's projects, under MIT.**
    That project's stage checks private terms and attribution only; the owner, as its author,
    allows the file and its tests here under this repository's MIT licence. The rest of the
    kit's design (secrets, conflict markers, `.env` files, the routine and full scans, the
    stamp) is built here. Every part is falsified here, the ported part included.
14. **A word on the owner's term list is in the public itinerary skill, and the skill changes,
    not the list.** The skill uses one listed city as its running example, on seven lines
    (`REVIEW-2026-11-17.md`, F1). Session 1 replaces those examples with another city's, which
    the owner approves before they are written. History already pushed keeps the old text and
    is not rewritten.
15. **The draft is kept in two parts in `PDD.md`:** the owner's request and the crux-finder
    draft, both verbatim, the draft's headings moved two levels down. The original draft stays
    outside the repository.
16. **The itinerary audit is kept as `REVIEW-2026-11-17.md`,** with the shape of the kit's
    review template: evidence, not scope.
17. **The owner's handle is the published name** in the marketplace's `owner.name` and in every
    `gold.md`'s `approved_by`, as it already is in the licence.
18. **The itinerary skill's versions:** it is `1.0` today in its frontmatter. Session 2's
    restructure changes its shipped files and releases **1.0.1**; Session 3's fixes release
    **1.1.0**. Session 1 also changes the skill (decision 14) but cuts no version, because the
    skill has no manifest until Session 2; 1.0.1's changelog entry carries that change too. The
    skill as first published becomes `1.0.0` in its changelog. Every skill also carries its
    version as `metadata.version` in its `SKILL.md`, so the targets that copy or zip the skill
    folder, which have no `plugin.json`, still show it.
19. **Where the READMEs live:** each plugin has `plugins/<skill>/README.md` (crux-finder's holds
    what PDD B, *Distribution* puts in the root README); the root README lists the skills and
    links each one.
20. **crux-finder 1.0.0 is tagged `crux-finder--v1.0.0`,** the form `claude plugin tag` creates,
    so the tag says which skill it marks. Tagging and pushing the tag are each asked on their
    own.
21. **The rest of PDD B is carried unchanged.** Where a requirement cannot be built as written,
    the session that builds it asks the owner at its start, with a recommended answer; no session
    fills a gap by itself. The known gaps are written into Sessions 5 and 6 as *Ask at the
    start*.
    **Amended 2026-11-22 by the user:** PDD B, *Procedure*, step 6's ranking is not carried
    unchanged. Chosen from the eval cycles' results, a pair of stated claims ranks above one
    holding an inferred premise (Session 7, crux-finder 0.2.0), and a claim a party says outright
    would change their conclusion ranks first among double cruxes (Session 7b, 0.4.0), each
    before depth (§3).
22. **One eval cycle per session.** A cycle is the 20 runs and the owner's review of each. A
    cycle that misses a pass bar ends its session with the skill changed, its version bumped and
    the results recorded; the next cycle is an inserted session (7a, 7b…), added with the owner.
    Only a cycle run on the skill as it stands can meet the bars.
23. **crux-finder 1.0.0 is cut only with every pass bar met** (PDD B, *Pass bars*), the claude.ai
    smoke test passed, and no change to the skill's instructions or references since the last
    full run; its version fields are the one change allowed. A change after that run, one the
    smoke test calls for included, needs a new cycle first.
24. **8 sessions** (`SESSIONS.md`): 8 build sessions, which release travel-itinerary-builder
    1.0.1 and 1.1.0 and crux-finder 0.1.0, 0.2.0 (when the first cycle changes the skill) and
    1.0.0. No architecture reviews (decision 12).
25. **Versions.** Per skill (decision 3), in the plugin's `plugin.json` and `metadata.version`;
    a session that changes no skill cuts none. Shown in `/plugin` and in each plugin's
    changelog. The milestone is crux-finder 1.0.0, tagged.
26. **The draft was not edited on the way in,** except the heading levels of Part B. It names
    no private detail and credits no AI tool.
27. **Nothing private enters the repository.** The owner publishes on purpose the handle
    `FairCat-GD` (the licence, the marketplace, `approved_by`) and their name as commit author
    (decision 5). The hygiene stage of `verify` checks what `ARCHITECTURE.md`'s testing strategy
    lists, and the last read of each diff covers the rest.
    **Amended 2026-11-18 by the user:** the owner's name is also published as each plugin's
    `author` in its `plugin.json`, chosen over the handle at the start of Session 2. The handle
    stays the marketplace's `owner.name` (decision 17).
28. **Licence: MIT,** for the repository and every skill (`license: MIT` in each `SKILL.md`).
29. **The remote is `origin`, the public `FairCat-GD/claude-skills`.** Every push is asked on
    its own, and each request says what the push makes installable: a push after Session 4
    lists crux-finder at a 0.x version. Because each plugin sets a version, people who
    installed a skill receive a change only when its version moves.
30. **Out of v1** (each in `docs/BACKLOG.md`): live moderation, any UI, deciding who is right
    (PDD B, *Scope*); CI; a test of either skill on Codex or another agent; a type-check stage;
    renaming the GitHub account.

## 2. What v1 is, and is not

**v1 is** this repository as a marketplace of skills built under the workflow: `verify` green
with every stage; travel-itinerary-builder 1.1.0 with every audit finding resolved; and
crux-finder 1.0.0, which meets every pass bar of PDD B, *Pass bars* on Claude Code, passes the
claude.ai smoke test, and installs from `faircat-skills`.

**v1 is not:** live moderation, any UI, or a verdict on who is right; CI; a skill tested on
Codex or another agent (their install steps are documented, not run); a repo-wide user guide;
an account rename.

## 3. PDD amendments

| PDD place | PDD says | Now | Where decided |
|---|---|---|---|
| B, *Scope*, *Repo structure* | A single-plugin marketplace repository `crux-finder/` | A plugin in the `faircat-skills` marketplace, in this repository | decisions 1, 10; `ARCHITECTURE.md`, *Layout and boundaries* |
| B, *Repo structure* | `evals/` at the root | `evals/crux-finder/` | decision 1; `ARCHITECTURE.md`, *Layout and boundaries* |
| B, *Repo structure*, `marketplace.json` | `"name": "crux-finder"`, `"owner": { "name": "<owner>" }`, one plugin | `"name": "faircat-skills"`, `"owner": { "name": "FairCat-GD" }`, one entry per skill | decisions 10, 17 |
| B, *Repo structure*; *CI* | `.github/workflows/ci.yml`, running both validators on every push | No CI; `verify`'s `skills` and `plugins` stages run both validators before every commit | decision 4; `ARCHITECTURE.md`, *verify* |
| B, *Distribution*, Claude Code | `/plugin marketplace add <owner>/crux-finder`, `/plugin install crux-finder@crux-finder` | `/plugin marketplace add FairCat-GD/claude-skills`, `/plugin install crux-finder@faircat-skills` | decision 10 |
| B, *Distribution*, README | The root README: install steps per target, one example report, the eval results table | `plugins/crux-finder/README.md`; the root README lists the skills | decision 19 |
| B, *Build order* 8 | CI, README, public release | README, release | decision 4 |
| B, *Procedure*, step 6 | Rank double cruxes first, then by depth; the primary crux is the deepest double crux, else the deepest single crux | Double cruxes first; then a claim a party says outright would change their conclusion (0.4.0); then a pair of stated claims above one holding an inferred premise (0.2.0); then by depth | decision 21, amended; `ARCHITECTURE.md`, *crux-finder* |
| B, *Evals*, *Runner* and *Deterministic checks* | Checks and bars as written | As written, where buildable; each known gap asked at the start of Session 5 or 6 | decision 21 |
| A, item 3 | "Review if any updates … are needed" | The review is `REVIEW-2026-11-17.md`; every finding is scope | decisions 8, 16 |

## 4. Traceability

| Requirement | Session |
|---|---|
| A 1: set up the workflow kit | 0 (the documents), 1 (`verify`, hygiene) |
| A 2: a structure for many skills | 2 |
| A 3: review the itinerary skill | 0 (the review), 1 (F1), 2 (F2), 3 (the rest) |
| A 4: kick off crux-finder | 4–8 |
| B *Scope*: one Agent Skill, conforming, packaged as a plugin | 4; the marketplace, 2 |
| B *Scope*: instructions and references only, no scripts, network or dependencies | 4 (and the `skills` stage holds it) |
| B *Scope*: eval tooling, Python ≥ 3.10, standard library only | 5 |
| B *Scope*: targets Claude Code, claude.ai | 4 (thin slice), 7 (eval and smoke test) |
| B *Scope*: targets Codex, other agents | 8 (install steps); running them: Backlog |
| B *Scope*: out of scope for v1 | Backlog |
| B *Inputs*: the four rows | 4 (the gate); proved in 7 |
| B *Repo structure*: the plugin's files and the three references | 4 |
| B *Repo structure*: `marketplace.json` | 2 (the file), 4 (crux-finder's entry) |
| B *Repo structure*: `plugin.json` name equals the entry name | 2 (the check), 4 |
| B *Repo structure*: references one level deep | 2 (the check), 4 |
| B *Repo structure*: `SKILL.md` under 300 lines; the frontmatter | 2 (the check), 4 |
| B *Procedure*, steps 1–9 | 4; proved in 7 |
| B *Output format*: the template, ≤ 400 words, the claim map on request | 4 |
| B *Output format*: the three rules | 4; checked by 5's `checks.py` |
| B *Guardrails*: the seven | 4; proved in 7 |
| B *Evals*, *Cases*: ten cases, the set table | 6 |
| B *Cases*: `input.md` and `gold.md` frontmatter | 6 |
| B *Cases*: an agent may draft synthetic inputs; only the owner writes or approves gold | 6 |
| B *Cases*: each `gold.md` committed before any result | 6 (the commit), 5 (the check) |
| B *Runner* | 5 (built), 7 (run) |
| B *claude.ai smoke test* | 7 |
| B *Review*: `review.md` per run | 5 (its format), 7 (written) |
| B *Deterministic checks*: the six | 5 |
| B *Pass bars*: the ten | 5 (the summary table), 7 (met) |
| B *Distribution*: public, MIT | 2 (licence field), 8 |
| B *Distribution*: Claude Code, Codex, claude.ai, other agents | 4 (local install), 8 (the README) |
| B *Distribution*: README contents | 8 |
| B *CI* | none: amended (§3) |
| B *Build order* 1–2 | 4 |
| B *Build order* 3 | 5 |
| B *Build order* 4–5 | 6 |
| B *Build order* 6–7 | 7 |
| B *Build order* 8 | 8 |
| Audit F1–F22 | `REVIEW-2026-11-17.md` §6 |

## 5. Definition of done for v1

1. Every block in `SESSIONS.md` has its done-note with its Review section; every inserted
   session and amendment is logged with its reason.
2. travel-itinerary-builder 1.1.0 resolves every finding of `REVIEW-2026-11-17.md`, and
   crux-finder 1.0.0 meets every pass bar of PDD B, *Pass bars*, with the results and reviews in
   `evals/crux-finder/results/` and the summary table in its README.
3. `verify` is green with every stage, with the counts in `ARCHITECTURE.md`'s baseline.
4. Every invariant's enforcement exists and is described in `ARCHITECTURE.md`.
5. `docs/ARCHITECTURE.md`'s Built parts describe the repository as built; each plugin has a
   truthful README and changelog; the root README lists the skills; `CLAUDE.md` points at the
   plugin READMEs.
6. Everything still open is in `docs/BACKLOG.md`, and `docs: close round 1` has emptied
   `docs/spec/`.
