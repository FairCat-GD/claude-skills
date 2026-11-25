---
type: llm
---

The reply answers a request to find where two parties really disagree. It is either a crux
report, which has a `## Crux report` heading and a `### The crux` section, or a question back to
the user. A report's primary crux is the one-sentence blockquote right under the label that
opens `### The crux`: **Double crux**, **Crux for A** or **Crux for B**, then ` · ` and a type,
or **No crux** alone. A crux under `### Secondary cruxes` is not the primary crux.

The expected primary crux, in the answer the maintainer wrote before any run:

> Whether the panels' savings would reach the hall's £6,000 share within ten years.

Any wording about whether the panels pay for themselves within ten years is a match.

PASS if the reply is a crux report whose primary crux is a match.

FAIL if the reply has no crux report, or if its label is **No crux**, or if its primary crux is
about anything else, even where a secondary crux is a match.

Judge only what the primary crux is about: its type label, its exact wording and the rest of the
report do not matter here.
