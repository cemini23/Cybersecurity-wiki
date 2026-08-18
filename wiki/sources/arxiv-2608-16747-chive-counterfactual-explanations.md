---
title: "CHIVE — counterfactual simulatability of LLM explanations (arXiv 2608.16747)"
type: source
tags: [source, arxiv, interpretability, eval, k290]
keywords: [2608.16747, CHIVE, counterfactual simulatability, SAE, CoT, Gemma, randomNum]
related:
  - concepts/counterfactual-simulatability-llm-explanations.md
  - entities/tools/chive.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/llm-code-review-agent-security.md
maturity: draft
read_status: read
created: 2026-08-18
updated: 2026-08-18
phase_0_verdict: "GO REFERENCE clone 2026-08-18 — github.com/adamkarvonen/chive MIT ~11MB shallow `.local/adopts/chive`. Runtime wont_wire (interpretability eval, not a pentest tool)."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K290 CHIVE)"
---

**Briefs:** `briefs/2026-08-18_k290-chive-counterfactual.md`

## Relations

- @concepts/counterfactual-simulatability-llm-explanations.md
- @entities/tools/chive.md
- @concepts/ai-redteam-evidential-ceiling.md
- @concepts/faithful-agent-asr-measurement.md
- @concepts/llm-code-review-agent-security.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Would this change your answer? Evaluating Explanations of LLM Behavior In The Wild with Counterfactual Experiments |
| Authors | Adam Karvonen, Euan Ong, Subhash Kantamneni, Samuel Marks (Anthropic Fellows / Anthropic) |
| arXiv | 2608.16747 (cs.LG, v1 17 Aug 2026) |
| Code | `github.com/adamkarvonen/chive` — **MIT** |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.16747-would-this-change-your-answer-evaluating-explana.pdf` |
| Retrieved | 2026-08-18 |
| Read status | read (full extract) |

## Narrative

CHIVE (Counterfactual Hypothesis Investigation Via Edits) judges explanations by **counterfactual simulatability**: does the explanation predict behavior on related counterfactual inputs? Pipeline: sample → screen unexpected behaviors → investigator runs 5–15 prompt edits → independent verify. Labels come from resampled counterfactual outcomes, not the investigator's narrative.

Headline: activation-reading interpretability tools (activation oracles, NL autoencoders, SAEs) gave **no uplift** over a transcript-only predictor on in-the-wild behaviors. Gemma-3-27B `randomNum(max,min)` over-indexes on parameter **names** (max/min trigger the range error; a/b nearly extinguishes it). Training models to predict CHIVE counterfactual outcomes generalizes better than training them to emit open-ended explanations. [TENTATIVE] single paper; clone is REFERENCE only.

Steal: do not treat narrative CoT / SAE write-ups of refusals or bugs as evidence without a counterfactual test.

## Snippets

> Surprisingly, we find no uplift from any of the interpretability techniques studied. [Source: arXiv 2608.16747 abstract]

> Gemma over-indexes on the parameter names: names that suggest a range trigger the error (max/min, upper/lower), while neutral names suppress it (a/b, multiplier/offset). [Source: arXiv 2608.16747 Fig. 1]
