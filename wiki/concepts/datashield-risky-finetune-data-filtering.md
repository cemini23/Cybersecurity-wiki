---
title: DataShield — filtering risky fine-tune data via consensus subspaces
type: concept
tags: [concept, llm-safety, fine-tuning, data-centric]
keywords: [datashield, fine-tune safety degradation, segment masking, consensus subspace]
related:
  - sources/arxiv-2607-15081-datashield-risky-finetune-data.md
  - entities/tools/datashield.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/agent-runtime-guardrails.md
  - concepts/self-evolving-agent-security.md
  - concepts/ai-for-cybersecurity.md
  - concepts/rubric-capability-tree-diagnosis.md
  - sources/arxiv-2607-16122-craft-rubric-capability-diagnosis.md
  - concepts/defender-centric-jailbreak-utility.md
  - sources/arxiv-2607-17152-a-mess-defender-centric-jailbreak.md
  - concepts/gradient-immunity-malicious-finetune.md
  - sources/arxiv-2608-05045-gradient-immunity-malicious-finetune.md
maturity: draft
created: 2026-07-17
updated: 2026-08-06
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc"
---

## Relations

- @sources/arxiv-2607-17152-a-mess-defender-centric-jailbreak.md
- @concepts/defender-centric-jailbreak-utility.md
- @sources/arxiv-2607-15081-datashield-risky-finetune-data.md — paper
- @entities/tools/datashield.md — implementation
- @concepts/rubric-capability-tree-diagnosis.md — diagnose capability gaps then filter FT risk
- @sources/arxiv-2607-16122-craft-rubric-capability-diagnosis.md
- @concepts/gradient-immunity-malicious-finetune.md
- @sources/arxiv-2608-05045-gradient-immunity-malicious-finetune.md

## Raw Concept

How do you keep safety alignment when fine-tuning on “benign” domain data that still shifts the model toward harmful compliance?

## Narrative

**Problem:** Fine-tuning on normal task data can raise ASR on harmful queries even when samples look clean.

**DataShield approach:** Build joint safety-critical semantic spaces from multiple aligned LLMs → extract consensus safe/unsafe subspaces → score each sample/segment by relative alignment → filter samples or mask risky segments.

Prefer **segment masking** when utility must stay high (−32.3% ASR vs −14.6% for sample filter in paper). [CONFIRMED — abstract]

### Ops checklist

| Step | Action |
|------|--------|
| 1 | Inventory any planned fine-tune corpus |
| 2 | Run consensus risk scoring (multi-model) |
| 3 | Mask high-risk segments before train |
| 4 | Re-eval jailbreak ASR + utility after FT |

## Snippets

See source page.
