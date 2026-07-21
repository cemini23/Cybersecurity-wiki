---
title: Industrial safety–security convergence (prEN 50742 / IO-Link Wireless)
type: concept
tags: [ot, iiot, functional-safety, industrial-wireless, cybersecurity]
keywords: [prEN 50742, SRSL, IO-Link Wireless, OPC UA Safety, private 5G, Wi-Fi 6]
related:
  - sources/arxiv-2607-15840-io-link-wireless-pren-50742.md
  - concepts/network-security.md
  - concepts/wireless-pentest.md
  - concepts/6g-cps-closed-loop-security.md
  - sources/arxiv-2606-22939-citadel-csi-jamming-iiot.md
  - concepts/solver-grounded-agentic-ot.md
  - sources/arxiv-2607-18147-llms-agents-smart-grids-tutorial.md
maturity: draft
created: 2026-07-20
updated: 2026-07-21
---

## Relations

- @sources/arxiv-2607-18147-llms-agents-smart-grids-tutorial.md
- @concepts/solver-grounded-agentic-ot.md
- @sources/arxiv-2607-15840-io-link-wireless-pren-50742.md — empirical SRSL latency/capacity study
- @concepts/network-security.md — OT/IIoT umbrella
- @concepts/wireless-pentest.md — RF access vs safety-fieldbus crypto
- @concepts/6g-cps-closed-loop-security.md — CPS wireless budgets
- @sources/arxiv-2606-22939-citadel-csi-jamming-iiot.md — IIoT RF jamming defense (adjacent)

## Raw Concept

Functional safety historically treated the network as a **black channel** (CRC, sequence numbers). Draft **prEN 50742** and similar rules push **cryptographic security into the safety path**, changing capacity, latency tails, and attacker economics on industrial wireless.

## Narrative

### Why it matters for security work

- **Availability as a safety property:** crypto payload bloat can cut IO-Link Wireless devices/track from 8→2 — an attacker who forces higher SRSL modes or noisy RF may trigger watchdog trips / capacity exhaustion without classic "break crypto"
- **Transport choice:** private **5G** can beat Wi-Fi 6 on **worst-case** determinism even when Wi-Fi wins average latency [Source: arxiv-2607.15840]
- **Scope notes for OT pentests:** document SRSL level, cycle time, and wireless medium; "wireless" here is fieldbus safety, not WPA cracking

### Practitioner checklist

1. Inventory safety vs non-safety wireless segments
2. Measure **device-count headroom** under target SRSL, not only crypto ms
3. Prefer deterministic campus 5G for safety functions when watchdogs are tight
4. Map findings to IEC 62443 + prEN 50742 language for client reports

## Snippets

See source page for abstract quote on 8→2 device collapse.
