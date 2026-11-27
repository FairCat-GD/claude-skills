---
case: retracted-origin-mmr-autism
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T19:16:27Z
cost_usd: 1.3656
duration_s: 183
turns: 37
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
- WebSearch: measles mumps rubella vaccine linked to autism claim
- WebSearch: Wakefield 1998 Lancet ileal-lymphoid-nodular hyperplasia MMR autism
- WebSearch: "12 children" Wakefield MMR autism paper
- WebSearch: origin of the MMR autism claim history first appeared
- WebSearch: MMR vaccine autism fact check Snopes OR "Full Fact" OR Reuters
- WebFetch: https://www.thelancet.com/pdfs/journals/lancet/PIIS0140-6736(97)11096-0.pdf
- WebFetch: https://en.wikipedia.org/wiki/MMR_vaccine_and_autism
- WebFetch: https://en.wikipedia.org/wiki/H._Hugh_Fudenberg
- WebFetch: https://www.ktep.org/2025-03-05/the-history-behind-an-enduring-public-health-falsehood-that-vaccines-cause-autism
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/S0140-6736(97)11096-0&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1007/BF02628672&resultType=core&format=json
- WebFetch: https://api.crossref.org/works/10.1016/S0140-6736(97)11096-0
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320&resultType=core&format=json
- WebFetch: https://link.springer.com/article/10.1007/BF02628672
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/S0140-6736(10)60175-4&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:20137807&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:15016483&resultType=core&format=json
- WebFetch: https://static1.squarespace.com/static/57698667d2b8574e2db7710a/t/591966f39de4bb3c019734fb/1494836984275/andrew-wakefiled-1998-lancet.pdf
- WebFetch: https://www.factcheck.org/2025/11/revised-cdc-website-about-autism-and-vaccines-is-not-evidence-based/
- WebFetch: https://www.gavi.org/vaccineswork/can-mmr-vaccines-cause-autism
- WebFetch: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(97)11096-0/fulltext
- WebFetch: https://www.bmj.com/content/342/bmj.c5347.full
- WebFetch: https://www.open.edu/openlearn/health-sports-psychology/health/the-mmr-vaccine-public-health-private-fears/content-section-2
- WebFetch: https://www.acpjournals.org/doi/10.7326/M18-2101
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:30831578&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:21209060&resultType=core&format=json
- WebFetch: https://briandeer.com/mmr/lancet-paper.htm
- WebFetch: https://api.crossref.org/works/10.1007/BF02628672

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "The MMR vaccine causes autism."

**Roots:** Independent · **Grounding:** Primary differs · Mutated · Origin retracted · Origin corrected
**Earliest instance found:** [Fudenberg, *Dialysable lymphocyte extract (DLyE) in infantile onset autism: a pilot study*, *Biotherapy*](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1007/BF02628672&resultType=core&format=json), 1996 (date from: byline, Europe PMC and [Crossref](https://api.crossref.org/works/10.1007/BF02628672) records). Its link to MMR is known only from Wikipedia, because the full text was behind a login wall. Earlier instances may exist.
**Roots:** 2 · **Retellings found:** 9

### Chain
Your version: "The MMR vaccine causes autism" (where you met it: not given)
 ├─ [FactCheck.org, McDonald & Yandell](https://www.factcheck.org/2025/11/revised-cdc-website-about-autism-and-vaccines-is-not-evidence-based/), 2025, Secondary → cites
 │   └─ [Wakefield et al., *Ileal-lymphoid-nodular hyperplasia, non-specific colitis, and pervasive developmental disorder in children*, *The Lancet* 351:637–41](https://briandeer.com/mmr/lancet-paper.htm), 1998, Primary, root 1 (abstract opened via [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320&resultType=core&format=json); full text opened in the copy on Brian Deer's site)
 ├─ [Gavi *VaccinesWork*, Geddes](https://www.gavi.org/vaccineswork/can-mmr-vaccines-cause-autism), 2025, Secondary → cites Wakefield et al. 1998 (root 1)
 ├─ [NPR *Throughline*, via KTEP](https://www.ktep.org/2025-03-05/the-history-behind-an-enduring-public-health-falsehood-that-vaccines-cause-autism), 2025, Secondary → cites Wakefield et al. 1998 (root 1)
 ├─ [OpenLearn, *The MMR vaccine: public health, private fears*](https://www.open.edu/openlearn/health-sports-psychology/health/the-mmr-vaccine-public-health-private-fears/content-section-2), date unknown, Secondary. It reports Wakefield's February 1998 press conference, where he called for single vaccines while saying there was no proof. → cites Wakefield et al. 1998 (root 1)
 ├─ [Wikipedia, *MMR vaccine and autism*](https://en.wikipedia.org/wiki/MMR_vaccine_and_autism), date unknown, Secondary. It says the link was first suggested in the early 1990s. → cites
 │   └─ Flaherty, *The Vaccine-Autism Connection*, *Annals of Pharmacotherapy*, 2011, (not opened), per Wikipedia → stopped: not opened
 └─ [Wikipedia, *H. Hugh Fudenberg*](https://en.wikipedia.org/wiki/H._Hugh_Fudenberg), date unknown, Secondary. It says Wakefield's 1998 paper cited Fudenberg's 1996 paper. → cites
     └─ [Fudenberg, *Biotherapy* 9:143–147](https://link.springer.com/article/10.1007/BF02628672), 1996, Primary (not opened, per Wikipedia, *H. Hugh Fudenberg*), root 2. The opened abstract does not mention MMR. Wikipedia reports that the full text says 15 *True Autism* patients developed symptoms within a week of MMR.

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Hedge dropped | the paper reports [“We did not prove an association”](https://briandeer.com/mmr/lancet-paper.htm) between MMR and the syndrome it describes | The MMR vaccine causes autism | your version |
| Correlation stated as causation | parents of 8 of the 12 children linked when symptoms began to the MMR jab; the paper reports this as a timing link only | The MMR vaccine causes autism | your version |
| Scope widened | 12 children referred to a paediatric gastroenterology unit with both bowel disease and developmental regression | The MMR vaccine causes autism | your version |

### Status of the root
- Ten of the 13 co-authors published *Retraction of an interpretation* in *The Lancet* 363:750 in March 2004 ([Europe PMC record](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:15016483&resultType=core&format=json)). Crossref files it as a correction ([Crossref record](https://api.crossref.org/works/10.1016/S0140-6736(97)11096-0)).
- *The Lancet* fully retracted the paper in February 2010, in vol. 375, p. 445 ([Europe PMC record](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:20137807&resultType=core&format=json)). Crossref lists this retraction too, dated 6 February 2010.
- In January 2011 the *BMJ* published an editorial by Godlee, Smith and Marcovitch titled *Wakefield's article linking MMR vaccine and autism was fraudulent* ([Europe PMC record](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:21209060&resultType=core&format=json)). The *BMJ*'s own page returned 403.
- Major later study: Hviid et al. followed 657,461 Danish children in a cohort study in *Annals of Internal Medicine* (2019). It concluded that [“MMR vaccination does not increase the risk for autism”](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:30831578&resultType=core&format=json).
- Fudenberg 1996: Crossref shows no retraction, correction or expression of concern ([Crossref record](https://api.crossref.org/works/10.1007/BF02628672)). The full text could not be opened.

### Cold trails
- [Wikipedia, *H. Hugh Fudenberg*](https://en.wikipedia.org/wiki/H._Hugh_Fudenberg), date unknown: it says Fudenberg began claiming in the 1980s that MMR causes autism, and gives no source for that date.

### Confidence
Medium: the Wakefield root was opened and its retraction notices were found, but root 2 (Fudenberg 1996) is known only from Wikipedia, and several dates in the chain are unknown.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
