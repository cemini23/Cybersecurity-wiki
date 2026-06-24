---
title: Autonomous defense agent transferability
type: concept
tags: [concept, blue-team, soc, autonomous-defense, eval, cyber-range, arena]
keywords: [agent transferability gap, arena, telemetry schema, soc agent, 2606.21377]
related:
  - sources/arxiv-2606-21377-arena-autonomous-defense-transferability.md
  - concepts/soc-operations.md
  - concepts/threat-hunting.md
  - concepts/adversary-emulation.md
  - concepts/ai-for-cybersecurity.md
  - entities/frameworks/mitre-attack.md
  - sources/arxiv-2606-05252-bas-to-siem-detection-as-code-synthesis.md
  - sources/arxiv-2606-21059-defengraph-knowledge-graph-blue-team.md
maturity: draft
created: 2026-06-24
updated: 2026-06-24
---

## Relations

- @sources/arxiv-2606-21377-arena-autonomous-defense-transferability.md — ARENA architecture (2606.21377)
- @concepts/soc-operations.md — SOC deployment context

## Raw Concept

Ingest 2026-06-24: arXiv:2606.21377 — **agent transferability gap** for autonomous cyber-defense LLM agents.

## Narrative

### Problem

SOC copilots validated on one benchmark/range are deployed on different SIEM schemas, OS mixes, and policy engines. **Same ATT&CK technique → different observations** (ECS JSON vs Splunk CIM; Windows Event Log vs Linux auditd).

Agents with **identical detection recall** in environment A can diverge in B — failure attributed to **observation semantics**, not recognition logic.

### ARENA decomposition

| Layer | Varies independently |
|-------|---------------------|
| Attacker emulation | STIX-constrained campaigns |
| SUT generation | Platform / topology |
| Typed agent runtime | Observation/action API |
| Policy verifier | Deterministic ground truth |

**Failure taxonomy:** schema | grounding | budget | policy

### Blue-team eval hygiene

- Never trust single-environment SOC agent benchmarks
- Re-run same technique across **≥2 telemetry schemas**
- Attribute degradation to taxonomy bucket before retraining
- Pair with BAS→Sigma detection-as-code synthesis (@sources/arxiv-2606-05252-bas-to-siem-detection-as-code-synthesis.md)

See `briefs/2026-06-24_arena-soc-agent-eval-handoff.md`.

`[TENTATIVE]` — controlled two-agent experiment; broader vendor coverage unverified.

## Snippets

> "An agent that succeeds in one environment often degrades when the same attack runs on a different platform, telemetry stack, or policy."

[Source: arxiv-2606.21377]
