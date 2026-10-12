---
title: "Secrets in preamble: practical and robust PHY information hiding for Wi-Fi"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.13367, k421]
related:
  - concepts/phy-layer-covert-channel-wifi-preamble.md
  - concepts/inference-time-covert-agentic-communication.md
  - concepts/physical-layer-deception-enterprise-wifi-auth.md
  - concepts/spectral-whitening-wireless-protocol-id.md
maturity: draft
read_status: read
created: 2026-10-12
updated: 2026-10-12
phase_0_verdict: "REFERENCE 2026-10-12 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K421)"
---

## Relations

## Relations

- @concepts/phy-layer-covert-channel-wifi-preamble.md
- @concepts/inference-time-covert-agentic-communication.md
- @concepts/physical-layer-deception-enterprise-wifi-auth.md
- @concepts/spectral-whitening-wireless-protocol-id.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Secrets in preamble: practical and robust PHY information hiding for Wi-Fi |
| arXiv | 2610.13367 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.13367-secrets-in-preamble-practical-and-robust-phy-inf.pdf |
| Retrieved | 2026-10-12 |
| Read status | read |

## Narrative

**K421 — a covert channel below the MAC, and its defensive dual.** Physical-layer information hiding embeds secrets inside PHY waveforms without breaking the primary link, enabling **covert communication, PHY steganography, and watermarking**. Prior Wi-Fi schemes were limited by low **steganographic capacity** and poor **robustness** to environmental change. This work hides the secret in the **legacy short training field (L-STF)** of the Wi-Fi preamble and **preserves the L-STF autocorrelation structure**, so **packet detection and coarse frequency-offset compensation** — which a receiver depends on — are not disturbed. A pair of **neural networks** learns the embedding and extraction rules.

Measured on a hardware prototype (**USRP B210**) in indoor *and* outdoor conditions, it reliably embeds **46 secret bits per Wi-Fi packet** across diverse channels, with the design explicitly targeting robustness against interference (tested at 1% and 10% of received signal power) and channel variation; secret-bit-error rate is the training loss, with BCH coding discussed as recovery. No code release (MATLAB/Simulink + SDR). Operator steal, two-sided: a **46-bit per-packet PHY covert channel survives real channels**, which is both an **exfil path invisible to upper-layer inspection** and a **watermark for transmitter authentication**. Authorized RF lab only. **No embedding recipes or code in wiki.**

## Snippets

> See arXiv 2610.13367 abstract. [Source: arXiv 2610.13367 (retrieved 2026-10-12)]
