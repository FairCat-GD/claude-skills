---
case: no-memory-bilingual-speech
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-27T09:14:29Z
cost_usd: 1.7465
duration_s: 222
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
- WebSearch: bilingualism causes language delay myth origin
- WebSearch: origin of belief bilingual children talk later history Saer 1923 bilingualism harmful
- WebSearch: bilingual toddlers first words later study Pearson Fernández Oller 1993 vocabulary
- WebSearch: where did the idea that bilingualism delays speech come from early 20th century research
- WebSearch: fact check "bilingual" children "speech delay" myth ASHA
- WebFetch: https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later
- WebFetch: https://littlewords.ai/blog/bilingual-children-speech-delay-myth
- WebFetch: https://trufluencykids.com/myth-busting-bilingualism-and-speech-delays/
- WebFetch: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1095164/full
- WebSearch: Madorah Smith 1939 Hawaii bilingual preschool children speech retarded mastery of English
- WebFetch: https://www.kqed.org/news/11914760/when-you-dont-learn-your-parents-language-what-is-lost
- WebFetch: https://www.francoisgrosjean.ch/myths_en.html
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1986)%20-%20MIRROR%20OF%20LANGUAGE%20THE%20DEBATE%20ON%20BILINGUALISM.pdf
- WebFetch: https://ubwp.buffalo.edu/history-of-cds/madorah-elizabeth-smith-1884/
- WebFetch: https://www.edweek.org/teaching-learning/bilingualism-a-cognitive-advantage-or-disadvantage-for-children/1987/04
- Read (denied): <temp>/config/projects/-private-tmp-e-BUf45e-home-cwd/6c2e14e7-3b44-47a7-9b3f-ed8d9be21c58/tool-results/webfetch-1795770933285-mmqnxt.pdf
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1987)%20-%20BILINGUALISM%20AND%20COGNITIVE%20DEVELOPMENT%20THREE%20PERSPE.pdf
- WebSearch: Smith 1939 "Genetic Psychology Monographs" bilingualism "retardation in speech" OR "speech retardation" Hawaii preschool conclusion
- WebSearch: Thompson 1952 child psychology textbook bilingual children "handicapped in their language growth"
- WebFetch: https://files.eric.ed.gov/fulltext/ED273152.pdf
- WebFetch (error): http://file.snnu.net/res/20137/4/1157197b-c5a7-4754-8f6c-a1f10112638e.pdf
- WebFetch: https://www.ericdigests.org/pre-9217/academic.htm
- WebFetch: https://commons.und.edu/cgi/viewcontent.cgi?article=10630&context=theses
- WebSearch: "Some light on the problem of bilingualism" Smith 1939 full text
- WebFetch: https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html
- WebFetch: https://web.stanford.edu/~hakuta/Publications/(1989)%20-%20BILINGUALISM%20AND%20INTELLIGENCE%20TESTING%20AN%20ANNOTATED%20.pdf
- WebFetch: https://files.eric.ed.gov/fulltext/ED054656.pdf
- WebFetch: https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Bilingual children start speaking later."

**Roots:** Independent · **Grounding:** No primary found · Mutated
**Earliest instance found:** H. T. Manuel, 1935, on bilingual children being "handicapped" in language and cognitive development (date from: cited by [Hantman et al., *Frontiers in Psychology*](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1095164/full), 2023). Earlier instances may exist.
**Roots:** 2 · **Retellings found:** 10

### Chain
Your version: "Bilingual children start speaking later." (where you met it: not given)
 └─ [TruFluency Kids, *Myth Busting: Bilingualism and Speech Delays*](https://trufluencykids.com/myth-busting-bilingualism-and-speech-delays/), date unknown, Tertiary → cites
     └─ [Izzy Bloom, KQED, *When You Don't Learn Your Parents' Language, What Is Lost?*](https://www.kqed.org/news/11914760/when-you-dont-learn-your-parents-language-what-is-lost), 2022, Tertiary. It traces the "language handicap" theory to anti-immigrant sentiment in the early 1900s → cites
         └─ [James Crawford, *Education Week*, *Bilingualism: A Cognitive Advantage or Disadvantage for Children?*](https://www.edweek.org/teaching-learning/bilingualism-a-cognitive-advantage-or-disadvantage-for-children/1987/04), 1987, Secondary. It names Kenji Hakuta's history of the theory and Goodenough (1926) → cites
             └─ George Thompson, *Child Psychology* (Houghton Mifflin), 1952, (not opened), per *Education Week* 1987. *Education Week* says this textbook told readers that children raised bilingually are handicapped in their language growth → stopped: not opened
 └─ [Judy Duchan, *A History of Speech-Language Pathology*, Madorah Smith entry](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html), date unknown, Secondary. It says Smith "concluded the simultaneous use of two languages contributed to a lag in speech development" → cites
     └─ Madorah E. Smith, *Some light on the problem of bilingualism…among preschool children of non-American ancestry in Hawaii*, *Genetic Psychology Monographs* 21, 1939, Primary (not opened, per Duchan). No free full text was found.
 └─ [Hantman et al., *Frontiers in Psychology*](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1095164/full), 2023, Secondary → cites
     └─ Manuel, 1935, Primary (not opened, per Hantman et al.). It is cited for the fear that bilingual children would be "handicapped" in language and cognitive development.

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | Smith studied preschool children aged 2–6 of non-American ancestry in 1930s Hawaii (per Duchan) | bilingual children | Thompson, *Child Psychology*, 1952 (not opened), as paraphrased in [*Education Week*](https://www.edweek.org/teaching-learning/bilingualism-a-cognitive-advantage-or-disadvantage-for-children/1987/04), 1987 |
| Context removed | Smith compared poor immigrant children with middle-class native-born norms and did not separate fluent from limited bilinguals, according to [Duchan](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html) | bilingual children start speaking later | Thompson, 1952 (not opened), per *Education Week* 1987 |
| Other: different measure | Smith reported a "lag in speech development", meaning progress in English speech at ages 2–6 (per Duchan) | start speaking later, meaning the age of first words | [amma.family, *Do Bilingual Children Start Speaking Later?*](https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later), 2024 |

### Status of the root
- Smith 1939 was not opened. I did not check it for a retraction or correction in Crossref, Retraction Watch or PubPeer. A 1939 monograph without a DOI was not something I could check in those databases within this trace.
- Smith 1939: [Duchan](https://www.acsu.buffalo.edu/~duchan/new_history/hist19c/subpages/smith.html) says her widely cited studies "were later found to be methodologically flawed".
- Major later study: Pearson, Fernández & Oller (1993) counted words in both languages of bilingual toddlers aged 8–30 months. As [Byers-Heinlein & Lew-Williams, *Learning Landscapes*](https://pmc.ncbi.nlm.nih.gov/articles/PMC6168212/), 2013, report it, the toddlers knew "approximately the same number of words as monolingual children".
- Manuel 1935 was not opened, and I ran no status checks on it.

### Cold trails
- [François Grosjean, *Myths about bilingualism*](https://www.francoisgrosjean.ch/myths_en.html), date unknown. It states the myth that bilingualism delays language acquisition, calls it popular "in the middle of the 20th Century", and cites no early source.
- [amma.family, *Do Bilingual Children Start Speaking Later?*](https://amma.family/blog/new-parent/do-bilingual-children-start-speaking-later), 2024. It states the claim in this exact form, in order to answer it, and names no origin.

### Confidence
Medium: neither root (Smith 1939, Manuel 1935) nor the Thompson 1952 textbook could be opened, so what they say comes from opened secondary sources, and Manuel's 1935 date rests on *cited by*.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
