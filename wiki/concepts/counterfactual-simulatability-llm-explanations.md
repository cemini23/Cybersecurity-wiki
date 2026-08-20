---
title: "Counterfactual simulatability of LLM explanations"
type: concept
tags: [concept, methodology, interpretability, eval, k290]
keywords: [counterfactual simulatability, CHIVE, explanation-as-evidence, SAE, CoT faithfulness]
related:
  - sources/arxiv-2608-16747-chive-counterfactual-explanations.md
  - entities/tools/chive.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/llm-code-review-agent-security.md
  - sources/arxiv-2608-18351-excess-authority-least-privilege.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K290)"
---

## Relations

- @sources/arxiv-2608-16747-chive-counterfactual-explanations.md
- @entities/tools/chive.md — GO REFERENCE clone, runtime wont_wire
- @concepts/ai-redteam-evidential-ceiling.md — narrative explanation ≠ certified cause
- @concepts/faithful-agent-asr-measurement.md — process-level measurement
- @concepts/llm-code-review-agent-security.md — do not accept agent “why” without a counterfactual

## Raw Concept

When is an explanation of model or agent behavior *evidence*? Only if it predicts related counterfactual inputs.

## Narrative

Open-ended CoT, SAE feature write-ups, and investigator narratives can be compelling and still wrong. CHIVE treats an explanation as a **behavioral claim** tested by prompt edits: true if the edit moves the behavior rate by a large margin, false if it barely moves. Interpretability tools that help in planted-quirk auditing games showed **no uplift** on naturally occurring behaviors.

**Operator steal.** When an agent or a review model explains a refusal, a bug, or a tool choice, require at least one counterfactual test before filing the explanation as evidence. Training to *predict* counterfactual outcomes beat training to *narrate* causes.

Runtime **wont_wire** — this is an eval discipline, not a pentest tool.

## Snippets

> Throughout, an explanation is a behavioral claim testable by counterfactual experiments, not an explanation of the model’s internal computation or of the training data that produced the behavior. [Source: arXiv 2608.16747 §1]
