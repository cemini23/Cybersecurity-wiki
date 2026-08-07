---
title: HarnessOpt-Bench harness optimization eval (arXiv 2608.06301)
type: source
tags: [source, arxiv, agent-harness, evaluation, scale-ai]
keywords: [2608.06301, HarnessOpt-Bench, harness optimization, agentic systems, TEE]
related:
  - concepts/harnessopt-bench.md
  - concepts/llm-pentest-automation.md
  - concepts/self-evolving-agent-security.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-08-07
updated: 2026-08-07
phase_0_verdict: "REFERENCE 2026-08-07 — Scale paper; no public HarnessOpt-Bench code found"
wire_status: wont_wire
wire_target: "eval-boundary / budgeted harness-edit pattern only"
---

**Briefs:** `briefs/2026-08-07_k252-harnessopt-prod.md`

## Relations

- @concepts/harnessopt-bench.md
- @concepts/llm-pentest-automation.md
- @concepts/self-evolving-agent-security.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | HarnessOpt-Bench: Evaluating LLMs at Harness Optimization |
| Authors | Varun Ursekar, Apaar Shanker, Yash Maurya, Shehab Yasser, Vijay S. Kalmath, Veronica Chatrath, Yuan (Emily) Xue (Scale AI) |
| arXiv | 2608.06301 |
| Code | none found (Phase-0 2026-08-07); labs.scale.com/papers/harnessopt-bench |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.06301-harnessopt-bench-evaluating-llms-at-harness-opti.pdf` |
| Retrieved | 2026-08-07 |

## Narrative

Benchmark for **automated harness optimization** (prompts/tools/control-flow/memory/orchestration) under expensive stochastic eval. Optimizer edits seed harness under fixed target-eval budget; scored on held-out normalized gain. TEE enforces eval boundary + audit versions. Finding: optimizer **model** separates more than coding harness; native harnesses not always better. [CONFIRMED abstract]

### Steal

1. Treat harness optimization as its own measurable capability (not only task ASR)
2. Keep held-out / budgeted eval boundaries — no peeking at test partition during search
3. Do not auto-optimize prod/LIVE harness without HITL + rollback (self-evolving risk)

## Snippets

> "optimizer models separate more than the coding harnesses they act through, native harnesses are not consistently superior"
[Source: arXiv 2608.06301 abstract]
