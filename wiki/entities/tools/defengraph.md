---
title: DEFENGRAPH — knowledge graph LLM blue-team assistant
type: entity
tags: [tool, blue-team, soc, knowledge-graph, rag, reference]
keywords: [defengraph, 2606.21059, knowledge graph, siem, alert triage]
related:
  - sources/arxiv-2606-21059-defengraph-knowledge-graph-blue-team.md
  - concepts/incident-response.md
  - concepts/soc-operations.md
  - concepts/siem.md
  - concepts/threat-hunting.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-06-23
updated: 2026-07-31
phase_0_verdict: "Reference 2026-06-23 — IEEE TIFS paper; no public implementation repo found; adopt pattern (static+dynamic KG RAG) not product"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

## Relations

- @sources/arxiv-2606-21059-defengraph-knowledge-graph-blue-team.md — eval provenance
- @concepts/siem.md — alert ingestion layer KG would sit above

## Narrative

Research framework (CSIRO/Data61) for **KG-grounded LLM** defender assistants during incidents. Dual-layer **static + dynamic** knowledge graph over SIEM alerts, topology, TTPs, and prior defensive actions.

**Phase-0: Reference** — no GitHub release located 2026-06-23. Useful as **architecture pattern** for SOC copilot RAG (graph path retrieval + re-rank) before adopting commercial SIEM LLM plugins.

Headline GPT-4o ticket-action recall **52% → 72%** on cyber-range data; precision **~29%** — human analyst remains decision authority.
