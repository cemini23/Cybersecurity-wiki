---
title: RF fingerprint temperature drift
type: concept
tags: [concept, wireless, rf-fingerprint, authentication]
keywords: [RFFP, thermal drift, device auth, 2607.25070]
related:
  - sources/arxiv-2607-25070-rffi-device-temperature.md
  - concepts/rf-fingerprint-probe-point-benchmark.md
  - concepts/wireless-pentest.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-07-30
updated: 2026-07-30
---

## Relations

- @sources/arxiv-2607-25070-rffi-device-temperature.md
- @concepts/rf-fingerprint-probe-point-benchmark.md
- @concepts/wireless-pentest.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

Hardware RF fingerprints shift with device temperature — classifiers that ignore T fail under unseen thermal conditions.

## Narrative

Pair with probe-point sensitivity: enrollment must capture temperature + RX geometry. Attacker can heat/cool a device to push it off the enrolled manifold. Defender: temperature-conditioned models + log T at verify. [CONFIRMED abstract]
