---
title: Browser Fingerprinting — A survey (Laperdrix et al., TWEB 2020)
type: source
tags: [source, arxiv, browser-fingerprint, privacy, opsec]
keywords: [1905.01051, Laperdrix, Bielova, Baudry, Avoine, TWEB]
related:
  - concepts/hardware-id-masking-opsec.md
  - concepts/anonymity-networks.md
  - "@osint-wiki/entities/tools/fingerprint-suite.md"
  - sources/arxiv-2201-09956-drawn-apart-gpu-fingerprinting.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — survey; no clone"
wire_status: wont_wire
---

## Relations

- @concepts/hardware-id-masking-opsec.md — distinguishes browser fingerprint from host HWID
- @concepts/anonymity-networks.md — Tor Browser is a uniformity defense in this literature
- @osint-wiki/entities/tools/fingerprint-suite.md — OSINT primary tool in this lane
- @sources/arxiv-2201-09956-drawn-apart-gpu-fingerprinting.md — GPU manufacturing fingerprint extends this survey

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Browser Fingerprinting: A survey |
| Authors | Laperdrix, Bielova, Baudry, Avoine |
| arXiv | 1905.01051 |
| Venue | ACM TWEB 14(2), 2020 (doi 10.1145/3386040) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-1905.01051-browser-fingerprinting-survey.pdf` |
| Retrieved | 2026-08-12 |

## Narrative

Survey of **stateless** identification through browser APIs and HTTP headers (not cookies). Explicitly excludes smartphone-app IDs, nmap packet fingerprints, and IP/geolocation as in-scope. Systematizes defenses (blocking, spoofing/randomization, uniformity). [CONFIRMED survey §1]

OPSEC steal: website tracking of “the same laptop” often does not need SMBIOS. Host-ID masking without an anti-fingerprinting browser leaves the web lane open. Conversely, fingerprint-suite (OSINT) is collection stealth, not host anonymity.

## Snippets

> "Contrarily to other identification techniques like cookies that rely on a unique identifier (ID) directly stored inside the browser, browser fingerprinting is qualified as completely stateless."
[Source: arxiv-1905.01051 §1.1]
