---
title: "bbot — AGPL recursive recon scanner (Extract-only)"
type: entity
tags: [entity, tool, recon, agpl, extract, k241]
keywords: [bbot, blacklanternsecurity, AGPL-3.0, recursive scanner]
related:
  - concepts/osint-for-cybersecurity.md
  - concepts/owned-target-whitehat-lab.md
  - entities/tools/nmap.md
  - entities/tools/rustscan.md
maturity: draft
created: 2026-08-20
updated: 2026-08-20
phase_0_verdict: "Extract-only 2026-08-20 — github.com/blacklanternsecurity/bbot AGPL-3.0. Clone lives on OSINT `.local/adopts/bbot` (~15MB). Do not re-clone into cyber. Never vendor into Atto/prod. No mass internet scan."
wire_status: policy_wired
wire_target: "license + scope policy (K241); runtime wont_wire; no Atto import"
---

**Briefs:** `briefs/2026-08-18_k241-bbot-agpl-recon.md`

## Relations

- @concepts/osint-for-cybersecurity.md — recon assist, not a C2
- @concepts/owned-target-whitehat-lab.md — written authorization before any module fan-out
- @entities/tools/nmap.md — still the port/service primitive
- @entities/tools/rustscan.md — sibling Extract recon (GPL); OSINT shelf, no second tree

## Raw Concept

Inbound K241 brief. Recursive OSINT/recon scanner. Earlier evals said GPL — **wrong**; SPDX is **AGPL-3.0**. Index row K71/K73 "Reject (copyleft)" for IP-sale surfaces stays true; this page is the Extract-only lab pointer.

## Local adoption

| Field | Value |
|-------|-------|
| Verdict | AGPL Extract-only |
| Path | OSINT `../OSINT WORKSPACE/.local/adopts/bbot` (do **not** copy into cyber `.local`) |
| LICENSE | GNU AGPL v3 (file verified 2026-08-20) |
| Size | ~15 MB (`du -sm`) |
| Wire | Isolate; **never** link into Atto or proprietary kits |

## Narrative

bbot fans out modules (subdomain, cloud, web) from a seed. That is useful on an **authorized target** and toxic as a mass-internet scanner or as an AGPL taint into closed products. CyberChef remains Context (K149). PrivFu / HTB cheatsheets / QUIC C2 / plugandpwn stay Context-no-PoC. [Source: briefs/2026-08-18_k241-bbot-agpl-recon.md]
