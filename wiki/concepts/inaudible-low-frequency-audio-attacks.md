---
title: "Inaudible low-frequency audio attacks — LALM red-team surface + DRG defense"
type: concept
tags: [methodology, llm-security, audio-attack, lalm, red-team, side-channel]
keywords: [inaudible audio attack, LALM, infrasound, 5-20 Hz, ILL, DRG, distributional requery, adversarial audio, ultrasonic]
related:
  - sources/arxiv-2608-09158-ill-inaudible-low-frequency-lalms.md
  - entities/tools/ill-inaudible-low-frequency-lockout.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-for-cybersecurity.md
  - concepts/llm-pentest-automation.md
  - concepts/airkey-wifi-acoustic-pin-sidechannel.md
maturity: draft
created: 2026-08-11
updated: 2026-08-11
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K267)"
---

# Inaudible low-frequency audio attacks — LALM red-team surface + DRG defense

## Relations

- @sources/arxiv-2608-09158-ill-inaudible-low-frequency-lalms.md
- @entities/tools/ill-inaudible-low-frequency-lockout.md
- @concepts/llm-adversarial-fuzzing.md — LALM input is another adversarial-fuzz surface, distinct from text jailbreaks
- @concepts/agent-runtime-guardrails.md — audio-side defenses (LF-suppression, denoising, DRG requery) are runtime guard inputs
- @concepts/ai-for-cybersecurity.md — LLM agents with audio/video frontends in scope for authorized lab
- @concepts/llm-pentest-automation.md — audio red-team loops must obey the same scope-enforcement model
- @concepts/airkey-wifi-acoustic-pin-sidechannel.md — adjacent acoustic side-channel family (PIN inference vs availability attack)

## Raw Concept

What is the security surface of audio-input models? The LALM encoder transforms raw waveform into model-side acoustic tokens, so the input surface is not defined by human perception. Anything the frontend passes through — including sub-20 Hz energy — can steer generation while being inaudible to the user. This page synthesizes the ILL paper (2608.09158) plus prior adversarial-audio work (hidden voice commands, DolphinAttack, Audio-Adv, Whisper muting, Audio-jailbreak) into a working concept.

## Narrative

### The perception-boundary mismatch

An LALM's audio frontend captures physical superposition `x(t) + δ(t)`. A signal below ~20 Hz is inaudible to a human but can still shift the model's encoded representation, producing **availability/reliability failures** (wrong ASR transcript, invalid audio-QA answer, missing translation semantics, wrong emotion decision) without the user noticing the interference. This is a *hidden input channel* distinct from ultrasonic "hidden voice commands" (which ride above 20 kHz): ILL occupies the infrasonic band 5–20 Hz that commodity microphones measurably pass.

### ILL construction (red-team method)

1. **Active-interval scheduling via attention** — a reference LALM forward pass over a speech corpus yields averaged self-attention; boundary scores at multiple scales locate spans of continuous semantic attention (median `Lon` 3.67–5.07 s). Duty ratio γ sets the off period.
2. **Frequency-confusion waveform** — STFT spectral centroids → n-state quantization → corpus transition matrix → DP most-probable non-self-loop state sequence → continuous-phase `sin(2π∫φ dt)` with smooth envelope and amplitude β. The tuple `(δon, Loff)` is fixed and reused for any test recording — a **universal template**, no per-utterance or per-target optimization.
3. **Deployment** — the attacker emits δ⋆(t) standalone (physical superposition), or simulates the received amplitude β.

### Why it works (mechanistic evidence)

- Reduced audio-attention mass (0.0777→0.0531 on RAVDESS) and lower cosine similarity (1.000→0.6309), recovered to ~0.96 under DRG.
- Correct-answer probability collapses (0.824→0.0179 on RAVDESS) — the model stops relying on acoustic evidence.
- Ablations: effectiveness depends on **structured state construction**, not raw low-frequency energy; Gaussian/fixed-frequency/sweep baselines underperform; duty cycle saturates beyond ~70%; amplitude knee at β≈4.

### Defense: Distributional Requery Guard (DRG)

- Offline: K-means (k=2) over ℓ1-normalized spectral descriptors of clean vs jammed training recordings; label the cluster with more low-frequency mass as interference.
- At inference: nearest-centroid assignment; only flagged inputs trigger a **second recording** requery with compare-and-answer — O(V) detection, no neural forward pass or target-LALM query for the detector itself.
- Requery is a **plug-in input filter**, not a model retrain; recovery works for other noise/attack types too (19/24 best-or-tied).

### Blue-team takeaways

- Audio-capable agent copilots should assume the mic path is attacker-influenced in scope; consider LF-attenuation / spectral-descriptor monitoring at the frontend.
- Defense-in-depth: DRG (requery) + denoising (DFL/MMSE) + refusal hardening are complementary; requery buys independent acoustic evidence only when the second recording is clean (persistent interference gains are smaller).
- Red-team scope: ILL-class work is **authorized lab only** — no emitting infrasound at uncontrolled targets; requires a low-frequency-capable source, not a laptop speaker. `[CONFIRMED]` for the paper's own ethics posture.

## Snippets

> A sufficiently low-frequency signal may therefore enter an LALM's audio frontend while remaining imperceptible to its user, creating a potential mismatch between the acoustic evidence available to the model and to the person interacting with it. [Source: arXiv:2608.09158 p.1]

> The 20 Hz boundary is a convention tied to human audibility, not a propagation cutoff in air. Controlled sources have generated and transmitted signals well below this boundary … coherent infrasound at a 3.8 km stand-off distance, with received signal-to-noise ratios of 5–15 dB. [Source: arXiv:2608.09158 Appendix A]

## Dead Ends

- **Laptop/phone speaker as ILL source** — conventional transducers face mass-dominated radiation impedance at very low frequencies; a physical realization needs a low-frequency-capable source (rotary subwoofer class). The paper deliberately withholds device-specific SPL/placement settings.
- **Require causality** — the authors characterize attention/representation/confidence shifts as consistent with reduced evidence use, not a proven causal mechanism.
