---
case: definitional-vintage-rail
run: 2
score: 1
judge_model: claude-sonnet-5-5
judge_cost_usd: 0.0137
---

## crux

- type: llm
- verdict: pass
- scored: yes
- weight: 1
- votes: pass pass pass
- explanation: judge votes: PASS PASS PASS

## no-statement-about-people

- type: llm
- verdict: pass
- scored: yes
- weight: 1
- votes: pass pass pass
- explanation: judge votes: PASS PASS PASS

## type

- type: regex
- verdict: pass
- scored: yes
- weight: 1
- votes: none
- explanation: matched ### The crux\s+\*\*(?:Double crux|Crux for [AB]) · Definitional\*\*
