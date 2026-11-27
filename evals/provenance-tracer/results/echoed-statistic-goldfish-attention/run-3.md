---
case: echoed-statistic-goldfish-attention
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T15:34:25Z
cost_usd: 1.3067
duration_s: 139
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
- WebSearch: "attention span" "shorter than a goldfish"
- WebSearch: humans 8 second attention span goldfish 9 seconds Microsoft study
- WebSearch: "8 seconds" attention span 2000 "12 seconds" Statistic Brain
- WebSearch: origin of goldfish attention span statistic
- WebSearch: goldfish attention span myth fact check BBC More or Less
- WebSearch: Microsoft Canada "Attention spans" consumer insights 2015 report PDF
- WebFetch: https://storage.googleapis.com/public.papers.www.brainsights.com/Microsoft_Attention%20Spans.pdf
- WebFetch (error): https://www.bbc.com/news/health-38896790
- WebFetch (error): https://web.archive.org/cdx/search/cdx?url=statisticbrain.com/attention-span-statistics/&limit=5
- WebSearch: TIME 2015 "You Now Have a Shorter Attention Span Than a Goldfish"
- WebFetch: https://pdfcoffee.com/microsoft-attention-spans-research-report-pdf-free.html
- WebFetch: https://time.com/3858309/attention-spans-goldfish/
- WebFetch: https://medium.com/psynamic/8-second-attention-spans-tracking-the-myth-that-just-wont-quit-614dd2cb9792
- WebFetch: https://elearningindustry.com/8-second-attention-span-organizational-learning
- WebFetch: https://pdfcookie.com/documents/microsoft-attention-spans-research-report-3lkzme99kplk
- WebFetch: https://www.mangalam.nl/wp-content/uploads/2019/05/microsoft-attention-spans-research-report.pdf
- WebFetch: https://scienceblog.com/t-humans-eight-second-attention-span-goldfish-myth/
- WebFetch: https://www.slideshare.net/sriushtiimx/microsoft-attentionspansresearchreport
- WebFetch (error): https://www.bbc.co.uk/news/health-38896790
- WebFetch: https://policyviz.com/2016/01/29/the-attention-span-statistic-fallacy/
- WebFetch: http://joyfulpublicspeaking.blogspot.com/2015/05/do-reporters-have-lower-attention-spans.html
- WebFetch (error): http://www.statisticbrain.com/attention-span-statistics/
- WebFetch: https://ccit.college.columbia.edu/sites/ccit/files/weinreich-web-use-study.pdf
- WebFetch: https://archive.org/wayback/available?url=statisticbrain.com/attention-span-statistics/&timestamp=20100101
- WebFetch: https://api.crossref.org/works/10.1145/1326561.1326566

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Human attention span is now shorter than a goldfish's."

**Roots:** Echo · **Grounding:** Primary differs · Mutated
**Earliest instance found:** [Statistic Brain, *Attention Span Statistics*](http://www.statisticbrain.com/attention-span-statistics/), 2012 (date from: archive, earliest Wayback capture 8 Feb 2012, via the [Wayback availability record](https://archive.org/wayback/available?url=statisticbrain.com/attention-span-statistics/&timestamp=20100101)). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 3

### Chain
Your version: "Human attention span is now shorter than a goldfish's" (where you met it: not given)
 └─ [Kevin McSpadden, *TIME*](https://time.com/3858309/attention-spans-goldfish/), 2015, Tertiary: credits a new Microsoft study → cites
     └─ [Microsoft Canada Consumer Insights, *Attention spans* (Spring 2015), SlideShare copy](https://www.slideshare.net/sriushtiimx/microsoft-attentionspansresearchreport), 2015, Tertiary: slide 6 gives 12 s (2000), 8 s (2013) and 9 s for a goldfish, with the line "Source: Statistic brain" → cites
         └─ [Statistic Brain, *Attention Span Statistics*](http://www.statisticbrain.com/attention-span-statistics/), 2012, Unknown (not opened, per [PolicyViz](https://policyviz.com/2016/01/29/the-attention-span-statistic-fallacy/)), root → credits Weinreich et al., the NCBI / U.S. National Library of Medicine and the Associated Press
             ├─ [Weinreich, Obendorf, Herder & Mayer, *Not quite the average: An empirical study of Web use*, ACM Transactions on the Web (Crossref record)](https://api.crossref.org/works/10.1145/1326561.1326566), 2008, Primary (credited, differs)
             └─ NCBI / U.S. National Library of Medicine and the Associated Press, date unknown, (not opened), per [PolicyViz](https://policyviz.com/2016/01/29/the-attention-span-statistic-fallacy/) → stopped: not opened

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Context removed | the root couldn't be opened; as the Microsoft report copies it, humans dropped from 12 s in 2000 to 8 s in 2013, and goldfish manage 9 s | Human attention span is now shorter than a goldfish's | [TIME](https://time.com/3858309/attention-spans-goldfish/), 2015 |

### Status of the root
- The root, Statistic Brain, is not a Primary and could not be opened. Its domain no longer resolves, and the Wayback capture could not be fetched. It had no retraction or correction to check.
- Weinreich et al. (the credited text): its [Crossref record](https://api.crossref.org/works/10.1145/1326561.1326566) describes a long-term study of how 25 people used the Web, covering backtracking, tabs and fast browsing. The abstract reports no attention span in seconds and nothing about goldfish. The record lists no retraction, correction or update.
- NCBI / National Library of Medicine: [PolicyViz](https://policyviz.com/2016/01/29/the-attention-span-statistic-fallacy/) (Jon Schwabish, 2016) reports that the NLM had received similar requests and replied that it "cannot verify it". The author's own email to Statistic Brain went unanswered.
- [eLearning Industry](https://elearningindustry.com/8-second-attention-span-organizational-learning) (Patti Shank, 2017) reports that the Weinreich study does not cite the listed statistics, and concludes "The numbers appear to be fiction!"
- Microsoft report: a [2015 blog post by Richard I. Garber](http://joyfulpublicspeaking.blogspot.com/2015/05/do-reporters-have-lower-attention-spans.html), published the day after TIME's article, says the 12-to-8-second drop was "NOT something found by the Microsoft research". The post says the figures were quoted from Statistic Brain on page 6. PolicyViz adds that the report's survey of 2,000 Canadians did not test attention span length.

### Cold trails
None.

### Confidence
Medium: the TIME and Microsoft nodes were opened and dated by byline, but the root (Statistic Brain) could not be opened, and its 2012 date rests on an archive capture record.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
