---
title: "Fine-tuning LLMs for translation — general forgetting vs MT instruction"
type: source
tags: [source, arxiv, agent-security]
keywords: [2609.28395, k368]
related:
  - concepts/translation-finetune-forgetting-mt-instruction-audit.md
  - concepts/cross-lingual-safety-transfer-lrl.md
maturity: validated
read_status: deep-read
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
| Read status | deep-read (2026-09-25) |

## Narrative

**K368** (AppTek/RWTH) — MT parallel-data **SFT** improves COMET (e.g. Amharic→En **45.6 → 71.5**) but risks **MT-IF** (formality, gender, length controls). **General forgetting mitigations** screened on Llama 3.2 1B then 3.1 8B (AR-EN, ES-EN): **EWC** best preserves **general benchmarks** (ES-EN avg general **−1.7** vs **−11.0** for plain SFT) yet **still drops formality/gender control** vs SFT; only **data mixing with control-task examples** retains controls — **does not generalize to unseen prompts** for the same control.

Steal: after **any domain fine-tune** on deployed agents, re-run **task-specific instruction eval**, not general retention alone (pairs K304 RIM).
## Snippets

> "Elastic Weight Consolidation preserves general capabilities best … yet its scores for formality and grammatical gender control remain close to standard fine-tuning. Only data mixing with control-task examples preserves these controls." [Source: arXiv 2609.28395 abstract]