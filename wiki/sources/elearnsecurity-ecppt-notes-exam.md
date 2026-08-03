---
title: "eLearnSecurity eCPPT Notes Exam"
type: source
tags: [cybersecurity, joas-corpus, ecppt, deep-read]
keywords: [ecppt, nmap, metasploit, ms17-010, pivoting, proxychains, buffer overflow, reporting]
related:
  - concepts/network-security.md
  - entities/certifications/ecppt.md
  - entities/people/joas-a-santos.md
  - entities/vendors/elearnsecurity.md
  - concepts/buffer-overflow.md
  - concepts/exploit-development.md
maturity: validated
created: 2026-05-12
updated: 2026-08-03
read_status: deep-read
---

## Relations

- @concepts/network-security.md
- @entities/certifications/ecppt.md
- @entities/people/joas-a-santos.md
- @entities/vendors/elearnsecurity.md
- @concepts/buffer-overflow.md
- @concepts/exploit-development.md

## Raw Concept

- **Title:** eCPPT (eLearnSecurity Certified Professional Penetration Tester) – Notes Exam
- **Author:** Joas A Santos (compiled exam notes)
- **Type:** 157-page PDF notes dump
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/elearnsecurity-ecppt-notes-exam.pdf` (archived 2026-08-03; Drive ID retained in prior revisions)
- **Retrieved:** 2026-05-12; deep-read 2026-08-02 (full PDF; systematic sample of sections)
- **Read status:** deep-read

## Narrative

**Warning on p.2:** these are content notes that *may* help the exam; they are **not** a guaranteed method list to pass.

**Lab simulation pointers:** VulnHub, HackTheBox, TryHackMe, overgrowncarrot1 eCPPT Labs CTB, CyberSecurityUP Buffer-Overflow-Labs.

Major blocks observed:

| Theme | Examples in notes |
|-------|-------------------|
| Recon | Large Nmap command catalog (SYN/FIN/version/OS, top-ports, intense scans, output `-oA`/`-oN`) |
| Metasploit recon | `RHOSTS` ranges; `THREADS` guidance; `db_nmap` / `db_import`; built-in portscan auxiliaries |
| Service enum | SMB version, SSH version, FTP anonymous, Dirb web content |
| Exploitation | **MS17-010** family (`psexec` with creds, `eternalblue`, admin command module) with decision tree (domain user vs local vs validation) |
| Priv-esc | Metasploit local exploit suggester patterns |
| Pivoting | Meterpreter + `autoroute` + `socks_proxy` + **proxychains** nmap/smbmap into secondary nets |
| Buffer overflow | Classic EIP overwrite narrative; lab prereqs (Kali + Windows VM, Defender off for learning labs) |
| Reporting | Fix research per finding; strategic recommendations beyond one-off patches (monitoring, least privilege) |

Treat as a **personal cram dump**, not vendor canon. Cross-check live INE/eLearnSecurity syllabus and lab rules before exam day. [CONFIRMED — PDF deep-read sampling across full 157 pages]

## Snippets

```text
MS17-010 choice guidance (notes ~p.28–29):
1. Domain user creds → want admin on host: exploit/windows/smb/ms17_010_psexec (+ creds)
2. Local user creds → want admin: auxiliary/admin/smb/ms17_010_command path noted
3. Validate vuln exists with stable exploit: exploit/windows/smb/ms17_010_eternalblue
```

[Source: elearnsecurity-ecppt-notes-exam.pdf ~p.28–29]

```text
Pivoting pattern: meterpreter sessions → post/multi/manage/autoroute (target subnet)
→ auxiliary/server/socks_proxy → proxychains nmap/smbmap on next hop
```

[Source: elearnsecurity-ecppt-notes-exam.pdf ~p.32–38]

```text
Reporting close: research most efficient fix per system; add strategic recommendations
(better monitoring if RT undetected; access control if excessive privileges)
```

[Source: elearnsecurity-ecppt-notes-exam.pdf ~p.156]
