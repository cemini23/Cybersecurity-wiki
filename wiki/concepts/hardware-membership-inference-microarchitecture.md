---
title: "Hardware membership inference through microarchitecture (K402)"
type: concept
tags: [concept, agent-security, k402]
keywords: [2610.06848, K402]
related:
  - sources/arxiv-2610-08739-bare-ai-bit-flip-resilience.md
  - concepts/dnn-bit-flip-detection-runtime-monitors.md
  - sources/arxiv-2610-06848-transcope-hardware-membership-inference.md
  - concepts/asleval-privacy-exposure-displacement.md
  - concepts/hardware-id-masking-opsec.md
  - concepts/tpm-attest-linux-integrity-attestation.md
maturity: draft
created: 2026-10-06
updated: 2026-10-07
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K402)"
---

## Relations

- @sources/arxiv-2610-08739-bare-ai-bit-flip-resilience.md — K403-K407 ingest source page
- @concepts/dnn-bit-flip-detection-runtime-monitors.md — K406 hardware-layer integrity: activation statistics as a tripwire
- @sources/arxiv-2610-06848-transcope-hardware-membership-inference.md
- @concepts/asleval-privacy-exposure-displacement.md
- @concepts/hardware-id-masking-opsec.md
- @concepts/tpm-attest-linux-integrity-attestation.md

## Raw Concept

Question: **Hardware membership inference through microarchitecture** — operator steal from arXiv 2610.06848?

## Narrative

"The model is constant-time and returns masked confidence, so it leaks nothing" is a **software** claim. This work shows the **hardware** still leaks: tokenisation performed at training time shifts the locality of vocabulary fetches at inference, which perturbs page-table access and the **TLB** in a way that depends on whether the input was in the training distribution. Reported at **0.9 AUC** and **98% accuracy at 1.5% FPR**, against 0.6 AUC for the best previously reported method. The operator consequence: a privacy or anti-extraction argument must cover the **memory system and any on-core accelerators**, not only the code path — and that surface is visible to a co-tenant or a host measuring cycles. Pairs the K347 privacy-exposure-displacement thread.

## Snippets

> See arXiv 2610.06848 abstract. [Source: arXiv 2610.06848 (retrieved 2026-10-06)]
