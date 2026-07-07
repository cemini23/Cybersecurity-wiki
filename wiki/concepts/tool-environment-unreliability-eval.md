---
title: Tool-environment unreliability evaluation
type: concept
tags: [concept, agent-evaluation, tool-use, reliability, benchmark]
keywords: [tool environment unreliability, ph vs p0, hazard diagnosis, toolbench-x, recovery path]
related:
  - sources/arxiv-2606-25819-toolbench-x-tool-environment-unreliability.md
  - entities/tools/toolbench-x.md
  - concepts/agent-runtime-guardrails.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/mcp-security-posture.md
  - concepts/llm-pentest-automation.md
  - sources/arxiv-2606-07992-vats-error-path-mcp-injection-2026-06-13.md
  - concepts/ai-for-cybersecurity.md
  - sources/arxiv-2606-26904-confidence-aware-tool-orchestration-robust-to.md
  - concepts/confidence-aware-tool-orchestration.md
  - concepts/security-tool-orchestration-determinants.md
  - sources/arxiv-2607-02873-hexstrike-security-tool-orchestration.md
maturity: draft
created: 2026-06-27
updated: 2026-07-03
---

**Briefs:** `briefs/2026-07-02_robust-to-confidence-aware-tool-routing-handoff.md`, `briefs/2026-07-02_prod-mcp-tool-confidence-contract-checklist.md`

## Relations

- @sources/arxiv-2606-25819-toolbench-x-tool-environment-unreliability.md — ToolBench-X benchmark (2606.25819)
- @concepts/seclaw-agent-security-evaluation.md — complementary security-trajectory eval

## Raw Concept

Ingest 2026-06-27: arXiv:2606.25819 — eval gap between clean tool kernels **P₀** and production **P_h** where tools drift, fail, or conflict.

## Narrative

### Problem framing

Classic function-calling benchmarks test **action correctness** under **P₀**: valid calls return documented outputs. Production MCP/API layers violate this — schemas drift, calls fail, outputs corrupt, sources disagree. Multi-step agents compound errors through argument generation and evidence aggregation.

Key metric: **V^π_P₀ − V^π_P_h** (performance degradation under hazards), not call syntax accuracy alone.

### Hazard taxonomy (ToolBench-X)

| Hazard | Agent challenge |
|--------|-----------------|
| Specification drift | Re-read schema / alternate tool |
| Invocation error | Retry with corrected args |
| Execution failure | Fallback path |
| Output drift | Normalize / validate fields |
| Cross-source conflict | Cross-check evidence |

Each injected instance must retain ≥1 **valid recovery path**.

### Diagnosis vs compute (2606.25819)

Hint-after-failure recovers **60–80%** of accuracy lost to hazards; extra interaction rounds (TTS) help less. Implies prod agents need **hazard classifiers + recovery policies**, not just bigger models or more tool calls.

### prod-mcp / lazy-tool checklist `[TENTATIVE]`

1. Regression-test Tier-2 agents on **injected tool faults**, not only happy-path MCP calls
2. Log hazard type when tool returns error/drift — measure diagnosis rate
3. Separate **security eval** (SeClaw/AgentDojo) from **reliability eval** (ToolBench-X class)
4. Pair with VATS error-path red-team (@sources/arxiv-2606-07992-vats-error-path-mcp-injection-2026-06-13.md) — adversarial errors ≠ benign faults but share recovery gap

See `briefs/2026-06-27_toolbench-x-prod-mcp-reliability-eval-checklist.md`.

### Confidence propagation (Robust-TO — 2606.26904)

ToolBench-X measures **whether agents recover** from hazards; Robust-TO adds **whether agents know they should distrust** degraded inputs — the **Blind Trust Problem** (accuracy drops while confidence stays flat). Steal: require MCP wrappers to return `(result, confidence)` and tier evidence before Tier-2 actions. Phase-0 **Reference** (video CV paper; code pending). See @concepts/confidence-aware-tool-orchestration.md and `briefs/2026-07-02_prod-mcp-tool-confidence-contract-checklist.md`.

## Snippets

Best ToolBench-X accuracy under hazards: **0.513** (Doubao-Seed-2.0-Lite); most frontier models **<0.50**.

[Source: arxiv-2606.25819 Table 2]
