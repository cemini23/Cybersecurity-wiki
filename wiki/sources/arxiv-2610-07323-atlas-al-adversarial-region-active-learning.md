---
title: "ATLAS-AL: adaptive trust-region for latent adversarial searches via active learning"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.07323, k403]
related:
  - concepts/threat-preserving-representation-sensitivity.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/adversarial-region-estimation-vs-single-example.md
  - concepts/benchmark-shortcut-attack-pyramid-audit.md
  - concepts/guardrail-construct-validity-agent-eval.md
maturity: draft
read_status: read
created: 2026-10-07
updated: 2026-10-09
phase_0_verdict: "REFERENCE 2026-10-07 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K403)"
---

## Relations

- @concepts/threat-preserving-representation-sensitivity.md — K408-K417 ingest / 2026-10-09
- @concepts/llm-adversarial-fuzzing.md — K408-K417 ingest / 2026-10-09
- @concepts/adversarial-region-estimation-vs-single-example.md — K408-K417 ingest / 2026-10-09
## Relations

- @concepts/adversarial-region-estimation-vs-single-example.md
- @concepts/threat-preserving-representation-sensitivity.md
- @concepts/benchmark-shortcut-attack-pyramid-audit.md
- @concepts/guardrail-construct-validity-agent-eval.md
- @concepts/llm-adversarial-fuzzing.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | ATLAS-AL: adaptive trust-region for latent adversarial searches via active learning |
| arXiv | 2610.07323 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.07323-atlas-al-adaptive-trust-region-for-latent-advers.pdf |
| Retrieved | 2026-10-07 |
| Read status | read (deep-read) |

## Narrative

**K403** — most black-box attacks optimise for **one** successful adversarial example. This argues the useful object is a **representative adversarial SET** — an estimate of the whole failure **region**, which tells you *where and how* a system fails and supports **continuous auditing** as robustness drifts. ATLAS casts attack generation as **active learning level-set estimation**, combining **calibrated approximations** of the target with a **local-global sampling** architecture: the model samples where it is uncertain rather than uniformly, so fewer queries land in regions already known well. On toy problems it recovers more of the adversarial region under a **limited query budget** than prior work, and on standard and adversarially-trained MNIST / CIFAR / ImageNet it produces better representative attacks than **NES, SignHunter, BayesOpt**. Operator steal: **audit coverage, not a single failure** — and note that adversarial training is a target condition here, not an assumed defence. Pairs K396 (report sensitivity, not one number) and K388 (breaking level): all three replace a point score with a claim about a region. Lab only, owned or procured models. **No attack code or perturbation recipes in wiki.**

## Snippets

> See arXiv 2610.07323 abstract. [Source: arXiv 2610.07323 (retrieved 2026-10-07)]
