---
title: "Red-TTT: test-time training for automated jailbreaking"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.05282, k399]
related:
  - concepts/test-time-training-redteam-attacker.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/piminer-agentic-prompt-injection-redteam.md
maturity: draft
read_status: read
created: 2026-10-06
updated: 2026-10-06
phase_0_verdict: "REFERENCE 2026-10-06 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K399)"
---

## Relations

## Relations

- @concepts/test-time-training-redteam-attacker.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/crescendo-multi-turn-jailbreak.md
- @concepts/piminer-agentic-prompt-injection-redteam.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Red-TTT: test-time training for automated jailbreaking |
| arXiv | 2610.05282 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.05282-red-ttt-test-time-training-for-automated-jailbre.pdf |
| Retrieved | 2026-10-06 |
| Read status | read (deep-read) |

## Narrative

**K399** — automated red-teaming either draws more samples at test time (search, rewriting, tree expansion) or trains a stronger attacker offline with RL. Both share one limit: **once an attack on a specific behaviour begins, the attacker's weights are frozen**, so anything learned about that behaviour stays in context instead of the model. Red-TTT updates the **attacker at test time** on the behaviour in front of it, and adapts the training objective to red-teaming — where success is judged by the **single best sample, not the average**. It needs only sampling access to the victim and drops into existing pipelines unchanged. HarmBench, four victim models: ASR **72.4%** vs **55.9%** for a budget-matched Best-of-N at 120 samples, improving in **every** configuration and gaining **+9.0 to +23.0** over frozen controls; on HarmBench standard-200 against Llama-3-8B it reaches **77.0%** against CodeChameleon **44.5%**, X-Teaming **21.5%**, AutoDAN-Turbo **27.0%**. Repo `github.com/SaFo-Lab/Red-TTT`. Operator steal: a **fixed-policy** attacker is a ceiling, and the right objective for red-teaming is best-of-N, not mean quality. Lab only; owned or procured models. **No jailbreak prompts or attack code in wiki.**

## Snippets

> See arXiv 2610.05282 abstract. [Source: arXiv 2610.05282 (retrieved 2026-10-06)]
