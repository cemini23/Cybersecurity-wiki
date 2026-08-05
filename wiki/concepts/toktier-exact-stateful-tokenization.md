---
title: TokTier — exact stateful tokenization for agent serving
type: concept
tags: [concept, llm-serving, tokenization, agents, performance]
keywords: [TokTier, stateful tokenization, TTFT, prompt cache, 2607.29678]
related:
  - sources/arxiv-2607-29678-toktier-stateful-tokenization.md
  - concepts/inferscale-kv-injection-personalized-serving.md
  - entities/tools/vllm.md
  - entities/tools/inferscale.md
  - concepts/ai-for-cybersecurity.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/adaptive-fuzzy-test-time-sampling.md
  - sources/arxiv-2608-03961-adaptive-fuzzy-test-time-sampling.md
maturity: draft
created: 2026-08-03
updated: 2026-08-05
wire_status: policy_wired
---

## Relations

- @sources/arxiv-2607-29678-toktier-stateful-tokenization.md
- @concepts/inferscale-kv-injection-personalized-serving.md — KV injection sibling; both privilege serving internals
- @entities/tools/vllm.md
- @entities/tools/inferscale.md
- @concepts/ai-for-cybersecurity.md
- @concepts/local-abliterated-llm-pentest-stack.md
- @concepts/adaptive-fuzzy-test-time-sampling.md
- @sources/arxiv-2608-03961-adaptive-fuzzy-test-time-sampling.md

## Raw Concept

As prompt-cache hit rates rise, tokenization — not decode — dominates agent TTFT; optimizations must stay byte-identical to reference tokenization.

## Narrative

Coding/pentest agents resubmit long transcripts after each tool result. Cached KV does not remove the need for correct token IDs on the append boundary. **TokTier** pattern: stateful session tokens + windowed repair + splice certificate + shadow verify. For local friend stacks (vLLM path A) and prod: treat tokenizer/KV desync like an injection bug, not a free speedup. [CONFIRMED abstract; code closed]
