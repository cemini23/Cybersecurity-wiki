---
title: "OOD — EvoOMG Wi-Fi 7/8 MLO multi-agent MAC guidance (arXiv 2607.07045)"
type: source
tags: [source, arxiv, ood, wireless, wifi7, mlo, multi-agent-rl]
keywords: [2607.07045, EvoOMG, multi-link operation, Wi-Fi 7, Wi-Fi 8, MADDPG, NS-3]
related:
  - sources/arxiv-ood-wireless-ofdm-isac-2607.14775.md
  - sources/arxiv-ood-wireless-uav-sensing-2607.14778.md
  - sources/arxiv-ood-wireless-localization-survey-2607.14938.md
  - concepts/wireless-pentest.md
  - concepts/network-security.md
maturity: draft
read_status: skimmed
created: 2026-07-20
updated: 2026-07-31
phase_0_verdict: "OOD 2026-07-20 — WLAN MAC/throughput RL for legacy+MLO coexistence; not wireless pentest. Brief-only; no adopt."
wire_status: wont_wire
wire_target: "OOD — not cybersec harness wire"
---

**Briefs:** `briefs/2026-07-20_ood-wireless-evoomg-mlo-route.md`

## Relations

- @concepts/network-security.md
- Sibling OOD wireless digest false-positives (@sources/arxiv-ood-wireless-ofdm-isac-2607.14775.md and kin)
- @concepts/wireless-pentest.md — contrast: this is scheduler/RL, not RF attack tradecraft

## Raw Concept

| Field | Value |
|-------|-------|
| Title | EvoOMG: An Evolution-Oriented Multi-Agent Guidance Framework for Heterogeneous Legacy-and-MLO Wi-Fi Networks |
| Authors | Junjie Wu, Lingjian Zhou, Zerui Shao, Yi Zou, Tianrui Li, Yi Zhang, Ziyuan Yang |
| arXiv | 2607.07045 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.07045-evoomg-an-evolution-oriented-multi-agent-guidanc.pdf` |
| Retrieved | 2026-07-20 |
| Read status | **skimmed** — OOD |
| Public code | None found at ingest |

## Narrative

Wi-Fi 7/8 **multi-link operation (MLO)** coexistence paper: multi-agent RL that stages contention-then-aggregation guidance so legacy single-link and MLO STAs share airtime. Evaluated in NS-3 vs EDCA / MADDPG baselines. **Not** WPA/BLE/evil-twin pentest content.

Stub exists so the daily digest skips re-fetch; wireless `arxiv_query` tightened to ANDNOT MLO/throughput-scheduler noise.
