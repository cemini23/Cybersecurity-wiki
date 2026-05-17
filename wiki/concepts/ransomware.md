---
title: Ransomware — Defensive Operations & Investigation
type: concept
tags: [ransomware, incident-response, blue-team, dfir, t1486, soc]
keywords: [ransomware, encryption, vssadmin, shadow copy, ransom note, lolbin, certutil, bitsadmin, t1486, lockbit, raas, double extortion, runbook, tp vs fp]
related:
  - concepts/incident-response.md
  - concepts/malware-analysis.md
  - concepts/soc-operations.md
  - concepts/threat-hunting.md
  - concepts/endpoint-detection-response.md
  - entities/tools/sysmon.md
  - entities/threat-actors/lockbit.md
  - entities/frameworks/mitre-attack.md
  - sources/ransomware-investigation-runbook.md
  - sources/ransomware-investigation-osint-and-hunting-overview-pt1.md
  - sources/2025-cybersecurity-attacks-playbooks.md
  - concepts/threat-intelligence.md
maturity: validated
created: 2026-05-17
updated: 2026-05-17
---

## Relations

- @concepts/incident-response.md
- @concepts/malware-analysis.md
- @concepts/soc-operations.md
- @concepts/threat-hunting.md
- @concepts/endpoint-detection-response.md
- @entities/tools/sysmon.md
- @entities/threat-actors/lockbit.md
- @entities/frameworks/mitre-attack.md
- @sources/ransomware-investigation-runbook.md
- @sources/ransomware-investigation-osint-and-hunting-overview-pt1.md
- @sources/2025-cybersecurity-attacks-playbooks.md
- @concepts/threat-intelligence.md

## Raw Concept

Created 2026-05-17 from deep-read of @sources/ransomware-investigation-runbook.md. The wiki had a LockBit threat-actor page (@entities/threat-actors/lockbit.md) and the runbook source stub, but no dedicated concept page that synthesizes the defensive-operations view of ransomware as a class. Scope here is defensive — detection + investigation + response. Pure technical reverse-engineering of a specific ransomware family belongs in @concepts/malware-analysis.md; doctrine/lifecycle belongs in @concepts/incident-response.md.

## Narrative

**Ransomware** = malware that encrypts (or, increasingly, only steals + threatens to publish) victim data, withholding access or non-publication until payment. Maps to MITRE ATT&CK technique **T1486 — Data Encrypted for Impact** (and T1657 — Financial Theft, T1485 — Data Destruction for wipers misclassified as ransomware). See @entities/frameworks/mitre-attack.md.

The modern criminal ecosystem is dominated by **RaaS** (Ransomware-as-a-Service): the operator/developer builds the malware + infrastructure, affiliates execute intrusions and split the proceeds (typically 70-80% affiliate / 20-30% operator). LockBit (@entities/threat-actors/lockbit.md), Black Basta, Akira, and Play are the dominant 2024-2026 brands. Each rebrand cycle (LockBit → after Op Cronos → reconstituted as new brand) is mostly the same operators + tooling under a new logo. [CONFIRMED]

### Double + triple extortion

Modern intrusions don't just encrypt — they:

1. **Exfiltrate** sensitive data first (often 100s of GB over days/weeks)
2. **Encrypt** with a fast symmetric cipher + per-file or per-victim key
3. **Threaten leak publication** on the operator's data-leak-site (DLS)
4. (Triple extortion) **Contact victim's customers/partners** directly to amplify pressure
5. (Quad extortion) **DDoS the victim's public services** during negotiation

This shifts the defender calculus: even with perfect backups, the exfiltration leg of the attack still creates a breach-notification + regulatory + reputational event. Network-egress monitoring and DLP matter for ransomware defense, not just file-write monitoring. [CONFIRMED] [Source: @sources/ransomware-investigation-runbook.md §7]

### Kill-chain phases — defender view

Each phase has its own detection surface:

| Phase | Adversary action | Defender signal |
|-------|------------------|-----------------|
| **Initial access** | Phishing (esp. macro/HTA droppers), exposed RDP, edge-device CVEs (Fortinet, Ivanti, Citrix, ConnectWise) | Email gateway, brute-force RDP alerts, vuln scanner |
| **Execution** | PowerShell `-EncodedCommand`, certutil downloader, mshta/regsvr32 proxy exec | Sysmon `1` + parent-process anomaly (@entities/tools/sysmon.md) |
| **Persistence** | Scheduled tasks, services, Run keys, WMI eventing | Sysmon `12-14`, `19-21`; Security `4697`, `4698-4702` |
| **Credential access** | LSASS dump (Mimikatz), DCSync, Kerberoasting | Sysmon `10` (process access on lsass.exe); 4769 with `0x17` encryption |
| **Lateral movement** | PsExec, WMI, RDP, SMB writes to file shares | Security `4624` (type 3/10), `5145`, Sysmon `3` |
| **Defense evasion** | Disable WinDefend, clear event logs, `vssadmin delete shadows` | Service-stop events, 1102 (log cleared), `4688` w/ vssadmin |
| **Discovery** | AD enumeration (BloodHound, ADExplorer), share enumeration | 4661 (handle to AD object), 5140/5145 |
| **Exfiltration** | Rclone to MEGA / Backblaze; HTTPS POST; FTP | Proxy/firewall — new-domain destination + large outbound volume |
| **Impact (encryption)** | Mass file-rename + ransom-note drop | File-audit burst (>500/min over baseline), ransom-note filename hunt |

### The single highest-confidence detection: VSS deletion

**`vssadmin delete shadows /all /quiet`** (or equivalents `wbadmin delete catalog`, `wmic shadowcopy delete`) is run by most ransomware families immediately before mass-encryption. The intent — kill the local backup recovery path — has no legitimate use-case in a normal end-user or server workflow.

Detection: alert on any `4688` (or Sysmon `1`) where the process name is `vssadmin.exe` / `wbadmin.exe` / `wmic.exe` AND the command line contains `delete shadows` / `delete catalog` / `shadowcopy delete`. The runbook's scoring rubric weights this at **+5** on its own; combined with mass file writes, it's effectively a confirmed-TP signal. [CONFIRMED] [Source: @sources/ransomware-investigation-runbook.md §6]

### TP vs FP — the scoring model

From @sources/ransomware-investigation-runbook.md §9 — additive evidence scoring:

```
Mass encryption / ransom notes confirmed      +8
Known ransomware hash/family match            +6
VSS / shadow copy deletion observed           +5
C2 to known-malicious IP/domain               +5
Lateral spread across multiple hosts          +4
Persistence object created                    +3
PowerShell/certutil use alone                 +1
Single uncorroborated heuristic               +1

≥12: strong TP (full IR)
 6-11: probable TP (preserve + escalate)
 ≤5: likely FP (collect more, check benign causes)
```

The discipline this enforces: a single ambiguous signal never escalates a ticket; corroboration is required. Most production false positives — Veeam backup jobs producing high write volume, scheduled compression, AV self-actions — fail this rubric naturally.

### Operational playbook — 10-step sequence

From @sources/ransomware-investigation-runbook.md §15. Adapt to your SOC ticket template:

1. **Triage** — capture alert metadata, EDR snapshot, decide containment urgency
2. **Contain** (if active) — EDR network-isolate first; full host shutdown only if isolation unavailable
3. **Collect** — EDR process tree, file events, registry hives, scheduled tasks, memory dump
4. **Search** — process creation (`4688` / Sysmon `1`), `vssadmin`/`wbadmin`, encoded PowerShell, mass file writes
5. **Enrich** — hash + domain + IP threat-intel lookups; map to ATT&CK techniques
6. **Correlate + timeline** — CSV: `Timestamp | Host | User | Process | Parent | PID | CommandLine | FileAction | NetDest | LogSource | Notes`
7. **Decide** — apply scoring rubric; declare TP/FP with documented evidence
8. **If TP** — preserve artifacts → eradicate (reimage) → recover from clean backups → rotate creds
9. **If FP** — document evidence → tune detection rules → close ticket
10. **Post-incident** — root-cause analysis, patching, detection improvements, tabletop exercise

### Recovery rules

- **Don't pay if avoidable.** No payment guarantees decryption; payment funds the next intrusion; many jurisdictions (US OFAC, UK NCSC guidance) make payment to sanctioned operators legally fraught.
- **Verify backup hygiene quarterly.** Backups that turn out to be online + encrypt-able when needed = no backups. Test restore-from-immutable / air-gapped tier.
- **Assume credential compromise.** Reset domain admin, service accounts, and any account that touched a compromised host. Rotate Kerberos `krbtgt` twice (double-rotation closes the Golden Ticket window).
- **Notify legal/regulatory early.** Breach-notification clocks (GDPR 72 hr, US state laws, sector regulators) start at discovery, not at full understanding.

### Critical LOLBins for ransomware tradecraft

Ransomware affiliates lean heavily on living-off-the-land binaries because they evade naive AV signatures. From the runbook §4 + supplementary cross-check:

| LOLBin | Normal use | Ransomware misuse | Detection cue |
|--------|-----------|-------------------|---------------|
| `powershell.exe` | Admin scripting | `-EncodedCommand`, IEX from URL, in-memory payload | Parent = Office; encoded args |
| `certutil.exe` | Cert utility | `-urlcache -split -f` to download payload | Run by non-admin or Office parent |
| `bitsadmin.exe` | Background transfer | Payload download via BITS jobs | New BITS job to external domain |
| `regsvr32.exe` | Register DLL | Squiblydoo: proxy remote-script execution | Remote URL in command line |
| `rundll32.exe` | Run DLL | Proxy DLL/script execution | Unusual DLL path |
| `mshta.exe` | HTA host | HTA from URL / inline JS | Almost always suspicious in modern env |
| `vssadmin.exe` | Shadow copies | `delete shadows /all /quiet` | Pre-encryption anti-recovery |
| `wbadmin.exe` | Windows backup | `delete catalog` | Pre-encryption anti-recovery |
| `wmic.exe` | WMI client | Lateral remote exec | Service creation in temp dirs |
| `psexec.exe` | SysInternals remote admin | Lateral remote exec | Service created in user/temp path |
| `schtasks.exe` | Scheduled tasks | Persistence via task w/ benign name | Task action references temp/user binary |
| `cscript.exe` / `wscript.exe` | Script host | VBS/JS dropper execution | Parent = Office macro |

### Cross-link

- @concepts/incident-response.md — lifecycle doctrine (NIST 800-61r2 / SANS PICERL)
- @concepts/malware-analysis.md — when reverse-engineering a captured sample
- @concepts/soc-operations.md — organizational context for the SOC analyst running this playbook
- @concepts/threat-hunting.md — proactive cousin: hunt for the VSS-deletion / mass-file-write / encoded-PowerShell patterns *before* an alert fires
- @entities/tools/sysmon.md — primary log source for the detection signals above
- @entities/threat-actors/lockbit.md — dominant RaaS brand of the 2020-2024 era

## Snippets

> **The single most diagnostic ransomware indicator** [Source: @sources/ransomware-investigation-runbook.md §6]
>
> "Deleting backups is an explicit step to prevent recovery — when combined with encryption this is a very strong TP signal."

> **Don't power off a suspected host** [Source: @sources/ransomware-investigation-runbook.md §1]
>
> If active encryption: EDR network-isolate first. If business-critical and unsure: live-memory dump *before* hard shutdown. Power-off destroys in-memory keys + injection state + process telemetry.

## Dead Ends

- **AV signature alone as the ransomware control** — modern affiliates compile per-victim binaries; signature-based AV often misses. EDR behavioral detection + log-correlation hunts (above) remain primary. [CONFIRMED]
- **Backup tier without air-gap or immutability** — online backups reachable by domain credentials get encrypted alongside production. Tested 3-2-1 with at least one offline/immutable copy is the actual control. [CONFIRMED]
- **Payment-for-decryption as a recovery plan** — failure rate (no decryptor, partial decryptor, second extortion) is significant; sanctioned-operator liability is real. Treat as last resort, not Plan A. [CONFIRMED]
- **Shannon-entropy file scanning as sole detection** — too many high-entropy false positives (zip, jpeg, sqlite-WAL). Use only as one signal among many. [CONFIRMED] [Source: @sources/ransomware-investigation-runbook.md §5]
