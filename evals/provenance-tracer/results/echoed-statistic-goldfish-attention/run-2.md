---
case: echoed-statistic-goldfish-attention
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:25:29Z
cost_usd: 1.4401
duration_s: 154
turns: 34
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
- WebSearch: humans have 8 second attention span goldfish 9 seconds
- WebSearch: Microsoft Canada 2015 attention spans consumer insights report goldfish
- WebSearch: "8 seconds" attention span Statistic Brain National Center for Biotechnology Information
- WebSearch: origin of goldfish attention span statistic source
- WebSearch: goldfish attention span myth fact check BBC
- WebFetch: https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf
- WebFetch (error): https://www.bbc.com/news/health-38896790
- WebFetch: https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/
- WebFetch: https://medium.com/psynamic/8-second-attention-spans-tracking-the-myth-that-just-wont-quit-614dd2cb9792
- Read (denied): <temp>/config/projects/-private-tmp-e-kud5Be-home-cwd/1d8dbc74-a87f-41aa-a8fe-765e77f5a963/tool-results/webfetch-1795825553341-f04506.pdf
- WebFetch (error): http://news.bbc.co.uk/2/hi/science/nature/1834682.stm
- WebSearch: "Busting the attention span myth" BBC Maybin
- WebFetch: https://www.mangalam.nl/wp-content/uploads/2019/05/microsoft-attention-spans-research-report.pdf
- WebFetch (error): https://web.archive.org/web/2017/https://www.bbc.com/news/health-38896790
- WebFetch (error): https://web.archive.org/web/2002/http://news.bbc.co.uk/2/hi/science/nature/1834682.stm
- WebFetch (error): https://web.archive.org/web/2015/http://www.statisticbrain.com/attention-span-statistics/
- WebSearch: "Microsoft attention spans" "Spring 2015" pdf Gausby
- WebFetch: https://time.com/3858309/attention-spans-goldfish/
- WebFetch: https://www.swordandthescript.com/2022/02/goldfish-attention-span/
- WebFetch: https://storage.googleapis.com/public.papers.www.brainsights.com/Microsoft_Attention%20Spans.pdf
- WebFetch: https://internet.psych.wisc.edu/wp-content/uploads/532-Master/532-UnitPages/Unit-09/Gausby_MicrosoftReport_2015_Excerpt.pdf
- WebFetch: https://exnihilomagazine.com/the-great-attention-spans-hoax-why-8-seconds-never-mattered/
- WebFetch: https://scienceblog.com/t-humans-eight-second-attention-span-goldfish-myth/
- WebFetch: https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/
- WebFetch: https://www.usecarly.com/blog/attention-span-statistics/

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Human attention span is now shorter than a goldfish's"

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** [BBC News article](http://news.bbc.co.uk/2/hi/science/nature/1834682.stm), 2002 (date from: cited by [A Patchwork of Perceptions](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/), which gives February 2002). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 6

### Chain
Your version: "Human attention span is now shorter than a goldfish's" (where you met it: not given)
 ├─ [Time, *You Now Have a Shorter Attention Span Than a Goldfish*](https://time.com/3858309/attention-spans-goldfish/), 2015, Tertiary → cites
 │   └─ [Microsoft Canada, *Attention spans* (Gausby)](https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf), 2015, (not opened), per [Sword and the Script](https://www.swordandthescript.com/2022/02/goldfish-attention-span/); Tertiary. Four copies returned no readable text. → cites
 │       └─ [Statistic Brain, attention span statistics page](https://web.archive.org/web/2015/http://www.statisticbrain.com/attention-span-statistics/), 2012–2015, (not opened), per [Sword and the Script](https://www.swordandthescript.com/2022/02/goldfish-attention-span/); Unknown. It names NCBI/US National Library of Medicine and the Associated Press as sources, per [Ex Nihilo Magazine](https://exnihilomagazine.com/the-great-attention-spans-hoax-why-8-seconds-never-mattered/). → stopped: not opened
 ├─ [Marketing Insider Group (Michael Brenner)](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/), 2014, Tertiary. The page is dated 2022 and says it was first published in 2014. → cites Statistic Brain (the node above)
 └─ [A Patchwork of Perceptions (Abigail Rose Drumm)](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/), 2022, Tertiary → cites
     └─ [BBC News article](http://news.bbc.co.uk/2/hi/science/nature/1834682.stm), 2002, (not opened), per A Patchwork of Perceptions; Unknown, root

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Number changed | "attention span of nine seconds – the same as a goldfish" ([source](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/)) | shorter than a goldfish's | [Marketing Insider Group](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/), 2014 |
| Context removed | the figure is tied to the addictive nature of web browsing | Human attention span is now shorter | [Time](https://time.com/3858309/attention-spans-goldfish/), 2015 |

### Status of the root
- No primary found, so there was no status to check.
- Microsoft Canada report: per [Sword and the Script](https://www.swordandthescript.com/2022/02/goldfish-attention-span/), the report's 8-second figure came from Statistic Brain, not from its own survey of 2,000 Canadians or its brain-activity tests on 112 people.
- Statistic Brain's listed sources: per [Ex Nihilo Magazine](https://exnihilomagazine.com/the-great-attention-spans-hoax-why-8-seconds-never-mattered/), the BBC's 2017 investigation found "neither organisation could find any record of research backing up the statistics."
- BBC News, *Busting the attention span myth* (Simon Maybin, 2017): this investigation of the claim could not be opened (the fetch tool could not reach bbc.com or the Wayback Machine). What it found is reported here only through the retellings above.
- Marketing Insider Group: the 2014 article that stated the claim now carries a correction saying the goldfish comparison has since been shown to be untrue ([source](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/)).

### Cold trails
None.

### Confidence
Low: no Primary was opened, the 2002 root and the Microsoft report could not be read, and the Statistic Brain branch stops at a page that could not be opened, short of any source that cites nothing.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
