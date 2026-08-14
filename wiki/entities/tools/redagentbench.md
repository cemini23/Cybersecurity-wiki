---
title: "REDAgentBench — executable agent red-teaming benchmark"
type: entity
tags: [tool, agent-security, red-team, benchmark, faithful-measurement, reference]
keywords: [REDAgentBench, executable red teaming, ASR, IVC taxonomy, service sandbox, trajectory-state-hybrid judge, Recognition-Execution Gap]
related:
  - sources/arxiv-2608-10669-redagentbench-faithful-agent-asr.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/agent-runtime-guardrails.md
  - sources/arxiv-2608-12996-atobench-deceptive-observations.md
  - concepts/atobench-verification-chain-deception.md
  - entities/tools/atobench.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — benchmark not yet released (no public repo). Pattern adopt for faithful ASR measurement only."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc + cemin-cybersec-agent-audit.mdc (K271)"
---

## Relations

- @sources/arxiv-2608-10669-redagentbench-faithful-agent-asr.md
- @concepts/faithful-agent-asr-measurement.md
- @concepts/agent-runtime-guardrails.md

## Raw Concept

Qwen DianJin Team / Alibaba Cloud + Fudan / HKUST benchmark (2608.10669): 1,661 executable agent red-team cases across 5 service surfaces, verified from service receipts and final-state diffs, with an exposure→execution→observation→adjudication ASR decomposition and a Trajectory–State–Hybrid judge system.

## Narrative

Use as the **reference pattern** for measuring agent-safety ASR faithfully: derive attacks from explicit constraints + vulnerabilities (IVC taxonomy), sandbox each case, verify harm from durable state, and report ASR as a tuple `(harness, judging configuration, evaluation cue, judge backbone)`. The Recognition–Execution Gap metric and the training-free action-time policy reminder are the two most stealable ideas for hardening Cemini-class agent harnesses.

**Local adoption: NO** — REFERENCE only until the benchmark and harnesses ship publicly. Not wired as a runtime MCP.

## Dead Ends

- No public repo at Phase-0 (2026-08-12); re-check for a GitHub/HF release before any lab run.
- Full-matrix repro needs paid model APIs (GPT-5.2, Qwen3.x-plus, KIMI-2.6, GLM-5.2) + 3 harnesses; expensive, defer.
