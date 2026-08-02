---
title: eCPPT (eLearnSecurity Certified Professional Penetration Tester)
type: entity
tags: [mid-level, hands-on, elearnsecurity]
keywords: [ecppt, elearnsecurity, ine, ptp]
related:
  - entities/vendors/elearnsecurity.md
  - concepts/red-team-operations.md
  - sources/elearnsecurity-ecppt-notes-exam.md
  - entities/people/joas-a-santos.md
  - concepts/buffer-overflow.md
  - concepts/exploit-development.md
  - concepts/network-security.md
maturity: draft
created: 2026-05-12
updated: 2026-08-02
---

## Relations

- @entities/vendors/elearnsecurity.md
- @concepts/red-team-operations.md
- @sources/elearnsecurity-ecppt-notes-exam.md — Joas exam notes deep-read 2026-08-02 (157p)
- @entities/people/joas-a-santos.md
- @concepts/buffer-overflow.md — classic stack BOF still in exam surface
- @concepts/exploit-development.md
- @concepts/network-security.md — recon / pivoting spine of notes

## Raw Concept

Anchored by eLearnSecurity eCPPT Notes Exam.pdf (Joas). Deep-read 2026-08-02 upgraded notes source; this page remains cert-overview (not a full syllabus scrape from INE).

## Narrative

eLearnSecurity / INE's mid-level hands-on pentest cert. Paired with the PTP (Penetration Testing Professional) course. [CONFIRMED]

**Format:** 7-day lab + 7-day reporting window. Less time-pressured than OSCP, but the report is weighted heavily and must be professional-grade. Strong on Active Directory + buffer overflow content. Sister cert: eCPTX (advanced).

### Study surface (from Joas notes deep-read — not official syllabus)

Operator notes emphasize: heavy **Nmap** catalog → **Metasploit** recon/aux scanners → service enum (SMB/SSH/FTP/web Dirb) → **MS17-010** exploit choice tree → Meterpreter **priv-esc** → **autoroute + socks + proxychains** pivoting → **buffer overflow** lab block → **reporting** with strategic recommendations. Treat as a community cram map; verify against current INE exam guide before sitting. [CONFIRMED — notes structure; TENTATIVE as official domain weights]

Lab practice pointers commonly cited: VulnHub, HTB, TryHackMe, Buffer-Overflow-Labs repos — always authorized environments only.
