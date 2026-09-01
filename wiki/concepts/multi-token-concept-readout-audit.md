---
title: "Multi-token concept readout audit — first token ≠ full concept (K318)"
type: concept
tags: [concept, interpretability, audit, agent-security, k318]
keywords: [J-lens, multi-token concepts, SAE verbalization, first token clue, refusal surface audit, Neuronpedia]
related:
  - sources/arxiv-2608-31084-j-lens-multi-token-readout.md
  - concepts/counterfactual-simulatability-llm-explanations.md
  - concepts/chain-of-thought-decorative-reasoning-audit.md
  - concepts/agent-runtime-guardrails.md
maturity: draft
created: 2026-09-01
updated: 2026-09-01
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K318)"
---

## Relations

- @sources/arxiv-2608-31084-j-lens-multi-token-readout.md — J-lens (2608.31084)
- @concepts/counterfactual-simulatability-llm-explanations.md — K290 CHIVE: explanations need counterfactual tests
- @concepts/chain-of-thought-decorative-reasoning-audit.md — K308: visible reasoning ≠ evidence

## Raw Concept

Question: **when does interpretability labeling mislead safety audits on multi-token behaviors?**

## Narrative

Single-token SAE labels can **misname** multi-token refusal/harm concepts. **J-lens (K318)** uses first-token generation as an anchor and iterates verbalization until the description matches the feature's multi-token role — useful for **pre-deployment refusal-surface mapping** alongside Taboo-style decoding probes.

**Operator steal:**
1. **Interpretability labels are hypotheses** — counterfactual-test before hardening (pairs K290).
2. **Recognition ≠ enforcement** — verbalized concepts do not replace hooks/Mandato/step gates (pairs K314).
3. Neuronpedia J-lens = **WATCH** tooling for lab audits; no runtime wire into prod harness.

## Snippets

> Standard verbalization can collapse multi-token semantics into a misleading single-token label. [Source: arXiv 2608.31084, paraphrase from abstract theme]
