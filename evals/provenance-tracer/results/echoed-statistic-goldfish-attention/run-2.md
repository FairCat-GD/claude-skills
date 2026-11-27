---
case: echoed-statistic-goldfish-attention
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T15:34:25Z
cost_usd: 1.3224
duration_s: 141
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
- WebSearch: humans 8 second attention span goldfish 9 seconds
- WebSearch: Microsoft Canada 2015 attention spans report goldfish
- WebSearch: "8.25 seconds" attention span Statistic Brain
- WebSearch: origin of goldfish attention span statistic myth source
- WebSearch: goldfish attention span fact check BBC More or Less
- WebFetch: https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf
- WebFetch (error): https://www.bbc.com/news/health-38896790
- WebFetch (error): https://web.archive.org/cdx/search/cdx?url=statisticbrain.com/attention-span-statistics/&limit=5
- WebFetch: https://medium.com/psynamic/8-second-attention-spans-tracking-the-myth-that-just-wont-quit-614dd2cb9792
- Read (denied): <temp>/config/projects/-private-tmp-e-dE5A6W-home-cwd/e12b7341-d2d8-48cb-b417-46ac65a60547/tool-results/webfetch-1795793690031-0i0xrf.pdf
- WebFetch: https://time.com/3858309/attention-spans-goldfish/
- WebFetch: https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/
- WebFetch: https://www.mangalam.nl/wp-content/uploads/2019/05/microsoft-attention-spans-research-report.pdf
- WebFetch: https://scienceblog.com/t-humans-eight-second-attention-span-goldfish-myth/
- WebFetch (error): https://www.statisticbrain.com/attention-span-statistics/
- WebFetch (error): https://dl.motamem.org/microsoft-attention-spans-research-report.pdf
- WebFetch: https://www.usecarly.com/blog/attention-span-statistics/
- WebFetch: https://www.whitehutchinson.com/printer-friendly/news/lenews/2017/august/article105.shtml
- WebFetch: https://www.scribd.com/document/265348695/Microsoft-Attention-Spans-Research-Report
- WebSearch: "attention span" goldfish "8 seconds" 2013 OR 2014 statisticbrain
- WebFetch: https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10061476
- WebFetch: https://patents.google.com/patent/US10061476B2/en
- WebFetch: https://idtips.substack.com/p/considering-attention-spans
- WebFetch (error): https://www.bbc.co.uk/news/health-38896790

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "The average human attention span is now shorter than a goldfish's."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** [Statistic Brain, *Attention Span Statistics*](https://www.statisticbrain.com/attention-span-statistics/), 2012 (date from: cited by [usecarly](https://www.usecarly.com/blog/attention-span-statistics/), which links a February 2012 Wayback Machine capture). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 5

### Chain
Your version: "Human attention span is now shorter than a goldfish's" (where you met it: not given)
 └─ [Time, Kevin McSpadden, *You Now Have a Shorter Attention Span Than a Goldfish*](https://time.com/3858309/attention-spans-goldfish/), 2015, Tertiary → cites
     └─ [Microsoft Canada Consumer Insights, *Attention spans*](https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf), Spring 2015, (not opened), per Time and usecarly. Four copies were tried: this PDF returned no text; [mangalam.nl](https://www.mangalam.nl/wp-content/uploads/2019/05/microsoft-attention-spans-research-report.pdf) returned 404; [motamem](https://dl.motamem.org/microsoft-attention-spans-research-report.pdf) had an expired certificate; [Scribd](https://www.scribd.com/document/265348695/Microsoft-Attention-Spans-Research-Report) was truncated before the chart. Per usecarly, the chart's source line credits Statistic Brain → cites
         └─ [Statistic Brain, *Attention Span Statistics*](https://www.statisticbrain.com/attention-span-statistics/), 2012, Unknown, (not opened, domain no longer resolves), per usecarly, root. Per usecarly, it named only the Associated Press as its source in 2012, and added the NCBI and the US National Library of Medicine by 2015 → stopped: not opened
 └─ (second branch) [White Hutchinson Leisure & Learning Group, *Leisure e-Newsletter*](https://www.whitehutchinson.com/printer-friendly/news/lenews/2017/august/article105.shtml), 2017, Tertiary → cites the Statistic Brain Research Institute, which is the root above

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Context removed | the average attention span in 2012 was 8 seconds, credited to the Associated Press (per usecarly) | Human attention span is now shorter than a goldfish's | [Time](https://time.com/3858309/attention-spans-goldfish/), 2015 |

### Status of the root
- No primary found, so there was no status to check.

### Cold trails
- Marketing Insider Group (Michael Brenner), *Thanks social media – our attention span is now shorter than a goldfish*, 2014 (not opened; date and title from the author's rewritten [2022 page](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/)). That page gives no source for the 2014 version, which it says used a 20-second figure for 2000. The 2022 rewrite now traces the claim to Statistic Brain and argues against it.

### Confidence
Medium: the Microsoft report and the Statistic Brain page could not be opened, so the key link and the 2012 date both rest on usecarly; the BBC's 2017 *More or Less* check (*Busting the attention span myth*, reported by usecarly as finding that neither the NCBI nor the AP had any record of research behind the figures) was also blocked from fetching.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
