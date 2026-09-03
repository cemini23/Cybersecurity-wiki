---
title: "Linguistic illegibility — LLM security implications (arXiv 2609.02852)"
type: source
tags: [source, arxiv, agent-security, audit, interpretability, k325]
keywords: [2609.02852, linguistic illegibility, CoT monitoring, taint tracking, sandbox]
related:
  - concepts/linguistic-illegibility-llm-security.md
maturity: draft
read_status: read
created: 2026-09-03
updated: 2026-09-03
phase_0_verdict: "REFERENCE 2026-09-03 — audit pattern; no sandbox-bypass payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K325)"
---

## Relations

- @concepts/linguistic-illegibility-llm-security.md — security floor below linguistic monitoring

## Raw Concept

| Field | Value |
|-------|-------|
| Title | The Implications of Linguistic Illegibility for LLM Security |
| arXiv | 2609.02852 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.02852-the-implications-of-linguistic-illegibility-for.pdf |
| Retrieved | 2026-09-03 |
| Read status | read (abstract + argument) |

## Narrative

Argues **linguistic illegibility**: externalized language and mechanistic linguistic probes may not reflect internal computation (math over activations with lossy NL bookends). Therefore **CoT monitoring, constitutional self-critique, and linguistically-defined activation probes** cannot be fully sound alone. Proposes **taint tracking** + robust sandboxing as a floor that does not depend on reading the model's linguistic self-report.

## Snippets

> Security mechanisms that rely on linguistic self-reporting can never be completely sound if linguistic illegibility is always possible. [Source: arXiv 2609.02852 abstract, paraphrase]
