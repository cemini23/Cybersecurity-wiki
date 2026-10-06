---
title: "TransScope: what the software hides about LLM training data, the hardware reveals at scale"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.06848, k402]
related:
  - concepts/hardware-membership-inference-microarchitecture.md
  - concepts/asleval-privacy-exposure-displacement.md
  - concepts/hardware-id-masking-opsec.md
  - concepts/tpm-attest-linux-integrity-attestation.md
maturity: draft
read_status: read
created: 2026-10-06
updated: 2026-10-06
phase_0_verdict: "REFERENCE 2026-10-06 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K402)"
---

## Relations

## Relations

- @concepts/hardware-membership-inference-microarchitecture.md
- @concepts/asleval-privacy-exposure-displacement.md
- @concepts/hardware-id-masking-opsec.md
- @concepts/tpm-attest-linux-integrity-attestation.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | TransScope: what the software hides about LLM training data, the hardware reveals at scale |
| arXiv | 2610.06848 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.06848-transcope-what-the-software-hides-about-llm-trai.pdf |
| Retrieved | 2026-10-06 |
| Read status | read (deep-read) |

## Narrative

**K402 — a privacy result that removes an assumption people rely on.** Membership is the root privacy primitive, and prior work found no hardware-based out-of-distribution detection against **constant-time, static** black-box models with masked confidence. This is the first **cycle-level** examination of how LLMs and ViTs interact with microarchitecture, including integrated accelerators, and the answer is that **training data does change the execution footprint** even with no input-dependent branch, no dynamic optimisation, and no early exit. The mechanism is specific and worth carrying: **tokenisation performed during training alters the locality of vocabulary-token fetches at inference**, which changes page-table access patterns and **TLB** behaviour in a data-dependent way, so microarchitectural state varies with whether the input was in-distribution. TLBs and on-core accelerators are the components that reveal or amplify it. Numbers: **AUC 0.9** against a best-previously-reported **0.6** (PETAL), and OOD-detection accuracy **98%** at **1.5% FPR**. Operator steal: **constant-time software does not imply a constant hardware footprint** — when you argue that a model reveals nothing about its training data, the argument has to cover the memory system, not just the code path. Pairs the privacy-exposure thread (K347). **No attack tooling in wiki.**

## Snippets

> See arXiv 2610.06848 abstract. [Source: arXiv 2610.06848 (retrieved 2026-10-06)]
