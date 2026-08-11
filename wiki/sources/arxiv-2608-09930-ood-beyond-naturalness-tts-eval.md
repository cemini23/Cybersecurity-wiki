---
title: "OOD — Beyond Naturalness: probing automated TTS evaluators (arXiv 2608.09930)"
type: source
tags: [source, arxiv, ood, tts, speech-eval]
keywords: [2608.09930, TTS, MOS, Audio-LLM judge, naturalness, ServiceNow]
related:
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: skimmed
created: 2026-08-11
updated: 2026-08-11
phase_0_verdict: "OOD 2026-08-11 — TTS linguistics / ServiceNow speech-eval meta-benchmark. Route image-gen or skip."
wire_status: wont_wire
wire_target: "OOD — speech/audio quality eval, not cybersec harness wire"
---

**Briefs:** `briefs/2026-08-11_ood-beyond-naturalness-tts-route.md`

## Relations

- @concepts/ai-for-cybersecurity.md — contrast only (Audio-LLM judges surface is adjacent to LALM red-teaming, but this is evaluation linguistics, not security)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Beyond Naturalness: Probing Automated Text-To-Speech Evaluators on Linguistically Grounded Dimensions |
| Authors | Bamgbose, Rosen, Shah, Brin, Nguyen, Koelzer, Hansen, Bogavelli, Riols (ServiceNow) |
| arXiv | 2608.09930 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.09930-beyond-naturalness-probing-automated-text-to-spe.pdf` |
| Retrieved | 2026-08-11 |
| Read status | **skimmed** — OOD |
| Public code | Dataset/annotation schema/eval code released by authors (TTS evaluation, not security) |

## Narrative

Deconstructs "naturalness" into a 10-dimension linguistically grounded annotation schema for TTS; benchmarks four MOS predictors and four Audio-LLM judges on 860 linguist-annotated utterances. Finds MOS predictors collapse onto acoustic signal quality and Audio-LLM judges are prompt-dependent and do not generalize across dimensions. **Not** security content — it is a speech-quality meta-evaluation benchmark (ServiceNow research). No agent-security, red-team, MCP, or LALM-attack payload. Stub blocks daily-digest re-fetch; route note: potential fringe value to `image-gen` wiki (audio/TTS synthesis evaluation) and to LALM-red-team context as an evaluator-robustness warning, but no cyber adopt.
