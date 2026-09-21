---
title: "Probe of Internal Recognition sandbagging audit (K352)"
type: concept
tags: [concept, agent-security, audit, sandbagging, eval, interpretability, k352]
keywords: [2609.21996, PIR, sandbagging, concealed knowledge, unlearning verification, internal recognition]
related:
  - sources/arxiv-2609-21996-lie-detector-probe-internal-recognition.md
  - concepts/counterfactual-simulatability-llm-explanations.md
  - concepts/chain-of-thought-decorative-reasoning-audit.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/faithful-agent-asr-measurement.md
maturity: draft
created: 2026-09-21
updated: 2026-09-21
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K352) + lab-redteam"
---

## Relations

- @sources/arxiv-2609-21996-lie-detector-probe-internal-recognition.md — PIR lie detector (2609.21996)

## Raw Concept

Question: **PIR sandbagging audit** — what should operators steal from this paper?

## Narrative

Capability evals assume models try to answer — **sandbagging** and concealed knowledge break that assumption. Behavior alone cannot distinguish hiding from genuine absence. **K352** steals **Probe of Internal Recognition (PIR)**: a reference-free internal-state readout that identifies which candidate answer a model recognizes, separating concealment from erasure.

Audit steal:

- Pair PIR claims with **counterfactual tests** (K290 CHIVE) — internal probes are hypotheses, not enforcement.
- Report **balanced accuracy vs unknown baseline**, not headline recognition alone.
- Use for **authorized-lab** sandbagging / unlearning verification only.
- **No probe templates, password-lock recipes, or sandbagging training payloads in wiki.**

**Runtime:** `scripts/k352_pir_sandbagging_precheck.py` (advisory checklist).

## Snippets

> When the model hides a known answer, recognition stays high; when unlearning removes knowledge, recognition drops to unknown baseline. [Source: arXiv 2609.21996 abstract]
