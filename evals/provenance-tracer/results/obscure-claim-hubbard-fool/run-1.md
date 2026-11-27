---
case: obscure-claim-hubbard-fool
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T15:42:49Z
cost_usd: 1.3567
duration_s: 170
turns: 30
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
- WebSearch: "wisdom consists in not exceeding the limit" Hubbard
- WebSearch: Elbert Hubbard damn fool five minutes a day Philistine Roycroft
- WebSearch: "damn fool for at least five minutes" quote investigator
- WebSearch: origin "wisdom consists in not exceeding the limit"
- WebSearch: Elbert Hubbard "five minutes every day" fool wikiquote
- WebFetch: https://quoteinvestigator.com/2026/11/20/fool-minutes/
- WebFetch: https://wist.info/hubbard-elbert-green/
- WebFetch: https://books.google.com/books?id=9YlHAAAAYAAJ&pg=PA192
- WebSearch: archive.org "The Philistine" volume 29 1909 Hubbard
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28philistine%29+AND+year%3A1909&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=volume&rows=50&output=json
- WebFetch: https://books.google.pl/books?id=9YlHAAAAYAAJ&pg=PA192&redir_esc=y
- WebFetch: https://archive.org/advancedsearch.php?q=identifier%3Aphilistine*&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=volume&fl%5B%5D=date&rows=100&output=json
- WebFetch: https://archive.org/advancedsearch.php?q=%22dam+fool+at+least+ten+minutes%22&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=date&rows=50&output=json
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28thousand+one+epigrams%29+AND+creator%3AHubbard&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=date&rows=20&output=json
- WebSearch: gutenberg OR archive.org Hubbard "Thousand and One Epigrams" OR "Roycroft Dictionary" full text
- WebFetch: https://archive.org/stream/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt
- WebFetch: https://www.gutenberg.org/files/36566/36566-h/36566-h.htm
- WebFetch: https://archive.org/stream/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt
- WebFetch: https://archive.org/stream/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt
- WebFetch: https://books.google.pl/books?id=9YlHAAAAYAAJ&q=%22dam+fool%22&redir_esc=y
- WebFetch: https://babel.hathitrust.org/cgi/ls?q1=%22dam+fool+at+least+ten+minutes%22&anyall1=phrase&lmt=ft

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Elbert Hubbard said every man is a damn fool for at least five minutes every day, and wisdom consists in not exceeding the limit."

**Roots:** Echo · **Grounding:** Grounded · Mutated
**Earliest instance found:** [*The Philistine*, vol. 29, no. 6, p. 192](https://books.google.com/books?id=9YlHAAAAYAAJ&pg=PA192), November 1909 (date from: cited by Quote Investigator and WIST). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 7

### Chain
Your version: "Elbert Hubbard said: every man is a damn fool for at least five minutes every day; wisdom consists in not exceeding the limit" (where you met it: not given)
 ├─ [Quote Investigator, *Quote Origin: Everyone Is a Damn Fool at Least Ten Minutes a Day*](https://quoteinvestigator.com/2026/11/20/fool-minutes/), 2026, Secondary → cites
 │   ├─ *The Fitzhenry & Whiteside Book of Quotations*, p. 304, 1981, Tertiary, (not opened), per Quote Investigator. Its wording is the closest to yours: the same sentence, credited to Hubbard → cites
 │   │   └─ Dale Carnegie, *How to Stop Worrying and Start Living*, p. 175, 1948, Tertiary, (not opened), per Quote Investigator. Credits Hubbard, with the *five minutes* wording → stopped: not opened
 │   ├─ *The Philistine*, vol. 30, no. 2, p. 57, January 1910, Primary (not opened, per Quote Investigator). The first *five minutes* wording, with a different ending → stopped: not opened
 │   └─ [*The Philistine*, vol. 29, no. 6, p. 192](https://books.google.com/books?id=9YlHAAAAYAAJ&pg=PA192), November 1909, Primary (not opened, per Quote Investigator), root
 ├─ [WIST, *Quotations from Hubbard, Elbert*](https://wist.info/hubbard-elbert-green/), 2004 (entry date on the page), Secondary → cites *The Philistine*, November 1909 (the root above)
 └─ [Elbert Hubbard, *Roycroft Dictionary and Book of Epigrams*, The Roycrofters](https://archive.org/stream/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt), 1923, Primary. It states the saying almost word for word as you have it, and cites no earlier printing.

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Number changed | every man is a fool at least *ten* minutes a day (from Quote Investigator's and WIST's transcriptions) | Elbert Hubbard said: every man is a damn fool for at least five minutes every day | *The Philistine*, vol. 30, no. 2, January 1910 (not opened, per [Quote Investigator](https://quoteinvestigator.com/2026/11/20/fool-minutes/)) |
| Other: spelling changed | the root spells the word *dam* | damn fool | [*Roycroft Dictionary and Book of Epigrams*](https://archive.org/stream/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt), 1923 (the earliest opened node with *damn*) |

### Status of the root
- No retraction or correction check applies to an aphorism in a 1909 magazine, so none was run. Every attempt to open the November 1909 issue failed: Google Books redirected to an unrelated volume, its search hit a bot wall, HathiTrust returned 403, and Internet Archive had no copy.
- [WIST](https://wist.info/hubbard-elbert-green/) cites the November 1909 *Philistine* and gives the full ten-minutes form, including the line about not exceeding the limit.
- [Quote Investigator](https://quoteinvestigator.com/2026/11/20/fool-minutes/) lists other early printings:
  - James K. Vardaman's Mississippi paper *The Issue* reprinted the saying on 13 November 1909, credited to *The Philistine*.
  - A 1922 Kansas newspaper item credited it to a local man, Abe Sturgess.
  - In *The Fra* of March 1910, Hubbard gave a *half an hour* version.
- Quote Investigator's conclusion: "Elbert Hubbard deserves credit for this saying."

### Cold trails
- [*Roycroft Dictionary and Book of Epigrams*](https://archive.org/stream/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt), 1923: states the saying in the five-minutes form and cites no earlier printing.

### Confidence
Medium: the 1909 root and the 1910 variant could not be opened, so their wording and dates rest on Quote Investigator and WIST. The 1923 Hubbard text with the five-minutes wording was opened.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
