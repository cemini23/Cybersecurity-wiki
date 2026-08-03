---
title: InferScale KV injection for personalized serving
type: concept
tags: [concept, llm-serving, kv-cache, memory, security]
keywords: [InferScale, KV injection, TTFT, tenant isolation, 2607.27090]
related:
  - sources/arxiv-2607-27090-inferscale-kv-injection.md
  - entities/tools/inferscale.md
  - concepts/ai-for-cybersecurity.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-security-posture.md
  - concepts/toktier-exact-stateful-tokenization.md
  - sources/arxiv-2607-29678-toktier-stateful-tokenization.md
maturity: draft
created: 2026-07-30
updated: 2026-08-03
---

## Relations

- @sources/arxiv-2607-27090-inferscale-kv-injection.md
- @entities/tools/inferscale.md
- @concepts/ai-for-cybersecurity.md
- @concepts/agent-runtime-guardrails.md
- @concepts/mcp-security-posture.md
- @concepts/toktier-exact-stateful-tokenization.md
- @sources/arxiv-2607-29678-toktier-stateful-tokenization.md

## Raw Concept

Reusable GPU KV for personalized memory cuts TTFT — and creates a privileged injection surface.

## Narrative

**2026-08-03:** Pair with TokTier (@concepts/toktier-exact-stateful-tokenization.md) — KV/TTFT wins must preserve exact tokenization.


Performance win: precompute fact KV, inject into paged cache (chunked RoPE). Security: treat injection like tool-output hierarchy risk; isolate tenants; provenance-log injected facts; never share KV across users/sessions without policy. [CONFIRMED abstract + BSD-3 lab]
