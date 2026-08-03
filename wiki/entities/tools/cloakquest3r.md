---
title: "spyboy-productions/CloakQuest3r — origin-IP behind reverse proxies"
type: entity
tags: [tool, recon, cloudflare, origin-ip, osint, mit, k220]
keywords: [cloakquest3r, cloudflare, origin ip, dns history, waf, reverse proxy]
related:
  - sources/osint-k220-cyber-agent-harness-eval-2026-08-03.md
  - entities/tools/cf-hero.md
  - entities/tools/reconftw.md
  - concepts/web-pentest-methodology.md
  - concepts/osint-for-cybersecurity.md
maturity: draft
created: 2026-08-03
updated: 2026-08-03
cross-wiki-source: "@osint-wiki/sources/eval-url-revenue-cyber-agent-harness-2026-08-03.md"
---

# CloakQuest3r — origin-IP exposure research

## Relations

- @sources/osint-k220-cyber-agent-harness-eval-2026-08-03.md — K220 parent
- @entities/tools/cf-hero.md — peer Cloudflare origin-IP discovery (Defer LICENSE)
- @entities/tools/reconftw.md — bulk recon orchestration; this is a CDN-unmask slice
- @concepts/web-pentest-methodology.md — authorized WAF/CDN assessment
- @concepts/osint-for-cybersecurity.md — DNS/history correlation

## Raw Concept

OSINT K220 Context → cyber Reference. Repo: https://github.com/spyboy-productions/CloakQuest3r

## Narrative

| Field | Value |
|-------|--------|
| **License** | MIT [CONFIRMED gh 2026-08-03] |
| **Stars / push** | ~2204 / 2026-01-06 |
| **Posture** | Reference — authorized recon only |

Python OSINT/recon tool for identifying **origin IP exposure** of sites behind Cloudflare and similar reverse proxies (DNS history, cert analysis, subdomain/IP correlation). Complements @entities/tools/cf-hero.md; does not replace subdomain enumeration in @entities/tools/reconftw.md.

**Ethics:** written authorization required — origin-IP discovery can bypass CDN WAF if misused.
