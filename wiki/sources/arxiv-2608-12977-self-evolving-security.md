---
title: "Beyond Handcrafted Security — HARD self-evolving runtime defense (2608.12977)"
type: source
tags: [source, arxiv, agent-security, harness-evolution, defense, k237]
keywords: [2608.12977, HARD, self-evolving defense, gate evolver, policy evolver, ASR]
related:
  - concepts/self-evolving-runtime-defense.md
  - sources/arxiv-2608-12851-skill-misevolution.md
  - concepts/skill-misevolution.md
  - concepts/safety-harness-evolution.md
  - concepts/self-evolving-agent-security.md
  - concepts/ai-for-cybersecurity.md
  - "@osint-wiki/sources/arxiv-2608.12977-self-evolving-security-2026-08-14.md"
maturity: draft
created: 2026-08-15
updated: 2026-08-15
read_status: skimmed
---

## Relations

- @concepts/self-evolving-runtime-defense.md — cyber synthesis
- @sources/arxiv-2608-12851-skill-misevolution.md — offense-side pair
- @osint-wiki/sources/arxiv-2608.12977-self-evolving-security-2026-08-14.md — primary ingest (OSINT K237)

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.12977, "Beyond Handcrafted Security: Towards Self-Evolving Runtime Defense" (HARD) |
| Retrieved | 2026-08-14 via OSINT → `briefs/2026-08-14_k237-self-evolving-defense-misevolution.md` |
| Location | OSINT archive; cyber synthesis only |
| Code | hunt before clone; REFERENCE unless SPDX + <500MB |

## Narrative

HARD is a borrowable **defense-evolution loop**: run attack tasks → judge trajectories → route failures to a **semantic-policy evolver** or a **tool-gate evolver** → redeploy → re-test on a held-out split. Reported ASR cut to 12.1%/1.3%/13.9%/7.4% (DPI/IPI/MC/SP) while holding benign utility 91–97%. Gate only high-confidence, low-FP, pre-execution-matchable patterns; else policy. Literal gate rules rot (0→97 rules, test split barely moved). Over-restriction is a failure mode. Pair with SHE (K268): name the owning harness artifact; HITL before mutating prod. [Source: arXiv:2608.12977]
