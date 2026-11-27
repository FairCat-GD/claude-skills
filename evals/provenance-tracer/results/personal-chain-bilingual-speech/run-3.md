---
case: personal-chain-bilingual-speech
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T19:12:45Z
cost_usd: 1.7274
duration_s: 187
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
- WebSearch: "bilingual children start speaking later"
- WebSearch: bilingualism causes language delay in children myth
- WebSearch: bilingual toddlers first words milestones study same age monolingual
- WebSearch: origin of belief bilingualism delays speech history early 20th century studies
- WebSearch: bilingual children speak later fact check
- WebSearch: bilingual children talk later business magazine raising bilingual kids
- WebFetch: https://pubs.asha.org/doi/10.1044/2023_JSLHR-23-00117
- WebFetch: https://files.eric.ed.gov/fulltext/ED020491.pdf
- WebFetch: https://www.cambridge.org/core/journals/journal-of-child-language/article/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers/0BFAB689DC70E5A2A5220976E1939948
- WebFetch: https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later
- WebFetch: https://pubs.asha.org/doi/pdf/10.1044/2023_JSLHR-23-00117
- WebFetch: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6168212/
- WebSearch: Beckey 1942 "A study of certain factors related to retardation of speech" bilingual
- WebSearch: Madorah Smith 1939 bilingual Hawaii preschool children speech retarded study
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/
- WebFetch: https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1986)%20-%20MIRROR%20OF%20LANGUAGE%20THE%20DEBATE%20ON%20BILINGUALISM.pdf
- WebFetch: https://www.themultilingualgarden.com/blog/do-bilingual-children-start-talking-later-than-monolinguals
- WebFetch: https://web.stanford.edu/~hakuta/www/research/publications/(1987)%20-%20BILINGUALISM%20AND%20COGNITIVE%20DEVELOPMENT%20THREE%20PERSPE.pdf
- WebSearch: "Some light on the problem of bilingualism" Smith 1939 Genetic Psychology Monographs full text
- WebFetch: https://files.eric.ed.gov/fulltext/ED273152.pdf
- WebFetch: https://mrstorkey.com/do-bilingual-babies-talk-later/
- WebSearch: Forbes OR "Harvard Business Review" OR Economist bilingual children "speak later" OR "talk later" OR "language delay"
- WebFetch: https://link.springer.com/chapter/10.1007/978-3-030-87063-8_2
- WebFetch: https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay
- WebFetch: https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html
- WebFetch: https://api.crossref.org/works?query.bibliographic=Smith+1939+Some+light+on+the+problem+of+bilingualism+Hawaii&rows=3
- WebFetch (error): https://web.archive.org/cdx/search/cdx?url=www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html&limit=1

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain beyond your message: your manager's name was never searched, and I couldn't identify the business magazine.

## Provenance: "Bilingual children start speaking later."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** Madorah E. Smith, *Some light on the problem of bilingualism as found from a study of the progress in mastery of English among preschool children of non-American ancestry in Hawaii*, Genetic Psychology Monographs 21, 1939 (date from: cited by [Judy Duchan's *History of Speech–Language Pathology*](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 5

### Chain
Your version: "Bilingual children start speaking later." (you heard it: your manager (Hearsay), who read it in a business magazine; year not given; the magazine was not found)
 └─ [Judy Felson Duchan, *A History of Speech–Language Pathology*: Madorah Smith](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html), date unknown (copyright line 2001–2023), Secondary → cites
     └─ Smith, *Some light on the problem of bilingualism…*, Genetic Psychology Monographs 21: 119/121–284, 1939, Primary (not opened, per Duchan's page), root
 └─ [*History of CDS*: Madorah Elizabeth Smith 1884–](https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/) (University at Buffalo, same history project), date unknown, Secondary → cites
     └─ Smith 1939 (the root, above)

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | Preschool children of immigrant ancestry in Hawaii, measured against Smith's Iowa norms ([Duchan](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html)) | Bilingual children start speaking later. | [Nationwide Children's Hospital, *Teaching Kids a Second Language*](https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay), 2017 |
| Hedge dropped | "simultaneous use of two languages contributed to a lag in speech development" ([Duchan](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html)) | Bilingual children start speaking later. | your version |
| Context removed (comparison group) | Smith compared immigrant children with middle-class native-born norms ([Duchan](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html)) | Bilingual children start speaking later. | [Nationwide Children's Hospital](https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay), 2017 |
| Other: different measure | A slower pace of mastering English between about ages 2 and 6, not when children first speak ([Duchan](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html)) | Bilingual children start speaking later. | your version |

### Status of the root
- No retraction or correction found. A Crossref bibliographic search returned no record for the 1939 monograph, so there was no DOI to check. I did not check Retraction Watch or PubPeer, and found no journal page for the monograph.
- [Duchan's page](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html) reports that Smith's widely cited studies were later judged methodologically flawed. They paired poor immigrant children with middle-class native-born Americans, and did not separate fluent bilinguals from limited ones. The page doesn't say who made that judgement.
- Later study: [Muszyńska et al., *Bilingual children reach early language milestones at the same age as monolingual peers*, Journal of Child Language](https://www.cambridge.org/core/journals/journal-of-child-language/article/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers/0BFAB689DC70E5A2A5220976E1939948), online 15 January 2025. It compared 302 Polish bilingual children with 302 matched monolingual children aged 0–24 months, using parent reports collected through an app. It found no significant difference in the age of babbling, first word, 10th or 50th word, or first multi-word utterance. It notes that bilinguals often have smaller vocabularies in each single language. It did not set out to repeat Smith's study.
- Later review: [Byers-Heinlein & Lew-Williams, *Bilingualism in the Early Years: What the Science Says*, Learning Landscapes](https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/), 2013. It says attitudes against early bilingualism are "often based on myths and misinterpretations, rather than scientific findings". It cites Paradis, Genesee & Crago (2010) and Petitto & Holowka (2002) for the point that bilingual children are no more likely to have language difficulties.

### Cold trails
- [Nationwide Children's Hospital, *Teaching Kids a Second Language: Can It Cause a Speech Delay?*](https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay), 2017: describes the belief as long-standing in the United States and says research has dispelled it. It cites no source for where the belief came from.
- [amma, *Do Bilingual Children Start Speaking Later?*](https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later), 2024: states the belief in order to call it a myth. It cites Byers-Heinlein & Lew-Williams (2013) and AAP/ASHA guidance for the rebuttal, but nothing for where the belief came from.

### Confidence
Medium: I couldn't open Smith's 1939 monograph, and its date comes from a citing page. Several pages that might name parallel or earlier studies from the 1930s–40s also would not open: a [2023 JSLHR review](https://pubs.asha.org/doi/10.1044/2023_JSLHR-23-00117) returned 403, and a [1966 ERIC paper](https://files.eric.ed.gov/fulltext/ED020491.pdf) and [Hakuta's 1986 *Mirror of Language*](https://web.stanford.edu/~hakuta/Publications/(1986)%20-%20MIRROR%20OF%20LANGUAGE%20THE%20DEBATE%20ON%20BILINGUALISM.pdf) are image-only scans with no readable text.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
