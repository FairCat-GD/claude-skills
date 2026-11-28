---
case: retracted-origin-mmr-autism
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: bf06fdf9900c0609534800b3c875cea27fc5b3b8
date: 2026-11-28T00:13:48Z
cost_usd: 1.2154
duration_s: 137
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
- WebSearch: "MMR vaccine causes autism"
- WebSearch: origin of MMR autism claim Wakefield 1998 Lancet
- WebSearch: Wakefield Lancet 1998 ileal-lymphoid-nodular hyperplasia retraction
- WebSearch: MMR autism link fact check
- WebSearch: Wakefield press conference 1998 single vaccines MMR how the scare began
- WebSearch: "12 children" MMR autism study Wakefield what it actually found
- WebFetch: https://www.thelancet.com/pdfs/journals/lancet/PIIS0140-6736(97)11096-0.pdf
- WebFetch: https://www.gavi.org/vaccineswork/can-mmr-vaccines-cause-autism
- WebFetch: https://www.thedailybeast.com/mmr-vaccine-scare-andrew-wakefields-fraudulent-study/
- WebFetch: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(10)60175-4/abstract
- WebFetch: https://api.crossref.org/works/10.1016/S0140-6736(97)11096-0
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/S0140-6736(97)11096-0&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/S0140-6736(10)60175-4&resultType=core&format=json
- WebFetch: https://www.open.edu/openlearn/health-sports-psychology/health/the-mmr-vaccine-public-health-private-fears/content-section-2
- WebFetch: https://www.bmj.com/content/342/bmj.c7452.full
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:20137807&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:21209059&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:15016483&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:30831578&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:12421889&resultType=core&format=json

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "The MMR vaccine causes autism"

**Roots:** Echo · **Grounding:** Primary differs · Mutated · Origin retracted · Origin corrected
**Earliest instance found:** [Wakefield et al., *The Lancet*](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320&resultType=core&format=json), 1998 (date from: byline). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 4

### Chain
Your version: "The MMR vaccine causes autism" (where you met it: not given)
 └─ [Gavi, *Can MMR vaccines cause autism?*](https://www.gavi.org/vaccineswork/can-mmr-vaccines-cause-autism), 2025, Secondary → cites
     ├─ [Wakefield AJ, Murch SH et al., *Ileal-lymphoid-nodular hyperplasia, non-specific colitis, and pervasive developmental disorder in children*, The Lancet 351:637–641](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320&resultType=core&format=json), 1998, Primary, root
     └─ [OpenLearn, *The MMR vaccine: public health, private fears*](https://www.open.edu/openlearn/health-sports-psychology/health/the-mmr-vaccine-public-health-private-fears/content-section-2), date unknown, Secondary → cites
         ├─ Wakefield et al., 1998 (the root above)
         └─ Brian Deer, *Sunday Times*, 22 February 2004, 2004, (not opened), per OpenLearn → stopped: not opened

The Gavi page credits the 1998 paper as the start of the concern. For Wakefield's press-conference advice to give the three vaccines separately, it links to the OpenLearn page. OpenLearn takes Wakefield's press-conference remarks from Deer's 2004 article.

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Hedge dropped | Parents of most of the 12 children dated symptom onset to MMR, and the authors tied the findings in time to *possible* environmental triggers | The MMR vaccine causes autism | your version |
| Correlation stated as causation | Parents reported that the symptoms followed the vaccine in time; the abstract does not claim a tested cause | The MMR vaccine causes autism | your version |
| Scope widened | A case series of 12 children referred to a gastroenterology clinic with bowel disease and developmental regression, 9 of them diagnosed with autism | The MMR vaccine causes autism | your version |

### Status of the root
- [Europe PMC's record of the 1998 paper](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320&resultType=core&format=json) tags it *Retracted Publication*. It lists two retraction entries (Lancet 2004;363:750 and Lancet 2010;375:445) and an expression of concern in *Eur J Gastroenterol Hepatol* 2011;23:1082.
- [Crossref record](https://api.crossref.org/works/10.1016/S0140-6736(97)11096-0): lists a retraction, DOI 10.1016/s0140-6736(10)60175-4, dated 6 February 2010, and a correction, DOI 10.1016/s0140-6736(04)15715-2, dated 6 March 2004.
- 2010 retraction: [Europe PMC's record of the notice](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:20137807&resultType=core&format=json) (Lancet 375(9713):445) confirms that it retracts the 1998 article. The notice's own text, on The Lancet's site, returned 403.
- 2004: [Europe PMC's record](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:15016483&resultType=core&format=json) shows *Retraction of an interpretation* by 10 of the paper's co-authors, Murch SH and others (Wakefield is not among them). Its text is behind a paywall, so it was not opened.
- The 1998 paper's full text (the Lancet PDF returned 403): the [OpenLearn page](https://www.open.edu/openlearn/health-sports-psychology/health/the-mmr-vaccine-public-health-private-fears/content-section-2) quotes the paper's authors as writing "We did not prove an association".
- Deer, *How the case against the MMR vaccine was fixed*, BMJ 342:c5347, 2011: [Europe PMC record](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:21209059&resultType=core&format=json) opened. The article text returned 403.
- Madsen et al., NEJM 2002, a cohort of 537,303 Danish children: [the abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:12421889&resultType=core&format=json) concludes the study gives "strong evidence against the hypothesis that MMR vaccination causes autism".
- Hviid et al., Annals of Internal Medicine 2019, a cohort of 657,461 Danish children: [the abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:30831578&resultType=core&format=json) says the study "strongly supports that MMR vaccination does not increase the risk for autism". It reports a hazard ratio of 0.93 (95% CI 0.85–1.02).

### Cold trails
None.

### Confidence
Medium: the root's abstract record, its retraction records and the citing pages were all opened, but the paper's full text, the notice texts and Deer's 2004 article were not.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
