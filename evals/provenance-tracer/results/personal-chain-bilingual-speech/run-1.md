---
case: personal-chain-bilingual-speech
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:41:47Z
cost_usd: 1.6701
duration_s: 211
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
- WebSearch: origin of belief bilingual children talk later language delay history
- WebSearch: bilingual toddlers first words age study Petitto Pearson milestones
- WebSearch: bilingual children speech delay fact check
- WebSearch: early 20th century studies bilingualism handicap children Saer 1923 Smith 1939 language retardation
- WebFetch: https://pubs.asha.org/doi/10.1044/2023_JSLHR-23-00117
- WebFetch: https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay
- WebFetch: https://drhajartukur.substack.com/p/apparently-you-and-i-are-linguistically
- WebFetch: https://www.themultilingualgarden.com/blog/do-bilingual-children-start-talking-later-than-monolinguals
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1044/2023_JSLHR-23-00117&resultType=core&format=json
- WebSearch: Madorah Smith 1939 "Some light on the problem of bilingualism" Genetic Psychology Monographs
- WebFetch: https://doi.org/10.1080/00220671.1937.10880748
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC11361784/
- WebFetch: https://files.eric.ed.gov/fulltext/ED273152.pdf
- WebFetch: https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html
- WebSearch: "progress in mastery of English among preschool children of non-American ancestry in Hawaii" archive.org OR full text
- WebFetch (error): https://web.archive.org/cdx/search/cdx?url=acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html&limit=1
- WebFetch: https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later
- WebFetch: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6168212/
- WebFetch: https://link.springer.com/chapter/10.1007/978-3-030-87063-8_2
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/
- WebSearch: Madorah Smith bilingual Hawaii preschool "speech" delay criticized socioeconomic history of bilingualism research
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1987)%20-%20BILINGUALISM%20AND%20COGNITIVE%20DEVELOPMENT%20THREE%20PERSPE.pdf
- WebFetch: https://www.tandfonline.com/doi/abs/10.1080/08856559.1949.10533499
- WebFetch: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0BFAB689DC70E5A2A5220976E1939948/S0305000924000655a.pdf/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers.pdf
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1017/S0305000924000655&resultType=core&format=json
- WebFetch: https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/
- WebFetch: https://www.levyinstitute.org/pubs/wp/229.pdf

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches. Your manager's name doesn't.
- Personal chain: you heard it from your manager, who read it in a business magazine. You didn't name the magazine or the year, so it can't be matched to a node.

## Provenance: "Bilingual children start speaking later."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** Madorah E. Smith, *Some light on the problem of bilingualism as found from a study of the progress in mastery of English among preschool children of non-American ancestry in Hawaii*, Genetic Psychology Monographs 21, 1939 (date from: cited by [A History of Speech–Language Pathology: Madorah Smith](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 10

### Chain
Your version: "Bilingual children start speaking later." (you heard it: your manager, Hearsay, who read it in a business magazine; year not given)
 ├─ [amma.family, *Do Bilingual Children Start Speaking Later?*](https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later), 2024, Tertiary → cites
 │   └─ [Byers-Heinlein & Lew-Williams, *Bilingualism in the Early Years: What the Science Says*](https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/), 2013, Secondary (cites nothing earlier for the belief; see Cold trails)
 ├─ [Hajar Tukur, *Apparently, you and i are 'linguistically disabled'*](https://drhajartukur.substack.com/p/apparently-you-and-i-are-linguistically), 2026, Tertiary → cites
 │   └─ M. E. Smith's work, which the post dates only to the 1920s–30s → the Smith 1939 root below
 ├─ [Peña, Bedore & Granados Vargas, *Exploring Assumptions of the Bilingual Delay…*, JSLHR](https://pmc.ncbi.nlm.nih.gov/articles/PMC11361784/), 2023, Secondary → cites
 │   └─ Arsenian, 1937, (not opened), per Peña et al. 2023 → stopped: not opened
 ├─ [University at Buffalo, *History of CDS: Madorah Elizabeth Smith*](https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/), date unknown, Secondary → cites the Smith 1939 root below
 └─ [A History of Speech–Language Pathology: Madorah Smith](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html), date unknown, Secondary → cites
     └─ Smith, *Some light on the problem of bilingualism…*, Genetic Psychology Monographs 21, 1939, Primary (not opened, per A History of Speech–Language Pathology), root

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | Per the Buffalo history page, Smith found that "simultaneous use of two languages contributed to a lag in speech development" ([source](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html)). The children were preschoolers of non-American ancestry in Hawaii. | Bilingual children start speaking later. | [Byers-Heinlein & Lew-Williams](https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/), 2013 |
| Hedge dropped | Two languages *contributed to* the lag: one factor among others | Bilingual children start speaking later. | [Byers-Heinlein & Lew-Williams](https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/), 2013 |
| Other: a different measure | The 1939 study tracked progress in mastering English, and the lag it reported was in speech development | Bilingual children start speaking later. | [amma.family](https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later), 2024 |

### Status of the root
- No journal page, Crossref, Retraction Watch or PubPeer check was run for the 1939 monograph. No online copy or DOI turned up in the searches.
- Smith 1939: the [University at Buffalo history page](https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/) says her widely cited studies were later found to be methodologically flawed. It says she "paired poor immigrant children with middle-class native-born Americans" and did not separate fluent bilinguals from children with a poor command of one language.
- Later study: [Muszyńska et al., *Journal of Child Language*, 2025](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1017/S0305000924000655&resultType=core&format=json) compared 302 Polish bilingual children with 302 matched monolinguals on milestones including the first, 10th and 50th word. They report that "typical bilingual development follows a trajectory similar to monolingual development".
- Peña et al. 2023 say the deficit view is old. Citing Arsenian 1937, they say bilingual children of that era scored lower on IQ and language tasks given in the majority language. They also say bilingual children have historically been over-identified as having language disorder.
- Background: Saer's 1923 study gave intelligence tests to Welsh children and reported that bilingual children did worse, per [Tukur's post](https://drhajartukur.substack.com/p/apparently-you-and-i-are-linguistically). It was about intelligence scores, not the age children start speaking. Not opened.

### Cold trails
- [Byers-Heinlein & Lew-Williams](https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/), 2013: reports that parents feel their bilingual child is behind and puts this down to myths and misinterpretations, citing no source for where the belief came from
- [Nationwide Children's Hospital, *Teaching Kids a Second Language: Can It Cause a Speech Delay?*](https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay), 2017: calls the idea a long-standing myth in the United States, cites nothing
- [The Multilingual Garden, *Do Bilingual Children Start Talking Later Than Monolinguals?*](https://www.themultilingualgarden.com/blog/do-bilingual-children-start-talking-later-than-monolinguals), date unknown: puts the belief down to misunderstandings and monolingual comparisons, cites nothing

### Confidence
Medium: the 1939 monograph could not be opened, its date and wording come only from the Buffalo pages, and fetches of other histories (Hakuta 1987, an ERIC paper, a Springer chapter, a Levy Institute paper) returned no readable text.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
