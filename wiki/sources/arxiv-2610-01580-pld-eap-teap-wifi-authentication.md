---
title: "Protocol integration of physical layer deception into EAP-TEAP Wi-Fi authentication"
type: source
tags: [source, arxiv, wireless-security]
keywords: [2610.01580, k393]
related:
  - concepts/physical-layer-deception-enterprise-wifi-auth.md
  - concepts/wireless-pentest.md
  - concepts/wifi-rf-fingerprinting-open-set.md
  - concepts/network-security.md
maturity: draft
read_status: read
created: 2026-10-03
updated: 2026-10-03
phase_0_verdict: "REFERENCE 2026-10-03 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K393)"
---

## Relations

## Relations

- @concepts/physical-layer-deception-enterprise-wifi-auth.md
- @concepts/wireless-pentest.md
- @concepts/wifi-rf-fingerprinting-open-set.md
- @concepts/network-security.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Protocol integration of physical layer deception into EAP-TEAP Wi-Fi authentication |
| arXiv | 2610.01580 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.01580-protocol-integration-of-physical-layer-deception.pdf |
| Retrieved | 2026-10-03 |
| Read status | read (deep-read) |

## Narrative

**K393** — credential-based EAP authenticates *whoever holds the credential*, so a cloned or exfiltrated credential makes an adversary indistinguishable at the credential layer. This adds **Physical Layer Deception (PLD)** as a second factor derived from the channel: each round exposes a deceptive primary object (`m = p ⊕ k`, fresh nonzero key) over the TEAP/TLS tunnel while a key-bearing **recovery object** travels separately over IEEE 802.11 Category-127 action frames, where a favourably-placed receiver recovers the true value more reliably than a remote one. Authentication-specific twist: a batch of L≤3 rounds with **exactly A active positions, A≥1**, no activation flag, and all rounds must verify — because an all-inactive attempt would leak every true challenge and never exercise the recovery path. Implemented end to end in **hostap 2.12** (server + hostapd + wpa_supplicant) under mac80211_hwsim; **1593 attempts** across four campaigns. The AP relays and never decrypts TEAP, so it never sees the plaintext primary object. Results: ordinary TEAP 30/30 accepted; full recovery L=3, A=1 and A=3 both 30/30; degraded recovery (r=.95, A=1) 29/30; the **naive credential-bearing attacker is rejected in all 30 attempts**. Trade-off is analytic: **PFA = r_E^A**, **PFR = 1 − r_B^A**, with a 2000 ms recovery deadline. Operator steal: a second factor can live in the **channel**, not in another secret — but the binding needs a recovery channel the attacker cannot co-locate with. Wireless/enterprise lab only.

## Snippets

> See arXiv 2610.01580 abstract. [Source: arXiv 2610.01580 (retrieved 2026-10-03)]
