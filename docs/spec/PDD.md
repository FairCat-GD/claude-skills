# The product design draft, round 1

Frozen as received on 2026-11-17. Two parts, both verbatim: the owner's request that opened the
round, and the draft of the first new skill. Nothing private needed replacing. Where this file
and `SPEC.md` differ, `SPEC.md` wins, and its §3 lists every place they do.

## Part A: the owner's request

> we will be working on various skills here please connect this folder with my skills repo
> first and then I'll give you the instructions

> here is what I want to do: I want to work on and store here different skills we create. so
> far it has only one.
>
> 1. Please set up my workflow from workflow kit in this repo
> 2. adjust repo structure to support many different skills
> 3. Review if any updates, improvements or changes are needed to the itinerary builder skill
> 4. kick off the development of the new crux-finder skill (spec attached)
>
>
> Please do not invent anything based on your assumptions, better ask me if you have questions

## Part B: the crux-finder draft (v1.2)

Below is the attached file, unchanged except that every heading outside a code block is two
levels deeper, so the draft sits under this part. Items are cited as "PDD B, <section>".

### Crux Finder: Claude Code spec (v1.2)

An Agent Skill that takes two positions and returns the smallest disagreement the rest of the argument hinges on.

#### Scope

- Deliverable: one Agent Skill, `crux-finder`, conforming to the Agent Skills spec (agentskills.io/specification), packaged as a Claude Code plugin in a single-plugin marketplace repo.
- Skill: instructions and references only. No scripts, no network access, no dependencies.
- Eval tooling (`evals/`): Python ≥ 3.10, standard library only.
- Targets: Claude Code, Codex, claude.ai, any agent that loads `SKILL.md`.
- Out of scope for v1: live moderation, any UI, deciding who is right.

#### Inputs

| Input | Handling |
| --- | --- |
| Two positions, each in its author's own words, labelled A and B | Run |
| Transcript with two identifiable speakers (chat log, thread, email chain) | Run; attribute claims by speaker |
| One party's position + that party's paraphrase of the other | Gate (see Guardrails) |
| Anything else | Ask for two positions labelled A and B |

#### Repo structure

```
crux-finder/
├── .claude-plugin/
│   └── marketplace.json
├── plugins/
│   └── crux-finder/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       └── skills/
│           └── crux-finder/
│               ├── SKILL.md                # trigger + core procedure, < 300 lines
│               └── references/
│                   ├── procedure.md        # full step definitions, loaded on demand
│                   ├── crux-types.md       # classification rules + 2 examples per type
│                   └── output-template.md  # exact report format
├── evals/
│   ├── cases/<id>/                         # input.md, gold.md
│   ├── results/<id>/                       # run-1.md, run-2.md, claude-ai.md, review.md
│   ├── run.py
│   └── checks.py
├── .github/workflows/ci.yml
├── LICENSE                                 # MIT
└── README.md
```

`marketplace.json`:

```json
{
  "name": "crux-finder",
  "owner": { "name": "<owner>" },
  "plugins": [
    {
      "name": "crux-finder",
      "source": "./plugins/crux-finder",
      "description": "Find the crux of a disagreement"
    }
  ]
}
```

- `plugin.json` `name` = `crux-finder` (must equal the marketplace entry name).
- References one level deep from `SKILL.md`.

`SKILL.md` frontmatter:

```yaml
name: crux-finder
description: "Find the crux of a disagreement: the smallest claim two positions hinge on. Use when the user shares two positions, a debate or a transcript and asks where people really disagree, why an argument goes in circles, or what would change someone's mind."
license: MIT
```

#### Procedure

Steps run in order. Steps 3 to 6 are internal; only their results reach the report.

1. **Gate.** Classify input per the Inputs table. Stop or ask per Guardrails.
2. **Steelman.** Restate each position in its strongest form, 2 to 4 sentences, using only content present in the input. Any premise not stated but required is marked `[inferred]`.
3. **Claim map.** Decompose each position into atomic claims `A1..An`, `B1..Bn`. Tag each: `stated` or `inferred`; role `conclusion` or `premise`; dependencies (`A3 depends on A1`).
4. **Common ground.** List claims both parties accept, explicitly or by clear implication.
5. **Conflict set.** Pair claims that cannot both be true or both be accepted.
6. **Crux test.** For each conflicting claim X ask: if A adopted B's view of X, would A's conclusion change? Then the reverse.
    - Yes for both: double crux.
    - Yes for one: crux for that party.
    - No for both: drop from the report.
    - Rank: double cruxes first, then by depth (a claim other conflicts depend on outranks them). The primary crux is the deepest double crux, else the deepest single crux.
7. **Classify** each reported crux by `references/crux-types.md`:
    - Empirical: a checkable present or past fact.
    - Predictive: a claim about future outcomes.
    - Definitional: one word, two meanings.
    - Value: same facts, different weighting of goods.
    - Framing: the parties answer different questions.
8. **Resolution path** per crux:
    - Empirical: the specific evidence that would settle it (data source, study type, measurement).
    - Predictive: an observable forecast with a date both could check.
    - Definitional: two labelled terms replacing the shared word.
    - Value: name the trade-off. Offer no resolution.
    - Framing: state both questions separately.
9. **No-conflict exit.** If step 6 yields nothing, report a Framing crux or state that the positions do not conflict. Never manufacture a crux.

#### Output format

Store as `references/output-template.md`. Default report ≤ 400 words. Full claim map from step 3 appended only when the user asks for it.

```markdown
## Crux report

**A, strongest form:** …
**B, strongest form:** …

### Common ground
- …

### The crux
**Double crux · Empirical**
> One sentence, neutral wording both parties would accept as a fair statement of the dispute.

- A holds: …
- B holds: …
- If A accepted B's view here: … (and the reverse)
- What would move it: …

### Secondary cruxes
Max 2. Same fields, one line each.

### Not actually in dispute
- Apparent disagreements that dissolve under definitions or framing.

### Confidence
High | Medium | Low, with the reason.
```

Rules:

- The crux sentence uses no loaded term from either side.
- Text shown as a quote must appear verbatim in the input.
- Steelman lengths for A and B within ±25% of each other by word count.

#### Guardrails

- **One-sided input.** Ask once for the other party's own words or a transcript. If the user proceeds anyway: run, label B as "reconstructed by A", cap Confidence at Low, and suggest sharing the report with B to confirm their side.
- **No verdict.** The report never states who is right. For Empirical cruxes it names the evidence that would settle the question, not the answer.
- **Claims, not people.** No statements about motives, intelligence, psychology or good faith of either party. Applies equally to personal and relationship disputes.
- **Symmetry.** Equal care and length for both sides (see Output rules).
- **No invented quotes.** Attributed text is verbatim from the input or paraphrased without quotation marks.
- **No manufactured cruxes.** Positions that do not conflict are reported as such.
- **Agent as party.** If one of the two parties is the agent itself in the current conversation, state this as the report's first line and recommend re-running in a fresh session with the transcript pasted as input.

#### Evals

##### Cases

10 cases in `evals/cases/<id>/`, each with `input.md` and `gold.md`.

| Set | Type | Cases |
| --- | --- | --- |
| Synthetic | Empirical | 2 |
| Synthetic | Predictive | 1 |
| Synthetic | Definitional | 1 |
| Synthetic | Value | 1 |
| Synthetic | Framing / talking past | 1 |
| Synthetic | One-sided input | 1 |
| Synthetic | No conflict | 1 |
| Real | Public-domain debate transcript excerpt (e.g. 1858 Lincoln-Douglas debates, US congressional hearings) | 1 |
| Real | Real dispute written up by the maintainer, fully anonymized | 1 |

- Real-set `input.md` frontmatter: `source:` (URL or citation), `license: public-domain` or `license: maintainer-authored`.
- `gold.md` frontmatter: `crux` (one sentence), `type`, `crux_for` (A | B | both | none), `approved_by` (maintainer handle).
- An agent may draft synthetic `input.md`. Only the maintainer writes or approves `gold.md`.
- Each `gold.md` is committed before any file under `results/<id>/` exists.

##### Runner

- `run.py --runs 2`: one fresh session per case per run via `claude -p` with `--plugin-dir plugins/crux-finder`; prompt = contents of `input.md`.
- Output saved to `results/<id>/run-N.md`.
- `run.py` never reads `gold.md`.

##### claude.ai smoke test

- Upload zip of `plugins/crux-finder/skills/crux-finder/` as a custom skill in claude.ai.
- Run cases: one Empirical, the one-sided case, the no-conflict case; one run each, fresh chat per case, prompt = contents of `input.md`.
- Save outputs to `results/<id>/claude-ai.md`; same review fields and deterministic checks as runner output.
- Pass: all 3 match gold, all deterministic checks pass.

##### Review

Maintainer reads every run and records in `results/<id>/review.md`, per run: `crux_match` (yes | no), `type_match` (yes | no), `people_statement` (yes | no), one-line note.

##### Deterministic checks (`checks.py`)

- Quotes: every quoted span in `run-N.md` found verbatim in `input.md`.
- Symmetry: steelman word counts A vs B within ±25%.
- Length: report ≤ 400 words.
- Gold order: first commit of each `gold.md` predates first commit under `results/<id>/` (via `git log`).
- `approved_by` present in every `gold.md`.
- Summary table of `review.md` results against pass bars.

##### Pass bars

| Check | Pass bar |
| --- | --- |
| Crux matches gold | ≥ 16 / 20 runs |
| Type matches gold | ≥ 18 / 20 runs |
| Stability: same primary crux in both runs | ≥ 8 / 10 cases |
| Quotes verbatim | all runs |
| Steelman symmetry | all runs |
| Length ≤ 400 words | all runs |
| `people_statement` no | all runs |
| One-sided gate fires (asks for B's words or labels B reconstructed) | 2 / 2 runs |
| No-conflict case reports no conflict or a Framing crux | 2 / 2 runs |
| Gold order + `approved_by` | all cases |

#### Distribution

- Public GitHub repo, MIT.
- Claude Code (desktop app session): `/plugin marketplace add <owner>/crux-finder`, then `/plugin install crux-finder@crux-finder`. Skill invoked as `/crux-finder:crux-finder` or by description match.
- Codex: copy `plugins/crux-finder/skills/crux-finder/` to `~/.agents/skills/` (user) or `.agents/skills/` (repo). Invoked as `$crux-finder` or by description match.
- claude.ai: zip of `plugins/crux-finder/skills/crux-finder/` uploaded as a custom skill.
- Other agents: copy the skill dir into the agent's skills directory.
- README: install steps per target, one example report, eval results table.

#### CI

GitHub Action on every push:

- `claude plugin validate .` (install the Claude Code CLI in the job; if `validate` requires authentication, run it in a pre-push hook instead).
- `skills-ref validate plugins/crux-finder/skills/crux-finder` (install: `uvx --from git+https://github.com/agentskills/agentskills#subdirectory=skills-ref`).

#### Build order

1. Skill files + plugin/marketplace manifests; `claude plugin validate .` and `skills-ref validate` pass.
2. Local install via `/plugin marketplace add ./` in a desktop app session; skill loads and runs on one hand-written input.
3. `run.py`, `checks.py`.
4. Synthetic `input.md` drafts → maintainer writes/approves all `gold.md` → commit.
5. Real-set cases → maintainer writes `gold.md` → commit.
6. Eval run, maintainer review, iterate skill until pass bars met.
7. claude.ai smoke test.
8. CI, README, public release.
