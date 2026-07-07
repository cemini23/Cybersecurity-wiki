---
title: Confidence-aware tool orchestration
type: concept
tags: [concept, agent-orchestration, tool-confidence, reliability, blind-trust]
keywords: [blind-trust-problem, result-confidence-pair, tiered-evidence, disturbance-aware-routing, robust-to]
related:
  - sources/arxiv-2606-26904-confidence-aware-tool-orchestration-robust-to.md
  - concepts/tool-environment-unreliability-eval.md
  - concepts/agent-runtime-guardrails.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/prompt-injection-detector-calibration.md
  - concepts/agent-least-privilege-tool-selection.md
  - concepts/mcp-security-posture.md
  - concepts/llm-pentest-automation.md
  - concepts/ai-for-cybersecurity.md
  - concepts/security-tool-orchestration-determinants.md
maturity: draft
created: 2026-07-02
updated: 2026-07-02
---

**Briefs:** `briefs/2026-07-02_robust-to-confidence-aware-tool-routing-handoff.md`, `briefs/2026-07-02_prod-mcp-tool-confidence-contract-checklist.md`

## Relations

- @sources/arxiv-2606-26904-confidence-aware-tool-orchestration-robust-to.md — Robust-TO (2606.26904) primary source
- @concepts/tool-environment-unreliability-eval.md — hazard injection + recovery under P_h

## Raw Concept

Ingest 2026-07-02: arXiv 2606.26904 names the **Blind Trust Problem** — agents (here Video-LLMs) consume heterogeneous tool/perception outputs without propagating **input-quality uncertainty**, so accuracy collapses under corruption while reported confidence stays high. **Robust-TO** steals to general agent stacks as confidence-aware orchestration.

## Narrative

### Blind Trust Problem (generalized)

| Symptom | Video-LLM instance (2606.26904) | MCP agent analogue |
|---------|--------------------------------|---------------------|
| Input degradation | Motion blur, glare, occlusion | Stale schema, partial JSON, rate-limit noise |
| Behavior | Large accuracy drop | Wrong tool args, hallucinated fields |
| Confidence | Flat / decoupled | Model proceeds as if tool output is authoritative |
| Downstream risk | Embodied planner acts on bad perception | Tier-2 side effects on untrusted evidence |

### Robust-TO pattern (transferable)

```
Inputs → reliability×relevance filter → tool call with sub-query
       → (result, confidence) per tool → tiered synthesis (H/M/L)
       → answer + calibrated confidence
```

**Design steals for Cemini / prod MCP:**

1. **(result, confidence) contract** — every MCP tool wrapper returns structured output + reliability score (latency, schema-validity, cross-tool agreement).
2. **Disturbance-aware routing** — route to alternate tools when confidence drops (narrow retry before privilege escalate per @concepts/agent-least-privilege-tool-selection.md).
3. **Three-tier fusion** — discard contradictory MEDIUM evidence; never average conflicting tool claims into a single "HIGH" decision.
4. **Eval coupling** — pair with ToolBench-X hazard suites (@concepts/tool-environment-unreliability-eval.md) and SeClaw security trajectories (@concepts/seclaw-agent-security-evaluation.md).

### Limits [TENTATIVE]

- Source paper is **video CV** — GRPO training recipe may not transfer without domain-specific disturbance estimators.
- Confidence scores can be **gamed** without frozen estimators or independent validators (@concepts/prompt-injection-detector-calibration.md).
- Not a substitute for MCP admission, DCI, or SPI gates (@concepts/mcp-security-posture.md).

## Snippets

> "A downstream planner has no signal that the perception it depends on has quietly become unreliable."
[Source: https://rova-v2.github.io/ (retrieved 2026-07-02) — motivating embodied case; generalized here to MCP planners]
