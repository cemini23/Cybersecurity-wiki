---
title: "OOD — Agentic Approach for Active Data Collection, Travel Behavior Modeling (arXiv 2608.20320)"
type: source
tags: [source, arxiv, ood, transportation, multi-agent, survey, travel-behavior]
keywords: [2608.20320, travel behavior, stated-preference survey, multi-agent workflow, McGill, mode choice, LLM prediction]
related:
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: skimmed
created: 2026-08-21
updated: 2026-08-21
phase_0_verdict: "OOD 2026-08-21 — transportation/civil-engineering (travel-behavior modeling), not a cyber runtime. No CCC runtime. Steal: auditable multi-agent survey→model workflow with researcher-approved revisions — a workflow-governance pattern, not cyber tradecraft."
wire_status: wont_wire
wire_target: "OOD — transportation; workflow-governance contrast only"
---

## Relations

- @concepts/ai-for-cybersecurity.md — contrast only (agent workflow governance, no cyber runtime)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | An Agentic Approach for Active Data Collection, Travel Behavior Modeling, and Weather-Sensitive Demand Prediction |
| Authors | Narges Ahmadi, Yubo Jiao, Jônatas Augusto Manzolli, Jiangbo Yu, Luis Miranda-Moreno (McGill) |
| arXiv | 2608.20320 (25 pp) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.20320-an-agentic-approach-for-active-data-collection-t.pdf` |
| Retrieved | 2026-08-21 |
| Read status | **skimmed** — OOD |
| Public code | none claimed for cyber adopt |

## Narrative

A **three-agent workflow** (conversational data collection → structured data processing → behavioral prediction) applied to travel-behavior research: a chatbot-administered, image-augmented stated-preference survey collected mode choices from **92 student commuters** across five weather scenarios (**454 respondent–scenario observations**). Weather associations modeled with multinomial logit; logistic regression + random forest as ML benchmarks; nine locally deployed LLMs (2–35B params) evaluated across zero-shot prompt/context conditions plus persona, few-shot, and vision configurations. Results: **random forest 69.6% five-class accuracy**; best text-only zero-shot LLM 69.9%; best vision-config LLM ~71.5% (Gemma 4:12B table entry); cycling most weather-sensitive; public transit rises under Snowy; habitual-travel info gives the most consistent LLM improvement.

**Why filed (OOD):** transportation/civil-engineering domain — no cyber runtime, no CCC wire. Steal (governance pattern only): the workflow uses **researcher-approved revisions** — stage diagnostics may motivate a new workflow version, never an automatic live mutation of an active study. That "reviewed revision, not auto-mutation" discipline is the only transferable idea; it parallels the wiki's harness-evolution HITL rules, not any cyber capability.

## Snippets

> …stage diagnostics may motivate a researcher-approved revision of an earlier survey, processing, or modeling specification in a subsequent workflow version. [Source: arXiv 2608.20320 §2.4/Fig 1, paraphrased]
