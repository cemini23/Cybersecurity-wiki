---
title: Wi-Fi broadcast rate cap for edge MoE inference (arXiv 2608.02341)
type: source
tags: [source, arxiv, wireless, wifi, edge-llm, moe]
keywords: [2608.02341, Wi-Fi broadcast, 54 Mbps, 802.11, edge MoE, NCCL]
related:
  - concepts/wifi-broadcast-rate-edge-moe.md
  - concepts/wireless-pentest.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/network-security.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-08-05
updated: 2026-08-05
phase_0_verdict: "REFERENCE 2026-08-05 — no public code; Wi-Fi MAC/policy + edge inference"
wire_status: wont_wire
wire_target: "REFERENCE — no clone"
---

**Briefs:** `briefs/2026-08-05_k241-wifi-broadcast-edge-moe-prod.md`

## Relations

- @concepts/wifi-broadcast-rate-edge-moe.md
- @concepts/wireless-pentest.md
- @concepts/local-abliterated-llm-pentest-stack.md
- @concepts/network-security.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Broadcast Rate Limits in Wi-Fi: A Forgotten Bottleneck for Collaborative Edge LLM Inference |
| Authors | Liujianfu Wang, Yuyang Du, Shiqi Xu, Soung Chang Liew |
| arXiv | 2608.02341 |
| Code | none located |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.02341-broadcast-rate-limits-in-wi-fi-a-forgotten-bottl.pdf` |
| Retrieved | 2026-08-05 |

## Narrative

Distributed MoE on cheap edge nodes needs one-to-many embedding dispatch. UDP broadcast + timeout retransmission beats sequential unicast (NCCL/TCP) **~1.4×** on wired 8-node. On Wi-Fi, IEEE **802.11 caps broadcast at 54 Mbps** regardless of PHY — legacy control-traffic policy. NS-3 shows much higher optimal rates at 1–5 m. [CONFIRMED abstract]

### Steal

1. Edge/lab multi-node LLM over WLAN: broadcast rate cap is a real bottleneck (not just SNR)
2. Wired UDP broadcast ≠ Wi-Fi broadcast performance
3. Pentest/ops: 54 Mbps broadcast ceiling is a planning constraint for wireless C2/lab fabrics too

## Snippets

> "IEEE 802.11 caps broadcast rates at 54 Mbps regardless of physical-layer capacity — a legacy policy built for sparse control traffic, not edge AI."
[Source: arXiv 2608.02341 abstract]
