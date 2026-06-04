---
title: "SeClaw — spec-driven agent security benchmark harness (Reference)"
type: entity
tags: [tool, ai-security, benchmark, evaluation, docker, trajectory, reference, k98]
keywords: [seclaw, seclaw-eval, trajectory-aware, docker-testbed, risk-spec, agent benchmark]
related:
  - concepts/agent-runtime-guardrails.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/llm-pentest-automation.md
  - entities/tools/airguard.md
  - entities/tools/nvidia-skillspector.md
  - entities/tools/agentredguard.md
  - entities/tools/defenseclaw.md
  - entities/tools/llm-defense-lattice.md
  - sources/arxiv-2606-02822-owasp-llm-defense-attribution.md
  - sources/arxiv-2606-02302-seclaw-spec-driven-agent-security.md
  - "@osint-wiki/concepts/seclaw-agent-security-evaluation.md"
  - "@osint-wiki/sources/arxiv-seclaw-spec-driven-agent-security-2606-02302-2026-06-04.md"
maturity: draft
created: 2026-06-04
updated: 2026-06-04
phase_0_verdict: "Reference 2026-06-04 — benchmark only; repo has no LICENSE file on GitHub API [NEEDS VERIFICATION 2026-06-04]; run laptop Docker eval after license audit before any code import."
---

# SeClaw — spec-driven agent security benchmark harness

## Relations

- @concepts/seclaw-agent-security-evaluation.md — canonical eval methodology (this entity = repo stub)
- @concepts/agent-runtime-guardrails.md — trajectory eval hygiene + guard stack under test
- @entities/tools/defenseclaw.md — runtime scanner gate vs benchmark
- @concepts/llm-adversarial-fuzzing.md — refusal/jailbreak fuzzing is orthogonal to stateful tool trajectories
- @concepts/llm-pentest-automation.md — pre-release regression for Tier-2 MCP copilots
- @entities/tools/airguard.md — runtime guard candidate to measure under SeClaw tasks
- @entities/tools/nvidia-skillspector.md — skill preflight before agent enters testbed
- @entities/tools/agentredguard.md — SaaS integration benchmark (AgentRedBench) vs general tool trajectory (SeClaw)
- @sources/arxiv-2606-02302-seclaw-spec-driven-agent-security.md — paper provenance
- @osint-wiki/concepts/seclaw-agent-security-evaluation.md — OSINT K98 synthesis
- @osint-wiki/sources/arxiv-seclaw-spec-driven-agent-security-2606-02302-2026-06-04.md — OSINT source anchor

## Raw Concept

Routed from K98 brief (`briefs/2026-06-04_k98-seclaw-agent-eval-from-osint.md`, 2026-06-04). GitHub: `seclaw-eval/seclaw-eval` (~0 stars at Phase-0 check; pushed 2026-06-02). arXiv:2606.02302.

## Narrative

**Reference-tier** Docker benchmark for measuring security failures in autonomous LLM agents. Generates tasks from structured risk specs; scores **execution trajectories**, not final answers alone.

**Use cases (authorized lab only)**:
- Regression before expanding MCP tool surface on pentest/SOC copilot stacks
- Compare guard stacks (prompt-only vs AIRGuard-class vs composition proxy)
- Complement @entities/tools/agentredguard.md (SaaS integration channel) and static jailbreak fuzzers

**Phase-0 blockers**:
- **No LICENSE** exposed via GitHub API at 2026-06-04 — defer code import until LICENSE file lands or maintainer confirms terms `[NEEDS VERIFICATION 2026-06-04]`
- Docker + LLM API cost for full benchmark sweeps — laptop subset only initially

**Not** a production runtime dependency — evaluation harness only.

## Snippets

```bash
# Phase-0 license check (2026-06-04 — returned null SPDX)
gh api repos/seclaw-eval/seclaw-eval --jq '.license.spdx_id'
```

Paper code URL: https://github.com/seclaw-eval/seclaw-eval

## Dead Ends

- **Final-response-only pass/fail** on tool-using agents — SeClaw exists because unsafe intermediate tool steps can be hidden behind polite summaries.
- **Manually curated task lists alone** — poor coverage scaling for emergent MCP/skill threats; spec-driven synthesis is the paper's scaling bet `[TENTATIVE]` until reproduced locally.
