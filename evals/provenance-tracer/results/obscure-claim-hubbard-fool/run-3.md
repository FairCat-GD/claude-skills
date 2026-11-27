---
case: obscure-claim-hubbard-fool
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:19:47Z
cost_usd: 1.3229
duration_s: 171
turns: 33
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- Read: <plugin>/skills/provenance-tracer/references/labels.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- WebSearch: "damn fool for at least five minutes every day" "not exceeding the limit"
- WebSearch: "every man is a damn fool for at least five minutes" Hubbard
- WebSearch: Elbert Hubbard "five minutes" fool wisdom limit Philistine
- WebSearch: "wisdom consists in not exceeding the limit"
- WebSearch: origin "five minutes every day" fool "exceeding the limit" quote
- WebSearch: quoteinvestigator fool five minutes a day wisdom exceeding limit Hubbard
- WebFetch: https://quoteinvestigator.com/2026/11/20/fool-minutes/
- WebFetch: https://wist.info/author/hubbard-elbert-green/
- WebFetch: https://en.wikiquote.org/wiki/Elbert_Hubbard
- WebFetch: https://books.google.com/books?id=9YlHAAAAYAAJ&pg=PA192&#v=onepage&q=%22dam%20fool%22&f=false
- WebFetch: https://www.google.com/books/edition/The_Philistine/iv4-AAAAYAAJ?hl=en&gbpv=1&dq=%22dam+fool%22&pg=PA57&printsec=frontcover
- WebFetch: https://www.newspapers.com/article/vardamans-weekly-philistine/210580938/
- WebFetch: https://www.azquotes.com/quote/531137
- WebFetch: https://books.google.pl/books?id=9YlHAAAAYAAJ&pg=PA192&redir_esc=y
- WebFetch: https://books.google.com/books?id=iv4-AAAAYAAJ&newbks=0&printsec=frontcover&pg=PA57&dq=%22dam+fool%22&hl=en
- WebSearch: "A Thousand & One Epigrams" Hubbard 1911 archive.org OR gutenberg
- WebFetch: https://books.google.pl/books?id=iv4-AAAAYAAJ&newbks=0&printsec=frontcover&pg=PA57&dq=%22dam+fool%22&hl=en&redir_esc=y
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28thousand+one+epigrams%29+AND+creator%3A%28hubbard%29&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=year&rows=10&output=json
- WebFetch: https://babel.hathitrust.org/cgi/ls?q1=%22damn+fool+for+at+least+five+minutes%22&anyall1=phrase&lmt=ft
- WebFetch: https://archive.org/advancedsearch.php?q=%22Thousand+and+one+epigrams%22+OR+%22thousand+%26+one+epigrams%22&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=year&rows=10&output=json
- WebSearch: "Roycroft Dictionary" Hubbard full text "damn fool" gutenberg OR archive.org
- WebFetch: https://www.gutenberg.org/files/36566/36566-h/36566-h.htm
- WebFetch: https://archive.org/stream/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt
- WebFetch: https://archive.org/stream/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt
- WebFetch: https://archive.org/stream/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Elbert Hubbard said: every man is a damn fool for at least five minutes every day; wisdom consists in not exceeding the limit."

**Roots:** Echo · **Grounding:** Grounded · Mutated
**Earliest instance found:** [*The Philistine*, Vol. 29, No. 6, p. 192](https://books.google.pl/books?id=9YlHAAAAYAAJ&pg=PA192&redir_esc=y), 1909 (date from: cited by Quote Investigator, which dates it November 1909). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 13

### Chain
Your version: "Elbert Hubbard said: every man is a damn fool for at least five minutes every day; wisdom consists in not exceeding the limit" (where you met it: not given)
 ├─ [AZQuotes](https://www.azquotes.com/quote/531137), date unknown, Secondary → cites
 │   └─ *A Thousand & One Epigrams: Selected from the Writings of Elbert Hubbard*, 1911, Primary (not opened, per AZQuotes) → stopped: not opened
 ├─ [Wikiquote, *Elbert Hubbard*](https://en.wikiquote.org/wiki/Elbert_Hubbard), date unknown, Secondary → cites
 │   └─ [*The Roycroft Dictionary and Book of Epigrams*](https://archive.org/stream/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt), 1923, Primary (a posthumous Roycrofters collection that cites nothing earlier)
 └─ [Quote Investigator, *Quote Origin: Everyone Is a Damn Fool at Least Ten Minutes a Day…*](https://quoteinvestigator.com/2026/11/20/fool-minutes/), 2026, Secondary → cites
     ├─ *Reader's Digest Quotable Quotes*, 1997, p. 25, (not opened), per Quote Investigator, Tertiary
     ├─ *The Fitzhenry & Whiteside Book of Quotations*, 1981, p. 304, (not opened), per Quote Investigator, Tertiary
     ├─ Dale Carnegie, *How to Stop Worrying and Start Living*, 1948, p. 175, (not opened), per Quote Investigator, Secondary. It introduces the line with "Elbert Hubbard said:", as your version does.
     ├─ *The Kansas City Kansan*, "Sidelines" column, 1922, (not opened), per Quote Investigator, Tertiary. This variant ("10 per cent of the time") credits a local man, Abe Sturgess.
     ├─ *The Fra*, Vol. 4, No. 6, March 1910, (not opened), per Quote Investigator, Primary (not opened, per Quote Investigator). Hubbard's variant: "locoed logically half an hour every day."
     ├─ [*The Philistine*, Vol. 30, No. 2, p. 57](https://books.google.pl/books?id=iv4-AAAAYAAJ&newbks=0&printsec=frontcover&pg=PA57&dq=%22dam+fool%22&hl=en&redir_esc=y), January 1910, Primary (not opened, per Quote Investigator). The scan page returned no text. This is where "five minutes every day" first appears.
     └─ *The Issue* (ed. James K. Vardaman), 13 November 1909, p. 5, (not opened), per Quote Investigator, Secondary → cites
         └─ [*The Philistine*, Vol. 29, No. 6, p. 192](https://books.google.pl/books?id=9YlHAAAAYAAJ&pg=PA192&redir_esc=y), November 1909, Primary (not opened, per Quote Investigator). The scan page returned no text. This is the root.

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Number changed | a fool for at least ten minutes a day (unsigned filler in Hubbard's magazine) | at least five minutes every day | *The Philistine*, January 1910, per Quote Investigator, which describes this as Hubbard's own revision |
| Other: spelling | "dam" | "damn" | *The Issue*, November 1909, per Quote Investigator, where Vardaman changed it |

### Status of the root
- The root is a magazine filler, not a study, so the retraction and correction checks (Crossref, Retraction Watch, PubPeer) don't apply and weren't run.
- Quote Investigator weighed James K. Vardaman and Abe Sturgess as other possible sources. It [concluded](https://quoteinvestigator.com/2026/11/20/fool-minutes/) "Elbert Hubbard deserves credit for this saying." It says Hubbard edited *The Philistine* and published three versions of the line, in 1909 and 1910.
- The 1923 Roycrofters collection, opened, prints the line as "[Every man is a damn fool for at least five minutes every day.](https://archive.org/stream/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt)" The next sentence is "Wisdom consists in not exceeding the limit." Wikiquote's version of this entry ("five minutes a day", "consists of") differs slightly from the scanned text.

### Cold trails
- [*The Roycroft Dictionary and Book of Epigrams*](https://archive.org/stream/roycroftdictiona00hubb/roycroftdictiona00hubb_djvu.txt), 1923: states the claim and cites nothing. It is a posthumous collection of Hubbard's writing, later than the 1909 root.

### Confidence
Medium: the 1909 and 1910 *Philistine* scans returned no readable text, so the root and its dates rest on Quote Investigator (cited by). The only Primary opened is the 1923 collection.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
