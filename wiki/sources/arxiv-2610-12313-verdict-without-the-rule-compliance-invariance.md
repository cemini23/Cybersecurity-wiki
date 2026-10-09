---
title: "Verdict without the rule: diagnosing and auditing LLM compliance systems"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.12313, k415]
related:
  - concepts/compliance-verdict-rule-invariance.md
  - concepts/citation-is-not-consultation.md
  - concepts/compliance-boundary-adjacent-pair-search.md
  - concepts/guardrail-construct-validity-agent-eval.md
maturity: draft
read_status: read
created: 2026-10-09
updated: 2026-10-09
phase_0_verdict: "REFERENCE 2026-10-09 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K415)"
---

## Relations

## Relations

- @concepts/compliance-verdict-rule-invariance.md
- @concepts/citation-is-not-consultation.md
- @concepts/compliance-boundary-adjacent-pair-search.md
- @concepts/guardrail-construct-validity-agent-eval.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Verdict without the rule: diagnosing and auditing LLM compliance systems |
| arXiv | 2610.12313 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.12313-verdict-without-the-rule-diagnosing-and.pdf |
| Retrieved | 2026-10-09 |
| Read status | read (deep-read) |

## Narrative

**K415 — an LLM compliance verdict may not depend on the rule it was given.** The test is direct: **delete, swap, or negate the governing rule while holding the case fixed**, and check whether the verdict changes (**OCS**) or the model's internal compliance representation shifts at all (**ICS-delta**). Across five models and 20 regulatory / platform-policy domains, neither moves much: mean **OCS-agg = 0.069**, i.e. roughly **7% of verdicts change** when the rule is perturbed, against ~90% baseline accuracy. Best single case is still only **0.265**.

Two things keep this from being a measurement artefact, and they are the reason to trust it. First, a **bias-corrected permutation null** puts the expected OCS near 0.5 while observed sits at 0.07–0.09 (every p < 0.0001). Second, on the **rule-necessary subset** — cases where the baseline is right and deletion makes it wrong — OCS-swap is **0.73–1.00** against a pooled 0.08–0.12. So the metric *does* fire when the rule genuinely decides. The authors' own reading is that low OCS largely reflects **scenario-side label signal**: the case facts alone determine the verdict in most items. LegalBench (**0.255**) and ContractNLI (**0.318**) move far more than the synthetic set (0.081), which is exactly what you would expect if the synthetic cases are easier to call from facts alone. Operator steal: **a compliance model's verdict is not evidence that it consulted the rule** — audit with a rule perturbation and report the rule-necessary subset separately. Pairs K416 and K398.

## Snippets

> See arXiv 2610.12313 abstract. [Source: arXiv 2610.12313 (retrieved 2026-10-09)]
