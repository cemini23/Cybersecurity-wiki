---
title: "Quantized-LLM jailbreak defense — atlas retrieval (K389)"
type: concept
tags: [concept, agent-security, k389]
keywords: [2610.01058, K389]
related:
  - sources/arxiv-2610-01058-momat-quantized-llm-jailbreak-defense.md
  - concepts/defender-centric-jailbreak-utility.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/instruction-hierarchy-conflict-benchmark.md
maturity: draft
created: 2026-10-02
updated: 2026-10-02
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K389)"
---

## Relations

- @sources/arxiv-2610-01058-momat-quantized-llm-jailbreak-defense.md
- @concepts/defender-centric-jailbreak-utility.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/crescendo-multi-turn-jailbreak.md
- @concepts/instruction-hierarchy-conflict-benchmark.md

## Raw Concept

Question: **Quantized-LLM jailbreak defense — atlas retrieval** — operator steal from arXiv 2610.01058?

## Narrative

**Quantisation degrades safety alignment, and smaller models lose more.** Before deploying a guard on a quantised model, re-measure **ASR at the shipped precision** — a model that was aligned in FP16 can be materially weaker at W4A8. Measure **FRR** too: a defense that suppresses ASR by over-refusing benign traffic is a failure, and the useful result here is zero ASR with **FRR unchanged**. The defense pattern worth stealing is **domain-localised retrieval** (atlases) rather than one flat safety corpus, because quantisation erodes exactly the global embedding geometry a flat corpus relies on.

## Snippets

> See arXiv 2610.01058 abstract. [Source: arXiv 2610.01058 (retrieved 2026-10-02)]
