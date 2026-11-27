---
case: personal-chain-bilingual-speech
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:21:23Z
cost_usd: 1.4160
duration_s: 165
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
- WebSearch: "bilingual children start speaking later"
- WebSearch: bilingualism causes language delay in children myth
- WebSearch: origin of belief bilingual children talk later history research
- WebSearch: bilingual toddlers first words age study vocabulary milestones monolingual comparison
- WebSearch: bilingual children speech delay fact check
- WebSearch: Saer 1923 bilingualism Welsh children early research language handicap
- WebSearch: Madorah Smith 1939 bilingual Hawaii preschool children vocabulary retardation
- WebFetch: https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay
- WebFetch: https://onlinelibrary.wiley.com/doi/10.1111/jpc.15051
- WebFetch: https://www.cambridge.org/core/journals/journal-of-child-language/article/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers/0BFAB689DC70E5A2A5220976E1939948
- WebFetch: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4132345/
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1986)%20-%20MIRROR%20OF%20LANGUAGE%20THE%20DEBATE%20ON%20BILINGUALISM.pdf
- WebFetch: https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC4132345/
- WebFetch: https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1987)%20-%20BILINGUALISM%20AND%20COGNITIVE%20DEVELOPMENT%20THREE%20PERSPE.pdf
- WebFetch: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6168212/
- WebFetch: https://www.healthychildren.org/English/ages-stages/gradeschool/school/Pages/7-Myths-Facts-Bilingual-Children-Learning-Language.aspx
- WebSearch: bilingual children "speak later" OR "talk later" Forbes OR "Harvard Business Review" OR Economist OR Fortune
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/
- WebFetch: https://www.habilnet.org/bilingual-children-do-not-start-speaking-later-than-monolingual-ones/
- WebFetch: https://www.levyinstitute.org/pubs/wp/229.pdf
- WebFetch: https://commons.und.edu/cgi/viewcontent.cgi?article=10630&context=theses
- WebFetch: https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html
- WebFetch: https://en.wikipedia.org/wiki/Cognitive_effects_of_bilingualism

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain beyond your message: the business magazine was not named, so I couldn't identify or search for that article, and the trace starts from the web.

## Provenance: "Bilingual children start speaking later than children who learn one language."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** Madorah E. Smith, *Some light on the problem of bilingualism as found from a study of the progress in mastery of English among preschool children of non-American ancestry in Hawaii*, Genetic Psychology Monographs 21, 1939 (date from: cited by [University at Buffalo, *History of Speech-Language Pathology*](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 8

### Chain
Your version: "Bilingual children start speaking later." (where you met it: a manager's retelling (Hearsay) of a business magazine article; no year given; matches no node found)
 ├─ [Annick De Houwer & Mareen Pascall, *Bilingual children do not start speaking later than monolingual ones*, Habilnet](https://www.habilnet.org/bilingual-children-do-not-start-speaking-later-than-monolingual-ones/), 2021 (German original), Secondary. It reports that the belief is still common among pediatricians, speech therapists and preschool teachers → cites its bibliography → stopped: not opened
 ├─ [Amma, *Do Bilingual Children Start Speaking Later?*](https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later), 2024, Tertiary. It states the question in your words and answers it → cites
 │   └─ [AAP / ASHA, *Young Children Learning Multiple Languages: Parent FAQs*, HealthyChildren.org](https://www.healthychildren.org/English/ages-stages/gradeschool/school/Pages/7-Myths-Facts-Bilingual-Children-Learning-Language.aspx), date unknown (last updated 2025), Tertiary. It lists "causes delays in their communication development" as a myth and cites no study
 ├─ [Wikipedia, *Cognitive effects of bilingualism*](https://en.wikipedia.org/wiki/Cognitive_effects_of_bilingualism), date unknown, Tertiary: "Researchers believed that bilinguals would have smaller vocabularies" (before the 1960s) → cites
 │   └─ Arsenian, 1937 (thesis), (not opened), per Wikipedia → stopped: not opened
 └─ [University at Buffalo, *History of Speech-Language Pathology*: Madorah Smith](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html), date unknown, Secondary → cites
     └─ Smith, *Some light on the problem of bilingualism…*, Genetic Psychology Monographs 21: 121–284, 1939, Primary (not opened, per University at Buffalo page)

Notes on the chain:
- I also opened [Ewa Haman's team's milestone study (Muszyńska et al.), *Journal of Child Language*](https://www.cambridge.org/core/journals/journal-of-child-language/article/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers/0BFAB689DC70E5A2A5220976E1939948), 2025. It tests the claim rather than retelling it, so it appears under *Status*.
- Two pages could not be read: [Isaacs, *Journal of Paediatrics and Child Health*](https://onlinelibrary.wiley.com/doi/10.1111/jpc.15051), 2021, was blocked (403), and [Hakuta, *Mirror of Language*](https://web.stanford.edu/~hakuta/Publications/(1986)%20-%20MIRROR%20OF%20LANGUAGE%20THE%20DEBATE%20ON%20BILINGUALISM.pdf), 1986, is a scanned PDF with no readable text. Search summaries pointed to both as histories of the belief. Neither is used as a node.

### How it changed
Smith's 1939 monograph was not opened. The "Root says" column therefore uses the University at Buffalo page's account of it.

| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | Preschool children of Chinese, Filipino, Japanese, Korean, Portuguese and Hawaiian ancestry in 1930s Hawaii, compared with English norms | bilingual children in general | [Nationwide Children's](https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay), 2017, which calls the general form "a long-standing myth in the United States" |
| Other: what is measured | Progress in mastering English: "a lag in speech development" | when children *start* speaking (onset of first words) | [De Houwer & Pascall](https://www.habilnet.org/bilingual-children-do-not-start-speaking-later-than-monolingual-ones/), 2021, the earliest opened page that gives the "start speaking later" wording |
| Context removed | Per the Buffalo page, Smith compared poor immigrant children with middle-class native-born Americans and did not separate fluent bilinguals from limited ones | stated without those conditions | [Nationwide Children's](https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay), 2017 |

### Status of the root
- No journal page, DOI or Crossref record was found for the 1939 monograph. Retraction Watch and PubPeer were not checked, so no retraction or correction status was established.
- [University at Buffalo, *History of Speech-Language Pathology*](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html): Smith's studies, "cited widely, were later found to be methodologically flawed". The page does not say who found the flaws or when.
- Later major study: [Muszyńska et al., *Journal of Child Language*](https://www.cambridge.org/core/journals/journal-of-child-language/article/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers/0BFAB689DC70E5A2A5220976E1939948), 2025. It studied 302 Polish bilingual children and 302 matched monolinguals and found no significant group differences in the ages of babbling, first word, 10th word, 50th word or first multiword utterance. The authors note that the later milestones rest on small samples. It was not designed as a replication of Smith.
- Later reviews: the [Italian Journal of Pediatrics abstract (Cucinotta et al.)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4132345/), 2014, states, citing King & Fogle (2006), that "bilingualism does not cause language delay or language disorders". The [AAP/ASHA parent page](https://www.healthychildren.org/English/ages-stages/gradeschool/school/Pages/7-Myths-Facts-Bilingual-Children-Learning-Language.aspx) says total word counts across both languages are about the same as a one-language child's.

### Cold trails
- [Nationwide Children's Hospital, *Teaching Kids a Second Language: Can It Cause a Speech Delay?*](https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay), 2017: states the belief and says research dispelled it, but names no study.

### Confidence
Medium. The root is known only through an opened secondary page, with its 1939 date resting on *cited by*, and the business magazine article your manager read could not be identified or linked to any node.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
