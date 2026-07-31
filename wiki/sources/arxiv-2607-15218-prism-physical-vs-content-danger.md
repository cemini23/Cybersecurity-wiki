---
title: PRISM — physical danger vs content danger in hidden-state risk space (arXiv 2607.15218)
type: source
tags: [source, arxiv, agent-safety, embodied, physical-danger, probing]
keywords: [2607.15218, prism, physical danger, content danger, psb-1k, safeagentbench, tsinghua]
related:
  - concepts/physical-vs-content-danger-embodied-agents.md
  - concepts/vulnerability-concept-graph-production-agent-red-teaming.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - concepts/agent-runtime-guardrails.md
  - concepts/amt-x-phase-structured-multi-turn-red-teaming.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-17
updated: 2026-07-31
phase_0_verdict: "REFERENCE 2026-07-17 — no public code found; steal CD/PD separability + probe-before-execute pattern"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

**Briefs:** `briefs/2026-07-17_prism-physical-vs-content-danger-handoff.md`, `briefs/2026-07-17_k185-prism-physical-vs-content-danger-prod.md`

## Relations

- @concepts/physical-vs-content-danger-embodied-agents.md — synthesis

## Raw Concept

| Field | Value |
|-------|-------|
| Title | When Words Are Safe But Actions Kill: Probing Physical Danger Beyond Text Safety in Hidden-State Risk Space |
| Authors | Weimeng Wang, Ziqiang Wang, Zihang Zhan, Chuanpu Fu, Qi Li, Ke Xu |
| Affiliation | Tsinghua; NTU |
| arXiv | 2607.15218 |
| Code | **none found** in paper (2026-07-17) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.15218-when-words-are-safe-but-actions-kill-probing-phy.pdf` |
| Retrieved | 2026-07-17 |
| Read status | **read** (CD/PD + PRISM + PSB-1K) |

## Narrative

LLMs as high-level planners for embodied agents face **physical danger (PD)** — linguistically benign instructions that are unsafe under physical causality (“microwave an egg”) — distinct from **content danger (CD)** (“ignite the curtain”). Hidden-state analysis shows CD and PD are separable signals.

### PRISM probe [CONFIRMED from abstract]

Single-layer L2-regularized logistic probe over full hidden states:

| Bench | PRISM | Same-scale LLM judges |
|-------|-------|------------------------|
| SafeAgentBench | **86.2–87.7%** acc, **11.7–13.7%** FPR | FPR **24.7–39.0%** (over-block) |
| PSB-1K (1k contrastive PD pairs, no harm keywords) | **99.6%** acc, **0.7%** FPR | Qwen2.5-3B rejects **67.8%** of safe tasks |

### Steal for Cemini

1. Text guardrails ≠ action/plan safety — add a **before-execute physical/causal monitor** for tool-acting agents
2. Prefer cheap representation probes over LLM-as-judge for PD (lower false positive on safe tasks)
3. Pairs Prebind (CAGE-1) and VCG enabling-conditions: PD is an enabling condition class for embodied/tool agents

### Phase-0

REFERENCE — methodology + benchmark claims; no installable artifact.

## Snippets

> "We show that content danger (CD) and physical danger (PD) form separable signals in LLM representations…"
[Source: arxiv-2607.15218 abstract]
