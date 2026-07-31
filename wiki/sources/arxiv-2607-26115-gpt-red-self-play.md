---
title: GPT-Red automated red teaming via self-play (arXiv 2607.26115)
type: source
tags: [source, arxiv, red-teaming, prompt-injection, openai]
keywords: [2607.26115, GPT-Red, self-play, GPT-5.6, prompt injection]
related:
  - concepts/gpt-red-self-play-red-teaming.md
  - concepts/pair-prompt-pattern.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-30
updated: 2026-07-31
phase_0_verdict: "REFERENCE 2026-07-30 — OpenAI paper; no public GPT-Red weights/code (inspect_ai cited only)"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

**Briefs:** `briefs/2026-07-30_k226-gpt-red-prod.md`

## Relations

- @concepts/gpt-red-self-play-red-teaming.md
- @concepts/pair-prompt-pattern.md
- @concepts/crescendo-multi-turn-jailbreak.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | GPT-Red: Automated Red Teaming via Self-Play at Scale |
| Authors | Wallace, Choquette-Choo, Kandpal, Toyer, Hunn, Lin, et al. (OpenAI) |
| arXiv | 2607.26115 |
| Code | none public (eval harness cite: UKGovernmentBEIS/inspect_ai — not adopted; ~400MB) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.26115-gpt-red-automated-red-teaming-via-self-play-at-s.pdf` |
| Retrieved | 2026-07-30 |

## Narrative

Scalable **self-play**: attacker discovers novel prompt-injection attacks against a population of co-trained defenders. Compute at RL post-training scale. Breaks past models through GPT-5.5; beats human red-teamers; generalizes to held-out environments/harnesses; used to adversarially train **GPT-5.6**. Scale attacker search + self-play diversity + defender diversity together.

### Steal

1. Red-team agents need a **population** of defenders, not one fixed target
2. Inference-time attack search scales — budget it in harness gates
3. Adversarial train production agents against automated attackers, not only static suites

## Snippets

> "it finds more successful attacks than human red-teamers, and it generalizes to held-out environments, defender models, and harnesses."
[Source: arxiv-2607.26115 abstract]
