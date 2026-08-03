---
title: "LasCC/HackTools — offensive browser extension cheatsheet"
type: entity
tags: [tool, browser-extension, cheatsheet, red-team, bug-bounty, k220]
keywords: [hacktools, chrome extension, firefox addon, payloads, xss, reverse shell]
related:
  - sources/osint-k220-cyber-agent-harness-eval-2026-08-03.md
  - concepts/web-pentest-methodology.md
  - concepts/bug-bounty.md
  - entities/tools/burp-suite.md
maturity: draft
created: 2026-08-03
updated: 2026-08-03
cross-wiki-source: "@osint-wiki/sources/eval-url-revenue-cyber-agent-harness-2026-08-03.md"
---

# HackTools browser extension

## Relations

- @sources/osint-k220-cyber-agent-harness-eval-2026-08-03.md — K220 parent
- @concepts/web-pentest-methodology.md — cheatsheet during authorized web tests
- @concepts/bug-bounty.md — payload/reference UX
- @entities/tools/burp-suite.md — primary proxy; HackTools is a side cheatsheet

## Raw Concept

OSINT K220 Context. Repo: https://github.com/LasCC/HackTools

## Narrative

| Field | Value |
|-------|--------|
| **License** | NOT FOUND [CONFIRMED gh 2026-08-03] |
| **Stars / push** | ~6938 / 2025-01-05 |
| **Posture** | Reference — license gate before install |

All-in-one browser extension for offensive security cheatsheets (payloads, reverse shells, XSS snippets, etc.). Useful as a **sidebar reference** during authorized engagements; last push ~2025-01 so treat as maintenance-risk. **Do not install** until SPDX/LICENSE is verified (browser-extension supply chain). Prefer Burp + written notes for production engagements.
