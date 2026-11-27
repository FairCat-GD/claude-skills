---
case: obscure-claim-hubbard-fool
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:18:10Z
cost_usd: 1.3961
duration_s: 192
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
- WebSearch: "damn fool for at least five minutes every day"
- WebSearch: "wisdom consists in not exceeding the limit"
- WebSearch: Elbert Hubbard fool five minutes a day wisdom limit
- WebSearch: Quote Investigator "five minutes" fool every day wisdom exceeding limit
- WebSearch: origin "fool for five minutes every day" Hubbard earliest
- WebSearch: "Every man is a fool for at least five minutes every day" Hubbard source Philistine OR "Roycroft"
- WebFetch: https://quoteinvestigator.com/2026/11/20/fool-minutes/
- WebFetch (error): https://wist.info/hubbard-elbert-green/
- WebFetch: https://en.wikiquote.org/wiki/Elbert_Hubbard
- WebFetch: https://books.google.com/books?id=9YlHAAAAYAAJ&pg=PA192&#v=onepage&q=%22dam%20fool%22&f=false
- WebFetch: https://www.google.com/books/edition/The_Philistine/iv4-AAAAYAAJ?hl=en&gbpv=1&dq=%22dam+fool%22&pg=PA57&printsec=frontcover
- WebFetch: https://www.newspapers.com/article/vardamans-weekly-philistine/210580938/
- WebFetch: https://books.google.pl/books?id=9YlHAAAAYAAJ&pg=PA192&redir_esc=y
- WebFetch: https://books.google.com/books?id=iv4-AAAAYAAJ&newbks=0&printsec=frontcover&pg=PA57&dq=%22dam+fool%22&hl=en
- WebFetch: https://books.google.pl/books?id=iv4-AAAAYAAJ&newbks=0&printsec=frontcover&pg=PA57&dq=%22dam+fool%22&hl=en&redir_esc=y
- WebSearch: archive.org "Philistine" Hubbard 1909 volume 29 "dam fool"
- WebFetch: https://quoteinvestigator.com/2026/11/20/fool-minutes/
- WebFetch: https://wist.info/author/hubbard-elbert-green/
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28philistine%29+AND+year%3A%5B1909+TO+1910%5D&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=volume&fl%5B%5D=year&rows=50&output=json
- WebFetch: https://babel.hathitrust.org/cgi/ls?q1=%22dam%20fool%20at%20least%20ten%20minutes%22;anyall1=phrase;lmt=all
- WebSearch: "A Thousand & One Epigrams" Hubbard 1911 full text archive.org OR gutenberg
- WebSearch: Carnegie "How to Stop Worrying" "damn fool for at least five minutes every day" "Elbert Hubbard"
- WebFetch: https://www.sawanonlinebookstore.com/part-six-fool-things-i-have-done/
- WebFetch: https://www.azquotes.com/quote/531137
- WebFetch: https://grahamchastney.com/2013/11/15/every-man-is-a-damn-fool-for-at-least-five-minutes-every-day-wisdom-consists-of-not-exceeding-the-limit-elbert-hubbard/
- WebFetch: https://books.google.com/books?id=Tf80AAAAMAAJ&q=%22dam+fool%22

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Elbert Hubbard said: every man is a damn fool for at least five minutes every day; wisdom consists in not exceeding the limit."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** [*The Philistine*, Vol. 29, No. 6, p. 192](https://books.google.pl/books?id=9YlHAAAAYAAJ&pg=PA192&redir_esc=y), November 1909 (date from: cited by Quote Investigator). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 13

### Chain
Your version: "Elbert Hubbard said: every man is a damn fool for at least five minutes every day; wisdom consists in not exceeding the limit." (where you met it: not given)
 ├─ [AZQuotes](https://www.azquotes.com/quote/531137), date unknown, Tertiary → cites
 │   └─ *A Thousand & One Epigrams*, 1911, (not opened), per AZQuotes → stopped: not opened
 ├─ [Wikiquote, *Elbert Hubbard*](https://en.wikiquote.org/wiki/Elbert_Hubbard), date unknown, Tertiary → cites
 │   └─ *The Roycroft Dictionary and Book of Epigrams*, 1923, (not opened), per Wikiquote → stopped: not opened
 ├─ [Graham Chastney blog](https://grahamchastney.com/2013/11/15/every-man-is-a-damn-fool-for-at-least-five-minutes-every-day-wisdom-consists-of-not-exceeding-the-limit-elbert-hubbard/), 2013, Tertiary → cites Hubbard, naming no work → stopped: no work named
 ├─ Dale Carnegie, *How to Stop Worrying and Start Living*, ch. 22, 1948, Secondary, opened as a [reproduction of the chapter](https://www.sawanonlinebookstore.com/part-six-fool-things-i-have-done/), which reads "[Every man is a damn fool for at least five minutes every day.](https://www.sawanonlinebookstore.com/part-six-fool-things-i-have-done/)" → cites Hubbard, naming no work → stopped: no work named
 └─ [Quote Investigator](https://quoteinvestigator.com/2026/11/20/fool-minutes/), 2026, Secondary → cites
     ├─ *Reader's Digest Quotable Quotes*, 1997, (not opened), per Quote Investigator
     ├─ *The Fitzhenry & Whiteside Book of Quotations*, 1981, (not opened), per Quote Investigator
     ├─ *Centre Daily Times*, 1979, (not opened), per Quote Investigator
     ├─ *The Kansas City Kansan*, 1922, credits a local man (Abe Sturgess) with a "10 per cent of the time" variant, (not opened), per Quote Investigator
     ├─ [*The Philistine*, Vol. 30, No. 2, p. 57](https://books.google.pl/books?id=iv4-AAAAYAAJ&newbks=0&printsec=frontcover&pg=PA57&dq=%22dam+fool%22&hl=en&redir_esc=y), January 1910, Primary (not opened, per Quote Investigator): the page's text was not returned. Hubbard's "five minutes every day" version.
     └─ [*The Issue*](https://www.newspapers.com/article/vardamans-weekly-philistine/210580938/) (ed. James K. Vardaman), 13 Nov 1909, (not opened, per Quote Investigator): fetch returned 403. → cites
         └─ [*The Philistine*, Vol. 29, No. 6, p. 192](https://books.google.pl/books?id=9YlHAAAAYAAJ&pg=PA192&redir_esc=y), November 1909, Primary (not opened, per Quote Investigator): the page's text was not returned. An uncredited filler item in Hubbard's magazine, saying "ten minutes".

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Number changed | ten minutes a day (per Quote Investigator) | five minutes every day | *The Philistine*, January 1910 (Hubbard's own revision, per Quote Investigator) |
| Other: spelling | "dam fool" (per Quote Investigator) | damn fool | *The Issue*, 13 Nov 1909 (per Quote Investigator) |
| Other: two versions merged | The short 1909 form had "ten minutes". The 1910 "five minutes" form added a passage about days of insight in a month (per Quote Investigator). | the short form with "five minutes" | Carnegie, 1948 (with "that limit"); "the limit" with a semicolon in Fitzhenry & Whiteside, 1981 (both per Quote Investigator) |
| Other: framing added | Uncredited aphorism in a list | "Elbert Hubbard said:" | Carnegie, 1948 (opened via the [reproduced chapter](https://www.sawanonlinebookstore.com/part-six-fool-things-i-have-done/)) |

### Status of the root
- The root is a 1909 magazine item, not a study. Retraction and correction databases do not apply, and none were checked. [Quote Investigator](https://quoteinvestigator.com/2026/11/20/fool-minutes/) concludes: "Elbert Hubbard deserves credit for this saying."
- The Kansas City Kansan, 1922 (per Quote Investigator): credited a "10 per cent of the time" variant to a local man, 13 years after *The Philistine* printed it.

### Cold trails
None.

### Confidence
Medium: I could not open either *Philistine* page or the Vardaman reprint, so the root's wording and dates come from Quote Investigator (*cited by*), while the Carnegie "Elbert Hubbard said" framing was confirmed in an opened text.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
