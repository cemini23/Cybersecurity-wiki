---
title: Purple Team Operations
type: concept
tags: [purple-team, collaboration, detection-engineering]
keywords: [purple team, red blue collaboration, detection engineering]
related:
  - concepts/red-team-operations.md
  - concepts/adversary-emulation.md
  - concepts/soc-operations.md
  - entities/tools/caldera.md
  - entities/tools/wazuh.md
  - sources/purple-team-lab-01-wazuh-and-win2016.md
  - entities/people/joas-a-santos.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
---

## Relations

- @concepts/red-team-operations.md
- @concepts/adversary-emulation.md
- @concepts/soc-operations.md
- @entities/tools/caldera.md
- @entities/tools/wazuh.md
- @sources/purple-team-lab-01-wazuh-and-win2016.md
- @entities/people/joas-a-santos.md

## Raw Concept

Anchored by Purple Team Lab 01 - Wazuh and Win2016.pdf.

## Narrative

Purple team = red + blue working **together** in real time. Where red team operations test the blue team blindly, a purple-team engagement is collaborative: attackers fire a known TTP, defenders watch + tune detections, both sides iterate until coverage is achieved. The corpus's hands-on lab (Wazuh + Windows 2016) is a typical entry point — Wazuh as SIEM, a Windows victim, MITRE ATT&CK technique catalog as the test menu. See @concepts/adversary-emulation.md for the technique-selection side and @entities/tools/wazuh.md for the SIEM side. [CONFIRMED]
