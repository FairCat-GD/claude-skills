---
case: echoed-statistic-goldfish-attention
run: 2
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-26T12:17:02Z
cost_usd: 1.4080
duration_s: 172
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
- WebSearch: humans have 8 second attention span goldfish 9 seconds
- WebSearch: Microsoft Canada 2015 attention spans consumer insights report goldfish
- WebSearch: "8 seconds" attention span Statistic Brain source
- WebSearch: origin of goldfish attention span statistic 8 seconds
- WebSearch: goldfish attention span claim fact check BBC
- WebFetch: https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf
- WebFetch (error): https://www.bbc.com/news/health-38896790
- WebFetch (error): https://web.archive.org/cdx/search/cdx?url=statisticbrain.com/attention-span-statistics/&limit=5
- WebFetch: https://time.com/3858309/attention-spans-goldfish/
- Read (denied): <temp>/config/projects/-private-tmp-e-sqzECH-home-cwd/1a7c65de-b781-46a7-a640-0e5a7e48d13b/tool-results/webfetch-1795695448099-m3jb6d.pdf
- WebFetch: https://medium.com/psynamic/8-second-attention-spans-tracking-the-myth-that-just-wont-quit-614dd2cb9792
- WebFetch: https://www.mangalam.nl/wp-content/uploads/2019/05/microsoft-attention-spans-research-report.pdf
- WebFetch (error): https://www.bbc.co.uk/news/health-38896790
- WebFetch: https://scienceblog.com/t-humans-eight-second-attention-span-goldfish-myth/
- WebFetch: https://dam-it.io/guides/goldfish-attention-span-myth-8-seconds
- WebFetch: https://www.swordandthescript.com/2022/02/goldfish-attention-span/
- WebFetch: http://advertising.microsoft.com/en/cl/31966/how-does-digital-affect-canadian-attention-spans
- WebFetch: https://www.marketplace.org/2014/02/11/business/goldfish-have-longer-attention-spans-americans-and-publishing-industry-knows-it
- WebFetch: https://www.scribd.com/document/736691392/Microsoft-Attention-Spans-Research-Report
- WebFetch: https://www.linkedin.com/business/marketing/blog/content-marketing/the-great-goldfish-attention-span-myth-and-why-its-killing-cont
- WebFetch (error): https://www.statisticbrain.com/attention-span-statistics/
- WebSearch: policyviz Schwabish goldfish attention span Statistic Brain
- WebSearch: Marketplace 2014 "goldfish have longer attention spans than Americans"
- WebFetch: https://www.marketplace.org/story/2014/02/11/goldfish-have-longer-attention-spans-americans-and-publishing-industry-knows-it
- WebFetch: https://policyviz.com/2016/01/29/the-attention-span-statistic-fallacy/
- WebFetch: https://www.firstcoastnews.com/article/news/verify/verify-do-you-have-the-attention-span-of-a-goldfish-animal/77-db9ed259-f0b6-4663-b8fe-b68f5bc79a16
- WebFetch: https://about.ads.microsoft.com/en/cl/31966/how-does-digital-affect-canadian-attention-spans
- WebFetch: https://internet.psych.wisc.edu/wp-content/uploads/532-Master/532-UnitPages/Unit-09/Attention_Goldfish_Abbreviated.pdf
- WebFetch: https://www.foxnews.com/tech/our-attention-span-is-now-worse-than-a-goldfishs.print

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Human attention span is now shorter than a goldfish's"

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** [Marketplace, *Goldfish have longer attention spans than Americans, and the publishing industry knows it*](https://www.marketplace.org/story/2014/02/11/goldfish-have-longer-attention-spans-americans-and-publishing-industry-knows-it), 2014 (date from: cited by [Sword and the Script](https://www.swordandthescript.com/2022/02/goldfish-attention-span/), whose link to it has the path 2014/02/11). I couldn't open it because the fetch came back empty. Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 6

### Chain
Your version: "Human attention span is now shorter than a goldfish's" (where you met it: not given)
 ├─ [Time, *You Now Have a Shorter Attention Span Than a Goldfish*](https://time.com/3858309/attention-spans-goldfish/), 2015, Secondary: "[people now generally lose concentration after eight seconds](https://time.com/3858309/attention-spans-goldfish/)". It cites no source for the goldfish figure. → cites
 │   └─ [Microsoft Canada, *Attention Spans*](https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf), 2015, Primary (not opened, per Time). The PDF returned no readable text, and two other copies failed. → cites
 │       └─ [Statistic Brain, *Attention Span Statistics*](https://www.statisticbrain.com/attention-span-statistics/), date unknown, (not opened), per [PolicyViz](https://policyviz.com/2016/01/29/the-attention-span-statistic-fallacy/) and [LinkedIn](https://www.linkedin.com/business/marketing/blog/content-marketing/the-great-goldfish-attention-span-myth-and-why-its-killing-cont). The site no longer resolves. → cites
 │           └─ NCBI / U.S. National Library of Medicine; The Associated Press; Weinreich et al., 2008, (not opened), per [PolicyViz](https://policyviz.com/2016/01/29/the-attention-span-statistic-fallacy/) → stopped: not opened
 └─ [Fox News (republished from Newser), *Our attention span is now worse than a goldfish's*](https://www.foxnews.com/tech/our-attention-span-is-now-worse-than-a-goldfishs.print), 2015, Tertiary: "[the jittery low of eight seconds today](https://www.foxnews.com/tech/our-attention-span-is-now-worse-than-a-goldfishs.print)". It credits the goldfish figure only to unnamed "researchers". → cites
     └─ Yahoo! Canada report of the Microsoft study, date unknown, (not opened), per Fox News → cites
         └─ Microsoft Canada, *Attention Spans*, 2015, Primary (not opened, per Fox News). This is the same node as above.

The earliest instance has no chain linking it to the nodes above:
 └─ [Marketplace](https://www.marketplace.org/story/2014/02/11/goldfish-have-longer-attention-spans-americans-and-publishing-industry-knows-it), 2014, Unknown, (not opened), per Sword and the Script → stopped: not opened

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Scope widened | Americans (Marketplace's title, as linked); Canadians in the Microsoft study, per Fox News: "the Canadian attention span" | Human attention span | [Time](https://time.com/3858309/attention-spans-goldfish/), 2015 ("people") |
| Attribution shifted (in the chain; your version credits no one) | the figure appears in a page-6 graphic that cites Statistic Brain, not the study's own results, per PolicyViz | (Time credits "a new study from Microsoft") | [Time](https://time.com/3858309/attention-spans-goldfish/), 2015 |

### Status of the root
- No primary found, so there was no status to check.
- Microsoft Canada report: [PolicyViz](https://policyviz.com/2016/01/29/the-attention-span-statistic-fallacy/) (Jon Schwabish, 2016) says the figure is in a page-6 graphic that references Statistic Brain, and that "[attention span length was not even tested as part of the study](https://policyviz.com/2016/01/29/the-attention-span-statistic-fallacy/)".
- Microsoft Canada report: [LinkedIn](https://www.linkedin.com/business/marketing/blog/content-marketing/the-great-goldfish-attention-span-myth-and-why-its-killing-cont) (Jason Miller, 2016) writes that "[the Microsoft research never once mentions the magic eight-second number at all](https://www.linkedin.com/business/marketing/blog/content-marketing/the-great-goldfish-attention-span-myth-and-why-its-killing-cont)".
- Statistic Brain: [PolicyViz](https://policyviz.com/2016/01/29/the-attention-span-statistic-fallacy/) reports what the page cited:
  - a 2008 web-usage study by Weinreich et al., which PolicyViz says did not test attention spans;
  - NCBI/NLM and the AP. When PolicyViz emailed the NLM, the reply said it could not verify the figure.
- BBC (Simon Maybin, *Busting the attention span myth*, 2017): the BBC page wouldn't open. [Sword and the Script](https://www.swordandthescript.com/2022/02/goldfish-attention-span/) and [Dam It!](https://dam-it.io/guides/goldfish-attention-span-myth-8-seconds) both report the BBC's findings:
  - Neither NCBI nor the AP could find research behind the figures.
  - A fish-behaviour expert said there is no evidence that goldfish have particularly short attention spans.

### Cold trails
None.

### Confidence
Low: the chain stops at pages that wouldn't open (the Microsoft report, Statistic Brain, the 2014 Marketplace piece, the BBC) before reaching anything that cites nothing.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
