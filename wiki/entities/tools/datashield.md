---
title: DataShield — risky fine-tune data filter (ZJU)
type: entity
category: tool
tags: [entity, tool, llm-safety, fine-tuning, mit, conditional-go]
keywords: [datashield, zju-llm-safety, consensus subspace]
related:
  - sources/arxiv-2607-15081-datashield-risky-finetune-data.md
  - concepts/datashield-risky-finetune-data-filtering.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-for-cybersecurity.md
  - concepts/self-evolving-agent-security.md
maturity: draft
created: 2026-07-17
updated: 2026-07-31
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc"
---

## Relations

- @sources/arxiv-2607-15081-datashield-risky-finetune-data.md — paper
- @concepts/datashield-risky-finetune-data-filtering.md — concept

**Local clone:** `raw-sources/repos/DataShield` (~3MB, gitignored under `raw-sources/`)

## Raw Concept

MIT FOSS toolkit for scoring/filtering fine-tune samples that degrade safety alignment via consensus subspace alignment across models.

## Narrative

### Phase-0 (2026-07-17): CONDITIONAL-GO

| Gate | Status |
|------|--------|
| License | **PASS** — MIT |
| Size | **PASS** — ~3MB |
| Maturity | **WATCH** — new (2026-07-16), 4★ |
| Stack | Python; `environment.yml` / `requirements.txt`; multi-model embeddings likely heavy at runtime |
| Verdict | **CONDITIONAL-GO** — laptop reference clone; run only in lab before any Cemini/TipDrop fine-tune |

### Final

- Cybersec: primary home
- Do not run against production model weights without isolated lab + authorization
