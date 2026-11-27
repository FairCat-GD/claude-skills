---
case: popular-myth-ten-percent-brain
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:25:23Z
cost_usd: 1.4902
duration_s: 175
turns: 35
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- Read: <plugin>/skills/provenance-tracer/references/labels.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- WebSearch: "use only 10% of their brains"
- WebSearch: "we only use 10 percent of our brain" myth
- WebSearch: William James Lowell Thomas Dale Carnegie 10 percent brain
- WebSearch: "ten percent" brain myth Karl Lashley Wilder Penfield origin
- WebSearch: origin of the "10 percent of the brain" claim earliest first appeared
- WebSearch: snopes 10 percent of brain
- WebFetch: https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth
- WebFetch: https://en.wikipedia.org/wiki/Talk:Ten_percent_of_the_brain_myth
- WebFetch: https://www.scientificamerican.com/article/do-people-only-use-10-percent-of-their-brains/
- WebFetch: https://www.snopes.com//fact-check/the-ten-percent-myth/
- WebFetch: https://en.wikipedia.org/wiki/Talk:Ten_percent_of_the_brain_myth
- WebFetch: https://www.scientificamerican.com/article/do-we-really-use-only-10/
- WebFetch: http://staff.washington.edu/chudler/pdf/tenper.pdf
- WebFetch: https://www.loc.gov/resource/sn90050307/1912-01-10/ed-1/?sp=3
- WebFetch: https://www.loc.gov/resource/sn90050307/1912-01-10/ed-1/?sp=3&st=text
- WebFetch: https://www.gutenberg.org/files/26217/26217-h/26217-h.htm
- WebFetch: https://chroniclingamerica.loc.gov/lccn/sn90050307/1912-01-10/ed-1/seq-3/ocr/
- WebFetch: https://psychclassics.yorku.ca/James/energies.htm
- WebSearch: "How to Win Friends" Lowell Thomas "A Shortcut to Distinction" "ten percent of his latent mental ability"
- WebFetch: https://www.loc.gov/chroniclingamerica/lccn/sn90050307/1912-01-10/ed-1/seq-3/ocr/
- WebFetch (error): http://www.cyberspacei.com/englishwiz/library/friends/how_to_win_friends.htm
- WebFetch (error): https://web.archive.org/web/2011/http://www.cyberspacei.com/englishwiz/library/friends/how_to_win_friends.htm
- WebSearch: archive.org "How to win friends and influence people" 1936 full text "Lowell Thomas"
- WebFetch: https://archive.org/stream/in.ernet.dli.2015.67270/2015.67270.How-To-Win-Friends-And-Influence-People_djvu.txt
- WebSearch: "ten per cent of his brain power" James 1912 advertisement commercial college
- WebFetch: https://api.crossref.org/works/10.1126/science.25.635.321
- WebFetch: https://www.bps.org.uk/psychologist/great-myths-brain-we-only-use-10-cent

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Humans use only 10% of their brains."

**Roots:** Echo · **Grounding:** Primary differs · Mutated
**Earliest instance found:** a display ad signed Tyler Commercial College, *The Prescott Daily News*, 10 January 1912, p. 3, (not opened), per the [Wikipedia talk page](https://en.wikipedia.org/wiki/Talk:Ten_percent_of_the_brain_myth) (date from: cited by that talk page). The earliest opened instance with the 10% figure is Lowell Thomas, 1936. Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 11

### Chain
Your version: "Humans use only 10% of their brains" (where you met it: not given)
 ├─ [Wikipedia, *Ten-percent-of-the-brain myth*](https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth), date unknown, Tertiary → cites
 │   └─ [Lowell Thomas, *A Short-Cut to Distinction*, preface to Dale Carnegie, *How to Win Friends and Influence People*](https://archive.org/stream/in.ernet.dli.2015.67270/2015.67270.How-To-Win-Friends-And-Influence-People_djvu.txt), 1936, Secondary: "the average man develops only ten per cent of his latent mental ability" → cites
 │       └─ [William James, *The Energies of Men*, *Science* 25(635)](https://psychclassics.yorku.ca/James/energies.htm), 1907, Primary: "only a small part of our possible mental and physical resources"
 ├─ [Barry L. Beyerstein, *Scientific American*](https://www.scientificamerican.com/article/do-we-really-use-only-10/), 2004, Secondary → cites Thomas 1936 and James 1907 (above)
 ├─ [Robynne Boyd, *Scientific American*](https://www.scientificamerican.com/article/do-people-only-use-10-percent-of-their-brains/), 2008, Secondary → cites James 1907 (above)
 ├─ [Christian Jarrett, *The Psychologist* (BPS)](https://www.bps.org.uk/psychologist/great-myths-brain-we-only-use-10-cent), 2014, Tertiary → cites Thomas 1936 (above)
 └─ [Wikipedia talk page, *Talk:Ten-percent-of-the-brain myth*](https://en.wikipedia.org/wiki/Talk:Ten_percent_of_the_brain_myth), 2026, Tertiary: quotes the ad as "the average man only uses ten per cent of his brain power". The post is dated 17 October 2026, and a reply on the page says a self-declared AI agent posted it → cites
     ├─ Tyler Commercial College ad, [*The Prescott Daily News*](https://www.loc.gov/resource/sn90050307/1912-01-10/ed-1/?sp=3), 1912, (not opened), per the talk page; the Library of Congress returned 403 → cites "the late Prof. James" → stopped: not opened
     └─ Moberly Commercial College ad, *Laclede Blade*, 12 January 1912, (not opened), per the talk page; same wording → stopped: not opened

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Number changed | "a small part" of our resources, with no figure ([James](https://psychclassics.yorku.ca/James/energies.htm)) | only 10% | Tyler Commercial College ad, 1912, (not opened), per the [talk page](https://en.wikipedia.org/wiki/Talk:Ten_percent_of_the_brain_myth). Earliest opened: [Thomas](https://archive.org/stream/in.ernet.dli.2015.67270/2015.67270.How-To-Win-Friends-And-Influence-People_djvu.txt), 1936 |
| Other: unused potential restated as unused brain | mental and physical resources, or energies; James does not describe the brain as tissue | their brains | Tyler Commercial College ad, 1912 ("brain power"), (not opened), per the [talk page](https://en.wikipedia.org/wiki/Talk:Ten_percent_of_the_brain_myth). [Beyerstein](https://www.scientificamerican.com/article/do-we-really-use-only-10/) credits the move from "capacity" to "brain" to later "positive thinking" writers |

### Status of the root
- [Crossref record](https://api.crossref.org/works/10.1126/science.25.635.321) for James 1907: no update, retraction or correction entries. The journal page, Retraction Watch and PubPeer were not checked.
- [Beyerstein (2004)](https://www.scientificamerican.com/article/do-we-really-use-only-10/) reports that James never gave a percentage, and that Thomas's 1936 preface tied the 10-percent figure to James.
- [Beyerstein (2004)](https://www.scientificamerican.com/article/do-we-really-use-only-10/) reports that the Albert Einstein Archives found no record of the version credited to Einstein. [Jarrett (2014)](https://www.bps.org.uk/psychologist/great-myths-brain-we-only-use-10-cent) says the same. Other origins these sources propose, such as Penfield's "silent cortex" work and misreadings of early brain research, are offered as contributing ideas. No chain traced here runs back to them.

### Cold trails
- 1929 *World Almanac* advertisement, (not opened), per [Wikipedia](https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth), which cites Beyerstein (1999) in *Mind Myths*. It credits unnamed "scientists and psychologists".
- Pelman Institute newspaper advert, 1944, (not opened), per [Jarrett (2014)](https://www.bps.org.uk/psychologist/great-myths-brain-we-only-use-10-cent), which reports the ad's "one-tenth of your real brain-power" wording.

### Confidence
Medium: the root (James 1907) and the 1936 Thomas link were opened and dated from their bylines, but the earliest instance found (the 1912 ads) was not opened, and the only source for it is an unreviewed talk-page post by a self-declared AI agent.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
