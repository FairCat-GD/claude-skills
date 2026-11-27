---
case: obscure-claim-hubbard-fool
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T15:44:45Z
cost_usd: 1.6032
duration_s: 160
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
- WebSearch: "damn fool for at least five minutes every day" Hubbard
- WebSearch: "wisdom consists in not exceeding the limit"
- WebSearch: Elbert Hubbard fool five minutes a day wisdom quote source
- WebSearch: who first said "every man is a damn fool for at least five minutes"
- WebSearch: quoteinvestigator fool five minutes every day wisdom not exceeding limit
- WebSearch: "five minutes every day" "exceeding the limit" Hubbard Philistine OR "Thousand and One Epigrams"
- WebFetch: https://quoteinvestigator.com/2026/11/20/fool-minutes/
- WebFetch: https://wist.info/author/hubbard-elbert-green/
- WebFetch: https://www.azquotes.com/quote/531137
- WebFetch: https://www.goodreads.com/quotes/80344-every-man-is-a-damn-fool-for-at-least-five
- WebSearch: archive.org "The Philistine" volume 29 1909 Hubbard
- WebSearch: "A Thousand and One Epigrams" Hubbard full text gutenberg OR archive.org
- WebSearch: "Roycroft Dictionary" Hubbard 1914 full text archive.org
- WebFetch: https://www.gutenberg.org/cache/epub/36566/pg36566.txt
- WebFetch: https://www.google.com/books/edition/_/MUsLAQAAIAAJ?gbpv=1&bsq=%22dam%20fool%22
- WebFetch: https://books.google.com/books?id=MUsLAQAAIAAJ&newbks=0&printsec=frontcover&q=%22dam+fool%22
- WebFetch: https://archive.org/advancedsearch.php?q=title%3Aphilistine+AND+year%3A1909&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=volume&fl%5B%5D=year&rows=50&output=json
- WebFetch: https://archive.org/stream/roycroftdiction00hubbgoog/roycroftdiction00hubbgoog_djvu.txt
- WebFetch: https://archive.org/stream/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt
- WebFetch: https://archive.org/stream/roycroftdiction00hubbgoog/roycroftdiction00hubbgoog_djvu.txt
- WebFetch: https://archive.org/stream/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt
- WebFetch: https://archive.org/stream/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt
- WebSearch: hathitrust "Thousand & one epigrams" Hubbard 1911 full view babel
- WebFetch: https://babel.hathitrust.org/cgi/pt/search?q1=minutes&id=mdp.39015010943275
- WebFetch: https://en.wikiquote.org/wiki/Elbert_Hubbard
- WebFetch: https://www.googleapis.com/books/v1/volumes?q=%22dam+fool+at+least+ten+minutes%22
- WebFetch: https://www.googleapis.com/books/v1/volumes?q=%22dam+fool+for+at+least+five+minutes%22
- WebFetch: https://archive.org/advancedsearch.php?q=identifier%3Aphilistineaperi*&fl%5B%5D=identifier&fl%5B%5D=volume&fl%5B%5D=date&rows=100&output=json

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Elbert Hubbard said every man is a damn fool for at least five minutes every day; wisdom consists in not exceeding the limit."

**Roots:** Echo · **Grounding:** Grounded · Mutated
**Earliest instance found:** [*The Philistine*, Vol. 29, No. 6, p. 192](https://www.google.com/books/edition/_/MUsLAQAAIAAJ?gbpv=1&bsq=%22dam%20fool%22), November 1909 (date from: cited by Quote Investigator). It was unsigned filler in Hubbard's own magazine and used *ten minutes*. Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 12

### Chain
Your version: "Elbert Hubbard said: every man is a damn fool for at least five minutes every day; wisdom consists in not exceeding the limit" (where you met it: not given)
 ├─ [Quote Investigator, *Quote Origin: Everyone Is a Damn Fool at Least Ten Minutes a Day…*](https://quoteinvestigator.com/2026/11/20/fool-minutes/), 2026, Secondary → cites
 │   ├─ *The Fitzhenry & Whiteside Book of Quotations*, p. 304, 1981, (not opened), per Quote Investigator. It credits Hubbard with your wording, semicolon included → cites
 │   │   └─ Dale Carnegie, *How to Stop Worrying and Start Living*, ch. 22, 1948, (not opened), per Quote Investigator. It has *five minutes* and *that limit* → stopped: not opened
 │   ├─ *The Philistine*, Vol. 30, No. 2, p. 57, January 1910, Primary (not opened, per Quote Investigator). Hubbard's first *five minutes* version, with a different second half → stopped: not opened
 │   ├─ *The Issue* (ed. James K. Vardaman), Jackson, Miss., 13 Nov 1909, (not opened), per Quote Investigator. Reprints it as *damn*, credited to *The Philistine* → cites
 │   │   └─ points to the root below
 │   └─ [*The Philistine*, Vol. 29, No. 6, p. 192](https://www.google.com/books/edition/_/MUsLAQAAIAAJ?gbpv=1&bsq=%22dam%20fool%22), November 1909, Primary (not opened, per Quote Investigator), root
 ├─ [Wist.info, Hubbard entry](https://wist.info/author/hubbard-elbert-green/), 2004 (date from: byline, entry added Feb 2004), Secondary → cites
 │   └─ *The Philistine*, Vol. 29, No. 6, Nov 1909: the root above
 ├─ [Wikiquote, *Elbert Hubbard*](https://en.wikiquote.org/wiki/Elbert_Hubbard), date unknown, Secondary → cites
 │   └─ [*Roycroft Dictionary and Book of Epigrams*](https://archive.org/stream/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt), 1923 (date from: byline, title page), Primary. This posthumous Hubbard collection has the five-minute line and the *wisdom* line together, with a full stop between them, near p. 129. It cites nothing.
 ├─ [AZQuotes](https://www.azquotes.com/quote/531137), date unknown, Tertiary → cites
 │   └─ [*A Thousand & One Epigrams*](https://babel.hathitrust.org/cgi/pt/search?q1=minutes&id=mdp.39015010943275), 1911, Primary (not opened, per AZQuotes) → stopped: not opened (HathiTrust returned 403)
 └─ [Goodreads](https://www.goodreads.com/quotes/80344-every-man-is-a-damn-fool-for-at-least-five), date unknown, Tertiary → credits *The Roycroft Dictionary* (1914)
     └─ [*The Roycroft Dictionary Concocted by Ali Baba and the Bunch on Rainy Days*](https://archive.org/stream/roycroftdiction00hubbgoog/roycroftdiction00hubbgoog_djvu.txt), 1914, Primary (credited, differs). I read the whole text and the line was not in it.

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Number changed | [“Every man is a dam fool at least ten minutes a day.”](https://quoteinvestigator.com/2026/11/20/fool-minutes/) (the 1909 text, as Quote Investigator gives it) | five minutes every day | *The Philistine*, Vol. 30, No. 2, January 1910 (not opened, per [Quote Investigator](https://quoteinvestigator.com/2026/11/20/fool-minutes/)) |
| Other: spelling, *dam* became *damn* | the 1909 filler spells it *dam* | damn fool | *The Issue*, 13 Nov 1909 (not opened, per [Quote Investigator](https://quoteinvestigator.com/2026/11/20/fool-minutes/)) |

### Status of the root
- The root is an unsigned aphorism in a magazine, not a study, so retraction, correction and replication checks don't apply.
- Quote Investigator concludes that the saying should be credited to Elbert Hubbard. It printed in his own *Philistine*, and he reworked it in January and March 1910. Quote Investigator also lists a 1922 *Kansas City Kansan* column crediting a local man, Abe Sturgess, with a *10 per cent of the time* version. That column came 13 years after *The Philistine*.
- *The Philistine* Vol. 29 could not be opened: Google Books returned a captcha and no Internet Archive copy of the volume was found. The 1911 *A Thousand & One Epigrams* could not be opened either (HathiTrust returned 403).

### Cold trails
- [*Roycroft Dictionary and Book of Epigrams*](https://archive.org/stream/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt), 1923: states the five-minute version and cites nothing. It is a later printing of the root's author.

### Confidence
Medium: the 1909 root and the 1910 five-minute revision are known only through Quote Investigator's citations, though the 1923 Hubbard collection was opened and has the line as you know it.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
