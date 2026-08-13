---
title: Qubes OS
type: entity
tags: [tool, os, qubes, xen, compartmentalization, desktop]
keywords: [Qubes OS, Xen, qube, disposable, Split GPG, Qubes-Whonix]
related:
  - concepts/hardened-alternative-operating-systems.md
  - sources/qubes-os-intro.md
  - sources/whonix-about.md
  - concepts/agent-vm-sandboxing.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party OS; no clone of Qubes ISO into wiki"
wire_status: wont_wire
---

## Relations

- @concepts/hardened-alternative-operating-systems.md
- @sources/qubes-os-intro.md
- @sources/whonix-about.md — Qubes-Whonix is the Tor-forced template pair
- @concepts/agent-vm-sandboxing.md — human workstation isolation vs agent lab VMs

## Raw Concept

Security-oriented single-user desktop OS. Xen VMs (“qubes”) as compartments. https://www.qubes-os.org/

## Narrative

Design assumption: software contains bugs that **will** be exploited; confine damage. Features: strong isolation, templates, Fedora/Debian/Windows templates, disposables, net/USB device isolation, Split GPG, CTAP proxy, Whonix integration. Unified desktop with **unforgeable colored window borders**. [CONFIRMED Qubes intro]

Needs competent hardware virtualization (VT-x/AMD-V + IOMMU). Not a phone. Not “more anonymous” unless you actually put Tor work in Whonix qubes and keep identities apart.
