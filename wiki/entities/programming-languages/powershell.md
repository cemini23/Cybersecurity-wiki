---
title: PowerShell (security-focused)
type: entity
tags: [windows, post-exploitation, scripting]
keywords: [powershell, empire, powerview, amsi, constrained language mode]
related:
  - concepts/windows-pentest.md
  - concepts/av-edr-bypass.md
  - concepts/red-team-operations.md
  - sources/pentest-com-powershell-overview.md
  - entities/people/joas-a-santos.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
---

## Relations

- @concepts/windows-pentest.md
- @concepts/av-edr-bypass.md
- @concepts/red-team-operations.md
- @sources/pentest-com-powershell-overview.md
- @entities/people/joas-a-santos.md

## Raw Concept

Anchored by Pentest com POWERSHELL - overview.pdf.

## Narrative

Windows-native scripting language. Central to Windows post-exploitation tradecraft. [CONFIRMED]

**Standard offensive tooling:** PowerView (AD recon), PowerSploit, Empire (legacy C2), Nishang (offensive helpers), Invoke-Mimikatz. Defenders have raised the cost of naive PowerShell offense via AMSI, ScriptBlock Logging, Constrained Language Mode, and Just Enough Administration (JEA). Modern red-team practice: bypass AMSI, run .NET assemblies via execute-assembly (Cobalt Strike) rather than raw PowerShell. See @concepts/av-edr-bypass.md.
