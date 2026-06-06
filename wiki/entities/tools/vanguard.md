---
title: "vanguard — single-binary DFIR toolkit (Velociraptor + Volatility + KAPE + YARA)"
type: entity
tags: [tool, dfir, incident-response, forensics, go, mit, velociraptor, volatility, kape, yara, mitre-attack]
keywords: [vanguard, ridgeline cyber defence, dfir, velociraptor, volatility, kape, yara, hayabusa, chainsaw, loki, mitre mapped, air-gap, go]
related:
  - concepts/incident-response.md
  - concepts/malware-analysis.md
  - concepts/soc-operations.md
  - concepts/endpoint-detection-response.md
maturity: draft
created: 2026-05-21
updated: 2026-05-21
cross-wiki-source: "@osint-wiki/sources/multi-wiki-link-eval-41url-2026-05-18.md"
---

# vanguard — single-binary DFIR toolkit

## Relations

- @concepts/incident-response.md — collapses ~45-minute IR tool setup into one binary
- @concepts/malware-analysis.md — bundles Volatility + YARA for memory and signature analysis
- @concepts/soc-operations.md — 28 MITRE-mapped use cases for SOC workflow integration
- @concepts/endpoint-detection-response.md — KAPE + Chainsaw for endpoint triage

## Raw Concept

Routed from K53 OSINT-wiki tool eval (2026-05-18). Single-binary DFIR toolkit for Windows/Linux. Adopt-tier, MIT, ~118 stars.

## Narrative

`ridgelinecyberdefence/vanguard` (MIT, ~118 stars) bundles Velociraptor, Volatility, KAPE, YARA, Hayabusa, Chainsaw, and Loki into a single cross-platform Go binary. 28 MITRE-mapped use cases. Terminal UI. Offline/air-gap capable.

Primary value: collapses the ~45-minute first-responder setup (install Velociraptor, configure Volatility, deploy KAPE, etc.) into one binary. For incident responders arriving at a compromised endpoint, vanguard removes the tool-deployment tax.

K53 eval originally reported Apache-2.0; license verified as MIT via GitHub API (2026-05-18). Both are permissive — the correction is noted for provenance.
