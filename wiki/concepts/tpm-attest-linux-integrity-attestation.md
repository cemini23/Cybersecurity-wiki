---
title: "TPM-Attest Linux integrity attestation (K351)"
type: concept
tags: [concept, attestation, tpm, anti-cheat, linux, product-security, k351]
keywords: [2609.20909, TPM-Attest, IMA, remote attestation, EOS, hardware-rooted integrity]
related:
  - sources/arxiv-2609-20909-tpm-attest-hardware-rooted-integrity-attestation.md
  - concepts/hardware-bound-identity-anticheat-licensing.md
  - concepts/mobile-app-attestation.md
  - concepts/secure-boot-vs-device-ownership.md
  - concepts/pre-release-product-pentest.md
maturity: draft
created: 2026-09-21
updated: 2026-09-21
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-containment.mdc (K351)"
---

## Relations

- @sources/arxiv-2609-20909-tpm-attest-hardware-rooted-integrity-attestation.md — TPM-Attest (2609.20909)

## Raw Concept

Question: **TPM-Attest Linux integrity attestation** — what should operators steal from this paper?

## Narrative

Kernel-mode anti-cheat on Linux conflicts with GPL, stable ABI, and security model — yet competitive multiplayer remains gated. **K351** steals an alternative: **hardware-rooted attestation** (TPM 2.0 quote + IMA execution log) at session start instead of invasive memory scanning. Server verifies a nonce-bound quote and Merkle-backed IMA chain before network play.

Defensive steal for **owned product pentest / authorized lab**:

- Treat attestation as a **trust boundary** — enumerate where plaintext state is materialized (pairs K280 TEE boundary thinking).
- Verify **server-side quote validation**, not client self-report.
- Document **known bypass conditions** separately from detection rate claims.
- Do not ship bypass tradecraft in wiki.

Open-source implementation claimed; **no SPDX-verified clone at hunt** → REFERENCE pattern steal only.

## Snippets

> TPM 2.0 + IMA can prove boot integrity and authorized software without Ring 0 anti-cheat drivers. [Source: arXiv 2609.20909 abstract]
