---
case: personal-chain-bilingual-speech
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:44:04Z
cost_usd: 1.7619
duration_s: 195
turns: 34
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- Read: <plugin>/skills/provenance-tracer/references/labels.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- WebSearch: "bilingual children start speaking later"
- WebSearch: bilingualism causes language delay in children myth origin
- WebSearch: bilingual children first words age study monolingual milestones Petitto
- WebSearch: history of belief bilingualism harmful children early 20th century studies Saer 1923 language handicap
- WebSearch: where does the idea bilingual kids talk later come from
- WebSearch: fact check bilingual children speech delay claim
- WebFetch: https://www.spanish.academy/blog/are-bilingual-children-more-likely-to-experience-a-speech-or-language-delay/
- WebFetch: https://littlewords.ai/blog/bilingual-children-speech-delay-myth
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC10395373/
- WebFetch: https://pubs.asha.org/doi/10.1044/2023_JSLHR-23-00117
- WebSearch: KQED Izzy Bloom bilingualism "language handicap" anti-immigrant
- WebSearch: Madorah Smith 1939 bilingualism Hawaii preschool children English retarded language development
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1044/2023_JSLHR-23-00117&resultType=core&format=json
- WebFetch: https://web.stanford.edu/~hakuta/www/research/publications/(1987)%20-%20BILINGUALISM%20AND%20COGNITIVE%20DEVELOPMENT%20THREE%20PERSPE.pdf
- WebFetch: https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC11361784/
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22Dual%20language%20exposure%20and%20early%20bilingual%20development%22&resultType=core&format=json
- WebFetch: https://www.levyinstitute.org/pubs/wp/229.pdf
- WebSearch: "Some light on the problem of bilingualism" Smith 1939 full text
- WebSearch: bilingual children speak later Forbes OR "Harvard Business Review" OR Economist OR "Fast Company" language delay
- WebFetch: https://api.crossref.org/works/10.1017/S0305000910000759
- WebFetch: https://commons.und.edu/cgi/viewcontent.cgi?article=10630&context=theses
- WebFetch: https://files.eric.ed.gov/fulltext/ED273152.pdf
- WebFetch: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0BFAB689DC70E5A2A5220976E1939948/S0305000924000655a.pdf/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers.pdf
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1017/S0305000924000655&resultType=core&format=json
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:11449947&resultType=core&format=json

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- Personal chain taken from your message: your manager told you, and they had read it in a business magazine. The magazine is not named, so it was not searched, and no year was given.

## Provenance: "Bilingual children start speaking later."

**Roots:** Independent · **Grounding:** Primary differs · Mutated
**Earliest instance found:** Smith, *Some light on the problem of bilingualism as found from a study of the progress in mastery of English among preschool children of non-American ancestry in Hawaii*, Genetic Psychology Monographs 21, 1939 (date from: cited by [A History of Speech-Language Pathology, Madorah Smith entry](https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/)). Earlier instances may exist.
**Roots:** 2 · **Retellings found:** 10

### Chain
Your version: "Bilingual children start speaking later." (you heard it: Hearsay, from your manager, who read it in a business magazine; year not given; no matching node found)
 ├─ [Duchan, *A History of Speech-Language Pathology*: Madorah Elizabeth Smith](https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/), date unknown, Secondary → cites
 │   └─ Smith, *Some light on the problem of bilingualism…*, Genetic Psychology Monographs 21, 1939, Primary (not opened, per Duchan's page), root 1
 ├─ [Hoff, *Why bilingual development is not easy*, Advances in Child Development and Behavior 61](https://pmc.ncbi.nlm.nih.gov/articles/PMC10395373/), 2021, Secondary → cites
 │   └─ [Hoff, Core, Place, Rumiche, Señor & Parra, *Dual language exposure and early bilingual development*, Journal of Child Language](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22Dual%20language%20exposure%20and%20early%20bilingual%20development%22&resultType=core&format=json), 2012 (online 2011), Primary, root 2
 └─ [Peña, Bedore & Vargas, *Exploring Assumptions of the Bilingual Delay in Children With and Without Developmental Language Disorder*, JSLHR 66](https://pmc.ncbi.nlm.nih.gov/articles/PMC11361784/), 2023, Secondary → cites
     └─ Clahsen & Jessen 2019; Fitton et al. 2019; Peña et al. 2011, (not opened), per Peña, Bedore & Vargas 2023 → stopped: not opened

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | Root 1 (per Duchan's page, not opened): a lag in speech development among 1930s preschoolers in Hawaii of non-American ancestry, which the author put down to the simultaneous use of two languages | Bilingual children start speaking later. | [Homeschool Spanish Academy blog](https://www.spanish.academy/blog/are-bilingual-children-more-likely-to-experience-a-speech-or-language-delay/), 2024 |
| Scope widened | Root 2: on single-language measures of vocabulary and grammar at 22–30 months, monolingual children [“were significantly more advanced than the bilingually developing children”](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22Dual%20language%20exposure%20and%20early%20bilingual%20development%22&resultType=core&format=json) | Bilingual children start speaking later. | [Homeschool Spanish Academy blog](https://www.spanish.academy/blog/are-bilingual-children-more-likely-to-experience-a-speech-or-language-delay/), 2024 |
| Context removed | Root 2: the two groups were comparable on total vocabulary across both languages | Bilingual children start speaking later. | your version |
| Other: the measure changed | Both roots measured progress in English (mastery of English; English vocabulary and grammar), not the age at which children begin to speak | Bilingual children start speaking later. | your version |

### Status of the root
- Smith 1939: Duchan's history page says her widely cited studies were [“later found to be methodologically flawed”](https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/). The page also says she compared bilingual children with norms she had collected earlier from monolingual children. I could not open the monograph itself, so I ran no retraction or correction check on it.
- Hoff et al. 2012: the [Crossref record](https://api.crossref.org/works/10.1017/S0305000910000759) lists no retraction, correction or erratum.
- Hoff et al. 2012, as Hoff's 2021 review reports it: the bilingual children in that sample [“reached that milestone in English 3 months later than the monolinguals”](https://pmc.ncbi.nlm.nih.gov/articles/PMC10395373/) (word combinations). There was no difference when each child's stronger language was counted.
- Later study: [Petitto et al. 2001, *Journal of Child Language* 28](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:11449947&resultType=core&format=json) found that a small group of children learning two languages from birth reached early milestones, including first words, on roughly the same schedule as monolingual children.
- Later study: [Muszyńska et al. 2025, *Journal of Child Language*](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1017/S0305000924000655&resultType=core&format=json) compared 302 Polish bilingual children with 302 matched monolingual children on babbling, first, 10th and 50th words and first multi-word utterances. Its abstract reports that bilingual development followed a similar trajectory.
- Later study: Peña, Bedore & Vargas 2023 studied 595 Spanish–English children aged 5–12. They describe a pervasive belief in bilingual delay and say their results [“go against the assumption of bilingual delay overall”](https://pmc.ncbi.nlm.nih.gov/articles/PMC11361784/). They also cite a Swedish study in which nurses put off language screening because of this belief.

### Cold trails
- [Homeschool Spanish Academy blog](https://www.spanish.academy/blog/are-bilingual-children-more-likely-to-experience-a-speech-or-language-delay/), 2024: presents the belief as a myth and links it to a supposed confusion and *silent period* in bilingual children. It cites no source for where the belief came from.
- [Little Words, *The bilingual speech delay myth*](https://littlewords.ai/blog/bilingual-children-speech-delay-myth), date unknown: puts the belief down to vocabulary being counted in only one language. Its only source (Pearson, Fernández & Oller 1993) is cited for the counter-finding, not for the belief itself.

### Confidence
Medium: root 1 (Smith 1939) was not opened, and the scanned copies of Hakuta's histories and of a thesis quoting Smith returned no text or refused access, so the oldest branch rests on Duchan's secondary account.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
