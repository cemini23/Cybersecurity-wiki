---
title: Threat Hunting
type: concept
tags: [proactive, blue-team, detection, sysmon]
keywords: [threat hunting, hunt, kibana, elastic, splunk, sysmon, pyramid of pain, hypothesis driven, mitre att&ck, event 4688, encoded powershell, dns rebinding, honeypot]
related:
  - concepts/soc-operations.md
  - concepts/incident-response.md
  - concepts/siem.md
  - concepts/endpoint-detection-response.md
  - concepts/malware-analysis.md
  - concepts/osint-for-cybersecurity.md
  - entities/frameworks/mitre-attack.md
  - entities/tools/sysmon.md
  - entities/people/joas-a-santos.md
  - sources/elearnsecurity-certified-threat-hunting-introduction-pt-1.md
  - sources/malware-hunting-threat-hunter-overview-1.md
  - sources/100-splunk-queries-soc-analyst.md
  - sources/blue-team-handbook.md
  - sources/blue-team-notes.md
  - sources/effective-threat-investigation-soc-analysts.md
  - sources/mitre-attack-framework-soc.md
  - sources/open-source-soc-guide.md
  - sources/soc-analyst-book.md
  - sources/50-free-online-tools-soc-analysts.md
  - sources/threat-hunting-101.md
  - concepts/ransomware.md
  - sources/ransomware-investigation-runbook.md
  - concepts/threat-intelligence.md
  - concepts/phishing-investigation.md
  - entities/people/mostafa-yahia.md
  - entities/tools/gopacket.md
  - entities/tools/splunk.md
  - sources/splunk-commands-reference.md
  - sources/splunk-siem-soc2-use-cases.md
  - entities/tools/qradar.md
  - sources/next-gen-soc-ibm-qradar.md
  - entities/tools/grex.md
  - entities/tools/cve-mcp-server.md
maturity: validated
created: 2026-05-12
updated: 2026-05-28
---

## Relations

- @concepts/soc-operations.md
- @concepts/incident-response.md
- @concepts/siem.md
- @concepts/endpoint-detection-response.md
- @concepts/malware-analysis.md
- @concepts/osint-for-cybersecurity.md
- @entities/frameworks/mitre-attack.md
- @entities/tools/sysmon.md
- @entities/people/joas-a-santos.md
- @sources/elearnsecurity-certified-threat-hunting-introduction-pt-1.md
- @sources/malware-hunting-threat-hunter-overview-1.md
- @sources/100-splunk-queries-soc-analyst.md
- @sources/blue-team-handbook.md
- @sources/blue-team-notes.md
- @sources/effective-threat-investigation-soc-analysts.md
- @sources/mitre-attack-framework-soc.md
- @sources/open-source-soc-guide.md
- @sources/soc-analyst-book.md
- @sources/50-free-online-tools-soc-analysts.md
- @sources/threat-hunting-101.md
- @concepts/ransomware.md
- @sources/ransomware-investigation-runbook.md
- @concepts/threat-intelligence.md
- @entities/tools/cve-mcp-server.md — on-demand CVE/KEV/EPSS context during hunt triage
- @concepts/phishing-investigation.md
- @entities/people/mostafa-yahia.md
- @entities/tools/gopacket.md — Go packet-decoding library; decoded packet metadata as a network-hunt substrate
- @entities/tools/splunk.md
- @sources/splunk-commands-reference.md
- @sources/splunk-siem-soc2-use-cases.md
- @entities/tools/qradar.md
- @sources/next-gen-soc-ibm-qradar.md

## Raw Concept

Multi-source anchor. Validated deep-read of LogRhythm's *Threat Hunting 101* (@sources/threat-hunting-101.md, 2026-05-17) provided the 8-hunt skeleton + Windows Event ID / Sysmon mapping. Supporting corpus context from the eLearnSecurity threat-hunting introduction, Blue Team Handbook, and the SOC-analyst books in the BlueTeam Kit.

## Narrative

**Threat hunting** = the proactive search for adversary activity in environments where no alert has fired. It's hypothesis-driven detection — "if [adversary] were already inside, what would I expect to see?" — and complements the alert-driven SOC workflow (@concepts/soc-operations.md), not replacing it. A mature hunt program closes the gap between MTTD-on-known-IOC (good) and MTTD-on-unknown-TTPs (the gap hunters fill).

### Mental model — David Bianco's Pyramid of Pain

Hash IOCs are easy for an attacker to rotate; TTPs cost an attacker real engineering effort. Hunting should bias toward the painful end of the pyramid:

```
TTPs                ← maximum attacker pain (rewrite of tradecraft)
Tools
Network/Host Artifacts
Domain Names
IP Addresses
Hash Values         ← minimum attacker pain (one rebuild)
```

[Source: Bianco, "Pyramid of Pain" (retrieved indirectly via @sources/threat-hunting-101.md framing and @sources/effective-threat-investigation-soc-analysts.md)] [CONFIRMED]

### Prerequisites — log substrate

A SIEM (@concepts/siem.md) ingesting the right log surfaces. From the LogRhythm reference (@sources/threat-hunting-101.md p.4), the minimum viable set:

- **Windows endpoints**: Security Log + Sysmon (@entities/tools/sysmon.md) + PowerShell logs
- **Linux endpoints**: `/var/log/messages`, audit logs, file-integrity-monitoring agents
- **Network**: firewalls, DNS servers, proxies, IDS/IPS
- **Identity**: AD logs, Kerberos, MFA, SSO
- **Security stack**: AV/EDR (@concepts/endpoint-detection-response.md), VPN, vulnerability scanners

### Hunt-technique catalog — 8 high-yield hunts

Synthesized from @sources/threat-hunting-101.md. Each hunt is a baseline → deviation → investigate loop.

#### 1. Suspicious software (process-name + hash)

**Sources**: Security Log `4688` (audit process tracking) or Sysmon `1` (process creation).

Hunt for spoofed process names mimicking OS executables — `d11host.exe`, `srvchost.exe`, `notpad.exe`. Hash hunting requires Sysmon and a per-patch-cycle whitelist refresh; pragmatically, process-name + parent-process behavior outperforms pure hash hunting (the *Threat Hunting 101* paper acknowledges this on p.10). [CONFIRMED]

Triage chain: alert → review process → Google name → VirusTotal full path → sandbox if still suspicious.

#### 2. Behavior changes (process + parent / process + user)

**Sources**: same as Hunt 1, with parent-process and account-context.

Word spawning RDP. Notepad opening an outbound socket. `powershell.exe` invoked by an Office macro. Single processes are one-dimensional; pairs surface intent. [CONFIRMED]

#### 3. Scripting abuse (LOLBins)

**Sources**: Security Log `4688`, Sysmon `1`, PowerShell operational log.

Hunt the scripting engines themselves: `cscript`, `wscript`, `powershell`. High-value subhunt: PowerShell with `-EncodedCommand` (a near-canonical obfuscation pattern in modern intrusions). PowerShell's `Microsoft-Windows-PowerShell/Operational` log captures script-block detail; Windows Scripting Host does not, so any WSH execution warrants investigation by default. [CONFIRMED]

#### 4. Antivirus follow-up

**Sources**: AV management console logs (Defender, CrowdStrike, etc.).

Don't treat "AV cleaned it" as case-closed. Look at the **path**:
- `C:\Users\<user>\Downloads\` → benign user download
- `C:\Windows\System32\` → admin-rights compromise occurred
- Path contains `metasploit` or `mimikatz` strings → hacker tooling was installed on this now-clean endpoint [CONFIRMED] [Source: @sources/threat-hunting-101.md p.16]

#### 5. Persistence

**Sources** (each requires the corresponding GPO audit policy enabled):

- Registry Run/RunOnce: Security Log `4663` (with registry auditing on specific keys) or Sysmon `12-14`
- Scheduled tasks: `4698`-`4702` (enable "Other Object Access Events")
- WMI eventing: Sysmon `19-21`
- Services: `4697` (enable "System Security Extension")

Mitigation that collapses most of the attack surface: remove local-admin from end-user workstation accounts. [CONFIRMED] Maps to MITRE ATT&CK Tactic TA0003 — Persistence.

#### 6. Lateral movement

**Sources**: Security Log `4624`/`4625` (logon), `5156` (network connection), Sysmon `3` (network connection).

Baseline tuples of `(ComputerName, NewLogonAccountName, Domain)` and alert on new combinations. Caveats: DHCP environments make IP-based baselining lossy; `5156` does not include hostname; Sysmon `3` only captures the hostname if it was used as part of the initial connection (i.e. resolved-via-DNS sessions show it, raw-IP sessions don't). [CONFIRMED]

#### 7. DNS abuse

**Sources**: firewall (port 53 traffic), endpoint DNS audit, `etc/hosts` file-integrity monitor (`4663`).

Hunts:
- Outbound DNS bypassing internal resolvers (client → 8.8.8.8 instead of → internal DNS)
- Abnormally large DNS packets (exfiltration over port 53 — see also DNSCat2, Iodine)
- `etc/hosts` modifications (`4663` + file auditing)
- DNS rebinding (small-TTL response flips A-record from external to internal IP; attacker-served JS then hits an internal-only API). The *Threat Hunting 101* paper notes LogRhythm fingerprints these via REST API patterns + JS filename + URL string (@sources/threat-hunting-101.md p.21).

#### 8. Honeypots / honey-accounts / honey-shares

**Sources**: any access whatsoever to the bait system.

Anything that touches a honey-credential or honey-share is — by construction — an intruder. Highest signal-to-noise hunt available, but operational overhead to build + maintain the bait realistically and monitor it. [CONFIRMED]

### Pairing with MITRE ATT&CK

The hunt catalog above maps cleanly to ATT&CK tactics:

| Hunt | Primary ATT&CK tactic(s) |
|------|--------------------------|
| 1 Suspicious software | TA0002 Execution; TA0005 Defense Evasion (masquerading T1036) |
| 2 Behavior changes | TA0002 Execution; TA0005 Defense Evasion |
| 3 Scripting abuse | T1059.001 PowerShell; T1059.005 Visual Basic |
| 4 AV follow-up | Cross-cutting — informs scope of prior compromise |
| 5 Persistence | TA0003 Persistence (T1547, T1053, T1546, T1543) |
| 6 Lateral movement | TA0008 Lateral Movement (T1021 Remote Services) |
| 7 DNS abuse | TA0011 C2 (T1071.004 DNS); T1048 Exfil over alt protocol |
| 8 Honeypots | Cross-cutting — detection technique, not adversary technique |

See @entities/frameworks/mitre-attack.md.

### Hunt program maturity ladder

1. **Ad-hoc** — analyst runs the same SPL queries weekly, no documentation.
2. **Repeatable** — hunts written up as playbooks; outputs feed back into detection-engineering backlog.
3. **Automated** — recurring hunts promoted to standing SIEM correlation rules; analyst time freed for novel hypotheses.
4. **Adversary-emulation-driven** — purple-team exercises (@concepts/purple-team-operations.md) generate hunt hypotheses; Atomic Red Team / Caldera (@concepts/adversary-emulation.md) generates the telemetry to validate against.

Most real SOCs operate at level 1-2. The transition to 3 requires both SIEM rule-content maintenance discipline and explicit Tier-3 hunter allocation.

## Snippets

> **Hash hunting's three weaknesses** [Source: Threat Hunting 101 PDF.pdf p.9]
>
> - Buffer overflows and related non-EXE binary code (no file → no hash)
> - Scripting abuse — PowerShell / WSH / JavaScript "live off the land" with no new binary
> - Maintenance — every patch creates a new hash; commercial whitelists lag patch releases

> **PowerShell encoded-command pattern** [Source: Threat Hunting 101 PDF.pdf p.13]
>
> Sysmon `1` or Security Log `4688` with command line containing `powershell.exe` and `-EncodedCommand` — high-signal hunt for obfuscated-script execution.

## Dead Ends

- **Hash-only whitelisting as primary hunt** — abandoned in favor of process-name + parent-process behavior, per @sources/threat-hunting-101.md p.10. The hash whitelist is supplementary; the maintenance burden defeats it as a primary control. [CONFIRMED]
- **IP-based lateral-movement baselining in DHCP environments** — `5156` doesn't include hostname; Sysmon `3` only captures hostname when DNS-resolved. Effective hunts in DHCP environments require correlating against the DHCP lease log to resolve IP → host. [CONFIRMED]
