---
title: SIEM (Security Information and Event Management)
type: concept
tags: [siem, soc, blue-team, detection, log-management]
keywords: [siem, log management, correlation, detection engineering, splunk, qradar, wazuh]
related:
  - concepts/soc-operations.md
  - concepts/threat-hunting.md
  - entities/tools/splunk.md
  - entities/tools/qradar.md
  - entities/tools/wazuh.md
  - sources/100-splunk-queries-soc-analyst.md
  - sources/next-gen-soc-ibm-qradar.md
  - sources/linux-log-analysis-wazuh.md
  - sources/open-source-soc-guide.md
  - sources/soc-log-types.md
  - sources/splunk-commands-reference.md
  - sources/splunk-siem-soc2-use-cases.md
  - sources/threat-hunting-101.md
  - entities/tools/sysmon.md
maturity: draft
created: 2026-05-16
updated: 2026-05-17
---

## Relations

- @concepts/soc-operations.md
- @concepts/threat-hunting.md
- @entities/tools/splunk.md
- @entities/tools/qradar.md
- @entities/tools/wazuh.md
- @sources/100-splunk-queries-soc-analyst.md
- @sources/next-gen-soc-ibm-qradar.md
- @sources/linux-log-analysis-wazuh.md
- @sources/open-source-soc-guide.md
- @sources/soc-log-types.md
- @sources/splunk-commands-reference.md
- @sources/splunk-siem-soc2-use-cases.md
- @sources/threat-hunting-101.md
- @entities/tools/sysmon.md

## Raw Concept

Stub created during the BlueTeam Kit 26-PDF ingest (2026-05-16). The corpus is SIEM-heavy —
Splunk query/command collections, a QRadar SOC book, and log-type / log-analysis references
— but no dedicated SIEM concept page existed; @concepts/soc-operations.md only mentioned it
in passing.

## Narrative

**SIEM** = the platform layer that centralizes log and event collection from disparate
sources (endpoints, servers, firewalls, IDS/IPS, cloud), normalizes and correlates them, and
surfaces alerts for SOC triage. It is the analytic backbone of a SOC (see
@concepts/soc-operations.md).

Core SIEM pipeline: log ingestion → parsing / normalization → correlation rules → alerting →
dashboards → threat hunting (see @concepts/threat-hunting.md). Detection content is written
in platform-specific query languages — SPL for Splunk, AQL for QRadar, KQL for Microsoft
Sentinel.

Common platforms: Splunk (@entities/tools/splunk.md), IBM QRadar (@entities/tools/qradar.md),
Wazuh (@entities/tools/wazuh.md, FOSS), Elastic, and Microsoft Sentinel. The corpus's
*Open-Source SOC* and *Low Cost SOC* material favours the FOSS path (Wazuh + Elastic). The
12 log types a SIEM ingests are catalogued in the corpus's *SOC logs* reference.
