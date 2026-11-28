---
case: obscure-claim-hubbard-fool
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:37:21Z
cost_usd: 1.5629
duration_s: 223
turns: 34
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
- WebSearch: Elbert Hubbard fool five minutes a day wisdom limit source
- WebSearch: quote investigator "five minutes every day" fool wisdom limit
- WebSearch: origin "every man is a damn fool for at least five minutes"
- WebSearch: wikiquote Elbert Hubbard "five minutes every day"
- WebFetch: https://quoteinvestigator.com/2026/11/20/fool-minutes/
- WebFetch: https://wist.info/author/hubbard-elbert-green/
- WebFetch: https://books.google.com/books?id=9YlHAAAAYAAJ&pg=PA192&#v=onepage&q=%22dam%20fool%22&f=false
- WebSearch: "dam fool at least ten minutes a day" Philistine archive.org
- WebFetch: https://books.google.pl/books?id=9YlHAAAAYAAJ&pg=PA192&redir_esc=y
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28philistine+periodical+of+protest%29&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=volume&fl%5B%5D=year&rows=100&output=json
- WebFetch: https://archive.org/metadata/sim_philistine-a-periodical-of-protest_1909-11_29_6
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28philistine+periodical+of+protest%29+AND+year%3A%5B1909+TO+1911%5D&fl%5B%5D=identifier&fl%5B%5D=title&rows=50&output=json
- WebSearch: "A Thousand & One Epigrams" Hubbard "dam fool" OR "damn fool" archive.org OR gutenberg
- WebFetch: https://www.google.com/books/edition/The_Philistine/iv4-AAAAYAAJ?hl=en&gbpv=1&dq=%22dam+fool%22&pg=PA57&printsec=frontcover
- WebFetch: https://www.azquotes.com/quote/531137
- WebFetch: https://www.goodreads.com/quotes/80344-every-man-is-a-damn-fool-for-at-least-five
- WebSearch: archive.org "Thousand and one epigrams" Hubbard 1911
- WebFetch: https://books.google.com/books?id=iv4-AAAAYAAJ&newbks=0&printsec=frontcover&pg=PA57&dq=%22dam+fool%22&hl=en
- WebFetch: https://archive.org/advancedsearch.php?q=hubbard+AND+%28epigrams+OR+philistine%29+AND+mediatype%3Atexts&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=year&fl%5B%5D=volume&rows=60&output=json
- WebFetch: https://books.google.pl/books?id=iv4-AAAAYAAJ&newbks=0&printsec=frontcover&pg=PA57&dq=%22dam+fool%22&hl=en&redir_esc=y
- WebFetch: https://archive.org/metadata/roycroftdictiona00hubb
- WebFetch: https://ia800600.us.archive.org/0/items/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt
- WebFetch: https://ia800600.us.archive.org/0/items/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt
- WebFetch: https://ia800600.us.archive.org/0/items/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Elbert Hubbard said every man is a damn fool for at least five minutes every day, and that wisdom consists in not exceeding the limit."

**Roots:** Echo · **Grounding:** Grounded · Mutated
**Earliest instance found:** [*The Philistine*, Vol. 29, No. 6, p. 192](https://books.google.pl/books?id=9YlHAAAAYAAJ&pg=PA192&redir_esc=y), November 1909 (date from: cited by Quote Investigator). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 10

### Chain
Your version: "Elbert Hubbard said: every man is a damn fool for at least five minutes every day; wisdom consists in not exceeding the limit" (where you met it: not given)
 ├─ [AZQuotes](https://www.azquotes.com/quote/531137), date unknown, Secondary → cites
 │   └─ *A Thousand & One Epigrams* (Hubbard, Roycrofters), 1911, Primary (not opened, per AZQuotes) → stopped: not opened
 ├─ [Goodreads](https://www.goodreads.com/quotes/80344-every-man-is-a-damn-fool-for-at-least-five), date unknown, Secondary → cites
 │   └─ *The Roycroft Dictionary* (Hubbard), 1914, (not opened), per Goodreads; a later edition is →
 │       └─ [*The Roycroft Dictionary and Book of Epigrams*](https://ia800600.us.archive.org/0/items/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt), 1923, Primary (Hubbard's own collection; the line as you typed it, p. 129, with a full stop for the semicolon)
 ├─ [WIST Quotations](https://wist.info/author/hubbard-elbert-green/), 2004 (entry date on page), Secondary → cites *The Philistine*, Nov 1909 (root, below)
 └─ [Quote Investigator](https://quoteinvestigator.com/2026/11/20/fool-minutes/), 2026, Secondary → cites
     ├─ [*The Philistine*, Vol. 30, No. 2, p. 57](https://books.google.pl/books?id=iv4-AAAAYAAJ&newbks=0&printsec=frontcover&pg=PA57&dq=%22dam+fool%22&hl=en&redir_esc=y), January 1910, Primary (not opened, per Quote Investigator): Hubbard's *five minutes* variant, with a different second half
     ├─ *The Issue* (ed. James K. Vardaman), Jackson, Miss., 13 Nov 1909, (not opened), per Quote Investigator → cites *The Philistine*
     └─ [*The Philistine*, Vol. 29, No. 6, p. 192](https://books.google.pl/books?id=9YlHAAAAYAAJ&pg=PA192&redir_esc=y), November 1909, Primary (not opened, per Quote Investigator), root

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Number changed | every man is a fool at least *ten* minutes a day | Elbert Hubbard said: every man is a damn fool for at least five minutes every day | [*The Philistine*, Vol. 30, No. 2](https://books.google.pl/books?id=iv4-AAAAYAAJ&newbks=0&printsec=frontcover&pg=PA57&dq=%22dam+fool%22&hl=en&redir_esc=y), 1910 |
| Spelling changed (*dam* became *damn*) | every man is a *dam* fool | every man is a damn fool | *The Issue*, 1909 (not opened) |

### Status of the root
- Quote Investigator looked at Hubbard, James K. Vardaman and Abe Sturgess as possible sources and concluded that "Elbert Hubbard deserves credit for this saying." ([Quote Investigator](https://quoteinvestigator.com/2026/11/20/fool-minutes/))
- WIST notes that the November 1909 *Philistine* printed the line unsigned among filler aphorisms, in a magazine that Hubbard edited. ([WIST Quotations](https://wist.info/author/hubbard-elbert-green/))
- The root is a magazine aphorism, not a study. No retraction, correction or replication checks apply.
- I could not open the text of either *Philistine* issue. Both Google Books copies returned only metadata, and the Internet Archive had no scan of the 1909–1910 volumes.

### Cold trails
None.

### Confidence
Medium. The 1909 root and the 1910 *five minutes* revision are known only from Quote Investigator's citations, which I could not open myself. Hubbard's own 1923 collection does print your exact wording, and I opened it.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
