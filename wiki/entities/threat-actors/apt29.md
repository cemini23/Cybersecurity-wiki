---
title: APT29 (Cozy Bear / Nobelium / Midnight Blizzard)
type: entity
tags: [threat-actor, apt, nation-state, russia-attributed, espionage]
keywords: [apt29, cozy bear, nobelium, midnight blizzard, the dukes, ymentous, svr, russia]
related:
  - entities/frameworks/mitre-attack.md
  - entities/threat-actors/apt28.md
  - concepts/adversary-emulation.md
  - concepts/cyberwarfare.md
  - concepts/red-team-operations.md
  - entities/people/joas-a-santos.md
  - concepts/threat-intelligence.md
maturity: draft
created: 2026-05-12
updated: 2026-05-17
---

## Relations

- @entities/frameworks/mitre-attack.md
- @entities/threat-actors/apt28.md
- @concepts/adversary-emulation.md
- @concepts/cyberwarfare.md
- @concepts/red-team-operations.md
- @entities/people/joas-a-santos.md
- @concepts/threat-intelligence.md

## Raw Concept

Companion threat-actor page to @entities/threat-actors/apt28.md. APT29 is the second of the two named Russian APT clusters most-cited in adversary-emulation work — often the more interesting target because their tradecraft trades operational tempo for stealth.

## Narrative

APT29 — aliases **Cozy Bear**, **Nobelium**, **Midnight Blizzard** (Microsoft current naming), **The Dukes**, **YTTRIUM**, **Iron Hemlock** — is a Russian state-sponsored cyberespionage group attributed by Western intelligence agencies to the **SVR** (Russian Foreign Intelligence Service). [NEEDS VERIFICATION 2026-05-12]

### Contrast with APT28

| Dimension | APT28 (Fancy Bear / GRU) | APT29 (Cozy Bear / SVR) |
|-----------|--------------------------|--------------------------|
| Attribution | GRU Unit 26165 (military) | SVR (foreign intelligence) |
| Operational style | Aggressive, fast, willing to be detected | Slow, quiet, prolonged dwell time |
| Targeting | NATO, military, election infrastructure | Foreign ministries, think tanks, COVID/vaccine R&D, tech-supply-chain |
| Distinguishing TTPs | Spearphishing + 0day + custom malware (X-Agent) | Living-off-the-land, supply-chain attacks, custom malware suites refreshed often |

### Notable operations (public attribution)

- **SolarWinds supply-chain compromise** (2020) — backdoored Orion update affected ~18,000 organizations including US federal agencies (Treasury, Commerce, DHS, DoJ, parts of DoD). Custom implants: **SUNBURST**, **TEARDROP**, **GoldMax**, **GoldFinder**, **Sibot**, **Sunshuttle**. [Source: CISA Alert AA20-352A, Microsoft MSTIC reports]
- **DNC intrusions** (2015-2016) — operated alongside APT28 in the US election interference campaigns.
- **Norwegian government / Dutch Safety Board** (2017) — investigation-related targeting.
- **COVID-19 vaccine R&D targeting** (2020) — UK NCSC / CISA joint advisory on pharma + medical-research targeting.
- **Microsoft / HPE source-code access** (2024) — credential-spray + abuse of OAuth applications to access executive emails + source code repositories.

### TTPs (high-level, MITRE-keyed)

[MITRE ATT&CK group page G0016](https://attack.mitre.org/groups/G0016/) is the canonical mapping. Notable techniques:

- **Initial access:** T1190 (exploit public-facing app), T1078 (valid accounts via password spray), T1195 (supply chain — SolarWinds being the textbook case)
- **Persistence:** T1098 (Azure AD identity persistence via app registrations + service principals), T1547 (boot/logon)
- **Defense evasion:** T1027 (custom packed implants), T1078.004 (cloud accounts), T1218 (signed-binary proxy)
- **Credential access:** T1110 (password spray), T1552 (unsecured credentials), Pass-the-Cookie for cloud identity
- **C2:** custom protocols layered over HTTPS, frequent infrastructure rotation

### Adversary emulation plans

- [MITRE Engenuity Center for Threat-Informed Defense — APT29 emulation plan](https://github.com/center-for-threat-informed-defense/adversary_emulation_library) (Round 2 of the ATT&CK evaluations was built around APT29 TTPs)
- [SCYTHE community threats — APT29 entries](https://github.com/scythe-io/community-threats)
- AttackIQ + Picus Security both publish managed APT29 emulation packages

### Detection priority

APT29's signature is **patience** — successful detection usually requires:

1. Strong identity-anomaly detection (impossible travel, atypical OAuth grants, service principal abuse)
2. Long-window correlation (90-day lookbacks for low-and-slow credential reuse)
3. Supply-chain integrity monitoring (signed-binary anomalies, SBOM verification)
4. Mature SIEM correlation (Wazuh / Splunk / Sentinel) — see @concepts/soc-operations.md
