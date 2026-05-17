---
title: Splunk
type: entity
tags: [siem, soc, log-analysis, detection-engineering, commercial]
keywords: [splunk, spl, siem, search processing language, soc, detection]
related:
  - concepts/siem.md
  - concepts/soc-operations.md
  - entities/tools/qradar.md
  - entities/tools/wazuh.md
  - sources/100-splunk-queries-soc-analyst.md
  - sources/splunk-commands-reference.md
  - sources/splunk-siem-soc2-use-cases.md
maturity: draft
created: 2026-05-16
updated: 2026-05-16
---

## Relations

- @concepts/siem.md
- @concepts/soc-operations.md
- @entities/tools/qradar.md
- @entities/tools/wazuh.md
- @sources/100-splunk-queries-soc-analyst.md
- @sources/splunk-commands-reference.md
- @sources/splunk-siem-soc2-use-cases.md

## Raw Concept

Stub created during the BlueTeam Kit 26-PDF ingest (2026-05-16). Three corpus PDFs are
Splunk-specific (a 100+ detection-query collection, an SPL command reference, and 24
SOC-2-mapped use cases), and Splunk is referenced across the SOC corpus — warranting a
dedicated tool entity.

## Narrative

Splunk is a commercial SIEM and machine-data analytics platform — it ingests, indexes, and
searches logs and events at scale using **SPL** (Search Processing Language). In SOC work it
underpins detection engineering, alerting, dashboards, and threat hunting. Detection content
is written as SPL searches; the corpus's query collections are essentially reusable SPL
detection libraries. Splunk competes with @entities/tools/wazuh.md (FOSS) and
@entities/tools/qradar.md (IBM) in the SIEM space — see @concepts/siem.md for the platform
category and @concepts/soc-operations.md for where it sits in a SOC. [CONFIRMED]
