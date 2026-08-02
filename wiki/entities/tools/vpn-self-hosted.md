---
title: "Self-Hosted VPN — WireGuard, OpenVPN, and Deployment Tools"
type: entity
tags: [entity, tool, vpn, wireguard, openvpn, infrastructure, privacy, self-hosted, tracking-hub]
keywords: [vpn, wireguard, openvpn, wg-easy, pivpn, tailscale, self-hosted, geo-bypass, tunnel, privacy, network-security]
related:
  - entities/tools/openvpn-install.md
  - concepts/network-security.md
  - concepts/zero-trust.md
  - concepts/system-hardening.md
  - entities/tools/super-spr.md
  - concepts/owned-target-whitehat-lab.md
maturity: draft
hub: true
created: 2026-05-17
updated: 2026-07-31
wire_status: deferred
wire_target: "Component Phase-0 not complete"
---

## Relations

- @concepts/owned-target-whitehat-lab.md — WireGuard/self-hosted VPN for multi-host lab isolation without full-tunneling daily traffic
- @entities/tools/openvpn-install.md — angristan's OpenVPN deployment script (Steal-from, Unlicense)
- @concepts/network-security.md — VPN as network-layer perimeter topic
- @concepts/zero-trust.md — Tailscale (WireGuard-based) as Zero Trust implementation
- @concepts/system-hardening.md — hardened VPN configs as system-hardening reference

## Raw Concept

Hub page cataloging all VPN and self-hosted tunnel tools documented across the Cemini wiki ecosystem. Created 2026-05-17 after a Polymarket-access VPN strategy brief surfaced the need for centralized VPN tool tracking. Previously, VPN tools were scattered across `openvpn-install.md`, `network-security.md`, `zero-trust.md`, and `system-hardening.md` with no single catalog page.

## Narrative

### Tool inventory

| Tool | Type | License | Verdict | Status |
|---|---|---|---|---|
| [wg-easy](https://github.com/wg-easy/wg-easy) | WireGuard + Web UI (Docker) | AGPL-3.0 | Adopt (operational use) | Not yet Phase-0 audited |
| [PiVPN](https://github.com/pivpn/pivpn) | WireGuard + OpenVPN installer (Shell) | MIT | Evaluate | Not yet Phase-0 audited |
| [angristan/openvpn-install](https://github.com/angristan/openvpn-install) | OpenVPN deployment (Bash) | Unlicense | Steal-from | Doc-level eval done (K50); Phase-0 clone audit pending |
| [Tailscale](https://github.com/tailscale/tailscale) | WireGuard mesh overlay | BSD-3-Clause | Reference | Documented in `zero-trust.md` + `3-26-f.md`; already in use for Cemini infra |
| [WireGuard (raw)](https://www.wireguard.com/) | Kernel-level VPN protocol | GPL-2.0 | N/A (protocol, not tool) | Built into Linux 5.6+; foundation for all WireGuard-based tools above |

### Rejected

| Tool | Reason | Date |
|---|---|---|
| [awesome-wireguard](https://github.com/cedrickchee/awesome-wireguard) | CC-BY-NC-ND license (NC clause = IP-sale poison pill on text content) | K44 eval (2026-05-14) |
| MasterDnsVPN | DNS tunneling → latency unacceptable for trading | K30 eval |

### VPN protocol decision matrix (2026)

WireGuard is the default choice for self-hosted VPN in 2026. Reasons:
- 2-4x higher throughput than OpenVPN on identical hardware (~940 Mbps vs 500-700 Mbps on 1 Gbps link)
- ~4,000 lines of code vs 70,000+ — smaller attack surface, formally verified
- Native Linux kernel module (5.6+) — no userspace context switching
- Sub-millisecond latency overhead vs 5-15ms for OpenVPN
- 4-line config files — drastically fewer misconfiguration risks

OpenVPN retains one critical advantage: TCP/443 mode, which is indistinguishable from HTTPS traffic at L4. This is essential for networks that block UDP (corporate firewalls, restrictive countries). For self-hosted VPN, run both: WireGuard as primary, OpenVPN on TCP/443 as fallback.

### When to use which

| Scenario | Recommendation |
|---|---|
| Personal VPN, home server, VPS with public IP | WireGuard via wg-easy (Docker) |
| Raspberry Pi or bare-metal Debian/Ubuntu | PiVPN (supports both WireGuard + OpenVPN) |
| Need TCP/443 firewall bypass | OpenVPN (or WireGuard tunneled via udp2raw/wstunnel) |
| Zero-config mesh network (multiple devices, behind NAT) | Tailscale |
| Enterprise auth (LDAP/RADIUS), per-user bandwidth, certificate revocation | OpenVPN |
| Maximum auditability, minimal attack surface | Raw WireGuard (no management layer) |

## Snippets

- WireGuard throughput benchmark: "~940 Mbps on 1 Gbps link, ~5.6% overhead vs ~25.7% overhead for OpenVPN" [Source: vpnselect.org, "Best VPN Protocol In 2026" (2026-04-15)]
- wg-easy: "The easiest way to run WireGuard VPN + Web-based Admin UI. 25.5K stars, AGPL-3.0, 120 contributors, active April 2026." [Source: github.com/wg-easy/wg-easy (retrieved 2026-05-17)]
- PiVPN: "The Simplest VPN installer, designed for Raspberry Pi. Supports WireGuard and OpenVPN. MIT license, 7,957 stars, v4.11.1." [Source: github.com/pivpn/pivpn (retrieved 2026-05-17)]
