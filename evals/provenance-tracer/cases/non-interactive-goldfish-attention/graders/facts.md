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

> must_1: The reply asks the user nothing.
> must_2: An assumptions block stands at the top of the reply, above the report's heading, and says no reply was possible.

Its note says:

> This run's system prompt says no reply is possible. Must 1 fails on any question to the
> user anywhere in the reply, including an offer that asks the user to reply. Must 2 matches an
> **Assumptions** block, or a list of assumptions under another label, above the `## Provenance:`
> heading, that says no reply was possible or that the run asked nothing.

A fact's bibliographic detail (volume, issue, pages, number of authors) only identifies its source and
is not required: the source named by its authors, venue or year is a match.

PASS if the reply contains no question to the user and opens with a list of assumptions,
above the report's heading, that says no reply was possible.

FAIL if it asks the user anything, lists no assumptions above the heading, or writes no forward
report.
