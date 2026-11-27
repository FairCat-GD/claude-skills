---
case: misattributed-quote-gandhi
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T15:36:46Z
cost_usd: 1.3701
duration_s: 168
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
- WebSearch: "be the change you wish to see in the world" Gandhi
- WebSearch: "If we could change ourselves, the tendencies in the world would also change" Gandhi
- WebSearch: origin of "be the change you wish to see" earliest
- WebSearch: quoteinvestigator "be the change" Gandhi
- WebSearch: Gandhi never said "be the change" fact check
- WebSearch: "we must be the change we wish to see" Arleen Lorrance 1974
- WebFetch: https://quoteinvestigator.com/2017/10/23/be-change/
- WebFetch: https://dailycallernewsfoundation.org/2019/12/06/fact-check-did-gandhi-say-you-must-be-the-change-you-wish-to-see-in-the-world/
- WebFetch: https://listserv.linguistlist.org/pipermail/ads-l/2017-October/149775.html
- WebFetch: https://en.wikiquote.org/wiki/Mahatma_Gandhi
- WebFetch: http://gandhiashramsevagram.org/gandhi-literature/mahatma-gandhi-collected-works-volume-12.pdf
- WebFetch: https://books.google.com/books?id=NcTimfiMzYUC&q=%22be+the+change+you+want+to+see%22
- WebSearch: archive.org "Collected Works of Mahatma Gandhi" volume 12 djvu.txt "Snake-Bite"
- WebFetch: https://professorbuzzkill.com/2020/08/05/arleen-lorrance-be-the-change/
- WebFetch: https://dokumen.pub/the-complete-works-of-mahatma-gandhi-volume-13-13.html
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28collected+works+mahatma+gandhi%29&fl%5B%5D=identifier&fl%5B%5D=title&rows=50&output=json
- WebFetch: https://archive.org/metadata/collectedworksofmahatmagandhivol12_741_n/files
- WebFetch: https://archive.org/download/collectedworksofmahatmagandhivol12_741_n/Collected%20works%20of%20Mahatma%20Gandhi%20Vol%2012_djvu.txt
- WebFetch: https://dn711000.ca.archive.org/0/items/collectedworksofmahatmagandhivol12_741_n/Collected%20works%20of%20Mahatma%20Gandhi%20Vol%2012_djvu.txt
- WebFetch: https://archive.org/stream/in.ernet.dli.2015.32787/2015.32787.Collected-Works-Of-Mahatma-Gandhi-Vol12_djvu.txt

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Gandhi said: be the change you wish to see in the world."

**Roots:** Echo · **Grounding:** No primary found · Mutated · Misattributed
**Earliest instance found:** [Arleen Lorrance, *The Love Project*, in *Developing Priorities and a Style*, ed. Richard D. Kellough, p. 85](https://books.google.com/books?id=NcTimfiMzYUC&q=%22be+the+change+you+want+to+see%22), 1974 (date from: cited by Quote Investigator). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 10

### Chain
Your version: "Gandhi said: be the change you wish to see in the world" (where you met it: not given)
 └─ [Daily Caller News Foundation fact check](https://dailycallernewsfoundation.org/2019/12/06/fact-check-did-gandhi-say-you-must-be-the-change-you-wish-to-see-in-the-world/), 2019, Secondary → cites
     └─ [Quote Investigator, *Quote Origin: Be the Change You Wish To See in the World*](https://quoteinvestigator.com/2017/10/23/be-change/), 2017, Secondary → cites
         ├─ *The Santa Fe New Mexican*, 22 March 1987, (not opened), per Quote Investigator → credits Gandhi
         │   └─ M. K. Gandhi, *Accidents: Snake-Bite*, *Indian Opinion*, 9 Aug 1913 (*Collected Works* vol. XII, p. 158), 1913, Primary (not opened, per Quote Investigator), credited, differs
         ├─ *Reno Evening Gazette*, 30 June 1975, (not opened), per Quote Investigator → cites
         │   └─ Lorrance, 1974 (the root below)
         └─ [Arleen Lorrance, *The Love Project*](https://books.google.com/books?id=NcTimfiMzYUC&q=%22be+the+change+you+want+to+see%22), 1974, Primary (not opened, per Quote Investigator), root
 └─ [ADS-L post by Garson O'Toole](https://listserv.linguistlist.org/pipermail/ads-l/2017-October/149775.html), 2017, Secondary → cites
     ├─ Robert K. Cooper, *Health & Fitness Excellence*, 1989, (not opened), per ADS-L → credits Gandhi
     │   └─ Gandhi, *Indian Opinion*, 1913 (the credited text above)
     ├─ *Los Angeles Times*, 1989, via *The Yale Book of Quotations*, (not opened), per ADS-L → stopped: not opened
     └─ Lorrance, 1974 (the root above)
 └─ [Professor Buzzkill, *Arleen Lorrance "Be the Change…" Special Episode*](https://professorbuzzkill.com/2020/08/05/arleen-lorrance-be-the-change/), 2020, Secondary → cites
     └─ Lorrance, 1974 (the root above)
 └─ [Wikiquote, *Mahatma Gandhi*](https://en.wikiquote.org/wiki/Mahatma_Gandhi), date unknown, Tertiary → cites
     └─ Quote Investigator, 2017 (above)

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Attribution shifted | Lorrance's own sentence. Quote Investigator reports that it names no one else, and that Gandhi's closest text, from 1913, is a longer conditional thought about changing ourselves | Gandhi said: be the change you wish to see in the world | *The Santa Fe New Mexican*, 1987 (not opened, per Quote Investigator) |
| Scope widened | ["be the change you wish to see happen"](https://professorbuzzkill.com/2020/08/05/arleen-lorrance-be-the-change/) | be the change you wish to see in the world | *The Santa Fe New Mexican*, 1987 (not opened, per Quote Investigator) |
| Context removed | the opening line of a teacher's report on starting a preventative program in a Brooklyn high school | be the change you wish to see in the world | *Reno Evening Gazette*, 1975 (not opened, per Quote Investigator) |

### Status of the root
- No primary found, so there was no status to check.
- Gandhi, *Indian Opinion*, 1913 (credited text): the [Daily Caller News Foundation](https://dailycallernewsfoundation.org/2019/12/06/fact-check-did-gandhi-say-you-must-be-the-change-you-wish-to-see-in-the-world/) searched the Gandhi Heritage Portal's 100 volumes of his collected works, found no match for the line, and rated the Gandhi attribution *False*.

### Cold trails
None.

### Confidence
Medium: neither Lorrance's 1974 chapter nor Gandhi's 1913 passage could be opened (Google Books blocked the fetch, and the Volume XII copies either failed or opened a non-English edition), so both, and the 1987 first Gandhi credit, rest on opened secondary pages that disagree slightly on her wording (*want* or *wish*) and on whether her phrase dates from 1970, as Professor Buzzkill relays from her own account.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
