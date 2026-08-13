---
title: GrapheneOS features overview (first-party)
type: source
tags: [source, grapheneos, android, vendor-doc]
keywords: [hardened_malloc, MTE, sandboxed Google Play, verified boot, Vanadium, user profiles]
related:
  - concepts/hardened-alternative-operating-systems.md
  - entities/tools/grapheneos.md
  - sources/grapheneos-faq.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — grapheneos.org/features"
wire_status: wont_wire
---

## Relations

- @concepts/hardened-alternative-operating-systems.md
- @entities/tools/grapheneos.md
- @sources/grapheneos-faq.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Features overview |
| Publisher | GrapheneOS |
| URL | https://grapheneos.org/features |
| Retrieved | 2026-08-12 |
| Location | vendor HTML |

## Narrative

Lists Graphene improvements **beyond AOSP 16** (not baseline Android sandbox/ASLR). Covers exploit mitigations (hardened_malloc, MTE), sandboxed Google Play, Network permission, verified-boot completion for out-of-band APKs, extra profiles, auto-reboot, duress wipe, Vanadium. [CONFIRMED]

## Snippets

> "GrapheneOS has a compatibility layer providing the option to install and use the official releases of Google Play in the standard app sandbox. Google Play receives absolutely no special access or privileges on GrapheneOS"
[Source: https://grapheneos.org/features (retrieved 2026-08-12)]
