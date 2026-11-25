# Backlog

Work that has been named but belongs to no session. Each item goes through an intake before it
runs (a `docs/spec/FEATURE-*.md` with the request verbatim and the decisions resolved, then a
block in `docs/spec/SESSIONS.md`; see `docs/DEVELOPMENT-WORKFLOW.md`). When an item is picked
up, it moves out of this file.

## Deferred

- **crux-finder: live moderation.** Running during a live dispute rather than on a finished
  one. Left out at the round 1 intake (PDD B, *Scope*).
- **crux-finder: any UI.** Left out at the round 1 intake (PDD B, *Scope*).
- **crux-finder: deciding who is right.** Out of scope by design, and also a guardrail; left out
  at the round 1 intake (PDD B, *Scope*).
- **crux-finder: a second real eval case.** PDD B's real set has two cases: a public-domain
  debate excerpt and a dispute the maintainer writes up. Session 6 committed the excerpt; the
  owner had no dispute to write up, so a fictional transcript took its place. A real one, from
  the owner or another public-domain source, joins as a new case with its gold committed
  before any of its results.
- **crux-finder: the Framing-or-Value line between two golds.** `framing-piano-lessons` (gold
  Framing) and `value-theatre-season` (gold Value) have the same shape, and no general tie-break
  found in Session 7 separates them. The owner decides whether either gold should change; a gold
  changed after its results exist fails the gold order, so the case would start over under a new
  id.
- **crux-finder: a case with the agent as a party.** The guardrail's note on the report's first
  line, and 0.3.0's rule that such a report has no secondary cruxes, are measured by no case:
  every eval input comes in a fresh session. A case would need the dispute to arise in the same
  conversation, which `run.py`'s single prompt cannot give (Session 7a's review).
- **Running a skill on Codex or another agent.** Each skill's install steps are documented; no
  session runs them. Left out at the round 1 intake.
- **provenance-tracer: a notes-vault mode.** An optional path to a notes folder as an extra
  source of evidence; the owner's spec parks it until the first version's evals pass. Left out
  at the round 2 intake.
- **provenance-tracer: truth verdicts.** The skill reports where a claim came from, never
  whether it is true; out of scope in the spec, and a guardrail. Left out at the round 2 intake.
- **provenance-tracer: more than one claim per run.** The skill asks the user to pick one, or
  traces the first when no reply is possible. Left out at the round 2 intake.

## Not yet checked by hand

Checks that need a person at the machine. Each has an automated check covering most of it;
these are the parts only a person can see.

- **Installing from GitHub** (travel-itinerary-builder, 1.1.0 since Session 3's push;
  crux-finder 1.0.0 since Session 8's push; provenance-tracer 0.1.0 since Session P1's push): run
  `/plugin marketplace add FairCat-GD/claude-skills`, then
  `/plugin install travel-itinerary-builder@faircat-skills`,
  `/plugin install crux-finder@faircat-skills` and
  `/plugin install provenance-tracer@faircat-skills` in Claude Code, and open each plugin's
  `homepage` link. The `plugins` stage validates the manifests, and Sessions 2, 4 and P1
  installed the same marketplace from this folder.

- **travel-itinerary-builder 1.1.0 on Codex, claude.ai and other agents.** Session 3's run
  was in Claude Code only. On claude.ai, check that the upload accepts the `compatibility`
  field and that the PDF is offered for download. The `skills` stage validates the folder
  against the specification.
- **provenance-tracer on claude.ai: page fetch.** The skill stops without page fetch, and its
  README asks only for web search on claude.ai. Whether a claude.ai chat with web search on can
  also open pages is checked in P5's smoke test. Named by Session P1's review.
- **The engine's result for an API error.** Session E1 could not provoke one. The shared runner
  writes nothing for a run with no grader results, as the engine's docs describe an API error,
  and its tests use that shape. The first rate limit or overload in a real cycle shows it.
- **The itinerary skill's fallbacks:** the interview asked in chat with no question tool, and
  the plan delivered in chat where WeasyPrint can't run. Session 3 measured the PDF build's
  own fallbacks (offline fonts, PyMuPDF page images); these two paths need an agent without the
  capability.

## Directions

- **crux-finder: what would move it, and common ground kept to what each party said.** The
  fourth eval cycle met every bar, and the owner's reviews still noted, below any bar: *what
  would move it* leaving out a record the gold names, or giving a calculation where gold names a
  measurement (the orchard and kiln cases), or no near dated check (the solar case); and
  common-ground lines widening what a party said (five cases). Session E3's cycle on the shared
  engine noted the same. No bar measures either; a later round could add one, with cases, before
  changing the skill for it.
- **crux-finder: the people grader's false fails, and the judge's reasons.** In Session E3 the
  judge failed `no-statement-about-people` on three reports (kiln, piano and solar, run 1) in
  which the fresh reader and the owner found no statement about either party; the owner
  overruled all three. The engine keeps only the votes (`judge votes: FAIL FAIL FAIL`), so
  nothing shows what the judge objected to. If later cycles repeat it, the grader's wording or
  the judge could change; a grader changed means its case starts over.

## Decided against

- CI: `verify` is the gate, run before every commit (round 1 intake).
- A type-check stage: the scripts are small; ruff and the tests cover them (round 1 intake).
- crux-finder in a repository of its own: every skill lives here (round 1 intake).
- One plugin holding every skill: each skill installs on its own (round 1 intake).
- Renaming the GitHub account: install commands embed the owner, and `FairCat-GD` stays
  (round 1 intake).
- A repo-wide `docs/USER-GUIDE.md`: each plugin's README is its user guide (round 1 intake).
- A separate docs-only command: `verify` takes seconds (round 1 intake).
- Architecture-review sessions: the round's last session reads `ARCHITECTURE.md` cold, which
  covers a codebase this small (round 1 intake).
- Taking the itinerary skill's example city off the owner's term list, or a per-repository
  hygiene exception for it: the skill's examples change instead (round 1 intake).
- An example report in crux-finder's README: the owner left it out, amending decision 19
  (round 1, Session 8).
- Moving the eval tooling's floor off Python 3.10: it is PDD B's floor, and running on it is
  what proves it. Raised by the plan review; the owner may revisit it.
