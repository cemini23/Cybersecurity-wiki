---
title: "OOD — Subcarrier-aware Wi-Fi respiratory monitoring (arXiv 2608.25612)"
type: source
tags: [source, arxiv, ood, healthcare, wireless-sensing, csi, isac]
keywords: [2608.25612, respiratory monitoring, CSI, subcarrier, Wi-Fi sensing, breathing-pause detection, home healthcare]
related:
  - concepts/airkey-wifi-acoustic-pin-sidechannel.md
  - concepts/wireless-pentest.md
maturity: draft
read_status: skimmed
created: 2026-08-28
updated: 2026-08-28
phase_0_verdict: "OOD 2026-08-28 — home-healthcare Wi-Fi CSI respiratory monitoring, not a pentest paper. No cyber adopt. Steal one sentence: commodity Wi-Fi CSI is a sensor (pairs rainfall CSI / AirKey). Authorized RF lab only — no LIVE/unauthorized eavesdropping or breath sensing."
wire_status: wont_wire
wire_target: "OOD — healthcare; commodity-CSI-as-sensor family contrast for AirKey/DoDTrack pages"
---

## Relations

- @concepts/airkey-wifi-acoustic-pin-sidechannel.md — same commodity-CSI sensing family; RF-lab-only framing
- @concepts/wireless-pentest.md — contrast only (no attack/defense payload)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | A Subcarrier-Aware Approach for Robust Respiratory Monitoring with Commodity Wi-Fi |
| Authors | Pei Tang, Yunpeng Ge, Ivan Wang-Hei Ho (HKU) |
| arXiv | 2608.25612 (~20 pp) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.25612-a-subcarrier-aware-approach-for-robust-respirato.pdf` |
| Retrieved | 2026-08-28 |
| Read status | **skimmed** — OOD |
| Public code | none claimed for cyber adopt |

## Narrative

**Problem:** Wi-Fi sensing is attractive for contact-free home-healthcare respiratory monitoring, but most methods treat CSI subcarriers **uniformly**, ignoring their heterogeneous response to breathing motion. The paper proposes a **subcarrier-aware** framework that characterizes **subcarrier-dependent respiratory sensitivity** and selects informative subcarriers; an **unsupervised clustering-based** breathing-estimation method then runs robustly. Reported: **97% breathing-rate estimation accuracy**, MAE reduced by **0.45 bpm** vs baselines; extended **breathing-pause detection** via an amplitude-attenuation threshold (MAE 1.6 bpm under pauses).

**Why filed (OOD with one steal):** this is a healthcare application of **commodity Wi-Fi CSI as a sensor** — the same physical-layer sensing family as AirKey (Wi-Fi CSI + acoustic PIN side channel), DoDTrack (indoor Doppler tracking), and PMN-RainSense (rainfall CSI). **No cyber adopt** — healthcare/physiological domain; no LIVE/unauthorized eavesdropping or breath sensing; authorized RF lab only.

## Snippets

> Conventional approaches typically treat CSI subcarriers uniformly, neglecting their heterogeneous responses to breathing motions … the proposed method achieves 97% breathing rate estimation accuracy and reduces the MAE by 0.45 bpm compared with baseline methods. [Source: arXiv 2608.25612 abstract]
