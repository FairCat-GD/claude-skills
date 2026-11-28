---
case: retracted-origin-mmr-autism
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: bf06fdf9900c0609534800b3c875cea27fc5b3b8
date: 2026-11-28T00:15:52Z
cost_usd: 1.3569
duration_s: 162
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
- WebSearch: MMR autism link claim Wakefield 1998 Lancet
- WebSearch: origin of the claim MMR vaccine autism first appeared
- WebSearch: MMR autism fact check Snopes OR "Full Fact" OR Reuters
- WebSearch: Wakefield press conference 1998 single vaccines MMR
- WebSearch: Lancet retraction Wakefield 2010 ileal-lymphoid-nodular hyperplasia
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/S0140-6736(97)11096-0&resultType=core&format=json
- WebFetch: https://www.factcheck.org/2026/08/trumps-false-mmr-vaccine-claims/
- WebFetch: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(10)60175-4/abstract
- WebFetch: https://api.crossref.org/works/10.1016/S0140-6736(97)11096-0
- WebFetch: https://briandeer.com/solved/key-dates.htm
- WebFetch: https://politifact.com/article/2026/aug/13/vaccines-autism-research-evidence/
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320&resultType=core&format=json
- WebFetch: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(04)15715-2/fulltext
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC2908388/
- WebSearch: "We did not prove an association between measles, mumps, and rubella vaccine and the syndrome described"
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:20137807&resultType=core&format=json
- WebFetch: https://hero.epa.gov/reference/4104953/
- WebFetch: https://www.aafp.org/pubs/afp/issues/2002/1201/p2113.html
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:30831578&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:10376617&resultType=core&format=json

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "The MMR vaccine causes autism."

**Roots:** Echo · **Grounding:** Primary differs · Mutated · Origin retracted
**Earliest instance found:** [Wakefield et al., *Ileal-lymphoid-nodular hyperplasia, non-specific colitis, and pervasive developmental disorder in children*, The Lancet](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320&resultType=core&format=json), 1998 (date from: byline, February 1998, vol. 351, pp. 637–641). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 6

### Chain
Your version: "The MMR vaccine causes autism" (where you met it: not given)
 ├─ [FactCheck.org, *Trump's False MMR Vaccine Claims*](https://www.factcheck.org/2026/08/trumps-false-mmr-vaccine-claims/), 2026, Secondary → cites
 │   ├─ [Brian Deer, *MMR: key dates in the crisis* (reprint of a *Sunday Times* piece)](https://briandeer.com/solved/key-dates.htm), 2009, Secondary → cites Wakefield et al. 1998 (below)
 │   └─ [Wakefield et al., *The Lancet*](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320&resultType=core&format=json), 1998, Primary, root
 ├─ [PolitiFact, *Vaccine research spans decades and doesn't show they cause autism*](https://politifact.com/article/2026/aug/13/vaccines-autism-research-evidence/), 2026, Secondary → cites Wakefield et al. 1998 (above). It names the 1998 Lancet paper and links PolitiFact's 2019 *5 facts about vaccines* (not opened).
 ├─ [Gerber & Offit, *Vaccines and Autism: A Tale of Shifting Hypotheses*, Clin Infect Dis](https://pmc.ncbi.nlm.nih.gov/articles/PMC2908388/), 2009, Secondary → cites Wakefield et al. 1998 (above)
 └─ [Kimmel, *Vaccine Adverse Events: Separating Myth from Reality*, Am Fam Physician](https://www.aafp.org/pubs/afp/issues/2002/1201/p2113.html), 2002, Secondary → cites Wakefield et al. 1998 (above)

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Correlation stated as causation | In 8 of 12 children, parents linked the onset of symptoms to MMR vaccination. The authors read this as a link in time with *possible* environmental triggers. ([abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320&resultType=core&format=json)) | The MMR vaccine causes autism | your version |
| Hedge dropped | The interpretation is framed as a possible trigger needing more study, and the discussion says no association was proven (per AAFP 2002) | The MMR vaccine causes autism | your version |
| Scope widened | A case series of 12 children referred to a London paediatric gastroenterology unit for bowel symptoms, with no control group | The MMR vaccine causes autism | your version |

### Status of the root
- The [Crossref record](https://api.crossref.org/works/10.1016/S0140-6736(97)11096-0) titles the paper *RETRACTED*. It lists two updates: a retraction dated 2010-02-06 (DOI 10.1016/s0140-6736(10)60175-4) and an item dated 2004-03-06 that it classes as a correction (DOI 10.1016/s0140-6736(04)15715-2). Both come from Retraction Watch records.
- The [Europe PMC record](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9500320&resultType=core&format=json) tags the paper *Retracted Publication*. It lists retractions in the Lancet on 6 March 2004 (vol. 363, p. 750) and 6 February 2010 (vol. 375, p. 445), and an expression of concern in Eur J Gastroenterol Hepatol in 2011.
- Retraction notice: Europe PMC's [record of the 2010 notice](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:20137807&resultType=core&format=json) classes it as a *Retraction Notice* for PMID 9500320. The notice's own text did not open: the Lancet page returned 403, and the Europe PMC and [EPA HERO](https://hero.epa.gov/reference/4104953/) records give no body text. The 2004 notice page also returned 403. PubPeer was not checked.
- Wakefield et al. 1998, as [AAFP 2002](https://www.aafp.org/pubs/afp/issues/2002/1201/p2113.html) quotes its discussion: "We did not prove an association between measles, mumps, and rubella vaccine".
- Later study: [Taylor et al., Lancet, 1999](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:10376617&resultType=core&format=json) looked at 498 autism cases in eight North Thames districts. Its analyses did not support a causal association between MMR and autism, and it says any such association would be too rare to detect in that sample.
- Later study: [Hviid et al., Ann Intern Med, 2019](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:30831578&resultType=core&format=json), a Danish registry cohort of 657,461 children, concluded that it "strongly supports that MMR vaccination does not increase the risk for autism".
- Background: [Brian Deer's chronology](https://briandeer.com/solved/key-dates.htm) dates the story's start before the paper. In February 1996, some parents were raising concerns about the vaccine and solicitor Richard Barr hired Wakefield. In June 1996, Wakefield and Barr asked the Legal Aid Board to fund research linking MMR and autism. In February 1998, Wakefield held a press conference recommending single vaccines at yearly intervals in place of MMR, without disclosing his interests. No retelling found credits these earlier parental or legal claims as the claim's source.

### Cold trails
None.

### Confidence
High: the root's abstract was opened with a byline date, and every retelling linking back to it was opened, although the retraction notices' own text could not be fetched.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
