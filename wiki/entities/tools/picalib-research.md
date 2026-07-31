---
title: picalib-research — PI detector calibration study artifacts
type: entity
tags: [tool, llm-security, research, benchmark, reference]
keywords: [picalib, 2606.22659, prompt injection calibration, severity metric, anas biswas]
related:
  - sources/arxiv-2606-22659-confidently-wrong-prompt-injection-calibration.md
  - concepts/prompt-injection-detector-calibration.md
  - entities/tools/llm-defense-lattice.md
  - concepts/llm-adversarial-fuzzing.md
maturity: draft
created: 2026-06-23
updated: 2026-07-31
phase_0_verdict: "Reference 2026-06-23 — github.com/anasbiswas1/picalib-research: 0★, LICENSE null/404; reproduce severity S eval only after license audit"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

## Relations

- @sources/arxiv-2606-22659-confidently-wrong-prompt-injection-calibration.md — paper + methodology
- @concepts/prompt-injection-detector-calibration.md — severity metric S framework

## Narrative

Public code/data for **Confidently Wrong** (2606.22659) — severity-aware evaluation of ProtectAI-v2 and Prompt-Guard-2 under five distribution shifts.

**Phase-0: Reference** until LICENSE file appears. Use to replicate **severity on missed attacks** metric before trusting vendor guard calibration claims in SOC copilot deployments.
