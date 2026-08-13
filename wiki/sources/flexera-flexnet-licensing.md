---
title: FlexNet Licensing (Revenera)
type: source
tags: [source, licensing, vendor-doc, product-pentest]
keywords: [FlexNet, FlexLM, Flexera, Revenera, floating license, node-locked, trusted storage, license server, entitlement]
related:
  - concepts/software-license-binding.md
  - concepts/pre-release-product-pentest.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — commercial licensing vendor overview (public marketing/docs)"
wire_status: wont_wire
---

## Relations

- @concepts/software-license-binding.md — commercial instance of the floating/node-locked binding menu
- @concepts/pre-release-product-pentest.md — entitlement enforcement as part of the owned-product ship bar

## Raw Concept

| Field | Value |
|-------|-------|
| Title | FlexNet Licensing |
| Publisher | Revenera (product page; www.flexera.com 301-redirects here) |
| URL | https://www.revenera.com/software-monetization/products/software-licensing/flexnet-licensing |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

Commercial licensing platform (on-prem / SaaS / cloud / embedded / IoT). License models: subscription, token, consumption-based, floating/concurrent, device-based, node-locked, named-user, capacity, metered, pay-for-use/overage, time-limited. **FlexNet Publisher** (formerly FlexLM) is the on-prem license-server flagship. Enforcement claims: tamper-resistant code, secure activation, VM-cloning detection (deny-or-report policy), trusted storage in embedded SDKs, FlexNet ID dongle as hostid, license-server authority for floating seats. Compliance telemetry flags "red flag behavior" (license cloning, clock wind-back).

For the wiki: this is the **online-lease + device-fingerprint** commercial exemplar — the third-party equivalent of the KMS/OA3 split, and a reference for what a product license server must do (server authority, anomaly reporting, revocation).

## Snippets

> "FlexNet Publisher (formerly FlexLM) is the de facto standard in software licensing solutions."

> "Report and act on 'red flag behavior', such as license cloning or clock wind-back."

[Source: https://www.revenera.com/software-monetization/products/software-licensing/flexnet-licensing (retrieved 2026-08-12)]
