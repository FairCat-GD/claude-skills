---
case: non-interactive-goldfish-attention
run: 1
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T15:39:58Z
cost_usd: 1.3867
duration_s: 171
turns: 36
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
- WebSearch: humans have 8 second attention span goldfish 9 seconds Microsoft study
- WebSearch: Statistic Brain attention span statistics 8.25 seconds source
- WebSearch: origin of goldfish attention span myth 8 seconds
- WebSearch: goldfish attention span claim fact check BBC More or Less
- WebSearch: Microsoft Canada "Attention Spans" consumer insights 2015 report PDF
- WebFetch: https://storage.googleapis.com/public.papers.www.brainsights.com/Microsoft_Attention%20Spans.pdf
- WebFetch: https://time.com/3858309/attention-spans-goldfish/
- WebFetch (error): https://www.bbc.com/news/health-38896790
- WebFetch (error): https://web.archive.org/cdx/search/cdx?url=statisticbrain.com/attention-span-statistics/&limit=5
- Read (denied): <temp>/config/projects/-private-tmp-e-tCY8SP-home-cwd/babfc370-6820-4de5-a5cc-9466b8dabd52/tool-results/webfetch-1795794025006-1fi2g6.pdf
- WebFetch (error): https://www.bbc.co.uk/news/health-38896790
- WebFetch (error): https://www.statisticbrain.com/attention-span-statistics/
- WebFetch (error): https://pdf4pro.com/view/microsoft-attention-spans-spring-2015-msadvertisingca-6dcfd0.html
- WebFetch: https://dam-it.io/guides/goldfish-attention-span-myth-8-seconds
- WebFetch: https://medium.com/psynamic/8-second-attention-spans-tracking-the-myth-that-just-wont-quit-614dd2cb9792
- WebFetch: https://www.mangalam.nl/wp-content/uploads/2019/05/microsoft-attention-spans-research-report.pdf
- WebFetch: https://stateofsurveillance.org/articles/corporate/attention-span-research-goldfish-myth-2026/
- WebFetch: https://en.wikipedia.org/wiki/Attention_span
- WebFetch (error): https://pdf4pro.com/view/microsoft-attention-spans-spring-2015-msadvertisingca-6dcfd0.html
- WebSearch: King's College London "attention span" goldfish Statistic Brain 2012 archive Associated Press report
- WebFetch: https://www.usecarly.com/blog/attention-span-statistics/
- WebFetch: https://www.tryhugo.app/blog/average-attention-span-goldfish-myth
- WebFetch: https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf
- WebFetch: https://www.kcl.ac.uk/policy-institute/assets/how-people-focus-and-live-in-the-modern-information-environment.pdf
- WebFetch (error): https://www.bbc.co.uk/programmes/p04vlq5r
- WebFetch: https://www.yourtango.com/self/your-attention-span-shorter-goldfishs-according-study
- WebFetch: https://www.geo.tv/latest/651046-global-pandemic-of-shrinking-attention-span

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Human attention span is now shorter than a goldfish's."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** [Statistic Brain, attention span statistics page](https://www.statisticbrain.com/attention-span-statistics/), 2012 (date from: cited by [usecarly](https://www.usecarly.com/blog/attention-span-statistics/), which links a Wayback Machine capture of 8 February 2012). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 6

### Chain
Your version: "Human attention span is now shorter than a goldfish's" (where you met it: not given)
 ├─ [YourTango](https://www.yourtango.com/self/your-attention-span-shorter-goldfishs-according-study), 2026, Tertiary → cites
 │   └─ [Geo TV](https://www.geo.tv/latest/651046-global-pandemic-of-shrinking-attention-span), 2026, Tertiary → cites nothing (cold trail; gives 8.25 seconds vs. 9 for a goldfish)
 └─ [Time](https://time.com/3858309/attention-spans-goldfish/), 2015, Tertiary → cites
     └─ [Microsoft Canada, *Attention spans*, Spring 2015](https://storage.googleapis.com/public.papers.www.brainsights.com/Microsoft_Attention%20Spans.pdf), 2015, (not opened), per [usecarly](https://www.usecarly.com/blog/attention-span-statistics/) and [Hugo](https://www.tryhugo.app/blog/average-attention-span-goldfish-myth). Both say its page 6 chart credits Statistic Brain. → cites
         └─ [Statistic Brain, attention span statistics page](https://www.statisticbrain.com/attention-span-statistics/), 2012, (not opened), per [usecarly](https://www.usecarly.com/blog/attention-span-statistics/), root → cites
             └─ Associated Press, date unknown, (not opened), per [usecarly](https://www.usecarly.com/blog/attention-span-statistics/) → stopped: not opened

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Date moved (the 8-second figure was relabelled from 2012 to 2013, then given as current) | According to usecarly's account of the 2012 capture, 8 seconds is the average attention span *in 2012*, against 9 seconds for a goldfish | Human attention span is now shorter than a goldfish's | [Time](https://time.com/3858309/attention-spans-goldfish/), 2015 |

### Status of the root
- No primary found, so there was no status to check.
- The Associated Press is the root's only cited source in 2012. [usecarly](https://www.usecarly.com/blog/attention-span-statistics/) reports that by March 2015 the Statistic Brain page also listed the NCBI and the US National Library of Medicine. It also reports that BBC *More or Less* (2017) contacted the NCBI and the AP, and found that "neither can find any record of research that backs up the stats." I could not fetch the BBC article itself.
- [Hugo](https://www.tryhugo.app/blog/average-attention-span-goldfish-myth) reports the same BBC check. It adds that the BBC could not reach Statistic Brain.

### Cold trails
- [Geo TV](https://www.geo.tv/latest/651046-global-pandemic-of-shrinking-attention-span), 2026: states the claim and cites nothing.

### Confidence
Low: the Microsoft report, the Statistic Brain page and its Associated Press credit could not be opened. Attempts on BBC, the Wayback Machine, statisticbrain.com and four copies of the report PDF all failed or returned no text. So the chain past Time rests on later secondary accounts, and it stops short of any node that cites nothing.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
