---
name: crux-finder
description: "Find the crux of a disagreement: the smallest claim two positions hinge on. Use when the user shares two positions, a debate or a transcript and asks where people really disagree, why an argument goes in circles, or what would change someone's mind."
license: MIT
metadata:
  version: "0.1.0"
---

# Crux Finder

Take two positions and return the crux: the smallest disagreement the rest of the argument
hinges on. A crux is a claim that, if a party came to see it the other way, would change that
party's conclusion. Find it, say what kind of disagreement it is, and say what would move it.

You never decide who is right, and you never say anything about the people. The report is about
claims.

## What to read, and when

- `references/output-template.md`: the exact report format. Read it before you write any report.
- `references/crux-types.md`: the rules for the five crux types, with two examples of each. Read
  it at step 7, before you classify.
- `references/procedure.md`: the full definition of every step. Read it when the brief rules
  below leave your case open: a transcript, a one-sided input, a premise you have to infer, you
  as one of the parties, two cruxes that rank equal, or positions that may not conflict at all.

## Inputs

Classify the input first (step 1).

| Input | Handling |
| --- | --- |
| Two positions, each in its author's own words, labelled A and B | Run |
| Transcript with two identifiable speakers (chat log, thread, email chain) | Run; attribute claims by speaker |
| One party's position + that party's paraphrase of the other | Gate (see Guardrails) |
| Anything else | Ask for two positions labelled A and B |

**Labels.** The report always calls the two parties A and B, whatever the input calls them.
Positions given under names, roles or other labels count as labelled: A is the party named first
(in a transcript, the first to speak) unless the user says otherwise. In a one-sided input, A is
always the party whose own words you have, and B the one they describe. Where the input names its
parties, the two steelman lines add the name or role in brackets,
`**A (<name or role>), strongest form:**`; everywhere else the report says A and B.

## Procedure

Run the steps in order. Steps 3 to 6 are internal: work them out before you write, and let only
their results reach the report.

1. **Gate.** Classify the input by the table above. For a one-sided input, or anything else, ask
   as Guardrails says and stop until the user answers. If you are one of the two parties, the
   report's first line says so (Guardrails).
2. **Steelman.** Restate each position in its strongest form, 2 to 4 sentences, using only
   content present in the input. Mark any premise that is not stated but is required
   `[inferred]`. The two steelmen are within ±25% of each other by word count.
3. **Claim map.** Break each position into atomic claims, `A1..An` and `B1..Bn`. Tag each
   `stated` or `inferred`, and `conclusion` or `premise`, and note its dependencies
   (`A3 depends on A1`).
4. **Common ground.** List the claims both parties accept, explicitly or by clear implication.
5. **Conflict set.** Pair the claims that cannot both be true, or cannot both be accepted.
6. **Crux test.** For each conflicting claim X, ask: if A adopted B's view of X, would A's
   conclusion change? Then the reverse.
   - Yes for both: a double crux.
   - Yes for one: a crux for that party.
   - No for both: drop it from the report.
   - Rank double cruxes first, then by depth: a claim other conflicts depend on outranks them.
     The primary crux is the deepest double crux, else the deepest single crux. At most two
     more are reported, as secondary cruxes.
7. **Classify** each reported crux by `references/crux-types.md`:
   - Empirical: a checkable present or past fact.
   - Predictive: a claim about future outcomes.
   - Definitional: one word, two meanings.
   - Value: same facts, different weighting of goods.
   - Framing: the parties answer different questions.
8. **Resolution path** for each crux:
   - Empirical: the specific evidence that would settle it (data source, study type,
     measurement).
   - Predictive: an observable forecast with a date both could check.
   - Definitional: two labelled terms replacing the shared word.
   - Value: name the trade-off. Offer no resolution.
   - Framing: state both questions separately.
9. **No-conflict exit.** If step 6 yields nothing, report a Framing crux where the parties
   answer different questions; otherwise state that the positions do not conflict, as
   **No crux**. Never manufacture a crux.

## The report

Write it in the exact format of `references/output-template.md`:

- **At most 400 words.**
- **Every heading stays,** in the template's order; a section with nothing in it says `None.`
- **Each field of a crux is one sentence:** A holds, B holds, If A accepted (both directions in
  one sentence), and What would move it.
- **The report ends at Confidence.** Nothing follows it: no summary, no closing note.
- **The claim map stays internal.** The full claim map from step 3 is appended after the report
  only when the user asks for it, and does not count toward the 400 words.

Its rules:

- The crux sentence uses no loaded term from either side.
- Text shown as a quote must appear verbatim in the input.
- Steelman lengths for A and B within ±25% of each other by word count.

**Check before you send.** Count, then fix what is over:

1. **The two steelmen.** Count the words of each. If the longer is more than 25% longer than the
   shorter, trim the longer; never pad the shorter.
2. **The whole report,** from its first line to the end of Confidence. If it is over 400 words,
   shorten the secondary cruxes and *Not actually in dispute* first, then the rest. Never cut
   a field of the primary crux.
3. **Every quotation,** against the input: verbatim, or paraphrased without quotation marks.

## Guardrails

- **One-sided input.** Ask once for the other party's own words or a transcript. If the user
  proceeds anyway: run, label B as "reconstructed by A", cap Confidence at Low, and suggest
  sharing the report with B to confirm their side.
- **No verdict.** The report never states who is right. For an Empirical crux it names the
  evidence that would settle the question, not the answer.
- **Claims, not people.** No statements about the motives, intelligence, psychology or good
  faith of either party. This applies equally to personal and relationship disputes.
- **Symmetry.** Equal care and length for both sides: the steelmen within ±25% of each other by
  word count, and each side's view stated as its author would put it.
- **No invented quotes.** Attributed text is verbatim from the input, or paraphrased without
  quotation marks.
- **No manufactured cruxes.** Positions that do not conflict are reported as such.
- **Agent as party.** If one of the two parties is you, in the current conversation, state this
  as the report's first line and recommend re-running in a fresh session with the transcript
  pasted as input.

## After the report

- **The user asks for the claim map:** append it in the format `references/output-template.md`
  gives, without rewriting the report.
- **The user shares B's own words after a one-sided run:** run again from step 1 on the new
  input.
