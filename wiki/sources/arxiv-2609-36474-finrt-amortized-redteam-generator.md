---
title: "FinRT: distilling adaptive red-teaming strategies into reusable adversarial generators in consumer finance"
type: source
tags: [source, arxiv, agent-security]
keywords: [2609.36474, k382]
related:
  - concepts/finrt-amortized-redteam-generator.md
  - concepts/experience-driven-redteam-skill-evolution.md
  - concepts/piminer-agentic-prompt-injection-redteam.md
  - concepts/ai-redteam-evidential-ceiling.md
maturity: draft
read_status: read
created: 2026-09-30
updated: 2026-09-30
phase_0_verdict: "REFERENCE 2026-09-30 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K382)"
---

## Relations

## Relations

- @concepts/finrt-amortized-redteam-generator.md
- @concepts/experience-driven-redteam-skill-evolution.md
- @concepts/piminer-agentic-prompt-injection-redteam.md
- @concepts/ai-redteam-evidential-ceiling.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | FinRT: distilling adaptive red-teaming strategies into reusable adversarial generators in consumer finance |
| arXiv | 2609.36474 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.36474-finrt-distilling-adaptive-red-teaming-strategies.pdf |
| Retrieved | 2026-09-30 |
| Read status | read (abstract + triage) |

## Narrative

**K382** — automated red-teaming trades attack effectiveness against generation cost and treats coverage, severity, and diversity as incidental. **FinRT** separates search from generation: forward elicitation searches policy × domain × strategy and scores attackability (uncensored surrogate), realism, and structural fidelity; inverse elicitation fine-tunes a **reusable adversarial-prompt generator** (Mistral-7B + LoRA) on spec → prompt pairs; **calibrated proxy DPO** approximates target-specific DPO from a small calibration subset. Held-out consumer finance (419 policy–domain–behavior specs, six victim models, K=10): ASR **32.9%** (FinRT-DPO-calibrated) vs Rainbow Teaming **17.2%** and PAIR-Lite **15.5%**; max severity **3.54** vs **2.66**; realism-constrained coverage@10 **1.0** vs **0.86**. Cost is front-loaded (~1.52M target-independent LLM calls) and **amortized**, not cheaper. Operator steal: report ASR + severity + realism-constrained coverage + diversity **jointly**; human-audit a sample of judge labels (97.9% agreement on 700); keep the reusable generator separate from target-facing calls. **No repo; the authors withhold high-severity prompts and target adapters.** **Runtime:** `scripts/k382_finrt_amortized_redteam_precheck.py`. Pairs K313 red-team skill evolution and K248 PIMiner.

## Snippets

> See arXiv 2609.36474 abstract. [Source: arXiv 2609.36474 (retrieved 2026-09-30)]
