---
case: retracted-origin-mmr-autism
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T19:18:55Z
cost_usd: 1.4173
duration_s: 181
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
- WebSearch: "MMR vaccine causes autism"
- WebSearch: MMR autism link claim origin Wakefield 1998 Lancet
- WebSearch: Wakefield 1998 press conference MMR single vaccines
- WebSearch: origin of MMR autism scare first appeared
- WebSearch: MMR vaccine autism fact check
- WebSearch: Lancet retraction Wakefield ileal-lymphoid-nodular hyperplasia 2010 notice
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320&resultType=core&format=json
- WebFetch: https://theconversation.com/mondays-medical-myth-the-mmr-vaccine-causes-autism-3739
- WebFetch: https://briandeer.com/mmr/lancet-summary.htm
- WebFetch: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(10)60175-4/abstract
- WebFetch: https://www.open.edu/openlearn/health-sports-psychology/health/the-mmr-vaccine-public-health-private-fears/content-section-10.1
- WebFetch: https://briandeer.com/mmr/lancet-paper.pdf
- WebFetch: http://briandeer.com/wakefield/royal-video.htm
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:20137807&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:15016483&resultType=core&format=json
- WebFetch: https://api.crossref.org/works/10.1016/s0140-6736(97)11096-0
- WebFetch: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(97)11096-0/fulltext
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:12421889&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:10376617&resultType=core&format=json
- WebSearch: JABS Richard Barr 1996 parents MMR autism legal aid before Wakefield paper
- WebFetch (error): https://web.archive.org/web/2010/http://www.thelancet.com/journals/lancet/article/PIIS0140-6736(97)11096-0/fulltext
- WebFetch: https://people.wou.edu/~bersanh/autism/scam.pdf
- WebFetch: https://en.wikipedia.org/wiki/JABS
- WebFetch: https://briandeer.com/mmr/lancet-deer-2.htm
- WebFetch: https://www.bmj.com/content/342/bmj.c5347

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "The MMR vaccine causes autism."

**Roots:** Echo · **Grounding:** Primary differs · Mutated · Origin retracted · Origin corrected
**Earliest instance found:** [Wakefield et al., *Ileal-lymphoid-nodular hyperplasia, non-specific colitis, and pervasive developmental disorder in children*, The Lancet](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320&resultType=core&format=json), 1998 (date from: byline). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 5

### Chain
Your version: "The MMR vaccine causes autism" (where you met it: not given)
 ├─ [Rachael Dunlop, *Monday's medical myth: the MMR vaccine causes autism*, The Conversation](https://theconversation.com/mondays-medical-myth-the-mmr-vaccine-causes-autism-3739), 2011, Secondary → cites
 │   ├─ [Brian Deer, Royal Free video news release page](http://briandeer.com/wakefield/royal-video.htm), date unknown, Secondary → cites
 │   │   └─ Royal Free Hospital Medical School press conference and video news release, February 1998, Primary (not opened, per Brian Deer) → stopped: not opened
 │   └─ [Wakefield et al., The Lancet 351:637–641](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320&resultType=core&format=json), 1998, Primary (abstract opened), root
 └─ [Open University, *The MMR vaccine: public health, private fears*, section 10.1](https://www.open.edu/openlearn/health-sports-psychology/health/the-mmr-vaccine-public-health-private-fears/content-section-10.1), date unknown, Secondary → cites
     └─ Wakefield et al., 1998 (the root, above)

The Conversation places the start of the claim at the press conference rather than the paper. It says ["The paper itself didn't address such a connection"](https://theconversation.com/mondays-medical-myth-the-mmr-vaccine-causes-autism-3739) and that Wakefield raised the concern with journalists. According to Deer's page, Wakefield said at the press conference that he could not support giving the three vaccines in combination until the issue was resolved, and he called for single shots given a year apart. The Open University reading describes UK news coverage in 2002, when broadcasts and newspapers referred to the jab as one that some doctors or some research had linked to autism.

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Correlation stated as causation | parents of 8 of the 12 children linked the start of symptoms in time to MMR vaccination; the abstract claims no cause | The MMR vaccine causes autism | Royal Free press conference, 1998 (not opened, per [Brian Deer](http://briandeer.com/wakefield/royal-video.htm)) |
| Scope widened | a case series of 12 children seen at one London gastroenterology clinic | The MMR vaccine causes autism | Royal Free press conference, 1998 (not opened, per [Brian Deer](http://briandeer.com/wakefield/royal-video.htm)) |
| Hedge dropped | links the condition in time with *possible* environmental triggers | The MMR vaccine causes autism | Royal Free press conference, 1998 (not opened, per [Brian Deer](http://briandeer.com/wakefield/royal-video.htm)) |

### Status of the root
- **Full retraction, 2010.** The Lancet retracted the paper in 2010, at 375(9713):445. [Europe PMC's record of the notice](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:20137807&resultType=core&format=json) lists it as a retraction of PMID 9500320. [Crossref](https://api.crossref.org/works/10.1016/s0140-6736(97)11096-0) records the retraction dated 6 February 2010, sourced from Retraction Watch. The Lancet's own page for the notice returned 403 and could not be opened.
- **Partial retraction, 2004.** Ten co-authors published *Retraction of an interpretation*, The Lancet 363:750, in March 2004 ([Europe PMC record](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:15016483&resultType=core&format=json); no text available there). Crossref lists it as a correction dated 6 March 2004.
- **Expression of concern, 2011.** Europe PMC's record of the root lists an expression of concern in *Eur J Gastroenterol Hepatol* 2011;23(11):1082.
- **Undisclosed legal-aid funding.** Brian Deer, in *The Sunday Times* (22 February 2004, [reprint](https://briandeer.com/mmr/lancet-deer-2.htm)), reported that the Legal Aid Board granted Wakefield and solicitor Richard Barr £55,000 in August 1996 to investigate possible MMR–autism links in 10 named children. He also reported that four or five of the paper's eight MMR-linked children were covered by that contract.
- **Later study: Taylor et al., 1999.** *Autism and measles, mumps, and rubella vaccine: no epidemiological evidence for a causal association*, The Lancet 353:2026–2029 ([abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:10376617&resultType=core&format=json)). The authors report that their analyses of a large regional UK sample do not support a causal association. They add that if one exists, it is too rare to find in that sample.
- **Later study: Madsen et al., 2002.** *A population-based study of measles, mumps, and rubella vaccination and autism*, NEJM 347:1477–1482 ([abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:12421889&resultType=core&format=json)). It concludes that it gives ["strong evidence against the hypothesis that MMR vaccination causes autism"](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:12421889&resultType=core&format=json).

### Cold trails
None.

### Confidence
Medium: the root's abstract and its retraction records were opened, but the paper's full text was not (two full-text copies returned 403 and a PDF gave no readable text), and the press-conference node is known only through Brian Deer's page.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
