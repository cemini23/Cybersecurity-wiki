---
title: "Effective dense retrieval using only in-context examples"
type: source
tags: [source, arxiv, agent-security]
keywords: [2609.38099, k386]
related:
  - concepts/rice-in-context-dense-retrieval.md
  - concepts/kamr-knowledge-aligned-multihop-retrieval.md
  - concepts/rag-safety-bench-evaluation.md
maturity: draft
read_status: read
created: 2026-09-30
updated: 2026-09-30
phase_0_verdict: "REFERENCE 2026-09-30 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K386)"
---

## Relations

## Relations

- @concepts/rice-in-context-dense-retrieval.md
- @concepts/kamr-knowledge-aligned-multihop-retrieval.md
- @concepts/rag-safety-bench-evaluation.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Effective dense retrieval using only in-context examples |
| arXiv | 2609.38099 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.38099-effective-dense-retrieval-using-only-in-context.pdf |
| Retrieved | 2026-09-30 |
| Read status | read (abstract + triage) |

## Narrative

**K386** — turning a decoder-only LLM into a dense retriever normally needs retriever training. **RICE** is **training-free**: condition both query and document encoding on the **same few in-context query–document pairs**, and take the hidden state before the LM head at the point the model is about to emit one representative word. On 10 BEIR datasets, average Recall@100 rises to **.539** (Qwen3-8B) and **.558** (Qwen3.5-9B) vs PromptReps-Dense **.503** / **.534** — the best among training-free baselines (CSQE .513, HyDE .488) — but stays below supervised **Qwen3-Embedding-8B .645** and **BGE-base-en-v1.5 .578**. Two stated limits carry into RAG ETL: **dynamic document-side exemplars hurt** vs a fixed set, and **random representative words** degrade recall (**.697** vs **.955** on SciFact) — a corrupted or mismatched exemplar set is a retrieval-quality failure mode. Tangential to security: the paper states **no threat model**. Repo `github.com/nourj98/RICE`, license **not stated** → REFERENCE, **no clone**. Pairs K228 KAMR and K328 RAG safety bench.

## Snippets

> See arXiv 2609.38099 abstract. [Source: arXiv 2609.38099 (retrieved 2026-09-30)]
