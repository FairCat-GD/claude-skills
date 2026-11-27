---
case: echoed-statistic-goldfish-attention
run: 3
model: claude-opus-5-5
claude: 2.1.330
skill_version: 0.1.0
commit: 641ce2aa514b01cc42f1b4a263dc7cea66d57641
date: 2026-11-26T12:17:02Z
cost_usd: 1.1640
duration_s: 132
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
- WebSearch: humans attention span 8 seconds goldfish 9 seconds
- WebSearch: Microsoft Canada 2015 attention spans report goldfish
- WebSearch: "8.25 seconds" attention span Statistic Brain
- WebSearch: source of the goldfish attention span statistic origin
- WebSearch: goldfish attention span fact check BBC More or Less
- WebFetch: https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf
- WebFetch (error): https://www.bbc.com/news/health-38896790
- WebFetch: https://time.com/3858309/attention-spans-goldfish/
- WebFetch: https://medium.com/psynamic/8-second-attention-spans-tracking-the-myth-that-just-wont-quit-614dd2cb9792
- WebFetch (error): https://web.archive.org/cdx/search/cdx?url=statisticbrain.com/attention-span-statistics/&limit=3
- WebFetch: https://www.mangalam.nl/wp-content/uploads/2019/05/microsoft-attention-spans-research-report.pdf
- WebFetch: https://scienceblog.com/t-humans-eight-second-attention-span-goldfish-myth/
- WebFetch: https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/
- WebFetch: https://internet.psych.wisc.edu/wp-content/uploads/532-Master/532-UnitPages/Unit-09/Goldfish_MythBusting.pdf
- WebFetch (error): http://news.bbc.co.uk/2/hi/science/nature/1834682.stm
- WebFetch (error): https://dl.motamem.org/microsoft-attention-spans-research-report.pdf
- WebFetch (error): https://www.statisticbrain.com/attention-span-statistics/
- Read (denied): <temp>/config/projects/-private-tmp-e-FSUwfk-home-cwd/96bce03e-5060-4997-9fe0-a626df659de7/tool-results/webfetch-1795695448099-6va9o9.pdf
- WebFetch: http://advertising.microsoft.com/en/cl/31966/how-does-digital-affect-canadian-attention-spans
- WebFetch: https://www.whitehutchinson.com/news/lenews/2017/august/article105.shtml
- WebFetch: https://www.socialmediatoday.com/marketing/mobile-use-attention-spans-and-how-reach-next-generation-social-customers
- WebFetch: https://www.usecarly.com/blog/attention-span-statistics/
- WebFetch: https://about.ads.microsoft.com/en/cl/31966/how-does-digital-affect-canadian-attention-spans
- WebFetch (error): http://www.telegraph.co.uk/news/science/science-news/11607315/Humans-have-shorter-attention-span-than-goldfish-thanks-to-smartphones.html

## Reply

**Assumptions** (no reply is possible, so I asked nothing):
- The claim's text goes into web searches.
- No personal chain: traced from the web alone.

## Provenance: "Human attention span is now shorter than a goldfish's."

**Roots:** Echo · **Grounding:** No primary found · Mutated
**Earliest instance found:** Statistic Brain, *Attention Span Statistics* page, 2012 (date from: cited by [usecarly.com](https://www.usecarly.com/blog/attention-span-statistics/), which links an Internet Archive capture of the page dated 8 February 2012; not opened). Earlier instances may exist.
**Roots:** 1 · **Retellings found:** 7

### Chain
Your version: "Human attention span is now shorter than a goldfish's" (where you met it: not given)
 ├─ [Time, *You Now Have a Shorter Attention Span Than a Goldfish*](https://time.com/3858309/attention-spans-goldfish/), 2015 (date from: byline), Secondary: "people now generally lose concentration after eight seconds". Credits the 8 seconds to a Microsoft study and cites nothing for the goldfish's 9 seconds → cites
 │   └─ Microsoft Canada Consumer Insights, *Attention spans*, 2015, Secondary (not opened, per Time and [usecarly.com](https://www.usecarly.com/blog/attention-span-statistics/)). I tried [this PDF copy](https://static1.squarespace.com/static/59bf2bf68fd4d28e59627113/t/5ab01bdff950b70546a08167/1521490918597/265348695-Microsoft-Attention-Spans-Research-Report.pdf), but its text could not be extracted. According to usecarly.com, the page 6 chart gives 12 s (2000), 8 s (2013) and 9 s for a goldfish, with the line "Source: Statistic brain" → cites
 │       └─ Statistic Brain, *Attention Span Statistics*, 2012, Unknown (not opened, per [usecarly.com](https://www.usecarly.com/blog/attention-span-statistics/) and [A Patchwork of Perceptions](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/)). [The live site](https://www.statisticbrain.com/attention-span-statistics/) no longer resolves → cites
 │           └─ Associated Press; US National Library of Medicine / NCBI, date unknown (not opened, per [A Patchwork of Perceptions](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/), 2022). That page reports that BBC *More or Less* reporter Simon Maybin, in 2017, found no record of the research at either body → stopped: not opened
 ├─ [Social Media Today](https://www.socialmediatoday.com/marketing/mobile-use-attention-spans-and-how-reach-next-generation-social-customers), 2016 (date from: byline), Tertiary: "now at just 8.25 seconds". Also cites Time, a Telegraph article and a Facebook marketing blog post → cites
 │   └─ Statistic Brain (the node above)
 └─ [White Hutchinson, *Leisure eNewsletter*](https://www.whitehutchinson.com/news/lenews/2017/august/article105.shtml), 2017 (date from: byline), Tertiary: "Human average attention span in 2015 - 8.25 seconds" → cites
     └─ Statistic Brain (the node above)

### How it changed
| Change | Root says | Your version | First appears in |
| --- | --- | --- | --- |
| Date moved (other) | 8 seconds given as a 2012 figure, credited to AP and NCBI (per usecarly.com and A Patchwork of Perceptions; root not opened) | "is now shorter" | [Time](https://time.com/3858309/attention-spans-goldfish/), 2015 |
| Context removed | the figures are given with their claimed sources (Associated Press, NCBI) | no figures and no source | your version |

Among the retellings, two more drifts appear, though neither is in your version:
- **Number changed:** 8 seconds becomes 8.25 seconds, first in [Social Media Today](https://www.socialmediatoday.com/marketing/mobile-use-attention-spans-and-how-reach-next-generation-social-customers), 2016.
- **Attribution shifted:** Time credits the figure to a Microsoft study, while the report credits Statistic Brain, according to usecarly.com.

### Status of the root
- No primary found, so there was no status to check.
- BBC *More or Less* (Simon Maybin, BBC News, *Busting the attention span myth*, 10 March 2017; not opened, as bbc.com would not fetch) is reported by [usecarly.com](https://www.usecarly.com/blog/attention-span-statistics/) as saying the two named sources "can find any record of research that backs up the stats", in a quote that begins "neither".

### Cold trails
- BBC News, science/nature article 1834682, 2002 (date from: cited by [A Patchwork of Perceptions](https://apatchworkofperceptions.wordpress.com/2022/08/17/goldfish-and-us-unsubstantiated-claims-about-the-human-attention-span/); [tried, not opened](http://news.bbc.co.uk/2/hi/science/nature/1834682.stm)). According to that blog, it says web browsing can leave you with a nine-second attention span, *the same as* a goldfish rather than shorter, and it cites no source. The blog also mentions a September 2000 *Guardian* web-design article that Andrew Littlefield found, without saying whether that article contains the claim. These pages are not linked by citation to the Statistic Brain chain.

### Confidence
Medium: the 2015 Time retelling and the later retellings were opened, but the Microsoft report, the Statistic Brain page and its claimed sources could not be opened, so the links behind Time and the 2012 date rest on later pages that cite them.

_Tiers describe position in the chain, not reliability. "No primary found" means this search found none, not that the claim is false._
