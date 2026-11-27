---
case: echoed-statistic-goldfish-attention
run: 2
score: 0.75
judge_model: claude-sonnet-5-5
judge_cost_usd: 0.0493
---

## facts

- type: llm
- verdict: fail
- scored: yes
- weight: 1
- votes: fail fail fail
- explanation: judge votes: FAIL FAIL FAIL

## footer

- type: regex
- verdict: pass
- scored: yes
- weight: 1
- votes: none
- explanation: matched Earlier instances may exist\.[\s\S]*[_*]Tiers describe position in the chain, not reliability\. ["“]No primary found["”] means this search found none, not that the claim is false\.[_*]

## labels

- type: regex
- verdict: pass
- scored: yes
- weight: 1
- votes: none
- explanation: matched \*\*Roots:\*\* Echo · \*\*Grounding:\*\* No primary found(?: · Mutated)?(?: · Misattributed)?(?: · Origin retracted)?(?: · Origin corrected)?(?: · Origin failed replication)?[ \t]*(?:\r?\n|$)

## no-verdict

- type: llm
- verdict: pass
- scored: yes
- weight: 1
- votes: pass pass pass
- explanation: judge votes: PASS PASS PASS
