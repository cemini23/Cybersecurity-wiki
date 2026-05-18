---
title: "100+ Splunk Queries for SOC Analyst.pdf"
type: source
tags: [soc, blue-team, splunk, siem, detection-engineering]
keywords: [splunk queries, spl, soc analyst, detection, threat hunting, brute force, lateral movement, ransomware, c2, dns tunneling, powershell empire]
related:
  - entities/tools/splunk.md
  - entities/tools/sysmon.md
  - entities/frameworks/mitre-attack.md
  - concepts/siem.md
  - concepts/soc-operations.md
  - concepts/threat-hunting.md
  - concepts/incident-response.md
  - concepts/ransomware.md
  - concepts/phishing-investigation.md
maturity: validated
read_status: read
created: 2026-05-16
updated: 2026-05-17
---

## Raw Concept

- **Title**: 100+ Splunk Queries for SOC Analyst.pdf
- **Author**: community-curated SPL collection (anonymous compiler; shared via Google Drive — BlueTeam Kit)
- **Type**: PDF
- **Location**: Google Drive — [BlueTeam Kit folder](https://drive.google.com/drive/folders/1v4dQsqYe6ekjgaoImDuU0CcEJKymx1Vs)
- **Retrieved**: 2026-05-16
- **Read-status**: read (full deep-read 2026-05-17)
- **Pages**: 110 SPL queries (one per detection use case; brief commentary)

## Narrative

A reference collection of 110 ready-to-use SPL queries spanning the SOC detection landscape. The structure is uniform: a one-line scenario, the SPL query, and (usually) a one-line note on threshold tuning or ATT&CK mapping. Less of a textbook, more of a SPL cookbook — meant to be pasted into Splunk search bar, tuned to a customer environment, and either promoted to a saved-search alert or used as a threat-hunting starting point.

Synthesized into the catalog tables on @entities/tools/splunk.md (Detection-query catalog section). The catalog there groups all 110 queries by hunt class:

- **Authentication + access** (28 queries) — failed/successful logins, sudo/su abuse, brute force per protocol, account creation, group changes, audit-policy tampering
- **Process + endpoint behavior** (18) — suspicious spawns, encoded PowerShell, PowerShell-Empire patterns, service/scheduled-task/WMI persistence, Defender alerts
- **Lateral movement** (8) — SMB, RDP, WMI, WinRM, DCOM, NetBIOS, PsExec, remote registry
- **Network anomalies + C2 + exfil** (15) — port scans, DNS tunneling, beaconing, large transfers, TOR egress, suspicious URLs
- **Web-app attacks** (6) — SQLi, command injection, XSS, web shells, path traversal
- **Ransomware** (5) — mass-rename, ransom extensions, shadow-copy deletion, Defender disable
- **Reconnaissance + CVE exploitation** (8) — Nmap-style scans, suspicious User-Agent, Log4Shell, Spring4Shell, ProxyShell/ProxyLogon
- **Phishing + email** (3) — bulk delivery, lookalike domains, spoofed sender
- **Data integrity + DDoS + account takeover** (remainder) — impossible-travel, off-hours admin, file-integrity, DDoS volumetric

### Patterns the source teaches

1. **Pipeline shape** — every query is `search → stats by → threshold → sort`. The same skeleton with different field names covers ~80% of the catalog. [CONFIRMED]
2. **Tuple-baselining for lateral movement** — `stats values(src_ip) by Computer, Account_Name` then alert on new tuples. Same idea recurs in @concepts/threat-hunting.md Hunt 6.
3. **Behavior-over-hash bias** — almost no hash matching; the catalog focuses on event codes, command lines, parent-process behavior. Same philosophy as @concepts/threat-hunting.md and the Pyramid of Pain framing.
4. **Encoded-PowerShell is split across event IDs** — `4688` shows the encoded blob, `4104` decodes it. Several queries pair both.

### Extraction confidence

Full text of all 110 queries was extracted in this deep-read. No deferred sections. Representative queries are quoted verbatim on @entities/tools/splunk.md (Snippets section).

## Snippets

> **Failed-logins by source IP (Linux)** [Source: 100+ Splunk Queries for SOC Analyst.pdf Q1]
>
> ```
> index=auth sourcetype=linux_secure "Failed password"
> | stats count by src_ip
> | where count > 10
> | sort -count
> ```

> **PowerShell encoded command (Sysmon / 4688)** [Source: 100+ Splunk Queries for SOC Analyst.pdf Q47]
>
> ```
> index=wineventlog EventCode=4688 Process_Command_Line="*-EncodedCommand*"
> | table _time, Account_Name, New_Process_Name, Process_Command_Line
> ```

> **Lateral movement via RDP (Logon_Type=10)** [Source: 100+ Splunk Queries for SOC Analyst.pdf Q68]
>
> ```
> index=wineventlog EventCode=4624 Logon_Type=10
> | stats count by Account_Name, src_ip, Computer
> | where count > 5
> ```

> **DNS tunneling — long query string** [Source: 100+ Splunk Queries for SOC Analyst.pdf Q73]
>
> ```
> sourcetype=dns
> | eval qlen=len(query)
> | where qlen > 50
> | stats count by src_ip, query
> ```

> **Ransomware shadow-copy deletion** [Source: 100+ Splunk Queries for SOC Analyst.pdf Q95]
>
> ```
> index=wineventlog EventCode=4688
> | search Process_Command_Line="*vssadmin delete shadows*"
>          OR Process_Command_Line="*wmic shadowcopy delete*"
> | table _time, host, Account_Name, Process_Command_Line
> ```

## Relations

- @entities/tools/splunk.md
- @entities/tools/sysmon.md
- @entities/frameworks/mitre-attack.md
- @concepts/siem.md
- @concepts/soc-operations.md
- @concepts/threat-hunting.md
- @concepts/incident-response.md
- @concepts/ransomware.md
- @concepts/phishing-investigation.md
