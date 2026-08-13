---
title: Whonix about / architecture (first-party)
type: source
tags: [source, whonix, tor, anonymity, vendor-doc]
keywords: [Whonix, Kicksecure, Gateway, Workstation, Tor]
related:
  - concepts/hardened-alternative-operating-systems.md
  - concepts/anonymity-networks.md
  - sources/kicksecure-vs-whonix.md
  - entities/tools/qubes-os.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — whonix.org About"
wire_status: wont_wire
---

## Relations

- @concepts/hardened-alternative-operating-systems.md
- @concepts/anonymity-networks.md — forced-Tor OS vs Tor Browser on stock
- @sources/kicksecure-vs-whonix.md
- @entities/tools/qubes-os.md — Qubes-Whonix

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Whonix - Overview |
| Publisher | Whonix |
| URL | https://www.whonix.org/wiki/About |
| Retrieved | 2026-08-12 |
| Location | vendor HTML |

## Narrative

Anonymous desktop OS: Kicksecure-hardened Debian split into **Whonix-Gateway** (Tor) and **Whonix-Workstation** (apps on isolated net). All Workstation Internet via Tor; designed to make DNS leaks fail closed. Runs on Type-I (Qubes-Whonix) or Type-II (KVM/VirtualBox) hypervisors. [CONFIRMED About]

They state that without advanced netflow correlation, an observer cannot easily determine sites visited. Pair with `@concepts/metadata-traffic-analysis-anonymity.md` — correlation remains the residual class. [CONFIRMED About; residual is this wiki’s traffic-analysis page]

## Snippets

> "Whonix consists of two VMs: the Whonix-Gateway™ and the Whonix-Workstation™. The former runs Tor processes and acts as a gateway, while the latter runs user applications on a completely isolated network."
[Source: https://www.whonix.org/wiki/About (retrieved 2026-08-12)]
