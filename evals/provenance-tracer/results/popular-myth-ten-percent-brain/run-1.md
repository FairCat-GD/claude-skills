---
case: popular-myth-ten-percent-brain
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:28:26Z
cost_usd: 1.8377
duration_s: 252
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
- WebSearch: "use only 10% of their brains"
- WebSearch: "ten percent of our brain" myth
- WebSearch: William James Lowell Thomas Dale Carnegie 10 percent brain
- WebSearch: "10 percent" brain claim origin
- WebSearch: origin of "10 percent of the brain" who first said earliest
- WebSearch: 10 percent of brain snopes OR "quote investigator"
- WebFetch: https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth
- WebFetch: https://en.wikipedia.org/wiki/Talk:Ten_percent_of_the_brain_myth
- WebFetch: https://www.scientificamerican.com/article/do-people-only-use-10-percent-of-their-brains/
- WebFetch: https://www.snopes.com//fact-check/the-ten-percent-myth/
- WebFetch: https://en.wikipedia.org/wiki/Talk:Ten_percent_of_the_brain_myth
- WebFetch (error): https://web.archive.org/web/20110515143209/http://www.cyberspacei.com/englishwiz/library/friends/how_to_win_friends.htm
- WebFetch: https://www.scientificamerican.com/article/do-we-really-use-only-10/
- WebFetch: https://www.loc.gov/resource/sn90050307/1912-01-10/ed-1/?sp=3
- WebSearch: "Energies of Men" William James 1907 full text "small part of our possible mental and physical resources"
- WebSearch: "develops only ten per cent of his latent mental ability" Lowell Thomas "How to Win Friends" archive.org
- WebFetch: https://ia601400.us.archive.org/23/items/in.ernet.dli.2015.67270/2015.67270.How-To-Win-Friends-And-Influence-People_text.pdf
- WebFetch: https://psychclassics.yorku.ca/James/energies.htm
- WebSearch: "ten per cent of his brain power" "Prof. James" 1912 chroniclingamerica
- WebSearch: "we use only about ten percent of our brain power" 1929 World Almanac advertisement
- WebFetch: https://chroniclingamerica.loc.gov/lccn/sn90050307/1912-01-10/ed-1/seq-3/ocr/
- WebFetch: https://archive.org/metadata/in.ernet.dli.2015.67270
- WebFetch: https://www.psychologytoday.com/us/blog/modern-minds/201803/why-do-we-only-use-10-percent-of-the-brain
- WebFetch: https://www.loc.gov/chroniclingamerica/lccn/sn90050307/1912-01-10/ed-1/seq-3/ocr/
- WebFetch: https://ia801400.us.archive.org/23/items/in.ernet.dli.2015.67270/2015.67270.How-To-Win-Friends-And-Influence-People_djvu.txt
- WebSearch: "TEN PERCENT of our brain power" "World Almanac" 1929 archive.org

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Humans use only 10% of their brains."

**Roots:** Echo · **Grounding:** Primary differs · Mutated
**Earliest instance found:** [Tyler Commercial College advertisement, *The Prescott Daily News*, p. 3](https://www.loc.gov/resource/sn90050307/1912-01-10/ed-1/?sp=3), 1912 (date from: cited by [Wikipedia talk page](https://en.wikipedia.org/wiki/Talk:Ten_percent_of_the_brain_myth)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 9

### Chain
Your version: "Humans use only 10% of their brains" (where you met it: not given)
 ├─ [*Do People Only Use 10 Percent of Their Brains?*, Scientific American (Robynne Boyd)](https://www.scientificamerican.com/article/do-people-only-use-10-percent-of-their-brains/), 2008, Secondary → credits William James
 │   └─ [William James, *The Energies of Men*, Science N.S. 25](https://psychclassics.yorku.ca/James/energies.htm), 1907, Primary (credited, differs)
 ├─ [*Ten-percent-of-the-brain myth*, Wikipedia](https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth), date unknown, Tertiary → cites
 │   ├─ [Lowell Thomas, *A Short-Cut to Distinction*, foreword to Dale Carnegie's *How to Win Friends and Influence People*](https://ia801400.us.archive.org/23/items/in.ernet.dli.2015.67270/2015.67270.How-To-Win-Friends-And-Influence-People_djvu.txt), 1936, Secondary → credits William James (credits James with saying the average man develops only ten per cent of his *latent mental ability*)
 │   │   └─ James, *The Energies of Men*, 1907: the same credited text as above
 │   └─ Barry Beyerstein, *Whence Cometh the Myth that We Only Use 10% of our Brains?*, in *Mind Myths* (Wiley), 1999, (not opened), per Wikipedia → cites
 │       └─ Self-help advertisement, *World Almanac*, 1929, (not opened), per Wikipedia → stopped: not opened
 ├─ [*Do we really use only 10 percent of our brains?*, Scientific American (Barry Beyerstein)](https://www.scientificamerican.com/article/do-we-really-use-only-10/), 2004, Secondary → cites
 │   └─ Lowell Thomas foreword, 1936: the same node as above
 ├─ [*Why Do We Only Use 10 Percent of the Brain?*, Psychology Today (Kevin Bennett)](https://www.psychologytoday.com/us/blog/modern-minds/201803/why-do-we-only-use-10-percent-of-the-brain), date unknown, Tertiary → cites
 │   └─ *World Almanac* advertisement, 1929: the same node as above
 └─ [*Talk: Ten-percent-of-the-brain myth*, section on a 1912 newspaper advertisement, Wikipedia](https://en.wikipedia.org/wiki/Talk:Ten_percent_of_the_brain_myth), 2026, Tertiary → cites
     └─ [Tyler Commercial College advertisement, *The Prescott Daily News* (Arkansas), 10 January 1912, p. 3](https://www.loc.gov/resource/sn90050307/1912-01-10/ed-1/?sp=3), 1912, (not opened), per Wikipedia talk page, root → credits William James
         └─ James, *The Energies of Men*, 1907: the same credited text as above

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Number changed | James gives no figure: [we use "only a small part of our possible mental and physical resources"](https://psychclassics.yorku.ca/James/energies.htm) | Humans use only 10% of their brains | [Prescott Daily News advertisement](https://www.loc.gov/resource/sn90050307/1912-01-10/ed-1/?sp=3), 1912 |
| Other: what is underused moved from mental and physical *resources* and *powers* to the brain | James's essay never uses the word *brain*. It speaks of powers people habitually leave unused | Humans use only 10% of their brains | [Prescott Daily News advertisement](https://www.loc.gov/resource/sn90050307/1912-01-10/ed-1/?sp=3), 1912 |
| Context removed | James argues that people habitually live within their limits, and that effort or excitement can draw on reserves they fail to use | Humans use only 10% of their brains | [Prescott Daily News advertisement](https://www.loc.gov/resource/sn90050307/1912-01-10/ed-1/?sp=3), 1912 |

### Status of the root
- No primary found at the root: the 1912 advertisement was not opened, so there was no status to check.
- James, *The Energies of Men*: the [opened text](https://psychclassics.yorku.ca/James/energies.htm) is a 1906 address printed in *Science* in 1907. It gives no percentage and does not use the word *brain*.
- James, *The Energies of Men*, per [Scientific American (Beyerstein, 2004)](https://www.scientificamerican.com/article/do-we-really-use-only-10/): James never gave a percentage and never linked potential to an amount of brain tissue. The article says Thomas's 1936 preface gave the idea its biggest boost.
- Wikipedia talk page, per [the same page](https://en.wikipedia.org/wiki/Talk:Ten_percent_of_the_brain_myth): a second editor noted that the 1912 advertisement comment was posted by a self-declared AI agent. The comment also reports the same wording in a *Laclede Blade* (Missouri) advertisement of 12 January 1912. That advertisement was not opened.

### Cold trails
- *World Almanac* self-help advertisement, 1929, (not opened), per [Wikipedia](https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth): it credits unnamed scientists and psychologists with the ten-percent-of-brain-power figure and names no source.

### Confidence
Medium: the root, a 1912 advertisement, was not opened because the Library of Congress refused both fetches of the scan, and its date and wording rest on one Wikipedia talk-page comment; the 1929 advertisement is also known only through retellings, and the Snopes page refused the fetch.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
