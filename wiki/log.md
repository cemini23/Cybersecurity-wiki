# Cybersecurity Wiki — Operations Log

Append-only chronological log of ingests, queries, and lint passes. Newest entries at the bottom.

---

## [2026-05-12] scaffold | Workspace bootstrapped from SEO wiki-template

- Forked `wiki-template/` to `~/Desktop/projects/Cybersecurity wiki/`
- Adapted `CLAUDE.md` for cybersecurity-vertical scope: offensive security + defensive operations + career/education
- Created entity subfolders: certifications, tools, frameworks, threat-actors, platforms, people, vendors, programming-languages
- Wrote README, ROADMAP, LESSONS, LICENSE, hot.md
- Added `Related Wikis` table linking `osint-wiki`, `image-gen-wiki`, `seo-wiki`, `3d-printing-wiki`
- Added cybersecurity-specific `Hands-on rules — ethics + legality` block (authorization, responsible disclosure, dual-use tools, kid-safety framing)

## [2026-05-12] ingest | Joas A Santos cybersecurity PDF corpus (227 PDFs)

- **Source**: shared Google Drive folder `ebooks Joas` (folder ID `12Mvq6kE2HJDwN2CZhEGWizyWt87YunkU`, owner joasantonio108@gmail.com)
- **Author**: Joas A Santos (Brazilian cybersecurity educator, Red Team Leader). LinkedIn: [joas-antonio-dos-santos](https://www.linkedin.com/in/joas-antonio-dos-santos/). GitHub: [CyberSecurityUP](https://github.com/CyberSecurityUP).
- **Method**: Drive API `parentId` query returned empty for shared folders, so contents were enumerated via Playwright DOM scrape (`[data-id]` attributes + tooltip-derived titles). Full inventory persisted to `.scratch/drive_inventory.tsv`
- **Pages touched** — 50+ entities/concepts + 226 source stubs:
  - **226 source stubs** generated via `scripts/build_source_stubs.py` (frontmatter + Drive file-ID provenance + read_status=unread-stub)
  - **2 validated frameworks**: MITRE ATT&CK (full deep-read from `Mitre Att&ck Study Overview.pdf`), Cyber Kill Chain (Unified Cyber Kill Chain content from `Red Team Operations – Concepts #1.pdf`)
  - **8 tool entities**: Cobalt Strike, Metasploit, Burp Suite, Caldera, Maltego, Wazuh, Nmap, BloodHound
  - **10 certification entities**: OSCP, OSWA, OSWE, CRTO, CEH, CompTIA Security+/PenTest+, eCPPT/eCPTX/eWPT
  - **5 vendor entities**: Offensive Security, eLearnSecurity, CompTIA, EC-Council, Zero-Point Security
  - **1 platform**: HackTheBox
  - **1 person**: Joas A Santos (anchor for the entire source corpus)
  - **1 threat actor**: APT28 (only named APT in the corpus)
  - **4 programming language entities**: Python, C/C++, JavaScript, PowerShell — all security-focused
  - **5 validated concepts**: Red Team Operations, Adversary Emulation, AV/EDR Bypass, Web Pentest Methodology, OSINT for Cybersecurity
  - **20+ draft concepts**: SOC Operations, Incident Response, Threat Hunting, Malware Analysis, Exploit Development, Cyber for Kids, Social Engineering, Windows Pentest, Privilege Escalation, Cloud Pentest, Mobile Pentest, Network Security, Container Security, Bug Bounty, Responsible Disclosure, Cybersecurity Careers, Anonymity Networks, Cyberwarfare, AI for Cybersecurity, Blockchain Security, Metaverse Security, Game Hacking, Zero Trust, Purple Team Operations
- **Deep-reads (anchor pages)**: 4 PDFs fully ingested:
  1. `Mitre Att&ck Study Overview.pdf` → @entities/frameworks/mitre-attack.md
  2. `Red Team Operations – Concepts #1.pdf` → @concepts/red-team-operations.md + @entities/frameworks/cyber-kill-chain.md + @concepts/adversary-emulation.md
  3. `AV and EDR Bypass Techniques for new Hackers - Update 2022.pdf` → @concepts/av-edr-bypass.md
  4. `Web PenTesting Checklist by Joas.pdf` → @concepts/web-pentest-methodology.md
- **Cross-wiki backlinks** added: web-pentest-methodology references `@seo-wiki/concepts/web-vitals.md`; osint-for-cybersecurity references `@osint-wiki/concepts/typed-relation-dependencies.md`
- **Read status**: 4 sources `deep-read`, 222 sources `unread-stub` (titles + provenance only; deep-read deferred to future sessions per the ROADMAP)
- **Maturity at write time**: 8 pages `validated` (5 concept + 2 framework + 1 person), 47 pages `draft` (will mature with future ingests + corpus deep-reads)

## [2026-05-12] cross-link | added cybersecurity-wiki backlinks to 4 sibling wikis

- Updated `osint-wiki` CLAUDE.md `Related Wikis` table → added `cybersecurity-wiki` row
- Updated `image-gen-wiki` CLAUDE.md `Related Wikis` table → added `cybersecurity-wiki` row
- Updated `seo-wiki` CLAUDE.md `Related Wikis` table → added `cybersecurity-wiki` row
- Updated `3d-printing-wiki` CLAUDE.md `Related Wikis` table → added `cybersecurity-wiki` row

## [2026-05-12] follow-ups | post-publication fixes + content expansion

- **Lint orphan fix**: improved `scripts/fix_wiki_refs.py` (3 passes, idempotent) — fixed the bidirectional-fix bug where `set_related()` failed to recognize one-space-indented `- foo` YAML list items. Result: orphans went 41 → 0, bidirectional gaps 0, dangling refs 0.
- **Deep-reads (3 more PDFs)** — upgraded the following from `draft` → `validated`:
  - `Linux Privilege Escalation – Overview.pdf` → @concepts/privilege-escalation.md (11 Linux privesc technique categories + enumeration script inventory + Windows privesc + community references)
  - `Incident response - overview.pdf` → @concepts/incident-response.md (NIST SP 800-61r2 + SANS PICERL + SOC-vs-CSIRT + DFIR tooling)
  - `INFOSEC PROEFICIENCY COLORS.pdf` → @concepts/cybersecurity-careers.md (the color taxonomy — Red/Blue/Purple/Yellow/Green/White/Orange teams, lane→role mapping, cert ladder by lane)
- **New threat-actor pages** (3): @entities/threat-actors/apt29.md (Cozy Bear / SVR), @entities/threat-actors/lazarus.md (DPRK), @entities/threat-actors/lockbit.md (RaaS criminal). Threat-actor coverage now 4 pages, spans state + criminal axes.
- **Cross-wiki fix**: replaced dangling `@seo-wiki/concepts/web-vitals.md` (page doesn't exist in SEO wiki) with `@seo-wiki/concepts/local-seo-foundations.md` (verified to exist). Cross-wiki dangling: 0.
- **Maturity counts after follow-up**: 11 pages `validated` (5 + 3 upgraded concepts + 2 framework + 1 person), 50 pages `draft`, 226 source stubs `draft + unread-stub`.
- Updated `image-gen-wiki` CLAUDE.md `Related Wikis` table → added `cybersecurity-wiki` row
- Updated `seo-wiki` CLAUDE.md `Related Wikis` table → added `cybersecurity-wiki` row
- Updated `3d-printing-wiki` CLAUDE.md `Related Wikis` table → added `cybersecurity-wiki` row
