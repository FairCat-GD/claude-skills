---
case: non-interactive-goldfish-attention
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T15:42:18Z
cost_usd: 1.2231
duration_s: 147
turns: 36
error: none
---

## Tool calls

- Skill: provenance-tracer:provenance-tracer
- Glob: {"pattern":"references/*.md","path":"<plugin>/skills/provenance-tracer"}
- Read: <plugin>/skills/provenance-tracer/references/output-template.md
- Read: <plugin>/skills/provenance-tracer/references/search-playbook.md
- Read: <plugin>/skills/provenance-tracer/references/labels.md
- Read: <plugin>/skills/provenance-tracer/references/mutation-types.md
- ToolSearch: {"query":"select:WebSearch,WebFetch","max_results":2}
- WebSearch: "attention span" "shorter than a goldfish"
- WebSearch: humans 8 second attention span goldfish 9 seconds
- WebSearch: Microsoft Canada attention spans report 2015 goldfish
- WebSearch: "8.25 seconds" attention span Statistic Brain source
- WebSearch: origin of goldfish attention span statistic myth source
- WebSearch: goldfish attention span fact check BBC More or Less
- WebFetch (error): https://www.bbc.com/news/health-38896790
- WebFetch: https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf
- WebFetch (error): https://web.archive.org/cdx/search/cdx?url=statisticbrain.com/attention-span-statistics/&limit=5
- WebFetch: https://time.com/3858309/attention-spans-goldfish/
- Read (denied): <temp>/config/projects/-private-tmp-e-Hlckhf-home-cwd/b56c7fd6-ef82-49f0-b6e8-8e84638d17f9/tool-results/webfetch-1795794167176-41iozj.pdf
- WebFetch (error): https://www.bbc.co.uk/news/health-38896790
- WebFetch: https://www.mangalam.nl/wp-content/uploads/2019/05/microsoft-attention-spans-research-report.pdf
- WebFetch: https://medium.com/psynamic/8-second-attention-spans-tracking-the-myth-that-just-wont-quit-614dd2cb9792
- WebFetch: https://scienceblog.com/t-humans-eight-second-attention-span-goldfish-myth/
- WebFetch: https://uxpsychology.substack.com/p/the-attention-span-myth
- WebFetch: https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/
- WebFetch (error): https://dl.motamem.org/microsoft-attention-spans-research-report.pdf
- WebFetch (error): https://www.statisticbrain.com/attention-span-statistics/
- WebFetch: https://www.prc.za.com/2016/11/18/attention-spans-report-microsoft-2015/
- WebFetch: https://dam-it.io/guides/goldfish-attention-span-myth-8-seconds
- WebFetch: https://prc.za.com/wp-content/uploads/2016/11/2015-Attention-Spans-Report-Microsoft.pdf
- WebFetch: https://en.wikipedia.org/wiki/Attention_span
- WebFetch: https://archive.org/wayback/available?url=statisticbrain.com/attention-span-statistics/&timestamp=20100101
- WebFetch: https://www.whitehutchinson.com/news/lenews/2017/august/article105.shtml
- WebFetch: https://www.scribd.com/document/265348695/Microsoft-Attention-Spans-Research-Report
- WebFetch: https://www.warc.com/newsandopinion/opinion/why-the-goldfish-myth-wont-die/3226

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Human attention span is now shorter than a goldfish's."

**Roots:** Echo · **Grounding:** No primary found
**Earliest instance found:** [Statistic Brain, *Attention Span Statistics*](https://www.statisticbrain.com/attention-span-statistics/), 2012 (date from: archive; the [Wayback availability record](https://archive.org/wayback/available?url=statisticbrain.com/attention-span-statistics/&timestamp=20100101) shows a capture of this URL dated 8 February 2012, but I could not open the capture itself). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 5

### Chain
Your version: "Human attention span is now shorter than a goldfish's" (where you met it: not given)
 └─ [Kevin McSpadden, *You Now Have a Shorter Attention Span Than a Goldfish*, Time](https://time.com/3858309/attention-spans-goldfish/), 2015, Secondary → cites
     └─ [Microsoft Canada Consumer Insights, *Attention spans*, Spring 2015](https://www.scribd.com/document/265348695/Microsoft-Attention-Spans-Research-Report), 2015, Secondary (not opened, per [Maria Panagiotidi, *The attention span myth*](https://uxpsychology.substack.com/p/the-attention-span-myth); the copies I fetched returned either no readable text or a text without the goldfish passage) → cites
         └─ [Statistic Brain, *Attention Span Statistics*](https://www.statisticbrain.com/attention-span-statistics/), 2012, Unknown (not opened, per [Dam It!](https://dam-it.io/guides/goldfish-attention-span-myth-8-seconds); the domain no longer resolves), root → cites
             └─ National Center for Biotechnology Information and Associated Press, date unknown, (not opened), per [Dam It!](https://dam-it.io/guides/goldfish-attention-span-myth-8-seconds) → stopped: not opened
 └─ [White Hutchinson Leisure & Learning Group, *You've only got 3 seconds to get their attention*](https://www.whitehutchinson.com/news/lenews/2017/august/article105.shtml), 2017, Tertiary → cites Statistic Brain (above): it lists the human span as 8.25 seconds in 2015 and a goldfish's as 9 seconds
 └─ [Michael Brenner, Marketing Insider Group](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/), 2022 (byline; the author says it first ran in 2014), Tertiary → cites Statistic Brain (above), via the Microsoft report

### How it changed
None found. I could not open the root, so I could not compare its wording with your version.

### Status of the root
- No primary found, so there was no status to check.
- Statistic Brain's credited sources: according to [Dam It!](https://dam-it.io/guides/goldfish-attention-span-myth-8-seconds), NCBI and the Associated Press "could find no record of research backing the numbers." Dam It! credits this finding to Simon Maybin's BBC investigation, [*Busting the attention span myth*](https://www.bbc.com/news/health-38896790), March 2017 (not opened: the fetch was refused).
- The Microsoft report's own data: according to [Panagiotidi](https://uxpsychology.substack.com/p/the-attention-span-myth), the report's figure came from a Statistic Brain graph and not from its own survey and EEG work. Panagiotidi calls that graph's information "entirely fabricated." Time describes the report's own research as a survey of 2,000 Canadians plus EEG recordings of 112 people.

### Cold trails
None.

### Confidence
Low: the chain stops at two pages I could not open, the Statistic Brain page and the sources it credited, so no node reaches the data behind the 8-second and 9-second figures.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
