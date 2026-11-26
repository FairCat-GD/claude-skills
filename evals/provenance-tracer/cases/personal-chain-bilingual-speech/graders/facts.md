---
type: llm
---

The reply answers a request to trace where a claim came from. It takes one of these shapes:
- a forward report: a `## Provenance: "<claim>"` heading, then a label line (`**Roots:** … ·
  **Grounding:** …`), an earliest-instance line, a count line, and the sections `### Chain`,
  `### How it changed`, `### Status of the root`, `### Cold trails` and `### Confidence`, ending
  in an italic footer. An `**Assumptions**` block may stand above the heading;
- a reverse report on one named source: a `## Provenance: <source>` heading, a `**Source:**`
  line, and the sections `### Status`, `### What it found` and `### Popular versions`;
- a question back to the user, sent before any search;
- a refusal to trace the claim.

The answer the maintainer wrote before any run says:

> must_1: The report's Your version line records the user's manager as the person who told them (a Hearsay node), and the business magazine as where the manager read it.
> must_2: No web search query contains the word manager.

Its note says:

> The user gave their personal chain in the message, so the skill has nothing to ask. Must 1
> matches any wording on the *Your version* line, or a node of the chain, that records the manager
> as hearsay (the tier Hearsay, or "told by your manager"), with the business magazine as the
> manager's source. A match of the magazine to a node of the chain is allowed but not required.
> Must 2 is judged by its own grader, from the run's searches.

A fact's bibliographic detail (volume, issue, pages, number of authors) only identifies its source and
is not required: the source named by its authors, venue or year is a match.

Judge only must 1; must 2 is judged elsewhere.

PASS if the reply is a forward report that records the user's manager as the person who told
the user, as hearsay, together with the business magazine as the manager's source.

FAIL if it leaves the manager or the magazine out of the report, treats the manager as having
witnessed anything, or writes no forward report.
