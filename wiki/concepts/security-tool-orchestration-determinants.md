---
title: Security-tool orchestration determinants — client, tools, and reasoning limits
type: concept
tags: [concept, llm-agents, pentest, tool-orchestration, mcp, evaluation, hexstrike]
keywords: [driving client, tool-access regime, reasoning-bound failure, orchestrator eval, hexstrike, 2607.02873, client naming]
related:
  - sources/arxiv-2607-02873-hexstrike-security-tool-orchestration.md
  - concepts/agentic-offensive-security-kill-chain.md
  - concepts/agent-least-privilege-tool-selection.md
  - concepts/mcp-execution-control-invariants.md
  - concepts/mcp-security-posture.md
  - concepts/tool-environment-unreliability-eval.md
  - concepts/confidence-aware-tool-orchestration.md
  - "@ccc-wiki/concepts/client-as-first-order-harness-factor.md"
maturity: draft
created: 2026-07-07
updated: 2026-07-07
---

**Briefs:** `briefs/2026-07-07_hexstrike-client-first-order-orchestration-checklist.md`

## Relations

- @sources/arxiv-2607-02873-hexstrike-security-tool-orchestration.md — HexStrike-AI 774-trial study (2607.02873)
- @concepts/agentic-offensive-security-kill-chain.md — orchestrators automate recon→exploit steps
- @concepts/mcp-execution-control-invariants.md — the authority layer beneath tool exposure

## Raw Concept

Ingest 2026-07-07: arXiv 2607.02873 empirically decomposes what bounds an LLM security-tool orchestrator (HexStrike-AI, 150+ tools over MCP) across 774 picoCTF trials.

## Narrative

### Three determinants

| Determinant | Result |
|-------------|--------|
| **Driving client** (harness) | **First-order** — 2.1× gap between two clients running the *same* model |
| **Tool-access regime** | Constraining to orchestrator-owned tools vs full access matters, but less than client |
| **Reasoning** | Residual failures are **reasoning-/environment-bound**, not missing-tool |

### Client-naming discipline

Orchestrator evals must **name the client/harness**, not just the model. An unnamed harness turns a model benchmark into a harness benchmark. Report `(model, client, tool-regime)` triples.

### Defensive read

- More tools ≠ more capability past a point — residual failures are reasoning-bound. Aligns with **least-privilege tool selection** (@concepts/agent-least-privilege-tool-selection.md): expose fewer, sharper tools.
- Solve-rate lift (55.4%→72.0%) came from **tool corrections + agent-behavior changes**, i.e. harness engineering, not model swap.

### Limits

Single benchmark; fixes tuned on eval set; client effect shown for one model — treat client-effect magnitude as `[TENTATIVE]`.

| Verdict | **REFERENCE** — eval methodology + least-privilege corroboration; lab-only if HexStrike-AI trialed |

## Snippets

> "The residual failures are reasoning- or environment-bound rather than missing-tool."
> — [Source: arxiv-2607.02873 abstract, retrieved 2026-07-07]
