---
title: A-MESS / AttackSHAP — defender-centric jailbreak evaluation (arXiv 2607.17152)
type: source
tags: [source, arxiv, jailbreak, safety-alignment, shapley, red-team]
keywords: [2607.17152, A-MESS, AttackSHAP, defender-centric, ASR vs safety utility]
related:
  - concepts/defender-centric-jailbreak-utility.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/pair-prompt-pattern.md
  - concepts/datashield-risky-finetune-data-filtering.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-21
updated: 2026-07-31
phase_0_verdict: "REFERENCE 2026-07-21 — method paper; no public code at ingest; steal AttackSHAP / subset selection over ASR ranking"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

**Briefs:** `briefs/2026-07-21_k197-a-mess-defender-centric-jailbreak-prod.md`

## Relations

- @concepts/defender-centric-jailbreak-utility.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/crescendo-multi-turn-jailbreak.md
- @concepts/pair-prompt-pattern.md
- @concepts/datashield-risky-finetune-data-filtering.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | How Jailbreak Attacks Inform Safety Alignment: A Defender-Centric, Shapley-Based Evaluation of Jailbreak Contributions |
| Authors | Yukai Zhou, Feiyang Lu, Xiaokai Mao, Jinfei Liu, Wenjie Wang |
| Affiliation | ShanghaiTech; Zhejiang University |
| arXiv | 2607.17152 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.17152-how-jailbreak-attacks-inform-safety-alignment-a.pdf` |
| Retrieved | 2026-07-21 |
| Public code | None found |

## Narrative

ASR rankings ask "what breaks the model?" A-MESS asks "which attack subsets most improve **downstream safety** when used as red-team training data?" Introduces **AttackSHAP** (Shapley attribution of subset utility) and budgeted subset selection (greedy / surrogate). Finding: ASR rankings are **weakly aligned** with defender utility; optimizing subsets beats attacker-centric or attribution-only selection.

### Steal

1. Rank jailbreak corpora by safety-train utility, not ASR alone
2. Prefer compact AttackSHAP-selected subsets under token/budget caps
3. Pair with DataShield when using jailbreak data for FT

### Phase-0

| Gate | Status |
|------|--------|
| Code | Missing |
| Verdict | **REFERENCE** |

## Snippets

> "an attack that breaks a model is not necessarily useful for improving its safety."
[Source: arxiv-2607.17152 abstract]
