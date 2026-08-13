---
title: Can Machine Learning Break Wi-Fi Privacy? (arXiv 2606.25788)
type: source
tags: [source, arxiv, wifi, privacy, mac-randomization, ml]
keywords: [2606.25788, Puig, MAC de-randomization, HT capabilities, DBSCAN]
related:
  - concepts/hardware-id-masking-opsec.md
  - concepts/wireless-pentest.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — paper; no clone"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-id-masking-opsec.md
- @concepts/wireless-pentest.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Can Machine Learning Break Wi-Fi Privacy? A Study on MAC Address Randomization |
| Authors | Puig, Michaelides, Pintor, Bellalta, Wilhelmi (UPF / University of Cagliari) |
| arXiv | 2606.25788 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2606.25788-ml-mac-address-randomization.pdf` |
| Retrieved | 2026-08-12 |

## Narrative

2026 unsupervised clustering study (K-Means / DBSCAN / OPTICS) on 22 devices / 6 vendors. Bitwise HT-capabilities decomposition + simulated RSSI; DBSCAN global accuracy up to **89.6%**. Notes IEEE 802.11aq randomization for pre-association probes; sequence numbers omitted because they no longer increment predictably across bursts. RSSI in this paper is simulated (dataset lacked environment). [CONFIRMED abstract + caveats in §I–II]

OPSEC steal: even after SN-based tricks aged out, capability IEs + RF spatial features still cluster devices. Flag simulated-RSSI when citing the 89.6% number. [TENTATIVE on field RSSI; CONFIRMED on HT-bit result in their setup]

## Snippets

> "This suggests that the existing MAC randomization solutions are insufficient and underscores the need for enhancing privacy within Wi-Fi standardization."
[Source: arxiv-2606.25788 abstract]
