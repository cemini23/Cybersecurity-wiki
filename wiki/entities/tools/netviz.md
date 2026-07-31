---
title: "netviz — browser-based network architecture visualizer (MIT)"
type: entity
tags: [tool, osint, recon, visualization, d3, graph, adopt, k93]
keywords: [netviz, shadowarcanist, network graph, d3, socket.io, infrastructure mapping, pentest recon]
related:
  - concepts/osint-for-cybersecurity.md
  - concepts/threat-intelligence.md
  - concepts/red-team-operations.md
  - entities/tools/maltego.md
  - entities/tools/bloodhound.md
  - entities/tools/reconftw.md
  - "@osint-wiki/entities/tools/shadowarcanist-netviz.md"
maturity: draft
created: 2026-06-01
updated: 2026-07-31
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md"
phase_0_verdict: "Adopt 2026-06-01 — MIT verified; upgraded from K53 Steal-from after K93 re-eval."
wire_status: policy_wired
wire_target: "CLAUDE.md#hands-on-rules-ethics--legality"
---

# netviz — browser-based network architecture visualizer (MIT)

## Relations

- @concepts/osint-for-cybersecurity.md — graph recon for external footprint / relationship mapping
- @concepts/threat-intelligence.md — actor/infrastructure relationship graphs for CTI briefings
- @concepts/red-team-operations.md — engagement topology mapping during recon
- @entities/tools/maltego.md — commercial OSINT graph analysis (netviz = lightweight self-hosted alternative)
- @entities/tools/bloodhound.md — AD attack-path graphs (different domain; same "graph as intel" discipline)
- @entities/tools/reconftw.md — recon output can feed manual graph construction in netviz
- @osint-wiki/entities/tools/shadowarcanist-netviz.md — cross-wiki mirror; OSINT federation index

## Raw Concept

Routed from K93 brief (`briefs/2026-06-01_k93-cybersec-digest-netviz-from-osint.md`, 2026-06-01). `ShadowArcanist/netviz` — MIT, ~392 stars, Python + D3.js + Socket.IO. K53 was **Steal-from**; K93 re-eval promotes to **Adopt** for pentest recon graph tooling.

## Narrative

**Local clone (2026-07-18):** `raw-sources/repos/netviz` (~1.3MB, shallow). Analyst laptop + brief export only.


netviz is a browser-based app for designing and visualizing network architectures. In cybersec workflows it supports **relationship mapping** during offensive recon (subdomain/host/service graphs) and defensive CTI (actor/infrastructure link charts) without Maltego licensing overhead.

**Phase-0 posture**: analyst laptop + brief export only — no prod `/opt/cemini` deploy until lab validation. Same import boundary as other Adopt-tier graph tooling in this wiki.

**Integration pattern**: export recon artifacts (hosts, edges, zones) into netviz sessions for engagement briefings and wiki `@path` cross-links in threat-actor pages.

## Snippets

```bash
gh api repos/ShadowArcanist/netviz --jq '.license.spdx_id'   # MIT
```

## Dead Ends

- **K53 Steal-from "strip for parts"** — superseded by K93 Adopt after license re-verification and pentest-recon fit reassessment; keep index provenance `K53, K93`.
