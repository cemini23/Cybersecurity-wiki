---
title: Multilingual long-horizon agent evaluation
type: concept
tags: [concept, benchmark, multilingual, long-horizon, agent-evaluation, harness]
keywords: [polyworkbench, multilingual compounding, hybrid eval, structural executable semantic, 2607.06008]
related:
  - sources/arxiv-2607-06008-polyworkbench-multilingual-long-horizon.md
  - entities/platforms/polyworkbench.md
  - concepts/security-tool-orchestration-determinants.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-for-cybersecurity.md
  - "@ccc-wiki/concepts/multilingual-long-horizon-agent-eval.md"
maturity: draft
created: 2026-07-10
updated: 2026-07-31
wire_status: wont_wire
wire_target: "REFERENCE eval — PolyWorkbench methodology"
---

**Briefs:** `briefs/2026-07-10_polyworkbench-multilingual-eval-handoff.md`

## Relations

- @sources/arxiv-2607-06008-polyworkbench-multilingual-long-horizon.md — PolyWorkBench (2607.06008)
- @concepts/security-tool-orchestration-determinants.md — client harness is first-order for long-horizon scores
- @entities/platforms/polyworkbench.md — benchmark entity

## Raw Concept

Ingest 2026-07-10: arXiv **2607.06008** — multilingual long-horizon eval discipline. Core question: do agents survive **language switches across many tool-use steps** without compounding error?

## Narrative

### Multilingual compounding degradation

Monolingual benchmark success **does not predict** multilingual long-horizon success. Each language boundary and each step can amplify prior errors — analogous to recoverable tool-reliability compounding (@concepts/security-tool-orchestration-determinants.md) on the **locale/context** axis.

### Hybrid eval rubric (steal for agent regression design)

| Layer | What it checks | Cybersec harness analogue |
|-------|----------------|---------------------------|
| **Structural** | Files, artifacts, schema | `wiki_lint.py`, report templates |
| **Executable** | Tests/commands pass | Lab repro steps, PoC scripts |
| **LLM semantic** | Rubric on intent/quality | Engagement narrative review — **not sole gate** |

PolyWorkBench shows LLM Judge is **bimodal** and weakly correlated with task completion (r=0.18 overall) — use as **supplement** for semantic failure modes deterministic checks miss, not primary score.

### Client / harness disclosure

PolyWorkBench evaluates **ClaudeCode, OpenClaw, Hermes, Codex** on identical tasks. Same model can swing **0.08–0.21** Pass@1 by harness alone. Any published agent benchmark number without harness label is **not comparable** [CONFIRMED 2607.06008].

### Applicability

| Audience | Adoption |
|----------|----------|
| **CCC / prod-mcp** | Hybrid rubric for harness A/B; always log (model, client, tool-regime) |
| **Pentest engagements** | Reference when scoping multilingual SOAR / global SOC agents |
| **David / TipDrop** | Defer unless multilingual Discord/content pipelines become primary |

| Verdict | **REFERENCE** — methodology steal; no benchmark install at Phase-0 |

## Snippets

> "Judge is therefore not a suitable ranking metric on its own, but it is the only component sensitive to the semantic degradations that pass every deterministic check."
> — [Source: arxiv-2607.06008 §4 eval consistency, retrieved 2026-07-10]
