---
case: obscure-claim-hubbard-fool
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:41:04Z
cost_usd: 1.7281
duration_s: 237
turns: 40
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
- WebSearch: who first said "five minutes every day" fool wisdom "not exceeding the limit"
- WebSearch: quoteinvestigator fool five minutes every day wisdom limit Hubbard
- WebSearch: "every man is a fool" "five minutes" "exceeding the limit" Hubbard Philistine OR Note Book OR Epigrams
- WebFetch: https://quoteinvestigator.com/2026/11/20/fool-minutes/
- WebFetch: https://wist.info/author/hubbard-elbert-green/
- WebFetch: https://books.google.com/books?id=9YlHAAAAYAAJ&pg=PA192&#v=onepage&q=%22dam%20fool%22&f=false
- WebSearch: "dam fool at least ten minutes a day" Philistine archive.org
- WebSearch: "A Thousand and One Epigrams" Hubbard archive.org "fool"
- WebFetch: https://books.google.pl/books?id=9YlHAAAAYAAJ&pg=PA192&redir_esc=y
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28philistine%29+AND+creator%3A%28hubbard%29&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=volume&fl%5B%5D=year&rows=50&output=json
- WebFetch: https://archive.org/metadata/philistinevolum00nygoog
- WebFetch: https://archive.org/metadata/philistineaperi00nygoog
- WebFetch: https://archive.org/metadata/philistineaperi03nygoog
- WebFetch: https://archive.org/metadata/philistineaperi02nygoog
- WebFetch: https://ia802802.us.archive.org/12/items/philistineaperi02nygoog/philistineaperi02nygoog_djvu.txt
- WebFetch: https://www.google.com/books/edition/_/ZLtU6_kAKZIC?gbpv=1&bsq=%22dam%20fool%22
- WebFetch: https://books.google.com/books?id=ZLtU6_kAKZIC&newbks=0&printsec=frontcover&q=%22dam+fool%22
- WebSearch: "Roycroft Dictionary" Hubbard archive.org full text
- WebFetch: https://www.goodreads.com/quotes/80344-every-man-is-a-damn-fool-for-at-least-five
- WebFetch: https://www.gutenberg.org/cache/epub/36566/pg36566.txt
- WebFetch: https://archive.org/metadata/roycroftdiction00hubbgoog
- WebFetch: https://ia601607.us.archive.org/28/items/roycroftdiction00hubbgoog/roycroftdiction00hubbgoog_djvu.txt
- WebFetch: https://ia601607.us.archive.org/28/items/roycroftdiction00hubbgoog/roycroftdiction00hubbgoog_djvu.txt
- WebFetch: https://archive.org/metadata/roycroftdictiona00hubb
- WebFetch: https://www.azquotes.com/quote/531137
- WebFetch: https://ia800600.us.archive.org/0/items/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt
- WebFetch: https://ia800600.us.archive.org/0/items/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt
- WebFetch: https://ia800600.us.archive.org/0/items/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt
- WebFetch: https://quotepark.com/quotes/1113094-elbert-hubbard-every-man-is-a-damn-fool-for-at-least-five-minutes/

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Elbert Hubbard said that every man is a damn fool for at least five minutes every day, and that wisdom consists in not exceeding the limit."

**Roots:** Echo · **Grounding:** Grounded · Mutated
**Earliest instance found:** *The Philistine*, Vol. 29, No. 6 (the magazine Hubbard edited), November 1909, p. 192 (date from: cited by [Quote Investigator](https://quoteinvestigator.com/2026/11/20/fool-minutes/) and [Wist](https://wist.info/author/hubbard-elbert-green/)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 14

### Chain
Your version: "Elbert Hubbard said: every man is a damn fool for at least five minutes every day; wisdom consists in not exceeding the limit" (where you met it: not given)
 ├─ [Goodreads](https://www.goodreads.com/quotes/80344-every-man-is-a-damn-fool-for-at-least-five), date unknown, Tertiary → credits *The Roycroft Dictionary* (1914) → stopped: citation does not hold
 ├─ [Quotepark](https://quotepark.com/quotes/1113094-elbert-hubbard-every-man-is-a-damn-fool-for-at-least-five-minutes/), date unknown, Secondary → cites
 │   └─ [*The Roycroft Dictionary and Book of Epigrams*](https://ia800600.us.archive.org/0/items/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt), 1923, Primary (cold trail)
 ├─ [AZQuotes](https://www.azquotes.com/quote/531137), date unknown, Tertiary → cites
 │   └─ *A Thousand & One Epigrams*, 1911, (not opened), per AZQuotes → stopped: not opened
 ├─ [Wist](https://wist.info/author/hubbard-elbert-green/), 2004 (entry added 1 Feb 2004), Secondary → cites
 │   └─ [*The Philistine*, Vol. 29, No. 6](https://books.google.pl/books?id=9YlHAAAAYAAJ&pg=PA192&redir_esc=y), 1909, Primary (not opened, per Quote Investigator and Wist), root
 └─ [Quote Investigator](https://quoteinvestigator.com/2026/11/20/fool-minutes/), 2026, Secondary → cites
     ├─ *The Philistine*, Vol. 29, No. 6, 1909: the root above
     ├─ James K. Vardaman's *The Issue*, Jackson, Miss., 13 Nov 1909, (not opened), per Quote Investigator → cites *The Philistine* (the root)
     ├─ [*The Philistine*, Vol. 30, No. 2, p. 57](https://ia802802.us.archive.org/12/items/philistineaperi02nygoog/philistineaperi02nygoog_djvu.txt), Jan 1910, Primary (cold trail)
     ├─ *The Fra*, Vol. 4, No. 6, Mar 1910, Primary (not opened, per Quote Investigator)
     ├─ *The Kansas City Kansan*, 16 Nov 1922, (not opened), per Quote Investigator
     ├─ Dale Carnegie, *How to Stop Worrying and Start Living*, 1948, (not opened), per Quote Investigator
     └─ *The Fitzhenry & Whiteside Book of Quotations*, 1981, (not opened), per Quote Investigator

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Number changed | every man is a fool at least *ten* minutes a day (per Quote Investigator; root not opened) | every man is a damn fool for at least five minutes every day | [*The Philistine*, Vol. 30, No. 2](https://ia802802.us.archive.org/12/items/philistineaperi02nygoog/philistineaperi02nygoog_djvu.txt), 1910 |
| Other: spelling | *dam* fool | damn fool | *The Issue*, 1909 (not opened, per Quote Investigator) |

### Status of the root
- No retraction or correction checks apply to a filler item in a 1909 magazine, so none were run. Two Google Books copies of the root were tried and returned no text. A captcha blocked a third copy.
- Per Wist, the November 1909 line ran uncredited in a list of aphorisms in *The Philistine*, which Hubbard edited.
- Quote Investigator concludes that "Elbert Hubbard deserves credit for this saying". It found that he published three versions.
- Quote Investigator: a 1922 Kansas City newspaper tied a *10 per cent of the time* version to a local man, Abe Sturgess. The page does not show him as its originator.
- *The Philistine*, Vol. 30, No. 2 (January 1910), opened: Hubbard's piece has the five-minutes sentence, but follows it with a clause about three days of insight a month. It does not have the wisdom sentence.
- *The Roycroft Dictionary and Book of Epigrams* (1923), opened: "Every man is a damn fool for at least five minutes every day." The next sentence is the wisdom line, in an untitled epigram in the *Book of Epigrams* section. Quote Investigator's timeline does not list this book.
- [*The Roycroft Dictionary*](https://ia601607.us.archive.org/28/items/roycroftdiction00hubbgoog/roycroftdiction00hubbgoog_djvu.txt) (1914), which Goodreads gives as the source, was read in full. *Damn fool* appears only in the entry *If*, a different joke. It does not have the five-minutes line.

### Cold trails
- [*The Philistine*, Vol. 30, No. 2](https://ia802802.us.archive.org/12/items/philistineaperi02nygoog/philistineaperi02nygoog_djvu.txt), 1910: states a five-minutes variant and cites nothing (Hubbard reworking his own line)
- [*The Roycroft Dictionary and Book of Epigrams*](https://ia800600.us.archive.org/0/items/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt), 1923: states the line in your wording and cites nothing

### Confidence
Medium: later Hubbard texts from 1910 and 1923 were opened, but the November 1909 root was not, and its date rests on Quote Investigator and Wist.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
