---
case: retracted-origin-mmr-autism
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:26:32Z
cost_usd: 1.3213
duration_s: 164
turns: 35
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
- WebSearch: MMR jab linked to autism claim
- WebSearch: Wakefield 1998 Lancet ileal-lymphoid-nodular hyperplasia MMR autism
- WebSearch: origin of MMR autism claim first appeared 1998 press conference
- WebSearch: MMR vaccine autism fact check
- WebSearch: Lancet retraction notice Wakefield 2010
- WebFetch: https://www.thelancet.com/pdfs/journals/lancet/PIIS0140-6736(97)11096-0.pdf
- WebFetch: https://en.wikipedia.org/wiki/Lancet_MMR_vaccine-autism_report
- WebFetch: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(97)11096-0/fulltext
- WebFetch: https://api.crossref.org/works/10.1016/S0140-6736(97)11096-0
- WebFetch: https://theconversation.com/mondays-medical-myth-the-mmr-vaccine-causes-autism-3739
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/9500320/
- WebFetch: https://static1.squarespace.com/static/57698667d2b8574e2db7710a/t/591966f39de4bb3c019734fb/1494836984275/andrew-wakefiled-1998-lancet.pdf
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/20137807/
- WebFetch: https://pubmed.ncbi.nlm.nih.gov/15016483/
- WebFetch: http://briandeer.com/wakefield/royal-video.htm
- WebFetch: https://briandeer.com/mmr/lancet-paper.htm
- WebFetch: https://edition.cnn.com/2010/HEALTH/02/02/lancet.retraction.autism/
- WebFetch: https://en.wikipedia.org/wiki/Lancet_MMR_vaccine-autism_report
- WebFetch: https://sciencebasedmedicine.org/lancet-retracts-wakefield-article/
- WebFetch: https://www.acpjournals.org/doi/10.7326/M18-2101
- WebFetch: https://en.wikipedia.org/wiki/Wakefield_MMR-autism_fraud
- WebFetch: https://www.poynter.org/fact-checking/2026/do-vaccines-cause-autism/
- WebFetch: https://autismsciencefoundation.org/wp-content/uploads/2019/03/vaccine.2019.pdf
- WebFetch: https://www.bmj.com/content/342/bmj.c7452
- WebFetch: https://www.sciencedirect.com/science/article/abs/pii/S0140673699012398
- WebFetch: https://www.gavi.org/vaccineswork/can-mmr-vaccines-cause-autism

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "The MMR vaccine causes autism."

**Roots:** Echo · **Grounding:** Primary differs · Mutated · Origin retracted · Origin corrected
**Earliest instance found:** [Wakefield AJ, Murch SH, Anthony A, et al., *Ileal-lymphoid-nodular hyperplasia, non-specific colitis, and pervasive developmental disorder in children*, The Lancet 351:637–41](https://briandeer.com/mmr/lancet-paper.htm), 1998 (date from: byline, 28 February 1998, on the reproduced paper). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 6

### Chain
Your version: "The MMR vaccine causes autism" (where you met it: not given)
 ├─ [Poynter / PolitiFact, *Decades of research show vaccines do not cause autism*](https://www.poynter.org/fact-checking/2026/do-vaccines-cause-autism/), 2026, Secondary → cites
 │   └─ Wakefield et al., *The Lancet*, 1998 (root, below)
 ├─ [Gavi VaccinesWork, *Can MMR vaccines cause autism?*](https://www.gavi.org/vaccineswork/can-mmr-vaccines-cause-autism), 2025, Secondary → cites
 │   └─ Wakefield et al., *The Lancet*, 1998 (root, below)
 ├─ [The Conversation, *Monday's medical myth: the MMR vaccine causes autism*](https://theconversation.com/mondays-medical-myth-the-mmr-vaccine-causes-autism-3739), 2011, Secondary → cites
 │   └─ Royal Free Hospital press conference and video news release, February 1998, Primary (not opened, per [Wikipedia](https://en.wikipedia.org/wiki/Lancet_MMR_vaccine-autism_report) and [briandeer.com](http://briandeer.com/wakefield/royal-video.htm)) → cites
 │       └─ Wakefield et al., *The Lancet*, 1998 (root, below)
 └─ [Wikipedia, *Lancet MMR vaccine-autism report*](https://en.wikipedia.org/wiki/Lancet_MMR_vaccine-autism_report), date unknown, Tertiary → cites
     └─ [Wakefield et al., *Ileal-lymphoid-nodular hyperplasia, non-specific colitis, and pervasive developmental disorder in children*, The Lancet](https://briandeer.com/mmr/lancet-paper.htm), 1998, Primary (full text read from a reproduction on Brian Deer's site; The Lancet's own [PDF](https://www.thelancet.com/pdfs/journals/lancet/PIIS0140-6736(97)11096-0.pdf) and [article page](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(97)11096-0/fulltext) returned 403)

- **What the root reports.** It is a case series of 12 children referred to the Royal Free Hospital who had bowel disease and developmental regression. In 8 of the 12, the onset of behavioural symptoms was linked to MMR vaccination "either by the parents or by the child's physician." The Discussion says: ["We did not prove an association between measles, mumps, and rubella vaccine"](https://briandeer.com/mmr/lancet-paper.htm).
- **Where the public version came from.** The Conversation (2011) says ["The tale was first suggested by Andrew Wakefield at a 1998 press conference"](https://theconversation.com/mondays-medical-myth-the-mmr-vaccine-causes-autism-3739). Wikipedia reports that at that press conference Wakefield said ["I can't support the continued use of these three vaccines given in combination"](https://en.wikipedia.org/wiki/Lancet_MMR_vaccine-autism_report). It also says that in the hospital's video news release he called for MMR to be suspended in favour of single vaccines.
- **Background found along the way.** Citing Brian Deer's 2004 *Sunday Times* investigation, Wikipedia says that about two years before publication, lawyer Richard Barr hired Wakefield as an expert witness for a planned class action over "vaccine damage." The children were recruited only after that. The UK Legal Aid Board assigned £55,000 to the first stage of the research.

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Hedge dropped | the authors write that they did not prove an association between MMR and the syndrome | The MMR vaccine causes autism | your version. No opened node asserts it without the hedge. The nearest is Wakefield's call to suspend MMR at the 1998 press conference (not opened, reported by [Wikipedia](https://en.wikipedia.org/wiki/Lancet_MMR_vaccine-autism_report)) |
| Correlation stated as causation | parents or physicians linked the timing of symptom onset to MMR in 8 of 12 children | The MMR vaccine causes autism | your version |
| Scope widened | 12 referred children with bowel disease and developmental regression (9 of them autistic) | the MMR vaccine, in general | your version |
| Other: subject shifted | the paper describes a bowel syndrome alongside developmental regression | autism alone | your version |

### Status of the root
- **Fully retracted, 2010.** The [Crossref record](https://api.crossref.org/works/10.1016/S0140-6736(97)11096-0) lists a Retraction (DOI 10.1016/s0140-6736(10)60175-4, 2010-02-06, Retraction Watch record 4036) and gives the title as *RETRACTED: …*. The notice, as quoted by [Science-Based Medicine](https://sciencebasedmedicine.org/lancet-retracts-wakefield-article/) on 3 February 2010, ends: "Therefore we fully retract this paper from the published record." It gives these reasons: the paper's claims that the children were "consecutively referred" and that the ethics committee had "approved" the investigations were proven false. The notice cites the UK General Medical Council panel's judgment of 28 January 2010.
- **Correction, 2004.** The same [Crossref record](https://api.crossref.org/works/10.1016/S0140-6736(97)11096-0) lists a Correction (DOI 10.1016/s0140-6736(04)15715-2, 2004-03-06, Retraction Watch record 17269). [Wikipedia](https://en.wikipedia.org/wiki/Lancet_MMR_vaccine-autism_report) identifies it as *Retraction of an interpretation* (Lancet 363:750), in which 10 of the 12 co-authors withdrew the paper's interpretation. The PubMed pages for this notice and for the 2010 retraction would not load (cookie wall).
- **Major later study.** [Gavi](https://www.gavi.org/vaccineswork/can-mmr-vaccines-cause-autism) (2025) reports on Hviid and colleagues, *Measles, Mumps, Rubella Vaccination and Autism: A Nationwide Cohort Study* (2019). The study followed more than 650,000 children born in Denmark from 1999 to 2010 and found no higher autism risk in vaccinated children, including those with risk factors. The study itself returned 403 when fetched ([acpjournals.org](https://www.acpjournals.org/doi/10.7326/M18-2101)), and its PDF copy gave no readable text.
- **Other later reviews.** Poynter/PolitiFact (2026) lists other later reviews among its sources, including NEJM 2002, the Institute of Medicine (2004) and a WHO evidence review covering 2010–2025. None of these was opened here.
- **Taylor et al., *Lancet* 1999.** This UK epidemiological study of MMR and autism could not be opened (403 from ScienceDirect).
- **Current US policy.** A [FactCheck.org](https://www.factcheck.org/2025/11/revised-cdc-website-about-autism-and-vaccines-is-not-evidence-based/) piece (November 2025) appeared in search results reporting a revised CDC web page on autism and vaccines. It was not opened, so its content is not used here.

### Cold trails
None.

### Confidence
Medium. The root's text was opened and dated by its byline, and its status comes from the Crossref record and a quoted copy of the notice. But the paper was read from a reproduction rather than the journal's site, the press-conference node was not opened, and the 2019 cohort study is known only from a report of it.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
