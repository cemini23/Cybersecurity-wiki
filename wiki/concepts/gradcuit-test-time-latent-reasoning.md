---
title: GradCuit — credit-assigned test-time latent reasoning
type: concept
tags: [concept, llm, test-time-compute, reasoning]
keywords: [GradCuit, latent reasoning, credit assignment, 2608.02585]
related:
  - sources/arxiv-2608-02585-gradcuit-test-time-latent-reasoning.md
  - concepts/ai-for-cybersecurity.md
  - concepts/llm-pentest-automation.md
  - concepts/inferscale-kv-injection-personalized-serving.md
maturity: draft
created: 2026-08-04
updated: 2026-08-04
---

## Relations

- @sources/arxiv-2608-02585-gradcuit-test-time-latent-reasoning.md
- @concepts/ai-for-cybersecurity.md
- @concepts/llm-pentest-automation.md
- @concepts/inferscale-kv-injection-personalized-serving.md

## Raw Concept

Optimize continuous latents at test time with direct gradient credit through the Transformer circuit — without updating weights.

## Narrative

Relevant as a **serving/steering** technique class adjacent to KV-injection research: privileged continuous state between prompt and generation. Cybersec posture: treat such latents as trusted control plane; do not accept unauthenticated external latent updates. Code closed/unlicensed — methodology only. [CONFIRMED abstract]
