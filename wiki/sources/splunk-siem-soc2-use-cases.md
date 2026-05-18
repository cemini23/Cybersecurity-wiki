---
title: "splunk SOC .pdf"
type: source
tags: [splunk, siem, soc, compliance, soc2]
keywords: [splunk use cases, soc 2 compliance, spl, detection, trust service criteria, rajneesh gupta, audit, cc6.1, cc6.7]
related:
  - entities/tools/splunk.md
  - entities/people/rajneesh-gupta.md
  - concepts/siem.md
  - concepts/soc-operations.md
  - concepts/threat-hunting.md
  - concepts/incident-response.md
maturity: validated
read_status: read
created: 2026-05-16
updated: 2026-05-17
---

## Raw Concept

- **Title**: splunk SOC .pdf — "24 Use Cases SPLUNK SIEM for SOC 2 Compliance"
- **Author**: Rajneesh Gupta (@rajneeshcyber)
- **Type**: PDF
- **Location**: Google Drive — [BlueTeam Kit folder](https://drive.google.com/drive/folders/1v4dQsqYe6ekjgaoImDuU0CcEJKymx1Vs)
- **Retrieved**: 2026-05-16
- **Read-status**: read (full deep-read 2026-05-17)
- **Pages**: 24 use cases (one per page-ish), each with scenario + SPL query + outcome + SOC 2 Trust Service Criteria mapping

## Narrative

A short, audit-framed Splunk-for-SOC-2 cheatsheet. Each use case follows the same structure: *narrative scenario → SPL query → expected outcome → SOC 2 Trust Service Criteria reference*. The value is the **mapping layer** — same SPL idioms appear in @sources/100-splunk-queries-soc-analyst.md, but here they're tied to control IDs (CC6.1, CC6.6, CC6.7, CC6.8) so a Splunk deployment can produce audit-traceable evidence rather than just alerts.

### Distribution by Trust Service Criterion

| TSC | Control | Use cases | Examples |
|-----|---------|-----------|----------|
| **CC6.1** Logical Access | Authentication + authorization | 13 (UC1, 2, 4, 7, 10, 11, 12, 14, 15, 17, 18, 20, 22) | Unauthorized access, brute force, privilege escalation, dormant accounts, MFA bypass, shared credentials, SSH-key abuse, account lockout |
| **CC6.6** Change Management | Authorized changes only | 1 (UC21) | Config change tracking |
| **CC6.7** System Operations | Monitoring + response | 8 (UC3, 5, 6, 9, 16, 19, 23, 24) | Malware, file-integrity, exfil, network anomalies, system errors, service availability, performance, log-source health |
| **CC6.8** Risk Mitigation | Vulnerability handling | 2 (UC8, UC13) | Vulnerability-scanner integration, patch-compliance |

### Patterns the source teaches

- **Audit-traceable detection** — the difference between a SOC SIEM and an audit-defensible SIEM is the control-ID layer. Same SPL, two presentation modes.
- **SOC 2 ≠ ATT&CK** — the use cases are framed around access-control / availability / change-management, not adversary TTPs. Both framings are needed: ATT&CK for the threat-modeler, SOC 2 for the auditor.
- **Operational telemetry counts** — about a third of the use cases are availability/system-health (CC6.7 broad reading), not attack detection. SIEM-for-SOC2 is half operational-monitoring tool.

### Synthesis location

The 24 use cases are summarized in the SOC 2 use-case mapping table on @entities/tools/splunk.md. The author's per-use-case SPL queries align closely with the patterns in @sources/100-splunk-queries-soc-analyst.md (failed-login, privilege escalation, exfil) — so the synthesis there is the canonical detection content, while this source is the canonical control-mapping reference.

### Extraction confidence

Full 24-use-case set was read. The PDF is short and structurally repetitive; no deferred sections.

## Snippets

> **UC2 — Brute-force authentication (CC6.1)** [Source: splunk SOC .pdf (Gupta) — Use Case 2]
>
> *Scenario*: detect repeated failed authentication against any AD account → maps to ATT&CK T1110.
> *Query*: `EventCode=4625 | stats count by Account_Name, src_ip | where count > 5`
> *Outcome*: alert routes to Tier-1; escalate to Tier-2 if privileged account or MFA-bypass.
> *SOC 2*: CC6.1 Logical Access.

> **UC9 — Data exfiltration via large outbound transfer (CC6.7)** [Source: splunk SOC .pdf (Gupta) — Use Case 9]
>
> *Query*: `index=firewall | stats sum(bytes_out) as bo by src_ip, dest_ip | where bo > 100000000`
> *Outcome*: investigate destination IP reputation, correlate with DLP, validate against business justification.
> *SOC 2*: CC6.7 System Operations.

> **UC21 — Unauthorized configuration change (CC6.6)** [Source: splunk SOC .pdf (Gupta) — Use Case 21]
>
> *Scenario*: change to AD GPO, firewall ruleset, or critical-config file outside change-window.
> *SOC 2*: CC6.6 Change Management.

## Relations

- @entities/tools/splunk.md
- @entities/people/rajneesh-gupta.md
- @concepts/siem.md
- @concepts/soc-operations.md
- @concepts/threat-hunting.md
- @concepts/incident-response.md
