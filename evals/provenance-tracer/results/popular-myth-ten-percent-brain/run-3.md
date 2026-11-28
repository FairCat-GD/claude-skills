---
case: popular-myth-ten-percent-brain
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:30:57Z
cost_usd: 1.8336
duration_s: 238
turns: 38
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- Read: <plugin>/skills/provenance-tracer/references/labels.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- WebSearch: "10% of their brains" origin
- WebSearch: we only use 10 percent of our brain myth history
- WebSearch: William James Lowell Thomas "10 percent" brain Dale Carnegie preface
- WebSearch: "ten percent" brain who first said
- WebSearch: snopes 10 percent of brain
- WebSearch: "The Energies of Men" William James "small part of our possible mental"
- WebFetch: https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth
- WebFetch: https://www.scientificamerican.com/article/do-we-really-use-only-10/
- WebFetch: https://www.snopes.com//fact-check/the-ten-percent-myth/
- WebFetch: https://psychclassics.yorku.ca/James/energies.htm
- WebFetch: https://www.psychologicalscience.org/uncategorized/myth-we-only-use-10-of-our-brains.html
- WebFetch (error): http://www.cyberspacei.com/englishwiz/library/friends/how_to_win_friends.htm
- WebFetch: https://faculty.washington.edu/chudler/pdf/tenper.pdf
- WebSearch: "develops only ten per cent of his latent mental ability" archive.org
- WebSearch: "A Shortcut to Distinction" Lowell Thomas "William James" "latent mental ability"
- WebFetch: https://mentalfloss.com/article/57658/do-you-use-only-10-your-brain
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28how+to+win+friends+and+influence+people%29+AND+date%3A%5B1936-01-01+TO+1940-12-31%5D&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=date&rows=20&output=json
- WebFetch: https://socialskillswisdom.com/introduction-a-shortcut-to-distinction-by-lowell-thomas/
- WebFetch: https://archive.org/metadata/how-to-win-friends_202311
- WebFetch: https://ia600502.us.archive.org/23/items/how-to-win-friends_202311/How%20to%20win%20friends_djvu.txt
- WebFetch: https://archive.org/metadata/howtowinfriendsi0000dale
- WebSearch: "TEN PERCENT of our brain power" World Almanac 1929 advertisement
- WebSearch: Beyerstein "Whence cometh the myth" ten percent brains Mind Myths 1999 pdf
- WebFetch: https://ruscio.pages.tcnj.edu/files/2016/08/Lilienfeld-et-al-2010-S-Top-Ten-Myths.pdf
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28world+almanac%29+AND+date%3A%5B1929-01-01+TO+1929-12-31%5D&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=date&rows=20&output=json
- WebFetch: https://archive.org/metadata/world-almanac-and-book-of-facts_1929
- WebFetch: https://ia600507.us.archive.org/13/items/world-almanac-and-book-of-facts_1929/world-almanac-and-book-of-facts_1929_djvu.txt
- WebFetch: https://ia600507.us.archive.org/13/items/world-almanac-and-book-of-facts_1929/world-almanac-and-book-of-facts_1929_djvu.txt
- WebFetch: https://ia600507.us.archive.org/13/items/world-almanac-and-book-of-facts_1929/world-almanac-and-book-of-facts_1929_djvu.txt
- WebFetch: https://ia600507.us.archive.org/13/items/world-almanac-and-book-of-facts_1929/world-almanac-and-book-of-facts_1929_djvu.txt

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Humans use only 10% of their brains."

**Roots:** Echo · **Grounding:** Primary differs · Mutated
**Earliest instance found:** [Pelman Institute of America advertisement, *The World Almanac and Book of Facts 1929*](https://ia600507.us.archive.org/13/items/world-almanac-and-book-of-facts_1929/world-almanac-and-book-of-facts_1929_djvu.txt), 1929 (date from: byline, the almanac's own title year). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 7

### Chain
Your version: "Humans use only 10% of their brains" (where you met it: not given)
 ├─ [Wikipedia, *Ten-percent-of-the-brain myth*](https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth), date unknown, Tertiary → cites
 │   ├─ Barry Beyerstein, *Whence Cometh the Myth that We Only Use 10% of our Brains?*, in *Mind Myths* (Wiley), 1999, (not opened), per Wikipedia → cites
 │   │   └─ [Pelman Institute of America advertisement, *The World Almanac and Book of Facts 1929*](https://ia600507.us.archive.org/13/items/world-almanac-and-book-of-facts_1929/world-almanac-and-book-of-facts_1929_djvu.txt), 1929, Tertiary, root
 │   └─ [Lowell Thomas, *A Shortcut to Distinction*, introduction to Dale Carnegie's *How to Win Friends and Influence People*](https://socialskillswisdom.com/introduction-a-shortcut-to-distinction-by-lowell-thomas/), 1936, Secondary → credits William James
 │       └─ [William James, *The Energies of Men*, *Science* 25:321–332](https://psychclassics.yorku.ca/James/energies.htm), 1907, Primary (credited, differs)
 ├─ [Barry L. Beyerstein, *Do we really use only 10 percent of our brains?*, *Scientific American*](https://www.scientificamerican.com/article/do-we-really-use-only-10/), 2004, Tertiary → cites Lowell Thomas, 1936, and Beyerstein, 1999 (both above)
 ├─ [Hannah Keyser, *Do You Use Only 10% of Your Brain?*, *Mental Floss*](https://mentalfloss.com/article/57658/do-you-use-only-10-your-brain), 2015, Tertiary → cites Lowell Thomas, 1936 (above)
 └─ [Association for Psychological Science, *Myth: We Only Use 10% of Our Brains*](https://www.psychologicalscience.org/uncategorized/myth-we-only-use-10-of-our-brains.html), 2018, Secondary → cites William James, 1907 (above), as a possible misread source

Notes on the chain:
- **The 1929 advertisement** is a home-study ad selling a mind-training booklet. It credits the ten-per-cent figure to unnamed *scientists and psychologists*, with no work named. I found it on the almanac scan's advertising pages, so it is the earliest instance in this trace.
- **The 1936 introduction** (signed *Lowell Thomas, 1936*, unrevised edition) gives the figure as a share of *latent mental ability* and credits William James. It cites nothing from the 1929 ad. In the [2005 ebook edition](https://ia600502.us.archive.org/23/items/how-to-win-friends_202311/How%20to%20win%20friends_djvu.txt), the same sentence says *average person* where the unrevised text says *average man*.
- **James's essay**, opened, gives no percentage and does not describe brain tissue as unused. It argues that people use only a small part of their mental and physical resources.

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Hedge dropped | the ad says scientists put our use at *about* ten per cent | Humans use only 10% of their brains | [Lowell Thomas, *A Shortcut to Distinction*](https://socialskillswisdom.com/introduction-a-shortcut-to-distinction-by-lowell-thomas/), 1936 |
| Other: a capacity read as the organ | the ad speaks of *brain power*, a capacity, not of the brain itself | Humans use only 10% of their brains | [*Scientific American*](https://www.scientificamerican.com/article/do-we-really-use-only-10/), 2004 |
| Other: an advertising pitch read as a plain statement | the figure appears in a sales ad for a mind-training course, credited to unnamed scientists | Humans use only 10% of their brains | [*Scientific American*](https://www.scientificamerican.com/article/do-we-really-use-only-10/), 2004 |

### Status of the root
- No primary found, so there was no status to check. The root is an advertisement passing on a figure it credits to unnamed scientists, not a study.
- William James, *The Energies of Men* (1907): it was presented as an address to the American Philosophical Association on 28 December 1906 and printed in *Science* in 1907, per the [York University *Classics in the History of Psychology* copy](https://psychclassics.yorku.ca/James/energies.htm). It gives no figure for how much of the brain or mind people use. The APS page says the myth may stem from a misunderstanding of this article.
- Background: other proposed sources were named in opened pages but not followed in this trace: Wilder Penfield's work (per Wikipedia), Karl Lashley's rat studies in the 1920s and 1930s (per *Mental Floss*), and a 1932 John W. Campbell story (per Wikipedia).

### Cold trails
None.

### Confidence
Medium: the root ad and the 1936 and 1907 texts were opened and dated by byline, but the Beyerstein 1999 chapter that links retellings to the ad was not opened, and the Snopes page (2000) returned an error.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
