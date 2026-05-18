---
title: Sysmon (System Monitor)
type: entity
tags: [sysmon, windows, blue-team, sysinternals, edr-lite, threat-hunting]
keywords: [sysmon, system monitor, sysinternals, event id 1, event id 3, event id 11, event id 12, event id 13, event id 14, event id 19, event id 20, event id 21, process creation, network connection, registry, wmi]
related:
  - concepts/threat-hunting.md
  - concepts/soc-operations.md
  - concepts/siem.md
  - concepts/endpoint-detection-response.md
  - entities/frameworks/mitre-attack.md
  - sources/threat-hunting-101.md
  - sources/effective-threat-investigation-soc-analysts.md
  - sources/blue-team-handbook.md
  - sources/open-source-soc-guide.md
  - concepts/ransomware.md
  - sources/ransomware-investigation-runbook.md
  - entities/tools/splunk.md
  - sources/100-splunk-queries-soc-analyst.md
  - entities/tools/qradar.md
  - sources/next-gen-soc-ibm-qradar.md
maturity: draft
created: 2026-05-17
updated: 2026-05-17
---

## Relations

- @concepts/threat-hunting.md
- @concepts/soc-operations.md
- @concepts/siem.md
- @concepts/endpoint-detection-response.md
- @entities/frameworks/mitre-attack.md
- @sources/threat-hunting-101.md
- @sources/effective-threat-investigation-soc-analysts.md
- @sources/blue-team-handbook.md
- @sources/open-source-soc-guide.md
- @concepts/ransomware.md
- @sources/ransomware-investigation-runbook.md
- @entities/tools/splunk.md
- @sources/100-splunk-queries-soc-analyst.md
- @entities/tools/qradar.md
- @sources/next-gen-soc-ibm-qradar.md

## Raw Concept

Sysmon kept surfacing as a load-bearing log source across the BlueTeam Kit corpus — every threat-hunt technique in @sources/threat-hunting-101.md maps to a Sysmon event ID, and the SOC-analyst books in the corpus assume it's deployed. A dedicated entity page formalizes its role as the no-cost EDR-lite that fills the visibility gap left by the default Windows Security Log.

## Narrative

**Sysmon** = a free Microsoft Sysinternals system service + device driver that emits high-fidelity Windows event-log entries beyond what the default Security Log captures. Installs as `Sysmon.exe`; configured by XML; logs land in the `Microsoft-Windows-Sysmon/Operational` channel. Source: [Sysmon @ docs.microsoft.com/sysinternals](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon).

**Why it matters for hunting**: the default Windows Security Log captures process tracking only when `4688` is enabled, and it omits the load-bearing context (command line is only captured with a GPO toggle; parent-process info is partial; outbound network connections aren't logged at all). Sysmon fills these gaps with structured per-event-class output, which is why every SIEM threat-hunt playbook in the corpus (@sources/threat-hunting-101.md, @sources/effective-threat-investigation-soc-analysts.md, @sources/blue-team-handbook.md) assumes Sysmon is shipping logs to the SIEM. [CONFIRMED]

### Key event IDs (mapped to hunt categories)

| Event ID | What it captures | Hunt use |
|----------|------------------|----------|
| `1` | Process creation (full command line, parent process, hash, signature) | Rogue-process and behavior-change hunts (see @concepts/threat-hunting.md) |
| `3` | Network connection (process → remote IP/port) | Lateral movement; C2 callback detection |
| `7` | Image loaded (DLL injection signal) | Defender-evasion + unsigned DLL hunts |
| `8` | CreateRemoteThread (process injection) | Classic injection TTP (MITRE T1055) |
| `10` | ProcessAccess (LSASS read = credential dumping signal) | Mimikatz / credential-access hunts |
| `11` | File creation | Dropper detection; ransomware-staging |
| `12-14` | Registry — key/value create, modify, delete | Persistence hunts (Run keys, services) |
| `19-21` | WMI event (filter, consumer, binding) | WMI persistence (MITRE T1546.003) |
| `22` | DNS query | DNS-tunneling / abuse hunts |
| `25` | Process tampering (process hollowing variant, Sysmon ≥13) | Defender-evasion |

[Source: Threat Hunting 101 PDF.pdf pp.6-21; sysinternals docs]

### Configuration

Default Sysmon config is minimal and produces enormous noise. The de-facto community baseline is the **SwiftOnSecurity** template — [github.com/SwiftOnSecurity/sysmon-config](https://github.com/SwiftOnSecurity/sysmon-config) — and its more aggressive sibling **Olaf Hartong's sysmon-modular** ([github.com/olafhartong/sysmon-modular](https://github.com/olafhartong/sysmon-modular)) which decomposes the config into MITRE ATT&CK-aligned modules. [NEEDS VERIFICATION 2026-05-17] — last-validated repo state is on the canonical-tool deep-read backlog.

Install + bootstrap:

```cmd
Sysmon64.exe -accepteula -i sysmonconfig.xml
Sysmon64.exe -c sysmonconfig.xml   :: live-reload after editing
```

### Where it sits in the defense stack

- **Below a commercial EDR**: CrowdStrike, Defender for Endpoint, and SentinelOne provide live response, behavioral detection, and managed-rule content that Sysmon alone does not.
- **Above the default Security Log**: provides command-line + parent-process + network-connection visibility the Security Log lacks.
- **The FOSS-SOC default**: Wazuh (@entities/tools/wazuh.md), Elastic, and Splunk (@entities/tools/splunk.md) all have first-class Sysmon parsers; the corpus's *Low Cost SOC* and *Open-Source SOC* PDFs (@sources/open-source-soc-guide.md) treat Sysmon-to-Wazuh as the canonical pipeline.

### Operational pitfalls

- **Config drift**: aggressive Sysmon configs (e.g., logging every network connection) can saturate a SIEM's ingest budget. Tune filter rules per environment.
- **Tamper protection**: Sysmon is not self-protecting. An attacker with SYSTEM can uninstall it (`sysmon -u`); detect that absence by alerting on missing-heartbeat or on the absence of expected Sysmon events.
- **Cross-architecture**: ship the `Sysmon64.exe` binary to 64-bit hosts and `Sysmon.exe` to 32-bit (still in the wild on legacy XP/Win7 OT environments).

## Snippets

> **Process-name vs hash hunt — Sysmon mapping** [Source: Threat Hunting 101 PDF.pdf p.5]
>
> | Basis | Source | Subsource |
> |-------|--------|-----------|
> | Process name | Security Log | Audit process tracking: 4688 |
> | Hash | Sysmon | Event 1: Process Creation |

> **Persistence — Sysmon registry events** [Source: Threat Hunting 101 PDF.pdf p.17]
>
> Registry key on the autoruns list → Sysmon `12-14`. WMI Eventing → Sysmon `19-21`. Both require Sysmon installed and configured to monitor the specific keys.

## Dead Ends

- **Naive global Sysmon install with default config** — produces unactionable noise volume. The community gravitated to SwiftOnSecurity / sysmon-modular for a reason. [CONFIRMED]
