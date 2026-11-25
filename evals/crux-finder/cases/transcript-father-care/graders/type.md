---
type: llm
---

The reply answers a request to find where two parties really disagree. It is either a crux
report, which has a `## Crux report` heading and a `### The crux` section, or a question back to
the user. A report's primary crux is the one-sentence blockquote right under the label that
opens `### The crux`: **Double crux**, **Crux for A** or **Crux for B**, then ` · ` and a type,
or **No crux** alone. A crux under `### Secondary cruxes` is not the primary crux.

The expected type of the primary crux is Value. The answer the maintainer wrote before any run
says:

> A run whose primary crux is whether carers would keep him safe counts no for crux and type,
> since both concede it.

PASS if the reply is a crux report whose primary crux's label names the type Value, whichever of
Double crux, Crux for A or Crux for B comes before it, and whose primary crux is not whether
carers would keep him safe.

FAIL otherwise.

Judge only the type the label names, as the report writes it, and the rule above; do not judge
whether that type is right for the crux.
