---
case: non-interactive-goldfish-attention
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.2.0
commit: 429b407cbc2a21a290178238c14f00e933353335
date: 2026-11-27T15:42:06Z
cost_usd: 1.8491
duration_s: 220
turns: 40
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
- WebSearch: human attention span 8 seconds goldfish 9 seconds
- WebSearch: Microsoft Canada 2015 attention spans consumer insights report goldfish
- WebSearch: "8 seconds" attention span 2000 "12 seconds" Statistic Brain
- WebSearch: origin of goldfish attention span statistic source
- WebSearch: goldfish attention span myth fact check BBC
- WebFetch: https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf
- WebFetch (error): https://www.bbc.com/news/health-38896790
- WebFetch: https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/
- WebFetch (error): https://web.archive.org/cdx/search/cdx?url=statisticbrain.com/attention-span-statistics/&limit=3
- Read (denied): <temp>/config/projects/-private-tmp-e-o96UyN-home-cwd/dbcbd473-f359-4b32-9bb3-dc32633112c2/tool-results/webfetch-1795794153292-biz9ye.pdf
- WebFetch (error): http://news.bbc.co.uk/2/hi/science/nature/1834682.stm
- WebFetch: https://time.com/3858309/attention-spans-goldfish/
- WebFetch: https://www.mangalam.nl/wp-content/uploads/2019/05/microsoft-attention-spans-research-report.pdf
- WebFetch (error): https://www.bbc.co.uk/news/health-38896790
- WebFetch: https://medium.com/psynamic/8-second-attention-spans-tracking-the-myth-that-just-wont-quit-614dd2cb9792
- WebSearch: "attention span of nine seconds" goldfish 2002 web browsing
- WebSearch: statisticbrain attention span statistics "goldfish" archive 2012 "Associated Press"
- WebSearch: "Busting the attention span myth" Maybin
- WebFetch: https://www.ministryoftruth.me.uk/2014/09/03/do-goldfish-have-a-longer-attention-span-than-american-internet-users/
- WebFetch: https://internet.psych.wisc.edu/wp-content/uploads/532-Master/532-UnitPages/Unit-09/Goldfish_MythBusting.pdf
- WebFetch (error): https://ssh.theartof.com/articles/fascinate-the-goldfish/
- WebSearch: "Attention spans" Microsoft Canada consumer insights spring 2015 pdf
- WebFetch: https://pdfcoffee.com/microsoft-attention-spans-research-report-pdf-free.html
- WebFetch: https://storage.googleapis.com/public.papers.www.brainsights.com/Microsoft_Attention%20Spans.pdf
- WebFetch: https://www.swordandthescript.com/2022/02/goldfish-attention-span/
- WebFetch: https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/
- WebFetch: https://elearningindustry.com/8-second-attention-span-organizational-learning
- WebFetch (error): https://www.statisticbrain.com/attention-span-statistics/
- WebFetch: https://dl.acm.org/doi/10.1145/1326561.1326566
- WebFetch: https://api.crossref.org/works/10.1145/1326561.1326566
- WebSearch: "Turning into digital goldfish" BBC 2002

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Human attention span is now shorter than a goldfish's."

**Roots:** Echo · **Grounding:** Primary differs · Mutated
**Earliest instance found:** [BBC News, *Turning into digital goldfish*](http://news.bbc.co.uk/2/hi/science/nature/1834682.stm), 2002 (date from: cited by [A Patchwork of Perceptions](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/), 2022). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 7

### Chain
Your version: "Human attention span is now shorter than a goldfish's" (where you met it: not given)
 ├─ [TIME, *You Now Have a Shorter Attention Span Than a Goldfish*](https://time.com/3858309/attention-spans-goldfish/), 2015, Tertiary → cites
 │   └─ [Microsoft Canada Consumer Insights, *Attention spans*](https://pdfcoffee.com/microsoft-attention-spans-research-report-pdf-free.html), 2015, Tertiary for this figure (the page with the figure was not readable in any of the 4 copies tried; its source line is reported by [Sword and the Script](https://www.swordandthescript.com/2022/02/goldfish-attention-span/), 2022) → cites
 │       └─ [Statistic Brain, *Attention span statistics*](https://www.statisticbrain.com/attention-span-statistics/), date unknown, (not opened), per [eLearning Industry](https://elearningindustry.com/8-second-attention-span-organizational-learning) → cites
 │           ├─ The Associated Press; National Center for Biotechnology Information / US National Library of Medicine, date unknown, (not opened), per eLearning Industry → stopped: not opened
 │           └─ → credits Weinreich, Obendorf, Herder & Mayer
 │               └─ [Weinreich et al., *Not quite the average: An empirical study of Web use*, ACM Transactions on the Web](https://api.crossref.org/works/10.1145/1326561.1326566), 2008, Primary (credited, differs)
 ├─ [Marketing Insider Group, Michael Brenner](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/), 2014, Tertiary → cites Statistic Brain (above)
 ├─ Zocalo Group marketing brochure, date unknown, (not opened), per [Ministry of Truth](https://www.ministryoftruth.me.uk/2014/09/03/do-goldfish-have-a-longer-attention-span-than-american-internet-users/), 2014 → cites
 │   └─ The Associated Press, 30 January 2012, (not opened), per Ministry of Truth → stopped: not opened
 └─ [BBC News, *Turning into digital goldfish*](http://news.bbc.co.uk/2/hi/science/nature/1834682.stm), 2002, (not opened), per A Patchwork of Perceptions, root (no source for the nine-second figure is named on any opened page; no opened retelling links it to the 2015 wave)

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Number changed | attention span of nine seconds, the *same* as a goldfish | Human attention span is now shorter than a goldfish's | [Statistic Brain](https://www.statisticbrain.com/attention-span-statistics/), date unknown |
| Hedge dropped | web browsing *can* leave you with a nine-second attention span | Human attention span is now shorter than a goldfish's | [Marketing Insider Group](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/), 2014 |
| Scope widened | applies to the habit of heavy web browsing | Human attention span is now shorter than a goldfish's | [Marketing Insider Group](https://marketinginsidergroup.com/content-marketing/thanks-social-media-average-attention-span-now-shorter-goldfish/), 2014 |

### Status of the root
- No primary found, so there was no status to check.
- Weinreich et al. (2008): the Crossref record lists no retraction, correction or other update. Its abstract describes a long-term study of how 25 participants browsed the web and mentions no attention span in seconds and no goldfish. [eLearning Industry](https://elearningindustry.com/8-second-attention-span-organizational-learning) (Patti Shank, 2017) reports that the study "does not cite the listed statistics."
- Microsoft Canada report: TIME credits the eight-second figure to Microsoft's own study, which surveyed 2,000 Canadians and recorded EEGs from 112 people. TIME puts it this way: "people now generally lose concentration after eight seconds". Sword and the Script reports that the figure carries the report's citation to Statistic Brain, not to that research. The report's foreword concludes: "digital won't be the cause of our (at least attentional) downfall." ([copy](https://pdfcoffee.com/microsoft-attention-spans-research-report-pdf-free.html))
- Statistic Brain's listed sources: Sword and the Script reports that BBC World Service's *More or Less* (Simon Maybin, *Busting the attention span myth*, 2017) contacted the NCBI and the Associated Press, and neither found any record of research behind the figures. The BBC page itself would not open. Marketing Insider Group says the Statistic Brain page no longer exists, and the statisticbrain.com domain did not resolve when fetched.
- Ministry of Truth (2014) argues that the 8- and 12-second figures look like measures of time spent on a web page, not of attention. It also says no one has measured a goldfish's attention span, and that the older goldfish claim was about a three-second *memory*.

### Cold trails
None.

### Confidence
Medium: the root and Statistic Brain could not be opened (the BBC and the Wayback Machine refused fetches, and Statistic Brain's domain is gone), so key links rest on what opened pages report about them.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
