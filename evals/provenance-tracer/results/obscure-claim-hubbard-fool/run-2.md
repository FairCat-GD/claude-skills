---
case: obscure-claim-hubbard-fool
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:18:18Z
cost_usd: 1.4956
duration_s: 292
turns: 36
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- Read: <plugin>/skills/provenance-tracer/references/labels.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- WebSearch: "every man is a damn fool for at least five minutes every day"
- WebSearch: "wisdom consists in not exceeding the limit"
- WebSearch: Elbert Hubbard damn fool five minutes a day quote source
- WebSearch: "five minutes every day" fool "not exceeding the limit" Hubbard
- WebSearch: who first said "damn fool for at least five minutes"
- WebSearch: quoteinvestigator OR wikiquote Hubbard "five minutes" fool wisdom limit
- WebFetch: https://quoteinvestigator.com/2026/11/20/fool-minutes/
- WebFetch (error): https://wist.info/author/hubbard-elbert-green/
- WebSearch: "The Philistine" 1909 volume 29 archive.org Hubbard "dam fool"
- WebSearch: "A Thousand & One Epigrams" Hubbard "dam fool" OR "damn fool" "not exceeding the limit"
- WebFetch: https://en.wikiquote.org/wiki/Elbert_Hubbard
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28philistine%29+AND+date%3A%5B1909-01-01+TO+1910-12-31%5D&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=date&rows=50&output=json
- WebFetch (error): https://wist.info/author/hubbard-elbert-green/
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28thousand+one+epigrams%29+OR+title%3A%28roycroft+dictionary%29&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=date&rows=50&output=json
- WebFetch: https://www.gutenberg.org/cache/epub/36566/pg36566.txt
- WebFetch: https://archive.org/stream/roycroftdictiona00hubbuoft/roycroftdictiona00hubbuoft_djvu.txt
- WebFetch: https://archive.org/stream/roycroftdictiona00hubbuoft/roycroftdictiona00hubbuoft_djvu.txt
- WebFetch: https://archive.org/stream/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt
- WebFetch: https://archive.org/stream/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt
- WebFetch: https://archive.org/stream/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt
- WebSearch: "Philistine" "periodical of protest" volume 29 1909 full text hathitrust OR archive.org
- WebFetch: https://archive.org/advancedsearch.php?q=identifier%3Asim_philistine-a-periodical-of-protest_1909*+OR+identifier%3Asim_philistine-a-periodical-of-protest_1910-01*&fl%5B%5D=identifier&fl%5B%5D=date&rows=50&output=json
- WebFetch: https://catalog.hathitrust.org/Record/000679447
- WebFetch: https://www.google.com/books/edition/_/MUsLAQAAIAAJ?gbpv=1&bsq=%22exceeding%20the%20limit%22
- WebFetch: https://books.google.com/books?id=MUsLAQAAIAAJ&newbks=0&printsec=frontcover&q=%22exceeding+the+limit%22
- WebFetch: https://www.azquotes.com/quote/531137
- WebFetch: https://www.goodreads.com/quotes/80344-every-man-is-a-damn-fool-for-at-least-five
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28thousand+epigrams%29+AND+creator%3A%28hubbard%29&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=date&rows=20&output=json

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Elbert Hubbard said that every man is a damn fool for at least five minutes every day, and that wisdom consists in not exceeding the limit."

**Roots:** Echo · **Grounding:** Grounded · Mutated
**Earliest instance found:** *The Philistine: A Periodical of Protest*, Vol. 29, No. 6, a filler item on p. 192, The Roycrofters, East Aurora, NY, 1909 (date from: cited by [Quote Investigator](https://quoteinvestigator.com/2026/11/20/fool-minutes/)). This version says "ten minutes a day." Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 10

### Chain
Your version: "Elbert Hubbard said: every man is a damn fool for at least five minutes every day; wisdom consists in not exceeding the limit" (where you met it: not given)
 ├─ [AZQuotes](https://www.azquotes.com/quote/531137), date unknown, Tertiary → cites
 │   └─ *A Thousand & One Epigrams*, Elbert Hubbard, 1911, (not opened), per AZQuotes, which gives no page → stopped: not opened
 ├─ [Goodreads](https://www.goodreads.com/quotes/80344-every-man-is-a-damn-fool-for-at-least-five), date unknown, Tertiary → cites
 │   └─ [*The Roycroft Dictionary Concocted by Ali Baba and the Bunch on Rainy Days*](https://archive.org/stream/roycroftdictiona00hubbuoft/roycroftdictiona00hubbuoft_djvu.txt), 1914 (date from: byline), Primary. I searched its whole OCR text and the line does not appear, so this citation does not hold → stopped: does not state the claim
 ├─ [Wikiquote, *Elbert Hubbard*](https://en.wikiquote.org/wiki/Elbert_Hubbard), date unknown, Secondary → cites
 │   └─ [*Roycroft Dictionary and Book of Epigrams*](https://archive.org/stream/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt), The Roycrofters, 1923 (date from: byline), Primary (Hubbard's text, published by his own press). It reads: "Every man is a damn fool for at least five minutes every day." The next sentence, about not exceeding the limit, follows near p. 129 → cites nothing
 └─ [Quote Investigator, *Quote Origin: Everyone Is a Damn Fool at Least Ten Minutes a Day…*](https://quoteinvestigator.com/2026/11/20/fool-minutes/), 2026 (date from: byline), Secondary. Its conclusion: "Elbert Hubbard deserves credit for this saying." → cites
     ├─ Dale Carnegie, *How to Stop Worrying and Start Living*, ch. 22, p. 175, 1948, (not opened), per Quote Investigator. Credits Hubbard and ends "not exceeding that limit"
     ├─ *The Fra*, Vol. 4, No. 6, p. 168, March 1910, (not opened), per Quote Investigator. Hubbard's "time-limit" variant
     ├─ *The Philistine*, Vol. 30, No. 2, p. 57, January 1910, (not opened), per Quote Investigator. Hubbard's first "five minutes" version, followed by a different second sentence
     ├─ *The Issue*, ed. James K. Vardaman, Jackson, Mississippi, p. 5, 13 November 1909, (not opened), per Quote Investigator. A reprint credited to *The Philistine*, spelled "damn"
     └─ *The Philistine*, Vol. 29, No. 6, p. 192, November 1909, Primary (not opened, per Quote Investigator). The "ten minutes a day" version, with the "wisdom… limit" sentence. The magazine was edited by Hubbard → stopped: not opened (HathiTrust returned 403, Google Books returned a CAPTCHA)

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Number changed | ten minutes a day (per Quote Investigator) | five minutes every day | *The Philistine*, January 1910, (not opened), per [Quote Investigator](https://quoteinvestigator.com/2026/11/20/fool-minutes/). With the "wisdom… limit" ending, first seen in an opened source in [*Roycroft Dictionary and Book of Epigrams*](https://archive.org/stream/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt), 1923 |
| Other: spelling changed | "dam fool" (per Quote Investigator) | damn fool | *The Issue*, 13 November 1909, (not opened), per [Quote Investigator](https://quoteinvestigator.com/2026/11/20/fool-minutes/) |

### Status of the root
- The root is a 1909 magazine aphorism, not a study, so retraction, correction and replication checks do not apply. The root issue was not opened: [HathiTrust](https://catalog.hathitrust.org/Record/000679447) returned 403, and Google Books returned a CAPTCHA.
- Quote Investigator names another candidate credit: a 1922 item in the *Kansas City Kansan* ("Sidelines" by A. E. Neal, not opened) gives the line to a local man, Abe Sturgess, as "10 per cent of the time." Quote Investigator still credits Hubbard.

### Cold trails
None.

### Confidence
Medium. I opened the 1923 Roycroft book, Hubbard's own press, and it has your wording almost exactly. But I could not open the 1909 and 1910 *Philistine* issues that start the chain, so their dates and wording rest on Quote Investigator.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
