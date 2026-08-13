---
title: Snowflake (Tor Project) — Censorship Circumvention via Volunteer Proxies
type: source
tags: [source, tor, snowflake, pluggable-transport, censorship-circumvention, webrtc]
keywords: [Snowflake, WebRTC, pluggable transports, bridges, proxy, censorship, Tor Browser]
related:
  - concepts/censorship-circumvention-pluggable-transports.md
  - concepts/anonymity-networks.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — first-party Tor anti-censorship project"
wire_status: wont_wire
---

## Relations

- @concepts/censorship-circumvention-pluggable-transports.md — Snowflake as a volunteer-proxy PT class
- @concepts/anonymity-networks.md — Tor primer; Snowflake is a first-hop reachability tool

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Snowflake — Pluggable Transports for Tor |
| Publisher | The Tor Project (anti-censorship) |
| URL | https://snowflake.torproject.org/ |
| Retrieved | 2026-08-12 |
| Location | vendor HTML (no PDF archive) |

## Narrative

Snowflake is Tor's volunteer-run, WebRTC-based circumvention system: a censored user's connection is routed through volunteer proxies in uncensored regions. It ships embedded in Tor Browser, Orbot, and Ricochet-Refresh; users enable it in settings. Because it uses WebRTC — "commonly employed by videoconferencing software" — the traffic resembles an ordinary video call, and the page frames the design as raising the cost of blocking: a censor "would have to cut off large portions of the Internet" to stop the whole class. [CONFIRMED, retrieved 2026-08-12]

Scale figure: **127,599 Snowflakes (and counting)** as of retrieval. Volunteers contribute three ways: a browser extension (Firefox/Chrome/Edge), a standalone proxy, or an embeddable website widget. The add-on's role is one-directional: "the browser add-on… is designed for people who want to support others in circumventing internet censorship" — running it lends bandwidth; it does not circumvent anything for its installer. [CONFIRMED, retrieved 2026-08-12]

The page situates Snowflake alongside meek and WebTunnel: a videocall (Snowflake), a connection to Microsoft (meek-azure), a standard HTTPS connect (WebTunnel).

## Snippets

> "Snowflake uses a technology called WebRTC, which is commonly employed by videoconferencing software."

> "Snowflake is a relatively new circumvention technology, part of the Pluggable Transports family, that is continuously being improved."

> "The browser add-on, on the other hand, is designed for people who want to support others in circumventing internet censorship."
[Source: https://snowflake.torproject.org/ (retrieved 2026-08-12)]
