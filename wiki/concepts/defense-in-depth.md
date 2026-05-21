---
title: "Defense in Depth"
type: concept
tags: [defense-in-depth, defensive-security, security-architecture, hardening]
keywords: [defense in depth, layered security, defense architecture, security controls, compensating controls]
related:
  - concepts/system-hardening.md
  - concepts/network-security.md
  - concepts/linux-security.md
  - concepts/incident-response.md
  - concepts/npm-supply-chain-defense.md
  - entities/tools/aisoc.md
  - entities/tools/supavec.md
  - sources/cybersecurity-blue-team-strategies.md
  - sources/encryption-and-hashing.md
  - entities/tools/super-spr.md
maturity: draft
created: 2026-05-15
updated: 2026-05-16
---

## Raw Concept

Stub created during Redteam Kit 22-PDF ingest (2026-05-15). Referenced by `concepts/system-hardening.md` as a foundational defensive concept.

## Narrative

Defense in Depth (DiD) is a layered security strategy that deploys multiple independent controls across the attack surface so that the failure of any single control does not result in a breach. Layers span: physical security, network perimeter (firewalls, IDS/IPS), host (HIDS, AV/EDR, hardening), application (WAF, RASP, input validation), data (encryption, DLP, access controls), and user (MFA, security awareness training). Core principle: no single point of security failure. Contrast with "castle-and-moat" perimeter-only models that assume everything inside the perimeter is trusted.

## Relations

- @concepts/system-hardening.md
- @concepts/network-security.md
- @concepts/linux-security.md
- @concepts/incident-response.md
- @concepts/npm-supply-chain-defense.md — package-manager hardening (release-age cooldown + pinning) as a defensive layer
- @entities/tools/aisoc.md — self-hosted AI SOC orchestrator (LangGraph, 14 log sources) — blue-team automation layer
- @entities/tools/supavec.md — PostgreSQL RLS multi-tenant isolation pattern for SOC incident-response tooling
- @sources/cybersecurity-blue-team-strategies.md
- @sources/encryption-and-hashing.md