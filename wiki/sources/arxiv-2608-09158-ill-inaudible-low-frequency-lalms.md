---
title: "ILL: From Inaudible Inputs to Model Failures — low-frequency safety risks in LALMs (arXiv 2608.09158)"
type: source
tags: [source, arxiv, llm-security, audio-attack, red-team, lalm]
keywords: [2608.09158, ILL, LALM, infrasound, low-frequency, DRG, audio red team, inaudible attack]
related:
  - concepts/inaudible-low-frequency-audio-attacks.md
  - entities/tools/ill-inaudible-low-frequency-lockout.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-for-cybersecurity.md
  - concepts/llm-pentest-automation.md
maturity: draft
read_status: read
created: 2026-08-11
updated: 2026-08-11
phase_0_verdict: "REFERENCE 2026-08-11 — no public code URL in paper; black-box red-team method + DRG defense. K267 policy wire."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K267)"
---

**Briefs:** `briefs/2026-08-11_k267-ill-inaudible-lalm-red-team.md`

## Relations

- @concepts/inaudible-low-frequency-audio-attacks.md
- @entities/tools/ill-inaudible-low-frequency-lockout.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/agent-runtime-guardrails.md
- @concepts/ai-for-cybersecurity.md
- @concepts/llm-pentest-automation.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | From Inaudible Inputs to Model Failures: Low-Frequency Safety Risks in LALMs |
| Authors | Zhang, Wang (BUPT); Ren, Lin (IIE-CAS); Zhou, Gao, Wang (NTU/JIUTIAN); Li (Tencent ARC); Sun, Su (BUPT/CQUPT) |
| arXiv | 2608.09158 |
| Code | None public at retrieval (2026-08-11) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.09158-from-inaudible-inputs-to-model-failures-low-freq.pdf` |
| Retrieved | 2026-08-11 |
| Read status | read (13 pp) |

## Narrative

ILL is a black-box, inaudible red-teaming method against large audio-language models (LALMs). It exploits the mismatch between the model's audio input surface (defined by the encoder) and human perception: a fixed universal waveform in the 5–20 Hz (infrasonic/low-frequency) band degrades ASR, translation, audio QA, and emotion classification while staying ~inaudible (mean human audibility 1.33/7 vs 1.17 clean; ANR 0.06–0.08%).

Construction (offline, reference LALM + speech corpus, no target querying):
- **Sentence Attention Scale Estimation** — averages self-attention across layers/heads, derives boundary scores at scales `{ρ, 5ρ, 10ρ}` to locate "active intervals" (`Lon`, median 3.67–5.07 s across datasets/models), sets a duty cycle γ.
- **Frequency Confusion Transfer** — STFT spectral centroids quantized into `n` states; corpus transition matrix decoded (DP, no self-loop) into a continuous-phase low-frequency state sequence; amplitude β with a smooth envelope; template fixed across test recordings.

DRG defense: K-means over ℓ1-normalized spectral descriptors to flag low-frequency distribution shift, then **conditional requery** — request a second recording of the same utterance and feed both to the LALM with compare-and-answer instruction. Detection F1 89.69–99.00% (Average training condition); clean reacquisition lifts mean attacked accuracy 28.5% → 46.1%; best/tied-best recovery in 19/24 settings across other attacks; benign utility cost small (10/12 scores within 0.03).

Transfer: built once on Qwen2.5-Omni, degrades all six targets (largest drop 67 pp on unseen StepAudio2 RAVDESS) — strong migration without per-target optimization. `[CONFIRMED]` from paper tables.

Physical chain caveat (Appendix A): 20 Hz boundary is a human-audibility convention, not an air propagation cutoff; rotary/infrasound sources (Park-Robertson 2009; Asmar 2018) generate the band at stand-off distance, but commodity laptop/phone speakers are mass-impedance-limited. Microphone response 0.5–20 Hz is measurable for electret + smartphone mics but non-flat (ports, AC coupling, high-pass, AGC).

## Snippets

> ILL reduces accuracy by up to 67 percentage points while receiving a mean human audibility rating of 1.33, close to 1.17 for clean audio; DRG raises mean attacked accuracy from 28.5% to 46.1% after clean reacquisition. [Source: arXiv:2608.09158 abstract]

> Across the six datasets, ILL has an ANR of only 0.06–0.08%, whereas all evaluated baselines exceed 98.9%. [Source: arXiv:2608.09158 p.5]

## Dead Ends

- No public code/repo at retrieval — **REFERENCE**; re-check GitHub before attempting local repro (do not hand-reconstruct emission hardware without a low-frequency-capable source).
- Author limitation: experiments simulate microphone reception, not the full loudspeaker→air→mic chain; no device-specific SPL/placement settings are provided. Physical feasibility is demonstrated, fidelity is not.
