---
title: IBM QRadar
type: entity
tags: [siem, soc, log-analysis, ibm, commercial]
keywords: [qradar, ibm qradar, siem, soc, offense, correlation, aql]
related:
  - concepts/siem.md
  - concepts/soc-operations.md
  - entities/tools/splunk.md
  - entities/tools/wazuh.md
  - sources/next-gen-soc-ibm-qradar.md
  - sources/soc-red-blue-team-drills.md
maturity: draft
created: 2026-05-16
updated: 2026-05-16
---

## Relations

- @concepts/siem.md
- @concepts/soc-operations.md
- @entities/tools/splunk.md
- @entities/tools/wazuh.md
- @sources/next-gen-soc-ibm-qradar.md
- @sources/soc-red-blue-team-drills.md

## Raw Concept

Stub created during the BlueTeam Kit 26-PDF ingest (2026-05-16). Anchored by *Building a
Next-Gen SOC with IBM QRadar* (Packt, 2023) and used as the detection platform in the
corpus's SOC drill notes.

## Narrative

IBM QRadar is a commercial SIEM platform — it aggregates security telemetry, correlates
events into **offenses**, and applies analytics and machine learning for detection and
reporting. It has been a long-standing leader in the SIEM market segment. Detection content
is expressed in QRadar's query language (AQL) and rule engine. Compare @entities/tools/splunk.md
and the FOSS @entities/tools/wazuh.md; see @concepts/siem.md for the category and
@concepts/soc-operations.md for the SOC context.
