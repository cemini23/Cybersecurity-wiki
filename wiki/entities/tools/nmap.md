---
title: Nmap + Nmap Scripting Engine
type: entity
tags: [recon, network-scanner, foss, industry-standard]
keywords: [nmap, nse, scanning, port scan, service detection]
related:
  - concepts/network-security.md
  - concepts/web-pentest-methodology.md
  - entities/people/joas-a-santos.md
  - entities/tools/pydns-scanner.md
  - entities/tools/pentest-ai-agents.md
  - concepts/dns-server-discovery-vs-subdomain-enumeration.md
maturity: draft
created: 2026-05-12
updated: 2026-05-13
---

## Relations

- @concepts/network-security.md
- @concepts/web-pentest-methodology.md
- @entities/people/joas-a-santos.md
- @entities/tools/pydns-scanner.md
- @entities/tools/pentest-ai-agents.md
- @concepts/dns-server-discovery-vs-subdomain-enumeration.md

## Raw Concept

Cited implicitly across the pentest corpus. Stub for completeness.

## Narrative

De-facto network discovery + port-scanning tool. Default for the recon phase of every engagement. Notable subsystems: NSE (Nmap Scripting Engine, ~600+ Lua scripts for vuln-detection and service-specific enumeration), Ndiff (diffing two scans), Nping (packet crafting). [CONFIRMED]

Standard recon-phase combinations: `-sV -sC -p- -T4` (all ports + service detection + default scripts), `--script vuln` (vulnerability NSE bundle), `-O` (OS fingerprinting). Output formats (`-oN/-oX/-oG/-oA`) feed cleanly into other tools like sqlmap, gobuster, BloodHound.
