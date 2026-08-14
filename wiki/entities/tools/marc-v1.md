---
title: "MARC v1 — Multi-Agent Reasoning and Coordination (clinical AI framework)"
type: entity
tags: [tool, multi-agent, orchestration, clinical-ai, llm, local-adopt, k279]
keywords: [MARC, Penn-RAIL, multi-agent orchestration, Decomposer, LangChain, Ollama, Gemini, stage-wise failure attribution, YAML agents, local CPU]
related:
  - sources/arxiv-2608-13476-marc-v1-clinical-multi-agent.md
  - concepts/deterministic-multi-agent-orchestration-failure-attribution.md
  - concepts/role-specialization-multi-tool-coordination.md
  - concepts/agent-runtime-guardrails.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14
phase_0_verdict: "GO 2026-08-14 — MIT, ~31MB (20MB shallow clone in raw-sources/repos/MARC-v1). Clinical runtime wont_wire; deterministic orchestration pattern adopted as harness reference."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-mcp-tool-control.mdc (K279)"
local_adoption: "cloned 2026-08-14 raw-sources/repos/MARC-v1 (shallow, 20MB); pip-installable Python package `marc`; not wired into adopted_security_preflight (reference, not runtime)"
---

## Relations

- @sources/arxiv-2608-13476-marc-v1-clinical-multi-agent.md — source paper + repo
- @concepts/deterministic-multi-agent-orchestration-failure-attribution.md — the orchestration steal
- @concepts/role-specialization-multi-tool-coordination.md — RSM (K277); MARC is the deterministic implementation of role coordination
- @concepts/agent-runtime-guardrails.md — stage-wise attribution as a runtime guardrail

## Raw Concept

MARC v1 is an open-source (MIT) Python framework for **deterministic multi-agent clinical reasoning** built on LangChain. YAML-declared role-specialized agents execute in a fixed sequence with explicit context passing; a **Decomposer** generates task-specific agent prompts from plain-language descriptions. Backends: Google Gemini API or local Ollama (CPU-compatible). 2 stars; academic release from Penn RAIL.

## Narrative

**Local adoption: GO (clone only, reference).** Cloned shallow 2026-08-14 (`raw-sources/repos/MARC-v1`, 20MB). MIT license confirmed. The value is the **orchestration pattern**, not the clinical domain:

- Deterministic sequential pipeline (Level-2 autonomy) with explicit handoffs — makes each stage inspectable
- **Stage-wise failure attribution** — errors localize to a specific agent/stage instead of a monolithic call
- **Decomposer** — LLM-generated task decomposition → structured 3-agent pipeline spec → validated → written to disk; eliminates manual prompt engineering
- Local CPU-compatible via Ollama (no GPU required for the framework itself)

**wont_wire for clinical runtime** — no patient data, no clinical workflow in Cemini scope. The pattern transfers to any multi-agent harness where auditability matters.

**Not wired into preflight** — reference clone, not a runtime tool. Do not install `marc` as a service; use as source for orchestration patterns.

## Dead Ends

- 2 stars / brand-new repo — expect rough edges; README is the doc of record. [TENTATIVE]

## Snippets

> Agents, models, prompts, and optional retrieval sources are defined in YAML. Adding, removing, or reordering agents requires no code changes. [Source: README]
