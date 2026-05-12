---
title: Cyber Kill Chain (Lockheed Martin) + Unified Cyber Kill Chain
type: entity
tags: [framework, intrusion-modelling, ordered-phases]
keywords: [lockheed martin, kill chain, unified kill chain, phases, ordered]
related:
  - entities/frameworks/mitre-attack.md
  - concepts/red-team-operations.md
  - concepts/adversary-emulation.md
  - concepts/incident-response.md
  - sources/introducao-ao-mitre-att-ck-e-ao-cyber-kill-chain.md
  - sources/red-team-operations-concepts-1.md
  - entities/people/joas-a-santos.md
maturity: validated
created: 2026-05-12
updated: 2026-05-12
---

## Relations

- @entities/frameworks/mitre-attack.md
- @concepts/red-team-operations.md
- @concepts/adversary-emulation.md
- @concepts/incident-response.md
- @sources/introducao-ao-mitre-att-ck-e-ao-cyber-kill-chain.md
- @sources/red-team-operations-concepts-1.md
- @entities/people/joas-a-santos.md

## Raw Concept

Companion framework to MITRE ATT&CK. Mentioned across the corpus when ordering matters in engagement / incident narratives. The Joas corpus uses the Unified Cyber Kill Chain (Paul Pols, 2017), a 18-phase superset of the original Lockheed Martin chain plus elements of ATT&CK.

## Narrative

Originally proposed by Lockheed Martin (Hutchins, Cloppert, Amin, 2011) as a 7-phase ordered model of network intrusion: Reconnaissance → Weaponization → Delivery → Exploitation → Installation → Command & Control → Actions on Objectives. The model's strength is its **ordered** nature — useful for narrating incidents — but it was criticized as too coarse for modern intrusions that loop through phases multiple times. [CONFIRMED]

**Unified Cyber Kill Chain** (Paul Pols, 2017) extends Lockheed's chain into 18 ordered phases and explicitly maps each phase to MITRE ATT&CK tactics: [Source: Red Team Operations – Concepts #1.pdf]

1. **Reconnaissance** — passive + active target identification
2. **Weaponization** — preparing attack infrastructure
3. **Delivery** — transmitting weaponized payload to target
4. **Social Engineering** — manipulating people into unsafe actions
5. **Exploitation** — vulnerability exploitation → code execution
6. **Persistence** — establishing durable footholds
7. **Defense Evasion** — avoiding detection (AV/EDR, monitoring)
8. **Command & Control (C2)** — communicating with compromised hosts
9. **Pivoting** — tunneling traffic through controlled hosts
10. **Discovery** — local + network enumeration
11. **Privilege Escalation** — gaining higher permissions
12. **Execution** — running attacker-controlled code
13. **Credential Access** — harvesting credentials
14. **Lateral Movement** — moving horizontally across systems
15. **Harvesting** — gathering target data prior to exfiltration
16. **Exfiltration** — removing data from the target network
17. **Impact** — manipulating, disrupting, or destroying systems/data
18. **Objectives** — sociotechnical end-goals of the operation

**ATT&CK vs Kill Chain — when to use which:** Use ATT&CK when the question is "what technique could be used here?" (technique-first). Use Kill Chain when the question is "how did this intrusion unfold?" (story-first). For red team reporting both are typically used together — phases give narrative structure, ATT&CK T-numbers give granular accountability.
