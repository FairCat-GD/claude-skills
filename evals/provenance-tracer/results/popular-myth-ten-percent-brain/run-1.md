---
case: popular-myth-ten-percent-brain
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T19:12:45Z
cost_usd: 1.8533
duration_s: 183
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
- WebSearch: "use only 10 percent of their brains"
- WebSearch: "10 percent of the brain" myth origin William James Lowell Thomas
- WebSearch: origin of "ten percent of the brain" earliest
- WebSearch: "ten percent of our brains" quote investigator OR snopes
- WebSearch: William James "The Energies of Men" "small part of our possible mental"
- WebSearch: Lowell Thomas preface Dale Carnegie "How to Win Friends" "only ten percent" latent mental ability
- WebFetch: https://www.scientificamerican.com/article/do-people-only-use-10-percent-of-their-brains/
- WebFetch: https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth
- WebFetch: https://www.snopes.com//fact-check/the-ten-percent-myth/
- WebFetch: https://psychclassics.yorku.ca/James/energies.htm
- WebSearch: archive.org "How to Win Friends and Influence People" 1936 full text "A Shortcut to Distinction" Lowell Thomas
- WebSearch: 1929 World Almanac advertisement "ten percent of our brain power" Pelman OR "Pelmanism"
- WebSearch: "ten per cent" brain James Sidis 1907 newspaper "per cent of" brain earliest use myth history
- WebFetch: https://en.wikipedia.org/wiki/Talk:Ten_percent_of_the_brain_myth
- WebFetch: https://ia801007.us.archive.org/34/items/Howtowin/Howtowin.pdf
- WebFetch: https://en.wikipedia.org/wiki/Talk:Ten_percent_of_the_brain_myth
- WebFetch: https://archive.org/stream/Howtowin/Howtowin_djvu.txt
- WebFetch: https://www.loc.gov/resource/sn90050307/1912-01-10/ed-1/?sp=3
- WebFetch: https://chroniclingamerica.loc.gov/lccn/sn90050307/1912-01-10/ed-1/seq-3/ocr/
- WebFetch: https://www.loc.gov/chroniclingamerica/lccn/sn90050307/1912-01-10/ed-1/seq-3/ocr/
- WebSearch: "uses ten per cent of his brain power" James Harvard 1912
- WebSearch: "ten per cent of his brain power" OR "ten per cent of their brain power" commercial college advertisement
- WebFetch: https://cdn.centerforinquiry.org/wp-content/uploads/sites/29/1999/03/22164948/p52.pdf
- WebFetch: https://www.mail-archive.com/tips@fre.fsu.umd.edu/msg02481.html
- WebFetch: https://www.bps.org.uk/psychologist/great-myths-brain-we-only-use-10-cent
- WebSearch: archive.org "World Almanac" 1929 full text "NO LIMIT to what the human brain can accomplish"

## Reply

**Assumptions** (no reply was possible, so I asked nothing):
- The claim's text went into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Humans use only 10% of their brains."

**Roots:** Echo · **Grounding:** Primary differs · Mutated
**Earliest instance found:** a Tyler Commercial College advertisement in *The Prescott Daily News* (Arkansas), 10 January 1912, p. 3 ([link tried](https://www.loc.gov/resource/sn90050307/1912-01-10/ed-1/?sp=3)), 1912 (date from: cited by [Wikipedia talk page](https://en.wikipedia.org/wiki/Talk:Ten_percent_of_the_brain_myth)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 10

### Chain
Your version: "Humans use only 10% of their brains" (where you met it: not given)
 ├─ [Wikipedia, *Ten-percent-of-the-brain myth*](https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth), date unknown, Secondary → cites
 │   ├─ *The World Almanac* self-help advertisement, 1929, (not opened), per Wikipedia (via Beyerstein, *Mind Myths*, 1999) → stopped: not opened
 │   └─ [Lowell Thomas, foreword *A Shortcut to Distinction*, in Carnegie, *How to Win Friends and Influence People*](https://archive.org/stream/Howtowin/Howtowin_djvu.txt), 1936, Secondary → credits William James
 │       └─ [William James, *The Energies of Men*, *Science* 25:321–332](https://psychclassics.yorku.ca/James/energies.htm), 1907, Primary (credited, differs)
 ├─ [Christian Jarrett, *Great myths of the brain: We only use 10 per cent*, BPS *The Psychologist*](https://www.bps.org.uk/psychologist/great-myths-brain-we-only-use-10-cent), 2014, Secondary → cites the Thomas foreword (above)
 ├─ [Robynne Boyd, *Do People Only Use 10 Percent of Their Brains?*, *Scientific American*](https://www.scientificamerican.com/article/do-people-only-use-10-percent-of-their-brains/), 2008, Secondary → credits James (above)
 ├─ [Jeff Ricker, TIPS mailing list post](https://www.mail-archive.com/tips@fre.fsu.umd.edu/msg02481.html), 1999, Tertiary → cites
 │   └─ Lewis, 1962, as quoted in Higbee & Clay (1998), (not opened), per Ricker → stopped: not opened
 └─ [Wikipedia talk page, section *Earliest documented source: 1912 newspaper advertisement*](https://en.wikipedia.org/wiki/Talk:Ten_percent_of_the_brain_myth), 2026, Secondary → cites
     ├─ [*The Prescott Daily News*, Tyler Commercial College ad](https://www.loc.gov/resource/sn90050307/1912-01-10/ed-1/?sp=3), 1912, Primary (not opened, per Wikipedia talk page), root
     └─ *Laclede Blade* (Missouri), Moberly Commercial College ad with the same wording, 1912, (not opened), per Wikipedia talk page → stopped: not opened

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Other: *brain power* became the brain itself | ["the average man only uses ten per cent of his brain power"](https://en.wikipedia.org/wiki/Talk:Ten_percent_of_the_brain_myth) (as transcribed on the talk page) | Humans use only 10% of their brains | [Scientific American](https://www.scientificamerican.com/article/do-people-only-use-10-percent-of-their-brains/), 2008 |
| Scope widened | the *average man* | Humans use only 10% of their brains | [Scientific American](https://www.scientificamerican.com/article/do-people-only-use-10-percent-of-their-brains/), 2008 |
| Context removed | a business college's advertising copy that credits the figure to the late Prof. James of Harvard | Humans use only 10% of their brains | your version |

### Status of the root
- The root is an advertisement, not a study, so no retraction or replication checks apply. Its page scan returned HTTP 403 when fetched through both the [loc.gov resource](https://www.loc.gov/resource/sn90050307/1912-01-10/ed-1/?sp=3) and the Chronicling America OCR address, so its wording rests only on the talk-page transcription.
- On the [Wikipedia talk page](https://en.wikipedia.org/wiki/Talk:Ten_percent_of_the_brain_myth), another editor noted on 17 October 2026 that the 1912 comment had been posted by a self-declared AI agent. It is not yet in the article.
- William James (credited text): in the [1907 essay](https://psychclassics.yorku.ca/James/energies.htm), James says people use only a small part of their mental and physical resources. The passage gives no percentage and does not mention the brain.
- Lowell Thomas foreword: the [opened text](https://archive.org/stream/Howtowin/Howtowin_djvu.txt) is signed 1936 but comes from an edition that says *First Published in 1937*. It credits James with saying people develop 10 percent of their *latent mental ability*, not their brain.
- [BPS *The Psychologist*](https://www.bps.org.uk/psychologist/great-myths-brain-we-only-use-10-cent) dates the claim's use in advertising to the Pelman Institute in 1944. It also reports that the Albert Einstein Archives could not locate the Einstein attribution.

### Cold trails
None.

### Confidence
Low: no page opened in this trace states a percentage of the brain before 2008, the 1912 root and the 1929 almanac ad come only through pages that cite them, and the [Snopes page](https://www.snopes.com//fact-check/the-ten-percent-myth/) (HTTP 402) and the 1999 *Skeptical Inquirer* PDF (no readable text) could not be opened.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
