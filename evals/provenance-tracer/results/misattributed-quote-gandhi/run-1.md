---
case: misattributed-quote-gandhi
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-26T12:17:02Z
cost_usd: 1.5034
duration_s: 208
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
- WebSearch: "be the change you wish to see in the world" Gandhi
- WebSearch: "If we could change ourselves, the tendencies in the world would also change" Gandhi
- WebSearch: Gandhi "be the change" Indian Opinion 1913 original text
- WebSearch: "be the change you want to see" earliest Arleen Lorrance 1974
- WebSearch: origin of "be the change you wish to see in the world" who first said
- WebSearch: quoteinvestigator.com "be the change" Gandhi
- WebFetch: https://quoteinvestigator.com/2017/10/23/be-change/
- WebFetch: https://dailycaller.com/2019/12/06/fact-check-mahatma-gandhi-change-wish-see-world/
- WebFetch: https://www.brainyquote.com/quotes/mahatma_gandhi_109075
- WebSearch: Collected Works of Mahatma Gandhi volume 12 "Snake-Bite" "We but mirror the world" pdf
- WebFetch: https://professorbuzzkill.com/2017/01/09/gandhi-be-the-change-you-wish-to-see-in-the-world/
- WebFetch: https://listserv.linguistlist.org/pipermail/ads-l/2017-October/149775.html
- WebFetch: https://www.gandhiashramsevagram.org/gandhi-literature/mahatma-gandhi-collected-works-volume-13.pdf
- WebFetch: https://dokumen.pub/the-complete-works-of-mahatma-gandhi-volume-13-13.html
- WebSearch: "If we could change ourselves, the tendencies in the world would also change" archive.org OR wikisource collected works
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28collected+works+of+mahatma+gandhi%29&fl[]=identifier&fl[]=title&rows=120&output=json
- WebFetch: https://archive.org/stream/in.ernet.dli.2015.32787/2015.32787.Collected-Works_djvu.txt
- WebFetch: https://archive.org/download/in.ernet.dli.2015.32787/2015.32787.Collected-Works_djvu.txt
- WebFetch: https://dn710806.ca.archive.org/0/items/in.ernet.dli.2015.32787/2015.32787.Collected-Works_djvu.txt
- WebFetch: https://archive.org/metadata/in.ernet.dli.2015.32787/files
- WebFetch: https://archive.org/download/in.ernet.dli.2015.32787/2015.32787.Collected-Works-Of-Mahatma-Gandhi--Vol12_djvu.txt
- WebFetch: https://dn710806.ca.archive.org/0/items/in.ernet.dli.2015.32787/2015.32787.Collected-Works-Of-Mahatma-Gandhi--Vol12_djvu.txt
- WebFetch: https://dn710806.ca.archive.org/0/items/in.ernet.dli.2015.32787/2015.32787.Collected-Works-Of-Mahatma-Gandhi--Vol12_djvu.txt
- WebFetch: https://dn710806.ca.archive.org/0/items/in.ernet.dli.2015.32787/2015.32787.Collected-Works-Of-Mahatma-Gandhi--Vol12_djvu.txt
- WebFetch: https://josephranseth.com/gandhi-didnt-say-be-the-change-you-want-to-see-in-the-world/

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Gandhi said: be the change you wish to see in the world."

**Roots:** Echo · **Grounding:** No primary found · Mutated · Misattributed
**Earliest instance found:** Arleen Lorrance, *The Love Project*, a chapter in *Developing Priorities and a Style* (ed. Richard D. Kellough), p. 85, 1974 (date from: cited by [Quote Investigator](https://quoteinvestigator.com/2017/10/23/be-change/)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 10

### Chain
Your version: "Gandhi said: be the change you wish to see in the world" (where you met it: not given)
 ├─ [Quote Investigator, *Quote Origin: Be the Change You Wish To See in the World*](https://quoteinvestigator.com/2017/10/23/be-change/), 2017, Secondary → cites
 │   ├─ Rita Gillmon, *The San Diego Union*, 1978 – Denise Kusel, *Santa Fe New Mexican*, 22 Mar 1987 (the earliest attribution to Gandhi QI found, as "You must be the change you want to see in the world"), (not opened), per Quote Investigator → stopped: not opened
 │   ├─ Pamela Galloway, *Reno Evening Gazette*, 30 Jun 1975, gives the line as a local minister's motto, (not opened), per Quote Investigator → cites
 │   │   └─ Lorrance, *The Love Project*, 1974 (below)
 │   ├─ Arleen Lorrance, *The Love Project*, in *Developing Priorities and a Style*, p. 85, 1974, Primary (not opened, per Quote Investigator), **root**
 │   └─ Gandhi, *General Knowledge About Health XXXII: Accidents: Snake-Bite*, *Indian Opinion*, 9 Aug 1913, in *Collected Works* Vol. XII, p. 158, 1913, Primary (not opened, per Quote Investigator). This is a thematic precursor and does not contain the slogan's words. [A scan labelled Vol. 12](https://dn710806.ca.archive.org/0/items/in.ernet.dli.2015.32787/2015.32787.Collected-Works-Of-Mahatma-Gandhi--Vol12_djvu.txt) opened, but its text is from 1937 volumes → stopped: not opened
 ├─ [Garson O'Toole, ADS-L post *Gandhi-Attributed Quote*](https://listserv.linguistlist.org/pipermail/ads-l/2017-October/149775.html), 2017, Secondary → cites
 │   ├─ Robert K. Cooper, health and fitness book crediting Gandhi with "You must be the change you wish to see in the world", 1989, (not opened), per ADS-L → stopped: not opened
 │   ├─ *Los Angeles Times*, 30 Jul 1989, "We must be the change we wish to see in the world", (not opened), per ADS-L and Quote Investigator → stopped: not opened
 │   └─ Lorrance, 1974, Primary (not opened, per ADS-L), the same root
 ├─ [Professor Buzzkill (Joseph Coohill)](https://professorbuzzkill.com/2017/01/09/gandhi-be-the-change-you-wish-to-see-in-the-world/), 2017, Secondary → cites
 │   ├─ Lorrance, 1974, Primary (not opened), the same root
 │   └─ Gandhi, *Indian Opinion*, 1913, cited as *Collected Works* vol. 13, ch. 153, p. 241, Primary (not opened, per Professor Buzzkill)
 └─ [Joseph Ranseth, *Gandhi didn't actually ever say…*](https://josephranseth.com/gandhi-didnt-say-be-the-change-you-want-to-see-in-the-world/), 2015, Tertiary → cites
     └─ Gandhi 1913 passage. The citation appears only in a 2017 author comment, as *Collected Works* vol. 13, ch. 153, p. 241, (not opened), per Ranseth

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Context removed | One way to start a "preventative program" in a Brooklyn school's Love Project is to "be the change you wish to see happen" ([ADS-L](https://listserv.linguistlist.org/pipermail/ads-l/2017-October/149775.html)) | a standalone motto | *Reno Evening Gazette*, 1975 (not opened, per [Quote Investigator](https://quoteinvestigator.com/2017/10/23/be-change/)) |
| Scope widened | "…to see happen" | "…to see in the world" | *Santa Fe New Mexican*, 1987 (not opened, per Quote Investigator) |
| Attribution shifted | written by Arleen Lorrance, in her own chapter | "Gandhi said" | *Santa Fe New Mexican*, 1987 (not opened, per Quote Investigator) |
| Other: wording "want" → "wish" | Quote Investigator gives "want to see happen", while ADS-L and Professor Buzzkill give "wish to see happen" | "wish to see in the world" | sources differ on the root's own word. "Wish… in the world" is in the 1989 Cooper book and *LA Times* (not opened, per ADS-L) |
| Other: compared with Gandhi's 1913 precursor, a conditional became a command | "If we could change ourselves, the tendencies in the world would also change" ([Professor Buzzkill](https://professorbuzzkill.com/2017/01/09/gandhi-be-the-change-you-wish-to-see-in-the-world/), quoting *Indian Opinion*) | "be the change…" | Quote Investigator calls the modern saying more concise and forceful than the 1913 passage |

### Status of the root
- The root is a 1974 book chapter. I didn't open it, and it has no journal page or DOI, so there was no retraction or correction record to check.
- Quote Investigator, after weighing the 1913 passage and the later citations, concludes: ["QI believes Arleen Lorrance should receive credit for the expression she wrote 1974."](https://quoteinvestigator.com/2017/10/23/be-change/) It also cites the *Yale Book of Quotations* (2006). That book reports that the Gandhi Institute for Nonviolence could not trace the line in Gandhi's writings, and that Gandhi's family believes he said it in conversation.
- Gandhi's 1913 passage (another Primary): sources give different locations for it. [Quote Investigator](https://quoteinvestigator.com/2017/10/23/be-change/) cites *Collected Works* Vol. XII (1964), pp. 156–158. [Professor Buzzkill](https://professorbuzzkill.com/2017/01/09/gandhi-be-the-change-you-wish-to-see-in-the-world/) and [Ranseth](https://josephranseth.com/gandhi-didnt-say-be-the-change-you-want-to-see-in-the-world/) cite vol. 13, ch. 153, p. 241. All three date it to *Indian Opinion*, 9 August 1913, and Quote Investigator says it was translated from Gujarati.

### Cold trails
None.

### Confidence
Medium: the chain back to the root was opened through Quote Investigator, ADS-L and Professor Buzzkill, which agree on it, but neither the 1974 chapter nor Gandhi's 1913 text could be opened. The Daily Caller fact-check and the BrainyQuote page both returned 403, and the root's date rests on *cited by*.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
