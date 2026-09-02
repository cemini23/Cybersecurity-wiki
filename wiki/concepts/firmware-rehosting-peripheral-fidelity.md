---
title: "Firmware rehosting peripheral fidelity — reactive modeling for dynamic analysis (K322)"
type: concept
tags: [concept, firmware, embedded, iot, lab-only, k322]
keywords: [firmware rehosting, peripheral modeling, embedded dynamic analysis, IoT pentest lab, hardware emulation]
related:
  - sources/arxiv-2608-29737-reactive-peripheral-firmware-rehosting.md
  - concepts/hardware-id-masking-opsec.md
  - concepts/secure-boot-vs-device-ownership.md
  - concepts/anti-tamper-protection-classes.md
maturity: draft
created: 2026-09-02
updated: 2026-09-02
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K322)"
---

## Relations

- @sources/arxiv-2608-29737-reactive-peripheral-firmware-rehosting.md — reactive peripheral modeling (2608.29737)
- @concepts/secure-boot-vs-device-ownership.md — device trust boundary vs lab rehost fidelity

## Raw Concept

Question: **why does off-chip firmware emulation miss bugs, and what improves fidelity?**

## Narrative

Dynamic analysis of embedded firmware often **rehosts** binary off the original MCU. Missing or oversimplified **peripheral models** break fidelity — code paths diverge from on-device behavior. **Reactive peripheral modeling (K322)** updates peripheral state from firmware I/O to better match hardware coupling.

**Operator steal:** treat rehosting fidelity as an **explicit acceptance criterion** in owned-device firmware labs; do not equate “runs in emulator” with “matches device.” **Authorized hardware lab only.**

## Snippets

> Unfaithful peripherals are a primary reason rehosted firmware diverges from on-device execution. [Source: arXiv 2608.29737, paraphrase]
