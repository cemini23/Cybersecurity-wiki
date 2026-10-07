---
title: "Runtime detection of bit-flip corruption in DNNs (K406)"
type: concept
tags: [concept, agent-security, k406]
keywords: [2610.08739, K406]
related:
  - sources/arxiv-2610-08739-bare-ai-bit-flip-resilience.md
  - concepts/hardware-membership-inference-microarchitecture.md
  - concepts/tpm-attest-linux-integrity-attestation.md
  - concepts/mobile-app-attestation.md
maturity: draft
created: 2026-10-07
updated: 2026-10-07
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K406)"
---

## Relations

- @sources/arxiv-2610-08739-bare-ai-bit-flip-resilience.md
- @concepts/hardware-membership-inference-microarchitecture.md
- @concepts/tpm-attest-linux-integrity-attestation.md
- @concepts/mobile-app-attestation.md

## Raw Concept

Question: **Runtime detection of bit-flip corruption in DNNs** — operator steal from arXiv 2610.08739?

## Narrative

A few flipped bits in model memory can gut accuracy, and the flips need not be random — targeted and adaptive attacks defeat simple checks. The practical defence is a **runtime monitor**, not a retrain: instrument the accelerator with lightweight counters over **per-layer activation statistics** (sparsity, entropy, kurtosis, spectral shift) and detect deviation from the clean profile. Detection is only half — you also need **localisation** (which layer) and **repair** (nudge anomalous weights back toward clean statistics). Reported at **up to 98%** detection on vision models and **74–95%** on LLMs, for **< 3% energy / < 4% area / ~10% latency**. The operator rule: a software-only integrity argument misses the memory system — pairs K402, where the same lesson arrives from the privacy side.

## Snippets

> See arXiv 2610.08739 abstract. [Source: arXiv 2610.08739 (retrieved 2026-10-07)]
