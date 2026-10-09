---
title: "A compliance verdict is not evidence the rule was read (K415+K416)"
type: concept
tags: [concept, agent-security, k415+k416]
keywords: [2609.12313 / 2609.12361, K415+K416]
related:
  - sources/arxiv-2610-11112-false-claims-credible-images.md
  - concepts/verification-generation-gap.md
  - concepts/citation-is-not-consultation.md
  - sources/arxiv-2610-12313-verdict-without-the-rule-compliance-invariance.md
  - sources/arxiv-2610-12361-cited-but-not-consulted-authority-swap-audit.md
  - concepts/compliance-boundary-adjacent-pair-search.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/faithful-agent-asr-measurement.md
maturity: draft
created: 2026-10-09
updated: 2026-10-09
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K415+K416)"
---

## Relations

- @sources/arxiv-2610-11112-false-claims-credible-images.md — K408-K417 ingest / 2026-10-09
- @concepts/verification-generation-gap.md — K408-K417 ingest / 2026-10-09
- @concepts/citation-is-not-consultation.md — K408-K417 ingest / 2026-10-09
- @sources/arxiv-2610-12313-verdict-without-the-rule-compliance-invariance.md
- @sources/arxiv-2610-12361-cited-but-not-consulted-authority-swap-audit.md
- @concepts/compliance-boundary-adjacent-pair-search.md
- @concepts/guardrail-construct-validity-agent-eval.md
- @concepts/faithful-agent-asr-measurement.md

## Raw Concept

Question: **A compliance verdict is not evidence the rule was read** — operator steal from arXiv 2609.12313 / 2609.12361?

## Narrative

Two matched audits from the same lab, and they say the same thing from two directions.

**K415:** perturb the **governing rule** — delete, swap, negate — with the case fixed. Mean **OCS-agg = 0.069**: only about **7%** of verdicts change, against ~90% baseline accuracy, with a permutation null near 0.5 and every p < 0.0001. On the **rule-necessary subset** the metric fires properly (**0.73–1.00**), so the tool works — it is the models that mostly do not use the rule. Detailed benchmarks move far more (**LegalBench 0.255, ContractNLI 0.318**) than a synthetic set (0.081), consistent with the synthetic cases being decidable from facts alone.

**K416:** substitute the **cited authority** for an unrelated one, hold facts fixed, and decode the verdict from hidden states. The verdict often does not follow the swap. A model naming the right statute is not evidence it reasoned from that statute.

The operator rule: **a citation is not a consultation, and a verdict is not proof the rule was applied.** Audit with a **rule perturbation**, report the rule-necessary subset separately, and where you can, read the decision from **hidden state** rather than the model's stated reason. Same family as K398 (adjacent-pair obligation boundaries) and K396 (report sensitivity, not one number).

## Snippets

> See arXiv 2609.12313 / 2609.12361 abstract. [Source: arXiv 2609.12313 / 2609.12361 (retrieved 2026-10-09)]
