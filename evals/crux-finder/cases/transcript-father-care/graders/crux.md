---
type: llm
---

The reply answers a request to find where two parties really disagree. It is either a crux
report, which has a `## Crux report` heading and a `### The crux` section, or a question back to
the user. A report's primary crux is the one-sentence blockquote right under the label that
opens `### The crux`: **Double crux**, **Crux for A** or **Crux for B**, then ` · ` and a type,
or **No crux** alone. A crux under `### Secondary cruxes` is not the primary crux.

The expected primary crux, in the answer the maintainer wrote before any run:

> Whether their father's own wish to stay at home should come before lowering his risk of
> another serious fall, with that risk agreed by both.

Any wording that sets his wish to stay against lowering his risk of a fall is a match.

The answer also says:

> A run whose primary crux is whether carers would keep him safe counts no for crux and type,
> since both concede it.

PASS if the reply is a crux report whose primary crux is a match.

FAIL if the reply has no crux report, or if its label is **No crux**, or if its primary crux is
about anything else, even where a secondary crux is a match, or if its primary crux is the one
the answer counts no.

Judge only what the primary crux is about: its type label, its exact wording and the rest of the
report do not matter here.
