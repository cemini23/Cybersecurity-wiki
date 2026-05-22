---
title: "six2dez/reconftw — apex deterministic recon automation framework"
type: entity
tags: [tool, recon, automation, bug-bounty, subdomain-enum, nuclei, axiom, bash, mit, adopt]
keywords: [reconftw, six2dez, recon automation, subdomain enumeration, nuclei, axiom, waf bypass, distributed scanning, bats testing]
related:
  - concepts/web-pentest-methodology.md
  - concepts/osint-for-cybersecurity.md
  - concepts/bug-bounty.md
  - entities/tools/nmap.md
  - entities/tools/cf-hero.md
maturity: draft
created: 2026-05-21
updated: 2026-05-22
cross-wiki-source: "@osint-wiki/sources/analyzing-github-projects-agentic-infra-2026-05-21.md"
---

# six2dez/reconftw — apex deterministic recon automation

## Relations

- @concepts/web-pentest-methodology.md — modular recon pipeline for web-app testing
- @concepts/osint-for-cybersecurity.md — OSINT correlation + breach data integration
- @concepts/bug-bounty.md — automated target scoping and enumeration
- @entities/tools/nmap.md — complements manual scanning with automated fleet distribution
- @entities/tools/cf-hero.md — CDN origin-IP unmasking slice (orthogonal to subdomain modules)

## Raw Concept

Routed from K56 OSINT-wiki ingest (2026-05-21). Bash-based recon automation framework. MIT, 7.5k+ stars. Apex of deterministic security automation.

## Narrative

`six2dez/reconftw` (MIT, 7.5k+ stars) is a Bash-based recon automation framework representing the apex of deterministic security automation before the LLM-driven transition. Modular architecture under `modules/*.sh`:

| Module | Scope |
|---|---|
| `subdomains.sh` | Subdomain enumeration (OSINT + active brute-forcing) |
| `web.sh` | Web asset analysis + Nuclei integration |
| `vulns.sh` | Direct vulnerability identification |
| `osint.sh` | OSINT correlation with breach + public records |
| `axiom.sh` | Distributed fleet management (parallelize across VPSes to bypass WAF rate-limits) |

Quality assurance: 100+ Bats unit tests + integration smoke tests + command-injection security tests. The Axiom-based fleet-distribution pattern is reusable architectural advice for any scanner that hits WAF rate limits.
