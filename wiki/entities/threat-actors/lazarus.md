---
title: Lazarus Group (Hidden Cobra / APT38 / TraderTraitor)
type: entity
tags: [threat-actor, apt, nation-state, dprk-attributed, financial-crime, espionage]
keywords: [lazarus, hidden cobra, apt38, dprk, north korea, bluenoroff, andariel, wannacry, swift]
related:
  - entities/frameworks/mitre-attack.md
  - concepts/adversary-emulation.md
  - concepts/cyberwarfare.md
  - concepts/blockchain-security.md
  - concepts/malware-analysis.md
  - entities/people/joas-a-santos.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
---

## Relations

- @entities/frameworks/mitre-attack.md
- @concepts/adversary-emulation.md
- @concepts/cyberwarfare.md
- @concepts/blockchain-security.md
- @concepts/malware-analysis.md
- @entities/people/joas-a-santos.md

## Raw Concept

The most active financially-motivated state-sponsored APT family — unique among state actors for primary revenue-generation tasking (not just espionage). Material from the corpus's *cyberwarfare books #1.pdf* + public threat intel (FireEye/Mandiant APT38 report 2018, Treasury OFAC designations, CISA MAR series).

## Narrative

**Lazarus Group** is an umbrella label for North Korean (DPRK) state-sponsored cyber operations attributed to the **Reconnaissance General Bureau (RGB)**. Western threat-intel typically clusters DPRK activity into three overlapping groups: [NEEDS VERIFICATION 2026-05-12]

- **Lazarus** (broad espionage + destructive ops) — aliases Hidden Cobra, Whois Team, Guardians of Peace, ZINC (Microsoft, retired naming), Diamond Sleet (Microsoft current)
- **APT38 / BlueNoroff** — financially-motivated subdivision; SWIFT-network bank heists, cryptocurrency exchange theft. Microsoft naming: Sapphire Sleet.
- **Andariel** — South Korea-focused espionage subdivision. Microsoft naming: Onyx Sleet.

The boundaries are porous — tools and infrastructure overlap across the three.

### Distinguishing feature: revenue mission

Unlike Russian (espionage + influence) or Chinese (espionage + IP theft) APTs, DPRK groups have an **explicit financial mission** — sanctioned isolation makes cyber-theft a state revenue stream. Estimated $3B+ in cryptocurrency stolen 2017-2023 per Chainalysis + UN Panel of Experts reports. This makes them functionally indistinguishable from criminal financially-motivated actors at the operational layer, despite the state sponsorship.

### Notable operations (public attribution)

- **Sony Pictures Entertainment destructive attack** (2014) — wiper malware + data leak; retaliation for *The Interview* film
- **Bangladesh Bank SWIFT heist** (2016) — attempted $951M theft via the SWIFT inter-bank messaging system; $81M actually exfiltrated. Foundational case study in financial-network intrusion
- **WannaCry ransomware** (May 2017) — global outbreak via EternalBlue (SMBv1 exploit leaked from the NSA). Damages estimated at $4-8B. Attribution to Lazarus by US, UK, CA, AU, NZ governments
- **FASTCash ATM cash-out scheme** (2016-ongoing) — manipulating bank application servers to authorize fraudulent ATM withdrawals globally
- **Cryptocurrency exchange theft series** — Coincheck ($530M, 2018), KuCoin, multiple bridge attacks (Ronin Bridge $620M 2022, Harmony Horizon $100M 2022). See @concepts/blockchain-security.md
- **Operation Dream Job** (ongoing) — fake LinkedIn / job-offer social-engineering campaigns against aerospace, defense, cryptocurrency, and IT-supply-chain targets
- **3CX supply-chain compromise** (2023) — trojanized desktop client used to deliver downstream malware

### TTPs (high-level)

[MITRE ATT&CK group page G0032](https://attack.mitre.org/groups/G0032/). Distinctive:

- **Social engineering at scale** — Dream Job-style LinkedIn lures targeting specific engineers; weaponized job-spec documents
- **Custom Windows + macOS malware** — Lazarus is one of the few state actors with mature macOS capability (KandyKorn, ObjCShellz, RustBucket); aerospace + cryptocurrency = mac-heavy targets
- **Living-off-the-land + custom backdoors** — PowerShell + WMI + legitimate cloud services for C2 (Slack, Telegram bots, Dropbox)
- **Cross-platform exploit reuse** — heavy use of leaked NSA tooling (EternalBlue, DoublePulsar) extended their useful life
- **Cryptocurrency-specific tradecraft** — chain analysis evasion via mixers (Tornado Cash, sanctioned 2022), peel-chain laundering, NFT bridges

### Detection / defense priorities

- Phishing-resistant MFA (FIDO2 keys) — blunts most initial-access vectors
- Macro disabling + LinkedIn-document scrutiny in HR / recruiter workflows
- Cryptocurrency operations: cold-storage discipline, multi-sig with airgapped signers, supply-chain integrity for trading infrastructure
- See @concepts/incident-response.md for the responder playbook
