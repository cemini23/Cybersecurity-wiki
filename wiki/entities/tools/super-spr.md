---
title: "super/SPR — zero-trust networking implementation (BSD-3-Clause)"
type: entity
tags: [tool, zero-trust, networking, vlan, wireguard, dns, go, bsd-3-clause, steal-from]
keywords: [super, spr-networks, zero trust networking, vlan segregation, wireguard, conntrack spoof prevention, per-device dns, dnat rewriting, mac identity]
related:
  - concepts/zero-trust.md
  - concepts/network-security.md
  - concepts/defense-in-depth.md
  - entities/tools/vpn-self-hosted.md
maturity: draft
created: 2026-05-21
updated: 2026-05-21
cross-wiki-source: @osint-wiki/sources/multi-wiki-tool-eval-19url-2026-05-20.md
---

# super/SPR — zero-trust networking implementation

## Relations

- @concepts/zero-trust.md — identity-centric network architecture
- @concepts/network-security.md — programmatic policy routing + VLAN segregation
- @concepts/defense-in-depth.md — per-device isolation as architectural primitive
- @entities/tools/vpn-self-hosted.md — WireGuard telemetry integration patterns

## Raw Concept

Routed from K55 OSINT-wiki tool eval (2026-05-20). Zero-trust networking implementation in JS/Go/Docker. Steal-from tier per eval, but BSD-3-Clause clears for full adoption. 565 stars.

## Narrative

`spr-networks/super` (BSD-3-Clause, 565 stars) implements zero-trust networking with several reusable engineering blueprints:

- **Unspoofable device identity** tied to MAC + per-device passwords + isolated /30 subnets
- **Conntrack-spoof prevention**
- **Per-device DNS controls**
- **WireGuard telemetry integration**
- **DNAT rewriting**
- **VLAN segregation in Go**

BSD-3-Clause clears for full commercial derivation. The K55 eval classified it as Steal-from, but the license permits direct adoption. Key extractables for cybersec-wiki: programmatic policy routing patterns, VLAN segregation in Go, and MAC randomization timeout logic (with [NEEDS VERIFICATION 2026-05-21] on the reassignment logic in Docker containers).
