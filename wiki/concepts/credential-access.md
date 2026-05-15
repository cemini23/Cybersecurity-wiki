---
title: "Credential Access"
type: concept
tags: [credential-access, mitre-attack, password-cracking, offensive-security]
keywords: [credential access, password cracking, hash dumping, LSASS, Mimikatz, credential harvesting, TA0006]
related:
  - concepts/privilege-escalation.md
  - concepts/windows-pentest.md
  - entities/frameworks/mitre-attack.md
  - entities/tools/metasploit.md
  - sources/password-cracking-techniques.md
maturity: draft
created: 2026-05-15
updated: 2026-05-15
---

## Raw Concept

Stub created during Redteam Kit 22-PDF ingest (2026-05-15). New source documents reference this topic area but no concept page existed. Will be filled in during subsequent deep-reads.

## Narrative

MITRE ATT&CK tactic TA0006 — techniques for stealing account credentials (usernames, passwords, hashes, tokens, Kerberos tickets). Key techniques: OS credential dumping (T1003 — LSASS memory, SAM database, NTDS.dit), brute force (T1110), password cracking (T1110.002), and unsecured credentials (T1552). Core tools: Mimikatz, Hashcat, John the Ripper, LaZagne. Critical phase in the attack lifecycle between Initial Access and Lateral Movement.

## Relations

- @concepts/privilege-escalation.md
- @concepts/windows-pentest.md
- @entities/frameworks/mitre-attack.md
- @entities/tools/metasploit.md
- @sources/password-cracking-techniques.md
