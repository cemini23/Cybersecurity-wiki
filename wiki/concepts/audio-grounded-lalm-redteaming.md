---
title: "Audio-grounded LALM red-teaming (text-safe + audio-harmful)"
type: concept
tags: [concept, methodology, llm-security, audio, lalm, red-team, k282]
keywords: [audio-grounded red-teaming, LALM, FDR, PSR, split judge, ARENA, ILL]
related:
  - sources/arxiv-2608-15578-arena-audio-lalm-redteam.md
  - entities/tools/arena-audio-redteam.md
  - concepts/inaudible-low-frequency-audio-attacks.md
  - sources/arxiv-2608-09158-ill-inaudible-low-frequency-lalms.md
  - entities/tools/ill-inaudible-low-frequency-lockout.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/llm-pentest-automation.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/faithful-agent-asr-measurement.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K282 ARENA-audio)"
---

## Relations

- @sources/arxiv-2608-15578-arena-audio-lalm-redteam.md — ARENA paper
- @entities/tools/arena-audio-redteam.md — REFERENCE (no public SPDX URL)
- @concepts/inaudible-low-frequency-audio-attacks.md — ILL K267: inaudible-LF availability vs this page's semantic audio-grounded harm
- @sources/arxiv-2608-09158-ill-inaudible-low-frequency-lalms.md
- @entities/tools/ill-inaudible-low-frequency-lockout.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/llm-pentest-automation.md
- @concepts/ai-redteam-evidential-ceiling.md — split train-judge vs frozen eval is an evidential-ceiling control
- @concepts/faithful-agent-asr-measurement.md — report FDR/PSR as a measurement tuple, not one ASR

## Raw Concept

What safety surface appears when a language model accepts audio as evidence? Text-only red-teaming misses cases where the text query is benign and the harmful intent lives in speech, speaker cues, or environmental sound.

## Narrative

**Two-sided condition.** Audio-grounded red-teaming requires (1) a text query that stays safe in isolation and (2) a joint text+audio input that induces unsafe assistance. The attack must choose whether harmful context is spoken or environmental, and recover from recognition failures, refusals, or answers that only restated the sound event.

**Split judges.** Train-time reward/search (ARENA: MD-Judge, adaptive) must not be the same model that labels the held-out report (ARENA: frozen Llama Guard 3). Collapsing them inflates discovery claims. Report **FDR and PSR separately**.

**Relation to ILL.** ILL (K267) is an *inaudible* 5–20 Hz availability attack. This page is *audible-to-the-model* semantic grounding: the user-visible text looks safe. Both are authorized acoustic lab / owned devices only — no LIVE eavesdrop, no attack audio in the wiki.

**Dual-ID:** Cybersec K282 ARENA-audio ≠ CCC K282 AgentRewind.

## Snippets

> Harmful intent can hide in the audio channel while the text query remains safe. [Source: arXiv 2608.15578 Fig. 1 caption]
