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
- **A Primary speaks to the claim:** it holds an assertion the claim could be a version of, the
  same idea with another number, subject, scope, strength, cause, wording or author. A work is
  **silent** on the claim only when you read the passage the citing page points to, or the whole
  text, in a copy checked to be the work (`search-playbook.md`, *Opening a page*), and it holds
  no such assertion. A silent work is no Primary for this claim, and the citation of it does not
  hold: it is not drawn as a node or a credited text, the citing node's branch ends
  `→ stopped: citation does not hold`, one bullet under *Status of the root* says what the work
  covers, and it adds nothing to Grounding or to the retellings counted. An abstract, a record,
  or a copy that leaves the passage out (another volume, edition or language, a text cut short)
  does not make a work silent: try another copy, or keep it `(not opened)`.
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
4. **Precursors are not roots.** A precursor is a work, beside a root that retellings credit,
   that no retelling of the claim credits itself: one the root names as background, or one that
   only a page recording its author's career, or the root's own reference list, ties to the claim
   (rule 8), whether or not the root names it. Name it in a background bullet under *Status of
   the root*, never as a root, as the earliest instance or as a retelling. A precursor is not
   something earlier the root cites: the root still cites nothing earlier, even where it names
   the precursor beside the claim, and a study with its own data stays a Primary for its own
   finding.
5. **A misattribution adds no root.** A node may credit the claim to a person or work whose own
   text, once opened, does not state it as theirs. Then the root is where the claim's words or
   finding first appear. The credited text, where it speaks to the claim (*Tiers*), counts as one
   opened Primary that differs, weighed with any other opened Primary by the Grounding rule for
   several Primaries below. It is drawn under the node that credits it and ends that branch, and
   it is not a root. A credited text silent on the claim is no Primary, as *Tiers* says. Either
   way, the credit gives Misattributed when the user's version carries it.
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

   **A root beyond the first needs a retelling that credits it,** as a source of the claim or as
   an earlier instance of it. A retelling passes on the claim or weighs its evidence, whatever
   else it is about: a news story, a blog, a fact-check, a quotation page, a review or a history
   of the evidence. What decides is what the page does with the claim, not whom it is about. A
   page that only records, as one fact of a person's career, that their work made the claim (a
   biography, an encyclopedia entry on them, an obituary) does not make that work a further
   root, and nor does a reference list: beside a root that retellings credit, the work is a
   precursor (rule 4), and the page is not drawn as a node.

## Counting retellings

**Retellings found** counts the nodes you found by search: the root, every node on a chain, and
every cold trail. The user's own version, and the Personal and Hearsay nodes of the personal
chain, are not counted. Nor are a credited text, which does not state the claim, or a precursor,
a silent work or a page *Roots* rule 8 keeps out of the chain, which are no nodes. A
`(not opened)` node is counted, since an opened page names it.

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
| Grounded | a Primary was opened and states the claim: as the user put it, or with no drift that changes what it asserts. A study whose own data show the claim's finding states it, an association included, unless the study itself hedges or disclaims the cause |
| Primary differs | a Primary was opened and says something materially different on the claim's point: a different number, scope, strength, cause or author |
| No primary found | no Primary was opened (a Primary known only as `not opened` counts as none, and so does a work silent on the claim) |

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
- **A biography is no retelling.** The user says a hot drink before bed shortens sleep. Every
  retelling cites a 2009 sleep-lab study with its own data, the root. An encyclopedia entry on a
  physician says she made the same claim in a 1994 paper, and no retelling of the claim credits
  that paper. Echo, one root: the 1994 paper is a background bullet, not a second root and not
  the earliest instance.
- **A cited work that differs, and one that is silent.** The user says a third of commuters fall
  asleep on the train. A blog cites two sources for it: a rail operator's 2004 passenger survey
  and its annual accounts. The survey, opened in full, gives a quarter: it speaks to the claim
  with another number, a Primary that differs. The accounts, opened in full, give fares and
  ridership and nothing on sleep: silent, so the citation of them does not hold. A bullet under
  *Status of the root* says what they cover, and they are neither a node nor a Primary.
- **Echo · Primary differs · Mutated · Origin retracted.** The user says a soil additive doubles
  wheat yields. The trial that started the claim, opened, reported a smaller gain on one farm; its
  journal's retraction notice, opened, withdraws it.
