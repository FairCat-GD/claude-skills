---
case: no-memory-bilingual-speech
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:37:21Z
cost_usd: 1.8882
duration_s: 266
turns: 39
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- Read: <plugin>/skills/provenance-tracer/references/labels.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- WebSearch: "bilingual children start speaking later"
- WebSearch: bilingualism causes language delay myth origin
- WebSearch: bilingual infants first words age same as monolingual Petitto 2001 milestones
- WebSearch: history bilingualism harmful children early 20th century studies Saer 1923 language handicap
- WebSearch: who first claimed bilingual children talk later speech delay earliest study
- WebSearch: fact check "bilingual" children "speech delay" myth
- WebFetch: https://en.wikipedia.org/wiki/Speech_delay
- WebFetch: https://pubs.asha.org/doi/10.1044/2023_JSLHR-23-00117
- WebFetch: https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later
- WebFetch: https://littlewords.ai/blog/bilingual-children-speech-delay-myth
- WebFetch: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6168212/
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC10395373/
- WebFetch: https://www.healthychildren.org/English/ages-stages/gradeschool/school/Pages/7-Myths-Facts-Bilingual-Children-Learning-Language.aspx
- WebSearch: Arsenian 1937 review bilingualism language delay history "bilingual delay" assumption Darcy
- WebFetch: https://pubs.asha.org/doi/full/10.1044/2023_JSLHR-23-00117
- WebFetch: https://www.sas.upenn.edu/~haroldfs/540/bilingtl/haugen.html
- WebSearch: Madorah Smith 1939 bilingualism preschool children Hawaii speech retardation study
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1986)%20-%20MIRROR%20OF%20LANGUAGE%20THE%20DEBATE%20ON%20BILINGUALISM.pdf
- WebFetch: https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/
- WebFetch: https://web.stanford.edu/~hakuta/www/research/publications/(1987)%20-%20BILINGUALISM%20AND%20COGNITIVE%20DEVELOPMENT%20THREE%20PERSPE.pdf
- WebSearch: "retardation in speech" "attempt to make use of two languages" Smith 1939
- WebFetch: https://commons.und.edu/cgi/viewcontent.cgi?article=10630&context=theses
- WebSearch: Smith "Some light on the problem of bilingualism" archive.org OR full text Genetic Psychology Monographs 1939
- WebFetch: https://files.eric.ed.gov/fulltext/ED273152.pdf
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/
- WebFetch: https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html
- WebFetch: https://link.springer.com/chapter/10.1007/978-3-030-87063-8_2
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=AUTH:"Smith M" AND (TITLE:"bilingualism" OR TITLE:"bilingual children") AND PUB_YEAR:[1930 TO 1940]&resultType=core&format=json
- WebFetch: https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay
- WebFetch: https://laura-ann-petitto.com/images/assets/publications/Publications/2001_PetittoKaterelosEtAl_ChildLanguage.pdf
- WebFetch: https://api.crossref.org/works?query.bibliographic=Some+light+on+the+problem+of+bilingualism+Smith+1939&rows=3

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Bilingual children start speaking later."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** Madorah E. Smith, *Some light on the problem of bilingualism as found from a study of the progress in mastery of English among preschool children of non-American ancestry in Hawaii*, *Genetic Psychology Monographs* 21, 1939 (date from: cited by [Duchan, *A History of Speech-Language Pathology*](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 11

### Chain
Your version: "Bilingual children start speaking later." (where you met it: not given)
 └─ [Judy Duchan, *A History of Speech-Language Pathology*: Madorah Smith](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html), date unknown (page copyright 2001–2023), Secondary → cites
     └─ Smith, *Some light on the problem of bilingualism…*, *Genetic Psychology Monographs* 21: 121–284, 1939, Primary (not opened, per Duchan page), root
 └─ [*Madorah Elizabeth Smith 1884–*, History of Communication Disorders, University at Buffalo](https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/), date unknown, Secondary → cites
     └─ Smith 1939, the root above
 └─ [*Why bilingual development is not easy*, PMC review](https://pmc.ncbi.nlm.nih.gov/articles/PMC10395373/), date unknown, Secondary → cites
     └─ [Kenji Hakuta, *Mirror of Language: The Debate on Bilingualism*](https://web.stanford.edu/~hakuta/Publications/(1986)%20-%20MIRROR%20OF%20LANGUAGE%20THE%20DEBATE%20ON%20BILINGUALISM.pdf), 1986, (not opened), per PMC review → stopped: not opened
     └─ Hoff, 2018; Nicoladis, Charbonnier & Popescu, 2016, (not opened), per PMC review → stopped: not opened

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | preschool children of non-American ancestry in Hawaii, measured against Smith's Iowa norms (per [Duchan page](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html)) | Bilingual children start speaking later. | [Nationwide Children's Hospital, 700 Children's blog](https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay), 2017 |
| Other: what is measured shifted from how far speech had developed to when speaking starts | Smith concluded that the [use of two languages contributed to a lag in speech development](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html) | Bilingual children start speaking later. | [amma.family, *Do Bilingual Children Start Speaking Later?*](https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later), 2024 |
| Context removed | poor immigrant children compared with middle-class native-born children, with fluent and limited bilinguals not told apart (per [University at Buffalo page](https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/)) | Bilingual children start speaking later. | [Nationwide Children's Hospital, 700 Children's blog](https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay), 2017 |

### Status of the root
- No DOI found: a [Crossref search](https://api.crossref.org/works?query.bibliographic=Some+light+on+the+problem+of+bilingualism+Smith+1939&rows=3) and a [Europe PMC search](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=AUTH:"Smith M" AND (TITLE:"bilingualism" OR TITLE:"bilingual children") AND PUB_YEAR:[1930 TO 1940]&resultType=core&format=json) returned no record of the 1939 monograph, so no retraction or correction notice could be checked there. Retraction Watch and PubPeer were not checked.
- Smith 1939, per the [Duchan page](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html): her widely cited studies were later judged methodologically flawed.
- Smith 1939, per the [University at Buffalo page](https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/): she compared poor immigrant children with middle-class native-born Americans, and did not separate fluent bilinguals from limited ones.
- Later studies, per the [PMC review](https://pmc.ncbi.nlm.nih.gov/articles/PMC10395373/): Petitto et al. (2001) found bilingual infants reached first words and first multiword utterances on the same timetable as monolinguals. Later work (Hoff 2018; Nicoladis et al. 2016) reports that bilingual children may at first lag behind monolinguals, with vocabulary size depending on how much of each language they hear. The Petitto 2001 PDF was fetched but its text could not be read.
- Background: an earlier paper by the same author, Smith, *A study of five bilingual children from the same family*, *Child Development* 2, 1931 (per University at Buffalo page), not opened.

### Cold trails
- [amma.family, *Do Bilingual Children Start Speaking Later?*](https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later), 2024: raises the idea and rejects it, without citing where it came from
- [Nationwide Children's Hospital, *Teaching Kids a Second Language: Can It Cause a Speech Delay?*](https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay), 2017: calls it a long-standing belief in the United States, without citing where it came from
- [AAP/ASHA, HealthyChildren.org, *Young Children Learning Multiple Languages: Parent FAQs*](https://www.healthychildren.org/English/ages-stages/gradeschool/school/Pages/7-Myths-Facts-Bilingual-Children-Learning-Language.aspx), 2024 (copyright line): raises the question and answers no, without citing where the idea came from
- [littlewords.ai, *The bilingual speech delay myth*](https://littlewords.ai/blog/bilingual-children-speech-delay-myth), date unknown: puts the origin down to misread vocabulary counts, without citing a source for that

### Confidence
Medium. The Smith 1939 monograph and Hakuta's 1986 history could not be opened, so the root rests on two opened pages that cite it. The earlier 1920s–30s intelligence studies, and a 2023 JSLHR review of how the delay idea arose, could not be opened either (403 errors, scans with no readable text).

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
