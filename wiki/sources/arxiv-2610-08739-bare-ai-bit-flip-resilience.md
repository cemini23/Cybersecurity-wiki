---
title: "BARE-AI: bit-flip attack resilience in AI hardware through built-in performance monitors"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.08739, k406]
related:
  - concepts/dnn-bit-flip-detection-runtime-monitors.md
  - concepts/hardware-membership-inference-microarchitecture.md
  - concepts/tpm-attest-linux-integrity-attestation.md
  - concepts/mobile-app-attestation.md
maturity: draft
read_status: read
created: 2026-10-07
updated: 2026-10-07
phase_0_verdict: "REFERENCE 2026-10-07 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K406)"
---

## Relations

## Relations

- @concepts/dnn-bit-flip-detection-runtime-monitors.md
- @concepts/hardware-membership-inference-microarchitecture.md
- @concepts/tpm-attest-linux-integrity-attestation.md
- @concepts/mobile-app-attestation.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | BARE-AI: bit-flip attack resilience in AI hardware through built-in performance monitors |
| arXiv | 2610.08739 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.08739-bare-ai-bit-flip-attack-resilience-in-ai-hardwar.pdf |
| Retrieved | 2026-10-07 |
| Read status | read (deep-read) |

## Narrative

**K406** — a **bit-flip attack** perturbs a few memory locations and degrades DNN accuracy sharply; existing defences carry heavy hardware cost, need retraining, or miss *targeted* flips. BARE-AI detects, localises, and mitigates at **runtime**. It adds **AI Performance Counters (APCs)** — lightweight monitors in the accelerator datapath that capture per-layer activation statistics (**sparsity, entropy, kurtosis, spectral shift**) — and feeds them to **PULSE**, a compact offline-trained ensemble realised on-chip as a small neural engine. For recovery it introduces an **Activation Shift Index (ASI)** for layer-level fault localisation and a **z-score statistical repair** that resets anomalous weights toward clean layer statistics. Across CNNs, ViTs and LLMs under random / targeted / adaptive / magnitude-based BFAs: **up to 98%** detection on vision models, **74–95%** on language models; near-clean accuracy restored for CNNs and ViTs, partial for LLMs. Cost is **< 3% energy, < 4% area, ~10% latency** (a configurable operating point takes latency to ~6%), and the overhead stays bounded as the tolerated flip count grows. Operator steal: **activation statistics are a cheap, model-agnostic tripwire for weight corruption**, and a monitor beats a retrain when the fault is physical. Pairs K402 — both are hardware-layer integrity stories that a software-only argument misses. Authorized hardware lab only. **No fault-injection recipes in wiki.**

## Snippets

> See arXiv 2610.08739 abstract. [Source: arXiv 2610.08739 (retrieved 2026-10-07)]
