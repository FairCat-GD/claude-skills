---
case: obscure-claim-hubbard-fool
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T15:42:51Z
cost_usd: 1.3580
duration_s: 201
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
- WebSearch: Elbert Hubbard "five minutes every day" fool wisdom source
- WebSearch: origin of "every man is a damn fool for at least five minutes"
- WebSearch: quoteinvestigator fool five minutes every day wisdom not exceeding the limit
- WebSearch: Hubbard "five minutes every day" wikiquote Thousand and One Epigrams
- WebFetch: https://quoteinvestigator.com/2026/11/20/fool-minutes/
- WebFetch: https://wist.info/author/hubbard-elbert-green/
- WebFetch: https://books.google.com/books?id=9YlHAAAAYAAJ&pg=PA192&#v=onepage&q=%22dam%20fool%22&f=false
- WebFetch: https://www.google.com/books/edition/The_Philistine/iv4-AAAAYAAJ?hl=en&gbpv=1&dq=%22dam+fool%22&pg=PA57&printsec=frontcover
- WebSearch: archive.org "Thousand & One Epigrams" Hubbard 1911
- WebFetch: https://books.google.pl/books?id=9YlHAAAAYAAJ&pg=PA192&redir_esc=y
- WebFetch: https://books.google.com/books?id=iv4-AAAAYAAJ&newbks=0&printsec=frontcover&pg=PA57&dq=%22dam+fool%22&hl=en
- WebFetch: https://catalog.hathitrust.org/Record/000780271
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28philistine%29+AND+date%3A%5B1909-01-01+TO+1910-12-31%5D&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=volume&fl%5B%5D=date&rows=50&output=json
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28thousand+one+epigrams%29&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=date&rows=20&output=json
- WebFetch: https://archive.org/advancedsearch.php?q=philistine+periodical+of+protest&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=volume&fl%5B%5D=date&rows=60&output=json
- WebFetch: https://archive.org/advancedsearch.php?q=creator%3A%28hubbard+elbert%29+AND+title%3A%28epigrams%29&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=date&rows=20&output=json
- WebFetch: https://archive.org/download/sim_philistine-a-periodical-of-protest_1909-11_29_6/sim_philistine-a-periodical-of-protest_1909-11_29_6_djvu.txt
- WebFetch: https://archive.org/download/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt
- WebFetch: https://ia600600.us.archive.org/0/items/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt
- WebFetch: https://books.google.pl/books?id=iv4-AAAAYAAJ&newbks=0&printsec=frontcover&pg=PA57&dq=%22dam+fool%22&hl=en&redir_esc=y
- WebFetch: https://ia600600.us.archive.org/0/items/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt
- WebFetch: https://archive.org/download/sim_philistine-a-periodical-of-protest_1909-11_29_6/sim_philistine-a-periodical-of-protest_1909-11_29_6_djvu.txt
- WebFetch: https://ia600600.us.archive.org/0/items/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt
- WebFetch: https://books.google.pl/books?id=9YlHAAAAYAAJ&q=%22dam+fool%22&redir_esc=y
- WebFetch: https://archive.org/metadata/sim_philistine-a-periodical-of-protest_1909-11_29_6
- WebFetch: https://archive.org/advancedsearch.php?q=identifier%3Asim_philistine-a-periodical-of-protest_19*&fl%5B%5D=identifier&fl%5B%5D=date&rows=200&sort%5B%5D=date+desc&output=json

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Elbert Hubbard said every man is a damn fool for at least five minutes every day, and wisdom consists in not exceeding the limit."

**Roots:** Echo · **Grounding:** Grounded · Mutated
**Earliest instance found:** *The Philistine*, vol. 29 no. 6, p. 192, November 1909 (date from: cited by [Quote Investigator](https://quoteinvestigator.com/2026/11/20/fool-minutes/)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 9

### Chain
Your version: "Elbert Hubbard said: every man is a damn fool for at least five minutes every day; wisdom consists in not exceeding the limit" (where you met it: not given)
 ├─ [Quote Investigator, *Quote Origin: Everyone Is a Damn Fool at Least Ten Minutes a Day…*](https://quoteinvestigator.com/2026/11/20/fool-minutes/), 2026, Secondary → cites
 │   ├─ [*The Philistine*, vol. 29 no. 6, p. 192](https://books.google.pl/books?id=9YlHAAAAYAAJ&pg=PA192&redir_esc=y), Nov 1909, Primary (not opened, per Quote Investigator), root
 │   ├─ *The Issue*, ed. James K. Vardaman, Jackson, Mississippi, 13 Nov 1909, (not opened), per Quote Investigator → cites *The Philistine*, Nov 1909 (root, above)
 │   ├─ [*The Philistine*, vol. 30 no. 2, p. 57](https://books.google.pl/books?id=iv4-AAAAYAAJ&newbks=0&printsec=frontcover&pg=PA57&dq=%22dam+fool%22&hl=en&redir_esc=y), Jan 1910, Primary (not opened, per Quote Investigator) → stopped: not opened
 │   ├─ *The Kansas City Kansan*, Sidelines column by A. E. Neal, 16 Nov 1922, (not opened), per Quote Investigator → credits Abe Sturgess, a local man → stopped: not opened
 │   ├─ Dale Carnegie, *How to Stop Worrying and Start Living*, 1948, (not opened), per Quote Investigator → stopped: not opened
 │   └─ *The Fitzhenry & Whiteside Book of Quotations*, 1981, (not opened), per Quote Investigator → stopped: not opened
 ├─ [WIST, *Quotations from Hubbard, Elbert*](https://wist.info/author/hubbard-elbert-green/), 2004, Secondary → cites *The Philistine*, Nov 1909 (root, above)
 └─ [Elbert Hubbard, *The Roycroft Dictionary and Book of Epigrams*, Roycrofters](https://ia600600.us.archive.org/0/items/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt), 1923, Primary (Hubbard's collected text, published after his death in 1915; cites nothing)

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Number changed | every man is a fool at least *ten* minutes a day; wisdom lies in not exceeding the limit | every man is a damn fool for at least five minutes every day | *The Philistine*, vol. 30 no. 2, Jan 1910 (not opened, per Quote Investigator) |
| Other: spelling changed | the expletive is spelled *dam* | damn | *The Issue*, 13 Nov 1909 (not opened, per Quote Investigator) |

### Status of the root
- No retraction, correction or replication checks apply. The root is a magazine aphorism, not a study, so none were run.
- Quote Investigator's verdict on authorship: "Elbert Hubbard deserves credit for this saying." It says Hubbard published three versions. The first is the 1909 *ten minutes* line. The second, in Jan 1910, uses *five minutes* and has a different second half about days of insight and love. The third, in *The Fra* in March 1910, says even the best men go *locoed* for half an hour a day.
- [WIST](https://wist.info/author/hubbard-elbert-green/) also gives *The Philistine*, Nov 1909, as the source of the ten-minute version. It lists the five-minute form as a variant.
- [*The Roycroft Dictionary and Book of Epigrams*](https://ia600600.us.archive.org/0/items/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt) (1923), opened, prints your version's two sentences: *five minutes every day* followed by *not exceeding the limit*. Quote Investigator's timeline does not list this book. In this trace it is the earliest opened source that pairs *five minutes* with the *limit* sentence.

### Cold trails
- [*The Roycroft Dictionary and Book of Epigrams*](https://ia600600.us.archive.org/0/items/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt), 1923: states the claim and cites nothing. It is Hubbard's own collected text, from the same origin as the root, not a separate one.

### Confidence
Medium: Google Books returned no page text for the 1909 or 1910 *Philistine* issues, and archive.org has no issues after 1906, so the root's wording and date rest on Quote Investigator's citation, although the 1923 Hubbard collection was opened and states your version.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
