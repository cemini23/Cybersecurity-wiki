---
title: "SpecGuard inference-time backdoor detection (K329)"
type: concept
tags: [concept, agent-security, backdoor, model-supply-chain, eval, k329]
keywords: [2609.11799, SpecGuard, inference-time backdoor, trigger detection, third-party models]
related:
  - sources/arxiv-2609-11799-specguard-backdoor-detection.md
  - concepts/rtl-codegen-poison-defense.md
  - concepts/gradient-immunity-malicious-finetune.md
  - concepts/measurement-integrity-mcp-security-eval.md
maturity: draft
created: 2026-09-11
updated: 2026-09-11
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K329)"
---

## Relations

- @sources/arxiv-2609-11799-specguard-backdoor-detection.md — SpecGuard: Inference-Time Backdoor Detection For Free (2609.11799)

## Raw Concept

Question: **SpecGuard inference-time backdoor detection** — what should operators steal from this paper?

## Narrative

Third-party fine-tunes and shared weights can carry **hidden backdoors** that activate on secret triggers. Pre-deployment audit is necessary but insufficient for frequently updated models. **K329 (SpecGuard)** proposes **latency-aware inference-time** backdoor detection without heavy auxiliary models. **Operator steal:** treat downloaded weights as supply-chain risk; pair runtime SpecGuard-style checks with provenance and teacher-student sanitize (pairs K310 RTLGuard pattern for codegen). No trigger payloads in wiki.

## Snippets

> Inference-time backdoor detection for latency-sensitive LLM serving on third-party weights. [Source: arXiv 2609.11799 abstract]
