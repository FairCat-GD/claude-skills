---
case: no-memory-bilingual-speech
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T15:38:12Z
cost_usd: 2.0290
duration_s: 247
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
- WebSearch: "bilingual children start speaking later"
- WebSearch: bilingualism causes language delay in children myth
- WebSearch: bilingual first words age study Petitto Holowka 2001 milestones
- WebSearch: origin of belief bilingualism delays speech history Saer 1923 "language handicap"
- WebSearch: bilingual children talk later fact check
- WebSearch: bilingual toddlers first word same age monolingual study Hoff 2012 vocabulary
- WebSearch: Madorah Smith 1939 bilingualism Hawaii preschool children speech retardation
- WebSearch: where does the myth that bilingual children speak later come from history early studies
- WebFetch: https://www.habilnet.org/bilingual-children-do-not-start-speaking-later-than-monolingual-ones/
- WebFetch: https://sites.google.com/view/multicsd/multilingualism-multiculturalism/working-with-cld-clients/pediatrics/myths-surrounding-language-development-treatment-in-bilingual-children
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1986)%20-%20MIRROR%20OF%20LANGUAGE%20THE%20DEBATE%20ON%20BILINGUALISM.pdf
- WebFetch: https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1987)%20-%20BILINGUALISM%20AND%20COGNITIVE%20DEVELOPMENT%20THREE%20PERSPE.pdf
- WebSearch: Smith 1939 "Some light on the problem of bilingualism" Genetic Psychology Monographs
- WebFetch: https://files.eric.ed.gov/fulltext/ED273152.pdf
- WebFetch: https://link.springer.com/chapter/10.1007/978-3-030-87063-8_2
- WebFetch: https://commons.und.edu/cgi/viewcontent.cgi?article=10630&context=theses
- WebFetch: https://www.levyinstitute.org/pubs/wp/229.pdf
- WebSearch: archive.org Smith "progress in mastery of English among pre-school children" Hawaii 1939
- WebFetch: https://web.stanford.edu/~hakuta/www/research/publications/(1987)%20-%20BILINGUALISM%20AND%20COGNITIVE%20DEVELOPMENT%20THREE%20PERSPE.pdf
- WebFetch (error): http://www.ciil-ebooks.net/html/bilingualism/part%201.htm
- WebFetch: https://www.amacad.org/sites/default/files/academy/multimedia/pdfs/IA4th-Chapter%206-LanguageDiversityandResilience.pdf
- WebFetch: https://www.cambridge.org/core/journals/journal-of-child-language/article/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers/0BFAB689DC70E5A2A5220976E1939948
- WebFetch: https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay
- WebSearch: Hakuta "Mirror of language" Madorah Smith "retardation in speech" bilingualism
- WebSearch: psycnet Smith 1939 bilingualism mastery of English pre-school children Hawaii abstract
- WebFetch: https://www.biorxiv.org/content/10.1101/2024.10.04.616691v1.full.pdf
- WebFetch: https://www.biorxiv.org/content/10.1101/2024.10.04.616691v1.full
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1017/s0142716412000744&resultType=core&format=json

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Bilingual children start speaking later."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** Madorah E. Smith, *Some light on the problem of bilingualism as found from a study of the progress in mastery of English among pre-school children of non-American ancestry in Hawaii*, *Genetic Psychology Monographs* 21, 1939 (date from: cited by [the Buffalo history page](https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/) and [Sade et al. 2024](https://www.biorxiv.org/content/10.1101/2024.10.04.616691v1.full)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 6

### Chain
Your version: "Bilingual children start speaking later." (where you met it: not given)
 ├─ [Sade, Rathwell, Kolb, Gonzalez & Gibb, *Bilingualism Modulates Executive Function Development in Pre-School Aged Children* (bioRxiv preprint)](https://www.biorxiv.org/content/10.1101/2024.10.04.616691v1.full), 2024, Secondary → cites
 │   └─ Smith, *Genetic Psychology Monographs* 21, 1939, Primary (not opened, per Sade et al. 2024), root
 └─ [*A History of Speech-Language Pathology* (Univ. at Buffalo), entry on Madorah Elizabeth Smith](https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/), date unknown, Secondary → cites
     └─ Smith 1939, the same root as above. Her earlier Hawaii papers (1931, 1933, 1935) are listed on this page and come from the same researcher, so they belong to the same root.

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Other: what is measured changed. Smith measured how much English children aged 2–6 had mastered; your version is about when they start speaking | Smith concluded that using two languages [“contributed to a lag in speech development”](https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/), based on English speech samples from preschoolers | Bilingual children start speaking later. | [MultiCSD](https://sites.google.com/view/multicsd/multilingualism-multiculturalism/working-with-cld-clients/pediatrics/myths-surrounding-language-development-treatment-in-bilingual-children), 2011 |
| Scope widened | Preschool children of Chinese, Filipino, Hawaiian, Japanese, Korean and Portuguese ancestry in 1930s Hawaii | Bilingual children start speaking later. | [MultiCSD](https://sites.google.com/view/multicsd/multilingualism-multiciculturalism/working-with-cld-clients/pediatrics/myths-surrounding-language-development-treatment-in-bilingual-children), 2011 |
| Context removed: comparison group dropped | Smith compared poor immigrant children in Hawaii with middle-class native-born samples from Iowa, and did not separate fluent from limited bilinguals | Bilingual children start speaking later. | [MultiCSD](https://sites.google.com/view/multicsd/multilingualism-multiculturalism/working-with-cld-clients/pediatrics/myths-surrounding-language-development-treatment-in-bilingual-children), 2011 |

### Status of the root
- Smith 1939 has no DOI, and I could not open a journal page for it, so there are no Crossref, Retraction Watch or PubPeer checks for it. The checks below are later accounts and later studies.
- [The Buffalo history page](https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/) reports that Smith's widely cited studies were later found to be methodologically flawed: different social classes were compared, and fluent bilinguals were not separated from limited ones.
- [Sade et al. 2024](https://www.biorxiv.org/content/10.1101/2024.10.04.616691v1.full) call Smith 1939 the most influential of the early studies. Citing Hakuta's *Mirror of Language* (1986), they say those studies did not control for age, socioeconomic status or sex, and tested children in only one language. Hakuta's book was found but [its PDF](https://web.stanford.edu/~hakuta/Publications/(1986)%20-%20MIRROR%20OF%20LANGUAGE%20THE%20DEBATE%20ON%20BILINGUALISM.pdf) returned no readable text.
- Later study: [De Houwer, Bornstein & Putnick, *Applied Psycholinguistics*, 2014](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1017/s0142716412000744&resultType=core&format=json) opens with “It is often assumed that young bilinguals are lexically delayed”. In 31 bilingual and 30 matched monolingual children, it found no group difference in word production. At 13 months the bilinguals understood more words; at 20 months the monolinguals knew more Dutch words.
- Later study: [Muszyńska et al., *Journal of Child Language*, published online 2025](https://www.cambridge.org/core/journals/journal-of-child-language/article/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers/0BFAB689DC70E5A2A5220976E1939948) compared 302 Polish bilingual children with 302 matched monolingual children. It reports no significant difference in age at first word. The authors call their evidence for the 50th-word and longer-utterance milestones inconclusive.

### Cold trails
- [MultiCSD, *Myths Surrounding Language Development & Treatment in Bilingual Children*](https://sites.google.com/view/multicsd/multilingualism-multiculturalism/working-with-cld-clients/pediatrics/myths-surrounding-language-development-treatment-in-bilingual-children), 2011 (updated 2022): traces the belief to unnamed past research that used monolingual standards, and names no study.
- [Nationwide Children's Hospital, *Teaching Kids a Second Language: Can It Cause a Speech Delay?*](https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay), 2017: calls the belief long-standing in the US and cites nothing.
- [De Houwer & Pascall, HaBilNet, *Bilingual children do not start speaking later than monolingual ones*](https://www.habilnet.org/bilingual-children-do-not-start-speaking-later-than-monolingual-ones/), 2021: says many professionals still hold the belief, and names no origin on the page.

### Confidence
Medium. The root rests on Smith's 1939 monograph, which I could not open (I found no online copy, and Hakuta's scanned PDFs returned no text), so its date and content come from the pages that cite it. Search results also pointed to 1920s studies of bilingualism and IQ (e.g. Saer 1923), but none of those was opened in this trace.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
