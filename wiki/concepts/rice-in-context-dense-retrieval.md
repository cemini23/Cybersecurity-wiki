---
title: "RICE in-context dense retrieval (K386)"
type: concept
tags: [concept, agent-security, k386]
keywords: [2609.38099, K386]
related:
  - sources/arxiv-2609-38099-rice-in-context-dense-retrieval.md
  - concepts/kamr-knowledge-aligned-multihop-retrieval.md
  - concepts/rag-safety-bench-evaluation.md
maturity: draft
created: 2026-09-30
updated: 2026-09-30
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K386)"
---

## Relations

- @sources/arxiv-2609-38099-rice-in-context-dense-retrieval.md
- @concepts/kamr-knowledge-aligned-multihop-retrieval.md
- @concepts/rag-safety-bench-evaluation.md

## Raw Concept

Question: **RICE in-context dense retrieval** — operator steal from arXiv 2609.38099?

## Narrative

**Training-free** dense retrieval: give query and document the **same in-context exemplar pairs**, and read the hidden state at the representative-word emission. Beats other training-free baselines but stays below supervised retrievers. For RAG pipelines the operator risk is **exemplar quality**: dynamic document-side exemplars and random representative words both **lower** recall. Audit-only — no precheck.

## Snippets

> See arXiv 2609.38099 abstract. [Source: arXiv 2609.38099 (retrieved 2026-09-30)]
