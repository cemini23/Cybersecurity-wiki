---
title: "WPA3 SAE cost asymmetry — DoS hardening (K392)"
type: concept
tags: [concept, wireless-security, k392]
keywords: [2609.31519, K392]
related:
  - sources/arxiv-2609-31519-wpa3-sae-asymmetric-pe-tickets.md
  - concepts/wireless-pentest.md
  - concepts/network-security.md
maturity: draft
created: 2026-10-03
updated: 2026-10-03
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K392)"
---

## Relations

- @sources/arxiv-2609-31519-wpa3-sae-asymmetric-pe-tickets.md
- @concepts/wireless-pentest.md
- @concepts/network-security.md

## Raw Concept

Question: **WPA3 SAE cost asymmetry — DoS hardening** — operator steal from arXiv 2609.31519?

## Narrative

SAE is deliberately expensive, which is both its strength and its availability weakness. The design rule to reuse: **put the expensive, unbounded work on the side that can afford to be exhausted, and make the other side's work fixed.** Here the client does the iteration and the AP does a single derivation; a variable-cost KDF adds a tunable delay on the supplicant (PBKDF2 / Argon2 with real iteration counts — 10 is a prototype value); stateless tickets let known devices skip the exchange. Two cautions: the slow path is what preserves offline-dictionary resistance, so shortening it is a security change, not a performance tweak; and ticket state/replay handling is the new surface. Assess an AP's SAE posture by **measuring per-authentication AP CPU cost under repeated failed attempts**, not by reading the cipher suite.

## Snippets

> See arXiv 2609.31519 abstract. [Source: arXiv 2609.31519 (retrieved 2026-10-03)]
