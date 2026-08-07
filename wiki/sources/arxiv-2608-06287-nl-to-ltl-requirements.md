---
title: NL-to-LTL requirements via LLMs (arXiv 2608.06287)
type: source
tags: [source, arxiv, formal-methods, requirements, llm]
keywords: [2608.06287, LTL, requirements engineering, formal specification, pass@k]
related:
  - concepts/nl-to-ltl-requirements-llm.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-08-07
updated: 2026-08-07
phase_0_verdict: "REFERENCE 2026-08-07 — eval study; no public code; light cyber (safety-critical specs)"
wire_status: wont_wire
wire_target: "HITL formalization assistant pattern only"
---

**Briefs:** `briefs/2026-08-07_k251-nl-ltl-prod.md`

## Relations

- @concepts/nl-to-ltl-requirements-llm.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Automatic Translation of Unstructured Requirements into Linear Temporal Logic through Large Language Models |
| Authors | Alexandra Newcomb, Omar Ochoa |
| arXiv | 2608.06287 |
| Code | none found |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.06287-automatic-translation-of-unstructured-requiremen.pdf` |
| Retrieved | 2026-08-07 |

## Narrative

Few-shot LLMs → LTL from unstructured NL requirements (15 reqs × 6 models × 5 gens = 450). Manual semantic eval + pass@k + self-consistency. Viable **front-end** for semi-automated formalization with explanations/visualization — not a replacement for expert review. [CONFIRMED abstract]

### Steal

1. For security/mission-critical requirements: LLM drafts LTL; human + solver verify
2. Prefer pass@k + consistency over single-shot formulas
3. Do not treat LLM LTL as authoritative policy without HITL

## Snippets

> "modern LLMs are becoming viable front-end assistants for semi-automated formalization workflows."
[Source: arXiv 2608.06287 abstract]
