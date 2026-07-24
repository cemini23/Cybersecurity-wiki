---
title: Experiential abstraction memory for LLM agents
type: concept
tags: [concept, llm-memory, abstractions, agent-ops]
keywords: [Notes-to-self, experiential abstractions, score-gated retrieval, 2607.20372]
related:
  - sources/arxiv-2607-20372-notes-to-self-experiential.md
  - entities/tools/notes-to-self.md
  - concepts/coding-agent-context-pruning.md
  - concepts/ai-for-cybersecurity.md
  - concepts/pats-policy-aware-agent-rl-scaffold.md
  - sources/arxiv-2607-21419-pats-agentic-rl.md
maturity: draft
created: 2026-07-23
updated: 2026-07-24
---

## Relations

- @sources/arxiv-2607-21419-pats-agentic-rl.md
- @concepts/pats-policy-aware-agent-rl-scaffold.md
- @sources/arxiv-2607-20372-notes-to-self-experiential.md
- @entities/tools/notes-to-self.md
- @concepts/coding-agent-context-pruning.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

Distill solution traces into short natural-language **abstractions** (strategies + cautions); retrieve or RL-train with them.

## Narrative

Two modes: inference-time retrieval; RL with abstraction-augmented prompts. Self-extract ≈ teacher. Cyber steal: keep a library of engagement/lab **cautions**, score-gate into context instead of dumping full histories (pairs with context pruning).

Local: `raw-sources/repos/Notes-to-self` (~16MB, Apache via verl).
