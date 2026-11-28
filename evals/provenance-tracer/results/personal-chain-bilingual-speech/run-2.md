---
case: personal-chain-bilingual-speech
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:42:28Z
cost_usd: 1.8794
duration_s: 246
turns: 40
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
- WebSearch: bilingualism causes language delay in toddlers myth
- WebSearch: bilingual children first words age study monolingual comparison Petitto first words milestones
- WebSearch: origin of belief bilingual children talk late history Saer 1923 bilingual handicap
- WebSearch: bilingual children speech delay fact check
- WebSearch: bilingual kids speak later business magazine raising bilingual children
- WebFetch: https://files.eric.ed.gov/fulltext/ED283368.pdf
- WebFetch: https://arxiv.org/pdf/physics/0510019
- WebFetch: https://parentdata.org/kids/do-bilingual-children-speak-later/
- WebFetch: https://www.themultilingualgarden.com/blog/do-bilingual-children-start-talking-later-than-monolinguals
- WebFetch: https://www.cambridge.org/core/journals/journal-of-child-language/article/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers/0BFAB689DC70E5A2A5220976E1939948
- WebFetch: https://www.trilingualchildren.com/2014/04/bilingualism-speech-delay.html
- WebSearch: "handicapped in his language growth" bilingual
- WebSearch: Madorah Smith 1939 bilingual children Hawaii speech retardation preschool vocabulary study
- WebFetch: https://tollbit.parentdata.org/kids/do-bilingual-children-speak-later/
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1987)%20-%20BILINGUALISM%20AND%20COGNITIVE%20DEVELOPMENT%20THREE%20PERSPE.pdf
- WebFetch: https://edweek.org/ew/articles/1987/04/01/27cog.h06.html
- WebFetch: https://our-languages.canada.ca/en/blogue-blog/multilinguisme-multilingualism-eng
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1986)%20-%20MIRROR%20OF%20LANGUAGE%20THE%20DEBATE%20ON%20BILINGUALISM.pdf
- WebFetch: https://web.stanford.edu/~hakuta/Courses/Ed330X%20Website/Educating%20Language%20Minority%20Students%20and%20Affirming%20their%20Equal%20Rights%20-%20Brown%20Lecture.pdf
- WebFetch: https://www.ericdigests.org/pre-9217/academic.htm
- WebFetch: https://www.levyinstitute.org/pubs/wp/229.pdf
- WebFetch: https://journals.sagepub.com/stoken/default+domain/qMtnCUVs54Gq3vdMD43N/full
- WebFetch: https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/
- WebSearch: "attempt to make use of two languages" Smith 1939
- WebFetch: https://web.stanford.edu/~hakuta/www/research/publications/(1987)%20-%20BILINGUALISM%20AND%20COGNITIVE%20DEVELOPMENT%20THREE%20PERSPE.pdf
- WebFetch: https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later
- WebFetch: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6168212/
- WebFetch: https://www.healthychildren.org/English/ages-stages/gradeschool/school/Pages/7-Myths-Facts-Bilingual-Children-Learning-Language.aspx
- WebSearch: Smith 1939 "Some light on the problem of bilingualism" Genetic Psychology Monographs full text
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/
- WebFetch: https://files.eric.ed.gov/fulltext/ED273152.pdf

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches. Your manager's name went into none.
- Personal chain as you gave it: your manager (Hearsay) read it in a business magazine. No year was given, and the magazine wasn't named, so I couldn't search for it.

## Provenance: "Bilingual children start speaking later."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** Madorah E. Smith, *Some light on the problem of bilingualism as found from a study of the progress in mastery of English among preschool children of non-American ancestry in Hawaii*, Genetic Psychology Monographs 21, 1939 (date from: cited by [A History of Speech-Language Pathology, University at Buffalo](https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 9

### Chain
Your version: "Bilingual children start speaking later." (you heard it: from your manager (Hearsay), who read it in a business magazine; year not given; matches no node, since the magazine was not found)
 ├─ [Trilingual Children blog](https://www.trilingualchildren.com/2014/04/bilingualism-speech-delay.html), 2014, Tertiary → cites
 │   └─ François Rochon, *Language development in bilingual babies: no delays, just a few adjustments*, University of Ottawa, date unknown, (not opened), per Trilingual Children → stopped: not opened
 ├─ [Education Week, James Crawford](https://edweek.org/ew/articles/1987/04/01/27cog.h06.html), 1987, Tertiary → cites
 │   └─ [Kenji Hakuta, *Mirror of Language: The Debate on Bilingualism*](https://web.stanford.edu/~hakuta/Publications/(1986)%20-%20MIRROR%20OF%20LANGUAGE%20THE%20DEBATE%20ON%20BILINGUALISM.pdf), 1986, (not opened, scanned PDF with no text), per Education Week → cites
 │       └─ George Thompson, child psychology textbook, 1952, (not opened), per Education Week → stopped: not opened
 └─ [A History of Speech-Language Pathology, University at Buffalo](https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/), date unknown, Secondary → cites
     └─ Smith, *Genetic Psychology Monographs* 21: 121–284, 1939, Primary (not opened, per A History of Speech-Language Pathology), root

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | Smith studied preschool children of many ethnic backgrounds in Hawaii (per the Buffalo history page) | Bilingual children start speaking later. | Thompson's textbook, 1952 (not opened, per [Education Week](https://edweek.org/ew/articles/1987/04/01/27cog.h06.html)) |
| Hedge dropped | Using two languages *contributed to* a lag, as one factor among others (per the Buffalo history page) | Bilingual children start speaking later. | Thompson's textbook, 1952 (not opened, per [Education Week](https://edweek.org/ew/articles/1987/04/01/27cog.h06.html)) |
| Other: what was measured | A lag in speech development, measured as preschoolers' progress in mastering English, became the age at which children *start* speaking | Bilingual children start speaking later. | [Trilingual Children blog](https://www.trilingualchildren.com/2014/04/bilingualism-speech-delay.html), 2014 |

### Status of the root
- No retraction or correction check was possible. I found no DOI or publisher page for the 1939 monograph, and I could not open any copy of it.
- Smith 1939: the [University at Buffalo history page](https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/) says her studies "were later found to be methodologically flawed". It says she compared poor immigrant children with middle-class children born in the US.
- Major later study: [Muszyńska et al., *Journal of Child Language*, 2025](https://www.cambridge.org/core/journals/journal-of-child-language/article/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers/0BFAB689DC70E5A2A5220976E1939948) followed 302 Polish bilingual children and 302 matched monolingual children. It found no difference in the age of the first word, the 10th word or the first multi-word sentence. It also notes that bilinguals' vocabulary in any one language can lag, which "do not necessarily imply clinically relevant delays".

### Cold trails
- [amma.family](https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later), 2024: states the idea and calls it one of the myths about bilingualism. It cites nothing for where the idea came from.
- [The Multilingual Garden](https://www.themultilingualgarden.com/blog/do-bilingual-children-start-talking-later-than-monolinguals), date unknown: describes it as a common worry among parents. It blames the idea on misunderstandings and cites no source for it.

### Confidence
Medium. The 1939 root and the 1952 textbook could not be opened, and the root's date rests on one undated history page.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
