---
title: "Physical layer deception as a second auth factor (K393)"
type: concept
tags: [concept, wireless-security, k393]
keywords: [2610.01580, K393]
related:
  - sources/arxiv-2610-01580-pld-eap-teap-wifi-authentication.md
  - concepts/wireless-pentest.md
  - concepts/wifi-rf-fingerprinting-open-set.md
  - concepts/network-security.md
maturity: draft
created: 2026-10-03
updated: 2026-10-03
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K393)"
---

## Relations

- @sources/arxiv-2610-01580-pld-eap-teap-wifi-authentication.md
- @concepts/wireless-pentest.md
- @concepts/wifi-rf-fingerprinting-open-set.md
- @concepts/network-security.md

## Raw Concept

Question: **Physical layer deception as a second auth factor** — operator steal from arXiv 2610.01580?

## Narrative

A credential is a bearer token: whoever holds it authenticates. A **channel-derived** second factor asks instead whether the claimant is *where* it claims — evidence a remote party cannot easily reproduce. The mechanism here is **deception, not measurement**: the server puts a deliberately wrong value on the primary path and a key on a secondary path, so only a well-positioned receiver recovers the truth. Design constraints worth keeping: at least one round must be active (all-inactive leaks the truth), no activation flag is transmitted (its presence would be the signal), and **all** rounds gate the result. Costs are explicit — a false-accept probability **r_E^A** traded against a false-reject **1 − r_B^A** — so it is only deployable where that trade is chosen deliberately. Pairs channel-fingerprint approaches; it does not replace them.

## Snippets

> See arXiv 2610.01580 abstract. [Source: arXiv 2610.01580 (retrieved 2026-10-03)]
