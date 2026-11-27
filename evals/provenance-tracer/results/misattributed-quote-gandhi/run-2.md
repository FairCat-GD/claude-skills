---
case: misattributed-quote-gandhi
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:35:09Z
cost_usd: 1.3877
duration_s: 169
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
- WebSearch: "be the change you want to see" Gandhi actual quote
- WebSearch: Gandhi "If we could change ourselves, the tendencies in the world would also change" Indian Opinion 1913
- WebSearch: "we must be the change we wish to see"
- WebSearch: origin of "be the change you wish to see in the world" earliest
- WebSearch: quoteinvestigator Gandhi be the change you wish to see
- WebFetch: https://quoteinvestigator.com/2017/10/23/be-change/
- WebFetch: https://dailycaller.com/2019/12/06/fact-check-mahatma-gandhi-change-wish-see-world/
- WebFetch: https://en.wikiquote.org/wiki/Mahatma_Gandhi
- WebSearch: Collected Works of Mahatma Gandhi Volume 12 pdf gandhiashramsevagram "General Knowledge About Health"
- WebFetch: https://dailycallernewsfoundation.org/2019/12/06/fact-check-did-gandhi-say-you-must-be-the-change-you-wish-to-see-in-the-world/
- WebFetch (error): https://www.nytimes.com/2011/08/30/opinion/falser-words-were-never-spoken.html
- WebFetch: http://gandhiashramsevagram.org/gandhi-literature/mahatma-gandhi-collected-works-volume-13.pdf
- WebFetch: https://library.bjp.org/jspui/bitstream/123456789/301/18/VOL013.PDF
- Read (denied): <temp>/config/projects/-private-tmp-e-llDTwt-home-cwd/434ace74-c24a-4953-904f-f5b7018b704b/tool-results/webfetch-1795772170969-jsfcer.pdf
- WebSearch: "We but mirror the world" "Snake-Bite" Gandhi Collected Works
- WebFetch: https://professorbuzzkill.com/2017/01/09/gandhi-be-the-change-you-wish-to-see-in-the-world/
- WebFetch: https://books.google.com/books?id=NcTimfiMzYUC&q=%22be+the+change+you+want+to+see%22
- WebFetch: https://jenniferlphillips.com/blog/2021/2/24/origin-story-be-the-change
- WebFetch: https://dokumen.pub/the-complete-works-of-mahatma-gandhi-volume-13-13.html

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Gandhi said: be the change you wish to see in the world."

**Roots:** Echo · **Grounding:** No primary found · Mutated · Misattributed
**Earliest instance found:** Arleen Lorrance, *The Love Project*, in *Developing Priorities and a Style: Selected Readings in Education for Teachers and Parents*, 1974 (date from: cited by [Quote Investigator](https://quoteinvestigator.com/2017/10/23/be-change/)). The earliest instance found that credits Gandhi is *The Santa Fe New Mexican*, 1987 (date from: cited by [Quote Investigator](https://quoteinvestigator.com/2017/10/23/be-change/)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 11

### Chain
Your version: "Gandhi said: be the change you wish to see in the world" (where you met it: not given)
 └─ [Daily Caller News Foundation fact check](https://dailycallernewsfoundation.org/2019/12/06/fact-check-did-gandhi-say-you-must-be-the-change-you-wish-to-see-in-the-world/) (Brad Sylvester), 2019, Secondary. It rates the attribution ["False"](https://dailycallernewsfoundation.org/2019/12/06/fact-check-did-gandhi-say-you-must-be-the-change-you-wish-to-see-in-the-world/) and reports no matches in the Gandhi Heritage Portal's Collected Works. → cites
     └─ [Quote Investigator, *Quote Origin: Be the Change You Wish To See in the World*](https://quoteinvestigator.com/2017/10/23/be-change/), 2017 (updated 2024), Secondary → cites
         ├─ [*New York Times*](https://www.nytimes.com/2011/08/30/opinion/falser-words-were-never-spoken.html), Brian Morton, *Falser Words Were Never Spoken*, 2011, (not opened), per Quote Investigator. It found no reliable documentary evidence for the Gandhi attribution. → stopped: not opened
         ├─ *Los Angeles Times*, 30 July 1989, (not opened), per Quote Investigator, citing *The Yale Book of Quotations* (2006). Variant: "We must be the change we wish to see in the world," credited to Gandhi. → stopped: not opened
         ├─ *The Santa Fe New Mexican*, Denise Kusel, 22 March 1987, (not opened), per Quote Investigator. Organizer Mary Lou Cook credits Gandhi with "you must be the change you want to see in the world." This is the earliest Gandhi attribution Quote Investigator found. → cites Gandhi by name, but no text is given → stopped: not opened
         ├─ Mohandas Gandhi, *General Knowledge About Health XXXII: Accidents Snake-Bite*, *Indian Opinion* (in Gujarati), 9 August 1913; *Collected Works*, Vol. XII (1964 edition), p. 158, Primary (not opened, per Quote Investigator). This is a related passage, not the slogan. Fetches of the [Sevagram PDF](http://gandhiashramsevagram.org/gandhi-literature/mahatma-gandhi-collected-works-volume-13.pdf) and the [BJP library PDF](https://library.bjp.org/jspui/bitstream/123456789/301/18/VOL013.PDF) returned no readable text. → stopped: not opened
         ├─ *Reno Evening Gazette*, 30 June 1975, and later 1976–1978 newspaper and book retellings of "Be the change you want to see happen," credited to Lorrance's Love Project, (not opened), per Quote Investigator → cites Lorrance
         └─ [Arleen Lorrance, *The Love Project*, in R. D. Kellough (ed.), *Developing Priorities and a Style*, MSS Information Corp., p. 85](https://books.google.com/books?id=NcTimfiMzYUC&q=%22be+the+change+you+want+to+see%22), 1974, Primary (not opened, per Quote Investigator; Google Books blocked the fetch). This is the root.
 ├─ [Professor Buzzkill (Joseph Coohill)](https://professorbuzzkill.com/2017/01/09/gandhi-be-the-change-you-wish-to-see-in-the-world/), 2017, Secondary. It dates Lorrance's report to 1970 and gives her line as ["be the change you wish to see happen"](https://professorbuzzkill.com/2017/01/09/gandhi-be-the-change-you-wish-to-see-in-the-world/). → cites *Indian Opinion* 1913, *Collected Works* vol. 13 p. 241, and Lorrance 1974 (all above)
 ├─ [Jennifer L. Phillips, *Origin Story: Be the Change*](https://jenniferlphillips.com/blog/2021/2/24/origin-story-be-the-change), 2021, Tertiary → cites Professor Buzzkill and Quote Investigator (both above)
 └─ [Wikiquote, *Mahatma Gandhi*](https://en.wikiquote.org/wiki/Mahatma_Gandhi), date unknown, Secondary. It lists the 1913 passage, ["If we could change ourselves, the tendencies in the world would also change."](https://en.wikiquote.org/wiki/Mahatma_Gandhi), and notes that Gandhi did not say the slogan in those exact words. → cites *Indian Opinion* 1913, the *NYT* 2011 and Quote Investigator (all above)

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Attribution shifted | Lorrance's own line about her school project, with no mention of Gandhi: ["be the change you want to see happen"](https://quoteinvestigator.com/2017/10/23/be-change/) | Gandhi said: be the change you wish to see in the world | *The Santa Fe New Mexican*, 1987, (not opened), per Quote Investigator |
| Scope widened | change you want to see *happen*, in a school's preventative program | change you wish to see *in the world* | *The Santa Fe New Mexican*, 1987 ("in the world"), (not opened), per Quote Investigator |
| Context removed | a method for a preventative program, followed in 1975–78 retellings by "instead of trying to change everyone else" | the slogan on its own | *The San Diego Union*, 1978, where it is a bare motto, (not opened), per Quote Investigator |
| Other: wording changed ("want" became "wish") | "want to see" | "wish to see" | *Los Angeles Times*, 1989, (not opened), per Quote Investigator. Professor Buzzkill quotes Lorrance herself with "wish," so the sources disagree on her exact wording. |

Gandhi's 1913 passage says something related in different words: the world reflects us, so if we change ourselves the world's tendencies change. Quote Investigator and Wikiquote call it the closest verifiable thing Gandhi wrote.

### Status of the root
- No primary found, so there was no status to check.
- Quote Investigator's conclusion is that Lorrance should get the credit for the expression she wrote in 1974.
- The Daily Caller News Foundation rated the Gandhi attribution "False." It quotes Gandhi scholar Johannes Bakker as calling the sentiment Gandhian but doubting it is a direct quote.
- Per Quote Investigator, *The Yale Book of Quotations* reports two things: the Gandhi Institute for Nonviolence has not traced the line to his writings, and the Gandhi family believes he said it.

### Cold trails
None.

### Confidence
Medium: neither the Lorrance text nor Gandhi's 1913 passage could be opened, so both rest on Quote Investigator and other opened secondary sources, and the 1974, 1987 and 1989 dates are *cited by* Quote Investigator.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
