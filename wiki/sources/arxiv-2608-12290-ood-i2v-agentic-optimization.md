---
title: "OOD — Agentic Self-Improvement for Image-to-Video adherence (arXiv 2608.12290)"
type: source
tags: [source, arxiv, ood, image-to-video, generative-ai, agentic-optimization]
keywords: [2608.12290, I2V, image-to-video, DSG, CMQ, VTA, Bayesian optimization, CFG scale, prompt optimization, Google, Veo]
related:
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: skimmed
created: 2026-08-13
updated: 2026-08-13
phase_0_verdict: "OOD 2026-08-13 — I2V generation optimization (Google Cloud/DeepMind); routed to image-gen wiki. Not cybersec harness wire."
wire_status: wont_wire
wire_target: "OOD — route to image-gen wiki"
---

**Briefs:** `briefs/2026-08-13_k277-rsm-role-specialization.md` (OOD route note section)

## Relations

- @concepts/ai-for-cybersecurity.md — general AI-research adjacency only (digest-cycle continuity; fetched in the llm-security paper lane)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Beyond Trial-and-Error: Agentic Optimization for Image-to-Video Adherence |
| Authors | Aman Tyagi, Hemanth Boinpally, Jonathan Chen, Douglas Gebert (Google Cloud); Steven Hickson (Google DeepMind) |
| arXiv | 2608.12290 (cs.CV, v1 12 Aug 2026) |
| Code | None public at retrieval |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.12290-beyond-trial-and-error-agentic-optimization-for.pdf` |
| Retrieved | 2026-08-13 |
| Read status | skimmed — OOD |

## Narrative

Google Cloud/DeepMind **Image-to-Video (I2V)** generation paper: a two-stage "Agentic Self-Improvement" loop that reframes video synthesis as closed-loop goal-directed optimization — (1) an mLLM iteratively refines the prompt against Davidsonian Scene Graph (DSG) semantic-adherence queries and Common Mistake Question (CMQ) artifact checks; (2) Bayesian optimization co-optimizes stochastic seeds and CFG scales, guided by a Video-Text Adherence (VTA) score. Human-preference win rates up to 69% over unguided search.

**OOD:** video-generation parameter optimization, not security. Routed to the **image-gen wiki** — the Agentic Self-Improvement loop (prompt optimization + Bayesian seed/CFG search + adherence scoring) is directly relevant to ComfyUI/video-gen workflows there. Stub exists so the daily digest skips re-fetch; the llm-security paper lane should ANDNOT I2V/generation-optimization noise.

## Snippets

> This work provides a practical and extensible methodology for enhancing the predictability and control of state-of-the-art video generation models, moving the field beyond speculative curiosities toward reliable, production-ready tools. [Source: arXiv:2608.12290 abstract]

## Dead Ends

- No cybersec attack/defense content; no adversarial-image content that intersects existing cyber pages.
- No public code; Google-internal product research.
