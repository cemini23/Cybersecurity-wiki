---
title: "BLOOM-WILT — logit tilting for automated LLM behaviour auditing (arXiv 2608.31105)"
type: source
tags: [source, arxiv, agent-security, red-team, audit, lab-only, k319]
keywords: [2608.31105, BLOOM-WILT, WILT, LogitTilt, behaviour elicitation, automated auditing, multi-turn]
related:
  - concepts/logit-tilting-rare-behaviour-audit.md
maturity: draft
read_status: read
created: 2026-09-01
updated: 2026-09-01
phase_0_verdict: "REFERENCE 2026-09-01 — github.com/AdrSkapars/bloom-wilt license:null HOLD; no weight/training wire. Authorized-lab audit only."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K319)"
---

## Relations

- @concepts/logit-tilting-rare-behaviour-audit.md — primary steal (multi-turn rare-behaviour elicitation)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | BLOOM-WILT: Logit Tilting for Behaviour Elicitation in Automated LLM Auditing |
| Authors | Adrians Skapars, Edoardo Manino |
| arXiv | 2608.31105 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.31105-bloom-wilt-logit-tilting-for-behaviour-elicitati.pdf |
| Retrieved | 2026-09-01 |
| Read status | read (abstract + method overview) |
| Public code | `AdrSkapars/bloom-wilt` — **license null** at hunt; HF dataset transcripts |

## Narrative

**BLOOM-WILT** extends the BLOOM auditing pipeline with **WILT**: (1) **G-PAIR-style** auditor input refinement across rounds from scored transcripts; (2) **LogitTilt** — reweights target decoding toward a behaviour-eliciting prompt distribution from the **same model's logits** (training-free, black-box beyond next-token logits).

**Goal:** elicit **natural multi-turn** instances of **rare behaviours** for audit/training monitors — not single-turn compliance to adversarial strings. Paper reports higher behaviour presence vs vanilla BLOOM across 4 models × 8 behaviours (e.g. 51%→100% self-harm encouragement elicitation on Qwen3.5-4B at matched compute).

**Why filed (K319):** lab **behaviour-audit** primitive pairs `@concepts/ai-redteam-evidential-ceiling.md` (deployment >> test volume). **Authorized lab only** — no elicitation payloads in wiki. Repo **HOLD** (null SPDX) — no clone until LICENSE verified.

## Snippets

> WILT adaptively reweights the target's decoding using the model's own distribution conditioned on an elicitation prompt. [Source: arXiv 2608.31105 abstract, paraphrase]
