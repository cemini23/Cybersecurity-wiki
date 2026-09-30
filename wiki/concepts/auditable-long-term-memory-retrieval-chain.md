---
title: "Auditable long-term memory retrieval chain (K385)"
type: concept
tags: [concept, agent-security, k385]
keywords: [2609.38021, K385]
related:
  - sources/arxiv-2609-38021-auditable-long-term-memory-retrieval-chain.md
  - concepts/trajectory-context-control.md
  - concepts/kamr-knowledge-aligned-multihop-retrieval.md
maturity: draft
created: 2026-09-30
updated: 2026-09-30
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K385)"
---

## Relations

- @sources/arxiv-2609-38021-auditable-long-term-memory-retrieval-chain.md
- @concepts/trajectory-context-control.md
- @concepts/kamr-knowledge-aligned-multihop-retrieval.md

## Raw Concept

Question: **Auditable long-term memory retrieval chain** — operator steal from arXiv 2609.38021?

## Narrative

Keep the **retrieval chain deterministic** and the LLM a **replaceable reader**. Report retrieval coverage (gold sessions in the pool, gold-complete packets) **separately** from the reader score, and measure **judge variance** and **verdict flips** on identical answers. Pre-commit a two-pass rule and run **negative controls** before accepting a verifier. Disclose operator context padded into reader calls. **No memory contents or scaffold sources in wiki.**

## Snippets

> See arXiv 2609.38021 abstract. [Source: arXiv 2609.38021 (retrieved 2026-09-30)]
