---
case: popular-myth-ten-percent-brain
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:24:08Z
cost_usd: 1.2578
duration_s: 137
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
- WebSearch: "use only 10% of their brains"
- WebSearch: "ten percent of the brain" myth origin William James
- WebSearch: Lowell Thomas preface Dale Carnegie "ten per cent of his latent mental ability"
- WebSearch: origin of "10 percent of the brain" earliest first appeared
- WebSearch: William James "The Energies of Men" "we are making use of only a small part of our possible mental"
- WebSearch: snopes 10 percent brain
- WebFetch: https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth
- WebFetch: https://www.psychologytoday.com/us/blog/modern-minds/201803/why-do-we-only-use-10-percent-of-the-brain
- WebFetch: https://en.wikipedia.org/wiki/Talk:Ten_percent_of_the_brain_myth
- WebFetch: https://gwern.net/doc/psychology/personality/conscientiousness/1907-james.pdf
- WebFetch: https://www.snopes.com//fact-check/the-ten-percent-myth/
- WebFetch: https://en.wikipedia.org/wiki/Talk:Ten_percent_of_the_brain_myth
- WebFetch (error): https://ebooks.adelaide.edu.au/j/james/william/memories/chapter10.html
- WebFetch (error): https://web.archive.org/web/20110515143209/http://www.cyberspacei.com/englishwiz/library/friends/how_to_win_friends.htm
- WebFetch: https://www.scientificamerican.com/article/do-people-only-use-10-percent-of-their-brains/
- WebFetch: https://www.loc.gov/resource/sn90050307/1912-01-10/ed-1/?sp=3
- WebFetch: https://www.gutenberg.org/files/5555/5555-h/5555-h.htm
- WebSearch: "A Shortcut to Distinction" Lowell Thomas "ten per cent" James full text How to Win Friends 1936
- WebFetch: https://ia801007.us.archive.org/34/items/Howtowin/Howtowin.pdf
- WebFetch: http://iapsop.com/ssoc/1914__james___the_energies_of_man.pdf
- WebFetch: https://www.britishcanada.org/how_to_win_friends.html
- WebFetch: https://en.wikisource.org/wiki/The_Energies_of_Men
- WebFetch: https://www.brainfacts.org/thinking-sensing-and-behaving/thinking-and-awareness/2019/debunked-the-10-percent-brain-myth-061719

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Humans use only 10% of their brains."

**Roots:** Echo · **Grounding:** Primary differs · Mutated
**Earliest instance found:** [a Tyler Commercial College ad in *The Prescott Daily News*](https://www.loc.gov/resource/sn90050307/1912-01-10/ed-1/?sp=3), 1912, (not opened; the page returned HTTP 403), per [Wikipedia talk page](https://en.wikipedia.org/wiki/Talk:Ten_percent_of_the_brain_myth) (date from: cited by the Wikipedia talk page). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 8

### Chain
Your version: "Humans use only 10% of their brains" (where you met it: not given)
 ├─ [Scientific American, *Do People Only Use 10 Percent of Their Brains?*](https://www.scientificamerican.com/article/do-people-only-use-10-percent-of-their-brains/), 2008, Secondary → cites
 │   └─ [William James, *The Energies of Men*](https://en.wikisource.org/wiki/The_Energies_of_Men), 1907, Primary
 ├─ [Wikipedia, *Ten-percent-of-the-brain myth*](https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth), date unknown, Tertiary → cites
 │   ├─ [Lowell Thomas, *A Shortcut to Distinction*, introduction to Dale Carnegie's *How to Win Friends and Influence People*](https://www.britishcanada.org/how_to_win_friends.html), 1936, Secondary → cites
 │   │   └─ William James, *The Energies of Men*, 1907, Primary (the same root as above)
 │   └─ A 1929 *World Almanac* ad, 1929, (not opened), per Wikipedia, which cites Beyerstein in *Mind Myths* (1999) → stopped: not opened
 ├─ [Wikipedia talk page, the section on a 1912 newspaper ad](https://en.wikipedia.org/wiki/Talk:Ten_percent_of_the_brain_myth), 2026, Tertiary → cites
 │   └─ [The ad in *The Prescott Daily News*](https://www.loc.gov/resource/sn90050307/1912-01-10/ed-1/?sp=3), 1912, (not opened), per the Wikipedia talk page. The talk page says the ad credits "The late Prof. James of Harvard" → stopped: not opened
 └─ [Psychology Today, *Why Do We Only Use 10 Percent of the Brain?*](https://www.psychologytoday.com/us/blog/modern-minds/201803/why-do-we-only-use-10-percent-of-the-brain), date unknown, Tertiary → cites
     └─ The same 1929 self-help ad, 1929, (not opened), per Psychology Today → stopped: not opened

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Number changed | No figure. People use "[only a small part of our possible mental and physical resources](https://en.wikisource.org/wiki/The_Energies_of_Men)" | 10% | Earliest opened source: [Thomas](https://www.britishcanada.org/how_to_win_friends.html), 1936, who wrote "[the average person develops only 10 percent of his latent mental ability](https://www.britishcanada.org/how_to_win_friends.html)". The unopened 1912 ad reportedly gives "ten per cent" earlier. |
| Other: unused capacity read as unused brain tissue | Unused powers and reserves of energy, framed as a matter of habit. Wikisource's text mentions no unused brain tissue. | "of their brains" | Earliest opened source: [Scientific American](https://www.scientificamerican.com/article/do-people-only-use-10-percent-of-their-brains/), 2008. The unopened 1912 and 1929 ads reportedly say "brain power". |
| Scope widened | Men "habitually" use a small part of the powers they could use "under appropriate conditions" | All humans, with no condition | Earliest opened source: [Thomas](https://www.britishcanada.org/how_to_win_friends.html), 1936 ("the average person") |
| Context removed | An argument about habit and energy that can be unlocked under some conditions | A plain statement about the brain | Earliest opened source: [Thomas](https://www.britishcanada.org/how_to_win_friends.html), 1936 |

### Status of the root
- *The Energies of Men* is a 1907 essay in *The American Magazine*, reprinted in 1911 by Moffat, Yard ([Wikisource](https://en.wikisource.org/wiki/The_Energies_of_Men)). It has no DOI, so I ran no Crossref, Retraction Watch or PubPeer check, and found no correction notice.
- [Scientific American](https://www.scientificamerican.com/article/do-people-only-use-10-percent-of-their-brains/) (2008) quotes neurologist Barry Gordon: "we use virtually every part of the brain."
- [BrainFacts/SfN](https://www.brainfacts.org/thinking-sensing-and-behaving/thinking-and-awareness/2019/debunked-the-10-percent-brain-myth-061719) (2019) quotes neuroscientist Nick Spitzer: "We use all of our brain."

### Cold trails
- The 1929 *World Almanac* ad, 1929, (not opened), per [Wikipedia](https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth): it credits the figure to unnamed "scientists and psychologists" and names no source.

### Confidence
Medium: James's essay and Thomas's 1936 text were opened, but the two earliest instances of "ten per cent" (the 1912 and 1929 ads) were not; their wording and dates rest on the pages that cite them, and a note on the talk page says the 1912 finding was posted by a self-declared AI agent. Snopes's page also returned HTTP 402 and was not opened.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
