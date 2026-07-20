---
title: Converging safety and security — IO-Link Wireless + OPC UA over 5G under prEN 50742 (arXiv 2607.15840)
type: source
tags: [source, arxiv, ot, iiot, industrial-wireless, functional-safety, pren-50742]
keywords: [2607.15840, IO-Link Wireless, OPC UA, private 5G, Wi-Fi 6, prEN 50742, SRSL, ETFA]
related:
  - concepts/industrial-safety-security-convergence.md
  - concepts/network-security.md
  - concepts/wireless-pentest.md
  - concepts/6g-cps-closed-loop-security.md
  - sources/arxiv-2606-22939-citadel-csi-jamming-iiot.md
maturity: draft
read_status: read
created: 2026-07-20
updated: 2026-07-20
phase_0_verdict: "REFERENCE 2026-07-20 — empirical OT measurement paper; no public code artifact; steal SRSL capacity/latency claims"
---

**Briefs:** `briefs/2026-07-20_industrial-safety-security-pren-50742-handoff.md`

## Relations

- @concepts/industrial-safety-security-convergence.md — synthesis
- @concepts/network-security.md — OT/IIoT wireless control chain
- @concepts/wireless-pentest.md — contrast: industrial fieldbus safety, not WLAN crack tradecraft
- @concepts/6g-cps-closed-loop-security.md — adjacent CPS wireless safety budgets

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Converging Safety and Security: IO-Link Wireless and OPC UA over 5G under prEN 50742 |
| Authors | Henry Beuster, Thomas Doebbert, Gerd Scholl |
| Affiliation | Helmut-Schmidt-University; Jungheinrich AG |
| Venue | Accepted ETFA 2026 |
| arXiv | 2607.15840 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.15840-converging-safety-and-security-io-link-wireless.pdf` |
| Retrieved | 2026-07-20 |
| Read status | **read** |
| Public code | None |

## Narrative

Draft **prEN 50742** requires cryptographic security **inside** safety-critical industrial communication (not black-channel CRC-only). Authors measure a full chain: IO-Link Wireless Safety device → OPC UA backbone → PLC, across Ethernet / Wi-Fi 6 / private 5G at different Safety-Related Security Levels (SRSLs).

### Headline results [CONFIRMED from paper]

| Finding | Detail |
|---------|--------|
| Crypto CPU cost | Negligible vs frame time |
| Real cost | **Payload expansion** from crypto wrappers |
| IOLW capacity | Max devices/track **8 → 2** (short 5 ms cycle) under highest SRSL |
| Wi-Fi 6 vs 5G | Wi-Fi 6 lower average latency; **private 5G** better worst-case determinism for safety watchdogs |

### Steal for OT engagements / purple

1. When scoping wireless safety systems, budget **device-count collapse** under mandated crypto — not just latency averages
2. Prefer private 5G over unlicensed Wi-Fi 6 for safety functions if watchdog margins matter
3. Treat prEN 50742 / SRSL as a regulatory pivot that changes attack surface (more crypto, fewer nodes, different timing DoS)

### Phase-0

| Gate | Status |
|------|--------|
| License / code | N/A — paper only |
| Verdict | **REFERENCE** |

## Snippets

> "while cryptographic execution time is negligible, the resulting frame payload expansion severely restricts wireless fieldbus capacity, reducing the maximum number of devices per IO-Link Wireless track from 8 to 2."
[Source: arxiv-2607.15840 abstract]
