---
title: GPT-Red self-play automated red teaming
type: concept
tags: [concept, red-teaming, prompt-injection, self-play]
keywords: [GPT-Red, self-play, defender population, 2607.26115]
related:
  - sources/arxiv-2607-26115-gpt-red-self-play.md
  - concepts/pair-prompt-pattern.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-07-30
updated: 2026-07-30
---

## Relations

- @sources/arxiv-2607-26115-gpt-red-self-play.md
- @concepts/pair-prompt-pattern.md
- @concepts/crescendo-multi-turn-jailbreak.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

Scale automated prompt-injection discovery by self-play against a co-trained defender population.

## Narrative

Static suites under-elicit. GPT-Red shows attacker search + defender diversity + large compute beats human red-teamers and transfers across harnesses. Use findings to adversarially train production models (GPT-5.6 claim). Operator: build multi-defender self-play loops in lab; do not rely on one fixed system prompt. [CONFIRMED abstract; weights closed]
