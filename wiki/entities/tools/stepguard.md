---
title: StepGuard (AgentDoG)
type: entity
tags: [entity, tool, agent-security, guardrail, k307]
keywords: [StepGuard, StepGen, Balance-GRPO, zheng977, ninty-seven, agent guard, EMNLP 2026]
related:
  - sources/arxiv-2608-24777-stepguard.md
  - concepts/step-level-agent-guardrails.md
  - concepts/agent-runtime-guardrails.md
maturity: draft
created: 2026-08-26
updated: 2026-09-30
phase_0_verdict: "CONDITIONAL-GO 2026-08-26 — github.com/zheng977/StepGuard. LICENSE cleared 2026-09-30: Apache-2.0. Sparse REFERENCE clone adopted 2026-09-30 (~3MB). HF weights held. Inventory: scripts/stepguard_inventory.sh. Runtime wont_wire."
wire_status: reference_clone
wire_target: "REFERENCE clone via scripts/stepguard_inventory.sh adopt (LICENSE cleared 2026-09-30); no default Cursor MCP — wont_wire runtime"
---

## Relations

- @sources/arxiv-2608-24777-stepguard.md
- @concepts/step-level-agent-guardrails.md

## Raw Concept

StepGuard is a **4B step-level guard model** (Shanghai AI Lab AgentDoG team) for pre-execution tool-action checking and post-hoc trajectory audit. Training uses StepGen synthetic data + Balance-GRPO safety–utility balancing.

## Narrative

| Field | Value |
|-------|-------|
| Repo | `https://github.com/zheng977/StepGuard` |
| Model | `https://huggingface.co/ninty-seven/StepGuard` |
| License | **Apache-2.0** — LICENSE file present; verified 2026-09-30 (was null SPDX at the 2026-08-26 hunt) |
| Size | ~6 MB repo (code + assets) |
| Verdict | **CONDITIONAL-GO** — methodology steal + REFERENCE clone (LICENSE cleared 2026-09-30); **no weight download** in wiki ingest; **wont_wire** as default harness MCP |
| Local adoption | `.local/adopts/StepGuard` (gitignored) — **sparse REFERENCE clone, ~4MB**, 2026-09-30. Keeps `src/ tests/ training/ scripts/ configs/ docs-open/ assets/ benchmarks/`; excludes the bundled `benchmark-repos/` (~46MB ASSEBench payload — the full tree is 54MB and trips the 50MB cap). Clone/refresh: `bash scripts/stepguard_inventory.sh adopt`. Note: the repo's own `benchmarks/README.md` says it does **not** redistribute benchmark payloads, so `pytest tests/` reports expected failures until those are downloaded separately |

**Adoption gate:** cleared 2026-09-30 (Apache-2.0); sparse REFERENCE clone adopted the same day. Re-hunt with `bash scripts/stepguard_inventory.sh check`, refresh with `adopt`. The clone is a **steal-from reference**, not a runtime dependency — `wont_wire` as a default Cursor MCP. Do not curl|bash install scripts. Lab eval only on owned agent harnesses; **no HF weight download** in wiki automation.

## Snippets

> StepGuard achieves the highest average accuracy among open-weight guard models, with performance comparable to GPT-5.4. [Source: arXiv 2608.24777 abstract — verify locally before citing in engagements]
