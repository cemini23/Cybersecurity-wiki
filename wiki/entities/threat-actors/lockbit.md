---
title: LockBit (LockBit 3.0 / LockBit Black)
type: entity
tags: [threat-actor, ransomware, raas, criminal, financially-motivated]
keywords: [lockbit, raas, ransomware-as-a-service, lockbit 3.0, lockbit black, operation cronos]
related:
  - entities/frameworks/mitre-attack.md
  - concepts/incident-response.md
  - concepts/malware-analysis.md
  - concepts/responsible-disclosure.md
  - concepts/windows-pentest.md
  - concepts/ransomware.md
  - entities/people/joas-a-santos.md
  - sources/ransomware-investigation-runbook.md
maturity: draft
created: 2026-05-12
updated: 2026-05-17
---

## Relations

- @entities/frameworks/mitre-attack.md
- @concepts/incident-response.md
- @concepts/malware-analysis.md
- @concepts/responsible-disclosure.md
- @concepts/windows-pentest.md
- @concepts/ransomware.md
- @entities/people/joas-a-santos.md
- @sources/ransomware-investigation-runbook.md

## Raw Concept

Non-state criminal threat-actor entry. The corpus does not have a dedicated LockBit PDF, but ransomware shows up across @concepts/malware-analysis.md, @sources/ransomware-investigation-osint-and-hunting-overview-pt1.md. This page covers the dominant ransomware family of 2020-2024 because most IR playbooks will encounter LockBit-affiliated intrusions.

## Narrative

**LockBit** is a Russian-language-using **ransomware-as-a-service (RaaS)** operation that dominated the criminal ransomware ecosystem from 2020 through Q1 2024. Tracked as **LockBit 1.0 → 2.0 (Red) → 3.0 (Black) → Green** across affiliate generations. [NEEDS VERIFICATION 2026-05-12]

### RaaS model

LockBit's operating model is the canonical RaaS template:

- **Operators** (core group) — develop + maintain the encryptor, the data-leak site, the affiliate panel, and the negotiation infrastructure
- **Affiliates** (typically dozens to hundreds, vetted via Russian-language forums) — gain initial access to victim networks themselves (typically via valid-account purchases, RDP brute force, public-facing CVE exploitation) → deploy the LockBit encryptor → split ransom payments roughly 80/20 with the operators
- This decouples operators from operational risk and makes attribution complicated — different affiliates have wildly different TTPs while sharing one encryptor signature

### Notable operations + impact

- **2,500+ confirmed victims** during peak years (2022-2023) per Justice Dept disclosures
- High-profile incidents: ICBC (Industrial and Commercial Bank of China) US subsidiary 2023, Boeing 2023, Royal Mail (UK) 2023, NHS supply-chain (via Synnovis affiliate) 2024, City of Oakland 2023, multiple municipal + healthcare orgs
- **Operation Cronos** (February 2024) — UK NCA, FBI, Europol coordinated takedown: data-leak-site seizure, affiliate panel access disclosed, decryption keys distributed, alleged operator (LockBitSupp / Dmitry Khoroshev) identified + sanctioned. The infrastructure was rebuilt within a week but reputational damage in the criminal community has been lasting.

### TTPs (high-level)

[MITRE ATT&CK group page G1029](https://attack.mitre.org/groups/G1029/). Variable per affiliate, but characteristic:

- **Initial access:** valid-account purchases from Initial Access Brokers, CVE exploitation (Fortinet, Citrix, Microsoft Exchange, Confluence, ESXi), RDP brute-force
- **Discovery + lateral movement:** [BloodHound](../tools/bloodhound.md), AdFind, Mimikatz, PsExec, SoftPerfect Network Scanner
- **Defense evasion:** Cobalt Strike Beacon for C2, BYOVD attacks against EDR (KillAV via vulnerable Windows drivers), shadow-copy deletion via vssadmin
- **Impact:** double extortion (encrypt + threaten to leak), occasional triple extortion (encrypt + leak + DDoS); ESXi targeting via custom Linux encryptor variants; self-spreading variant introduced in 2022 (LockBit 2.0 worm capability)

### Defender priorities

- Patch the **specific CVEs** in the LockBit affiliate playbook within the disclosure window (Fortinet SSL-VPN, Citrix NetScaler, Confluence, MOVEit, Microsoft Exchange ProxyShell, ESXi)
- Disable RDP for internet-facing systems; force MFA on remaining RDP
- Immutable backups (3-2-1-1-0 rule: 3 copies, 2 media, 1 offsite, 1 immutable, 0 verification errors)
- EDR with tamper protection + behavioral detection (not pure signature) — LockBit's BYOVD kill-AV path requires kernel-level visibility
- Macro disabling + LinkedIn-document scrutiny in HR / recruiter workflows
- **IR playbook** — see @concepts/incident-response.md. Ransomware response has its own well-developed playbook tree distinct from generic intrusion IR (negotiator engagement, OFAC sanction check before payment, decryptor inventory at [No More Ransom](https://www.nomoreransom.org/), forensic preservation before recovery from backup)
- **Don't pay if avoidable** — payment doesn't guarantee decryption, funds future attacks, and may violate OFAC sanctions (LockBit operators sanctioned 2024)

### See also

- [No More Ransom project](https://www.nomoreransom.org/) — free decryptors for many ransomware families
- CISA #StopRansomware advisories (per-strain TTPs + IOCs)
- Coveware quarterly ransomware reports (industry trend data)
