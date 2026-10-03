---
title: "Fast and secure simultaneous authentication of equals for WPA3"
type: source
tags: [source, arxiv, wireless-security]
keywords: [2609.31519, k392]
related:
  - concepts/wpa3-sae-dos-cost-asymmetry.md
  - concepts/wireless-pentest.md
  - concepts/network-security.md
maturity: draft
read_status: read
created: 2026-10-03
updated: 2026-10-03
phase_0_verdict: "REFERENCE 2026-10-03 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K392)"
---

## Relations

## Relations

- @concepts/wpa3-sae-dos-cost-asymmetry.md
- @concepts/wireless-pentest.md
- @concepts/network-security.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Fast and secure simultaneous authentication of equals for WPA3 |
| arXiv | 2609.31519 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.31519-fast-and-secure-simultaneous-authentication-of-e.pdf |
| Retrieved | 2026-10-03 |
| Read status | read (deep-read) |

## Narrative

**K392** — WPA3-SAE fixed the WPA2 offline-dictionary weakness but **introduced a DoS surface**: the hunting-and-pecking loop that derives the Password Element (PE) is expensive, and an attacker can force the AP to run it repeatedly (Dragonblood-class CPU exhaustion). Three changes make the cost asymmetric: **RIIE** moves the iterative discovery to the *client* so the AP does a one-step derivation; a **slow-path KDF** (PBKDF2/Argon2, variable cost) puts the deliberate delay on the supplicant rather than the AP; and **SFTR** adds stateless **session tickets** (Kerberos / TLS 1.3 style, STEK-encapsulated, sequential TID, IPsec-style anti-replay window) so known devices skip PE derivation entirely. Measured on hostapd 2.10 + wpa_supplicant 2.10 with OpenSSL, N=100: standard SAE **2284 µs** (σ=521.8) → proposed initial auth **72.5 µs** (σ=11.0, **−96.8%**) → ticket fast-path **21 µs** (σ=4.9, ~**99%**). Operator steal: the load-bearing idea is **which side pays** — a cost the client must pay is cheap to demand; a cost the AP must pay is a DoS lever. Also note the honest trade: moving iteration to the client is what keeps offline-dictionary resistance, so the slow-path KDF is not optional. PBKDF2 was run at only 10 iterations for functional validation and is stated to scale. Wireless lab only — the paper's goal is availability, not a bypass.

## Snippets

> See arXiv 2609.31519 abstract. [Source: arXiv 2609.31519 (retrieved 2026-10-03)]
