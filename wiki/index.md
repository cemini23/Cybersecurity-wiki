# Cybersecurity Wiki — Index

> Content-oriented catalog of every page in this wiki. Keep this curated by hand — it's the human-readable map.

---

## How to use this index

- **Concepts** are the *answers* (synthesized understanding of a topic). Start here when you ask "what is X?"
- **Entities** are the *nouns* (tools, certs, threat actors, people, vendors, programming languages, frameworks, platforms). Start here when you ask "tell me about X"
- **Sources** are the *raw inputs* (one page per PDF/article/repo). Mostly anchored from corresponding entity/concept pages — only browse them directly when you need provenance

---

## Concepts

### Doctrine + methodology

| Page | Maturity | Topic |
|------|----------|-------|
| @concepts/red-team-operations.md | validated | Red Team vs Pentest distinction; engagement model |
| @concepts/adversary-emulation.md | validated | APT-emulation plan structure |
| @concepts/purple-team-operations.md | draft | Red + blue collaborative engagements |
| @concepts/soc-operations.md | draft | Security Operations Center tooling + tiers |
| @concepts/incident-response.md | validated | NIST / SANS IR lifecycle |
| @concepts/threat-hunting.md | draft | Hypothesis-driven proactive detection |
| @concepts/responsible-disclosure.md | draft | Coordinated Vulnerability Disclosure + CVE process |
| @concepts/bug-bounty.md | draft | Public bounty programs + career path |
| @concepts/cybersecurity-careers.md | validated | Career map + certification ladder |
| @concepts/agent-vm-sandboxing.md | draft | LLM-driven agent-VM sandboxing framework |

### Offensive technique categories

| Page | Maturity | Topic |
|------|----------|-------|
| @concepts/web-pentest-methodology.md | validated | Web-app pentest checklist (Joas) |
| @concepts/windows-pentest.md | draft | Windows + Active Directory + O365 |
| @concepts/cloud-pentest.md | draft | AWS / Azure / GCP / O365 pentest |
| @concepts/mobile-pentest.md | draft | Android + iOS app pentest |
| @concepts/network-security.md | draft | Network / firewall / wireless / IoT / OT |
| @concepts/exploit-development.md | draft | Buffer overflow → ROP → kernel exploits |
| @concepts/av-edr-bypass.md | validated | AV/EDR evasion tradecraft |
| @concepts/privilege-escalation.md | validated | Linux + Windows privesc |
| @concepts/social-engineering.md | draft | Phishing + vishing + pretexting |
| @concepts/osint-for-cybersecurity.md | validated | Pre-engagement + threat-intel OSINT |
| @concepts/container-security.md | draft | Docker + Kubernetes attack/defense |
| @concepts/dns-server-discovery-vs-subdomain-enumeration.md | draft | DNS recon distinction (server discovery vs subdomain enum) |

### Defensive + analytical

| Page | Maturity | Topic |
|------|----------|-------|
| @concepts/malware-analysis.md | draft | Static + dynamic malware RE |

### Emerging / cross-domain

| Page | Maturity | Topic |
|------|----------|-------|
| @concepts/ai-for-cybersecurity.md | draft | LLM use in red + blue workflows |
| @concepts/llm-vulnerability-discovery.md | draft | LLM-driven vuln-discovery pipeline (Detect→Attack) |
| @concepts/llm-adversarial-fuzzing.md | draft | Adversarial LLM testing methodology (FuzzyAI umbrella) |
| @concepts/pair-prompt-pattern.md | draft | PAIR — single-turn LLM jailbreak (arXiv 2310.08419) |
| @concepts/crescendo-multi-turn-jailbreak.md | draft | Multi-turn LLM escalation attack (arXiv 2404.01833) |
| @concepts/llm-pentest-automation.md | draft | Tier 1/2 LLM pentest automation + scope-enforcement model |
| @concepts/blockchain-security.md | draft | Smart-contract + DeFi security |
| @concepts/metaverse-security.md | draft | VR / AR / immersive platform risk |
| @concepts/game-hacking.md | draft | Anti-cheat bypass as RE practice |
| @concepts/zero-trust.md | draft | Identity-centric defense architecture |
| @concepts/cyberwarfare.md | draft | Nation-state cyber operations |
| @concepts/anonymity-networks.md | draft | Tor + I2P |

### Education + ethics

| Page | Maturity | Topic |
|------|----------|-------|
| @concepts/cyber-for-kids.md | draft | Parent + teacher + LE-facing kid-safety material |

---

## Entities

### Frameworks

| Page | Maturity |
|------|----------|
| @entities/frameworks/mitre-attack.md | validated |
| @entities/frameworks/cyber-kill-chain.md | validated |

### Certifications

| Page | Maturity | Vendor |
|------|----------|--------|
| @entities/certifications/oscp.md | draft | Offensive Security |
| @entities/certifications/oswa.md | draft | Offensive Security |
| @entities/certifications/oswe.md | draft | Offensive Security |
| @entities/certifications/crto.md | draft | Zero-Point Security |
| @entities/certifications/ceh.md | draft | EC-Council |
| @entities/certifications/comptia-security-plus.md | draft | CompTIA |
| @entities/certifications/comptia-pentest-plus.md | draft | CompTIA |
| @entities/certifications/ecppt.md | draft | eLearnSecurity / INE |
| @entities/certifications/ecptx.md | draft | eLearnSecurity / INE |
| @entities/certifications/ewpt.md | draft | eLearnSecurity / INE |

### Tools

| Page | Maturity | Role |
|------|----------|------|
| @entities/tools/cobalt-strike.md | draft | Commercial C2 |
| @entities/tools/metasploit.md | draft | FOSS exploitation framework |
| @entities/tools/burp-suite.md | draft | Web-app testing proxy |
| @entities/tools/caldera.md | draft | Adversary emulation automation |
| @entities/tools/maltego.md | draft | OSINT graph analysis |
| @entities/tools/wazuh.md | draft | FOSS SIEM / host-IDS |
| @entities/tools/nmap.md | draft | Network scanner |
| @entities/tools/bloodhound.md | draft | AD attack-path graph |
| @entities/tools/cua.md | validated | Agent-VM sandbox (Apple Virtualization + Lume) |
| @entities/tools/fuzzyai.md | validated | LLM adversarial fuzz framework (CyberArk, Apache-2.0) |
| @entities/tools/pentest-ai-agents.md | validated | LLM-driven red-team automation (MIT) |
| @entities/tools/pydns-scanner.md | validated | DNS server discovery (ethical-use addendum) |

### Vendors

| Page | Maturity |
|------|----------|
| @entities/vendors/offensive-security.md | draft |
| @entities/vendors/elearnsecurity.md | draft |
| @entities/vendors/comptia.md | draft |
| @entities/vendors/ec-council.md | draft |
| @entities/vendors/zeropoint-security.md | draft |

### Platforms (labs / CTF)

| Page | Maturity |
|------|----------|
| @entities/platforms/hackthebox.md | draft |

### Programming languages

| Page | Maturity | Role |
|------|----------|------|
| @entities/programming-languages/python.md | draft | Scripting + automation |
| @entities/programming-languages/c.md | draft | Exploit dev + AV/EDR bypass |
| @entities/programming-languages/javascript.md | draft | Web exploitation + Node.js |
| @entities/programming-languages/powershell.md | draft | Windows post-exploitation |

### Threat actors

| Page | Maturity | Region |
|------|----------|--------|
| @entities/threat-actors/apt28.md | draft | Russia-attributed (GRU) |
| @entities/threat-actors/apt29.md | draft | Russia-attributed (SVR) |
| @entities/threat-actors/lazarus.md | draft | DPRK-attributed (RGB) |
| @entities/threat-actors/lockbit.md | draft | Criminal RaaS (Russian-language) |

### People

| Page | Maturity | Role |
|------|----------|------|
| @entities/people/joas-a-santos.md | validated | Corpus author |

---
- [xullexer/PYDNS-Scanner — async DNS recon (Slipstream + SlipNet)](entities/pydns-scanner-xullexer.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [0xSteph/pentest-ai-agents — shell-only Claude Code subagents for pentest workflows](entities/pentest-ai-agents-0xsteph.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [apktool-mcp-server — Android Reverse Engineering via MCP](entities/apktool-mcp-server.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [T-Pot — Multi-Honeypot Deception Framework](entities/tpotce.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Decepticon — Autonomous Red-Team Multi-Agent Framework](entities/decepticon.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Claude-Red — Offensive Security Skills Library for Claude Code](entities/claude-red-offensive-skills.md) — cross-wiki stub routed from ingest — `cross-wiki`

## Sources

227 source pages live in `sources/` — one per PDF in the seed Joas A Santos corpus. They're not individually catalogued here; instead, each entity and concept page lists the sources that synthesize into it under `related:`. Browse `sources/` directly for provenance lookups.

The corpus inventory (file ID + title for every PDF) lives at `.scratch/drive_inventory.tsv` (gitignored — see `ROADMAP.md` for the storage decision).

---

## Cross-wiki anchors

When this wiki references a sibling wiki's page, the citation uses `@<alias>/path/to/page.md`. Aliases:

- `osint-wiki` — financial / quant / prediction-market research
- `image-gen-wiki` — uncensored image generation, ComfyUI, LoRA
- `seo-wiki` — local SEO, GBP, GEO/AEO, web design
- `3d-printing-wiki` — FDM/FFF, Bambu, slicers, print farms

Bidirectional invariant: if this wiki cites `@osint-wiki/...`, the matching page in the OSINT wiki should cite `@cybersecurity-wiki/...` back. Run `python3 scripts/wiki_lint.py` to check.
