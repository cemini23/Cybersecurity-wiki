---
title: "ARENA — audio-grounded LALM red-team controller (REFERENCE)"
type: entity
tags: [tool, red-team, audio, lalm, reference, k282]
keywords: [ARENA, 2608.15578, MD-Judge, LlamaGuard3, audio red team]
related:
  - sources/arxiv-2608-15578-arena-audio-lalm-redteam.md
  - concepts/audio-grounded-lalm-redteaming.md
  - concepts/inaudible-low-frequency-audio-attacks.md
  - entities/tools/ill-inaudible-low-frequency-lockout.md
  - concepts/llm-adversarial-fuzzing.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
phase_0_verdict: "REFERENCE 2026-08-18 — no public repo URL / no SPDX at retrieval. Do not invent a clone path."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K282)"
---

## Relations

- @sources/arxiv-2608-15578-arena-audio-lalm-redteam.md
- @concepts/audio-grounded-lalm-redteaming.md
- @concepts/inaudible-low-frequency-audio-attacks.md
- @entities/tools/ill-inaudible-low-frequency-lockout.md
- @concepts/llm-adversarial-fuzzing.md

## Raw Concept

Paper artifact for closed-loop audio-grounded red-teaming of LALMs. Controller + split train/eval judges. No installable tree at retrieval.

## Narrative

Use as a **method template** when evaluating audio-capable models in the authorized lab: text-safe + audio-harmful pair; hold out AdvBench-class objectives; freeze the report judge. Re-check GitHub before any clone. Dual-ID: Cybersec K282 ≠ CCC K282 AgentRewind.

## Local adoption

| Field | Value |
|-------|-------|
| Verdict | REFERENCE (no public SPDX URL) |
| Path | none |
| LICENSE | n/a |
| Wire | K282 → `cemini-cybersec-lab-redteam.mdc` |
