---
title: Endpoint Detection and Response (EDR)
type: concept
tags: [edr, xdr, endpoint-security, soc, blue-team, detection]
keywords: [edr, xdr, endpoint detection, crowdstrike, cybereason, sentinelone, telemetry]
related:
  - concepts/soc-operations.md
  - concepts/incident-response.md
  - concepts/malware-analysis.md
  - concepts/av-edr-bypass.md
  - concepts/threat-hunting.md
  - entities/tools/sysmon.md
  - concepts/ransomware.md
  - sources/edr-tools-overview.md
  - sources/ransomware-investigation-runbook.md
maturity: draft
created: 2026-05-16
updated: 2026-05-17
---

## Relations

- @concepts/soc-operations.md
- @concepts/incident-response.md
- @concepts/malware-analysis.md
- @concepts/av-edr-bypass.md
- @concepts/threat-hunting.md
- @entities/tools/sysmon.md
- @concepts/ransomware.md
- @sources/edr-tools-overview.md
- @sources/ransomware-investigation-runbook.md

## Raw Concept

Stub created during the BlueTeam Kit 26-PDF ingest (2026-05-16). Anchored by the corpus's
*EDR tools* survey and *ransomware investigation* runbook. The wiki had an offensive
@concepts/av-edr-bypass.md but no defensive EDR page.

## Narrative

**EDR** = continuous endpoint telemetry collection (process trees, file and registry writes,
network connections, loaded modules) plus detection, investigation, and response capability —
remote host isolation, process termination, and memory capture. It shortens a SOC's
mean-time-to-detect (MTTD) and mean-time-to-respond (MTTR) and is the primary data source for
ransomware and lateral-movement investigations (see @concepts/incident-response.md and
@concepts/soc-operations.md).

**XDR** extends the same model across network, identity, and cloud telemetry. Leading
platforms include CrowdStrike Falcon, Cybereason, Microsoft Defender for Endpoint, and
SentinelOne. The offensive counterpart — evading these sensors — is covered in
@concepts/av-edr-bypass.md, and EDR telemetry is a core input to @concepts/malware-analysis.md.
