---
title: "cariddi — Go-based domain crawler for secrets/API-keys/endpoint hunting"
type: entity
category: tool
tags: [entity, tool, domain-crawler, secrets-hunting, endpoint-discovery, bug-bounty, burpsuite-proxy, k44, steal-from-gpl-poison]
keywords: [cariddi, edoardottt, go-colly, secrets-scanning, api-key-discovery, burpsuite-integration, gpl-3-poison-pill]
related: []
maturity: steal-from-doc-level-pending-phase-0
created: 2026-05-14
updated: 2026-05-14
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
---

## Relations

- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)

## Raw Concept

A heavily-adopted Go (98.4%) parallelized domain crawler for hunting exposed secrets, API keys, and sensitive endpoints. Uses go-colly framework. Native proxy integration with BurpSuite. **GPL-3.0, claimed 3,400 stars, last commit 2026-03-29**. K44 verdict: **Steal-from** (GPL-3.0 poison-pill prevents production deployment; patterns extractable for laptop-side or non-shipped tooling).

## Narrative

K44 primary fit: Cybersec-wiki (offensive security, bug-bounty, SOC). Cross-route: OSINT-wiki (endpoint hunting + metadata scraping for threat-actor profiling).

**License posture**: GPL-3.0 statically/dynamically linked into the Cemini production suite triggers copyleft propagation — **absolute poison for the IP sale**. Strict laptop-side execution only. Architectural patterns (parallelized go-colly crawler, BurpSuite proxy integration, secrets-detection signatures) re-implementable under MIT.

**Phase-0 gates**:
- G1: Star + maturity verification (`gh api repos/edoardottt/cariddi`)
- G2: License (GPL-3.0 confirmed, treat as poison-pill)
- G3: BurpSuite integration audit — useful for OSINT threat-actor profiling but only re-implementable under MIT
- G4: Endpoint-discovery heuristic comparison vs other secrets-crawlers (gitleaks-by-crawl variants)

## Snippets

> "Cariddi is a highly parallelized domain crawler engineered to hunt for exposed secrets, API keys, and sensitive endpoints, featuring native proxy integration with BurpSuite. These capabilities align flawlessly with the offensive security and threat intelligence workflows defined in the Cybersec-wiki."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶289]
