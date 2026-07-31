---
title: "Idov31/Nidhogg — Windows kernel rootkit (reference tradecraft)"
type: entity
tags: [tool, rootkit, windows, kernel, dkom, evasion, gpl-3.0, steal-from, blue-team]
keywords: [nidhogg, rootkit, dkom, activeprocesslinks, process hiding, windows kernel, mitre, mythic]
related:
  - concepts/av-edr-bypass.md
  - concepts/endpoint-detection-response.md
  - concepts/malware-analysis.md
  - concepts/privilege-escalation.md
  - concepts/red-team-operations.md
  - entities/frameworks/mitre-attack.md
  - "@osint-wiki/entities/tools/nidhogg.md"
maturity: draft
created: 2026-05-24
updated: 2026-07-31
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-36url-wiki-ingestion-2026-05-24.md"
phase_0_verdict: "Steal-from 2026-05-24 — GPL-3.0; document DKOM/process-hiding for blue-team MITRE mapping only; no binary import or production deployment."
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

# Idov31/Nidhogg — Windows kernel rootkit (reference tradecraft)

## Relations

- @concepts/av-edr-bypass.md — kernel-mode evasion surface EDR must reason about
- @concepts/endpoint-detection-response.md — detection engineering for hidden processes / tampered kernel structures
- @concepts/malware-analysis.md — static analysis of rootkit techniques without deploying payloads
- @concepts/privilege-escalation.md — persistence and concealment after Windows privesc
- @concepts/red-team-operations.md — adversary emulation context (Mythic C# integration cited in eval)
- @entities/frameworks/mitre-attack.md — map T1014 (Rootkit), T1055 (Process Injection), defense-evasion sub-techniques
- @osint-wiki/entities/tools/nidhogg.md — cross-wiki routing stub from K63 eval

## Raw Concept

Routed from K63 OSINT-wiki brief (`briefs/2026-05-24_k63-cybersec-nidhogg-from-osint.md`, 2026-05-24). `Idov31/Nidhogg` — GPL-3.0, C++, ~2.4k stars. Windows x64 kernel rootkit with 25+ features, Win10/Win11 compatible. **Steal-from** tier: extract tradecraft for defensive concepts; **do not import binaries** (copyleft + operational risk).

## Narrative

Nidhogg is an open-source **Windows kernel rootkit** used in security research to demonstrate how adversaries hide presence on endpoints. This wiki catalogs it for **blue-team detection mapping**, not for deployment.

### Tradecraft to document defensively (no binary required)

| Pattern | Defensive angle |
|---|---|
| **DKOM — `ActiveProcessLinks` unlinking** | Process visible to some APIs but missing from standard enumeration walks; hunt with cross-source process inventory (PsList vs handle table vs ETW) |
| **Process / thread / token hiding** | Gaps between user-mode tool output and kernel callbacks; correlate Sysmon Event 1 with kernel telemetry where available |
| **Mythic C# API integration** (per K63 eval) | C2 frameworks shipping kernel helpers — map to ATT&CK software pairings in threat-intel workflows |

### License and usage boundary

- **GPL-3.0** — copyleft poison pill for any production or commercial integration; same posture as `gitGraber` / `H4X-Tools` index entries (reference-only).
- **Authorized use**: read source + MITRE mapping in lab documentation; **never** load driver on production or client systems without explicit written authorization and isolated hardware.

### MITRE ATT&CK anchors [TENTATIVE — map on next deep-read]

- **T1014** Rootkit — kernel component conceals other malicious activity
- **T1562** Impair Defenses — disabling or subverting security tools from kernel mode
- Pair with @concepts/endpoint-detection-response.md for sensor-gap analysis

## Dead Ends

- **Deploying Nidhogg drivers during a client engagement without isolated lab approval** — GPL + kernel crash risk + legal exposure; use commercial adversary-emulation platforms with contractual scope instead.
- **Treating "process not in Task Manager" as clean** — DKOM specifically targets enumeration paths defenders rely on; validate with multiple instrumentation sources.
