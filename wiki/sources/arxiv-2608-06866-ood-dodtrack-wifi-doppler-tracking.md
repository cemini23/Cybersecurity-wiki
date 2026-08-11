---
title: "OOD — DoDTrack indoor Wi-Fi Difference-of-Doppler tracking (arXiv 2608.06866)"
type: source
tags: [source, arxiv, ood, wireless-sensing, localization]
keywords: [2608.06866, DoDTrack, Doppler, Wi-Fi sensing, indoor tracking, ISAC]
related:
  - concepts/wireless-pentest.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: skimmed
created: 2026-08-11
updated: 2026-08-11
phase_0_verdict: "OOD 2026-08-11 — Wi-Fi Doppler sensing/localization, not WPA/BLE/evil-twin pentest. No cyber adopt."
wire_status: wont_wire
wire_target: "OOD — sensing/localization, not cybersec harness wire"
---

**Briefs:** `briefs/2026-08-11_ood-dodtrack-wifi-doppler-route.md`

## Relations

- @concepts/wireless-pentest.md — contrast only (physical-layer sensing family, no attack/defense payload)
- @concepts/ai-for-cybersecurity.md — contrast only (LLM/sensing adjacency is nil for cyber ops)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | DoDTrack: Indoor Mobile Devices Tracking via Difference-of-Doppler |
| Authors | Zhang, Chen, Yu, Zhang, Wang (SUSTech / CUHK-SZ) |
| arXiv | 2608.06866 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.06866-dodtrack-indoor-mobile-devices-tracking-via-diff.pdf` |
| Retrieved | 2026-08-11 |
| Read status | **skimmed** — OOD |
| Public code | None claimed for cyber adopt |

## Narrative

Uses Difference-of-Doppler (DoD) across distributed receive antennas sharing one oscillator to reconstruct an active Wi-Fi device's indoor trajectory without prior starting position. Conjugate multiplication cancels CFO/SFO, STFT peak detection yields DoDs, and an EKF + gradient-descent starting-position search solves an MMSE trajectory problem. Median tracking error 0.34 m over a 6 m × 6 m area on USRP-X310. Integrated sensing and communication (ISAC) design, **not** a Wi-Fi security/pentest paper — no WPA/BLE/evil-twin, RF-jamming, or SIGINT tradecraft relevant to `wireless-pentest`. Kept as a stub to block daily-digest re-fetch; route brief notes possible physical-security value (device-tracking via passive Doppler) only if a client engagement explicitly covers it.
