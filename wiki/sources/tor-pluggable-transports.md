---
title: Tor Project — Pluggable Transports Documentation
type: source
tags: [source, tor, pluggable-transports, obfs4, meek, dpi, censorship]
keywords: [pluggable transports, obfs4, meek, FTE, ScrambleSuit, DPI, deep packet inspection, bridges]
related:
  - concepts/censorship-circumvention-pluggable-transports.md
  - concepts/anonymity-networks.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party Tor documentation"
wire_status: wont_wire
---

## Relations

- @concepts/censorship-circumvention-pluggable-transports.md — the PT class taxonomy this doc anchors
- @concepts/anonymity-networks.md — Tor primer; bridges/PTs are the reachability layer

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Tor: Pluggable Transports (project documentation) |
| Publisher | The Tor Project |
| URL | https://2019.www.torproject.org/docs/pluggable-transports.html.en |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

First-party Tor documentation explaining the censorship problem and the PT answer. Key structure: IP-based blocking is beaten by bridge relays; but "the censor can use DPI to recognize and filter Tor traffic flows even when they connect to unexpected IP addresses." Pluggable Transports solve the DPI layer: they "transform the Tor traffic flow between the client and the bridge," so censors monitoring that hop see innocent-looking traffic. [CONFIRMED, retrieved 2026-08-12]

Deployed transports documented: **obfs4** (ScrambleSuit-class obfuscation + elligator2 public-key obfuscation + ntor one-way auth; "currently the most effective transport to bypass censorship"); **meek** (HTTP for carrying bytes + TLS for obfuscation, relayed through a third-party server — historically Google App Engine — using a trick that makes the client look like it is talking to an unblocked server, i.e. the domain-fronting class); **FTE** (Format-Transforming Encryption, transforms Tor traffic to arbitrary formats); **ScrambleSuit** (anti-probing; changes packet-length distribution and inter-arrival times). Undeployed/experimental: StegoTorus (splits streams to avoid packet-size signatures). [CONFIRMED, retrieved 2026-08-12]

## Snippets

> "Pluggable Transports (PT) transform the Tor traffic flow between the client and the bridge. This way, censors who monitor traffic between the client and the bridge will see innocent-looking transformed traffic instead of the actual Tor traffic."

> "obfs4 is currently the most effective transport to bypass censorship."
[Source: https://2019.www.torproject.org/docs/pluggable-transports.html.en (retrieved 2026-08-12)]
