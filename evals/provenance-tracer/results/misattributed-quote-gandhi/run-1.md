---
case: misattributed-quote-gandhi
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T15:34:25Z
cost_usd: 1.4929
duration_s: 192
turns: 32
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- Read: <plugin>/skills/provenance-tracer/references/labels.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- WebSearch: "be the change you wish to see in the world" Gandhi
- WebSearch: Quote Investigator "be the change you wish to see in the world"
- WebSearch: origin of "be the change you want to see in the world"
- WebSearch: Gandhi "If we could change ourselves, the tendencies in the world would also change" Collected Works
- WebSearch: "be the change" Gandhi misattributed Arleen Lorrance 1974
- WebSearch: "be the change you wish to see" Gandhi fact check earliest appearance
- WebFetch: https://quoteinvestigator.com/2017/10/23/be-change/
- WebFetch: https://dailycallernewsfoundation.org/2019/12/06/fact-check-did-gandhi-say-you-must-be-the-change-you-wish-to-see-in-the-world/
- WebFetch: https://professorbuzzkill.com/2017/01/09/gandhi-be-the-change-you-wish-to-see-in-the-world/
- WebFetch: https://books.google.com/books?id=NcTimfiMzYUC&q=%22be+the+change+you+want+to+see%22
- WebFetch: https://archive.org/details/in.ernet.dli.2015.32787/page/n187/mode/2up
- WebFetch: http://www.gandhiashramsevagram.org/gandhi-literature/mahatma-gandhi-collected-works-volume-13.pdf
- WebFetch: https://archive.org/metadata/in.ernet.dli.2015.32787
- WebSearch: "We but mirror the world" Gandhi "Snake-bite" Indian Opinion 1913 Collected Works text
- WebFetch: https://archive.org/download/in.ernet.dli.2015.32787/2015.32787.Collected-Works-Of-Mahatma-Gandhi--Vol12_djvu.txt
- WebFetch: https://dn710806.ca.archive.org/0/items/in.ernet.dli.2015.32787/2015.32787.Collected-Works-Of-Mahatma-Gandhi--Vol12_djvu.txt
- WebFetch: https://dn710806.ca.archive.org/0/items/in.ernet.dli.2015.32787/2015.32787.Collected-Works-Of-Mahatma-Gandhi--Vol12_djvu.txt
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28Developing+Priorities+and+a+Style%29&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=year&rows=10&output=json
- WebSearch: "Santa Fe New Mexican" 1987 "Mary Lou Cook" Gandhi "be the change"
- WebFetch (error): https://www.nytimes.com/2011/08/30/opinion/falser-words-were-never-spoken.html
- WebFetch: https://falschzitate.blogspot.com/2019/08/sei-du-selbst-die-veranderung-die-du.html
- WebFetch: https://quoteiac.com/blogs/journal/be-the-change-the-most-famous-quote-gandhi-probably-never-said
- WebFetch: https://josephranseth.com/gandhi-didnt-say-be-the-change-you-want-to-see-in-the-world/
- WebFetch: https://www.brainyquote.com/quotes/mahatma_gandhi_109075

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Gandhi said: be the change you wish to see in the world."

**Roots:** Echo · **Grounding:** No primary found · Mutated · Misattributed
**Earliest instance found:** Arleen Lorrance, *The Love Project*, a chapter in *Developing Priorities and a Style: Selected Readings in Education for Teachers and Parents*, ed. Richard D. Kellough, p. 85, 1974 (date from: cited by Quote Investigator). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 7

### Chain
Your version: "Gandhi said: be the change you wish to see in the world" (where you met it: not given)
 ├─ [Daily Caller News Foundation fact check](https://dailycallernewsfoundation.org/2019/12/06/fact-check-did-gandhi-say-you-must-be-the-change-you-wish-to-see-in-the-world/), 2019, Tertiary. It rated the Gandhi attribution *False*. → cites
 │   └─ [Quote Investigator](https://quoteinvestigator.com/2017/10/23/be-change/), 2017, Secondary → cites
 │       ├─ *The Santa Fe New Mexican*, Denise Kusel, 22 March 1987, p. 4, (not opened), per Quote Investigator. This is the earliest Gandhi credit Quote Investigator lists, given by organizer Mary Lou Cook. → credits Gandhi
 │       │   └─ [Gandhi, *Indian Opinion*, 1913, reprinted in *Collected Works* vol. XII, p. 158](https://archive.org/details/in.ernet.dli.2015.32787/page/n187/mode/2up), 1913, Primary (not opened, per Quote Investigator), credited text → stopped: not opened
 │       └─ [Arleen Lorrance, *The Love Project*, in *Developing Priorities and a Style*](https://books.google.com/books?id=NcTimfiMzYUC&q=%22be+the+change+you+want+to+see%22), 1974, Primary (not opened, per Quote Investigator), root
 ├─ [Professor Buzzkill](https://professorbuzzkill.com/2017/01/09/gandhi-be-the-change-you-wish-to-see-in-the-world/), 2017, Secondary → cites
 │   ├─ Lorrance, 1974, the root above
 │   └─ Gandhi, *Indian Opinion*, 9 August 1913, cited here as *Collected Works* vol. 13, ch. 153, p. 241, (not opened), per Professor Buzzkill → stopped: not opened
 ├─ [Quoteiac](https://quoteiac.com/blogs/journal/be-the-change-the-most-famous-quote-gandhi-probably-never-said), 2026, Tertiary → cites Quote Investigator (above)
 └─ [Joseph Ranseth](https://josephranseth.com/gandhi-didnt-say-be-the-change-you-want-to-see-in-the-world/), 2015, Tertiary: cold trail (below)

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Attribution shifted | Lorrance's own line, with no mention of Gandhi: ["be the change you want to see happen."](https://quoteinvestigator.com/2017/10/23/be-change/) | Gandhi said: be the change you wish to see in the world | *The Santa Fe New Mexican*, 1987 (not opened) |
| Scope widened | the change should *happen*, with no wider reach named | be the change you wish to see in the world | *The Santa Fe New Mexican*, 1987 (not opened) |
| Context removed | advice on how to start a preventative program, in a chapter for teachers and parents | be the change you wish to see in the world | *The Santa Fe New Mexican*, 1987 (not opened) |

### Status of the root
- No primary found, so there was no status to check.
- Gandhi, 1913: the closest passage that sources trace to Gandhi is a 1913 *Indian Opinion* article on snakebite. One retelling gives it as ["the tendencies in the world would also change"](https://josephranseth.com/gandhi-didnt-say-be-the-change-you-want-to-see-in-the-world/), after a condition about changing ourselves. Sources cite it in different places: Quote Investigator gives *Collected Works* vol. XII, p. 158, and Professor Buzzkill gives vol. 13, p. 241. Quoteiac traces it to the 1921 English translation, *A Guide to Health*. I tried two copies and opened neither: the vol. 13 PDF link redirects to a 404 page, and the Internet Archive scan labelled vol. XII holds 1937 material in the pages I read.
- The [Daily Caller News Foundation](https://dailycallernewsfoundation.org/2019/12/06/fact-check-did-gandhi-say-you-must-be-the-change-you-wish-to-see-in-the-world/) reports that the saying ["has not been found in any of his written works or speeches"](https://dailycallernewsfoundation.org/2019/12/06/fact-check-did-gandhi-say-you-must-be-the-change-you-wish-to-see-in-the-world/).

### Cold trails
- [Joseph Ranseth](https://josephranseth.com/gandhi-didnt-say-be-the-change-you-want-to-see-in-the-world/), 2015: discusses the saying and gives a longer Gandhi passage, but the article cites no source for either.

### Confidence
Medium: the root and the credited Gandhi text were both found only through opened retellings and never opened themselves. The 1974 and 1987 dates rest on *cited by* Quote Investigator, and the retellings disagree on Lorrance's verb: Quote Investigator and the Daily Caller give *want*, while Professor Buzzkill and Quoteiac give *wish*.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
