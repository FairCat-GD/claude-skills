---
case: popular-myth-ten-percent-brain
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:23:09Z
cost_usd: 1.4188
duration_s: 154
turns: 29
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- Read: <plugin>/skills/provenance-tracer/references/labels.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- WebSearch: "10 percent of their brains" origin
- WebSearch: "we only use 10% of our brain" who first said
- WebSearch: William James "small part of our possible mental resources" ten percent brain myth Lowell Thomas
- WebSearch: "ten percent" brain myth earliest appearance history
- WebSearch: 10 percent brain myth snopes OR "quote investigator"
- WebSearch: Beyerstein "Whence cometh the myth that we only use ten percent of our brains"
- WebFetch: https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth
- WebFetch: https://www.scientificamerican.com/article/do-we-really-use-only-10/
- WebFetch: https://www.snopes.com//fact-check/the-ten-percent-myth/
- WebFetch: https://www.gutenberg.org/files/26000/26000-h/26000-h.htm
- WebFetch (error): http://www.cyberspacei.com/englishwiz/library/friends/how_to_win_friends.htm
- WebFetch: https://en.wikisource.org/wiki/The_Energies_of_Men
- WebSearch: "A Shortcut to Distinction" Lowell Thomas "ten percent of his latent mental ability" full text
- WebSearch: "World Almanac" 1929 advertisement "ten percent of our brain power" Pelman
- WebFetch (error): https://web.archive.org/web/2011/http://www.cyberspacei.com/englishwiz/library/friends/how_to_win_friends.htm
- WebFetch: https://www.psychologicalscience.org/uncategorized/myth-we-only-use-10-of-our-brains.html
- WebFetch: https://gizmodo.com/where-the-10-percent-of-our-brains-myth-comes-from-a-1598507369
- WebSearch: archive.org "How to Win Friends and Influence People" 1936 full text "latent mental ability"
- WebFetch: https://archive.org/stream/in.ernet.dli.2015.67270/2015.67270.How-To-Win-Friends-And-Influence-People_djvu.txt
- WebFetch: https://faculty.washington.edu/chudler/tenper.html
- WebFetch: https://api.crossref.org/works/10.1126/science.25.635.321

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Humans use only 10% of their brains."

**Roots:** Echo · **Grounding:** Primary differs · Mutated
**Earliest instance found:** A self-help advertisement in the *World Almanac* that says people use about ten percent of their "brain power". It is dated 1929 (date from: cited by [Wikipedia](https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth), which cites Beyerstein 1999, p. 11). I did not open the advertisement itself. Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 10

### Chain
Your version: "Humans use only 10% of their brains" (where you met it: not given)
 └─ [Wikipedia, *Ten-percent-of-the-brain myth*](https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth), date unknown, Tertiary → cites
     ├─ Barry Beyerstein, *Whence Cometh the Myth that We Only Use 10% of our Brains?*, in *Mind Myths* (ed. Della Sala, Wiley), 1999, (not opened), per Wikipedia → cites
     │   └─ *World Almanac* self-help advertisement, 1929, (not opened), per Wikipedia. Its wording, as Wikipedia gives it: [“we use only about TEN PERCENT of our brain power”](https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth). The ad credits only unnamed "scientists and psychologists" → stopped: not opened
     └─ Lowell Thomas, *A Short-Cut to Distinction*, the introduction to Dale Carnegie's [*How to Win Friends and Influence People*](https://archive.org/stream/in.ernet.dli.2015.67270/2015.67270.How-To-Win-Friends-And-Influence-People_djvu.txt), 1936, Secondary. Thomas credits the figure to James: [“the average man develops only ten per cent of his latent mental ability”](https://archive.org/stream/in.ernet.dli.2015.67270/2015.67270.How-To-Win-Friends-And-Influence-People_djvu.txt) → cites
         └─ William James, [*The Energies of Men*](https://en.wikisource.org/wiki/The_Energies_of_Men), 1907, Primary. James wrote that we use [“only a small part of our possible mental and physical resources”](https://en.wikisource.org/wiki/The_Energies_of_Men). The essay gives no percentage and does not discuss the brain as an organ.

 └─ Barry Beyerstein, [*Do we really use only 10 percent of our brains?*](https://www.scientificamerican.com/article/do-we-really-use-only-10/), *Scientific American*, 2004, Secondary → cites Beyerstein 1999 and Thomas 1936 (above). It says self-help writers gradually turned "10 percent of our capacity" into "10 percent of our brain", and that Thomas's 1936 preface tied the claim to James.
 └─ Andrew Tarantola, [*How the "10 Percent of Our Brains" Myth Started*](https://gizmodo.com/where-the-10-percent-of-our-brains-myth-comes-from-a-1598507369), Gizmodo, 2014, Tertiary → cites James and Thomas (above). It also names Flourens, Sidis and Lashley as possible influences.
 └─ [Association for Psychological Science lesson page](https://www.psychologicalscience.org/uncategorized/myth-we-only-use-10-of-our-brains.html), 2018, Secondary → cites James 1907 (above). It says the origin "is unclear".
 └─ Eric Chudler, [*Neuroscience for Kids: 10% of the Brain Myth*](https://faculty.washington.edu/chudler/tenper.html), date unknown, Tertiary → cites James, Thomas (dated 1937 there), Beyerstein 1999 and Snopes. Chudler says he could not find the myth's exact source.
     └─ [Snopes, *The Ten-Percent Myth*](https://www.snopes.com//fact-check/the-ten-percent-myth/), date unknown, (not opened, the fetch returned HTTP 402), per Chudler → stopped: not opened

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Number changed | no figure: "a small part" of our resources | 10% | *World Almanac* ad, 1929 (not opened, per Wikipedia) |
| Other: capacity became brain tissue | possible mental and physical resources: energy, will, effort | "their brains" | *World Almanac* ad, 1929 ("brain power"; not opened, per Wikipedia). *Scientific American* (2004) describes the shift from "capacity" to "brain". |
| Context removed | an essay about people working below their energy and effort, with no claim about anatomy | a plain statement about how much of the brain is used | *World Almanac* ad, 1929 (not opened, per Wikipedia) |
| Other: the figure credited to James, then the credit dropped | James gives no percentage | no one credited | Thomas, *How to Win Friends and Influence People*, 1936 (credit to James). The credit is missing in your version. |

### Status of the root
- William James, *The Energies of Men*, *Science* 25 (635): 321–332, 1907. The [Crossref record](https://api.crossref.org/works/10.1126/science.25.635.321) shows no retraction, correction or expression of concern. The essay is an address, not a data study. I did not check the journal page, Retraction Watch or PubPeer.

### Cold trails
- *World Almanac* self-help advertisement, 1929 (not opened, per [Wikipedia](https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth)): it states the figure and credits only unnamed "scientists and psychologists".

### Confidence
Medium. James (1907) and Thomas (1936) were opened and dated by byline. The earliest instance of the 10% figure (the 1929 ad), Beyerstein's 1999 chapter and the Snopes fact-check were not opened.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
