# The procedure, step by step

The full definition of each step of `SKILL.md`'s procedure. Steps 3 to 6 are internal: only
their results reach the report.

## 1. Gate

Decide which row of the Inputs table the input is.

- **Two positions.** Each is in its author's own words, and the two are told apart: labelled A
  and B, or given under two names or roles. Run.
- **A transcript.** A chat log, a thread, an email chain or a debate with two identifiable
  speakers. Run, and attribute each claim to the speaker who made it, never to the one who
  answered it. A speaker's position is what they said across the whole transcript, not one
  message.
- **One-sided.** One party's own position, and that party's account of what the other thinks
  ("my business partner says…", "they think…"). The sign is one voice giving both sides. Gate it.
- **Anything else.** A single position with no account of the other side, a topic with no
  positions, or more than two parties. Ask for two positions labelled A and B.

**Labels.** The report calls the parties A and B, whatever the input calls them. Where the input
uses other labels or names, A is the party named first (in a transcript, the first to speak)
unless the user says otherwise, and the two steelman lines add the name or role in brackets. In
a one-sided input, A is always the party whose own words you have.

### Asking

Ask once, in one short message, and stop until the user answers. Write no report while you wait.

- **Anything else:** ask for two positions, labelled A and B, each in its author's own words, or
  a transcript of the two.
- **One-sided:** ask once for the other party's own words, or a transcript of the exchange.

### When the user proceeds without the other side

If the user cannot or will not share B's own words, or asks you to go ahead, run on what you have:

- label B's steelman `**B (reconstructed by A), strongest form:**`;
- cap Confidence at Low, with the reason that B's side is A's account of it;
- suggest, in Confidence, sharing the report with B to confirm their side.

### You as one of the parties

If one of the two parties is you, in the current conversation (the user disputes something you
said and asks where the two of you really disagree), still run. The report's first line says
that you are one of the parties and recommends re-running in a fresh session with the transcript
pasted as input.

## 2. Steelman

The strongest form of a position is the version its author would accept as better put than their
own words: the same conclusion, the best reasons the input gives for it, its premises made
explicit.

- **2 to 4 sentences** for each side, at most 50 words.
- **Only content present in the input.** No new evidence, no new arguments, no outside facts.
- **`[inferred]`** follows any premise the conclusion needs but the input never states. Infer
  only what the position cannot stand without.
- **Symmetry.** The two steelmen are within ±25% of each other by word count, with the same care
  for each. If one runs long, cut it back rather than padding the other.
- **Each in terms its author would accept,** without the other side's loaded words.

## 3. Claim map

Break each position into atomic claims: one assertion each, which can be true or false, or
accepted or rejected, on its own. Split a claim joined by "and" into two. Number them `A1..An`
and `B1..Bn`, and tag each:

- **`stated`** if the input says it, in words or in close paraphrase; **`inferred`** if the
  position needs it but never says it (the steelman's `[inferred]` premises);
- **`conclusion`** for what the party argues for, usually one per party; **`premise`** for a
  reason given for it;
- **dependencies:** `A3 depends on A1` when A3 holds only if A1 does.

The map stays internal. When the user asks for it, it is appended in the format of
`output-template.md`.

## 4. Common ground

List the claims both parties accept: explicitly, when both state it, or by clear implication,
when one states it and the other's argument assumes it. Silence is not agreement: a claim one
side makes and the other never touches is neither common ground nor in conflict.

## 5. Conflict set

Pair the claims that cannot both be true (facts, forecasts) or cannot both be accepted (values,
meanings). Each pair names the claim at issue, X.

Each claim in a pair is stated by its own party, in words or close paraphrase. A premise you
inferred, or a point one party never touches, is in no pair, however much the other side's case
rests on it: when one side argues from such a point and the other never answers it, the conflict
is the stated claim it supports. Silence is not disagreement, as it is not agreement (step 4).

An apparent conflict that dissolves once a shared word is split into its two meanings, or once
two questions are told apart, leaving both parties agreeing on everything else, is not a
conflict. It goes under *Not actually in dispute*.

## 6. Crux test

For each pair, take the claim at issue, X, and ask both ways:

- If A adopted B's view of X, keeping everything else A holds, would A's conclusion change?
- If B adopted A's view of X, keeping everything else B holds, would B's conclusion change?

A conclusion changes when its party could no longer reach it on the reasons they give.

- **Yes for both:** a double crux.
- **Yes for one:** a crux for that party.
- **No for both:** drop it from the report.

**Rank** double cruxes first, then by depth: a claim other conflicts depend on, by step 3's
dependencies, outranks the claims that depend on it. The **primary crux** is the deepest double
crux, else the deepest single crux. The next two by the same ranking are the **secondary
cruxes**; report no more than two. If two cruxes rank equal, report one as primary, put the
other first among the secondary cruxes, and say in Confidence that the two are close.

## 7. Classify

Give each reported crux exactly one type, by `crux-types.md`: Empirical, Predictive,
Definitional, Value or Framing.

## 8. Resolution path

For each reported crux, what would move it, by its type:

- **Empirical:** the specific evidence that would settle it: the data source, the study type or
  the measurement, and which records. Name the evidence, never the answer: do not say what it
  will show.
- **Predictive:** an observable forecast with a date both could check: what both could look at,
  and when, that would show which way it went.
- **Definitional:** two labelled terms replacing the shared word, one for each meaning, so each
  side can state its claim without the word.
- **Value:** name the trade-off: which goods are weighed against which, and how each side weighs
  them. Offer no resolution: no compromise, no ranking of the goods.
- **Framing:** state both questions separately, each as a question, without quotation marks.

## 9. No-conflict exit

If step 6 yields nothing (the conflict set is empty, or every pair was dropped):

- **The parties answer different questions** (their conclusions seem to clash, but their reasons
  answer different questions): report a Framing crux. Run the crux test on the question itself:
  if A took up B's question, would A's conclusion change? Then the reverse. Label the crux by the
  result; if neither conclusion would change, the positions do not conflict.
- **Otherwise,** state that the positions do not conflict: *The crux* reads **No crux**, with one
  neutral sentence saying why both positions can hold at once, and Secondary cruxes says `None.`

Never manufacture a crux to fill the report.
