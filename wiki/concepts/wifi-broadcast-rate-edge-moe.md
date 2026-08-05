---
title: Wi-Fi broadcast rate cap vs collaborative edge MoE
type: concept
tags: [concept, wireless, wifi, edge-llm]
keywords: [802.11 broadcast, 54 Mbps, MoE, edge inference, 2608.02341]
related:
  - sources/arxiv-2608-02341-wifi-broadcast-rate-edge-moe.md
  - concepts/wireless-pentest.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/network-security.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-08-05
updated: 2026-08-05
---

## Relations

- @sources/arxiv-2608-02341-wifi-broadcast-rate-edge-moe.md
- @concepts/wireless-pentest.md
- @concepts/local-abliterated-llm-pentest-stack.md
- @concepts/network-security.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

802.11 broadcast is rate-capped (~54 Mbps) even on modern PHY — a forgotten bottleneck when spreading MoE experts across WLAN edge nodes.

## Narrative

Friend/local multi-GPU is usually PCIe/NVLink or wired; if anyone shards experts over Wi-Fi, expect the broadcast cap before GPU saturation. Same ceiling matters for noisy wireless lab fabrics. Not a new crack technique — infrastructure constraint. [CONFIRMED abstract]
