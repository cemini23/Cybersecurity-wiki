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
  - entities/tools/iron-proxy.md
  - concepts/exceptional-access-risk-quantification.md
  - sources/arxiv-2606-19106-exceptional-access-compromise-risk-quantification.md
maturity: draft
created: 2026-05-15
updated: 2026-06-18
---

## Raw Concept

Stub created during Redteam Kit 22-PDF ingest (2026-05-15). Referenced by `concepts/system-hardening.md` as a foundational defensive concept.

## Narrative

Defense in Depth (DiD) is a layered security strategy that deploys multiple independent controls across the attack surface so that the failure of any single control does not result in a breach. Layers span: physical security, network perimeter (firewalls, IDS/IPS), host (HIDS, AV/EDR, hardening), application (WAF, RASP, input validation), data (encryption, DLP, access controls), and user (MFA, security awareness training). Core principle: no single point of security failure. Contrast with "castle-and-moat" perimeter-only models that assume everything inside the perimeter is trusted.

### Key custody as a non-bypassable layer

Exceptional-access and platform-scale key architectures introduce a **cryptographic custody layer** that DiD must treat explicitly — not as "just another encryption control":

| Control pattern | DiD role | Failure mode |
|-----------------|----------|--------------|
| HSM + compartmentalised KMS | Limits blast radius of single compromise | HSM extraction (P2 in EA scenario models) |
| t-of-N threshold key splitting | Removes unitary operator authority | Common-mode failure across trustees |
| Segregated key vs data stores (OTT-EA) | Requires multi-stage breach chain | Cross-cutting compromise (keys + data in one campaign) |
| Rapid revocation + rotation | Limits irreversibility window | Master-key exfiltration is permanent for historical ciphertext |

2606.19106 argues EA mandates **add** this layer's attack surface by construction (strictly higher modelled risk vs no-EA counterfactual). DiD design for operators holding signing keys, vault encryption keys, or LI infrastructure should prioritise **tail-risk reduction** (detection, revocation, segregation) over expected-value minimisation alone. See @concepts/exceptional-access-risk-quantification.md.

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