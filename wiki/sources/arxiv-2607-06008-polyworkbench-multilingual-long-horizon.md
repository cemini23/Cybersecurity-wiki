---
title: PolyWorkBench — multilingual long-horizon agents (arXiv 2607.06008)
type: source
tags: [source, arxiv, benchmark, multilingual, long-horizon, agent-evaluation]
keywords: [2607.06008, polyworkbench, tencent, bjtu, claudecode, openclaw, hermes, codex]
related:
  - concepts/multilingual-long-horizon-agent-evaluation.md
  - entities/platforms/polyworkbench.md
  - concepts/security-tool-orchestration-determinants.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - concepts/ai-for-cybersecurity.md
  - sources/arxiv-2607-03510-cage-1-enterprise-agent-governance.md
  - "@ccc-wiki/sources/arxiv-polyworkbench-multilingual-long-horizon-2607.06008.md"
maturity: draft
read_status: read
created: 2026-07-10
updated: 2026-07-10
phase_0_verdict: "REFERENCE 2026-07-10 — 67-task benchmark paper; ClaudeCode/OpenClaw/Hermes/Codex harness matrix; no public GitHub at Phase-0; steal hybrid eval rubric + client-disclosure discipline"
---

**Briefs:** `briefs/2026-07-10_polyworkbench-multilingual-eval-handoff.md`, `briefs/2026-07-10_k152-polyworkbench-multilingual-eval-prod.md`

## Relations

- @concepts/multilingual-long-horizon-agent-evaluation.md — synthesis
- @sources/arxiv-2607-03510-cage-1-enterprise-agent-governance.md — governance eval complement (same batch)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | PolyWorkBench: Benchmarking Multilingual Long-Horizon LLM Agents |
| Authors | Hongliang Li, Yijin Liu, Zhiwei Zhang, et al. (BJTU + Weixin AI, Tencent) |
| arXiv | 2607.06008v2 [cs.AI] |
| Code | **Not found** at Phase-0 — paper states benchmark manifest ships with release |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.06008-2607-06008v1-polyworkbench-benchmarking-multilin.pdf` |
| Retrieved | 2026-07-10 |
| Read status | **read** (67 tasks, hybrid eval, harness sensitivity, leaderboard) |

## Narrative

PolyWorkBench evaluates **multilingual long-horizon workplace workflows** — language variation embedded in execution, not a single translation step.

### Benchmark design

| Stat | Value |
|------|-------|
| Tasks | **67** (29 baseline ~6–8 steps, 38 stress ~8–12 steps; mean **8.5** steps) |
| Domains | Commerce (16), Legal (15), Knowledge (11), Localization (11), Manufacturing (14) |
| Languages | 10 — EN, ZH, JA, KO, VI, RU, FR, ES, DE, AR |
| Trilingual | **88%** of tasks use **3+ languages** across instruction/source/output roles |
| Inputs | ~9.3 files/task; ~3.9 output artifacts/task |

### Hybrid evaluation

| Component | Role | Alignment |
|-----------|------|-----------|
| **Pytest** | Executable verification | Strong |
| **Grade()** | Weighted structural rubric | r=**0.85** with Pytest |
| **LLM Judge** | Semantic/fluency | r=**0.18** with Grade overall; bimodal (60% ≥0.8, 22.5% ≤0.5) |

Within Grade≥0.5 regime, Grade–Judge correlation **collapses to r=−0.04** — Judge catches semantic degradations deterministic checks miss but is **not a standalone ranking metric**.

### Leaderboard highlights [CONFIRMED paper Table 1]

| Model × Harness | Pass@1 (mean Grade) |
|-----------------|---------------------|
| Claude Opus 4.8 × ClaudeCode | **0.921** |
| DeepSeek-v4-Flash × ClaudeCode | 0.796 |
| GPT-5.5 × OpenClaw | 0.776 |
| Qwen-Agent-World × OpenClaw/Hermes | ~0.762 |

**Harness sensitivity:** same model spans **≥0.08–0.21** Pass@1 across harnesses; ClaudeCode best or tied-best when available — corroborates @concepts/security-tool-orchestration-determinants.md client-first-order thesis.

**Pass@3 headroom:** mid-tier models gain **+0.10–0.21** from best-of-3; top models near-saturated (+0.007).

### Phase-0 (2026-07-10)

| Gate | Status |
|------|--------|
| Public artifact | **NOT FOUND** — monitor for Tencent/BJTU release |
| Domain fit | Harness regression design; weak direct pentest tradecraft |
| Verdict | **REFERENCE** — hybrid eval steal; disclose harness in any agent score |

## Snippets

> "Reporting a model's benchmark score without disclosing the harness is therefore not meaningful."
> — [Source: arxiv-2607.06008 §4 harness sensitivity, retrieved 2026-07-10]

> "Multilinguality introduces compounding effects across reasoning and execution steps."
> — [Source: arxiv-2607.06008 abstract, retrieved 2026-07-10]
