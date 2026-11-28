---
case: no-memory-bilingual-speech
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:37:21Z
cost_usd: 2.0742
duration_s: 307
turns: 41
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
- WebSearch: origin of the belief that bilingualism causes speech delay history
- WebSearch: bilingual first words age study same milestones monolingual Petitto Genesee
- WebSearch: Saer 1923 bilingualism Welsh children inferior early research language handicap
- WebSearch: fact check bilingual babies talk later speech delay
- WebFetch: https://littlewords.ai/blog/bilingual-children-speech-delay-myth
- WebFetch: https://www.teachingangel.com/articles/late-talking-and-bilingualism/
- WebFetch: https://www.spanish.academy/blog/are-bilingual-children-more-likely-to-experience-a-speech-or-language-delay/
- WebFetch: https://www.rubytherapy.ca/speech-therapy-resources/speech-therapy-edmonton-bilingual-language-development-66h28
- WebFetch: https://www.themultilingualgarden.com/blog/bilingual-child-speech-delay
- WebFetch: https://en.wikipedia.org/wiki/Speech_delay
- WebSearch: Leung Kao 1999 "Evaluation and management of the child with speech delay" American Family Physician bilingual home
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC4180217
- WebFetch: https://www.aafp.org/afp/1999/0601/p3121
- WebFetch: https://www.aafp.org/afp/2011/0515/p1183
- WebSearch: "Saer" 1923 "bilingualism" "language development" obstacle Pintner Peal Lambert
- WebSearch: Saer "The effect of bilingualism on intelligence" British Journal of Psychology 1923 abstract
- WebSearch: Madorah Smith 1939 Hawaii bilingual preschool children vocabulary retarded English mastery study
- WebFetch: https://bpspsychub.onlinelibrary.wiley.com/doi/abs/10.1111/j.2044-8295.1923.tb00110.x
- WebFetch: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0BFAB689DC70E5A2A5220976E1939948/S0305000924000655a.pdf/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers.pdf
- WebFetch: https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1986)%20-%20MIRROR%20OF%20LANGUAGE%20THE%20DEBATE%20ON%20BILINGUALISM.pdf
- WebFetch (error): https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1017/S0305000924000655&resultType=core&format=json
- WebFetch: https://web.stanford.edu/~hakuta/www/research/publications/(1987)%20-%20BILINGUALISM%20AND%20COGNITIVE%20DEVELOPMENT%20THREE%20PERSPE.pdf
- WebFetch: https://www.levyinstitute.org/pubs/wp/229.pdf
- WebSearch: "Smith" 1939 bilingual children Hawaii "speech" delay belief origin bilingualism myth history review
- WebFetch: https://commons.und.edu/cgi/viewcontent.cgi?article=10630&context=theses
- WebFetch: https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html
- WebFetch: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22Lexical%20development%20in%20bilingual%20infants%20and%20toddlers%22&resultType=core&format=json
- WebSearch: Pearson Fernández Oller 1993 "Lexical development in bilingual infants and toddlers: Comparison to monolingual norms" Language Learning abstract
- WebFetch: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-1770.1993.tb00174.x
- WebFetch: https://api.crossref.org/works/10.1111/j.1467-1770.1993.tb00174.x

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Bilingual children start speaking later."

**Roots:** Echo · **Grounding:** Primary differs · Mutated
**Earliest instance found:** [Leung & Kao, *Evaluation and Management of the Child with Speech Delay*, American Family Physician](https://www.aafp.org/afp/1999/0601/p3121), 1999 (date from: byline). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 6

### Chain
Your version: "Bilingual children start speaking later." (where you met it: not given)
 ├─ [Little Words, *The bilingual speech delay myth*](https://littlewords.ai/blog/bilingual-children-speech-delay-myth), date unknown, Secondary → cites
 │   └─ [Pearson, Fernández & Oller, *Lexical Development in Bilingual Infants and Toddlers*, Language Learning 43(1)](https://api.crossref.org/works/10.1111/j.1467-1770.1993.tb00174.x), 1993, Primary (differs)
 └─ [Leung & Kao, American Family Physician](https://www.aafp.org/afp/1999/0601/p3121), 1999, Tertiary, root

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Hedge dropped | a bilingual home "may cause a temporary delay in the onset of both languages" ([Leung & Kao](https://www.aafp.org/afp/1999/0601/p3121)) | Bilingual children start speaking later. | [Teaching Angel](https://www.teachingangel.com/articles/late-talking-and-bilingualism/), 2022 |
| Context removed | the delay is *temporary*, and the child's understanding of both languages is normal for their age | Bilingual children start speaking later. | [Teaching Angel](https://www.teachingangel.com/articles/late-talking-and-bilingualism/), 2022 |

### Status of the root
- No primary found, so there was no status to check.
- Pearson, Fernández & Oller (1993): the abstract compares 25 bilingual and 35 monolingual children aged 8–30 months and found "no statistical basis for concluding that the bilingual children were slower" ([Crossref record](https://api.crossref.org/works/10.1111/j.1467-1770.1993.tb00174.x)). The Crossref record lists no correction or retraction. The Wiley page returned an error (403).
- Pearson, Fernández & Oller (1993): the 2011 review in the same journal as the root, [McLaughlin, *Speech and Language Delay in Children*](https://www.aafp.org/afp/2011/0515/p1183), cites Leung & Kao only for the point that bilingual children usually become proficient in both languages by age five. It says bilingual children should be referred for speech therapy on the same criteria as monolingual children.
- Background: Madorah Smith, *Some light on the problem of bilingualism…*, Genetic Psychology Monographs 21, 1939 (not opened). It studied preschool children in Hawaii, and according to a history-of-the-field biography she concluded that "simultaneous use of two languages contributed to a lag in speech development" ([Duchan, *A History of Speech-Language Pathology*](https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/)). The same page says her widely cited studies were later found to be methodologically flawed: she compared poor immigrant children with middle-class native-born children. No retelling of the claim that I opened credits her by name.
- Background: [The Multilingual Garden](https://www.themultilingualgarden.com/blog/bilingual-child-speech-delay) traces the belief to flawed early-twentieth-century studies that compared working-class immigrant children with better-off monolingual peers. It names no study.

### Cold trails
- [The Multilingual Garden, *Bilingual Child Speech Delay*](https://www.themultilingualgarden.com/blog/bilingual-child-speech-delay), date unknown: describes the belief and credits unnamed early-1900s studies.
- [Teaching Angel, *Late Talking and Bilingualism*](https://www.teachingangel.com/articles/late-talking-and-bilingualism/), 2022: describes the belief as common and cites nothing for where it came from.
- [Homeschool Spanish Academy, *Are Bilingual Children More Likely to Experience a Speech or Language Delay?*](https://www.spanish.academy/blog/are-bilingual-children-more-likely-to-experience-a-speech-or-language-delay/), 2024: traces the belief to the idea that bilingual children get confused, and cites nothing for that.

### Confidence
Medium: the 1999 root was opened and dated from its byline, but it cites nothing, and the likely older academic source (Smith 1939) and the 1993 study's full text could not be opened.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
