---
title: RustScan — fast port scanner wrapper around nmap
type: entity
tags: [entity, tool, recon, rust, k237]
keywords: [rustscan, nmap, port scan, recon, owned-lab]
related:
  - entities/tools/cyberscraper-2077.md
  - entities/tools/nmap.md
  - concepts/owned-target-whitehat-lab.md
  - concepts/osint-for-cybersecurity.md
  - "@osint-wiki/entities/tools/rustscan.md"
maturity: draft
created: 2026-08-15
updated: 2026-08-15
wire_status: wont_wire
wire_target: "OSINT extract / PATH — no second clone in cyber; GPL-aware"
---

## Relations

- @entities/tools/nmap.md — RustScan is a fast front-end; nmap still does the service/script work
- @entities/tools/cyberscraper-2077.md — same inbound brief
- @concepts/owned-target-whitehat-lab.md — written authorization before any scan

## Raw Concept

Inbound `briefs/2026-08-14_k237-cyberscraper-rustscan.md`. Fast Rust port scanner that shells nmap for the interesting ports.

## Narrative

RustScan finds open ports quickly, then hands them to nmap. **Authorized lab / engagement scope only** — mass-scanning third-party space is out of scope. Prefer OSINT's extract (GPL) rather than a second tree here. Do not treat "fast" as permission to skip rate limits or scope. [Source: briefs/2026-08-14_k237-cyberscraper-rustscan.md]
