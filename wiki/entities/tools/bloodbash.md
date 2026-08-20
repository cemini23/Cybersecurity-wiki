---
title: "BloodBash — offline SharpHound/AzureHound JSON analyzer (Extract-only)"
type: entity
tags: [entity, tool, ad-recon, extract, k242]
keywords: [BloodBash, SquidSec, SharpHound, AzureHound, offline graph, no Neo4j]
related:
  - entities/tools/bloodhound.md
  - concepts/windows-pentest.md
  - concepts/owned-target-whitehat-lab.md
maturity: draft
created: 2026-08-20
updated: 2026-08-20
phase_0_verdict: "Extract-only 2026-08-20 — github.com/SquidSec/BloodBash MIT. Clone lives on OSINT `.local/adopts/BloodBash` (~104MB). Do not re-clone into cyber. No attack-path payloads in wiki. Context-no-PoC: H.I.V.E, WireTapper, PrivFu, QUIC C2, pwneye."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K242 Extract pointer); runtime wont_wire"
---

**Briefs:** `briefs/2026-08-19_k242-bloodbash-hive-context.md`

## Relations

- @entities/tools/bloodhound.md — BloodHound CE/Enterprise still owns Neo4j/UI; this is offline JSON
- @concepts/windows-pentest.md — AD/Entra graphs from authorized collectors only
- @concepts/owned-target-whitehat-lab.md — JSON already collected from owned/contracted directories

## Raw Concept

Inbound K242 brief. MIT offline analyzer for the same SharpHound / AzureHound JSON BloodHound consumes, without a Neo4j server.

## Local adoption

| Field | Value |
|-------|-------|
| Verdict | Extract-only / REFERENCE pointer |
| Path | OSINT `../OSINT WORKSPACE/.local/adopts/BloodBash` (do **not** copy into cyber `.local`) |
| LICENSE | MIT (file verified 2026-08-20) |
| Size | ~104 MB (`du -sm`) |
| Wire | Policy: authorized JSON only; **runtime wont_wire** in Cursor |

## Narrative

BloodBash builds a local graph from collector JSON and surfaces AD/Entra attack-path **views**. Use only on files already collected under written scope. Wiki does **not** document path payloads, collector evasion, or H.I.V.E / WireTapper / PrivFu / QUIC C2 / pwneye. Those names stay Context-listed, no clone, no PoC. Qwen uncensored MLX remains Watch (no weight download). [Source: briefs/2026-08-19_k242-bloodbash-hive-context.md]
