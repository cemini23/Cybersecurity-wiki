---
title: "CounterSteer: suppressing indirect prompt injection with activation steering"
type: source
tags: [source, arxiv, agent-security]
keywords: [2609.36570, k383]
related:
  - concepts/countersteer-activation-steering-ipi-defense.md
  - concepts/prompt-injection-detector-calibration.md
  - concepts/piminer-agentic-prompt-injection-redteam.md
maturity: draft
read_status: read
created: 2026-09-30
updated: 2026-09-30
phase_0_verdict: "REFERENCE 2026-09-30 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-mcp-tool-control.mdc (K383)"
---

## Relations

## Relations

- @concepts/countersteer-activation-steering-ipi-defense.md
- @concepts/prompt-injection-detector-calibration.md
- @concepts/piminer-agentic-prompt-injection-redteam.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | CounterSteer: suppressing indirect prompt injection with activation steering |
| arXiv | 2609.36570 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.36570-countersteer-suppressing-indirect-prompt-injecti.pdf |
| Retrieved | 2026-09-30 |
| Read status | read (abstract + triage) |

## Narrative

**K383** — indirect prompt injection (IPI) makes an agent treat untrusted retrieved text as instructions. **CounterSteer** is an **inference-time** defense: per model, a five-step recipe fits a residual-stream direction from paired episodes that differ only in whether an embedded instruction is followed, keeps it only if it passes pre-specified **causal** (subtract lowers follow, add raises follow) and **capability** gates, then subtracts a fixed dose from **every tool-result token during prefill**. Always-on — no detector to evade; needs white-box serving + tool-span tags; no fine-tune, auxiliary model, or added tokens. Five open-weights models (8B–106B): held-out ASR **0.00–0.17** vs **0.21–1.00** undefended; AgentDojo compromise **0.006–0.079** vs **0.10–0.49**; benign utility **93–100%** typography-normalized. None of **2,052** replayed LLMail-Inject attacks succeeds. **Residual gap:** parameter manipulation — attacker-chosen arguments in otherwise legitimate calls — is only partly resisted (**13/18** cracked); steering does not remove it, so pair with **argument-provenance controls**. Artifact ships attack drivers (**code-available**, license not stated) → **no clone**. **Runtime:** `scripts/k383_countersteer_ipi_precheck.py`. Pairs K248 PIMiner and IPI detector calibration.

## Snippets

> See arXiv 2609.36570 abstract. [Source: arXiv 2609.36570 (retrieved 2026-09-30)]
