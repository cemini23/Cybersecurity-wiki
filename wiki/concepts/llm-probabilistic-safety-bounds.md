---
title: Sound probabilistic safety bounds for LLMs
type: concept
tags: [concept, llm-safety, formal-methods, pac]
keywords: [Clopper-Pearson, PAC lower bound, harm probability, latent search, 2607.20286]
related:
  - sources/arxiv-2607-20286-probabilistic-llm-safety-bounds.md
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-07-23
updated: 2026-07-23
---

## Relations

- @sources/arxiv-2607-20286-probabilistic-llm-safety-bounds.md
- @concepts/agent-runtime-guardrails.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

Statistical **certification** of P(harm | prompt) via sound PAC lower bounds — not just empirical refusal rates.

## Narrative

Alignment reduces but does not eliminate harm probability. Clopper-Pearson intervals + latent-guided tree search yield **sound** lower bounds even for rare events. Use for high-stakes prompt classes before agent deploy. [CONFIRMED abstract]

No public code yet — methodology steal only.
