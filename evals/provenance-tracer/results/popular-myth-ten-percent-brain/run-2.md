---
case: popular-myth-ten-percent-brain
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:28:50Z
cost_usd: 1.6310
duration_s: 181
turns: 31
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
- WebSearch: "ten percent of the brain" myth
- WebSearch: William James Boris Sidis "latent mental energy" 10 percent brain Lowell Thomas Carnegie preface
- WebSearch: "10 percent" brain myth Lashley Penfield silent cortex
- WebSearch: origin of the 10 percent of brain myth who first said
- WebSearch: 10% brain myth Snopes OR Scientific American OR Beyerstein
- WebFetch: https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth
- WebFetch: https://www.scientificamerican.com/article/do-we-really-use-only-10/
- WebFetch: https://www.discovermagazine.com/the-10-percent-of-your-brain-myth-that-just-wont-die-42817
- WebFetch: https://www.snopes.com/fact-check/the-ten-percent-myth/
- WebFetch: https://psychclassics.yorku.ca/James/energies.htm
- WebFetch: https://www.bps.org.uk/psychologist/great-myths-brain-we-only-use-10-cent
- WebSearch: "World Almanac" 1929 advertisement "ten percent of our brain power" Pelman OR "Scientists and psychologists tell us"
- WebSearch: "used to say that the average man develops only ten percent of his latent mental ability" archive.org
- WebSearch: "we use only about ten percent of our brain power" World Almanac 1929 archive.org
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28how+to+win+friends+and+influence+people%29+AND+date%3A%5B1936-01-01+TO+1940-12-31%5D&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=date&rows=20&output=json
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28world+almanac%29+AND+year%3A1929&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=date&rows=20&output=json
- WebFetch: https://archive.org/metadata/world-almanac-and-book-of-facts_1929
- WebFetch: https://archive.org/metadata/how-to-win-friends_202311
- WebFetch: https://ia600507.us.archive.org/13/items/world-almanac-and-book-of-facts_1929/world-almanac-and-book-of-facts_1929_djvu.txt
- WebFetch: https://ia800502.us.archive.org/23/items/how-to-win-friends_202311/How%20to%20win%20friends_djvu.txt
- WebFetch: https://ia600507.us.archive.org/13/items/world-almanac-and-book-of-facts_1929/world-almanac-and-book-of-facts_1929_djvu.txt
- WebFetch: https://www.psychologytoday.com/us/blog/consciousness-and-the-brain/201106/do-we-use-only-10-percent-our-brain

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Humans use only 10% of their brains."

**Roots:** Echo · **Grounding:** Primary differs · Mutated
**Earliest instance found:** [Pelman Institute of America advertisement, *The World Almanac and Book of Facts 1929*](https://ia600507.us.archive.org/13/items/world-almanac-and-book-of-facts_1929/world-almanac-and-book-of-facts_1929_djvu.txt), 1929 (date from: byline). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 10

### Chain
Your version: "Humans use only 10% of their brains" (where you met it: not given)
 └─ [Wikipedia, *Ten-percent-of-the-brain myth*](https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth), date unknown, Tertiary → cites
     ├─ Barry L. Beyerstein, *Whence cometh the myth that we only use ten percent of our brains?*, in *Mind Myths* (Wiley), 1999, (not opened), per Wikipedia → cites
     │   └─ [Pelman Institute of America advertisement, *The World Almanac and Book of Facts 1929*](https://ia600507.us.archive.org/13/items/world-almanac-and-book-of-facts_1929/world-almanac-and-book-of-facts_1929_djvu.txt), 1929, Primary, root
     ├─ [Lowell Thomas, *A Shortcut to Distinction*, in Dale Carnegie, *How to Win Friends and Influence People*](https://ia800502.us.archive.org/23/items/how-to-win-friends_202311/How%20to%20win%20friends_djvu.txt), 1936, Secondary → credits William James
     │   └─ [William James, *The Energies of Men*, *Science*](https://psychclassics.yorku.ca/James/energies.htm), 1907, Primary (credited, differs)
     └─ [Ezequiel Morsella, *Do we use only 10 percent of our brain?*, Psychology Today](https://www.psychologytoday.com/us/blog/consciousness-and-the-brain/201106/do-we-use-only-10-percent-our-brain), 2011, Secondary → credits Wilder Penfield
         └─ Wilder Penfield's brain-stimulation studies, date unknown, Primary (not opened, per Psychology Today) → stopped: not opened
 └─ [Barry L. Beyerstein, *Do we really use only 10 percent of our brains?*, Scientific American](https://www.scientificamerican.com/article/do-we-really-use-only-10/), 2004, Tertiary → cites
     ├─ Lowell Thomas, 1936 (drawn above)
     └─ Beyerstein, *Mind Myths* chapter, 1999 (drawn above)
 └─ [Christian Jarrett, *Great myths of the brain: We only use 10 per cent*, The Psychologist (BPS)](https://www.bps.org.uk/psychologist/great-myths-brain-we-only-use-10-cent), 2014, Tertiary → cites
     ├─ Lowell Thomas, 1936 (drawn above)
     └─ Pelman Institute newspaper advertisement, 1944, (not opened), per BPS (citing Christopher Wanjek) → stopped: not opened
 └─ [Avery Hurt, *The 10-Percent-of-Your-Brain Myth That Just Won't Die*, Discover](https://www.discovermagazine.com/the-10-percent-of-your-brain-myth-that-just-wont-die-42817), 2021, Secondary → cites
     └─ William James, 1907 (drawn above)

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Other: a share of mental capacity became a share of the brain itself | ["we use only about TEN PER CENT of our mental power"](https://ia600507.us.archive.org/13/items/world-almanac-and-book-of-facts_1929/world-almanac-and-book-of-facts_1929_djvu.txt) | Humans use only 10% of their brains | [Scientific American](https://www.scientificamerican.com/article/do-we-really-use-only-10/), 2004 |
| Hedge dropped | the ad gives roughly ten per cent (*about*) | Humans use only 10% of their brains | [Lowell Thomas, in Carnegie](https://ia800502.us.archive.org/23/items/how-to-win-friends_202311/How%20to%20win%20friends_djvu.txt), 1936 |
| Context removed | a mail-order mind-training advert that credits unnamed scientists and psychologists | Humans use only 10% of their brains | [Lowell Thomas, in Carnegie](https://ia800502.us.archive.org/23/items/how-to-win-friends_202311/How%20to%20win%20friends_djvu.txt), 1936 |

### Status of the root
- The root is an advertisement, not a paper. It has no journal page, Crossref record, Retraction Watch entry or PubPeer entry to check. It credits only unnamed scientists and psychologists, so it gives no earlier source to follow.
- William James, *The Energies of Men* (1907): Lowell Thomas credits this text with the 10% figure. Read in full, it gives no percentage and never mentions the brain in this sense. Its point is that we use [only a small part of our possible mental and physical resources](https://psychclassics.yorku.ca/James/energies.htm).
- Background: Wikipedia names the 1890s reserve-energy theories of William James and Boris Sidis as a likely origin, with no direct citation. No retelling I opened credits a specific Sidis text.
- Barry Beyerstein, *Scientific American* (2004): he found no single source. He describes the figure drifting among positive-thinking writers from a share of capacity to a share of the brain. The Albert Einstein Archives had no record of Einstein making the statement.
- Pelman Institute, 1944: according to BPS, citing Christopher Wanjek, the same institute ran a newspaper advertisement 15 years later with a one-tenth figure.

### Cold trails
None.

### Confidence
Medium: the root was opened and its date comes from the almanac itself, but its text is an OCR scan that is partly garbled in places. Wikipedia's link to the root runs through Beyerstein's 1999 chapter, which I did not open. Penfield's studies and the 1944 Pelman ad were not opened, and Snopes returned a paywall (HTTP 402). The copy of the Lowell Thomas sketch I opened is a 2005 ebook edition, which reads *average person* where other pages give *average man*.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
