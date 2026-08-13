---
title: Tor Support — Why the First Hop Is Stable (Entry Guards)
type: source
tags: [source, tor, anonymity, entry-guard, threat-model]
keywords: [entry guard, guard relay, first hop, traffic confirmation, Hopper, Tor threat model]
related:
  - concepts/metadata-traffic-analysis-anonymity.md
  - concepts/anonymity-networks.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party Tor support doc"
wire_status: wont_wire
---

## Relations

- @concepts/metadata-traffic-analysis-anonymity.md — guard pinning is Tor's mitigation for a relay-controlling adversary
- @concepts/anonymity-networks.md — entry guard as part of the Tor circuit model

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Why Tor doesn't use a different guard (Tor Support) |
| Publisher | The Tor Project (support.torproject.org) |
| URL | https://support.torproject.org/tbb/tbb-2/ |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

First-party Tor support article explaining why the first hop stays fixed. Tor "selects a stable and trusted 'guard relay' to be the first hop in your circuit"; the guard stays for roughly 2–3 months, and "the rest of your circuit changes with every new website you visit." The stated purpose is defense against "a known anonymity-breaking attack" — the paper this is an active countermeasure to is Hopper et al. on entry guards — where an adversary who controls many relays could otherwise be repeatedly chosen as the first hop and observe the user's connections over time. [CONFIRMED Tor support, retrieved 2026-08-12]

The page is narrow (guard behavior only) — the broader traffic-confirmation and global-observer threat model is documented on the sibling concept @concepts/metadata-traffic-analysis-anonymity.md and the Murdoch & Danezis paper.

## Snippets

> "Tor selects a stable and trusted 'guard relay' to be the first hop in your circuit."

> "The rest of your circuit changes with every new website you visit."
[Source: https://support.torproject.org/tbb/tbb-2/ (retrieved 2026-08-12)]
