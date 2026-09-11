---
title: "SpecGuard — inference-time backdoor detection for LLMs (arXiv 2609.11799)"
type: source
tags: [source, arxiv, agent-security, backdoor, model-supply-chain, eval, k329]
keywords: [2609.11799, SpecGuard, inference-time backdoor, trigger detection, third-party models]
related:
  - concepts/specguard-inference-time-backdoor-detection.md
maturity: draft
read_status: read
created: 2026-09-11
updated: 2026-09-11
phase_0_verdict: "REFERENCE 2026-09-11 — inference-time backdoor detection; no clone until SPDX verified."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K329)"
---

## Relations

- @concepts/specguard-inference-time-backdoor-detection.md — K329 concept

## Raw Concept

| Field | Value |
|-------|-------|
| Title | SpecGuard: Inference-Time Backdoor Detection For Free |
| arXiv | 2609.11799 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.11799-specguard-inference-time-backdoor-detection-for.pdf |
| Retrieved | 2026-09-11 |
| Read status | read (abstract + triage) |

## Narrative

Third-party fine-tunes and shared weights can carry **hidden backdoors** that activate on secret triggers. Pre-deployment audit is necessary but insufficient for frequently updated models. **K329 (SpecGuard)** proposes **latency-aware inference-time** backdoor detection without heavy auxiliary models. **Operator steal:** treat downloaded weights as supply-chain risk; pair runtime SpecGuard-style checks with provenance and teacher-student sanitize (pairs K310 RTLGuard pattern for codegen). No trigger payloads in wiki.

## Snippets

> Inference-time backdoor detection for latency-sensitive LLM serving on third-party weights. [Source: arXiv 2609.11799 abstract]
