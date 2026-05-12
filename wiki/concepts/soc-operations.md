---
title: SOC Operations
type: concept
tags: [soc, blue-team, siem, detection]
keywords: [soc, siem, monitoring, wazuh, elk, splunk]
related:
  - concepts/ai-for-cybersecurity.md
  - concepts/incident-response.md
  - concepts/purple-team-operations.md
  - concepts/threat-hunting.md
  - concepts/zero-trust.md
  - entities/people/joas-a-santos.md
  - entities/tools/wazuh.md
  - sources/100-security-operation-center-tools.md
  - sources/interview-question-tips-pentest-red-team-appsec-and-blue-team.md
  - sources/low-cost-soc-tools-2.md
  - sources/low-cost-soc.md
  - sources/red-team-and-blue-team-labs-and-ctf.md
  - sources/security-operation-center-40-tools.md
  - sources/security-operation-center-and-analysis.md
  - sources/security-operation-center-open-source-pt-en.md
  - sources/security-operation-center-open-source.md
  - sources/security-operation-center-operations-development.md
  - sources/security-operation-center-study-and-career-2022.md
  - sources/soc-analyst-career.md
  - sources/soc-open-source-tools.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
---

## Relations

- @concepts/ai-for-cybersecurity.md
- @concepts/incident-response.md
- @concepts/purple-team-operations.md
- @concepts/threat-hunting.md
- @concepts/zero-trust.md
- @entities/people/joas-a-santos.md
- @entities/tools/wazuh.md
- @sources/100-security-operation-center-tools.md
- @sources/interview-question-tips-pentest-red-team-appsec-and-blue-team.md
- @sources/low-cost-soc-tools-2.md
- @sources/low-cost-soc.md
- @sources/red-team-and-blue-team-labs-and-ctf.md
- @sources/security-operation-center-40-tools.md
- @sources/security-operation-center-and-analysis.md
- @sources/security-operation-center-open-source-pt-en.md
- @sources/security-operation-center-open-source.md
- @sources/security-operation-center-operations-development.md
- @sources/security-operation-center-study-and-career-2022.md
- @sources/soc-analyst-career.md
- @sources/soc-open-source-tools.md


## Raw Concept

11+ corpus PDFs scope into SOC operations.

## Narrative

Security Operations Center = the people + processes + tooling that detect, triage, and respond to security events 24×7. Tiered model: Tier-1 (alert triage), Tier-2 (incident analysis), Tier-3 (threat hunting + IR + advanced reverse engineering). Tooling stack: SIEM (Wazuh / Splunk / Elastic / Sentinel / QRadar), SOAR (Cortex XSOAR / Tines), EDR (CrowdStrike / Defender for Endpoint / SentinelOne), threat-intel (MISP / OpenCTI). The corpus's *Low Cost SOC* PDFs explicitly cover the FOSS path: Wazuh + Elastic + TheHive + MISP + Velociraptor. See @entities/tools/wazuh.md and @concepts/threat-hunting.md.
