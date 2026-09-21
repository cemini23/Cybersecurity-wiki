---
title: "TPM-Attest — hardware-rooted integrity attestation for Linux anti-cheat (arXiv 2609.20909)"
type: source
tags: [source, arxiv, attestation, tpm, anti-cheat, linux, product-security, k351]
keywords: [2609.20909, TPM-Attest, IMA, remote attestation, Linux gaming, EOS, Merkle tree]
related:
  - concepts/tpm-attest-linux-integrity-attestation.md
  - concepts/hardware-bound-identity-anticheat-licensing.md
maturity: draft
read_status: read
created: 2026-09-21
updated: 2026-09-21
phase_0_verdict: "REFERENCE 2026-09-21 — open-source claimed; no matching SPDX repo at hunt → no clone."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-containment.mdc (K351)"
---

## Relations

- @concepts/tpm-attest-linux-integrity-attestation.md — K351 concept

## Raw Concept

| Field | Value |
|-------|-------|
| Title | TPM-Attest: Hardware-Rooted Integrity Attestation as a Kernel-Level Anti-Cheat Alternative for Linux |
| arXiv | 2609.20909 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.20909-tpm-attest-hardware-rooted-integrity-attestation.pdf |
| Retrieved | 2026-09-21 |
| Read status | read (abstract + triage) |

## Narrative

**TPM-Attest** replaces invasive Ring 0 kernel anti-cheat with **TPM 2.0 + Linux IMA** remote attestation: prove boot integrity and authorized software execution without proprietary kernel drivers or memory scanning. A userspace `LD_PRELOAD` hook gates Epic Online Services session access on a live TPM quote bound to a server nonce; an index-prefixed Merkle tree over the IMA log resists duplicate-leaf collisions. Reported 100% detection on 500 tamper sessions; repeat attestation under 3s with leaf caching on real TPM hardware. **K351** is a **defensive product-security pattern steal** for owned Linux multiplayer surfaces — pairs mobile attestation and hardware-bound identity concepts. No bypass recipes in wiki. Open-source release claimed; **no matching public repo with SPDX at hunt** → REFERENCE only.

## Snippets

> Instead of scanning memory at runtime, TPM-Attest asks: did this machine boot into a known-good state and execute only authorised software? [Source: arXiv 2609.20909 abstract]

> Index-prefixed Merkle tree over the IMA log immune to duplicate-leaf collision attacks. [Source: arXiv 2609.20909 abstract]
