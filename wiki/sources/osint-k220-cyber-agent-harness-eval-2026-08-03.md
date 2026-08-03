---
title: "OSINT K220 — cyber/agent-harness revenue eval (cross-wiki)"
type: source
tags: [cross-wiki, tool-eval, k220, recon, red-team, lab, osint]
keywords: [cloakquest3r, damn-vulnerable-drone, hacktools, raccoon, black-cat, bypassav, torbot, awesome-hacking]
related:
  - entities/tools/cloakquest3r.md
  - entities/tools/damn-vulnerable-drone.md
  - entities/tools/hacktools.md
  - entities/tools/raccoon.md
  - entities/tools/black-cat.md
  - entities/tools/bypassav.md
  - entities/tools/torbot.md
  - entities/tools/cf-hero.md
  - concepts/osint-for-cybersecurity.md
  - concepts/web-pentest-methodology.md
  - concepts/av-edr-bypass.md
  - concepts/ai-pentest-harness-landscape.md
  - concepts/llm-pentest-automation.md
  - concepts/owned-target-whitehat-lab.md
  - concepts/red-team-operations.md
maturity: draft
created: 2026-08-03
updated: 2026-08-03
read_status: deep-read
cross-wiki-source: "@osint-wiki/sources/eval-url-revenue-cyber-agent-harness-2026-08-03.md"
---

## Relations

- @osint-wiki/sources/eval-url-revenue-cyber-agent-harness-2026-08-03.md — parent OSINT K220 eval (Cursor stand-in for Gemini v10.4)
- @entities/tools/cloakquest3r.md — MIT CDN/origin-IP recon
- @entities/tools/damn-vulnerable-drone.md — intentional drone hacking lab
- @entities/tools/hacktools.md — browser extension cheatsheet
- @entities/tools/raccoon.md — offensive recon scanner
- @entities/tools/black-cat.md — hypothesis-ledger Claude Code skill (null SPDX)
- @entities/tools/bypassav.md — AV/EDR technique mindmap
- @entities/tools/torbot.md — Tor/.onion crawler (GPL-3)
- @entities/tools/cf-hero.md — peer CDN origin-IP tool (Defer LICENSE)
- @concepts/osint-for-cybersecurity.md
- @concepts/web-pentest-methodology.md
- @concepts/av-edr-bypass.md
- @concepts/ai-pentest-harness-landscape.md
- @concepts/llm-pentest-automation.md
- @concepts/owned-target-whitehat-lab.md
- @concepts/red-team-operations.md

## Raw Concept

| Field | Value |
|-------|--------|
| **Parent** | OSINT K220 revenue eval — cyber/agent-harness batch |
| **Runtime** | Cursor Agent (Gemini UI blanked) |
| **URLs (cyber-relevant)** | 10 of 20 |
| **License check** | OSINT `.local/reports/license-spot-check-k220-2026-08-03.txt` + gh API 2026-08-03 |
| **Cemini product** | No Integrate into Atto/GuruWatcher — cyber wiki Context / Reference |

## Narrative

OSINT K220 scored a mixed cyber + CCC batch. Revenue tiers were Context/Pass for Cemini product stacks; **this wiki keeps the tradecraft**. Authorized-use only. No exploit wiring into Cemini trading stacks.

### Cyber-useful register

| Repo | SPDX (2026-08-03) | Stars / push | Cyber posture |
|------|-------------------|--------------|---------------|
| spyboy-productions/CloakQuest3r | MIT | ~2204 / 2026-01-06 | **Reference** — origin-IP behind Cloudflare-like proxies; peer to @entities/tools/cf-hero.md |
| nicholasaleks/Damn-Vulnerable-Drone | MIT | ~725 / 2026-07-08 | **Lab Reference** — ArduPilot/MAVLink intentional vuln simulator |
| LasCC/HackTools | NOT FOUND | ~6938 / 2025-01-05 | **Reference** — browser extension cheatsheet; license gate |
| evyatarmeged/Raccoon | MIT | ~3847 / 2026-04-21 | **Reference** — high-perf recon / vuln scanner |
| 0rangec3t/Black-cat | NOT FOUND | ~218 / 2026-08-03 | **Steal-from pattern** — hypothesis→evidence state machine + JSONL ledger; **no clone** |
| matro7sh/BypassAV | NOT FOUND | ~3400 / 2025-03-28 | **Reference mindmap** → @concepts/av-edr-bypass.md |
| DedSecInside/TorBot | GPL-3.0 (LICENSE.md) | ~4500 / 2026-07-28 | **Reference-only** — dark-web crawler; copyleft + legal friction |
| Hack-with-Github/Awesome-Hacking | CC0-1.0 | ~117k / 2026-07-26 | **Reference** — already K55-2 cleared; meta index only |
| dinosn/mariadb-13-rce-lab | NOT FOUND | ~17 / 2026-08-03 | **Lab note only** — do not wire exploit payloads; owned-lab awareness |
| The-Osint-Toolbox/Social-Media-OSINT | NOT FOUND | ~961 / 2026-07-12 | Light OSINT catalog pointer (primary OSINT wiki) |

### Steal worth keeping (Black-cat)

Hypothesis-first state machine (RECON ⇄ ENUMERATE ⇄ VALIDATE) with JSONL case ledger and machine `verify --report` before REPORT — better harness pattern than fixed recon→scan→exploit pipelines. Fits @concepts/llm-pentest-automation.md and @concepts/ai-pentest-harness-landscape.md. Null SPDX blocks clone/vendor; extract patterns into skill design only. Keep HITL for high-blast actions.

### Hard stops

- No auto-install of null-SPDX / NOASSERTION tools
- TorBot / BypassAV / HackTools = study or authorized lab only
- MariaDB RCE lab = owned Docker lab awareness — not a product dependency
