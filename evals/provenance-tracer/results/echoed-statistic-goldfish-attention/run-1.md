---
case: echoed-statistic-goldfish-attention
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-26T12:17:02Z
cost_usd: 1.3264
duration_s: 160
turns: 38
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
- WebSearch: humans 8 second attention span goldfish 9 seconds
- WebSearch: Microsoft Canada 2015 attention spans consumer insights report goldfish
- WebSearch: "8.25 seconds" attention span Statistic Brain source
- WebSearch: origin of goldfish attention span statistic where did it come from
- WebSearch: goldfish attention span myth fact check BBC
- WebFetch: https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf
- WebFetch (error): https://www.bbc.com/news/health-38896790
- WebFetch: https://medium.com/psynamic/8-second-attention-spans-tracking-the-myth-that-just-wont-quit-614dd2cb9792
- WebFetch (error): https://web.archive.org/cdx/search/cdx?url=statisticbrain.com/attention-span-statistics/&limit=5
- Read (denied): <temp>/config/projects/-private-tmp-e-D3RUvj-home-cwd/6f0e8036-5b71-4a8c-9a83-d654410ff05f/tool-results/webfetch-1795695448440-bylzwf.pdf
- WebFetch (error): https://www.bbc.co.uk/news/health-38896790
- WebFetch: https://www.swordandthescript.com/2022/02/goldfish-attention-span/
- WebFetch: http://www.marketplace.org/2014/02/11/business/goldfish-have-longer-attention-spans-americans-and-publishing-industry-knows-it
- WebFetch: http://time.com/3858309/attention-spans-goldfish/
- WebFetch: https://www.mangalam.nl/wp-content/uploads/2019/05/microsoft-attention-spans-research-report.pdf
- WebFetch: https://scienceblog.com/t-humans-eight-second-attention-span-goldfish-myth/
- WebFetch: https://www.scribd.com/document/736691392/Microsoft-Attention-Spans-Research-Report
- WebFetch: https://uxpsychology.substack.com/p/the-attention-span-myth
- WebFetch: https://www.marketplace.org/2014/02/11/business/goldfish-have-longer-attention-spans-americans-and-publishing-industry-knows-it
- WebSearch: statisticbrain "attention span statistics" goldfish 2013 "Associated Press" earliest
- WebFetch: https://www.tryhugo.app/blog/average-attention-span-goldfish-myth
- WebFetch: https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/
- WebFetch: https://www.prc.za.com/2016/11/18/attention-spans-report-microsoft-2015/
- WebFetch: https://policyviz.com/2016/01/29/the-attention-span-statistic-fallacy/
- WebFetch (error): http://news.bbc.co.uk/2/hi/science/nature/1834682.stm
- WebFetch: https://prc.za.com/wp-content/uploads/2016/11/2015-Attention-Spans-Report-Microsoft.pdf
- WebFetch (error): https://www.statisticbrain.com/attention-span-statistics/
- WebFetch: https://ccit.college.columbia.edu/sites/ccit/files/weinreich-web-use-study.pdf
- WebFetch (error): http://www.telegraph.co.uk/science/2016/03/12/humans-have-shorter-attention-span-than-goldfish-thanks-to-smart/

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Human attention span is now shorter than a goldfish's"

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** [Statistic Brain, *Attention Span Statistics*](https://www.statisticbrain.com/attention-span-statistics/), 2012 (date from: cited by [Hugo](https://www.tryhugo.app/blog/average-attention-span-goldfish-myth), which reports a Wayback Machine capture from 8 February 2012). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 5

### Chain
Your version: "Human attention span is now shorter than a goldfish's" (where you met it: not given)
 └─ [Time, *You Now Have a Shorter Attention Span Than a Goldfish*](http://time.com/3858309/attention-spans-goldfish/), Kevin McSpadden, 2015, Secondary: "people now generally lose concentration after eight seconds". It credits the figure to "a new study from Microsoft" → cites
     └─ [Microsoft Canada Consumer Insights, *Attention Spans*](https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf), Spring 2015, (not opened), per [Sword and the Script](https://www.swordandthescript.com/2022/02/goldfish-attention-span/), [UX Psychology](https://uxpsychology.substack.com/p/the-attention-span-myth) and [PolicyViz](https://policyviz.com/2016/01/29/the-attention-span-statistic-fallacy/). These pages say the report's chart gives 12 s (2000), 8 s (2013) and 9 s for a goldfish, says the figures come from Statistic Brain, and that the report's own survey and EEG work did not measure attention span in seconds. Its PDF came back as unreadable binary. → cites
         └─ [Statistic Brain, *Attention Span Statistics*](https://www.statisticbrain.com/attention-span-statistics/), 2012, (not opened), per [Hugo](https://www.tryhugo.app/blog/average-attention-span-goldfish-myth). Hugo says the 2012 capture labels 8 s as "2012" and credits the Associated Press, and a 2015 capture relabels it "2013" and adds NCBI/NLM. The domain no longer resolves. → cites
             └─ The Associated Press, date unknown, (not opened), per [PolicyViz](https://policyviz.com/2016/01/29/the-attention-span-statistic-fallacy/) and [Hugo](https://www.tryhugo.app/blog/average-attention-span-goldfish-myth). No article was named. → stopped: not opened

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Context removed | A dated figure: 8 seconds in 2012 (later relabelled 2013), against 12 seconds in 2000 and 9 for a goldfish, per Hugo's reading of the archive | "now shorter than a goldfish's" | [Time](http://time.com/3858309/attention-spans-goldfish/), 2015 |
| Other: date moved | 8 seconds labelled as the 2012 figure | 8 seconds labelled 2013 (Microsoft report and later retellings) | Statistic Brain 2015 capture, per [Hugo](https://www.tryhugo.app/blog/average-attention-span-goldfish-myth) |

### Status of the root
- No primary found, so there was no status to check.
- [PolicyViz](https://policyviz.com/2016/01/29/the-attention-span-statistic-fallacy/) (2016) reports that it emailed the US National Library of Medicine, which Statistic Brain listed as a source. The library said it "cannot verify it". Statistic Brain did not answer PolicyViz's email.
- [Sword and the Script](https://www.swordandthescript.com/2022/02/goldfish-attention-span/) (2022) reports that the BBC's *More or Less* (Simon Maybin, 2017) contacted the sources Statistic Brain listed, and neither could find supporting research. It also quotes the BBC as saying there is no evidence that goldfish have particularly short attention spans. The BBC article itself could not be fetched.

### Cold trails
- [BBC News](http://news.bbc.co.uk/2/hi/science/nature/1834682.stm), February 2002, (not opened), per [A Patchwork of Perceptions](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/). It states a variant: web browsing can leave you with a nine-second attention span, the same as a goldfish's. It cites nothing for this, and the opened post calls it the first instance of the comparison stated as fact. No chain links it to Statistic Brain.

### Confidence
Low. Only Time was opened among the pages that state the claim, and the chain stops at sources that were not opened (the Microsoft report, the Statistic Brain archive captures, the Associated Press) short of any node that cites nothing.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
