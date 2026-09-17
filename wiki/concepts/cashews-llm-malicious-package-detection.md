---
title: "CASHEWS LLM malicious package preprocessor (K346)"
type: concept
tags: [concept, supply-chain, npm, malware, agent-security, k346]
keywords: [2609.18862, CASHEWS, npm, malicious package, obfuscation, token density, supply chain]
related:
  - sources/arxiv-2609-18862-cashews-malicious-package-detection.md
  - concepts/coding-agent-supply-chain-install-gap.md
  - concepts/skillsec-lifecycle-agent-skill-security.md
  - concepts/product-build-integrity-slsa-sigstore.md
  - concepts/codepoisonrag-racg-knowledge-poisoning.md
maturity: draft
created: 2026-09-17
updated: 2026-09-17
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K346)"
---

## Relations

- @sources/arxiv-2609-18862-cashews-malicious-package-detection.md — CASHEWS: Source Preprocessor for LLM-based Malicious Package Detection (2609.18862)

## Raw Concept

Question: **CASHEWS LLM malicious package preprocessor** — what should operators steal from this paper?

## Narrative

LLM-based **malicious npm package detection** is evaded via **obfuscation**, high **token density**, and bundling malicious code with benign files that exceed context limits. **K346 (CASHEWS)** preprocesses source to normalize/evade-resistant inputs before LLM classification. **Defensive steal:** treat package ingest as supply-chain boundary — preprocess + size/token limits + human review; pairs install-gap and SkillSec lifecycle.

## Snippets

> CASHEWS preprocesses npm sources to counter obfuscation and token-density evasion of LLM package classifiers. [Source: arXiv 2609.18862 abstract]
