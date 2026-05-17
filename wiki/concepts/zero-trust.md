---
title: Zero Trust
type: concept
tags: [architecture, defense]
keywords: [zero trust, ztna, beyondcorp, microsegmentation]
related:
  - concepts/network-security.md
  - concepts/soc-operations.md
  - sources/zero-trust-testing-checklist.md
  - entities/people/joas-a-santos.md
  - sources/open-source-soc-guide.md
maturity: draft
created: 2026-05-12
updated: 2026-05-17
---

## Relations

- @concepts/network-security.md
- @concepts/soc-operations.md
- @sources/zero-trust-testing-checklist.md
- @entities/people/joas-a-santos.md
- @sources/open-source-soc-guide.md

## Raw Concept

Anchored by Zero Trust Testing Checklist.pdf.

## Narrative

Zero Trust = an architectural philosophy: **never trust, always verify** — every request is authenticated + authorized regardless of network position. Core tenets (per NIST SP 800-207): explicit verification, least privilege, assume breach. Implementations: BeyondCorp (Google's original), Zscaler ZTNA, Cloudflare Access, Tailscale (WireGuard-based). Testing a Zero Trust deployment: identity-spoofing attempts across federations, MFA-bypass attempts, conditional-access policy edge cases, posture-check evasion, service-mesh policy enforcement.
