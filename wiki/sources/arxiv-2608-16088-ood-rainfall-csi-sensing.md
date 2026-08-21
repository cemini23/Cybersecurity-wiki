---
title: "OOD — Rainfall Sensing via Mobile Communication Signals / PMN-RainSense (arXiv 2608.16088)"
type: source
tags: [source, arxiv, ood, meteorology, wireless-sensing, csi, isac]
keywords: [2608.16088, PMN-RainSense, rainfall sensing, CSI, sub-6 GHz, ISAC, Doppler, meteorology]
related:
  - concepts/airkey-wifi-acoustic-pin-sidechannel.md
  - sources/arxiv-2608-06866-ood-dodtrack-wifi-doppler-tracking.md
  - concepts/wireless-pentest.md
maturity: draft
read_status: skimmed
created: 2026-08-21
updated: 2026-08-21
phase_0_verdict: "OOD 2026-08-21 — meteorology/hydrology paper (rainfall sensing), not a pentest paper. No cyber adopt. Steal one sentence: commodity Wi-Fi/LTE CSI is an environmental sensor (pairs AirKey/DoDTrack). Authorized RF lab only — no LIVE/unauthorized rainfall or device sensing."
wire_status: wont_wire
wire_target: "OOD — meteorology; sensing family contrast for AirKey/DoDTrack pages"
---

## Relations

- @concepts/airkey-wifi-acoustic-pin-sidechannel.md — same commodity-CSI sensing family; RF-lab-only framing
- @sources/arxiv-2608-06866-ood-dodtrack-wifi-doppler-tracking.md — DoDTrack indoor Doppler tracking; same physical-layer sensing family
- @concepts/wireless-pentest.md — contrast only (no attack/defense payload)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Rainfall Sensing via Mobile Communication Signals |
| Authors | Zhongqin Wang, J. Andrew Zhang, Kai Wu, Y. Jay Guo (UTS) |
| arXiv | 2608.16088 (13 pp) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.16088-rainfall-sensing-via-mobile-communication-signal.pdf` |
| Retrieved | 2026-08-21 |
| Read status | **skimmed** — OOD |
| Public code | none claimed for cyber adopt |

## Narrative

**PMN-RainSense** uses **sub-6 GHz mobile communication signals** for rainfall sensing with single-antenna deployment: a spectral–temporal CSI compensation method suppresses packet-wise timing/phase distortion, rainfall-sensitive features are extracted from the **delay–Doppler domain**, and Doppler-domain normalization improves cross-link robustness. Controlled Wi-Fi experiments achieve **95.48% three-class classification accuracy** (random forest); **LTE** CSI from cellular base stations over 11 carrier frequencies (0.763–2.68 GHz) yields **MAE 0.25–0.27 mm/h** for rainfall intensity (1-D CNN). Not an attenuation-based approach — sub-6 GHz rain attenuation is only hundredths of a dB.

**Why filed (OOD with one steal):** commodity Wi-Fi/LTE **CSI is an environmental sensor** — the same physical-layer sensing family as AirKey (Wi-Fi CSI + acoustic PIN side channel) and DoDTrack (indoor Doppler tracking). Any future "CSI-as-sensor" cyber work (device detection, occupancy, environmental correlation) sits on this family. **No cyber adopt** — meteorology/hydrology domain; no LIVE/unauthorized rainfall or device sensing; authorized RF lab only.

## Snippets

> Rainfall-correlated Doppler fluctuations serve as the dominant sensing signature … a three-class classification accuracy of 95.48% using a random forest classifier. [Source: arXiv 2608.16088 abstract]
