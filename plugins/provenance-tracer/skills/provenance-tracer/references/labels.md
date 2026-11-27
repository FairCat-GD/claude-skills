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

- **A node is Primary only if you opened it:** a paper whose abstract or full text you fetched,
  for what that text states, or a book's, speech's or document's passage, from any copy whose text
  the fetch returned. Try other copies first (`search-playbook.md`, *Opening a page*). A Primary
  you know only because an opened page names it is `Primary (not opened, per <opened source>)`,
  and the report's Confidence is at most Medium.
- **A work that gives the claim with a source for it is a node that cites that source,** whatever
  kind of work it is: a chart's source line, a footnote, *according to X*. It is a Primary only for
  its own data or its own text. A report, an advert or a survey that passes on someone else's
  figure is no Primary for that figure.
- **Personal and Hearsay nodes come from the user,** in the personal chain (forward step 2). They
  are shown on the *Your version* line, never searched by name unless they are public figures or
  publications, and never counted as retellings.
- **A page that only summarises search results,** such as an index or an aggregator with no text
  of its own, is not a node; open what it points to instead.

## Roots

A **root** is where a chain begins. Find the roots this way:

1. **Follow every chain back** until a node cites nothing earlier. A node *cites* what it gives
   as the source of the claim's words, number or finding. Naming a person, work or body as that
   source counts, even with no link or reference: a page that says *as the survey found* cites
   the survey.
2. **A node that cites nothing earlier and originates the claim is a root:** a Primary that is its
   own data, study, document, speech or text, or the work the claim grew from.
3. **A study with its own data is where its own finding begins.** What it names as background, as
   a method, or as the idea it set out to test is not a hop.
4. **Precursors are not roots.** A work that a root names, but that no retelling of the claim
   cites, is a precursor: name it in a background bullet under *Status of the root*, never as an
   earlier root or as the earliest instance. A page about its author, or the root's own
   reference list, does not make it a retelling. A precursor is not something earlier the root
   cites: the root still cites nothing earlier, even where it names the precursor beside the
   claim, and a study with its own data stays a Primary for its own finding.
5. **A misattribution adds no root.** A node may credit the claim to a person or work whose own
   text, once opened, does not state it as theirs. Then the root is where the claim's words or
   finding first appear. The credited text counts as one opened Primary that differs, weighed
   with any other opened Primary by the Grounding rule for several Primaries below, and it gives
   Misattributed when the user's version carries the credit. It is drawn under the node that
   credits it and ends that branch, and it is not a root.
6. **Where no chain reaches such an origin, the earliest instance found is the one root.**
7. **Every other node that states the claim and cites nothing is a cold trail:** listed under
   *Cold trails*, counted as a retelling, never as a root. Two blog posts that each repeat a claim
   with no source are cold trails of one root, not two roots.
8. **Two roots are independent origins,** each reached by its own chain: two documents written
   apart, or two studies by different teams, each with its own data. A study by another team with
   its own data is a root of its own when retellings of the claim credit it as a source, even if
   it names the earlier study as background. Studies by one team are one root. A review, a
   meta-analysis, a guideline or a textbook weighs others' data: it is a node, and the studies it
   names are leads to follow.

## Counting retellings

**Retellings found** counts the nodes you found by search: the root, every node on a chain, and
every cold trail. The user's own version, and the Personal and Hearsay nodes of the personal
chain, are not counted. Nor are a credited text, which does not state the claim, or a precursor,
which is no node. A `(not opened)` node is counted, since an opened page names it.

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

The three *Origin* modifiers need an opened notice or study: a page that only calls a study
*discredited* is a lead to follow, not a status. With no Primary root, none of them applies.

## The label line

````markdown
**Roots:** Echo · **Grounding:** Primary differs · Mutated · Misattributed
````

The count line below it, `**Roots:** 1 · **Retellings found:** 5`, gives the number of roots and of
retellings found. It is a different line, though it starts with the same word.

## Examples

Invented: one for each value, and one for each roots rule that is easy to get wrong.

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
- **Independent · Grounded, the later study naming the earlier.** The user says that walking to
  work lowers blood pressure. A 1962 survey of Tarrow postal workers, with its own data, found it.
  A 1981 cohort study of Elsby office staff, by another team with its own data, found it too, and
  names the 1962 survey as its background. Retellings credit both. Two roots.
- **Echo · Primary differs · Mutated · Misattributed.** The user credits a line about patience to
  a 19th-century ferry captain. The line first appears, opened, in a 1987 self-help book that
  paraphrases the captain's logbook; the logbook, opened, says something narrower. The book is
  the one root; the logbook is the credited text, drawn under the node that credits it, not a
  second root.
- **A precursor.** The user says a fertiliser makes tomatoes sweeter. Every retelling cites a 2004
  trial with its own data, the root. The trial names a 1990 greenhouse note as the idea it tested;
  no retelling cites the note, so it is a background bullet under *Status of the root*.
- **Echo · Primary differs · Mutated · Origin retracted.** The user says a soil additive doubles
  wheat yields. The trial that started the claim, opened, reported a smaller gain on one farm; its
  journal's retraction notice, opened, withdraws it.
