---
case: no-memory-bilingual-speech
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:37:21Z
cost_usd: 1.9860
duration_s: 261
turns: 42
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
- WebSearch: origin of belief bilingual children talk later history Saer 1923 bilingualism harmful
- WebSearch: bilingual toddlers first words age study vocabulary Pearson Fernández Oller 1993
- WebSearch: where did the idea that bilingual children speak late come from
- WebSearch: fact check "bilingual" children "speech delay" myth
- WebFetch: https://www.spanish.academy/blog/are-bilingual-children-more-likely-to-experience-a-speech-or-language-delay/
- WebFetch: https://littlewords.ai/blog/bilingual-children-speech-delay-myth
- WebFetch: https://pubs.asha.org/doi/10.1044/2023_JSLHR-23-00117
- WebFetch: https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/
- WebFetch: https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay
- WebFetch: https://www.themultilingualgarden.com/blog/do-bilingual-children-start-talking-later-than-monolinguals
- WebSearch: Madorah Smith 1939 bilingualism Hawaii preschool children vocabulary "language handicap"
- WebSearch: KQED bilingual children "language handicap" anti-immigrant early 1900s speech delay myth
- WebSearch: Petitto Holowka 2002 "Evaluating attributions of delay and confusion in young bilinguals"
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1987)%20-%20BILINGUALISM%20AND%20COGNITIVE%20DEVELOPMENT%20THREE%20PERSPE.pdf
- WebFetch: https://trufluencykids.com/myth-busting-bilingualism-and-speech-delays/
- WebFetch: https://commons.und.edu/cgi/viewcontent.cgi?article=10630&context=theses
- WebFetch: https://www.kqed.org/news/11914760/when-you-dont-learn-your-parents-language-what-is-lost
- WebFetch: https://web.stanford.edu/~hakuta/Courses/Ed330X%20Website/Educating%20Language%20Minority%20Students%20and%20Affirming%20their%20Equal%20Rights%20-%20Brown%20Lecture.pdf
- WebFetch: https://escholarship.org/content/qt11g6t4n8/qt11g6t4n8.pdf
- WebFetch: https://www.edweek.org/teaching-learning/bilingualism-a-cognitive-advantage-or-disadvantage-for-children/1987/04
- WebFetch: https://www.amacad.org/sites/default/files/academy/multimedia/pdfs/IA4th-Chapter%206-LanguageDiversityandResilience.pdf
- WebSearch: "an important factor in the retardation in speech" Smith 1939 bilingual Hawaii
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1986)%20-%20MIRROR%20OF%20LANGUAGE%20THE%20DEBATE%20ON%20BILINGUALISM.pdf
- WebFetch: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-1770.1993.tb00174.x
- WebFetch: https://en.wikipedia.org/wiki/Simultaneous_bilingualism
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1989)%20-%20BILINGUALISM%20AND%20INTELLIGENCE%20TESTING%20AN%20ANNOTATED%20.pdf
- WebFetch: https://files.eric.ed.gov/fulltext/ED283368.pdf
- WebFetch: https://archive.org/advancedsearch.php?q=title%3A%28genetic+psychology+monographs%29+AND+year%3A1939&fl%5B%5D=identifier&fl%5B%5D=title&rows=20&output=json
- WebFetch: https://archive.org/metadata/dli.ernet.4555
- WebFetch: https://ia601909.us.archive.org/26/items/dli.ernet.4555/4555-Genetic%20Psychology%20Monographs%20V-21_djvu.txt
- WebFetch: https://ia601909.us.archive.org/26/items/dli.ernet.4555/4555-Genetic%20Psychology%20Monographs%20V-21_djvu.txt

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: you said you don't remember where you heard it, so this is traced from the web alone.

## Provenance: "Bilingual children start speaking later."

**Roots:** Echo · **Grounding:** Primary differs · Mutated
**Earliest instance found:** [Madorah E. Smith, monograph on bilingualism among pre-school children in Hawaii, *Genetic Psychology Monographs* vol. 21](https://ia601909.us.archive.org/26/items/dli.ernet.4555/4555-Genetic%20Psychology%20Monographs%20V-21_djvu.txt), 1939 (date from: byline). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 14

### Chain
Your version: "Bilingual children start speaking later." (where you met it: not given)
 ├─ [TruFluency Kids, *Myth Busting: Bilingualism and Speech Delays*](https://trufluencykids.com/myth-busting-bilingualism-and-speech-delays/), date unknown, Tertiary → cites
 │   └─ [KQED, Izzy Bloom, *When You Don't Learn Your Parent's Language, What Is Lost?*](https://www.kqed.org/news/11914760/when-you-dont-learn-your-parents-language-what-is-lost), 2022, Tertiary → cites
 │       └─ [Education Week, James Crawford, *Bilingualism: A Cognitive Advantage or Disadvantage for Children?*](https://www.edweek.org/teaching-learning/bilingualism-a-cognitive-advantage-or-disadvantage-for-children/1987/04), 1987, Secondary → cites
 │           ├─ George Thompson, child psychology textbook, 1952, Primary (not opened, per Education Week) → stopped: not opened
 │           └─ [Kenji Hakuta, *Bilingualism and cognitive development: three perspectives*](https://web.stanford.edu/~hakuta/Publications/(1987)%20-%20BILINGUALISM%20AND%20COGNITIVE%20DEVELOPMENT%20THREE%20PERSPE.pdf), 1987, (not opened: an image-only scan with no readable text), per Education Week, which names Hakuta as having traced the "language handicap" theory → stopped: not opened
 ├─ [Wikipedia, *Simultaneous bilingualism*](https://en.wikipedia.org/wiki/Simultaneous_bilingualism), date unknown, Tertiary → cites
 │   └─ Diaz, 1984, (not opened), per Wikipedia → stopped: not opened
 └─ [Smith, *Genetic Psychology Monographs* vol. 21](https://ia601909.us.archive.org/26/items/dli.ernet.4555/4555-Genetic%20Psychology%20Monographs%20V-21_djvu.txt), 1939, Primary, root (found by searching for its own words; none of the retellings I could open cites it directly)

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | [Smith](https://ia601909.us.archive.org/26/items/dli.ernet.4555/4555-Genetic%20Psychology%20Monographs%20V-21_djvu.txt): trying to use two languages was "an important factor in the retardation in speech" among pre-school children of non-American ancestry in Hawaii | Bilingual children start speaking later. | [Education Week](https://www.edweek.org/teaching-learning/bilingualism-a-cognitive-advantage-or-disadvantage-for-children/1987/04), 1987 |
| Other: what was measured changed | progress in mastering English (the monograph's title), not the age at which children begin to talk | Bilingual children start speaking later. | [amma](https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later), 2024 |
| Context removed | the conclusions (p. 272) put the retardation down to two handicaps; bilingualism is one named factor among others | Bilingual children start speaking later. | [Education Week](https://www.edweek.org/teaching-learning/bilingualism-a-cognitive-advantage-or-disadvantage-for-children/1987/04), 1987 |

### Status of the root
- Smith's 1939 monograph has no DOI. I did not run the retraction and correction checks (journal page, Retraction Watch, PubPeer) because the fetch budget ran out.
- Later study: Pearson, Fernández & Oller (1993, *Language Learning*) is a Primary I could not open (the Wiley page returned 403), per [Byers-Heinlein & Lew-Williams, *Bilingualism in the Early Years: What the Science Says*, 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/). That review cites it, with Petitto & Holowka (2002), for this finding: bilingual children know fewer words in each language, but the gap disappears when vocabulary is counted across both languages. Neither later study set out to repeat Smith's.
- Background: [Education Week](https://www.edweek.org/teaching-learning/bilingualism-a-cognitive-advantage-or-disadvantage-for-children/1987/04) also names Goodenough (1926), on foreign-language use at home and group IQ. That is a related question, not speech onset, and no retelling credits it for this claim.

### Cold trails
- [Nationwide Children's Hospital](https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay), 2017: calls it a long-standing myth in the US, cites no source for where it began
- [Byers-Heinlein & Lew-Williams](https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/), 2013: puts parents' worries down to myths and misinterpretations, cites nothing for their origin
- [Spanish Academy, Leanne Sherred](https://www.spanish.academy/blog/are-bilingual-children-more-likely-to-experience-a-speech-or-language-delay/), 2024: suggests the belief comes from the idea that bilingual children get confused, cites nothing
- [amma](https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later), 2024: names the belief, gives no source for its origin
- [The Multilingual Garden, Karin Martin](https://www.themultilingualgarden.com/blog/do-bilingual-children-start-talking-later-than-monolinguals), date unknown: blames comparisons with monolingual children, cites nothing
- [Little Words](https://littlewords.ai/blog/bilingual-children-speech-delay-myth), date unknown: blames vocabulary counted in only one language, cites no source for that origin

### Confidence
Medium. The root is an opened Primary dated by its byline. But no retelling I could read links the popular claim back to Smith: Hakuta's reviews and the ERIC review were image-only scans, and the ASHA 2023 article returned 403. Several links in the chain stay not opened.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
