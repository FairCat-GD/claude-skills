---
case: no-memory-bilingual-speech
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T15:39:34Z
cost_usd: 1.5216
duration_s: 197
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
- WebSearch: origin of belief bilingual children talk late history Saer 1923 bilingualism handicap
- WebSearch: bilingual toddlers first words age study Pearson Fernández Oller 1993 vocabulary
- WebSearch: fact check "bilingual" children "speech delay" myth
- WebSearch: Smith 1939 bilingual Hawaii preschool vocabulary "language handicap" bilingualism early research
- WebFetch: https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later
- WebFetch: https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay
- WebFetch: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6562894/
- WebFetch: https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC6562894/
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1986)%20-%20MIRROR%20OF%20LANGUAGE%20THE%20DEBATE%20ON%20BILINGUALISM.pdf
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/
- WebFetch: https://frontiersin.org/articles/10.3389/fpsyg.2019.01346/full
- WebFetch: https://www-leland.stanford.edu/~hakuta/www/research/publications/(1987)%20-%20BILINGUALISM%20AND%20COGNITIVE%20DEVELOPMENT%20THREE%20PERSPE.pdf
- WebFetch: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-1770.1993.tb00174.x
- WebSearch: "Some light on the problem of bilingualism" Smith 1939 Genetic Psychology Monographs full text
- WebSearch: history myth bilingual children "language delay" Smith 1939 Hawaii "speech retardation" bilingual review
- WebFetch: https://files.eric.ed.gov/fulltext/ED273152.pdf
- WebFetch: https://commons.und.edu/cgi/viewcontent.cgi?article=10630&context=theses
- WebFetch: https://www.expressable.com/learning-center/tips-and-resources/do-bilingual-children-have-language-delays
- WebFetch: https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/
- WebFetch: https://www.cambridge.org/core/journals/journal-of-child-language/article/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers/0BFAB689DC70E5A2A5220976E1939948

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Bilingual children start speaking later than children who learn one language."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** Madorah Smith, *Some light on the problem of bilingualism as found from a study of the progress in mastery of English among preschool children of non-American ancestry in Hawaii*, Genetic Psychology Monographs 21, 1939 (date from: cited by [Duchan, *A History of Speech-Language Pathology*](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 7

### Chain
Your version: "Bilingual children start speaking later." (where you met it: not given)
 ├─ [Judy Duchan, *A History of Speech-Language Pathology*, Smith entry](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html), date unknown (site copyright 2001–2023), Secondary → cites
 │   └─ Smith, *Some light on the problem of bilingualism…*, Genetic Psychology Monographs 21, 1939, Primary (not opened, per Duchan), root
 └─ [Bright & Filippi, *Editorial: Perspectives on the 'Bilingual Advantage'*, Frontiers in Psychology](https://frontiersin.org/articles/10.3389/fpsyg.2019.01346/full), 2019, Secondary → credits Saer 1923
     └─ Saer, *The effect of bilingualism on intelligence*, British Journal of Psychology 14, 1923, Primary (not opened, per Bright & Filippi) → stopped: not opened

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | Preschoolers of non-American ancestry in Hawaii, measured against Smith's Iowa monolingual norms | Bilingual children start speaking later. | [Byers-Heinlein & Lew-Williams](https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/), 2013 |
| Other: the outcome changed, from progress in mastering English between ages 2 and 6 to the age at which speech begins | "simultaneous use of two languages contributed to a lag in speech development" ([Duchan](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html)) | Bilingual children start speaking later. | [amma.family, *Do Bilingual Children Start Speaking Later?*](https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later), 2024 |

### Status of the root
- No retraction or correction check was possible. The 1939 monograph has no DOI, its publisher (Journal Press) no longer exists, and I found no journal page or online copy. Crossref, Retraction Watch and PubPeer have nothing to search for it.
- [Duchan's history page](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html) reports that Smith's widely cited studies were later found to be methodologically flawed. It names two problems. Her poor immigrant children were compared with middle-class native-born American children. She also did not separate fluent bilinguals from children with limited command of either language.
- Later study: [Pearson, Fernández & Oller, *Lexical Development in Bilingual Infants and Toddlers*, Language Learning 43](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-1770.1993.tb00174.x), 1993, not opened (the fetch returned 403). [Byers-Heinlein & Lew-Williams (2013)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/) cite it for this finding: bilingual toddlers know fewer words in each language, but about as many as monolinguals when both languages are counted.
- Later study: [Muszyńska et al., *Bilingual children reach early language milestones at the same age as monolingual peers*, Journal of Child Language](https://www.cambridge.org/core/journals/journal-of-child-language/article/bilingual-children-reach-early-language-milestones-at-the-same-age-as-monolingual-peers/0BFAB689DC70E5A2A5220976E1939948), 2025. It followed 302 Polish bilingual children and 302 matched monolingual children, using parent reports. The milestones included first words, the 10th and 50th words, and first word combinations. The authors report that the bilingual children reached these milestones at similar ages.
- Review: [Byers-Heinlein & Lew-Williams (2013)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/) state that bilingual children are no more likely than monolingual children to show delays or to be diagnosed with a language disorder. They cite Paradis, Genesee & Crago (2010) and Petitto & Holowka (2002).
- Saer 1923: [Bright & Filippi (2019)](https://frontiersin.org/articles/10.3389/fpsyg.2019.01346/full) credit this Welsh IQ study as one early source of advice to raise children with one language. As they describe it, it reported a general mental delay on intelligence tests, not later speech. It was not opened, so its status was not checked.

### Cold trails
- [Byers-Heinlein & Lew-Williams, *Bilingualism in the Early Years: What the Science Says*](https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/), 2013: presents the belief as a misperception and gives no source for it. It suggests the belief arises from children knowing fewer words in each single language.
- [Nationwide Children's Hospital, *Teaching Kids a Second Language: Can It Cause a Speech Delay?*](https://www.nationwidechildrens.org/family-resources-education/700childrens/2017/12/teaching-kids-a-second-language-can-it-cause-a-speech-delay), 2017 (date from: byline, first published December 2017): calls it a long-standing myth in the United States that research has dispelled, and cites no studies.
- [amma.family, *Do Bilingual Children Start Speaking Later?*](https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later), 2024: states the belief in order to dispute it, and gives no source for where it came from.
- [Expressable, *Speech Delay in Bilingual & Multilingual Children*](https://www.expressable.com/learning-center/tips-and-resources/do-bilingual-children-have-language-delays), 2026: calls it a stubborn myth. It says the belief persists because adults count only the child's words in the majority language.

### Confidence
Medium: the root comes from an opened history page that names Smith's 1939 monograph, but the monograph itself could not be opened, so its date and conclusion rest on *cited by*.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
