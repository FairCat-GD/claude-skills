---
case: popular-myth-ten-percent-brain
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T19:15:48Z
cost_usd: 1.8763
duration_s: 230
turns: 39
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- Read: <plugin>/skills/provenance-tracer/references/labels.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- WebSearch: "only 10% of their brains"
- WebSearch: "we only use 10 percent of our brain" origin
- WebSearch: William James Lowell Thomas Dale Carnegie "10 percent" brain origin
- WebSearch: "ten percent of their mental" OR "10 per cent of their latent mental ability" Lowell Thomas 1936
- WebSearch: who first said humans use only 10 percent of their brain earliest
- WebSearch: 10 percent brain myth snopes OR "quote investigator" OR scientific american
- WebFetch: https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth
- WebFetch: https://www.scientificamerican.com/article/do-people-only-use-10-percent-of-their-brains/
- WebFetch: https://www.snopes.com//fact-check/the-ten-percent-myth/
- WebSearch: "A Shortcut to Distinction" Lowell Thomas "ten per cent of his latent mental ability"
- WebSearch: 1929 World Almanac advertisement "TEN PERCENT of our brain power" Pelman
- WebSearch: William James "The Energies of Men" "small part of our possible mental and physical resources" text
- WebFetch: https://psychclassics.yorku.ca/James/energies.htm
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28how+to+win+friends+and+influence+people%29+AND+date%3A%5B1936-01-01+TO+1937-12-31%5D&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=date&rows=20&output=json
- WebFetch: https://socialskillswisdom.com/introduction-a-shortcut-to-distinction-by-lowell-thomas/
- WebFetch: https://archive.org/stream/how-to-win-friends_202311/how-to-win-friends_djvu.txt
- WebFetch: https://archive.org/stream/how-to-win-friends_202311/How%20to%20win%20friends_djvu.txt
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28world+almanac%29+AND+date%3A%5B1929-01-01+TO+1929-12-31%5D&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=date&rows=20&output=json
- WebFetch: https://www.brain-zone.net/learn/research/myths/10-percent-brain-myth
- WebFetch: https://archive.org/stream/world-almanac-and-book-of-facts_1929/world-almanac-and-book-of-facts_1929_djvu.txt
- WebFetch: https://archive.org/stream/world-almanac-and-book-of-facts_1929/world-almanac-and-book-of-facts_1929_djvu.txt
- WebFetch: https://archive.org/stream/world-almanac-and-book-of-facts_1929/world-almanac-and-book-of-facts_1929_djvu.txt
- WebSearch: Pelman "ten per cent" brain advertisement 1920s earliest "per cent of our brain"
- WebSearch: Beyerstein "Whence cometh the myth that we only use 10% of our brains" Mind Myths 1999
- WebFetch: https://de.wikipedia.org/wiki/10-Prozent-Mythos
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28dental+register%29+AND+date%3A%5B1910-01-01+TO+1910-12-31%5D&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=date&fl%5B%5D=volume&rows=20&output=json
- WebFetch: https://books.google.com/books?id=P9oDAAAAMBAJ&pg=PA63
- WebFetch: https://books.google.pl/books?id=P9oDAAAAMBAJ&pg=PA63&redir_esc=y
- WebFetch: https://archive.org/advancedsearch.php?q=%22dental+register%22+AND+year%3A1910&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=date&rows=20&output=json
- WebFetch: https://babel.hathitrust.org/cgi/ls?q1=%22one-tenth%20of%20his%20brain%20possibilities%22&anyall1=phrase&lmt=ft
- WebFetch: https://books.google.pl/books?id=4I01AQAAMAAJ&q=%22brain+possibilities%22&redir_esc=y

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Humans use only 10% of their brains."

**Roots:** Echo · **Grounding:** Primary differs · Mutated
**Earliest instance found:** *The Dental Register*, vol. 64, p. 26, 1910 (date from: cited by [German Wikipedia, *10-Prozent-Mythos*](https://de.wikipedia.org/wiki/10-Prozent-Mythos)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 10

### Chain
Your version: "Humans use only 10% of their brains" (where you met it: not given)
 ├─ [Wikipedia, *Ten-percent-of-the-brain myth*](https://en.wikipedia.org/wiki/Ten-percent-of-the-brain_myth), date unknown, Tertiary → cites
 │   ├─ [Pelman Institute of America advertisement, *The World Almanac and Book of Facts 1929*](https://archive.org/stream/world-almanac-and-book-of-facts_1929/world-almanac-and-book-of-facts_1929_djvu.txt), 1929, Tertiary: it credits only unnamed experts, "Scientists and psychologists tell us we use only about TEN PER CENT" → stopped: names no source
 │   └─ [Lowell Thomas, *A Shortcut to Distinction*, foreword to Dale Carnegie's *How to Win Friends and Influence People*](https://socialskillswisdom.com/introduction-a-shortcut-to-distinction-by-lowell-thomas/), 1936, Secondary: says William James used to say "the average man develops only 10 percent of his latent mental ability" → credits William James
 │       │   (a [2005 ebook copy](https://archive.org/stream/how-to-win-friends_202311/How%20to%20win%20friends_djvu.txt) has *average person* in place of *average man*)
 │       └─ [William James, *The Energies of Men*, *Science* 25:321–332](https://psychclassics.yorku.ca/James/energies.htm), 1907, Primary (credited, differs): he says we use "only a small part of our possible mental and physical resources", with no percentage
 ├─ [German Wikipedia, *10-Prozent-Mythos*](https://de.wikipedia.org/wiki/10-Prozent-Mythos), date unknown, Tertiary → cites
 │   ├─ *The Dental Register*, vol. 64, p. 26, 1910, (not opened), per German Wikipedia, root
 │   ├─ *Young Men* (a YMCA magazine), vol. 41, p. 129, 1915, (not opened), per German Wikipedia: credits *the late Professor James* with one-tenth of brain power → stopped: not opened
 │   ├─ Advertisement for *The Secret of Mental Power*, *Popular Science Monthly*, vol. 101, p. 21, 1922, (not opened), per German Wikipedia: credits James with a tenth part of the brain → stopped: not opened
 │   │   └─ [Same advertisement reprinted in *Popular Mechanics*, Sept. 1922, p. 63](https://books.google.pl/books?id=P9oDAAAAMBAJ&pg=PA63&redir_esc=y), 1922, (not opened), per German Wikipedia → stopped: not opened
 │   └─ Pelman Institute advertisement, *Popular Science*, Nov. 1928, p. 173, (not opened), per German Wikipedia: the same wording as the 1929 ad → stopped: not opened
 └─ [Robynne Boyd, *Do People Only Use 10 Percent of Their Brains?*, *Scientific American*](https://www.scientificamerican.com/article/do-people-only-use-10-percent-of-their-brains/), 2008, Secondary: says no single source started the claim, and links it to James's *The Energies of Men* and to Einstein → credits William James (the 1907 essay above)

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Other: brain *possibilities* (capacity) read as the brain itself | the average man uses ["one-tenth of his brain possibilities"](https://de.wikipedia.org/wiki/10-Prozent-Mythos) | Humans use only 10% of their brains | *The Secret of Mental Power* advertisement, *Popular Science Monthly*, 1922 (not opened, per German Wikipedia) |
| Scope widened | the average man | Humans use only 10% of their brains | [*Scientific American*](https://www.scientificamerican.com/article/do-people-only-use-10-percent-of-their-brains/), 2008 |

### Status of the root
- No primary found, so there was no status to check.
- William James, *The Energies of Men* (1907): this is the text that the 1915, 1922 and 1936 retellings credit. Opened, it speaks of unused mental and physical resources in general, and gives no figure and no share of the brain.
- Background: Barry Beyerstein's chapter *Whence Cometh the Myth that We Only Use 10% of our Brains?* (in *Mind Myths*, Wiley, 1999, pp. 3–24) is named by the retellings as where the 1929 almanac ad was first reproduced. It was not opened.

### Cold trails
- [Pelman Institute advertisement, *World Almanac* 1929](https://archive.org/stream/world-almanac-and-book-of-facts_1929/world-almanac-and-book-of-facts_1929_djvu.txt), 1929: states the claim and credits only unnamed scientists.
- Pelman Institute advertisement, *Popular Science*, 1928, (not opened), per German Wikipedia: the same wording, with no named source.

### Confidence
Medium: the 1929 ad, the 1936 foreword and James's essay were opened, but the root (1910) and the 1915 and 1922 versions are known only through German Wikipedia, since Google Books blocked access and Snopes returned a paywall error (HTTP 402).

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
