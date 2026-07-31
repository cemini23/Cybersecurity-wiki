---
title: What AI red-team evaluations can and cannot prove (arXiv 2607.21735)
type: source
tags: [source, arxiv, llm-safety, red-teaming, evaluation]
keywords: [2607.21735, evidential ceiling, HarmBench, AdvBench, null result]
related:
  - concepts/ai-redteam-evidential-ceiling.md
  - entities/tools/ai-redteam-evidential-limits.md
  - concepts/ai-for-cybersecurity.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/pair-prompt-pattern.md
maturity: draft
read_status: read
created: 2026-07-29
updated: 2026-07-31
phase_0_verdict: "GO 2026-07-29 — MIT; github.com/hackwither/ai-redteam-evidential-limits ~528KB"
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc"
---

**Briefs:** `briefs/2026-07-29_k220-ai-redteam-evidential-ceiling-prod.md`

## Relations

- @concepts/ai-redteam-evidential-ceiling.md
- @entities/tools/ai-redteam-evidential-limits.md
- @concepts/ai-for-cybersecurity.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/pair-prompt-pattern.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | What AI Red-Team Evaluations Can and Cannot Prove |
| Authors | Bandana Kaur (APIsec Research Labs) |
| arXiv | 2607.21735 |
| Code | github.com/hackwither/ai-redteam-evidential-limits (MIT) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.21735-what-ai-red-team-evaluations-can-and-cannot-prov.pdf` |
| Retrieved | 2026-07-29 |

## Narrative

Defines an **evidential ceiling**: largest belief-update factor a fixed-budget evaluation can produce. Closed form for benchmark null results. Above a calculable harm rate, a modest clean benchmark certifies a category and can outweigh a single reproduced failure; below it, no feasible passive benchmark provides the stated safety evidence. Audits eight suites — adequate for high-frequency harms, orders of magnitude short for rare catastrophic ones.

### Steal

1. State which propositions an eval licenses **before** running it
2. Do not treat clean sheets on small suites as rare-catastrophe safety proof
3. Discrimination between hypotheses (not raw ASR) determines evidential worth — applies to adaptive/automated red teaming too

## Snippets

> "Safety benchmarks are not uninformative. They are informative about a specific and computable set of propositions, and the discipline they need is to state which."
[Source: arxiv-2607.21735 abstract]
