---
case: non-interactive-goldfish-attention
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.3.0
commit: 5d9abd7e7e30527131c5babd47898bd9930d1f4f
date: 2026-11-28T00:28:23Z
cost_usd: 1.4655
duration_s: 155
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
- WebSearch: humans 8 seconds attention span goldfish 9 seconds Microsoft study
- WebSearch: "8 seconds" attention span Statistic Brain source
- WebSearch: origin of goldfish attention span statistic
- WebSearch: goldfish attention span myth fact check BBC
- WebSearch: Microsoft Canada "Attention Spans" consumer insights 2015 report pdf
- WebFetch: https://storage.googleapis.com/public.papers.www.brainsights.com/Microsoft_Attention%20Spans.pdf
- WebFetch (error): https://www.bbc.co.uk/news/health-38896790
- WebFetch: https://time.com/3858309/attention-spans-goldfish/
- WebFetch: https://medium.com/psynamic/8-second-attention-spans-tracking-the-myth-that-just-wont-quit-614dd2cb9792
- Read (denied): <temp>/config/projects/-private-tmp-e-XRyWTQ-home-cwd/0432273f-5107-4fa5-a31c-531a291faa00/tool-results/webfetch-1795825726401-hipnfm.pdf
- WebFetch (error): https://www.bbc.com/news/health-38896790
- WebFetch (error): https://web.archive.org/cdx/search/cdx?url=statisticbrain.com/attention-span-statistics/&limit=3
- WebFetch: https://pdfcoffee.com/microsoft-attention-spans-research-report-pdf-free.html
- WebFetch: https://scienceblog.com/t-humans-eight-second-attention-span-goldfish-myth/
- WebFetch: https://www.swordandthescript.com/2022/02/goldfish-attention-span/
- WebFetch: https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf
- WebFetch (error): https://www.statisticbrain.com/attention-span-statistics/
- WebSearch: Policy Options Gausby Microsoft attention span goldfish misinterpreted
- WebSearch: Statistic Brain "attention span" goldfish 2012 2013 archived "Associated Press"
- WebFetch: https://internet.psych.wisc.edu/wp-content/uploads/532-Master/532-UnitPages/Unit-09/Gausby_MicrosoftReport_2015_Excerpt.pdf
- WebFetch: https://www.ceros.com/originals/no-dont-attention-span-goldfish/
- WebFetch: https://internet.psych.wisc.edu/wp-content/uploads/532-Master/532-UnitPages/Unit-09/Goldfish_MythBusting.pdf
- WebFetch: https://www.usecarly.com/blog/attention-span-statistics/
- WebFetch: https://policyviz.com/2016/01/29/the-attention-span-statistic-fallacy/
- WebFetch: https://www.linkedin.com/business/marketing/blog/content-marketing/the-great-goldfish-attention-span-myth-and-why-its-killing-cont
- WebFetch: https://ccit.college.columbia.edu/sites/ccit/files/weinreich-web-use-study.pdf
- WebFetch (error): https://archive.ph/newest/http://www.statisticbrain.com/attention-span-statistics/

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Human attention span is now shorter than a goldfish's."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** [Statistic Brain, *Attention Span Statistics*](https://www.statisticbrain.com/attention-span-statistics/), 2012 (date from: cited by [usecarly](https://www.usecarly.com/blog/attention-span-statistics/), which gives a Wayback capture of February 2012). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 6

### Chain
Your version: "Human attention span is now shorter than a goldfish's" (where you met it: not given)
 └─ [Kevin McSpadden, *You Now Have a Shorter Attention Span Than a Goldfish*, Time](https://time.com/3858309/attention-spans-goldfish/), 2015, Tertiary → cites
     └─ [Microsoft Canada Consumer Insights (Alyson Gausby), *Attention spans*](https://storage.googleapis.com/public.papers.www.brainsights.com/Microsoft_Attention%20Spans.pdf), Spring 2015, (not opened), per [Sword and the Script](https://www.swordandthescript.com/2022/02/goldfish-attention-span/) → cites
         └─ [Statistic Brain, *Attention Span Statistics*](https://www.statisticbrain.com/attention-span-statistics/), 2012, (not opened), per [usecarly](https://www.usecarly.com/blog/attention-span-statistics/), root → cites
             ├─ The Associated Press, date unknown, (not opened), per [usecarly](https://www.usecarly.com/blog/attention-span-statistics/) → stopped: not opened
             ├─ National Center for Biotechnology Information, U.S. National Library of Medicine, date unknown, (not opened), per [PolicyViz](https://policyviz.com/2016/01/29/the-attention-span-statistic-fallacy/) → stopped: not opened
             └─ [Weinreich et al., web-use study](https://ccit.college.columbia.edu/sites/ccit/files/weinreich-web-use-study.pdf), 2008, (not opened), per [PolicyViz](https://policyviz.com/2016/01/29/the-attention-span-statistic-fallacy/) → stopped: not opened

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Context removed | per [usecarly](https://www.usecarly.com/blog/attention-span-statistics/), the 2012 capture gave 8 seconds as the average attention span *in 2012*. A March 2015 capture relabelled the same figure *2013*. | Human attention span is now shorter than a goldfish's | [Time](https://time.com/3858309/attention-spans-goldfish/), 2015 |
| Other: a dated figure turned into a comparison with a goldfish | per [usecarly](https://www.usecarly.com/blog/attention-span-statistics/), a bare figure for one year, citing only the Associated Press | Human attention span is now shorter than a goldfish's | [Time](https://time.com/3858309/attention-spans-goldfish/), 2015 |

### Status of the root
- No primary found, so there was no status to check.
- Time: the article cites a Microsoft study for the human figure, saying "people now generally lose concentration after eight seconds"; it gives no source for the goldfish's nine seconds ([Time](https://time.com/3858309/attention-spans-goldfish/), 2015).
- Microsoft Canada report: Frank Strong writes that the eight-second figure appears in the report, credited to Statistic Brain, but "did not actually come from Microsoft's research" ([Sword and the Script](https://www.swordandthescript.com/2022/02/goldfish-attention-span/), 2022).
- Microsoft Canada report: Jason Miller writes that "the Microsoft research never once mentions the magic eight-second number at all" ([LinkedIn](https://www.linkedin.com/business/marketing/blog/content-marketing/the-great-goldfish-attention-span-myth-and-why-its-killing-cont), 2016).
- Statistic Brain's sources: Jon Schwabish reports that the Weinreich 2008 paper studied web browsing in 25 participants and did not test attention spans, that the National Library of Medicine told him it could not verify the figure, and that Statistic Brain did not respond. He concludes "that number is made up" ([PolicyViz](https://policyviz.com/2016/01/29/the-attention-span-statistic-fallacy/), 2016).
- Statistic Brain's sources: the BBC's *More or Less* (Simon Maybin, 2017) contacted the listed sources, and per usecarly, "neither can find any record of research that backs up the stats" ([usecarly](https://www.usecarly.com/blog/attention-span-statistics/), 2026). The BBC article itself (bbc.com/news/health-38896790) could not be fetched.

### Cold trails
None.

### Confidence
Low: the BBC article, the Wayback Machine and the Statistic Brain site could not be fetched, and every copy of the Microsoft report came back as unreadable PDF data, so the chain past Time rests on later pages that describe those sources.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
