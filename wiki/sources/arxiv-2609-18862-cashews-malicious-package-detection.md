---
title: "CASHEWS — source preprocessor for LLM-based malicious package detection (arXiv 2609.18862)"
type: source
tags: [source, arxiv, supply-chain, npm, malware, agent-security, k346]
keywords: [2609.18862, CASHEWS, npm, malicious package, obfuscation, token density, supply chain]
related:
  - concepts/cashews-llm-malicious-package-detection.md
maturity: draft
read_status: read
created: 2026-09-17
updated: 2026-09-17
phase_0_verdict: "REFERENCE 2026-09-17 — supply-chain preprocessor pattern; no malicious package bodies in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K346)"
---

## Relations

- @concepts/cashews-llm-malicious-package-detection.md — K346 concept

## Raw Concept

| Field | Value |
|-------|-------|
| Title | CASHEWS: Source Preprocessor for LLM-based Malicious Package Detection |
| arXiv | 2609.18862 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.18862-cashews-source-preprocessor-for-llm-based-malici.pdf |
| Retrieved | 2026-09-17 |
| Read status | read (abstract + triage) |

## Narrative

LLM-based **malicious npm package detection** is evaded via **obfuscation**, high **token density**, and bundling malicious code with benign files that exceed context limits. **K346 (CASHEWS)** preprocesses source to normalize/evade-resistant inputs before LLM classification. **Defensive steal:** treat package ingest as supply-chain boundary — preprocess + size/token limits + human review; pairs install-gap and SkillSec lifecycle.

## Snippets

> CASHEWS preprocesses npm sources to counter obfuscation and token-density evasion of LLM package classifiers. [Source: arXiv 2609.18862 abstract]
