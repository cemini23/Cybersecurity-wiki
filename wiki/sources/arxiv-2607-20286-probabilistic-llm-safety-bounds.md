---
title: Sound probabilistic safety bounds for LLMs (arXiv 2607.20286)
type: source
tags: [source, arxiv, llm-safety, formal-methods, pac]
keywords: [2607.20286, Clopper-Pearson, PAC, harm probability, latent-space search]
related:
  - concepts/llm-probabilistic-safety-bounds.md
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-23
updated: 2026-07-31
phase_0_verdict: "REFERENCE 2026-07-23 — no public code located; methodology steal only"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

**Briefs:** `briefs/2026-07-23_k213-probabilistic-llm-safety-bounds-prod.md`

## Relations

- @concepts/llm-probabilistic-safety-bounds.md
- @concepts/agent-runtime-guardrails.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Sound Probabilistic Safety Bounds for Large Language Models |
| Authors | Nazeri, Schmuck, Soudjani, Abate (Oxford / MPI-SWS / Birmingham) |
| arXiv | 2607.20286 |
| Code | none located |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.20286-sound-probabilistic-safety-bounds-for-large-lang.pdf` |
| Retrieved | 2026-07-23 |

## Narrative

Framework for **rigorous lower bounds** on P(harmful output | prompt) via Clopper-Pearson → PAC intervals. Algorithm prioritizes latent-space branches in the auto-regressive tree that are likelier harmful — enables useful lower bounds even when true harm rate is tiny; bounds are **sound** (proven ≤ true probability).

### Steal

1. Alignment ≠ certification — need statistical lower bounds for high-stakes prompts
2. Latent-guided rare-event search beats naive sampling for tiny harm probs
3. Useful for pre-deploy safety review of tool-using agents on high-risk prompts

## Snippets

> "the obtained lower bounds are sound, i.e., formally proven to be less than the actual harmfulness probability"
[Source: arxiv-2607.20286 abstract]
