---
title: "SeClaw — spec-driven security task synthesis for evaluating autonomous agents (arXiv:2606.02302)"
type: source
tags: [arxiv, agent-security, evaluation, benchmark, trajectory, docker-testbed, research-paper, k98]
keywords: [seclaw, 2606.02302, trajectory-aware, risk-spec, openclaw, tool-using agents, docker testbed]
related:
  - concepts/agent-runtime-guardrails.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/llm-pentest-automation.md
  - entities/tools/seclaw-eval.md
  - entities/tools/airguard.md
  - entities/tools/nvidia-skillspector.md
  - sources/arxiv-2605-30454-agent-prompt-injection-surface-evaluation.md
  - sources/arxiv-2606-02240-agentredbench.md
  - sources/arxiv-2606-02822-owasp-llm-defense-attribution.md
  - "@osint-wiki/sources/arxiv-seclaw-spec-driven-agent-security-2606-02302-2026-06-04.md"
  - "@osint-wiki/concepts/seclaw-agent-security-evaluation.md"
maturity: draft
read_status: read
created: 2026-06-04
updated: 2026-06-04
---

## Relations

- @concepts/agent-runtime-guardrails.md — trajectory-aware eval complements guardrail stack
- @concepts/llm-adversarial-fuzzing.md — jailbreak fuzzing vs stateful tool-trajectory security tasks
- @concepts/llm-pentest-automation.md — pre-release regression harness for Tier-2 MCP agents
- @entities/tools/seclaw-eval.md — benchmark repo (`seclaw-eval/seclaw-eval`)
- @entities/tools/airguard.md — runtime guard to score under SeClaw-style tasks
- @entities/tools/nvidia-skillspector.md — skill preflight before agent enters testbed
- @sources/arxiv-2605-30454-agent-prompt-injection-surface-evaluation.md — per-surface ASR vs trajectory scoring
- @sources/arxiv-2606-02240-agentredbench.md — SaaS integration redteam benchmark (complementary)
- @osint-wiki/sources/arxiv-seclaw-spec-driven-agent-security-2606-02302-2026-06-04.md — OSINT K98 ingest anchor
- @osint-wiki/concepts/seclaw-agent-security-evaluation.md — OSINT synthesis

## Raw Concept

- **Title**: SeClaw: Spec-Driven Security Task Synthesis for Evaluating Autonomous Agents
- **Authors**: Hao Cheng et al. (HKUST, Ant Group, XJTU, Oxford, …)
- **Type**: arXiv preprint
- **Location**: `raw-sources/arxiv-2606.02302-seclaw-spec-driven-security-task-synthesis-for-e.pdf`
- **URL**: https://arxiv.org/abs/2606.02302
- **Code**: https://github.com/seclaw-eval/seclaw-eval
- **Retrieved**: 2026-06-04
- **Read-status**: read (abstract + framework sections; skimmed full PDF)

## Narrative

Benchmark framework for **stateful tool-using LLM agents** (files, memory, MCP, external services). Two pillars:

1. **Spec-driven task synthesis** — security tasks generated from structured risk specifications (scalable coverage vs hand-curated prompt lists).
2. **SeClaw Docker testbed** — reproducible execution environment for diverse safety-risk scenarios.

Risk taxonomy spans **resources**, **user tasks**, **environment**, and **intrinsic agent behavior**. Core eval innovation: **trajectory-aware** unsafe-action detection — unsafe tool steps count even when the final chat response looks benign. Directly addresses the gap flagged in @sources/arxiv-2605-30454-agent-prompt-injection-surface-evaluation.md (outcome-only scoring overstates defense).

Motivation cites OpenClaw-style agent stacks where tool access creates emergent attack surface beyond static injection lists.

**Wiki tier**: Reference benchmark harness — not a runtime guard. Pair with SkillSpector preflight + AIRGuard/ChainCaps-class enforcement when running authorized lab regressions.

## Snippets

> "Current agent security benchmarks often rely on manually curated tasks, provide limited coverage of emerging threats, and focus primarily on final outcomes rather than the execution processes that lead to unsafe behavior."

> "supports trajectory-aware assessment of unsafe actions beyond final responses"

[Source: arXiv:2606.02302 abstract, retrieved 2026-06-04]
