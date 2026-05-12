---
title: C / C++ (security-focused)
type: entity
tags: [systems, exploit-dev, low-level]
keywords: [c, c++, buffer overflow, shellcode, windows api]
related:
  - concepts/av-edr-bypass.md
  - concepts/exploit-development.md
  - concepts/game-hacking.md
  - concepts/malware-analysis.md
  - entities/people/joas-a-santos.md
  - sources/c-for-hackers-overview-pt.md
  - sources/c-for-pentest.md
  - sources/programacao-c-e-c-para-seguranca-ofensiva-digital.md
  - sources/programming-language-for-hacking-books.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
---

## Relations

- @concepts/av-edr-bypass.md
- @concepts/exploit-development.md
- @concepts/game-hacking.md
- @concepts/malware-analysis.md
- @entities/people/joas-a-santos.md
- @sources/c-for-hackers-overview-pt.md
- @sources/c-for-pentest.md
- @sources/programacao-c-e-c-para-seguranca-ofensiva-digital.md
- @sources/programming-language-for-hacking-books.md


## Raw Concept

Two corpus PDFs anchor (C for Hackers - Overview PT + Programação C e C++ para Segurança Ofensiva).

## Narrative

Foundational for buffer overflow + exploit development + AV/EDR bypass tradecraft + shellcode + Windows API manipulation. [CONFIRMED]

**Why it's central:** every modern OS kernel is C; the Windows API is C-callable; most EDR-evasion techniques (process injection, syscall stubs, indirect-syscall jump tables, DLL unhooking) ship as C/C++ proof-of-concept code. See @concepts/exploit-development.md and @concepts/av-edr-bypass.md.
