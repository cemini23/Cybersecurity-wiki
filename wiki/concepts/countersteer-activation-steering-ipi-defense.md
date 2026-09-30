---
title: "CounterSteer inference-time IPI steering defense (K383)"
type: concept
tags: [concept, agent-security, k383]
keywords: [2609.36570, K383]
related:
  - sources/arxiv-2609-36570-countersteer-activation-steering-ipi-defense.md
  - concepts/prompt-injection-detector-calibration.md
  - concepts/piminer-agentic-prompt-injection-redteam.md
maturity: draft
created: 2026-09-30
updated: 2026-09-30
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-mcp-tool-control.mdc (K383)"
---

## Relations

- @sources/arxiv-2609-36570-countersteer-activation-steering-ipi-defense.md
- @concepts/prompt-injection-detector-calibration.md
- @concepts/piminer-agentic-prompt-injection-redteam.md

## Raw Concept

Question: **CounterSteer inference-time IPI steering defense** — operator steal from arXiv 2609.36570?

## Narrative

A **suppression** defense, not a detector: fit one residual direction per model, gate it causally and on capability, then subtract it from **every tool-result token at prefill**. Always on, so there is no detection decision to evade. Needs **white-box serving** and marked tool-result spans. **Steering does not fix parameter manipulation** — add argument-provenance controls. **No injection payloads or fitted directions in wiki.**

## Snippets

> See arXiv 2609.36570 abstract. [Source: arXiv 2609.36570 (retrieved 2026-09-30)]
