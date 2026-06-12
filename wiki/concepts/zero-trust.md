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
  - entities/tools/vpn-self-hosted.md
  - entities/tools/super-spr.md
  - entities/tools/iron-proxy.md
  - concepts/6g-cps-closed-loop-security.md
  - sources/arxiv-2606-08173-ai-native-closed-loop-6g-cps-security.md
maturity: draft
created: 2026-05-12
updated: 2026-06-12
---

## Relations

- @concepts/network-security.md
- @concepts/soc-operations.md
- @sources/zero-trust-testing-checklist.md
- @entities/people/joas-a-santos.md
- @sources/open-source-soc-guide.md
- @entities/tools/vpn-self-hosted.md — VPN tool hub; Tailscale (WireGuard-based) is documented as Zero Trust mesh overlay implementation
- @entities/tools/iron-proxy.md — egress firewall for untrusted workloads (K68 Adopt-eligible)

## Raw Concept

Anchored by Zero Trust Testing Checklist.pdf.

## Narrative

Zero Trust = an architectural philosophy: **never trust, always verify** — every request is authenticated + authorized regardless of network position. Core tenets (per NIST SP 800-207): explicit verification, least privilege, assume breach. Implementations: BeyondCorp (Google's original), Zscaler ZTNA, Cloudflare Access, Tailscale (WireGuard-based). Testing a Zero Trust deployment: identity-spoofing attempts across federations, MFA-bypass attempts, conditional-access policy edge cases, posture-check evasion, service-mesh policy enforcement.
