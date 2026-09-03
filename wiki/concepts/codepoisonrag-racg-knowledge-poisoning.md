---
title: "CodePoisonRAG — upstream RAG poisoning for code generation (K323)"
type: concept
tags: [concept, agent-security, rag, poisoning, code-gen, lab-only, k323]
keywords: [CodePoisonRAG, RACG, knowledge poisoning, CWE injection, semantic mislabeling, retrieval trust boundary]
related:
  - sources/arxiv-2609-02774-codepoisonrag-knowledge-poisoning.md
  - concepts/agent-data-injection-attacks.md
  - concepts/committee-certified-rag-provenance.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - concepts/llm-pentest-automation.md
  - concepts/salami-collusive-memory-poisoning.md
maturity: draft
created: 2026-09-03
updated: 2026-09-03
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K323)"
---

## Relations

- @sources/arxiv-2609-02774-codepoisonrag-knowledge-poisoning.md — CodePoisonRAG (2609.02774)
- @concepts/agent-data-injection-attacks.md — retrieval is an integrity boundary

## Raw Concept

Question: **can a single upstream poisoned code artifact steer RACG toward an attacker-chosen weakness without model weight access?**

## Narrative

**RACG** adds a **retrieval trust boundary**: poisoned docs/patches can influence generated code without touching the LLM weights. **K323 (CodePoisonRAG)** shows **targeted** upstream poisoning (CWE-specific injection + semantic mislabeling) achieves high Top-k retrieval and ASR at **sub-1% corpus ratio**. Context-only defenses (e.g. CodeGuarder) reduce but do not eliminate success.

**Operator steal:** treat code/doc **vector ingest** like supply-chain — provenance, allowlists, mutation tests on retrieved snippets before generation context. **Authorized lab eval only**; no poison artifact bodies in wiki.

## Snippets

> Attack success rates between 0.80 and 0.93 across three generators at 0.7% corpus poisoning ratio. [Source: arXiv 2609.02774 abstract]
