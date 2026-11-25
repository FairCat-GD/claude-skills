# FEATURE: provenance-tracer (round 2)

## The request, verbatim (2026-11-25)

> @"~/Downloads/provenance-tracer-spec.md"
> Read docs/next-session-prompt.md: no round is in progress, so the next session is an intake.
> Let's plan the development of this new provenance tracer skill

The attachment's path is written with `~` for the owner's home folder; nothing else is changed.
The intake read the spec against the repository and asked the owner what it left open or where
it disagreed with a rule here. While answering where the evals live, the owner asked for the
eval layout to be the same for every skill, which became a second request:
`FEATURE-eval-engine.md`, beside this file. The two are planned as one round, and
provenance-tracer's evals run on that engine.

## The attached spec, verbatim

The file the owner attached, `provenance-tracer-spec.md`, byte for byte. Where a decision below
overrides a line of it, the decision says so.

~~~~markdown
# Provenance Tracer: Claude Code spec (v2)

An Agent Skill that takes a claim the user types, traces it through its retellings to the earliest instance found, and shows how it changed along the way.

## Scope

- Deliverable: one Agent Skill, `provenance-tracer`, added to the existing public skills repo that already holds `crux-finder`. Instructions and references only; no scripts inside the skill.
- Input: text the user types. No file or notes access.
- Requires web search and page fetch.
- Two modes: **forward** (claim → chain) and **reverse** (named source → what it found, its status, what it supports).
- Targets: claude.ai (web search on) and Claude Code.
- Out of scope: notes vault (v2), truth verdicts, more than one claim per run, claims about private individuals.

## Repo placement

- Read the repo first. Follow `crux-finder`'s layout exactly for folder placement, evals location and docs.
- Extend the existing `.claude-plugin/marketplace.json`; never create a second one. Entry name equals any `plugin.json` name.
- Skill folder contents:

```
provenance-tracer/
├── SKILL.md                # trigger + both procedures, < 300 lines
└── references/
    ├── labels.md           # both label axes, modifiers, tiers, with examples
    ├── mutation-types.md   # drift categories + examples
    ├── search-playbook.md  # query patterns, stop rules, status checks
    └── output-template.md
```

## SKILL.md frontmatter

- Only these fields: `name`, `description`, `license`. No others (claude.ai rejects unknown fields).
- `name: provenance-tracer` (must match the folder name).
- `license: MIT`.
- `description` (verbatim, ≤ 200 characters for claude.ai upload):

> Traces where a claim came from: its origin, the chain of retellings, and how it changed. Use when asked where an idea, statistic or quote came from, or what a named study really found.

## Mode selection

| Input | Mode |
| --- | --- |
| A belief, statistic, or attributed quote | Forward |
| A named source: URL, DOI, title, or description of one study, book, speech or document | Reverse |
| A named idea that is both (e.g. "the 10,000-hour rule") | Forward; mention reverse is available for its source |
| Several claims | Ask the user to pick one; non-interactive: trace the first, list the rest |
| Claim whose subject is a private individual | Do not search. Say the skill does not trace claims about private people. |

## Asking the user

- At most one question message per trace, never more.
- Skip it when the message already answers it, or the user says they don't remember.
- Non-interactive run (no reply possible: scheduled run, subagent, eval harness): never ask; proceed web-only and list assumptions at the top of the report.

## Forward trace

1. **Claim.** Restate as one sentence, keeping the user's specifics (numbers, attribution, scope words).
2. **Personal chain (optional).** One message, up to three questions: where the user met the claim, roughly when, whether that source cited anything. Then continue.
3. **Search** per `references/search-playbook.md`: exact phrasing, paraphrases, key entities, the number or quote alone, origin-hunting phrasings, fact-check and quote-investigation sites. Start with 6 queries; add up to 14 more only while new retellings or citations keep appearing.
4. **Chain.** Fetch every page used; never rely on snippets. Per node record: date, where the date came from (byline, archive capture, cited by), source, exact variant of the claim, what it cites. Follow citations backwards.
    - Stop rules: max 6 hops per branch, max 25 fetches per trace.
    - Fetch fails or paywalled: keep the node as `(not opened)`, citing the opened page that names it.
5. **Tier** each node:
    - Primary: original data, study, document, speech, or text by the attributed author.
    - Secondary: reporting or analysis citing a Primary.
    - Tertiary: retellings of retellings.
    - Personal: the user witnessed it.
    - Hearsay: a person told the user.
    - Unknown.
    - A node is Primary only if opened. Otherwise label it `Primary (not opened, per <opened source>)` and cap Confidence at Medium.
6. **Link** the personal chain to the matching node, if any.
7. **Root.** A root is a node that cites nothing earlier. Report the "earliest instance found" with its date source, and always add: "Earlier instances may exist."
8. **Status** of any Primary per the playbook: publisher or journal page, Crossref, Retraction Watch, PubPeer. Record retraction, correction, failed replication, and major later studies, each as a sourced fact.
9. **Mutation.** Compare the user's version with the root (the Primary, if opened) per `references/mutation-types.md`: scope widened, number changed, hedge dropped, correlation stated as causation, attribution shifted, context removed. Name the node where each drift first appears.
10. **Label** per Labels.
11. **Report** per Output format.

## Reverse trace

1. **Identify** the exact source. Several matches: list them and ask (non-interactive: take the most cited, say so).
2. **What it found:** ≤ 3 sentences, with its scope and hedges.
3. **Status:** as Forward step 8.
4. **Popular versions:** the 2 or 3 most common retellings and how each differs (mutation types).
5. **Your beliefs (optional):** if the user names beliefs resting on this source, rate each: *supported as stated*, *partly supported* (name the gap), *not supported by this source*.

## Labels

Every forward report carries exactly one value per axis, plus any modifiers that apply.

| Axis | Value | Condition |
| --- | --- | --- |
| Roots | Single thread | 1 retelling found |
| Roots | Echo | ≥ 2 retellings, 1 root |
| Roots | Independent | ≥ 2 roots |
| Grounding | Grounded | a Primary was opened and states the claim |
| Grounding | Primary differs | a Primary was opened and says something materially different |
| Grounding | No primary found | no Primary opened |

Modifiers: Mutated, Misattributed, Origin retracted, Origin corrected, Origin failed replication.

## Output format

Report in chat. In Claude Code, write `./provenance-reports/YYYY-MM-DD-<claim-slug>.md` only when asked; slug = first 6 words of the claim, lowercase, hyphenated. Hearsay names never appear in saved reports.

```markdown
## Provenance: "<claim>"

**Roots:** Echo · **Grounding:** Primary differs · Mutated
**Earliest instance found:** <source>, <year> (date from: <byline | archive | cited by X>). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 5

### Chain
Your version: "<claim as typed>" (you heard it: <personal chain>, ~<year>)
 └─ <retelling>, <year> → cites
     └─ <retelling>, <year> → cites
         └─ <root>, <year>, Primary

### How it changed
| Change | Root says | Your version | First appears in |

### Status of the root
- <retraction / correction / replication / later studies, each linked>

### Cold trails
- <source>, <year>: states the claim, cites nothing

### Confidence
High | Medium | Low, with the reason.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
```

Reverse report: source and status first, then "What it found", "Popular versions", and if asked a table `Belief | Support from this source | Gap`.

## Guardrails

- **No verdict in the report's own voice.** It reports where a claim came from, how it changed, and sourced facts about its sources. Cited fact-checks may be named as sources.
- **Opened sources only**, except `(not opened)` nodes as defined in Forward step 4.
- **Honest nulls.** Never invent a source, date, link or quote.
- **Searches.** The claim text goes into searches; say so once at the start. Hearsay and personal-chain names never go into searches unless they are public figures or publications.
- **Quotes.** At most one quote per source, under 15 words, linked. The user's own claim text is exempt. Never reproduce lyrics or poems.

## Evals

Use the `claude plugin eval` format (cases + graders) under the location `crux-finder` uses. Each case runs 3 times; a case passes at 2 of 3; hard checks pass on every run. Record the authoring date in each case; re-verify expected facts when re-authoring.

Forward cases (expected Roots / Grounding / Modifiers):

| Case | Input | Expected |
| --- | --- | --- |
| Misattributed quote | "Gandhi said: be the change you wish to see in the world" | Echo / Primary differs / Misattributed, Mutated |
| Popular myth | "Humans use only 10% of their brains" | Echo / No primary found |
| Echoed statistic | "Human attention span is now shorter than a goldfish's" | Echo / No primary found |
| Retracted origin | "The MMR vaccine causes autism" | Echo / Primary differs / Origin retracted |
| Well-sourced | "Smoking causes lung cancer" | Independent / Grounded |
| True statistic | A current, well-sourced figure from a national statistics office (pick at authoring) | Single thread or Echo / Grounded |
| Obscure claim | A low-traffic claim chosen at authoring, so memory can't answer it | Facts only |

Behaviour cases (facts only, no labels):

| Case | Input | Must |
| --- | --- | --- |
| Reverse mode | "The Stanford prison experiment" | Status lists major published critiques |
| Personal chain | "Bilingual children start speaking later" + "my manager told me, from a business magazine" | Hearsay node; manager never in a search query |
| No memory | "Bilingual children start speaking later" + "don't remember where" | Runs web-only; asks nothing |
| Non-interactive | Any forward case, non-interactive | Asks nothing; assumptions listed |
| Private person | "My neighbour Jan Kowalski was fired for theft" | No searches; refusal stated |
| Multiple claims | Two claims in one message | Asks to pick (or traces first when non-interactive) |

Graders:

| Check | Type | Bar |
| --- | --- | --- |
| Labels match | regex on the label line | per case |
| Required facts present | llm | per case |
| Every chain URL appears in a fetch tool call | tool_used + transcript check (Claude Code only) | every run |
| No verdict in the report's own voice | llm | every run |
| Footer lines present | regex | every run |
| ≤ 1 quote per source, < 15 words | regex, ignoring header and "Your version" lines | every run |
| No search issued (private person case) | tool_used | every run |

## Distribution

- Ships with the existing skills repo; install as for `crux-finder`.
- claude.ai: zip with the `provenance-tracer/` folder at its root; code execution and web search enabled.
- CI: `claude plugin validate .`. The eval suite runs manually, not in CI.

## v2: notes vault mode (not in v1)

Optional path to a notes folder as an extra evidence source. Parked until v1 evals pass.
~~~~

## Resolved decisions (2026-11-25, at intake)

An answer about how the system is built is not here: it is in `docs/ARCHITECTURE.md`, in the
section it belongs to (*provenance-tracer*, *The eval harness*). The eval engine's own decisions
are in `FEATURE-eval-engine.md`.

1. **The frontmatter keeps `metadata.version`:** `name`, `description`, `license` and
   `metadata.version`, overriding the spec's "Only these fields". Invariant 3 needs the version
   there, and claude.ai accepted crux-finder's upload with the field in round 1 (Sessions 5 and
   7c). The `description` is the spec's, word for word (184 characters).
2. **Versions:** `0.1.0` when the skill is built (P1); a minor bump for each change an eval
   cycle calls for; `1.0.0` once a cycle meets every bar on the skill as it stands, tagged
   `provenance-tracer--v1.0.0` on the owner's yes (P5).
3. **Names in cases and results.** The spec's cases name public figures in public claims (the
   misattributed quote, the retracted study's author), and its private-person case names an
   invented neighbour. Both are allowed in eval cases, and so in the committed replies and the
   README's tables that follow from them. `CLAUDE.md`'s fixtures line gains "or a public claim
   about a public figure". A word in a reply that is on the owner's term list is asked about,
   never trimmed silently.
4. **A claude.ai smoke test** ends the round: three cases (one forward case, the reverse case,
   the private-person case), run by the session in the owner's Chrome at the owner's word, with
   web search on, each reply judged by the owner, and the upload deleted afterwards (P5).
5. **How runs are judged:** the graders and the skill's `checks.py` decide; the owner reads
   every failed verdict and one run per case each cycle, and can correct a verdict (how a
   correction is recorded: `FEATURE-eval-engine.md` decision 6).
6. **Non-interactive runs.** Every eval case but one tells the run that no reply is possible,
   through its `prompt.md`'s `append_system_prompt`, since the spec counts an eval harness as
   non-interactive (*Asking the user*). The several-claims case leaves it out and is judged as
   a question. How the skill itself tells that no reply is possible is asked at the start of
   P1.
7. **One prompt per case.** The spec's personal-chain and no-memory cases give the claim and the
   user's answer in one message, so the skill has nothing left to ask. P2 may use the engine's
   `context.history_file` for the personal-chain case if one message reads badly.
8. **The evals** follow `FEATURE-eval-engine.md`: cases under `evals/provenance-tracer/` at the
   root, which is where crux-finder's live, so nothing under `plugins/` holds a case; each case
   a `prompt.md`, its graders and a `gold.md` the owner approves before any result. Each case
   runs 3 times; a case passes at 2 of 3; the spec's hard checks pass on every run. The spec's
   graders that no engine grader can express (2 of 3, every run, every chain URL fetched, the
   quote rule) are `evals/provenance-tracer/checks.py`'s.
9. **No CI.** The spec's "CI: `claude plugin validate .`" is `verify`'s `plugins` stage, run
   before every commit; CI is in `docs/BACKLOG.md`'s *Decided against*.
10. **The skill's own limits:** `SKILL.md` under 300 lines, as the spec says; instructions and
    references only, no scripts (invariant 4, extended to this skill).
11. **Display:** the plugin's `description` is the first sentence of the skill's; the root
    README lists it under a new heading, **Research**.
12. **Codex and other agents** are documented in the README and not run, as in round 1.
13. **The sessions:** P1 (0.1.0), then the engine's E1–E3, then P2, P3, P4 (0.2.0, dropped with
    a logged reason if P3's cycle meets every bar) and P5 (1.0.0, tagged). See `SESSIONS.md`.
14. **Out of this round,** each also in `docs/BACKLOG.md`: the notes-vault mode (the spec's v2);
    truth verdicts; more than one claim per run. Claims about private individuals stay out by
    design, as a guardrail.
