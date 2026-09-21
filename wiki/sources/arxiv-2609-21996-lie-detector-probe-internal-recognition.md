---
title: "PIR — lie detector test for language models (arXiv 2609.21996)"
type: source
tags: [source, arxiv, agent-security, audit, sandbagging, eval, k352]
keywords: [2609.21996, PIR, Probe of Internal Recognition, sandbagging, concealed knowledge, unlearning verification]
related:
  - concepts/probe-internal-recognition-sandbagging-audit.md
  - concepts/counterfactual-simulatability-llm-explanations.md
maturity: draft
read_status: read
created: 2026-09-21
updated: 2026-09-21
phase_0_verdict: "REFERENCE 2026-09-21 — internal-state audit method; no probe payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K352) + lab-redteam"
---

## Relations

- @concepts/probe-internal-recognition-sandbagging-audit.md — K352 concept

## Raw Concept

| Field | Value |
|-------|-------|
| Title | A Lie Detector Test for Language Models: Reading Knowledge a Model Won't Reveal |
| arXiv | 2609.21996 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.21996-a-lie-detector-test-for-language-models-reading.pdf |
| Retrieved | 2026-09-21 |
| Read status | read (abstract + triage) |

## Narrative

**Probe of Internal Recognition (PIR)** adapts the Concealed Information Test: present a question with candidate answers and read from internal states which answer the model recognizes — **reference-free** (no honest reference model, no labeled truth corpus). Across eight models, balanced accuracy 0.70–0.87 vs 0.28–0.40 unknown baseline; stays readable under prompted deception, trained sandbagging, and password-locked checkpoints. Separates **will not answer** from **cannot answer** — relevant for sandbagging audits and unlearning verification. **K352** is an **authorized-lab eval / audit primitive**; pairs K290 CHIVE counterfactual discipline and K314 recognition≠enforcement. No probe recipes or concealment payloads in wiki.

## Snippets

> PIR separates a model that will not answer from one that cannot — supporting sandbagging audits and unlearning verification. [Source: arXiv 2609.21996 abstract]

> Reference-free: needs no honest reference model and no labeled truth corpus. [Source: arXiv 2609.21996 abstract]
