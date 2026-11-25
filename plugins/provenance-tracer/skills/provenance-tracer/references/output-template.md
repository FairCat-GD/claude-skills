# Report formats

The exact shape of everything you send. A forward trace ends in the forward report; a reverse trace
in the reverse report. A question, a refusal and the assumptions block have their own forms below.
Everything is in chat; a report is saved to a file only when the user asks (the end of this file).

## The forward report

````markdown
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
````

## Filling it in

- **The heading.** `## Provenance: "<claim>"`: the claim as restated in forward step 1, one
  sentence, in quotation marks.
- **The label line** is the first line under the heading. It holds `**Roots:**` and one value,
  ` · **Grounding:**` and one value, then each modifier that applies, each after ` · `, in this
  order: Mutated, Misattributed, Origin retracted, Origin corrected, Origin failed replication.
  For example, `**Roots:** Echo · **Grounding:** Primary differs · Mutated · Misattributed`. The
  values and when each applies are in `labels.md`.
- **The earliest instance line.** The earliest node you found that states the claim, linked, with
  its year and where the year came from, as `search-playbook.md` dates it. It always ends with
  `Earlier instances may exist.`
- **The count line,** the third line, also starts with `**Roots:**`, but it gives numbers: how many
  roots, and how many retellings were found, counted as `labels.md` counts them. It is not a
  second label.
- **The chain.** One line per node, indented one step per hop, from the user's version down to a
  root:
  - **A node** is `<source>, <year>, <tier>`, the source linked to the URL exactly as you passed it
    to the fetch tool, and the year with `date unknown` where you found none. The template shows
    the tier on the root line; give it on every node.
  - **A node not opened** is `<citation>, <year>, (not opened), per <opened source>`. A Primary
    you did not open is `Primary (not opened, per <opened source>)`. Link its URL only if you
    tried to fetch it.
  - **Each node but the last** ends with `→ cites`.
  - **More than one branch:** draw each branch from the node where it splits.
  - **A branch that ends short of a root,** at the hop limit, a failed fetch or the end of the
    budget, ends with its reason: `→ stopped: 6 hops`, `→ stopped: not opened`,
    `→ stopped: fetch budget`.
  - **Your version.** Your version: "<claim as typed>", then in brackets the personal chain:
    - where the user met the claim, the role of whoever told them (Hearsay) or what they saw
      themselves (Personal), and the year;
    - `matches <node>` where it links to one (forward step 6);
    - with no personal chain, `(where you met it: not given)`.
- **How it changed.** One row per drift, as `mutation-types.md` writes the table. With none,
  `None found.` under the heading.
- **Status of the root.** One bullet per sourced fact, each linked: a retraction, a correction, a
  failed replication, a major later study. With checks run and nothing found, one bullet naming
  the checks: `- No retraction, correction or failed replication found (journal page, Crossref,
  Retraction Watch, PubPeer).` With no Primary root, `- No primary found, so there was no status
  to check.`
- **Cold trails.** Each node that states the claim and cites nothing, other than the root (the
  rule in `labels.md`), linked, with its year. With none, `None.`
- **Confidence** in the trace, not in the claim: `High`, `Medium` or `Low`, then the reason in one
  sentence.
  - **High:** the root is an opened Primary, every link back to it was opened, and its date comes
    from a byline or an archive.
  - **Medium:** a link or the Primary was not opened (Medium is then the most it can be), or a key
    date rests on *cited by*.
  - **Low:** no node was opened that states the claim before the user's source, or the chain stops
    at its limits short of anything that cites nothing.
- **The footer** is the last line of every forward report, word for word as in the template, and
  the last line of your reply. Nothing follows it: no rule, no summary, no "in short", no note on
  how the search went.
- **Every heading stays,** in the template's order.

## Quotes and titles

- **Quotes.** At most one quote per source, under 15 words, in quotation marks, linked to the
  source. Quote only text the source says word for word. Never reproduce lyrics or poems. The
  user's own claim text, on the heading and the *Your version* line, is exempt.
- **Titles in italics,** never in quotation marks, so quotation marks hold only quotes and the
  user's claim.
- **No verdict.** No sentence of your own calls the claim true, false, a myth or debunked. A
  fact-check that says so is a source: name it and give its finding in its words, within the
  quote rule, or a neutral paraphrase.

## The search note

The first line of your reply, unless you asked a question that carried it, or the assumptions
block below carries it:

````markdown
The claim's text goes into web searches; no name of anyone who told you about it does.
````

In reverse mode: `The source's details go into web searches.`

## When no reply is possible

The assumptions block comes first, above the report's heading, so the template's own lines stay in
order. Its first bullet is the search note; then one bullet per default you took:

````markdown
**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.
- Several claims were given; this report traces the first. Not traced: "<claim 2>", "<claim 3>".

## Provenance: "<claim>"
````

In reverse mode, the bullets name the source chosen among several (`the most cited of <n>
matches`), and the other matches.

## The question

One message, sent before any search, and nothing else in it. Ask only what the message has not
already answered.

**The personal chain** (forward step 2), up to three questions:

````markdown
The claim's text goes into web searches; no name of anyone who told you about it does.

Before I search: where did you come across this, roughly when, and did that source cite anything? If you don't remember, say so and I'll trace it from the web alone.
````

**Several claims.** The choice, with the personal-chain questions for the one picked, so the trace
keeps one question message:

````markdown
This traces one claim per run. Which should I trace?

1. "<claim 1>"
2. "<claim 2>"

For the one you pick: where did you come across it, roughly when, and did that source cite anything? The claim's text goes into web searches.
````

**Several matching sources** (reverse step 1): list each match with its authors, title in italics,
venue and year, and ask which one.

## The refusal

A claim about a private individual: no tool call of any kind, and this reply alone:

````markdown
This skill doesn't trace claims about private people, so I haven't searched for this one. It can trace a claim about a public figure, a publication, a statistic or an idea.
````

Do not repeat the person's name, and do not say anything about them.

## The reverse report

The source and its status first, then what it found and its popular versions, then the beliefs
table only if the user named beliefs. It carries no labels.

````markdown
## Provenance: <source, as the user named it>

**Source:** [<authors>, *<title>*, <venue>, <year>](<url as fetched>)

### Status
- <retraction / correction / replication / major later studies, each linked>

### What it found
<At most 3 sentences, with its scope and hedges.>

### Popular versions
| Version | Where it appears | How it differs |
| --- | --- | --- |
| <the retelling, quoted or paraphrased> | [<source>](<url as fetched>), <year> | <mutation types, and what changed> |

### Your beliefs
| Belief | Support from this source | Gap |
| --- | --- | --- |
| <the belief as the user put it> | supported as stated / partly supported / not supported by this source | <the gap, for partly supported> |
````

- **Status** follows *Status of the root* above, including its line for checks that found
  nothing.
- **What it found** is the source's own result, in the source's terms: its sample, place, period
  and hedges. Paraphrase it, or use the one quote the source allows.
- **Popular versions:** the 2 or 3 most common retellings, each opened and linked, with the drifts
  `mutation-types.md` names.
- **Your beliefs** appears only when the user named beliefs resting on this source. The
  `Support from this source` cell holds one of the three ratings, word for word.
- **The last section is the end of your reply:** *Popular versions*, or *Your beliefs* when it
  appears. Nothing follows it: no rule, no summary, no "in short", no note on how the search went.
  A check that failed or a page that would not open is said in *Status*.

## Saving a report

Only when the user asks, and only in Claude Code:

- **Write the report as sent in chat** to `./provenance-reports/YYYY-MM-DD-<claim-slug>.md`, with
  today's date.
- **The slug** is the first 6 words of the claim, lowercase, hyphenated, punctuation dropped:
  `humans-only-need-four-hours-of`. For a reverse report, it is made from the source as the user
  named it.
- **Hearsay names never appear in a saved report:** write the role (a colleague, a friend, a
  relative) in their place.
- **Say where you saved it,** in one line after the report.
