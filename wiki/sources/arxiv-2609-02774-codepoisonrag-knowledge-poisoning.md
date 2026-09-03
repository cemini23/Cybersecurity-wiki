---
title: "CodePoisonRAG — knowledge poisoning on retrieval-augmented code generation (arXiv 2609.02774)"
type: source
tags: [source, arxiv, agent-security, rag, poisoning, lab-only, k323]
keywords: [2609.02774, CodePoisonRAG, RACG, knowledge poisoning, CWE injection, semantic mislabeling]
related:
  - concepts/codepoisonrag-racg-knowledge-poisoning.md
maturity: draft
read_status: read
created: 2026-09-03
updated: 2026-09-03
phase_0_verdict: "REFERENCE 2026-09-03 — no poison artifact bodies in wiki; authorized lab eval only."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc + agent-audit.mdc (K323)"
---

## Relations

- @concepts/codepoisonrag-racg-knowledge-poisoning.md — upstream RAG trust boundary for code gen

## Raw Concept

| Field | Value |
|-------|-------|
| Title | CodePoisonRAG: Knowledge Poisoning Attacks on Retrieval-Augmented Code Generation |
| arXiv | 2609.02774 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.02774-codepoisonrag-knowledge-poisoning-attacks-on-ret.pdf |
| Retrieved | 2026-09-03 |
| Read status | read (abstract + method) |

## Narrative

Black-box upstream poisoning for **retrieval-augmented code generation (RACG)**: one task-matched artifact per query can propagate an **attacker-selected CWE** via vulnerability injection + semantic mislabeling (false safety claims). 85 artifacts, 0.7% corpus ratio, Top-3 retrieval for all queries; ASR 0.80–0.93 across three generators; partial retention vs CodeGuarder (0.40–0.71). **Lab eval surface only** — no poison templates in wiki.

## Snippets

> Prior work shows that selecting existing vulnerable examples can increase vulnerability rate; CodePoisonRAG shows targeted construction of attacker-selected weaknesses via upstream knowledge poisoning. [Source: arXiv 2609.02774 abstract, paraphrase]
