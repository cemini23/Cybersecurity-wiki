---
title: Privilege Escalation
type: concept
tags: [post-exploitation, linux, windows]
keywords: [privilege escalation, linpeas, winpeas, kernel exploit, sudo abuse]
related:
  - concepts/windows-pentest.md
  - concepts/exploit-development.md
  - sources/linux-privilege-escalation-overview.md
  - sources/windows-privilege-escalation-overview.md
  - sources/conceitos-basicos-de-pos-exploracao-1.md
  - sources/introducao-a-pos-exploracao.md
  - entities/people/joas-a-santos.md
  - entities/certifications/oscp.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
---

## Relations

- @concepts/windows-pentest.md
- @concepts/exploit-development.md
- @sources/linux-privilege-escalation-overview.md
- @sources/windows-privilege-escalation-overview.md
- @sources/conceitos-basicos-de-pos-exploracao-1.md
- @sources/introducao-a-pos-exploracao.md
- @entities/people/joas-a-santos.md
- @entities/certifications/oscp.md

## Raw Concept

Anchored by Linux + Windows privesc PDFs + two post-exploitation overviews.

## Narrative

Privilege Escalation = going from initial low-privilege foothold to higher privileges (typically root / SYSTEM / Domain Admin). Splits cleanly by OS: **Linux** — SUID binaries (GTFOBins reference), sudo misconfig, weak file permissions, kernel exploits, capability abuse, cron jobs, NFS no_root_squash, container escapes. **Windows** — service misconfigurations (AlwaysInstallElevated, modifiable service binaries, unquoted service paths), token impersonation (RoguePotato / PrintSpoofer family), DLL hijacking, kernel exploits, scheduled-task abuse. Standard enumeration: LinPEAS / WinPEAS, PowerUp, Seatbelt. See @concepts/windows-pentest.md.
