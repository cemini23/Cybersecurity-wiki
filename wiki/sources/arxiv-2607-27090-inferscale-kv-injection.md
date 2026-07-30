---
title: InferScale GPU-native KV injection for personalized LLM serving (arXiv 2607.27090)
type: source
tags: [source, arxiv, llm-serving, kv-cache, memory, security]
keywords: [2607.27090, InferScale, KV injection, vLLM, Mem0, TTFT]
related:
  - concepts/inferscale-kv-injection-personalized-serving.md
  - entities/tools/inferscale.md
  - concepts/ai-for-cybersecurity.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-security-posture.md
maturity: draft
read_status: read
created: 2026-07-30
updated: 2026-07-30
phase_0_verdict: "GO 2026-07-30 — BSD-3-Clause; github.com/saltsystemslab/InferScale ~1.4MB"
---

**Briefs:** `briefs/2026-07-30_k227-inferscale-prod.md`

## Relations

- @concepts/inferscale-kv-injection-personalized-serving.md
- @entities/tools/inferscale.md
- @concepts/ai-for-cybersecurity.md
- @concepts/agent-runtime-guardrails.md
- @concepts/mcp-security-posture.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | InferScale: GPU-Native KV Injection for Personalized LLM Serving |
| Authors | Li, Pandey (Northeastern) |
| arXiv | 2607.27090 |
| Code | github.com/saltsystemslab/InferScale (BSD-3-Clause) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.27090-inferscale-gpu-native-kv-injection-for-personali.pdf` |
| Retrieved | 2026-07-30 |

## Narrative

Personalized memory (Mem0/MemGPT/Zep-class) forces repeated prefill → TTFT grows with retrieval budget. InferScale precomputes fact KV once, injects into vLLM paged cache via chunked RoPE + context-aware encoding. **Security steal:** KV injection is a privileged serving path — treat injected memory as an instruction/data surface; isolate per-tenant KV; audit what gets injected.

### Steal

1. Gate KV-injection APIs like tool outputs (U≻T class risk)
2. Per-tenant / per-session KV isolation — no cross-user cache bleed
3. Provenance: log which memory facts were injected into each request

## Snippets

> "replaces the repeated prefill of retrieved memory with reusable KV state: it precomputes each fact’s KV once and injects it into vLLM’s paged cache"
[Source: arxiv-2607.27090 conclusion]
