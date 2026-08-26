---
title: "Compliance-detector rule blindness"
type: concept
tags: [concept, guard-models, audit, watch]
keywords: [rule blindness, crossed-rule benchmark, ICS, guard verdict]
related:
  - sources/arxiv-2608-16852-rule-blindness-compliance-detectors.md
  - concepts/llm-generated-compliance-artifacts.md
  - concepts/prompt-injection-detector-calibration.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/chain-of-thought-decorative-reasoning-audit.md
maturity: draft
created: 2026-08-20
updated: 2026-08-20
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (crossed-rule audit)"
---

## Relations

- @sources/arxiv-2608-16852-rule-blindness-compliance-detectors.md
- @concepts/prompt-injection-detector-calibration.md
- @concepts/ai-redteam-evidential-ceiling.md
- @concepts/faithful-agent-asr-measurement.md — a verdict is not a grounded measurement

## Raw Concept

Does a compliance guard's verdict actually track the *stated* rule?

## Narrative

**Detector verdict ≠ rule compliance.** Before treating Llama Guard / Qwen3Guard / an activation probe as an audit control, run a **crossed-rule** counterfactual: two rules × two scenarios so that neither the rule text nor the scenario alone predicts the label. If accuracy is invariant to rule deletion/permutation/substitution, the detector is reading surface scenario features. Citation of the clause is not dependence on the clause. [Source: arXiv 2608.16852]

**ICS** (Internal Compliance Score): cheap, training-free, 10 labelled pairs. Use it to *audit many guards*, not as the production detector. Bag-of-words matching its pooled generalization is the honesty check; adaptive white-box attack is the durability check.

**Phase-0:** Watch / 0 MB. No FujitsuResearch clone as this paper's artifact. No jailbreak/exploit PoC.

## Snippets

> Step by step reasoning, not any fast detector we test, is what escapes [rule blindness]. [Source: arXiv 2608.16852 abstract]
