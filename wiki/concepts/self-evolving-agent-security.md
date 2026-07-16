---
title: Self-evolving agent security
type: concept
tags: [agent-security, self-evolution, mlas, containment, openclaw]
keywords: [2606.23075, mlas, self-evolving agents, attack persistence, optimizer optimizee collapse, capability ratchet]
related:
  - concepts/ai-for-cybersecurity.md
  - sources/arxiv-2606-23075-self-evolving-llm-agent-safety-mlas.md
  - concepts/agentic-containment-principles.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-security-posture.md
  - concepts/agent-skill-injection.md
  - concepts/safeclawbench-staged-agent-security.md
  - sources/arxiv-2606-01494-clawhub-security-signals.md
  - sources/openreview-openclaw-real-world-safety-analysis.md
  - entities/tools/defenseclaw.md
  - entities/tools/nvidia-skillspector.md
  - sources/arxiv-2607-13987-agent-skill-security-skillsec-eval.md
  - concepts/skillsec-lifecycle-agent-skill-security.md
maturity: draft
created: 2026-06-23
updated: 2026-07-16
---

## Relations

- @sources/arxiv-2606-23075-self-evolving-llm-agent-safety-mlas.md — MLAS matrix + case studies
- @concepts/agentic-containment-principles.md — P1–P6 static framework audit (insufficient alone)

## Narrative

Ingest 2026-06-23: arXiv:2606.23075 — **self-evolution** (autonomous updates to weights, memory, tools, architecture) removes the **session reset** safety anchor.

### Static vs self-evolving (Table 1 summary)

| Dimension | Static agent | Self-evolving agent |
|-----------|--------------|-------------------|
| Attack persistence | Session-scoped | Cross-cycle; embedded in weights/memory/tools |
| Defense anchors | Fixed weights + tool set | **No immutable anchor** |
| Amplification | Linear | Compounding feedback loops |
| Multi-agent | Independent compromise | Contagion via shared evolution |

### MLAS audit shortcut

Map your deployment to **5 modules × 5 lifecycle stages**. If **Self-Design** or **Commit** stages are agent-controlled, treat optimizer–optimizee collapse as **critical**.

### Scanner gap

Pre-install skill/MCP scanners (SkillSpector, DefenseClaw, Skillgate) do **not** cover evolution pathways — OpenClaw case: **2.5%** block rate on evolution-path attacks vs **100%** persistence in Hermes eval.

### Operator stance

- **Default deny** self-modifying agents on prod-mcp until MLAS cells documented
- Immutable external verifier not modifiable by the agent under evolution
- Pair with @concepts/safeclawbench-staged-agent-security.md endpoint ladder (semantic vs sandbox harm)

See `briefs/2026-06-23_self-evolving-agent-assessment-checklist.md`.
