---
case: retracted-origin-mmr-autism
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T19:16:16Z
cost_usd: 1.3813
duration_s: 182
turns: 36
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
- WebSearch: measles mumps rubella vaccine autism link claim
- WebSearch: Wakefield 1998 Lancet ileal-lymphoid-nodular hyperplasia autism MMR
- WebSearch: origin of MMR autism claim first appeared
- WebSearch: MMR vaccine autism fact check
- WebSearch: Wakefield 1998 press conference Royal Free single vaccines
- WebFetch: https://www.thelancet.com/pdfs/journals/lancet/PIIS0140-6736(97)11096-0.pdf
- WebFetch: https://theconversation.com/mondays-medical-myth-the-mmr-vaccine-causes-autism-3739
- WebFetch: https://en.wikipedia.org/wiki/MMR_vaccine_and_autism
- WebFetch: https://en.wikipedia.org/wiki/H._Hugh_Fudenberg
- WebFetch: https://briandeer.com/solved/bmj-wakefield-timeline.htm
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/S0140-6736(97)11096-0&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1007/BF02628672&resultType=core&format=json
- WebFetch: https://api.crossref.org/works/10.1016/S0140-6736(97)11096-0
- WebFetch: https://briandeer.com/wakefield/royal-video.htm
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320&resultType=core&format=json
- WebFetch: https://static1.squarespace.com/static/57698667d2b8574e2db7710a/t/591966f39de4bb3c019734fb/1494836984275/andrew-wakefiled-1998-lancet.pdf
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/S0140-6736(10)60175-4&resultType=core&format=json
- WebFetch: https://link.springer.com/article/10.1007/BF02628672
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:20137807&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:15016483&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1345/aph.1Q318&resultType=core&format=json
- WebFetch: https://www.sciencedirect.com/science/article/abs/pii/S0140673699012398
- WebFetch: https://www.chop.edu/vaccine-education-center/vaccine-safety/vaccines-and-other-conditions/autism
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:10376617&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1136/bmj.c5347&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.7326/M18-2101&resultType=core&format=json
- WebFetch: https://www.open.edu/openlearn/mod/oucontent/view.php?id=2552&printable=1

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "The MMR vaccine causes autism."

**Roots:** Independent · **Grounding:** Primary differs · Mutated · Origin retracted · Origin corrected
**Earliest instance found:** [Fudenberg, *Dialysable lymphocyte extract (DLyE) in infantile onset autism: a pilot study*, Biotherapy 9:143–147](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1007/BF02628672&resultType=core&format=json), 1996 (date from: byline, Europe PMC record). The abstract does not mention MMR. The MMR passage is known only from the [Wikipedia article on Fudenberg](https://en.wikipedia.org/wiki/H._Hugh_Fudenberg), which quotes the full text: 15 children with autism developed symptoms within a week of MMR vaccination. Earlier instances may exist.
**Roots:** 2 · **Retellings found:** 11

### Chain
Your version: "The MMR vaccine causes autism" (where you met it: not given)
 ├─ [Children's Hospital of Philadelphia, *Vaccines and autism*](https://www.chop.edu/vaccine-education-center/vaccine-safety/vaccines-and-other-conditions/autism), date unknown (only a 2026 review date), Secondary → cites
 │   └─ Wakefield et al. 1998 (root 1, below)
 ├─ [The Open University, *The MMR vaccine: public health, private fears*](https://www.open.edu/openlearn/mod/oucontent/view.php?id=2552&printable=1), 2004, Secondary → cites
 │   └─ Wakefield et al. 1998 (root 1, below). It adds that the link was put forward at a press conference, not stated outright in the paper.
 ├─ [Dunlop, *Monday's medical myth: the MMR vaccine causes autism*, The Conversation](https://theconversation.com/mondays-medical-myth-the-mmr-vaccine-causes-autism-3739), 2011, Secondary → cites
 │   ├─ [Brian Deer, Royal Free video news release page](https://briandeer.com/wakefield/royal-video.htm), date unknown, Secondary → cites
 │   │   └─ Royal Free Hospital press conference and video news release, Feb 1998, Primary (not opened, per Brian Deer's page). These were Wakefield's own spoken statements, the same team as root 1 → stopped: not opened
 │   └─ Wakefield et al. 1998 (root 1, below)
 ├─ [Brian Deer, *Timeline of Wakefield MMR scandal*, BMJ](https://briandeer.com/solved/bmj-wakefield-timeline.htm), 2011, Secondary → cites
 │   └─ the Feb 1998 press conference (above)
 ├─ [Wikipedia, *MMR vaccine and autism*](https://en.wikipedia.org/wiki/MMR_vaccine_and_autism), date unknown, Tertiary → cites
 │   └─ [Flaherty, *The vaccine-autism connection…*, Annals of Pharmacotherapy 45:1302–4](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1345/aph.1Q318&resultType=core&format=json), 2011, Secondary → cites
 │       └─ Wakefield et al. 1998 (root 1, below)
 ├─ [Wikipedia, *H. Hugh Fudenberg*](https://en.wikipedia.org/wiki/H._Hugh_Fudenberg), date unknown, Secondary → cites
 │   └─ Fudenberg, Biotherapy 9:143–147, 1996, Primary (not opened, per Wikipedia, *H. Hugh Fudenberg*), root 2. The [Springer full text](https://link.springer.com/article/10.1007/BF02628672) redirected to a login wall. The [Europe PMC abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1007/BF02628672&resultType=core&format=json) opened but does not mention MMR.
 └─ [Wakefield, Murch, Anthony et al., *Ileal-lymphoid-nodular hyperplasia, non-specific colitis, and pervasive developmental disorder in children*, Lancet 351:637–41](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320&resultType=core&format=json), Feb 1998, Primary, root 1. The abstract was opened through the Europe PMC record after [the Lancet PDF](https://www.thelancet.com/pdfs/journals/lancet/PIIS0140-6736(97)11096-0.pdf) returned 403 and [a mirror PDF](https://static1.squarespace.com/static/57698667d2b8574e2db7710a/t/591966f39de4bb3c019734fb/1494836984275/andrew-wakefiled-1998-lancet.pdf) returned no readable text.

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Correlation stated as causation | Parents of 8 of the 12 children linked the onset of symptoms to MMR. The paper's interpretation speaks of a pattern "which was generally associated in time with possible environmental triggers" | The MMR vaccine causes autism | [The Open University](https://www.open.edu/openlearn/mod/oucontent/view.php?id=2552&printable=1), 2004 |
| Hedge dropped | the link is put as *possible* and *associated in time*, as reported by parents | The MMR vaccine causes autism | [The Open University](https://www.open.edu/openlearn/mod/oucontent/view.php?id=2552&printable=1), 2004 |
| Scope widened | a case series of 12 children with bowel symptoms and developmental disorder, referred to one hospital unit | The MMR vaccine causes autism | [The Open University](https://www.open.edu/openlearn/mod/oucontent/view.php?id=2552&printable=1), 2004 |

### Status of the root
- **Retraction, 2010:** *The Lancet* fully retracted the 1998 paper in a [notice at Lancet 375:445](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:20137807&resultType=core&format=json) (Feb 2010). The paper's [Crossref record](https://api.crossref.org/works/10.1016/S0140-6736(97)11096-0) lists the retraction dated 2010-02-06, with Retraction Watch as the source of that entry, and titles the paper *RETRACTED*.
- **Partial retraction, 2004:** 10 of the 13 authors published [*Retraction of an interpretation*, Lancet 363:750](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:15016483&resultType=core&format=json) (March 2004). Crossref types it as a correction, dated 2004-03-06. The notice's text was not in the record, so it was not read.
- **Expression of concern:** the [Europe PMC record of the paper](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320&resultType=core&format=json) also links an expression of concern in Eur J Gastroenterol Hepatol, Nov 2011. That notice was not opened.
- **Misconduct findings:** per [Brian Deer's BMJ timeline](https://briandeer.com/solved/bmj-wakefield-timeline.htm), in May 2010 a General Medical Council panel ordered Wakefield and Walker-Smith erased from the UK medical register. The same timeline records that in February 1996 a lawyer working for parents retained Wakefield. It also records that in June 1997 Wakefield filed a patent for a single measles vaccine.
- **Deer, *How the case against the MMR vaccine was fixed*, BMJ 2011;342:c5347:** the [record was opened](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1136/bmj.c5347&resultType=core&format=json), but it holds no abstract and the full text is subscription-only, so its findings were not read.
- **Later study, Taylor et al. 1999:** [Lancet 353:2026–9](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:10376617&resultType=core&format=json) looked at 498 children with autism in North Thames, UK. It found no step-up in cases after MMR was introduced in 1988 and no clustering of onset after vaccination. The authors concluded their analyses did not support a causal association.
- **Later study, Hviid et al. 2019:** [Annals of Internal Medicine 170:513–20](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.7326/M18-2101&resultType=core&format=json) followed 657,461 Danish children, with a fully adjusted autism hazard ratio of 0.93 (95% CI 0.85–1.02). It concluded that MMR vaccination "does not increase the risk for autism."
- **Fudenberg 1996 (root 2):** no status was checked, since the full text was behind a login wall and the fetch budget ran out.
- **Not checked:** a separate Retraction Watch or PubPeer search for the 1998 paper was not run beyond the Crossref entries above.

### Cold trails
- [Wikipedia, *H. Hugh Fudenberg*](https://en.wikipedia.org/wiki/H._Hugh_Fudenberg), date unknown: says Fudenberg was claiming an MMR–autism link in the 1980s, with no citation for that date.
- [Wikipedia, *MMR vaccine and autism*](https://en.wikipedia.org/wiki/MMR_vaccine_and_autism), date unknown: dates the first suggestion of the link to the early 1990s. The source it cites ([Flaherty 2011](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1345/aph.1Q318&resultType=core&format=json)) names Wakefield in 1998 in its abstract and gives no early-1990s origin.

### Confidence
Medium: root 1 was opened only as its abstract record, root 2 (Fudenberg 1996) and the 1998 press conference were not opened, and three nodes have no date.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
