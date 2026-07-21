---
title: Solver-grounded agentic OT / smart-grid agents
type: concept
tags: [ot, smart-grid, agentic, verification]
keywords: [solver-grounded, CVXPY, trusted tool, physical setpoints]
related:
  - sources/arxiv-2607-18147-llms-agents-smart-grids-tutorial.md
  - entities/tools/llms-agents-smartgrids-code.md
  - concepts/network-security.md
  - concepts/6g-cps-closed-loop-security.md
  - concepts/industrial-safety-security-convergence.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-07-21
updated: 2026-07-21
---

## Relations

- @sources/arxiv-2607-18147-llms-agents-smart-grids-tutorial.md
- @entities/tools/llms-agents-smartgrids-code.md
- @concepts/network-security.md
- @concepts/6g-cps-closed-loop-security.md
- @concepts/industrial-safety-security-convergence.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

LLM agents in power systems must **orchestrate**, not invent physics. Solver-grounded design: numerical claims come only from trusted tools + verification gates.

## Narrative

### Division of labor

| Agent | Trusted tool |
|-------|----------------|
| Plan / retrieve / explain | LLM |
| Optimize / power-flow / schedule | Solver (CVXPY etc.) |
| Act | Only after verification |

### Evidence (UCSD tutorial)

EV Agent reproduces CVXPY optimum; unmet energy ↓ 7.5–9.5× vs LLM-only. GridDebugAgent: 17/39 contingencies repaired; violations ↓ 52.3%. Eval needs faithfulness + safe failure, not only task utility.
