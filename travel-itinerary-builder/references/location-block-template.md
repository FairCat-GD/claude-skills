# Location block template

Compact, scannable, with personality. Every sightseeing stop uses this structure.

## Sightseeing block — required fields

```
### [N]. [Place name] · [Wikipedia](https://en.wikipedia.org/wiki/...)

**What & why:** 3–4 sentences in an engaging guide voice. Describe what it feels like to be there, not just facts. Include one specific detail or story when you have one.
**Time to spend:** ~[X] hr
**Hours:** [HH:MM–HH:MM] (verify)  *(append day or closed days if it varies, e.g. "10:00–18:00, closed Mon")*
**Entry fee:** [local amount] (~[home currency amount])
**Booking:** [Advance ticket required / Timed entry recommended / Walk-up fine] *(omit if no booking concern)*
**Getting there:** From [previous stop], [walk / metro line + stations / bus + route / drive + parking], ~[X] min.
**Tip:** [Optional — best time of day, what to skip inside, photo spot, etc.]
```

## Restaurant block — required fields

Same idea, with a Rating line added. Drop "Booking" if walk-in.

```
### [N]. [Restaurant name](official website, or the rating-source URL if it has none) · [Cuisine / vibe in 3 words]

**Why here:** 2–3 sentences. What they're known for, what the room feels like, why it fits the route.
**Rating:** [4.6/5 TripAdvisor (1,200+ reviews) / 1 Michelin star, 2024 guide / etc.]
**Price range:** [local symbol + approx per person] (~[home currency])
**Hours:** [HH:MM–HH:MM, closed Mondays]
**Booking:** [Reservation recommended / Walk-in OK]
**Getting there:** From [previous stop], [transport], ~[X] min.
**Tip:** [What to order, where to sit, what to skip]
```

## Snack/drink stop — optional mini-block

Inserted *between* anchor blocks when a small, characteristic on-route bite or sip would genuinely add to the day. Examples: the Ladurée counter on the Champs-Élysées; *balık-ekmek* boats by Galata Bridge in Istanbul; a Pyana Vyshnya kiosk in Lviv; a granita at a *bar* in Palermo.

**Three rules — all must hold:**
1. **On-route** — ≤2 min off the line of travel between two anchor blocks.
2. **Characteristic** — something locals are quietly proud of, not a generic café.
3. **Small enough that skipping it costs nothing** — one cup, one shot, one pastry. Never a sit-down meal.

**Do not invent these.** If no spot fits the three rules, leave the concept out for that route — forced snack stops feel padded and cheapen the rest of the document.

Visual treatment: no order number and **no marker glyph** — the tinted background and indent already set it apart. Lead with the bold name, italic body, indented slightly under the previous block. Render in the PDF with a subtle tinted background and a smaller font size (see `output-formats.md` for the CSS).

```
> **[Name]** — *2 sentences on why this little bite/sip is what locals are quietly proud of, and exactly where it is.* (Open [hours]; ~[X] UAH / per item)
```

### Worked example — snack stop

```
> **Pyana Vyshnya kiosk** — *Lviv's iconic cherry-vodka shot, sold from corner kiosks in carved wood stalls since 1900. One shot, one cherry left in the glass, gone in fifteen seconds. The one on Soborna Square is the original.* (Open 11:00–23:00; ~80 UAH a shot)
```

## Worked example — sightseeing

```
### 2. Jerónimos Monastery · [Wikipedia](https://en.wikipedia.org/wiki/Jer%C3%B3nimos_Monastery)

**What & why:** Manueline architecture at its most exuberant — every column carved with rope, shells, and astrolabes, a 16th-century shipbuilder's stone catalogue of an empire reaching east. Vasco da Gama is buried in the church to your right as you enter. The cloister, two stories of pale limestone, is where the building stops being a monument and starts being a place you want to sit in.
**Time to spend:** ~1.5 hr
**Hours:** 10:00–17:30, last entry 17:00 (verify)
**Entry fee:** €12 (~$13). Church is free; cloister is paid.
**Booking:** Advance timed ticket strongly recommended in May — walk-up lines are 45+ min.
**Getting there:** From Belém Tower, walk 12 min east along the riverside park.
**Tip:** The cloister's upper level gets the best light in late morning. Skip the carriage museum next door unless you have extra time.
```

## Worked example — restaurant

```
### 3. Cervejaria Ramiro · seafood institution

**Why here:** A Lisbon ritual since 1956. You sit on plastic-y banquettes under fluorescent light and eat plate after plate of garlic prawns, tiger shrimp, percebes, and crab — finished with a prego steak roll because that's the rule. Service is brusque and fast; the queue out the door means it's working.
**Rating:** 4.5/5 Google Maps (28,000+ reviews); featured in Time Out Lisbon
**Price range:** €25–40 per person (~$27–43)
**Hours:** 12:00–24:00; closed Mondays
**Booking:** Walk-in only — go before 19:30 or after 22:00 to skip the worst of the queue
**Getting there:** From Igreja de São Vicente, Metro yellow line, Anjos to Intendente — 4 min — then a 5-min walk.
**Tip:** Order in waves, not all at once. Start with prawns and percebes, then judge appetite before the crab. End with the prego — non-negotiable.
```

## Formatting notes

- Prices always **local first, then home currency in parentheses**. Use a single exchange rate across the document and note it once in the Trip Context section.
- Hours: write `(verify)` if you couldn't confirm on the official site. Never invent. Append day-of-week or closure info inline ("10:00–18:00, closed Mon") rather than using a separate label.
- Wikipedia link goes on the place name as plain hyperlinked text — no arrow or other glyph.
- Restaurant ratings: prefer Google Maps or TripAdvisor for general spots, Michelin/Bib Gourmand for higher-end, named press for niche picks. Include review count when high (>500) since that signals reliability.
- **Hyperlink the restaurant name** to its official website; if it has none, link to the rating source you used (its Google Maps listing, TripAdvisor page, or Michelin/guide entry). Applies to both the daily route blocks and the Appendix A table. Never invent a URL — if you can't find a real one, leave the name unlinked.
- "Tip" is optional and only included when you actually have a non-obvious one. A weak tip is worse than no tip.
- Snack stops are optional. When in doubt, leave them out — forced snack stops cheapen the rest of the document.
