---
title: DEFENGRAPH — KG-enhanced LLMs for blue team defense (arXiv 2606.21059)
type: source
tags: [source, arxiv, blue-team, soc, knowledge-graph, rag, incident-response]
keywords: [2606.21059, defengraph, knowledge graph, siem, alert triage, cyber range]
related:
  - entities/tools/defengraph.md
  - concepts/incident-response.md
  - concepts/soc-operations.md
  - concepts/siem.md
  - concepts/threat-hunting.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-06-23
updated: 2026-06-23
phase_0_verdict: "Reference 2026-06-23 — IEEE TIFS submission; no public repo located on GitHub search 2026-06-23"
---

## Relations

- @entities/tools/defengraph.md — framework entity + eval numbers
- @concepts/incident-response.md — defender decision-support during incidents

## Raw Concept

| Field | Value |
|-------|-------|
| Title | DEFENGRAPH: Knowledge Graph-Enhanced LLMs for Blue Team Cyber Defense |
| Authors | Zhen Wang et al. (CSIRO/Data61 + collaborators) |
| arXiv | 2606.21059v1 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2606.21059-2606-21059v1-defengraph-knowledge-graph-enhanced.pdf` |
| Retrieved | 2026-06-23 |
| Read status | **read** (abstract, intro, eval headline metrics) |

## Narrative

**DEFENGRAPH** — LLM assistant for human defenders combining **dual-layer Static-Dynamic Knowledge Graph** with graph path retrieval, LLM contextual filtering, and reasoning-based re-ranking. Grounds outputs in long-term domain knowledge + evolving incident context.

### KG inputs

Heterogeneous security artifacts: **SIEM alerts**, system topology, attacker behaviours, prior defensive actions.

### Evaluation setting

Live **Red vs Blue cyber range** exercises simulating critical-infrastructure attacks — noisy, realistic defender workflows.

### Headline results (GPT-4o)

| Metric | Baseline → DEFENGRAPH |
|--------|----------------------|
| Reasoning-recall | 61.45% → **73.49%** |
| Ticket-action recall | 52.17% → **72.46%** |
| Ticket-action precision | 24.49% → **29.24%** |
| Correct defense actions surfaced | 36 → **50** (next-best baseline) |

Similar gains on LLaMA-3, DeepSeek-R1, Qwen-3. Fault rates held steady.

### SOC relevance

Addresses LLM **hallucination + poor temporal reasoning** in alert triage — complements rule-based SIEM (@concepts/siem.md) with KG-grounded RAG, not replacement.

`[TENTATIVE]` — precision still ~29% on ticket-action; human-in-loop mandatory.

## Snippets

> "DEFENGRAPH improves contextual reasoning by integrating a dual-layer Static-Dynamic Knowledge Graph (KG) with graph-based path retrieval, LLM-driven contextual filtering, and reasoning-based re-ranking."

[Source: arxiv-2606.21059-defengraph-knowledge-graph-blue-team.pdf]
