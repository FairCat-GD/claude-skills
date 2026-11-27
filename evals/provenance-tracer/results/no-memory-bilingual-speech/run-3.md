---
case: no-memory-bilingual-speech
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:14:29Z
cost_usd: 1.2655
duration_s: 160
turns: 31
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
- WebSearch: origin of belief bilingual children talk later history Saer 1923 Smith 1939 Hawaii
- WebSearch: bilingual toddlers first words age study Pearson Fernández Oller 1993 vocabulary
- WebSearch: bilingual children speak later fact check
- WebSearch: "bilingual" "speech delay" earliest claim "mental confusion" 1920s research history
- WebFetch: https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1987)%20-%20BILINGUALISM%20AND%20COGNITIVE%20DEVELOPMENT%20THREE%20PERSPE.pdf
- WebFetch: https://www.levyinstitute.org/pubs/wp/229.pdf
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC5214932/
- WebFetch: https://www.habilnet.org/bilingual-children-do-not-start-speaking-later-than-monolingual-ones/
- WebFetch: https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay
- WebSearch: Madorah Smith 1939 "Some light on the problem of bilingualism" Genetic Psychology Monographs
- WebFetch: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6562894/
- WebFetch (error): https://web.archive.org/cdx/search/cdx?url=acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html&limit=1
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC6562894/
- WebFetch: https://files.eric.ed.gov/fulltext/ED273152.pdf
- WebFetch: https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/
- WebFetch: https://link.springer.com/chapter/10.1007/978-3-030-87063-8_2
- WebFetch: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-1770.1993.tb00174.x
- WebFetch: https://www.famly.co/us/blog/bilingualism-language-development-in-early-childhood
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/
- WebFetch (error): http://www.ciil-ebooks.net/html/bilingualism/part%201.htm

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Bilingual children start speaking later."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** Madorah Smith, *Some light on the problem of bilingualism as found from a study of the progress in mastery of English among preschool children of non-American ancestry in Hawaii*, Genetic Psychology Monographs 21, 1939 (date from: cited by [Judy Duchan's History of Speech-Language Pathology](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 5

### Chain
Your version: "Bilingual children start speaking later." (where you met it: not given)
 └─ [Judy Duchan, *Madorah Smith*, History of Speech-Language Pathology](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html), date unknown, Secondary. It says Smith concluded that using two languages "contributed to a lag in speech development". → cites
     └─ Smith, M. (1939), *Some light on the problem of bilingualism…*, Genetic Psychology Monographs 21, 1939, Primary (not opened, per Duchan) → stopped: not opened

 A related branch about an older and different 1920s claim (mental confusion and low intelligence, not later speech):
 └─ [Bialystok & Werker, *The Systematic Effects of Bilingualism on Children's Development*, Developmental Science](https://pmc.ncbi.nlm.nih.gov/articles/PMC5214932/), 2017, Secondary. It says that from the 1920s psychologists issued "warnings of “mental confusion” (Saer, 1923) and “retardation” (Goodenough, 1926)", and that the public accepted these warnings widely enough to make parents anxious about raising children bilingually. → cites
     ├─ Saer, D. J. (1923), *The effect of bilingualism on intelligence*, British Journal of Psychology 14, 1923, Primary (not opened, per Bialystok & Werker) → stopped: not opened
     └─ Goodenough, F. (1926), 1926, Primary (not opened, per Bialystok & Werker) → stopped: not opened

### How it changed
These rows compare your version with Smith 1939 as Duchan describes it, because the monograph itself could not be opened.

| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | Preschool children of non-American ancestry in Hawaii, studied for their progress in English | bilingual children (all of them) | [habilnet, De Houwer & Pascall](https://www.habilnet.org/bilingual-children-do-not-start-speaking-later-than-monolingual-ones/), 2021, as a belief it attributes to professionals |
| Hedge dropped | Using two languages "contributed to" a lag | stated flatly | habilnet, 2021 |
| Context removed | Duchan says Smith compared poor immigrant children with middle-class native-born Americans, measuring English only | no comparison group or language of measurement given | your version |
| Other: the outcome changed | A lag in speech *development*, measured in preschoolers' English | a later *start* to speaking | habilnet, 2021 |

### Status of the root
- Smith 1939 has no DOI I could find and its text could not be opened, so I could not check it through the journal page, Crossref, Retraction Watch or PubPeer.
- [Duchan's page](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html) says Smith's studies were "later found to be methodologically flawed". The page names no source for this, so it is a lead and not a confirmed status.
- A major later study, Pearson, Fernández & Oller, *Lexical Development in Bilingual Infants and Toddlers: Comparison to Monolingual Norms*, Language Learning 43, 1993, was (not opened): [the Wiley page](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-1770.1993.tb00174.x) returned 403. I can't report its findings from an opened page.
- Bialystok & Werker 2017, on the Saer/Goodenough branch: the article says research from Peal & Lambert (1962) onward took the opposite view to those early warnings.

### Cold trails
- [habilnet, De Houwer & Pascall, *Bilingual children do not start speaking later than monolingual ones*](https://www.habilnet.org/bilingual-children-do-not-start-speaking-later-than-monolingual-ones/), 2021 (byline: German original April 2021). It says many professionals "are still convinced that bilingual children start speaking later than monolingual ones". It cites research on development but nothing for where the belief came from.
- [Nationwide Children's Hospital, 700 Children's blog](https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay), 2017. It calls the idea one that "has been a long-standing myth in the United States" and cites no sources.
- [Famly, Caley O. Nunnally, *Myth: Bilingualism causes language delay in early childhood*](https://www.famly.co/us/blog/bilingualism-language-development-in-early-childhood), 2024. It calls the idea a "common misconception" and cites nothing for its origin.

### Confidence
Medium. The root (Smith 1939) and the Saer/Goodenough primaries could not be opened, the root's date rests on *cited by*, and the Duchan page's own date could not be found because the archive lookup failed.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
