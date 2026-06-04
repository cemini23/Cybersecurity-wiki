---
title: SeClaw — trajectory-aware agent security evaluation
type: concept
tags: [concept, agent-security, evaluation, benchmark, trajectory, k98]
keywords: [seclaw, 2606.02302, trajectory-aware, docker-testbed, spec-driven tasks, tool-using agents]
related:
  - concepts/agent-runtime-guardrails.md
  - concepts/llm-pentest-automation.md
  - concepts/llm-adversarial-fuzzing.md
  - entities/tools/seclaw-eval.md
  - entities/tools/defenseclaw.md
  - entities/tools/nvidia-skillspector.md
  - sources/arxiv-2606-02302-seclaw-spec-driven-agent-security.md
  - "@osint-wiki/concepts/seclaw-agent-security-evaluation.md"
  - "@ccc-wiki/concepts/seclaw-agent-security-evaluation.md"
  - "@ccc-wiki/briefs/2026-06-04_cybersecurity-handoff-defenseclaw-seclaw.md"
maturity: draft
created: 2026-06-04
updated: 2026-06-04
---

# SeClaw — trajectory-aware agent security evaluation

## Relations

- @concepts/agent-runtime-guardrails.md — trajectory eval hygiene + guard stack under test
- @concepts/llm-pentest-automation.md — pre-release regression for Tier-2 MCP copilots
- @concepts/llm-adversarial-fuzzing.md — refusal fuzzing orthogonal to stateful tool trajectories
- @entities/tools/seclaw-eval.md — benchmark repo entity (Reference until LICENSE + code ship)
- @entities/tools/defenseclaw.md — runtime scanner/sidecar gate (complementary, not substitute)
- @entities/tools/nvidia-skillspector.md — skill preflight before agent enters testbed
- @sources/arxiv-2606-02302-seclaw-spec-driven-agent-security.md — paper provenance
- @osint-wiki/concepts/seclaw-agent-security-evaluation.md — OSINT synthesis (Cemini boundary)
- @ccc-wiki/concepts/seclaw-agent-security-evaluation.md — CCC harness pointer (methodology only)

## Raw Concept

Canonical cybersec-wiki concept from K98 + `@ccc-wiki/briefs/2026-06-04_cybersecurity-handoff-defenseclaw-seclaw.md`. arXiv:2606.02302 — **spec-driven security task synthesis** + Docker testbed scoring **unsafe tool trajectories**, not final-answer politeness alone.

## Narrative

| Design choice | Pentest / blue-team implication |
|---------------|----------------------------------|
| **Risk specs → tasks** | Scalable coverage vs static jailbreak lists |
| **Trajectory scoring** | Unsafe intermediate tool steps can hide behind polite summaries |
| **Docker testbed** | Laptop regression harness — not a prod runtime dependency |

### vs defenseclaw

| Tool | Role | Tier (2026-06-04) |
|------|------|-------------------|
| **SeClaw** | Benchmark — measure/diagnose agent security failures | Reference (NO LICENSE + README-only repo) |
| **defenseclaw** | Runtime gate — MCP/skill scanners + optional sidecar | CONDITIONAL-GO (CLI scanners adopted on laptop) |

Use SkillSpector/defenseclaw **before** expanding MCP surface; use SeClaw **after** code ships to regression-test trajectory safety.

### Adoption posture

| Check | Status |
|-------|--------|
| Repo | `github.com/seclaw-eval/seclaw-eval` |
| License | **None** on GitHub API; root `LICENSE` 404 `[CONFIRMED 2026-06-04]` |
| Code | README states code coming soon; 0★ at Phase-0 |
| Verdict | **NO-GO (install)** — **REFERENCE (methodology)** until LICENSE + runnable benchmark |

Re-run Phase-0 when repo ships LICENSE + SeClaw-Bench code. Until then: `@entities/tools/defenseclaw.md` scanner patterns + `@entities/tools/llm-defense-lattice.md` for OWASP HTTP BAS.

## Snippets

> "trajectory-aware assessment of unsafe actions beyond final responses"

[Source: arXiv:2606.02302, retrieved 2026-06-04]

## Dead Ends

- **Final-response pass/fail** on tool-using agents — insufficient for MCP/shell side effects.
- **Conflating with EMS/trading RBAC** — agent tool misuse ≠ trading bypass (OSINT `@concepts/ems-execution-security-gaps.md` scope).
