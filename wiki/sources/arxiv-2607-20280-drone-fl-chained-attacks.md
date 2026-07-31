---
title: Chained attacks on drone-based federated learning (arXiv 2607.20280)
type: source
tags: [source, arxiv, wireless, federated-learning, drones, deauth]
keywords: [2607.20280, Flower, 802.11 deauthentication, impersonation, Non-IID, Jetson]
related:
  - concepts/drone-fl-chained-deauth-impersonation.md
  - concepts/wireless-pentest.md
  - concepts/industrial-safety-security-convergence.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-24
updated: 2026-07-31
phase_0_verdict: "REFERENCE 2026-07-24 — no public code; Flower-based physical testbed paper"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

**Briefs:** `briefs/2026-07-24_k215-drone-fl-chained-attacks-prod.md`

## Relations

- @concepts/drone-fl-chained-deauth-impersonation.md
- @concepts/wireless-pentest.md
- @concepts/industrial-safety-security-convergence.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Chained Attacks on Drone-Based Federated Learning: From Network Disruption to Device Impersonation |
| Authors | Sabo, Alkharsh, Li, Ahmed, Abadi, Nagaraja, Ranjan (Newcastle) |
| arXiv | 2607.20280 |
| Code | none located |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.20280-chained-attacks-on-drone-based-federated-learnin.pdf` |
| Retrieved | 2026-07-24 |

## Narrative

Chained attack on drone FL: (1) **802.11 deauth** forces legitimate drone offline; (2) **credential impersonation** fills the session vacancy. Empirical Flower testbeds on Raspberry Pi + NVIDIA Jetson; IID and Non-IID. Single-factor auth permits post-disconnect impersonation — server incorporated impersonator updates (training loss continued converging).

### Steal

1. FL client auth must survive availability attacks — not just join-time checks
2. Deauth → impersonation is a real physical-layer → app-layer chain for edge FL
3. Lab: reproduce with Flower on Pi/Jetson if building drone/edge FL labs

## Snippets

> "an adversary can: (1) force legitimate drones offline using 802.11 deauthentication attacks, and (2) subsequently impersonate the disconnected drone using extracted credentials."
[Source: arxiv-2607.20280 abstract]
