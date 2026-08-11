---
title: "SHE — Safety Harness Evolution (trajectory-driven harness learning)"
type: entity
tags: [tool, agent-security, harness-evolution, adopted, guardrail]
keywords: [SHE, safety harness, harness evolution, Apache-2.0, Agent-SafetyBench, Rule Bank, Safety Memory, 2608.09885]
related:
  - sources/arxiv-2608-09885-she-safety-harness-evolution.md
  - concepts/safety-harness-evolution.md
  - concepts/agent-runtime-guardrails.md
  - concepts/harnessopt-bench.md
  - concepts/self-evolving-agent-security.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-08-11
updated: 2026-08-11
phase_0_verdict: "GO 2026-08-11 — Apache-2.0; shallow clone ~4.7MB; lab adopt for harness-evolution pattern. K268 policy wire."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc + cemin-cybersec-lab-redteam.mdc (K268)"
---

## Relations

- @sources/arxiv-2608-09885-she-safety-harness-evolution.md
- @concepts/safety-harness-evolution.md
- @concepts/agent-runtime-guardrails.md
- @concepts/harnessopt-bench.md
- @concepts/self-evolving-agent-security.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

Shanghai AI Lab / AgentDoG Team harness-evolution framework (2608.09885). Evolves four safety artifacts (System Prompt, Rule Bank, Safety Memory, Tool Policy) from rollout trajectories under a safety–utility selection loop. Not an attack tool; a defensive harness-learning method.

## Narrative

Use locally as the **reference pattern** for making a harness evolve from trajectory failures: four-artifact decomposition for attribution, validity-checked bounded edits, and safety–utility selection. The clone is a lab shelf for reading the artifact schemas (Rule Bank records, Safety Memory contrastive boundaries, Tool Policy detectors) and reusing them when hardening Cemini-class agent harnesses. It is **not** a runtime MCP and is not wired to any production agent loop.

## Local adoption

| Field | Value |
|-------|-------|
| Verdict | GO (Apache-2.0, shallow clone) |
| Path | `raw-sources/repos/SHE` |
| LICENSE | Apache-2.0 (`LICENSE`) |
| SHA | `0c656460d9d8acdf406a2271d657f7a7b60bb255` |
| Size | ~4.7MB |
| Runtime wire | none — policy wire K268; harness-evolution pattern only |
