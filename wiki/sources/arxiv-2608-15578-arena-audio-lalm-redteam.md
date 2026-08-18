---
title: "ARENA — automated red-teaming for large audio language models (arXiv 2608.15578)"
type: source
tags: [source, arxiv, llm-security, audio, lalm, red-team, k282]
keywords: [2608.15578, ARENA, LALM, audio-grounded red-teaming, FDR, PSR, MD-Judge, LlamaGuard3, AdvBench]
related:
  - concepts/audio-grounded-lalm-redteaming.md
  - entities/tools/arena-audio-redteam.md
  - concepts/inaudible-low-frequency-audio-attacks.md
  - sources/arxiv-2608-09158-ill-inaudible-low-frequency-lalms.md
  - entities/tools/ill-inaudible-low-frequency-lockout.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/llm-pentest-automation.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/faithful-agent-asr-measurement.md
maturity: draft
read_status: read
created: 2026-08-18
updated: 2026-08-18
phase_0_verdict: "REFERENCE 2026-08-18 — paper says code is on GitHub but no URL at retrieval; gh search found no SPDX'd ARENA-audio repo. Dual-ID: Cybersec K282 ≠ CCC K282 AgentRewind."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K282 ARENA-audio)"
---

**Briefs:** `briefs/2026-08-18_k282-arena-audio-lalm.md`

## Relations

- @concepts/audio-grounded-lalm-redteaming.md — synthesized concept
- @entities/tools/arena-audio-redteam.md — REFERENCE entity
- @concepts/inaudible-low-frequency-audio-attacks.md — ILL K267 sibling (inaudible-LF vs audio-grounded harm)
- @sources/arxiv-2608-09158-ill-inaudible-low-frequency-lalms.md
- @entities/tools/ill-inaudible-low-frequency-lockout.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/llm-pentest-automation.md
- @concepts/ai-redteam-evidential-ceiling.md
- @concepts/faithful-agent-asr-measurement.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | ARENA: Automated Red-Teaming for Large Audio Language Models |
| Authors | Jiaming He, Zhicong Huang, Tian Jin, Zhen Sun, Cheng Hong, Yi Yu, Wenbo Jiang, Xudong Jiang (NTU / Ant Group / CUHK-Shenzhen / Jilin / UESTC) |
| arXiv | 2608.15578 (cs.SD, v1 16 Aug 2026) |
| Code | claimed “available at Github”; **no URL** in PDF; hunt 2026-08-18 found no matching SPDX repo |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.15578-arena-automated-red-teaming-for-large-audio-lang.pdf` |
| Retrieved | 2026-08-18 |
| Read status | read (full extract) |

## Narrative

ARENA studies **automated audio-grounded red-teaming**: the text query must remain safe in isolation while the joint text+audio input induces harmful target behavior. A closed-loop controller is trained on an independent 2,000-case text-audio set. **MD-Judge** supplies training rewards and adaptive search feedback; a separate, non-adaptive **Llama Guard 3** evaluator alone labels final outcomes. Evaluation is 520 held-out AdvBench objectives.

Reported FDR/PSR: Audio Flamingo 3 **87.9/100**; Qwen2-Audio **71.5/96.3**; MiMo-Audio **68.1/100**; GPT-Audio **75.4/98.5**. Ablations: feedback-based refinement and audio-variant search improve discovery. [TENTATIVE] single paper; no local repro.

**Cybersec K282** (≠ CCC K282 AgentRewind). Authorized acoustic lab / owned devices only. No jailbreak audio payloads in this wiki.

## Snippets

> We study automated audio-grounded red-teaming, where a text query must remain safe in isolation while the joint text-audio input induces harmful target behavior. [Source: arXiv 2608.15578 abstract]

> MD-Judge supplies training rewards and adaptive search feedback, while a separate, non-adaptive Llama Guard 3 evaluator alone labels final outcomes. [Source: arXiv 2608.15578 abstract]
