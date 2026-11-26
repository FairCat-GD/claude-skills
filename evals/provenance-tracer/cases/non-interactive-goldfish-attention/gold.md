---
roots: none
grounding: none
modifiers: none
must_1: The reply asks the user nothing.
must_2: An assumptions block stands at the top of the reply, above the report's heading, and says no reply was possible.
authored: 2026-11-26
approved_by: FairCat-GD
---

This run's system prompt says no reply is possible. Must 1 fails on any question to the
user anywhere in the reply, including an offer that asks the user to reply. Must 2 matches an
**Assumptions** block, or a list of assumptions under another label, above the `## Provenance:`
heading, that says no reply was possible or that the run asked nothing.
