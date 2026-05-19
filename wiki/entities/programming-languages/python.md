---
title: Python (security-focused)
type: entity
tags: [scripting, automation, tooling]
keywords: [python, scapy, impacket, pwntools]
related:
  - concepts/exploit-development.md
  - concepts/osint-for-cybersecurity.md
  - sources/python-for-hackers-bootcamp.md
  - sources/python-for-hackers-pt-1.md
  - sources/python-libs-for-security-pt-1.md
  - sources/python-ethical-hacking-masterclass.md
  - entities/people/joas-a-santos.md
maturity: draft
created: 2026-05-12
updated: 2026-05-19
---

## Relations

- @concepts/exploit-development.md
- @concepts/osint-for-cybersecurity.md
- @sources/python-for-hackers-bootcamp.md
- @sources/python-for-hackers-pt-1.md
- @sources/python-libs-for-security-pt-1.md
- @sources/python-ethical-hacking-masterclass.md — video course teaching Python from scratch alongside the offensive workflow
- @entities/people/joas-a-santos.md

## Raw Concept

Three corpus PDFs anchor this (Python for Hackers Bootcamp, PYTHON FOR HACKERS PT 1, Python Libs for Security PT.1).

## Narrative

De-facto scripting language for cybersecurity work. Used across nearly every offensive + defensive workflow. [CONFIRMED]

**Notable security libraries (Joas corpus + community standard):**
- **Scapy** — packet crafting, sniffing, dissection
- **Impacket** — Windows protocols (SMB, MS-RPC, Kerberos) → smbexec, secretsdump, GetUserSPNs, ntlmrelayx
- **pwntools** — CTF + exploit-development helpers
- **requests** — HTTP — the foundation of web-pentest scripting
- **paramiko** — SSH automation
- **PyCryptodome / cryptography** — crypto primitives
- **frida / pyfrida** — runtime instrumentation (mobile + Windows)
