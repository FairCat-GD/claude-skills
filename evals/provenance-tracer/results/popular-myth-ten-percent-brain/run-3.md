---
case: popular-myth-ten-percent-brain
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T19:15:51Z
cost_usd: 1.6354
duration_s: 183
turns: 30
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- Read: <plugin>/skills/provenance-tracer/references/labels.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- WebSearch: "only use 10% of their brains"
- WebSearch: "ten percent of our brain" myth origin
- WebSearch: William James "small part of our possible mental resources" ten percent brain
- WebSearch: "10 percent" brain claim Lowell Thomas Dale Carnegie preface
- WebSearch: who first said humans use only 10 percent of brain earliest
- WebSearch: snopes 10 percent of brain
- WebFetch: https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth
- WebFetch: https://www.snopes.com//fact-check/the-ten-percent-myth/
- WebFetch: https://www.scientificamerican.com/article/do-we-really-use-only-10/
- WebFetch: https://faculty.washington.edu/chudler/tenper.html
- WebFetch (error): http://www.cyberspacei.com/englishwiz/library/friends/how_to_win_friends.htm
- WebFetch: https://en.wikisource.org/wiki/The_Energies_of_Men
- WebSearch: archive.org "How to Win Friends and Influence People" 1936 full text "latent mental ability"
- WebSearch: 1929 World Almanac advertisement "ten percent of our brain power" Pelman OR "Scientists and psychologists tell us"
- WebFetch: https://archive.org/stream/in.ernet.dli.2015.67270/2015.67270.How-To-Win-Friends-And-Influence-People_djvu.txt
- WebSearch: Beyerstein "Whence cometh the myth" 1929 World Almanac advertisement pdf
- WebSearch: archive.org "World Almanac" 1929 full text "NO LIMIT to what the human brain"
- WebFetch: https://www.brainfacts.org/thinking-sensing-and-behaving/thinking-and-awareness/2019/debunked-the-10-percent-brain-myth-061719
- WebFetch: https://skepticalinquirer.org/1999/03/the-ten-percent-myth/
- WebFetch (error): https://web.archive.org/cdx/search/cdx?url=en.wikipedia.org/wiki/Ten_percent_of_the_brain_myth&limit=1
- WebFetch: https://centerforinquiry.s3.amazonaws.com/wp-content/uploads/sites/29/1999/03/22164948/p52.pdf
- WebFetch: https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Humans use only 10% of their brains."

**Roots:** Echo · **Grounding:** Primary differs · Mutated
**Earliest instance found:** a self-help advertisement in *The World Almanac*, 1929 (date from: cited by [Wikipedia](https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth), citing Beyerstein 1999). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 7

### Chain
Your version: "Humans use only 10% of their brains" (where you met it: not given)
 ├─ [Wikipedia, *Ten-percent-of-the-brain myth*](https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth), date unknown, Tertiary → cites
 │   ├─ Barry L. Beyerstein, *Whence Cometh the Myth that We Only Use 10% of our Brains?*, in S. Della Sala (ed.), *Mind Myths* (Wiley), p. 11, 1999, (not opened), per Wikipedia → cites
 │   │   └─ Self-help advertisement, *The World Almanac*, 1929, Primary (not opened, per Wikipedia), root
 │   └─ [Lowell Thomas, *A Short-Cut to Distinction*, foreword to Dale Carnegie, *How to Win Friends and Influence People*](https://archive.org/stream/in.ernet.dli.2015.67270/2015.67270.How-To-Win-Friends-And-Influence-People_djvu.txt), 1936 (byline: copyright 1936, in a later Pocket Book printing), Secondary → credits William James
 │       └─ [William James, *The Energies of Men*](https://en.wikisource.org/wiki/The_Energies_of_Men), 1907 (byline: copyright 1907, *The American Magazine*; 1911 edition), Primary (credited, differs: it says people use only part of their mental and physical *resources*, gives no percentage and says nothing about brain tissue)
 ├─ [Barry L. Beyerstein, *Do we really use only 10 percent of our brains?*, *Scientific American*](https://www.scientificamerican.com/article/do-we-really-use-only-10/), 2004, Secondary → cites
 │   └─ Beyerstein 1999 and Thomas 1936, both drawn above
 └─ [Eric H. Chudler, *Neuroscience For Kids: 10% of the Brain Myth*](https://faculty.washington.edu/chudler/tenper.html), date unknown, Tertiary → cites
     ├─ [Snopes, *The Ten-Percent Myth*](https://www.snopes.com//fact-check/the-ten-percent-myth/), date unknown, (not opened), per Chudler → stopped: not opened (HTTP 402)
     ├─ Beyerstein 1999, drawn above
     └─ credits William James, 1908, p. 12 → *The Energies of Men*, drawn above

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Hedge dropped | ["we use only about TEN PERCENT of our brain power"](https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth) | Humans use only 10% of their brains | [Lowell Thomas, foreword to Carnegie](https://archive.org/stream/in.ernet.dli.2015.67270/2015.67270.How-To-Win-Friends-And-Influence-People_djvu.txt), 1936 |
| Other: capacity read as brain tissue | the ad speaks of *brain power*, a capacity, not of the brain itself | Humans use only 10% of their brains | [Beyerstein, *Scientific American*](https://www.scientificamerican.com/article/do-we-really-use-only-10/), 2004 |

### Status of the root
- The root is a 1929 advertisement, known here only through Wikipedia's citation of Beyerstein (1999). It has no journal page or DOI, so there is no retraction, correction or replication record to check.
- *The Energies of Men* (credited text): an essay, not a study with data, so it has no status record to check. In the opened text, James describes people as working far within their limits, gives no percentage, and does not mention brain tissue.
- Beyerstein (2004, *Scientific American*) traces one line of the story back to William James. He reports that the 1936 Lowell Thomas foreword attributed the 10-percent figure to James. He also writes that later self-help writers shifted *10 percent of our capacity* to *10 percent of our brain*. He found no record of Einstein saying it.
- Wikipedia lists other proposed sources that do not use the 10% figure and that no node here cites as its source: James and Boris Sidis's 1890s reserve-energy ideas, John W. Campbell's 1932 story (which says *half*), Wilder Penfield's stimulation work, and misread early neurology.

### Cold trails
None.

### Confidence
Medium: the root advertisement and Beyerstein's 1999 chapter were not opened, and the 1929 date rests on Wikipedia's citation, though Thomas's 1936 foreword and James's essay were both opened.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
