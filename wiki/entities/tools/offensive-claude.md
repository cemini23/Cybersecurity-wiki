---
title: "offensive-claude — dedicated offensive-security Claude Code workstation"
type: entity
tags: [tool, offensive-security, claude-code, skill-modules, red-team, exploit-dev, web-pentest, cloud-security, recon]
keywords: [offensive-claude, hypnguyen1209, claude code config, offensive security, skill modules, sub-agents, vulnerability patterns, opus tier]
related:
  - concepts/llm-pentest-automation.md
  - concepts/red-team-operations.md
  - entities/tools/pentest-ai-agents.md
  - entities/tools/kali-linux.md
  - concepts/ai-for-cybersecurity.md
  - entities/tools/reverse-skill.md
  - entities/tools/black-cat.md
maturity: draft
created: 2026-05-21
updated: 2026-08-03
cross-wiki-source: "@osint-wiki/sources/analyzing-github-projects-agentic-infra-2026-05-21.md"
---

# offensive-claude — dedicated offensive-security Claude Code workstation

## Relations


- @entities/tools/black-cat.md — K220 hypothesis-ledger skill pattern (Steal-from; no clone)
- @concepts/llm-pentest-automation.md — skill-module taxonomy comparison
- @concepts/red-team-operations.md — C2 infrastructure + persistence + LOLBins modules
- @entities/tools/pentest-ai-agents.md — competing Claude Code offensive framework
- @entities/tools/kali-linux.md — traditional tool catalog vs. LLM-driven skill catalog
- @concepts/ai-for-cybersecurity.md — LLM-driven offensive tooling ecosystem

## Raw Concept

Routed from K56 OSINT-wiki ingest (2026-05-21). Claude Code configuration package transforming standard Claude Code into a dedicated offensive-security workstation. One-liner global curl install. 25 skill modules + 6 sub-agents + 46 vulnerability pattern reference files. Targets Opus tier.

## Narrative

`hypnguyen1209/offensive-claude` transforms the standard Claude Code interface into a dedicated offensive-security workstation via a one-liner global curl install. 25 skill modules + 6 sub-agents + 46 vulnerability pattern reference files. Targets Opus tier.

Eight skill module classifications:

1. **recon-osint** — Subdomain enumeration, CVE intel, breach data, DNS history, Shodan/Censys
2. **vulnerability-analysis** — Taint analysis, source-sink tracing, false positive discipline
3. **exploit-development** — ROP chains, heap exploitation, custom shellcode, mitigation bypass
4. **reverse-engineering** — IDA/Ghidra, Frida, angr, anti-RE bypass
5. **web-pentest** — SQLi/XSS/SSRF/race conditions/GraphQL/business logic
6. **network-attack** — AD exploitation, lateral movement, pivoting, wireless
7. **red-team-ops** — C2 infrastructure, persistence, privilege escalation, LOLBins, exfil
8. **cloud-security** — AWS/Azure/GCP escalation, container escape, K8s compromise, IaC review

Direct competitor to `pentest-ai-agents` — comparison of module taxonomy vs. agent taxonomy is a useful architectural analysis. The skill-module approach (offensive-claude) is more monolithic and curated; the agent-framework approach (pentest-ai-agents) is more composable and extensible.
