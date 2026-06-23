---
title: Confidently Wrong — severity-aware PI detector calibration (arXiv 2606.22659)
type: source
tags: [source, arxiv, prompt-injection, guard-model, calibration, llm-security]
keywords: [2606.22659, protectai, prompt-guard-2, severity metric, confident false negatives, content-keying, bipia]
related:
  - concepts/ai-for-cybersecurity.md
  - concepts/prompt-injection-detector-calibration.md
  - entities/tools/picalib-research.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-security-posture.md
  - entities/tools/llm-defense-lattice.md
  - concepts/llm-adversarial-fuzzing.md
  - sources/arxiv-2606-02822-owasp-llm-defense-attribution.md
maturity: draft
read_status: read
created: 2026-06-23
updated: 2026-06-23
phase_0_verdict: "Reference 2026-06-23 — github.com/anasbiswas1/picalib-research: 0★, gh api LICENSE null/404; reproduce severity metric only after SPDX audit"
---

## Relations

- @concepts/prompt-injection-detector-calibration.md — severity metric S + shift testing framework
- @entities/tools/picalib-research.md — public code/data artifact

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Confidently Wrong: Severity-Aware Calibration of Prompt-Injection Detectors under Attack Shift |
| Author | Md Anas Biswas (University of Portsmouth) |
| arXiv | 2606.22659v1 |
| Code | [github.com/anasbiswas1/picalib-research](https://github.com/anasbiswas1/picalib-research) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2606.22659-2606-22659v1-confidently-wrong-severity-aware-ca.pdf` |
| Retrieved | 2026-06-23 |
| Read status | **read** (abstract, eval design, key findings) |

## Narrative

Studies **confidence of prompt-injection guard scores** under **distribution shift** — not just accuracy at a frozen threshold.

### Detectors tested

- **ProtectAI-v2**
- **Prompt-Guard-2** (two checkpoints, ~4× size range)

Single source-calibrated threshold **frozen and transported** across **five shift conditions**.

### Severity metric S

Confidence assigned to **missed attacks** (confident false negatives). Across all shifts/detectors:

- **Severity on misses: 0.99–1.00** (miss with near-certainty)
- **FNR: 0.01–0.97** depending on shift

### Critical blind spot

**Indirect behavior-hijack injection** (BIPIA-style) — unanimous miss across both vendors. Pooled calibration error **hides** this: one detector rated 0.06 ECE overall but **0.91 miscalibrated on attacks alone**.

Live-model tests: missed injections pass **working exploits** at rates comparable to caught attacks.

### Root cause

**Content-keying** rather than injection structure — instruction-tuned judge models show same hijack blind spot. Black-box rewriter can **manufacture confident misses**, strongest on most dangerous attack category.

### Defender takeaway

Guard-model **block/allow decisions are insufficient** — log and alert on **high-confidence passes of untrusted content** after shift testing. Complements OWASP LLM01 attribution (@entities/tools/llm-defense-lattice.md).

## Snippets

> "When these detectors miss, they miss with near-certainty."

> "Standard pooled calibration error does not register this; one detector it rates well-calibrated, at 0.06, is miscalibrated at 0.91 on the attacks alone."

[Source: arxiv-2606.22659-confidently-wrong-prompt-injection-calibration.pdf]
