---
title: "eLearnSecurity Certified Threat Hunting Introduction PT 1"
type: source
tags: [cybersecurity, joas-corpus, threat-hunting, deep-read]
keywords: [threat hunting, hypothesis hunting, intel-based, IoC, IoA, STIX, TAXII, IR, Joas]
related:
  - concepts/threat-hunting.md
  - entities/people/joas-a-santos.md
  - entities/vendors/elearnsecurity.md
  - concepts/incident-response.md
  - concepts/threat-intelligence.md
maturity: validated
created: 2026-05-12
updated: 2026-08-03
read_status: deep-read
---

## Relations

- @concepts/threat-hunting.md
- @entities/people/joas-a-santos.md
- @entities/vendors/elearnsecurity.md
- @concepts/incident-response.md
- @concepts/threat-intelligence.md

## Raw Concept

- **Title:** Threat Hunting Introduction PT.1
- **Author:** Joas Antonio (Joas A Santos)
- **Type:** 59-page bilingual (EN/PT) intro deck — *not* a full eLearnSecurity CTH exam dump; title references certified-threat-hunting track as context
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/elearnsecurity-cth-intro-pt1.pdf` (archived 2026-08-03; Drive ID retained in prior revisions)
- **Retrieved:** 2026-05-12; deep-read 2026-08-02
- **Read status:** deep-read

## Narrative

Introduces threat hunting as **human-driven search for unknowns** beyond SIEM/EDR alerts. Key frames:

1. **Data fertility first** — hunting needs enterprise telemetry already collecting; no data → no hunt program
2. **Types of hunting**
   - **Intel-based** — start from threat intel / IoCs
   - **Hypothesis hunting** — proactive library aligned to **MITRE ATT&CK**; uses IoAs/TTPs; monitor behavior patterns before damage
   - **Custom / situational** — customer requirements, geopolitical triggers; may blend intel + hypothesis using IoA and IoC
3. **Structured / unstructured / situational** deeper investigations from a hypothesis or trigger
4. **Career entry** — barrier relatively low if you have endpoint/network/security telemetry and curiosity; skill up Python/Go/Perl for autonomy
5. **IR six-step framing** (prep → … → recovery) as adjacent discipline; hunting feeds IR
6. **IoC vs IoA** — IoC forensic artifacts; IoA focuses on attacker behaviors/TTPs (closer to hypothesis hunting)
7. **STIX/TAXII** resource pointers for intel exchange
8. **Lab pointers** — ActiveCM threat-hunting labs, BlueTeam Labs Online, YouTube lab builds

Synthesizes cleanly into existing @concepts/threat-hunting.md hypothesis-driven model. [CONFIRMED — PDF deep-read]

## Snippets

```text
Hypothesis hunting (p.9):
- Proactive model using a threat hunting library
- Aligned with MITRE ATT&CK + global detection playbooks
- Uses IoAs and TTPs; identify actors by environment/domain/behaviors
- Monitor activity patterns to detect/isolate before damage
```

[Source: elearnsecurity-cth-intro-pt1.pdf p.9]

```text
Data fertility (p.3): successful hunting program requires enterprise security system
already collecting data — telemetry is the fuel; hunters complement SIEM/EDR automation
```

[Source: elearnsecurity-cth-intro-pt1.pdf p.3]
