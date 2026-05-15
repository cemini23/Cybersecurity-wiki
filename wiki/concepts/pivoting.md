---
title: "Pivoting & Lateral Movement"
type: concept
tags: [pivoting, lateral-movement, tunneling, post-exploitation, offensive-security]
keywords: [pivoting, lateral movement, SSH tunneling, port forwarding, proxychains, chisel, ligolo]
related:
  - concepts/red-team-operations.md
  - concepts/network-security.md
  - concepts/windows-pentest.md
  - sources/ssh-hardening-and-offensive-mastery.md
  - sources/network-attacks-and-exploitation.md
maturity: draft
created: 2026-05-15
updated: 2026-05-15
---

## Raw Concept

Stub created during Redteam Kit 22-PDF ingest (2026-05-15). New source documents reference this topic area but no concept page existed. Will be filled in during subsequent deep-reads.

## Narrative

Post-exploitation techniques for moving from an initially compromised host to other targets within an internal network. Key methods: SSH tunneling (local/remote/dynamic port forwarding), SOCKS proxying (proxychains, SSH -D), TCP relay tools (chisel, ligolo-ng, socat), and living-off-the-land (netsh, SSH, RDP). Critical skill for red team operations and network penetration testing — the initial foothold is rarely the final objective.

## Relations

- @concepts/red-team-operations.md
- @concepts/network-security.md
- @concepts/windows-pentest.md
- @sources/ssh-hardening-and-offensive-mastery.md
- @sources/network-attacks-and-exploitation.md
