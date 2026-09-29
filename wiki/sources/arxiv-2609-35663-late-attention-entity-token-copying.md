---
title: "Late attention layers alone can copy entity tokens, but not without attending to their context"
type: source
tags: [source, arxiv, agent-security]
keywords: [2609.35663, k380]
related:
  - concepts/late-attention-entity-token-copying-interpretability.md
maturity: draft
read_status: read
created: 2026-09-29
updated: 2026-09-29
phase_0_verdict: "REFERENCE 2026-09-29 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K380)"
---

## Relations

- @concepts/late-attention-entity-token-copying-interpretability.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Late attention layers alone can copy entity tokens, but not without attending to their context |
| arXiv | 2609.35663 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.35663-late-attention-layers-alone-can-copy-entity-toke.pdf |
| Retrieved | 2026-09-29 |
| Read status | read (abstract + triage) |

## Narrative

**K380** — LLMs perform **entity copying** (copy entity tokens from the prompt into the answer). On Qwen3-8B, **late layers in the second half** of the model are necessary and sufficient for that copy; **context-token attention to the entity tokens** is also required for exact copy, even when those context tokens do not store the entity themselves. Audit steal: interpretability and provenance work should not treat entity copy as a late-layer-only trick without context attention. **Audit only — no precheck script.** **No attack payloads in wiki.**

## Snippets

> See arXiv 2609.35663 abstract. [Source: arXiv 2609.35663 (retrieved 2026-09-29)]
