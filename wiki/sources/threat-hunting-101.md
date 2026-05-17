---
title: "Threat Hunting 101 PDF.pdf"
type: source
tags: [threat-hunting, soc, blue-team, white-paper, logrhythm, sysmon]
keywords: [threat hunting, rogue process, persistence, lateral movement, dns abuse, sysmon, event 4688, encoded powershell, dns rebinding, honeypot]
related:
  - concepts/threat-hunting.md
  - concepts/soc-operations.md
  - concepts/siem.md
  - entities/tools/sysmon.md
maturity: validated
read_status: read
created: 2026-05-16
updated: 2026-05-17
---

## Relations

- @concepts/threat-hunting.md
- @concepts/soc-operations.md
- @concepts/siem.md
- @entities/tools/sysmon.md

## Raw Concept

- **Title**: Threat Hunting 101 — 8 Threat Hunts You Can Do with Available Resources
- **Author**: Randy Franklin Smith (UltimateWindowsSecurity.com, LOGbinder, Microsoft Security MVP); LogRhythm white paper
- **Type**: PDF (24 pages, ~2.1 MB)
- **Location**: Google Drive — [BlueTeam Kit folder](https://drive.google.com/drive/folders/1v4dQsqYe6ekjgaoImDuU0CcEJKymx1Vs); file ID `1SKG__vdTZ12kZr7nqm_H7TmOvq7YEAc8`
- **Retrieved**: 2026-05-16
- **Pages**: 24
- **Read-status**: read (deep-read 2026-05-17)

## Narrative

LogRhythm-vendored introductory white paper structured as 8 distinct threat-hunt techniques, each anchored to a Windows event ID or Sysmon event class. The framing is pragmatic — built for a SOC analyst with a SIEM but limited dedicated hunt time, not for a full Tier-3 hunt team. Vendor branding (LogRhythm-specific UI screenshots, AI Engine "Whitelist Rule Block") is interleaved but the underlying technique is platform-neutral.

The 8 hunts (recurring pattern across the paper: identify the Windows/Sysmon log source, derive a baseline, alert on deviations, investigate):

1. **Suspicious Software** — process name vs hash. Process-name hunting via `4688` (Security Log audit process tracking) or Sysmon Event ID 1. Hash hunting requires Sysmon installed + maintained, and a whitelist that survives patching. Spoofed names — `d11host.exe`, `srvchost.exe` — masquerade as `dllhost.exe` / `svchost.exe`. Triage chain: alert → review process → Google name → VirusTotal full path → sandbox if still suspicious.
2. **Behavior Changes** — process + parent-process or process + username gives the context that bare process monitoring lacks. Canonical example: Microsoft Word spawning RDP. Outbound network connections from `notepad.exe` (or `powershell.exe`) similarly cue dropper / C2 activity.
3. **Scripting Abuse** — "living off the land" via `cscript`, `wscript`, `powershell`. Hunt the scripting engines themselves, especially with `-EncodedCommand`. PowerShell has audit logs that capture every command + block + output; WSH does not.
4. **Antivirus Follow-Up** — don't just trust "AV cleaned it." Look at the path where it was cleaned: `C:\Users\<user>\Downloads` is benign; `C:\Windows\System32` implies an admin-rights compromise. Paths containing `metasploit` or `mimikatz` strings = a now-clean endpoint that had hacker tooling installed.
5. **Persistence** — registry Run/RunOnce keys (`4663` w/ registry auditing or Sysmon 12-14), scheduled tasks (`4698`-`4702`), WMI eventing (Sysmon 19-21), services (`4697`). Mitigation note: removing local-admin from workstation users collapses the attacker's persistence surface.
6. **Lateral Movement** — new user/endpoint logon combos (`4624` / `4625`), abnormal network-connection pairs (`5156` or Sysmon 3). DHCP complicates IP-based baselining; filter on intra-range endpoint-to-endpoint traffic and treat workstation → workstation as suspicious.
7. **DNS Abuse** — outbound DNS bypassing internal resolvers, abnormally large DNS packets (port-53 exfiltration), `etc/hosts` modifications (`4663` + file auditing), and DNS rebinding (small-TTL DNS entry flips to internal IP so attacker-served JavaScript hits an internal API).
8. **Bait the Bad Guy** — honeypots / honey-accounts / honey-shares deliberately exposed to draw attackers away from production. Implementation overhead is the main cost.

The paper's strength is the per-hunt Windows Event ID + Sysmon mapping — useful as a quick reference when writing SIEM rules. Its weaknesses: vendor-locked LogRhythm UI screenshots add no transferable value; the lateral-movement section is the thinnest (no NTLM-relay, no Kerberoasting); MITRE ATT&CK is never named (the paper predates ATT&CK's dominance as the lingua franca of detection engineering).

This document anchors @concepts/threat-hunting.md as a starter framework, but a mature hunt program should pair it with the MITRE ATT&CK technique tree (@entities/frameworks/mitre-attack.md) and a hypothesis-driven workflow (David Bianco's Pyramid of Pain).

## Snippets

> "Threat hunting is the process of proactively searching for malware or attackers that reside on your network. The generally accepted method is to leverage a security information and event management (SIEM) solution that centrally collects log data from disparate sources — endpoints, servers, firewalls, security solutions, antivirus (AV), and more — providing visibility into network, endpoint, and application activity that might indicate an attack." [Source: Threat Hunting 101 PDF.pdf p.3]

> **Suspicious software hunt — process-name LogRhythm Lucene query**
> `vendorMessageId:("4688" OR "1") AND process:*` [Source: Threat Hunting 101 PDF.pdf p.6]

> **Baseline SQL — deduplicated process list**
> `Select distinct ProcessName from Events where EventId=4688 OR EventId=1` [Source: Threat Hunting 101 PDF.pdf p.6]

> **Spoofed-name examples**: `C:\Windows\System32\d11host.exe` and `C:\Windows\System32\srvchost.exe` — close enough to `dllhost.exe` and `svchost.exe` to slip past a glance, but neither is part of the OS. [Source: Threat Hunting 101 PDF.pdf p.8]

> **Persistence — Windows event IDs to audit**:
> - Registry: Security Log `4663` (with registry auditing enabled via GPO) or Sysmon `12-14`
> - Scheduled Tasks: `4698`-`4702` (requires "Other Object Access Events" auditing)
> - WMI Eventing: Sysmon `19-21`
> - Services: `4697` (requires "System Security Extension" auditing) [Source: Threat Hunting 101 PDF.pdf p.17]

> **Lateral movement — log source map**:
> - New user/endpoint logon combos: Security Log `4624`, `4625` (baseline tuple of `ComputerName` + `NewLogonAccountName` + `Domain`)
> - New endpoint/endpoint connection combos: Sysmon `3` or Security Log `5156`
> - Note: Security Log event `5156` does **not** include hostname; Sysmon `3` only captures hostname if it was used as part of the initial connection. [Source: Threat Hunting 101 PDF.pdf p.19]

> **DNS rebinding mechanism**: "The DNS entry for the compromised site or ad is set with a very small time to live (TTL) value, causing the client to need to refresh the DNS cache to reinitialize the session. The site then points the browser to an internal IP address, at which time the malicious JavaScript code executes against a local system that would otherwise be inaccessible from the outside." [Source: Threat Hunting 101 PDF.pdf p.21]

## Dead Ends

- **Hash-based whitelisting at scale** — the paper itself flags this as expensive: every patch creates a new hash, .NET produces hundreds of per-system optimized DLLs, commercial whitelists lag patches. [CONFIRMED] — pragmatic SOCs treat hash whitelisting as a supplementary signal, not a primary hunt; per-process-name + parent-process behavior remains the higher-yield hunt.
- **Windows Scripting Host auditing** — the paper notes: "Auditing the usage of Windows Scripting Host is nearly impossible, as no logs capture what the script is doing, other than at a process level." [CONFIRMED] — defenders should treat any `wscript`/`cscript` execution as worth investigating because the script body is opaque.
