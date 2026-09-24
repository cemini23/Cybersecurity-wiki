---
title: "Fine-tuning LLMs for translation — general forgetting vs MT instruction"
type: source
tags: [source, arxiv, agent-security]
keywords: [2609.28395, k368]
related:
  - concepts/translation-finetune-forgetting-mt-instruction-audit.md
  - concepts/cross-lingual-safety-transfer-lrl.md
maturity: draft
read_status: read
created: 2026-09-24
updated: 2026-09-24
phase_0_verdict: "REFERENCE 2026-09-24 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K368)"
---

## Relations

- @concepts/translation-finetune-forgetting-mt-instruction-audit.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Fine-tuning LLMs for translation — general forgetting vs MT instruction |
| arXiv | 2609.28395 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.28395-fine-tuning-llms-for-translation-general-forgett.pdf |
| Retrieved | 2026-09-24 |
| Read status | read (abstract + triage) |

## Narrative

**K368** — **general forgetting mitigation** metrics on broad benchmarks do **not** guarantee preservation of **MT-specific instruction following** after parallel-data fine-tune. Steal: any domain fine-tune is a **safety/capability event** — re-run task-specific eval (pairs K304 RIM). REFERENCE.

## Snippets

> See arXiv 2609.28395 abstract. [Source: arXiv 2609.28395 (retrieved 2026-09-24)]
