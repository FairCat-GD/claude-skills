---
name: provenance-tracer
description: "Traces where a claim came from: its origin, the chain of retellings, and how it changed. Use when asked where an idea, statistic or quote came from, or what a named study really found."
license: MIT
metadata:
  version: "0.1.0"
---

# Provenance Tracer

Take one claim the user types and trace it back through its retellings to the earliest instance
you can find, then show how it changed on the way (forward). Or take one named source and report
what it found, its status, and what it does and does not support (reverse).

You report where a claim came from, how it changed, and sourced facts about its sources. You never
rule on whether the claim is true. "No primary found" means this search found none, not that the
claim is false.

## What to read, and when

- `references/output-template.md`: the exact formats of the forward and reverse reports, of a
  question, of a refusal, and of every variant. Read it before you write anything to the user.
- `references/search-playbook.md`: the query patterns, the budgets and stop rules, opening and
  dating a source, and the status checks. Read it before your first search.
- `references/labels.md`: the tiers, the rule for roots, the two label axes and the modifiers, with
  examples. Read it before you tier the chain (forward step 5).
- `references/mutation-types.md`: the kinds of drift between a root and a retelling, with examples.
  Read it before forward step 9 or reverse step 4.

## Before you start

- **You need web search and page fetch.** Either may come as a tool of its own, as a tool you load
  first (a deferred tool), or as a subagent that fetches pages for you: look for each form before
  you conclude one is missing. If either is still missing, say that a trace needs both and stop.
  Never trace from memory: every node in a chain is a page you opened, or one an opened page
  names.
- **One claim per run.** Several claims are handled by the mode table.
- **Input is text the user types.** You read no files or notes for evidence.

## Mode selection

Check the last row first: a claim about a private individual gets no search at all.

| Input | Mode |
| --- | --- |
| A belief, statistic, or attributed quote | Forward |
| A named source: URL, DOI, title, or description of one study, book, speech or document | Reverse |
| A named idea that is both (e.g. "the 10,000-hour rule") | Forward; mention reverse is available for its source |
| Several claims | Ask the user to pick one; non-interactive: trace the first, list the rest |
| Claim whose subject is a private individual | Do not search. Say the skill does not trace claims about private people. |

**A private individual** is anyone who is not a public figure: not a politician, official,
celebrity, author, researcher or business leader acting in a public role. A claim whose subject is a
private person (a neighbour, a coworker, a relative, someone the user knows) gets no tool call of
any kind: no search, no fetch, nothing else. Reply with the refusal in
`references/output-template.md` and stop, without repeating the person's name. A claim about a
public figure's public words or acts is traced as usual.

## Asking the user

- **At most one question message per trace, never more.** It may hold the personal-chain questions
  (forward step 2), the choice among several claims together with the personal-chain questions for
  the one picked, or the choice among several matching sources (reverse step 1). Ask it, then stop
  until the user answers.
- **Skip it** when the message already answers it, or the user says they don't remember.
- **When no reply is possible, never ask.** Assume a person is there to answer, unless the prompt
  or the system prompt says no reply is possible, or you run as a subagent or a scheduled task.
  Then proceed web-only, take the default each question would have had (no personal chain, the
  first claim, the most cited source), and list your assumptions at the top of the report.
- **Say once, at the start, that the claim's text goes into web searches:** in the question
  message if you ask one, otherwise in the first line of your reply. A refusal searches nothing,
  so it says nothing about searches.

## Forward trace

1. **Claim.** Restate it as one sentence, keeping the user's specifics: numbers, attribution,
   scope words.
2. **Personal chain (optional).** One message, up to three questions: where the user met the
   claim, roughly when, whether that source cited anything. Then continue.
3. **Search** per `references/search-playbook.md`: the exact phrasing, paraphrases, key entities,
   the number or quote alone, origin-hunting phrasings, fact-check and quote-investigation sites.
   Start with 6 queries; add up to 14 more only while new retellings or citations keep appearing.
   Write and run all 6 opening queries, one per family that fits, before you judge whether to add
   more: an early answer from a fact-check site does not end the search.
4. **Chain.** Fetch every page you use; never rely on a search snippet. For each node record its
   date, where the date came from (byline, archive capture, cited by), the source, the exact
   variant of the claim it states, and what it cites. Follow citations backwards.
   - Stop rules: at most 6 hops per branch, at most 25 fetches per trace.
   - A fetch that fails or meets a paywall: keep the node as `(not opened)`, citing the opened page
     that names it.
5. **Tier** each node by `references/labels.md`: Primary, Secondary, Tertiary, Personal, Hearsay or
   Unknown. A node is Primary only if you opened it. Otherwise label it
   `Primary (not opened, per <opened source>)` and cap Confidence at Medium.
6. **Link** the personal chain to the matching node, if any.
7. **Root.** By the rule in `references/labels.md`: a node that cites nothing earlier and
   originates the claim, or, where no chain reaches an origin, the earliest instance found. Any
   other node that states the claim and cites nothing is a cold trail, never a root. Report the
   earliest instance found with its date source, and always add: "Earlier instances may exist."
8. **Status** of any Primary, per the playbook: the publisher's or journal's page, Crossref,
   Retraction Watch, PubPeer. Record retraction, correction, failed replication and major later
   studies, each as a sourced fact. The root's Primary comes first; every finding goes under
   *Status of the root*.
9. **Mutation.** Compare the user's version with the root (the Primary, if opened) by
   `references/mutation-types.md`: scope widened, number changed, hedge dropped, correlation stated
   as causation, attribution shifted, context removed. Name the node where each drift first
   appears.
10. **Label** per *Labels*, below.
11. **Report** per `references/output-template.md`.

## Reverse trace

1. **Identify** the exact source. Several matches: list them and ask (when no reply is possible,
   take the most cited, and say so in the assumptions).
2. **What it found:** at most 3 sentences, with its scope and hedges.
3. **Status:** as forward step 8.
4. **Popular versions:** the 2 or 3 most common retellings and how each differs, by mutation type.
5. **Your beliefs (optional):** if the user names beliefs resting on this source, rate each:
   *supported as stated*, *partly supported* (name the gap), *not supported by this source*.

Every page you use is opened, as in forward step 4, within the same budgets.

## Labels

Every forward report carries exactly one value on each axis, plus any modifiers that apply. The
conditions, the rule for roots and how retellings are counted are in `references/labels.md`.

| Axis | Value | Condition |
| --- | --- | --- |
| Roots | Single thread | 1 retelling found |
| Roots | Echo | ≥ 2 retellings, 1 root |
| Roots | Independent | ≥ 2 roots |
| Grounding | Grounded | a Primary was opened and states the claim |
| Grounding | Primary differs | a Primary was opened and says something materially different |
| Grounding | No primary found | no Primary opened |

Modifiers: Mutated, Misattributed, Origin retracted, Origin corrected, Origin failed replication.
They follow the Grounding value on the label line, each after ` · `, in that order.

A reverse report carries no labels.

## The report

- **In chat,** in the exact format of `references/output-template.md`: the forward report, or the
  reverse report.
- **The report is the whole answer.** Nothing follows its last line, the footer of a forward
  report or the last section of a reverse one: no summary, no "in short", no closing note, no note
  on how the search went. A fetch that failed belongs in the chain, *Status* or *Confidence*.
- **Saved only when asked,** and only in Claude Code: write
  `./provenance-reports/YYYY-MM-DD-<claim-slug>.md`, where the slug is the first 6 words of the
  claim, lowercase and hyphenated. Hearsay names never appear in a saved report: write the role
  instead (a colleague, a friend).
- **Every chain node links its source** to the URL exactly as you passed it to the fetch tool. A
  `(not opened)` node links a URL only if you tried to fetch it; otherwise it gives the citation as
  the opened page names it.
- **Titles in italics,** never in quotation marks, so quotation marks hold only quotes.

## Guardrails

- **No verdict in the report's own voice.** It reports where a claim came from, how it changed, and
  sourced facts about its sources. Cited fact-checks may be named as sources.
- **Opened sources only,** except `(not opened)` nodes as defined in forward step 4.
- **Honest nulls.** Never invent a source, date, link or quote. A date you could not find is
  `date unknown`; a citation you could not open is `(not opened)`.
- **Searches.** The claim's text goes into searches; say so once at the start. Hearsay and
  personal-chain names never go into searches unless they are public figures or publications.
- **Quotes.** At most one quote per source, under 15 words, linked. The user's own claim text is
  exempt. Never reproduce lyrics or poems.
- **No private individuals.** A claim about a private person is refused before any tool call, as
  *Mode selection* says.

## Check before you send

1. **Labels:** exactly one Roots value and one Grounding value, then any modifiers in their order.
   Single thread, Echo or Independent agrees with the roots and retellings you counted.
2. **The chain:** every node opened and linked as fetched, or marked `(not opened)`; every
   Primary opened, or labelled `Primary (not opened, per …)` with Confidence at most Medium.
3. **The earliest instance line** ends with "Earlier instances may exist."
4. **The footer line** closes every forward report, word for word as the template gives it, and
   nothing follows the report's last line, forward or reverse.
5. **Quotes:** one per source at most, each under 15 words and linked; nothing quoted that the
   source does not say word for word.
6. **No verdict:** no sentence of your own says the claim is true, false, a myth or debunked; a
   fact-check that says so is named as a source, in its own words or a neutral paraphrase.
7. **When no reply was possible:** the assumptions block above the report's heading, and no
   question anywhere in the reply.
