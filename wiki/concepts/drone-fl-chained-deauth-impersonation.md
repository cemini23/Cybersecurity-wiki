---
title: Drone FL chained deauth → impersonation
type: concept
tags: [concept, wireless, federated-learning, drones, availability]
keywords: [802.11 deauth, Flower FL, credential impersonation, edge intelligence, 2607.20280]
related:
  - sources/arxiv-2607-20280-drone-fl-chained-attacks.md
  - concepts/wireless-pentest.md
  - concepts/industrial-safety-security-convergence.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-07-24
updated: 2026-07-24
---

## Relations

- @sources/arxiv-2607-20280-drone-fl-chained-attacks.md
- @concepts/wireless-pentest.md
- @concepts/industrial-safety-security-convergence.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

Availability attack at Wi-Fi creates a join vacancy that single-factor FL auth happily fills with an impersonator.

## Narrative

```
deauth legitimate drone → extract/reuse credentials → join as client → poison/contribute updates
```

Physical Pi/Jetson Flower validation. Defender: continuous/client-bound auth, not join-once; monitor for abrupt client identity reuse after RF disruption. [CONFIRMED abstract]
