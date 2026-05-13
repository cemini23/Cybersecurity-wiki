---
title: Metasploit Framework
type: entity
tags: [exploitation, framework, foss, rapid7]
keywords: [metasploit, msf, msfvenom, meterpreter, rapid7, h.d. moore]
related:
  - concepts/exploit-development.md
  - concepts/red-team-operations.md
  - concepts/av-edr-bypass.md
  - sources/ebook-invadindo-com-metasploit-vl-1.md
  - sources/pentest-with-metasploit-overview.md
  - entities/people/joas-a-santos.md
  - entities/tools/pentest-ai-agents.md
maturity: draft
created: 2026-05-12
updated: 2026-05-13
---

## Relations

- @concepts/exploit-development.md
- @concepts/red-team-operations.md
- @concepts/av-edr-bypass.md
- @sources/ebook-invadindo-com-metasploit-vl-1.md
- @sources/pentest-with-metasploit-overview.md
- @entities/people/joas-a-santos.md
- @entities/tools/pentest-ai-agents.md

## Raw Concept

Cited across the corpus as the standard FOSS exploitation framework. Stub anchored to two corpus PDFs (ebook Invadindo com Metasploit VL 1 + Pentest with metasploit - overview).

## Narrative

Open-source exploitation framework maintained by Rapid7, originally created by H.D. Moore in 2003. The default toolbox for opportunistic exploitation and post-exploitation. [CONFIRMED]

**Core components:**
- **msfconsole** — interactive console for selecting/configuring/running modules
- **msfvenom** — payload generator (encoders, formats, templates). Cited in the corpus for AV-bypass workflows where stock payloads get signatured immediately
- **Meterpreter** — interactive payload supporting in-memory operation, port forwarding, hash dumping, screenshot/keylogger, etc.

**Module taxonomy:** exploit / auxiliary / post / encoder / nop / payload / evasion / post-exploitation. ~2000+ exploit modules; auxiliary scanners cover most enumeration tasks.

**Where it falls short for modern engagements:** default Meterpreter/msfvenom payloads are signatured by every vendor. For red team / adversary-emulation work, Metasploit is most useful for *initial access* + lab scenarios — operators typically shift to Cobalt Strike, Sliver, or Mythic for the C2 / post-exploitation phase. See @entities/tools/cobalt-strike.md.
