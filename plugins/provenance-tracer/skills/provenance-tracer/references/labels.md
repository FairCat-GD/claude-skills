# Tiers, roots and labels

How to tier each node of a chain, which nodes are roots, and the label line every forward report
carries. Tiers and labels describe where a claim came from and how far the trace got, never
whether the claim is true.

Every example below is invented, to show the shape: the places, bodies, studies and numbers do
not exist. Never cite them.

## Tiers

Tier every node by its position in the chain, not by how reliable it seems.

| Tier | A node that is |
| --- | --- |
| Primary | original data, a study, a document, a speech, or text by the attributed author |
| Secondary | reporting or analysis that cites a Primary |
| Tertiary | a retelling of a retelling: it cites a Secondary or a Tertiary, or nothing |
| Personal | something the user witnessed |
| Hearsay | something a person told the user |
| Unknown | none of these can be told from what you opened |

- **A node is Primary only if you opened it.** A Primary you know only because an opened page
  names it is `Primary (not opened, per <opened source>)`, and the report's Confidence is at most
  Medium.
- **Personal and Hearsay nodes come from the user,** in the personal chain (forward step 2). They
  are shown on the *Your version* line, never searched by name unless they are public figures or
  publications, and never counted as retellings.
- **A page that only summarises search results,** such as an index or an aggregator with no text
  of its own, is not a node; open what it points to instead.

## Roots

A **root** is where a chain begins. Find the roots this way:

1. **Follow every chain back** until a node cites nothing earlier. Naming a person, work or body as
   the claim's source counts as citing it, even with no link or reference: a page that says "as
   the survey found" cites the survey.
2. **A node that cites nothing earlier and originates the claim is a root:** a Primary that is its
   own data, study, document, speech or text, or the work the claim grew from.
3. **Where no chain reaches such an origin, the earliest instance found is the one root.**
4. **Every other node that states the claim and cites nothing is a cold trail:** listed under
   *Cold trails*, counted as a retelling, never as a root. Two blog posts that each repeat a claim
   with no source are cold trails of one root, not two roots.
5. **Two roots are independent origins,** each reached by its own chain and neither citing the
   other: two studies with their own data, two documents written apart. A later study that
   repeats an earlier one, and cites it, is a node in the earlier one's chain.

## Counting retellings

**Retellings found** counts the nodes you found by search: the root, every node on a chain, and
every cold trail. The user's own version, and the Personal and Hearsay nodes of the personal
chain, are not counted. A `(not opened)` node is counted, since an opened page names it.

## The two axes

Every forward report carries exactly one value on each axis.

**Roots,** decided in this order:

| Value | When |
| --- | --- |
| Independent | 2 or more roots |
| Echo | 1 root and 2 or more retellings found |
| Single thread | 1 retelling found: the chain is the user's version and one source |

**Grounding:**

| Value | When |
| --- | --- |
| Grounded | a Primary was opened and states the claim: as the user put it, or with no drift that changes what it asserts |
| Primary differs | a Primary was opened and says something materially different: a different number, scope, strength, cause or author |
| No primary found | no Primary was opened (a Primary known only as `not opened` counts as none) |

With more than one opened Primary: Grounded if any of them states the claim, and the report's *How
it changed* notes any that differs; Primary differs only if every opened Primary differs.

## Modifiers

Add each that applies, after the Grounding value, each after ` · `, in this order:

| Modifier | When |
| --- | --- |
| Mutated | at least one drift from `mutation-types.md` between the root and the user's version |
| Misattributed | the user's version credits words or a finding to a person or source that the root shows did not say, write or find them, a paraphrase given as their exact words included. It is always also an attribution-shifted drift, so Mutated applies too |
| Origin retracted | a root that is a Primary was retracted, by a notice you opened |
| Origin corrected | a root that is a Primary has a published correction or erratum, by a notice you opened |
| Origin failed replication | a later study set out to repeat a root's finding and did not, by the study or a report of it you opened |

The three *Origin* modifiers need an opened notice or study: a page that only says a study was
"discredited" is a lead to follow, not a status. With no Primary root, none of them applies.

## The label line

````markdown
**Roots:** Echo · **Grounding:** Primary differs · Mutated · Misattributed
````

The count line below it, `**Roots:** 1 · **Retellings found:** 5`, gives the number of roots and of
retellings found. It is a different line, though it starts with the same word.

## Examples

Invented, one for each value.

- **Single thread · Grounded.** The user says the Harlow Valley Transit Board counted about 41,000
  weekday riders last year. The board's own annual table, opened, gives 41,200. One source, a
  Primary that states the claim.
- **Echo · No primary found.** The user says Lake Mirren is the clearest lake in Europe. A 2021
  travel blog cites a 2016 magazine feature, which cites nothing; a 2012 regional brochure states
  it too, cites nothing, and is the earliest instance found. No chain reaches a measurement. One
  root (the brochure), the magazine a cold trail, three retellings.
- **Independent · Grounded.** The user says moss grows faster on the north side of trees in the
  Corran Hills. Two field surveys, by two universities in different years, each with its own plots
  and neither citing the other, were opened and each reports it. Two roots.
- **Echo · Primary differs · Mutated.** The user says a study found that orchard workers who drink
  cider sleep two hours longer. The study, opened, reports a 20-minute difference in a sample of 30
  workers, and calls it preliminary. Retellings dropped the hedge and changed the number.
- **Echo · Primary differs · Mutated · Misattributed.** The user credits a line about patience to
  a 19th-century ferry captain. The line first appears, opened, in a 1987 self-help book that
  paraphrases the captain's logbook; the logbook, opened, says something narrower.
- **Echo · Primary differs · Mutated · Origin retracted.** The user says a soil additive doubles
  wheat yields. The trial that started the claim, opened, reported a smaller gain on one farm; its
  journal's retraction notice, opened, withdraws it.
