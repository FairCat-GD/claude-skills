---
case: retracted-origin-mmr-autism
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: bf06fdf9900c0609534800b3c875cea27fc5b3b8
date: 2026-11-28T00:15:46Z
cost_usd: 1.4274
duration_s: 283
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
- WebSearch: origin of the MMR autism scare history
- WebSearch: vaccines cause autism fact check MMR
- WebSearch: Wakefield Lancet 1998 retraction notice "Ileal-lymphoid-nodular hyperplasia"
- WebSearch: Wakefield 1998 press conference MMR single vaccines Royal Free
- WebFetch: https://www.thelancet.com/journals/lancet/article/PIIS0140673697110960/fulltext
- WebFetch: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(10)60175-4/abstract
- WebFetch (error): https://www.npr.org/2025/03/05/nx-s1-5285571/the-history-behind-an-enduring-public-health-falsehood-that-vaccines-cause-autism
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC3136032/
- WebFetch: https://www.thelancet.com/pdfs/journals/lancet/PIIS0140-6736(97)11096-0.pdf
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/S0140-6736(97)11096-0&resultType=core&format=json
- WebFetch: https://api.crossref.org/works/10.1016/S0140-6736(97)11096-0
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320&resultType=core&format=json
- WebFetch: https://en.wikipedia.org/wiki/Vaccines_and_autism
- WebFetch: https://www.poynter.org/fact-checking/2026/do-vaccines-cause-autism/
- WebSearch: "We did not prove an association between measles, mumps, and rubella vaccine and the syndrome described" full text
- WebFetch: https://briandeer.com/wakefield/royal-video.htm
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/9500320/
- WebFetch: https://www.aafp.org/afp/2002/1201/p2113
- WebFetch (error): https://www.npr.org/2025/03/05/nx-s1-5285571/the-history-behind-an-enduring-public-health-falsehood-that-vaccines-cause-autism
- WebFetch: https://en.wikipedia.org/wiki/Lancet_MMR_vaccine-autism_report
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:30831578&resultType=core&format=json
- WebFetch: https://en.wikipedia.org/wiki/H._Hugh_Fudenberg
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:15016483&resultType=core&format=json

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "The MMR vaccine causes autism."

**Roots:** Echo · **Grounding:** Primary differs · Mutated · Origin retracted
**Earliest instance found:** [Wakefield et al., *Ileal-lymphoid-nodular hyperplasia, non-specific colitis, and pervasive developmental disorder in children*, The Lancet](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320&resultType=core&format=json), 1998 (date from: byline, the Europe PMC and [Crossref](https://api.crossref.org/works/10.1016/S0140-6736(97)11096-0) records). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 8

### Chain
Your version: "The MMR vaccine causes autism" (where you met it: not given)
 ├─ [Poynter / PolitiFact, Madison Czopek](https://www.poynter.org/fact-checking/2026/do-vaccines-cause-autism/), 2026, Secondary → cites
 │   └─ [Wakefield et al., The Lancet](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320&resultType=core&format=json), 1998, Primary (abstract record opened; the Lancet's full text returned 403), root
 ├─ [Wikipedia, *Vaccines and autism*](https://en.wikipedia.org/wiki/Vaccines_and_autism), date unknown, Secondary → cites Wakefield et al. 1998 (root, above)
 ├─ [Wikipedia, *Lancet MMR vaccine-autism report*](https://en.wikipedia.org/wiki/Lancet_MMR_vaccine-autism_report), date unknown, Secondary → cites Wakefield et al. 1998 (root, above)
 ├─ [Rao & Andrade, *The MMR vaccine and autism: Sensation, refutation, retraction, and fraud*, Indian J Psychiatry](https://pmc.ncbi.nlm.nih.gov/articles/PMC3136032/), 2011, Secondary → cites Wakefield et al. 1998 (root, above)
 ├─ [Kimmel, *Vaccine adverse events: separating myth from reality*, Am Fam Physician](https://www.aafp.org/afp/2002/1201/p2113), 2002, Secondary → cites Wakefield et al. 1998 (root, above)
 └─ [Brian Deer, *Andrew Wakefield: the fraud investigation*](https://briandeer.com/wakefield/royal-video.htm), date unknown, Secondary → cites Wakefield et al. 1998 (root, above), and
     └─ Royal Free Hospital Medical School press conference and video news release, 1998, Primary (not opened, per the Deer page) → stopped: not opened

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Correlation stated as causation | In a case series, parents of 8 of the 12 children linked when their child's symptoms began to MMR vaccination. The paper described the bowel disease and developmental regression as *associated in time* with possible environmental triggers, and per [Kimmel](https://www.aafp.org/afp/2002/1201/p2113) it said it had not proved an association with the vaccine | The MMR vaccine causes autism | your version |
| Hedge dropped | The paper called for further study of the syndrome and its *possible* relation to the vaccine | The MMR vaccine causes autism | your version |
| Scope widened | 12 referred children, 9 diagnosed with autism, all with intestinal abnormalities: a proposed syndrome combining bowel disease and regression | The MMR vaccine causes autism | your version |

### Status of the root
- Crossref lists two updates to the paper: a [2010-02-06 retraction](https://api.crossref.org/works/10.1016/S0140-6736(97)11096-0) (DOI 10.1016/s0140-6736(10)60175-4) and a 2004-03-06 correction (DOI 10.1016/s0140-6736(04)15715-2). The [Lancet's retraction notice page](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(10)60175-4/abstract) returned 403 and was not opened.
- The [Europe PMC record](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320&resultType=core&format=json) tags the paper *Retracted Publication*. It lists retraction notices from 2004 and 2010 and a 2011 expression of concern in *Eur J Gastroenterol Hepatol*.
- 2004: ten of the co-authors published [*Retraction of an interpretation*](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:15016483&resultType=core&format=json) in The Lancet. The record opened is metadata only, with no text.
- [Rao & Andrade](https://pmc.ncbi.nlm.nih.gov/articles/PMC3136032/) report that the co-authors' 2004 retraction stated "no causal link was established between MMR vaccine and autism". They also report that the 2010 retraction followed findings of selective sampling and of investigations done without ethical clearance.
- Later study: [Hviid et al., Annals of Internal Medicine](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:30831578&resultType=core&format=json), 2019, a Danish nationwide cohort, reported an autism hazard ratio of 0.93 for MMR-vaccinated vs unvaccinated children. It concluded that MMR "does not trigger autism in susceptible children".
- The fact-check [Poynter / PolitiFact](https://www.poynter.org/fact-checking/2026/do-vaccines-cause-autism/), 2026, reports that large studies across many populations found no association between childhood vaccines and autism.
- Background: per [Wikipedia, *H. Hugh Fudenberg*](https://en.wikipedia.org/wiki/H._Hugh_Fudenberg), Fudenberg made the MMR–autism claim from the 1980s. He published a 1996 pilot study in *Biotherapy*, and the 1998 Lancet paper cites it. None of the retellings opened credits it as a source of the claim, so it is a precursor. Not opened.

### Cold trails
None.

### Confidence
Medium: the root was opened only as an abstract record, because the Lancet's full text and retraction notice pages returned 403; the press conference was not opened; and two nodes have no date.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
