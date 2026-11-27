---
case: no-memory-bilingual-speech
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:14:29Z
cost_usd: 1.4625
duration_s: 229
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
- WebSearch: "bilingual children start speaking later"
- WebSearch: bilingualism causes language delay myth origin
- WebSearch: bilingual toddlers first words milestones study Petitto Pearson
- WebSearch: history of belief bilingualism harmful children 1920s studies "language handicap"
- WebSearch: where does the idea that bilingual children talk late come from
- WebSearch: bilingual children speech delay fact check
- WebFetch (error): https://www.britishcouncil.org/voices-magazine/few-more-myths-about-speakers-multiple-languages
- WebFetch: https://speechblubs.com/blog/bilingual-kids-do-they-speak-later-unpacking-the-myth
- WebFetch: https://www.sas.upenn.edu/~haroldfs/540/bilingtl/haugen.html
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1986)%20-%20MIRROR%20OF%20LANGUAGE%20THE%20DEBATE%20ON%20BILINGUALISM.pdf
- WebFetch: https://ila.onlinelibrary.wiley.com/doi/full/10.1002/trtr.70016
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1985)%20-%20THE%20RELATIONSHIP%20BETWEEN%20DEGREE%20OF%20BILINGUALISM%20AND.pdf
- WebSearch: Madorah Smith 1939 bilingual Hawaii preschool children speech retarded vocabulary
- WebSearch: Saer 1923 "The effect of bilingualism on intelligence" British Journal of Psychology Welsh
- WebFetch: https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1987)%20-%20BILINGUALISM%20AND%20COGNITIVE%20DEVELOPMENT%20THREE%20PERSPE.pdf
- WebFetch: https://www.levyinstitute.org/pubs/wp/229.pdf
- WebFetch: https://www.themultilingualgarden.com/blog/do-bilingual-children-start-talking-later-than-monolinguals
- Read (denied): <temp>/config/projects/-private-tmp-e-IRSKSn-home-cwd/7d463ec0-c121-4501-a432-440465707735/tool-results/webfetch-1795770903606-g3zk9p.pdf
- WebFetch: https://scholarspace.manoa.hawaii.edu/server/api/core/bitstreams/7d8cc822-c4b1-4f16-ae7b-de8ce9b00033/content
- WebFetch: https://journals.sagepub.com/stoken/default+domain/qMtnCUVs54Gq3vdMD43N/full
- WebFetch: https://www.cambridge.org/core/journals/journal-of-child-language/article/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers/0BFAB689DC70E5A2A5220976E1939948
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC4180217
- WebFetch: https://bpspsychub.onlinelibrary.wiley.com/doi/abs/10.1111/j.2044-8295.1923.tb00110.x
- WebFetch: https://api.crossref.org/works/10.1111/j.2044-8295.1923.tb00110.x
- WebFetch: https://en.wikipedia.org/wiki/Cognitive_effects_of_bilingualism
- WebFetch: https://www.spanish.academy/blog/are-bilingual-children-more-likely-to-experience-a-speech-or-language-delay/

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Bilingual children start speaking later."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** Madorah Smith, *Some light on the problem of bilingualism as found from a study of the progress in mastery of English among preschool children of non-American ancestry in Hawaii*, Genetic Psychology Monographs 21, 1939 (date from: cited by [Duchan, *Madorah Smith*](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 7

### Chain
Your version: "Bilingual children start speaking later." (where you met it: not given)
 ├─ [Speech Blubs, *Bilingual Kids: Do They Speak Later? Unpacking the Myth*](https://speechblubs.com/blog/bilingual-kids-do-they-speak-later-unpacking-the-myth), 2025, Tertiary: describes the worry that bilingualism causes children to "start talking later than their monolingual peers". It treats this as an outdated belief, cites no origin, and is listed under Cold trails.
 ├─ [The Multilingual Garden, *Do Bilingual Children Start Talking Later Than Monolinguals?*](https://www.themultilingualgarden.com/blog/do-bilingual-children-start-talking-later-than-monolinguals), date unknown, Tertiary: says the idea "stems from misunderstandings and a lack of reliable information". It cites no origin and is listed under Cold trails.
 ├─ [Homeschool Spanish Academy, *Does Bilingualism cause Speech Delays?*](https://www.spanish.academy/blog/are-bilingual-children-more-likely-to-experience-a-speech-or-language-delay/), 2024, Tertiary: says the belief "most likely springs from the idea that bilingual children are more prone to confusion". It cites no origin and is listed under Cold trails.
 ├─ [Duchan, *Madorah Smith* (history of speech-language pathology, University at Buffalo)](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html), date unknown (copyright 2001–2023), Secondary: Smith found that the "simultaneous use of two languages contributed to a lag in speech development" → cites
 │   └─ Smith, M. (1939), *Genetic Psychology Monographs* 21, 121–284, 1939, Primary (not opened, per Duchan)
 └─ [Wikipedia, *Cognitive effects of bilingualism*](https://en.wikipedia.org/wiki/Cognitive_effects_of_bilingualism), date unknown, Tertiary: "Researchers believed that bilinguals would have smaller vocabularies" → cites
     └─ Arsenian, S. (1937), a thesis on bilingual children in New York City, 1937, (not opened), per Wikipedia → stopped: not opened

### How it changed
Smith's study was not opened, so the "Root says" column describes the root as Duchan reports it.

| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | preschool children of non-American ancestry in Hawaii learning English (per Duchan) | bilingual children | [Speech Blubs](https://speechblubs.com/blog/bilingual-kids-do-they-speak-later-unpacking-the-myth), 2025, the earliest dated node opened that states the general form |
| Other: the measure changed | a "lag in speech development", measured as progress in mastering English against mainland US norms (per Duchan) | start speaking later | [Speech Blubs](https://speechblubs.com/blog/bilingual-kids-do-they-speak-later-unpacking-the-myth), 2025 |
| Context removed: the cause is gone | the simultaneous use of two languages "contributed to" the lag (per Duchan) | a plain statement that bilingual children speak later, with no cause given | your version |

### Status of the root
- Smith (1939) has no DOI or journal page that this search could open, so no retraction or correction check was possible.
- [Duchan](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html) reports that Smith's studies "were later found to be methodologically flawed". The page names no later study.
- Major later study: [Muszyńska et al., *Bilingual children reach early language milestones at the same age as monolingual peers*, Journal of Child Language, 2025](https://www.cambridge.org/core/journals/journal-of-child-language/article/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers/0BFAB689DC70E5A2A5220976E1939948). It compared 302 Polish-bilingual children with 302 matched monolingual children, using parent reports in an app. It found no significant difference in the age of the first word, the 10th word or the first multiword utterance. For the 50th word and 3-word utterances, the evidence was inconclusive.

### Cold trails
- [Speech Blubs](https://speechblubs.com/blog/bilingual-kids-do-they-speak-later-unpacking-the-myth), 2025: states the belief and cites nothing for its origin.
- [The Multilingual Garden](https://www.themultilingualgarden.com/blog/do-bilingual-children-start-talking-later-than-monolinguals), date unknown: states the belief and cites nothing for its origin.
- [Homeschool Spanish Academy](https://www.spanish.academy/blog/are-bilingual-children-more-likely-to-experience-a-speech-or-language-delay/), 2024: states the belief and cites nothing for its origin.

### Confidence
Medium: the root is a Primary I could not open, dated only through Duchan. No modern retelling cites Smith, so the link between your version and the root rests on matching content, not on citations. Several secondary sources on the 1920s–30s "language handicap" research (Haugen 1956, Hakuta 1986 and 2011, the British Council, *The Reading Teacher*, PMC) failed to load or returned unreadable scans.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
