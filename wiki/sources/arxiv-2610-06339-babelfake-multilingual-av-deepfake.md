---
title: "BabelFake: a multilingual audio-visual deepfake benchmark"
type: source
tags: [source, routed, agent-security]
keywords: [arXiv 2610.06339]
related:
  - concepts/armor-plusplus-agentic-deepfake-detector-attacks.md
maturity: draft
read_status: read (routed brief)
created: 2026-10-07
updated: 2026-10-07
phase_0_verdict: "REFERENCE 2026-10-07 — routed brief, no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (inbound brief)"
---

## Relations

- @concepts/armor-plusplus-agentic-deepfake-detector-attacks.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | BabelFake: a multilingual audio-visual deepfake benchmark |
| Identifier | arXiv 2610.06339 |
| Type | arXiv paper (routed from image-gen 2026-10-07) |
| Location | not held locally — routed brief only |
| Retrieved | 2026-10-07 |
| Read status | read (routed brief) |

## Narrative

**A detection benchmark, not a generation resource** — which is why image-gen routed it here. First **consent-sourced, multilingual audio-visual** deepfake detection benchmark: IRB-approved, paid participants consenting to their likeness and voice being manipulated, released behind a data-use agreement.

**Scale:** 399k clips / 1,323 hours / 496 individuals across English, German, Italian, French, Spanish. **20,117 real + 379,582 fake**, identity-disjoint 70/10/20 split. Built from **11 video manipulation methods** (face swap, lipsync, portrait animation) and **4 voice-cloning engines**, conditioned on pristine and synthetic audio.

**Detection results:** SpeechForensics best overall at **AUC 79.79** (peak **83.83** Spanish, **80.99** English). Multimodal beats unimodal (**74.27 vs 71.44** macro AUC). The operational finding: detectors **degrade sharply when the visual fake keeps authentic audio** — the real audio track removes the signal they lean on. No language is consistently hardest; demographic gaps mostly under 4 AUC.

**Access:** no repository, no code, no weights, not on GitHub or Hugging Face — controlled non-commercial licence with institutional verification and a data-use agreement.

## Snippets

> Routed brief, not a first-hand read of the source. [Source: `briefs/` inbound route (2026-10-07)]
