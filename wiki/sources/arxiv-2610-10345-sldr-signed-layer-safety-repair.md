---
title: "SLDR: repairing malicious fine-tunes by touching two layers"
type: source
tags: [source, routed]
keywords: [arXiv 2610.10345]
related:
  - concepts/local-suppression-vs-repair.md
  - concepts/speculative-decoding-safety-asymmetry.md
maturity: draft
read_status: read (routed brief)
created: 2026-10-09
updated: 2026-10-09
phase_0_verdict: "REFERENCE 2026-10-09 — routed brief, no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (inbound brief)"
---

## Relations

- @concepts/local-suppression-vs-repair.md — K408-K417 ingest / 2026-10-09
- @concepts/speculative-decoding-safety-asymmetry.md — K408-K417 ingest / 2026-10-09

## Raw Concept

| Field | Value |
|-------|-------|
| Title | SLDR: repairing malicious fine-tunes by touching two layers |
| Identifier | arXiv 2610.10345 |
| Type | arXiv paper (routed by OSINT K285) |
| Location | not held locally — routed brief only |
| Retrieved | 2026-10-09 |
| Read status | read (routed brief) |

## Narrative

**Layer safety sensitivity is signed.** Malicious fine-tuning — a rented poisoned LoRA — strips refusal, and SLDR's finding is that the layers which matter have a **direction**. So it repairs only the **two extreme-sensitivity layers** with a LoRA recovery adapter, and **routes only malicious queries** through the repair (cosine-based malicious score, tau = 0).

**Result:** average **Harmful Score 11.54 → 0.08** with finetune accuracy **92.39 → 92.32**, near-lossless, beating BDS / Panacea / Lisa / Antidote / STAR-DSS. Works across Llama-3.1, Llama-3, Qwen-2.5, Mistral. Operator steal: a repair does not have to be global — **find the signed layers and route only the traffic that needs repair.** Pairs K410 (constrained-action remediation) and the K285 PatchBench finding that breadth of repair is what causes collateral damage.

## Snippets

> Routed brief, not a first-hand read of the source. [Source: `briefs/` inbound route (2026-10-09)]
