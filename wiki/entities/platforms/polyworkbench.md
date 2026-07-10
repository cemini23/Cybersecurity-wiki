---
title: PolyWorkBench
type: entity
tags: [entity, benchmark, platform, multilingual, long-horizon, agent-evaluation]
keywords: [polyworkbench, 2607.06008, tencent, workplace agent benchmark]
related:
  - sources/arxiv-2607-06008-polyworkbench-multilingual-long-horizon.md
  - concepts/multilingual-long-horizon-agent-evaluation.md
  - concepts/security-tool-orchestration-determinants.md
  - concepts/seclaw-agent-security-evaluation.md
  - entities/platforms/hackthebox.md
maturity: draft
created: 2026-07-10
updated: 2026-07-10
phase_0_verdict: "Reference 2026-07-10 — 67-task multilingual workplace benchmark; no public repo at ingest; cite for hybrid eval + harness disclosure; not a pentest lab platform"
---

**Briefs:** `briefs/2026-07-10_polyworkbench-multilingual-eval-handoff.md`

## Relations

- @sources/arxiv-2607-06008-polyworkbench-multilingual-long-horizon.md — paper provenance
- @concepts/multilingual-long-horizon-agent-evaluation.md — synthesis

## Raw Concept

Entity stub from arXiv **2607.06008** ingest (2026-07-10). PolyWorkBench = multilingual long-horizon **workplace agent** benchmark (BJTU + Tencent Weixin AI).

## Narrative

**Not** a CTF/lab platform like @entities/platforms/hackthebox.md — an **evaluation benchmark** for enterprise-style workflows (commerce, legal, knowledge work, localization, manufacturing).

### Phase-0 audit verdict (2026-07-10): Reference

| # | Gate | Status | Finding |
|---|------|--------|---------|
| G0 | License / artifact | **FAIL** | No public GitHub/HuggingFace repo located at ingest |
| G1 | Domain fit | PASS | Agent harness regression methodology |
| G2 | Maturity | PARTIAL | 67 hand-curated tasks; paper claims manifest release |
| G3 | Failure mode | N/A | Benchmark only — misuse risk low |
| G4 | Wiki overlap | PASS | Complements SeClaw trajectory eval, HexStrike orchestration study |

**Final:** **REFERENCE** — monitor for artifact drop; steal hybrid eval + harness matrix discipline.

## Snippets

> 67 tasks · 10 languages · 88% trilingual by construction · mean 8.5 tool-use steps.
> — [Source: arxiv-2607.06008 §3, retrieved 2026-07-10]
