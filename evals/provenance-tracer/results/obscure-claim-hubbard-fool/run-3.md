---
case: obscure-claim-hubbard-fool
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:41:42Z
cost_usd: 1.4383
duration_s: 143
turns: 28
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- Read: <plugin>/skills/provenance-tracer/references/labels.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- WebSearch: "damn fool for at least five minutes every day"
- WebSearch: "wisdom consists in not exceeding the limit"
- WebSearch: Elbert Hubbard every man is a fool five minutes a day wisdom quote source
- WebSearch: quote investigator "five minutes every day" fool wisdom limit
- WebSearch: origin "fool for five minutes" "not exceeding the limit" earliest
- WebSearch: wikiquote Elbert Hubbard "damn fool"
- WebFetch: https://quoteinvestigator.com/2026/11/20/fool-minutes/
- WebFetch: https://wist.info/author/hubbard-elbert-green/
- WebFetch: https://en.wikiquote.org/wiki/Elbert_Hubbard
- WebSearch: "dam fool at least ten minutes a day" Philistine
- WebSearch: "dam fool for at least five minutes every day" Philistine archive.org
- WebFetch: https://books.google.com/books?id=9YlHAAAAYAAJ&pg=PA192
- WebFetch: https://books.google.pl/books?id=9YlHAAAAYAAJ&pg=PA192&redir_esc=y
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28philistine%29+AND+creator%3A%28hubbard%29&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=volume&fl%5B%5D=date&rows=100&output=json
- WebSearch: "Thousand and One Epigrams" Hubbard "dam fool" "ten minutes" OR "five minutes" archive.org OR gutenberg
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28thousand+one+epigrams%29&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=date&rows=20&output=json
- WebSearch: "Philosophy of Elbert Hubbard" "dam fool" OR "damn fool" "minutes every day" gutenberg OR wikisource OR archive.org
- WebFetch: https://www.google.com/books/edition/The_Philistine/iv4-AAAAYAAJ?hl=en&gbpv=1&dq=%22dam+fool%22&pg=PA57&printsec=frontcover
- WebFetch: https://books.google.com/books?id=iv4-AAAAYAAJ&newbks=0&printsec=frontcover&pg=PA57&dq=%22dam+fool%22&hl=en
- WebFetch: https://wist.info/hubbard-elbert-green/1975/

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Elbert Hubbard said that every man is a damn fool for at least five minutes every day, and that wisdom consists in not exceeding the limit."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** *The Philistine*, Vol. 29, No. 6, p. 192, November 1909 (date from: cited by [Quote Investigator](https://quoteinvestigator.com/2026/11/20/fool-minutes/) and [WIST](https://wist.info/hubbard-elbert-green/1975/)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 12

### Chain
Your version: "Elbert Hubbard said: every man is a damn fool for at least five minutes every day; wisdom consists in not exceeding the limit" (where you met it: not given)
 ├─ [Quote Investigator, *Quote Origin: Everyone Is a Damn Fool at Least Ten Minutes a Day…*](https://quoteinvestigator.com/2026/11/20/fool-minutes/), 2026, Secondary → cites
 │   ├─ *Reader's Digest Quotable Quotes*, 1997, (not opened), per Quote Investigator → stopped: not opened
 │   ├─ *The Fitzhenry & Whiteside Book of Quotations*, 1981, (not opened), per Quote Investigator → stopped: not opened
 │   ├─ Dale Carnegie, *How to Stop Worrying and Start Living*, 1948, (not opened), per Quote Investigator → stopped: not opened
 │   ├─ *The Kansas City Kansan*, A. E. Neal's *Sidelines* column, 1922, (not opened), per Quote Investigator → stopped: not opened
 │   ├─ Elbert Hubbard, *Commonsense and Life-Insurance*, *The Fra*, Vol. 4, No. 6, March 1910, Primary (not opened, per Quote Investigator) → stopped: not opened
 │   ├─ [Elbert Hubbard, untitled article, *The Philistine*, Vol. 30, No. 2, p. 57](https://www.google.com/books/edition/The_Philistine/iv4-AAAAYAAJ?hl=en&gbpv=1&dq=%22dam+fool%22&pg=PA57&printsec=frontcover), January 1910, Primary (not opened, per Quote Investigator) → stopped: not opened
 │   ├─ James K. Vardaman's weekly *The Issue*, p. 5, 13 November 1909, (not opened), per Quote Investigator → cites
 │   │   └─ *The Philistine*, November 1909 (root, below)
 │   └─ [*The Philistine*, Vol. 29, No. 6, p. 192, filler item](https://books.google.pl/books?id=9YlHAAAAYAAJ&pg=PA192&redir_esc=y), November 1909, Primary (not opened, per Quote Investigator), root
 ├─ [WIST, *Quotations from Hubbard, Elbert*](https://wist.info/hubbard-elbert-green/1975/), 2004, Secondary → cites
 │   └─ *The Philistine*, November 1909 (root, above)
 └─ [Wikiquote, *Elbert Hubbard*](https://en.wikiquote.org/wiki/Elbert_Hubbard), date unknown, Tertiary → cites
     └─ *The Roycroft Dictionary and Book of Epigrams*, 1923, (not opened), per Wikiquote → stopped: not opened

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Number changed | every man is a fool *ten minutes* a day (per Quote Investigator) | every man is a damn fool for at least five minutes every day | Hubbard's *The Philistine*, January 1910 (not opened) |
| Other: spelling | the root spells it *dam* | damn | Vardaman's *The Issue*, 13 November 1909 (not opened) |

### Status of the root
- No primary found, so there was no status to check. The Google Books scan I fetched for November 1909 opened as volumes 28–29 and showed no page text. The January 1910 scan redirected and was not read, and an Internet Archive catalogue search found no copy of volumes 29 or 30.
- WIST says the November 1909 line ran without a byline in a list of aphorisms in *The Philistine*, and that Hubbard was the magazine's editor and a presumed contributor.
- Quote Investigator says Hubbard published three versions of the saying (ten minutes, five minutes, half an hour) and concludes that ["Elbert Hubbard deserves credit for this saying."](https://quoteinvestigator.com/2026/11/20/fool-minutes/)
- Quote Investigator: Hubbard's January 1910 version uses *five minutes every day*. In that version the sentence goes on about three days a month of insight and great love, and it does not include the *not exceeding the limit* clause.
- Quote Investigator: the wording you have, word for word, is the one it cites from the 1981 Fitzhenry & Whiteside collection. Carnegie's 1948 version ends *that limit*.

### Cold trails
None.

### Confidence
Medium: the chain back to Hubbard rests on two opened secondary sources that agree (Quote Investigator and WIST), but no copy of the 1909 or 1910 *Philistine* page was opened, and its date rests on *cited by*.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
