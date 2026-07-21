---
title: LLMs and agentic AI for smart grids — solver-grounded tutorial (arXiv 2607.18147)
type: source
tags: [source, arxiv, ot, smart-grid, agentic, solver-grounded]
keywords: [2607.18147, smart grid agents, CVXPY, GridDebugAgent, solver-grounded]
related:
  - concepts/solver-grounded-agentic-ot.md
  - concepts/network-security.md
  - concepts/6g-cps-closed-loop-security.md
  - concepts/industrial-safety-security-convergence.md
  - concepts/ai-for-cybersecurity.md
  - entities/tools/llms-agents-smartgrids-code.md
maturity: draft
read_status: read
created: 2026-07-21
updated: 2026-07-21
phase_0_verdict: "REFERENCE 2026-07-21 — github.com/d2rojas/LLMs-Agents-For-SmartGrids-Code ~15MB, NO LICENSE file/API; steal solver-grounded pattern only"
---

**Briefs:** `briefs/2026-07-21_k199-solver-grounded-smart-grid-agents-prod.md`

## Relations

- @concepts/solver-grounded-agentic-ot.md
- @entities/tools/llms-agents-smartgrids-code.md
- @concepts/network-security.md
- @concepts/6g-cps-closed-loop-security.md
- @concepts/industrial-safety-security-convergence.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | LLMs and Agentic AI Systems for Smart Grids: A Tutorial on Architectures and Applications |
| Authors | Daniela Rojas et al. (UCSD; U Alberta) |
| arXiv | 2607.18147 |
| Code | [github.com/d2rojas/LLMs-Agents-For-SmartGrids-Code](https://github.com/d2rojas/LLMs-Agents-For-SmartGrids-Code) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.18147-llms-and-agentic-ai-systems-for-smart-grids-a-tu.pdf` |
| Retrieved | 2026-07-21 |

## Narrative

**Solver-grounded design:** report a numerical result only when it originates from a trusted tool and passes verification. Case studies (wind forecast, EV charging, power flow, contingency diagnosis): EV Agent matches CVXPY optimum and cuts unmet energy 7.5–9.5× vs LLM-only; GridDebugAgent repairs 17/39 contingencies and cuts violations 52.3%. Four-group eval: task utility, solver-grounded correctness, faithfulness/safe failure, cost/latency.

### Steal for OT / agentic control

1. Never let LLM invent setpoints — wrap solvers
2. Explicit verification gate before acting on physical systems
3. Eval must include safe-failure + faithfulness, not only task score

### Phase-0

| Gate | Status |
|------|--------|
| License | **FAIL** — GitHub API null; no LICENSE file |
| Size | ~15MB |
| Verdict | **REFERENCE** — no local clone |

## Snippets

> "a numerical result is reported only when it originates from a trusted tool and passes explicit verification."
[Source: arxiv-2607.18147 abstract]
