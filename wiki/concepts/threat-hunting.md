---
title: Threat Hunting
type: concept
tags: [proactive, blue-team, detection]
keywords: [threat hunting, hunt, kibana, elastic, splunk]
related:
  - concepts/soc-operations.md
  - concepts/incident-response.md
  - entities/frameworks/mitre-attack.md
  - sources/elearnsecurity-certified-threat-hunting-introduction-pt-1.md
  - sources/malware-hunting-threat-hunter-overview-1.md
  - entities/people/joas-a-santos.md
  - concepts/malware-analysis.md
  - concepts/osint-for-cybersecurity.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
---

## Relations

- @concepts/soc-operations.md
- @concepts/incident-response.md
- @entities/frameworks/mitre-attack.md
- @sources/elearnsecurity-certified-threat-hunting-introduction-pt-1.md
- @sources/malware-hunting-threat-hunter-overview-1.md
- @entities/people/joas-a-santos.md
- @concepts/malware-analysis.md
- @concepts/osint-for-cybersecurity.md

## Raw Concept

Two corpus PDFs anchor.

## Narrative

Threat Hunting = proactive search for adversary activity in environments where no alert has fired. Hypothesis-driven: "if APT29 were already inside, what would I expect to see in scheduled tasks / WMI subscriptions / unusual parent-child process trees?" Pyramid of Pain (David Bianco) is the canonical mental model — hash IOCs are easy to dodge, TTPs are not. Hunting workflows pair tightly with MITRE ATT&CK (the technique tree) and the SIEM (query substrate).
