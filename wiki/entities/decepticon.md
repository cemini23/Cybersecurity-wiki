---
title: Decepticon — Autonomous Red-Team Multi-Agent Framework
type: entity
tags: [tool, red-team, multi-agent, langgraph, autonomous-pentest, apache-2, offensive-security]
keywords: [decepticon, langgraph agents, kill-chain agents, litellm fallback, postgresql neo4j, steal-from]
related:
  - concepts/red-team-operations.md
  - concepts/llm-pentest-automation.md
  - "@osint-wiki/entities/tools/decepticon.md"
maturity: draft
created: 2026-05-14
updated: 2026-05-15
cross-wiki-source: @osint-wiki/entities/tools/decepticon.md
---

# Decepticon — Autonomous Red-Team Multi-Agent Framework

## Relations

- @concepts/red-team-operations.md — primary use case; 16 specialist agents organized by kill-chain phase
- @concepts/llm-pentest-automation.md — methodology umbrella; LangGraph subagent topology + LiteLLM fallback patterns
- @osint-wiki/entities/tools/decepticon.md  (cross-wiki source)

## Raw Concept

Cross-wiki stub routed from `@osint-wiki/entities/tools/decepticon.md` during ingest.
What prompted this page + which sources synthesize into it — fill in on next
ingest pass.

## Narrative

Autonomous red-team framework with 16 specialist LangGraph agents organized by kill chain phase, PostgreSQL + Neo4j dual persistence, and LiteLLM model fallback chains. Apache-2.0 license, 3.7k stars. Steal-from tier per K45 v3 multi-wiki tool eval — extract LangGraph subagent topology and LiteLLM fallback patterns; do NOT deploy agents (offensive ops conflate with financial state tools).
