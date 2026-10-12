---
title: "Toward lightweight aerial 5G gNBs: a reproducible OAI testbed on commodity ARM"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.05007, k418]
related:
  - concepts/aerial-ran-testbed-pws-broadcast.md
  - concepts/wireless-pentest.md
  - concepts/network-security.md
maturity: draft
read_status: read
created: 2026-10-12
updated: 2026-10-12
phase_0_verdict: "REFERENCE 2026-10-12 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K418)"
---

## Relations

## Relations

- @concepts/aerial-ran-testbed-pws-broadcast.md
- @concepts/wireless-pentest.md
- @concepts/network-security.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Toward lightweight aerial 5G gNBs: a reproducible OAI testbed on commodity ARM |
| arXiv | 2610.05007 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.05007-toward-lightweight-aerial-5g-gnbs-reproducible-o.pdf |
| Retrieved | 2026-10-12 |
| Read status | read |

## Narrative

**K418 — a reproducible open-source RAN testbed, and a public-warning channel on it.** For a battery-powered UAV base station every gram and watt spent on RAN compute competes with flight time, so the design keeps the **5G Core and central unit (CU) on the ground** and flies only the backhaul endpoint, **distributed unit (DU)**, and radio over the **3GPP F1 split**. The measured question: can **commodity ARM** boards run a real **OpenAirInterface (OAI) 5G DU**? With **Raspberry Pi 5** and **Jetson Orin Nano** as DUs, a **USRP B210**, and a commercial handset, Jetson preserves **88.4%** of x86 split-DU Ethernet DL throughput and **87.5-89.0%** across three bearers; **5G/WireGuard** keeps **76.4-77.1%** of each host's wired DL rate. The integrated payload weighs **657.4 g** and draws ~**28 W** under sustained traffic.

A controlled link-adaptation intervention moves split DL from **23.4 to 99.4 Mb/s** as the dominant MCS moves **3 to 26** — the collapse was scheduling/timing, not the platform. The security-relevant artifact is a **PWS-over-F1 patch**: it carries the **Write-Replace Warning** procedure from the ground CU to the remote DU so **SIB8** is scheduled to handsets, giving an area-wide **Public Warning System** emergency broadcast. Repos `github.com/promaaa/oai-cu-du-lab` and `github.com/promaaa/jetson-kernel-sctp`; licence not stated. Operator steal: a **reproducible ARM RAN testbed** lowers the bar to exercise the wireless/emergency-broadcast surface in an authorized lab, and a **PWS channel is a high-integrity target** — it is meant to be believed by every handset in range. Authorized lab only. **No exploit steps in wiki.**

## Snippets

> See arXiv 2610.05007 abstract. [Source: arXiv 2610.05007 (retrieved 2026-10-12)]
