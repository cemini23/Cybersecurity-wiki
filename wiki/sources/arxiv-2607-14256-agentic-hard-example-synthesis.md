---
title: Agentic hard-example synthesis for multimodal content safety (arXiv 2607.14256)
type: source
tags: [source, arxiv, multimodal, content-safety, red-teaming, google]
keywords: [2607.14256, hard example synthesis, agentic data curation, fnr, multimodal safety]
related:
  - concepts/agentic-hard-example-synthesis-content-safety.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/amt-x-phase-structured-multi-turn-red-teaming.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: skimmed
created: 2026-07-17
updated: 2026-07-17
phase_0_verdict: "REFERENCE 2026-07-17 — Google/UCLA methodology; no public repo; steal agentic hard-example loop + FNR metric"
---

**Briefs:** `briefs/2026-07-17_agentic-hard-example-synthesis-handoff.md`, `briefs/2026-07-17_k186-agentic-hard-example-synthesis-prod.md`

## Relations

- @concepts/agentic-hard-example-synthesis-content-safety.md — synthesis

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Automatic Hard Example Synthesis with Multi-Level Agentic Data Curation |
| Authors | Genglin Liu, Muye Zhang, Krishnamurthy Viswanathan, et al. |
| Affiliation | UCLA; Google |
| arXiv | 2607.14256 |
| Code | **none found** |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.14256-automatic-hard-example-synthesis-with-multi-leve.pdf` |
| Retrieved | 2026-07-17 |
| Read status | **skimmed** |

## Narrative

Multi-agent loop (Architect + image generator + multi-level LLM rater committee on Gemini 3) synthesizes hard multimodal safety edge cases without human labeling. Using synthesized examples as test-time retrieval in-context demos cuts False Negative Rate **41.2% → 24.5%**. [Source: abstract]

### Steal

1. Agentic hard-example curation beats passive active-learning queues for content-safety coverage
2. Report **FNR** on safety classifiers, not only ASR on jailbreaks
3. Multi-level verification committee mirrors AMT-X dual-gate spirit

### Phase-0

REFERENCE — no public code; Gemini-backed internal stack.

## Snippets

> "…reducing the False Negative Rate (FNR) from 41.2% to 24.5% in our evaluation without relying on any human labeling."
[Source: arxiv-2607.14256 abstract]
