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
- **Running either skill on Codex or another agent.** Their install steps are documented; no
  session runs them. Left out at the round 1 intake.

## Not yet checked by hand

Checks that need a person at the machine. Each has an automated check covering most of it;
these are the parts only a person can see.

- **Installing from GitHub** (travel-itinerary-builder, 1.1.0 since Session 3's push;
  crux-finder 1.0.0 since Session 8's push): run
  `/plugin marketplace add FairCat-GD/claude-skills`, then
  `/plugin install travel-itinerary-builder@faircat-skills` and
  `/plugin install crux-finder@faircat-skills` in Claude Code, and open each plugin's `homepage`
  link. The `plugins` stage validates the manifests, and Sessions 2 and 4 installed the same
  marketplace from this folder.

- **travel-itinerary-builder 1.1.0 on Codex, claude.ai and other agents.** Session 3's run
  was in Claude Code only. On claude.ai, check that the upload accepts the `compatibility`
  field and that the PDF is offered for download. The `skills` stage validates the folder
  against the specification.
- **The itinerary skill's fallbacks:** the interview asked in chat with no question tool, and
  the plan delivered in chat where WeasyPrint can't run. Session 3 measured the PDF build's
  own fallbacks (offline fonts, PyMuPDF page images); these two paths need an agent without the
  capability.

## Directions

- **crux-finder: what would move it, and common ground kept to what each party said.** The
  fourth eval cycle met every bar, and the owner's reviews still noted, below any bar: *what
  would move it* leaving out a record the gold names, or giving a calculation where gold names a
  measurement (the orchard and kiln cases), or no near dated check (the solar case); and
  common-ground lines widening what a party said (five cases). No bar measures either; a later
  round could add one, with cases, before changing the skill for it.

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
