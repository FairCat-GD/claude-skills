---
case: misattributed-quote-gandhi
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:35:09Z
cost_usd: 1.0890
duration_s: 119
turns: 23
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
- WebSearch: "be the change you want to see in the world" origin
- WebSearch: Gandhi "If we could change ourselves, the tendencies in the world would also change"
- WebSearch: who first said "be the change you wish to see"
- WebSearch: quoteinvestigator be the change you wish to see in the world Gandhi
- WebSearch: "be the change" Gandhi misattributed fact check
- WebFetch: https://quoteinvestigator.com/2017/10/23/be-change/
- WebFetch: https://dailycallernewsfoundation.org/2019/12/06/fact-check-did-gandhi-say-you-must-be-the-change-you-wish-to-see-in-the-world/
- WebFetch: https://en.wikiquote.org/wiki/Mahatma_Gandhi
- WebFetch: https://archive.org/details/HindSwaraj-CWMG-012/page/158/mode/1up
- WebFetch: https://books.google.com/books?id=NcTimfiMzYUC&q=%22be+the+change+you+want+to+see%22
- WebFetch (error): https://www.nytimes.com/2011/08/30/opinion/falser-words-were-never-spoken.html
- WebFetch: https://archive.org/stream/HindSwaraj-CWMG-012/CWMG-v012-XII-MC-BETA_djvu.txt
- WebFetch: https://archive.org/stream/HindSwaraj-CWMG-012/CWMG-v012-XII-MC-BETA_djvu.txt
- WebFetch: https://archive.org/stream/HindSwaraj-CWMG-012/CWMG-v012-XII-MC-BETA_djvu.txt

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Gandhi said: be the change you wish to see in the world"

**Roots:** Independent · **Grounding:** Primary differs · Mutated · Misattributed
**Earliest instance found:** Arleen Lorrance, *The Love Project*, a chapter in *Developing Priorities and a Style*, ed. Richard Dean Kellough, 1974 (date from: cited by [Quote Investigator](https://quoteinvestigator.com/2017/10/23/be-change/)). Earlier instances may exist.
**Roots:** 2 · **Retellings found:** 10

### Chain
Your version: "Gandhi said: be the change you wish to see in the world" (where you met it: not given)
 └─ [Wikiquote, *Mahatma Gandhi*](https://en.wikiquote.org/wiki/Mahatma_Gandhi), date unknown, Tertiary → cites
 ├─ [Daily Caller News Foundation fact check](https://dailycallernewsfoundation.org/2019/12/06/fact-check-did-gandhi-say-you-must-be-the-change-you-wish-to-see-in-the-world/), 2019, Secondary. It searched the 100 volumes on the Gandhi Heritage Portal, found no match, and rated the attribution "False". → cites
 └─ [Quote Investigator, *Quote Origin: Be the Change You Wish To See in the World*](https://quoteinvestigator.com/2017/10/23/be-change/), 2017, Secondary → cites
     ├─ [Brian Morton, *Falser Words Were Never Spoken*, *The New York Times*](https://www.nytimes.com/2011/08/30/opinion/falser-words-were-never-spoken.html), 2011, (not opened), per Quote Investigator → stopped: not opened
     ├─ Fred R. Shapiro, *The Yale Book of Quotations*, p. 299, 2006, (not opened), per Quote Investigator. It notes the Gandhi Institute for Nonviolence had not traced the saying in his writings. → cites
     │   └─ *Los Angeles Times*, "We must be the change we wish to see in the world", 1989, (not opened), per Quote Investigator → stopped: not opened
     ├─ Denise Kusel, *The Santa Fe New Mexican*, p. A4, 1987, (not opened), per Quote Investigator. Organizer Mary Lou Cook credits Gandhi with "You must be the change you want to see in the world". This is the earliest Gandhi attribution in the chain. → cites
     │   └─ Mohandas K. Gandhi, *General Knowledge About Health XXXII: Accidents: Snake-Bite*, *Indian Opinion*, 9 Aug 1913, repr. [*Collected Works of Mahatma Gandhi*, vol. XII, p. 158](https://archive.org/stream/HindSwaraj-CWMG-012/CWMG-v012-XII-MC-BETA_djvu.txt), 1913, Primary (root 1)
     ├─ Diane Kennedy Pike, *Life is Victorious!*, p. 196, 1976, (not opened), per Quote Investigator → cites
     └─ Arleen Lorrance, *The Love Project*, in [*Developing Priorities and a Style*](https://books.google.com/books?id=NcTimfiMzYUC&q=%22be+the+change+you+want+to+see%22), p. 85, 1974, Primary (not opened, per Quote Investigator) (root 2)

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Attribution shifted | Lorrance's 1974 chapter has [“be the change you want to see happen”](https://quoteinvestigator.com/2017/10/23/be-change/) and does not mention Gandhi | "Gandhi said: be the change…" | *The Santa Fe New Mexican*, 1987 (not opened, per Quote Investigator) |
| Other: a conditional observation recast as a command | Gandhi wrote [“If we could change ourselves, the tendencies in the world would also change.”](https://archive.org/stream/HindSwaraj-CWMG-012/CWMG-v012-XII-MC-BETA_djvu.txt) | "be the change you wish to see in the world" | *The Santa Fe New Mexican*, 1987 (not opened, per Quote Investigator) |
| Context removed | Gandhi's line sits in a newspaper health column about snake-bite: as a person changes, the world's attitude towards them changes | a stand-alone motto about changing the world | *The Santa Fe New Mexican*, 1987 (not opened, per Quote Investigator) |
| Other: wording changed | Lorrance: "want to see happen" | "wish to see in the world" | "in the world": *The Santa Fe New Mexican*, 1987; "wish": *Los Angeles Times*, 1989 (both not opened, per Quote Investigator) |

### Status of the root
- Gandhi, 1913: the passage is reprinted in the *Collected Works of Mahatma Gandhi*, vol. XII, p. 158, dated 9-8-1913 ([opened](https://archive.org/stream/HindSwaraj-CWMG-012/CWMG-v012-XII-MC-BETA_djvu.txt)). It is a newspaper column, not a study, so there is no retraction, correction or replication record to check.
- Lorrance, 1974: a book chapter, not a study, so there is no retraction or replication record to check. The Google Books page returned a captcha and was not opened.
- *The Yale Book of Quotations*, as reported by [Quote Investigator](https://quoteinvestigator.com/2017/10/23/be-change/), records that the Gandhi family believed the saying to be original with him.

### Cold trails
None.

### Confidence
Medium: Gandhi's 1913 text was opened in the *Collected Works*, but the 1974 Lorrance chapter and the 1987 and 1989 attribution nodes were not opened, and their dates come from Quote Investigator (date from: cited by).

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
