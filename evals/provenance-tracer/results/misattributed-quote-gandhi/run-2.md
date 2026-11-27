---
case: misattributed-quote-gandhi
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T15:36:44Z
cost_usd: 1.7148
duration_s: 194
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
- WebSearch: "be the change you want to see" origin
- WebSearch: Gandhi "If we could change ourselves, the tendencies in the world would also change"
- WebSearch: who first said "be the change you wish to see" earliest
- WebSearch: quote investigator "be the change you wish to see in the world"
- WebSearch: "be the change" Gandhi misattributed fact check
- WebFetch: https://quoteinvestigator.com/2017/10/23/be-change/
- WebFetch: https://dailycaller.com/2019/12/06/fact-check-mahatma-gandhi-change-wish-see-world/
- WebSearch: Collected Works of Mahatma Gandhi volume 13 "We but mirror the world" Indian Opinion 1913 archive.org OR gandhiheritageportal
- WebFetch: http://www.gandhiashramsevagram.org/gandhi-literature/mahatma-gandhi-collected-works-volume-13.pdf
- WebFetch: https://dokumen.pub/the-complete-works-of-mahatma-gandhi-volume-13-13.html
- WebSearch: archive.org "Collected Works of Mahatma Gandhi" volume XII OR 12 OR 13 1913 djvu
- WebFetch: https://slate.com/podcasts/decoder-ring/2026/10/be-the-change-mahatma-gandhi-quotation-arleen-lorrance-bishop-james-pike-al-gore
- WebSearch: wikisource "We but mirror the world" Gandhi "General Knowledge About Health"
- WebFetch: https://archive.org/details/HindSwaraj-CWMG-012
- WebFetch: https://archive.org/download/HindSwaraj-CWMG-012/CWMG-v012-XII-MC-BETA_djvu.txt
- WebFetch: https://dn760107.eu.archive.org/0/items/HindSwaraj-CWMG-012/CWMG-v012-XII-MC-BETA_djvu.txt
- WebFetch: https://dn760107.eu.archive.org/0/items/HindSwaraj-CWMG-012/CWMG-v012-XII-MC-BETA_djvu.txt
- WebFetch: https://dailycallernewsfoundation.org/2019/12/06/fact-check-did-gandhi-say-you-must-be-the-change-you-wish-to-see-in-the-world/
- WebFetch (error): https://www.nytimes.com/2011/08/30/opinion/falser-words-were-never-spoken.html
- WebSearch: Lorrance "Developing Priorities and a Style" 1974 "be the change you want to see happen"
- WebFetch: https://books.google.com/books?id=NcTimfiMzYUC&q=%22be+the+change+you+want+to+see%22
- WebFetch: https://compassionatespirit.com/wpblog/2012/08/14/be-the-change-where-did-this-saying-come-from/
- WebFetch: https://www.professorbuzzkill.com/arleen-lorrance-be-the-change/

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Gandhi said, 'Be the change you wish to see in the world.'"

**Roots:** Echo · **Grounding:** Primary differs · Mutated · Misattributed
**Earliest instance found:** [Arleen Lorrance, *The Love Project*, in *Developing Priorities and a Style* (ed. Richard Dean Kellough)](https://books.google.com/books?id=NcTimfiMzYUC&q=%22be+the+change+you+want+to+see%22), 1974 (date from: cited by Quote Investigator). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 8

### Chain
Your version: "Gandhi said: be the change you wish to see in the world" (where you met it: not given)
 ├─ [Daily Caller News Foundation, *FACT CHECK: Did Gandhi Say, 'You Must Be The Change You Wish To See In The World'?*](https://dailycallernewsfoundation.org/2019/12/06/fact-check-did-gandhi-say-you-must-be-the-change-you-wish-to-see-in-the-world/), 2019, Tertiary → cites
 │   └─ [Quote Investigator, *Quote Origin: Be the Change You Wish To See in the World*](https://quoteinvestigator.com/2017/10/23/be-change/), 2017, Secondary → cites
 │       ├─ [Arleen Lorrance, *The Love Project*, in *Developing Priorities and a Style*](https://books.google.com/books?id=NcTimfiMzYUC&q=%22be+the+change+you+want+to+see%22), 1974, Primary (not opened, per Quote Investigator), root
 │       └─ Denise Kusel, *Celebration of the human spirit*, *The Santa Fe New Mexican*, 1987, (not opened), per Quote Investigator → credits Gandhi
 │           └─ [M. K. Gandhi, *General Knowledge About Health XXXII: Accidents: Snake-Bite*, *Indian Opinion*, in *The Collected Works of Mahatma Gandhi*, Vol. XII, p. 158](https://dn760107.eu.archive.org/0/items/HindSwaraj-CWMG-012/CWMG-v012-XII-MC-BETA_djvu.txt), 1913, Primary (credited, differs)
 ├─ [Slate, *Decoder Ring*: Gandhi never said "be the change" (episode page)](https://slate.com/podcasts/decoder-ring/2026/10/be-the-change-mahatma-gandhi-quotation-arleen-lorrance-bishop-james-pike-al-gore), 2026, Secondary → cites
 │   └─ Quote Investigator, 2017, and Lorrance, 1974 (root), both above
 ├─ [Professor Buzzkill, *Arleen Lorrance 'Be the Change…' Special Episode!*](https://www.professorbuzzkill.com/arleen-lorrance-be-the-change/), 2020, Secondary → cites
 │   └─ Lorrance, 1974 (root, above)
 └─ [Keith Akers, *'Be the Change' — where did this saying come from?*, Compassionate Spirit](https://compassionatespirit.com/wpblog/2012/08/14/be-the-change-where-did-this-saying-come-from/), 2012, Tertiary → cites
     └─ Craig Schindler and Gary Lapid, *The Great Turning*, p. 121, 1989, (not opened), per Compassionate Spirit → credits Gandhi
         └─ Gandhi, 1913 (credited, differs, above)

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Attribution shifted | Lorrance wrote it in her own chapter on her school Love Project and credited it to no one else | Gandhi said: be the change you wish to see in the world | Denise Kusel, *The Santa Fe New Mexican*, 1987 (not opened, per Quote Investigator) |
| Scope widened | [“be the change you want to see happen”](https://quoteinvestigator.com/2017/10/23/be-change/), offered as a way to start a preventive programme in schools; *happen* later became *in the world* | Gandhi said: be the change you wish to see in the world | Denise Kusel, *The Santa Fe New Mexican*, 1987 (not opened, per Quote Investigator) |
| Other: wording, *want* became *wish* | *want*, in Quote Investigator's transcription (Professor Buzzkill's copy of the same sentence has *wish*) | Gandhi said: be the change you wish to see in the world | *Los Angeles Times*, 1989 (not opened, per Quote Investigator, via *The Yale Book of Quotations*) |

### Status of the root
- Lorrance's 1974 chapter is a book chapter, not a study, so no retraction, correction or replication check applies. None was run.
- Gandhi's 1913 text (the credited text): the opened *Collected Works* scan, Vol. XII, has a related passage in a health-series instalment on snakebite. It says that if people changed themselves, the tendencies of the world would change too. It does not contain the slogan's wording.
- Gandhi's 1913 text: the [Daily Caller News Foundation](https://dailycallernewsfoundation.org/2019/12/06/fact-check-did-gandhi-say-you-must-be-the-change-you-wish-to-see-in-the-world/) rated the attribution *False* in 2019. It reported that a search of the Gandhi Heritage Portal's collected works found no match, and that Gandhi scholar Johannes Bakker doubted it is a direct quote but called the sentiment Gandhian.
- Gandhi attribution: [Quote Investigator](https://quoteinvestigator.com/2017/10/23/be-change/) lists Lorrance's wording in print from 1975 to 1978 with no mention of Gandhi. Gandhi's name first appears with it in a 1987 newspaper, and *The Yale Book of Quotations* (2006) cites a 1989 *Los Angeles Times* version credited to him.

### Cold trails
None.

### Confidence
Medium: the root (Lorrance's 1974 chapter) could not be opened because Google Books blocked the fetch, so its date and wording rest on Quote Investigator, copies disagree on *want* versus *wish*, and Slate and Akers name earlier Lorrance items (a 1971 *New York Daily News* article and her 1972 book *The Love Project*) that this search did not open.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
