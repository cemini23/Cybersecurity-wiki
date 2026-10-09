---
title: "LipDA: lipsync forgery detection and source attribution"
type: source
tags: [source, routed]
keywords: [arXiv 2610.08417]
related:
  - concepts/lipsync-forgery-detection-attribution.md
  - concepts/armor-plusplus-agentic-deepfake-detector-attacks.md
maturity: draft
read_status: read (routed brief)
created: 2026-10-09
updated: 2026-10-09
phase_0_verdict: "REFERENCE 2026-10-09 — routed brief, no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (inbound brief)"
---

## Relations

- @concepts/lipsync-forgery-detection-attribution.md — K408-K417 ingest / 2026-10-09
- @concepts/armor-plusplus-agentic-deepfake-detector-attacks.md — K408-K417 ingest / 2026-10-09

## Raw Concept

| Field | Value |
|-------|-------|
| Title | LipDA: lipsync forgery detection and source attribution |
| Identifier | arXiv 2610.08417 |
| Type | arXiv paper (routed from image-gen 2026-10-08) |
| Location | not held locally — routed brief only |
| Retrieved | 2026-10-09 |
| Read status | read (routed brief) |

## Narrative

**Exploit the biological coupling between lip motion and head pose** — a coupling lipsync generators break. Real mouths move pose-consistently; generated ones do not. Detection aligns a **lip-ROI ResNet encoder** with a **6-DoF head-pose landmark encoder** via margin contrastive loss; attribution adds audio-visual cross-attention plus a temporal CNN/Bi-LSTM over keypoints to capture per-generator fingerprints.

**Detection AUC:** LipSync-A **99.42**, AVLips **99.82**, TalkHeadBench **97.50** — about 8 points over SpeechForensics. **Attribution: 97.5% accuracy / 93.9 F1**, over 12 points above TALL; generalises to unseen generators (Sonic 87.8, KDTalker 84.6, OmniSync 95.5) and Celeb-DF 92.76. Ships **LipSync-A**: 15 generators, 7 architectures, 16,000 labelled forged videos. Code at `github.com/AnsonShe/LipDA` — **no licence stated**; ~270 samples come from commercial APIs, so **verify terms before use**.

**Two caveats worth carrying.** Attribution leans on **generator leakage** — high numbers mean fingerprints are distinctive, not that forgeries are detectable in the wild; and the generator set is fixed, so the **84-95% generalisation figures are the honest bound.**

## Snippets

> Routed brief, not a first-hand read of the source. [Source: `briefs/` inbound route (2026-10-09)]
