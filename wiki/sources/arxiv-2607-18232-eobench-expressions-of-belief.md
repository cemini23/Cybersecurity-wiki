---
title: EoBench — evaluating LLM responses to expressions of belief (arXiv 2607.18232)
type: source
tags: [source, arxiv, llm-eval, persuasion, context-following, acl]
keywords: [2607.18232, EoBench, expressions of belief, context vs prior, ACL 2026]
related:
  - concepts/llm-belief-expression-robustness.md
  - concepts/social-engineering.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-21
updated: 2026-07-31
phase_0_verdict: "REFERENCE 2026-07-21 — github.com/clarakuempel/EoB ~71MB NO LICENSE; HF dataset kdu4108/EoBench; steal typology only"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

**Briefs:** CCC handoff; cyber `briefs/2026-07-21_eobench-belief-expression-handoff.md`

## Relations

- @concepts/llm-belief-expression-robustness.md
- @concepts/social-engineering.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | It's Not What You Say, It's How You Say It: Evaluating LLM Responses to Expressions of Belief |
| Authors | Kevin Du, Clara Kümpel, Michelle Wastl, Alex Warstadt |
| Venue | ACL 2026 |
| arXiv | 2607.18232 |
| Code | github.com/clarakuempel/EoB (no LICENSE) |
| Dataset | hf.co/datasets/kdu4108/EoBench |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.18232-it-s-not-what-you-say-it-s-how-you-say-it-evalua.pdf` |
| Retrieved | 2026-07-21 |

## Narrative

**EoBench** tests how linguistic framing of user beliefs (19 types across form/evidentiality/stance/tone) pushes models to follow **context vs prior knowledge**. Larger + instruct-tuned models tend to be *less* context-following than smaller/base models. Some EoB framings are consistently more persuasive.

### Steal

1. Prompt/social-eng adjacent: frame sensitivity is a robustness axis
2. Don't assume bigger instruct models are more "stubborn" about truth — measure EoB susceptibility
3. No clone (no LICENSE)

### Phase-0

| Verdict | **REFERENCE** |

## Snippets

> "bigger models and instruction-tuned models tend to be less context-following than smaller models and base models."
[Source: arxiv-2607.18232 abstract]
