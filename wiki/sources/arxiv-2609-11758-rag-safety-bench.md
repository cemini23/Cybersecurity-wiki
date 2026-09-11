---
title: "RAG-Safety-Bench — reliable evaluation of retrieval-augmented LLM safety (arXiv 2609.11758)"
type: source
tags: [source, arxiv, agent-security, rag, safety, eval, k328]
keywords: [2609.11758, RAG-Safety-Bench, retrieval-augmented safety, harmful content, eval reliability]
related:
  - concepts/rag-safety-bench-evaluation.md
maturity: draft
read_status: read
created: 2026-09-11
updated: 2026-09-11
phase_0_verdict: "REFERENCE 2026-09-11 — RAG safety eval bench; no clone until SPDX verified."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K328)"
---

## Relations

- @concepts/rag-safety-bench-evaluation.md — K328 concept

## Raw Concept

| Field | Value |
|-------|-------|
| Title | RAG-Safety-Bench: Reliable Evaluation of Retrieval-Augmented LLM Safety |
| arXiv | 2609.11758 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.11758-rag-safety-bench-reliable-evaluation-of-retrieva.pdf |
| Retrieved | 2026-09-11 |
| Read status | read (abstract + triage) |

## Narrative

RAG can improve factuality but also **changes the safety profile** when harmful queries retrieve corpus content. **K328 (RAG-Safety-Bench)** provides a benchmark and analysis framework for **reliable** measurement of retrieval-conditioned safety — separating retrieval effects from base-model refusal behavior. Pairs **K323 CodePoisonRAG** (upstream poisoning) with downstream safety measurement. Report mechanisms, corpus conditions, and judge configuration; do not treat a single scalar as a safety certificate.

## Snippets

> Retrieval-augmented generation can alter safety outcomes; dedicated bench measures retrieval-conditioned harmful response rates. [Source: arXiv 2609.11758 abstract]
