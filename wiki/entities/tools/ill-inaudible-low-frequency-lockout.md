---
title: "ILL — Intermittent Low-Frequency Lockout (inaudible LALM red-team method)"
type: entity
tags: [tool, red-team, audio-attack, lalm, reference]
keywords: [ILL, inaudible, low-frequency, LALM, DRG, distributional requery, 2608.09158]
related:
  - sources/arxiv-2608-09158-ill-inaudible-low-frequency-lalms.md
  - concepts/inaudible-low-frequency-audio-attacks.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-08-11
updated: 2026-08-11
phase_0_verdict: "REFERENCE 2026-08-11 — no public code URL; black-box method + DRG defense. K267 policy wire."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K267)"
---

## Relations

- @sources/arxiv-2608-09158-ill-inaudible-low-frequency-lalms.md
- @concepts/inaudible-low-frequency-audio-attacks.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/agent-runtime-guardrails.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

Paper artifact (2608.09158): ILL = black-box red-teaming method + DRG = plug-in input-filter defense for large audio-language models. No repo at retrieval — method/template description only.

## Narrative

Use when evaluating audio-capable LLM agents (mic frontend) in the authorized lab: ILL is the reference for the 5–20 Hz availability-attack surface; DRG is the reference for the spectral-descriptor requery defense. Do not treat as an installable tool — no public code. Physical deployment requires a low-frequency-capable source; authorized scope only.

## Local adoption

| Field | Value |
|-------|-------|
| Verdict | REFERENCE (no public repo) |
| Path | none (paper-only) |
| LICENSE | n/a |
| Wire | K267 policy wire → `cemini-cybersec-lab-redteam.mdc` |
