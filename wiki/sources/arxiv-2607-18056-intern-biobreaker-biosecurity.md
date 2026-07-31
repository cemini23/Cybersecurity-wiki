---
title: Intern-BioBreaker — early warning of biosecurity risks in frontier LLMs (arXiv 2607.18056)
type: source
tags: [source, arxiv, biosecurity, dual-use, jailbreak, frontier-llm]
keywords: [2607.18056, Intern-BioBreaker, Shanghai AI Lab, bio-red-teaming, ASR]
related:
  - concepts/llm-biosecurity-red-teaming.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/responsible-disclosure.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: skimmed
created: 2026-07-21
updated: 2026-07-31
phase_0_verdict: "REFERENCE 2026-07-21 — dual-use bio red-team paper; no standalone public attack-tool adopt; steal early-warning + synthesis-screening posture only"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

**Briefs:** `briefs/2026-07-21_k198-biosecurity-llm-early-warning-prod.md`

## Relations

- @concepts/llm-biosecurity-red-teaming.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/responsible-disclosure.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | An Early Warning of Emerging Biosecurity Risks in Frontier LLMs |
| Authors | Shanghai Artificial Intelligence Laboratory (alphabetical) |
| arXiv | 2607.18056 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.18056-an-early-warning-of-emerging-biosecurity-risks-i.pdf` |
| Retrieved | 2026-07-21 |
| Read status | **skimmed** — dual-use; no operational bio content filed |

## Narrative

**Intern-BioBreaker** bio-red-teams frontier LLMs with a computational→wet-lab validation chain. Claims: high/saturated task-level ASR on several open-weight + proprietary models; some sequence-level generations with pathogenic potential; selected designs physically realized in controlled lab settings. Underscores need for bio red-teaming, nucleic-acid synthesis screening, and safeguards that keep pace with scientific capability.

### Wiki policy

Do **not** reproduce jailbreak prompts, viral sequences, or wet-lab recipes here. File risk posture + defender actions only.

### Steal (defensive)

1. Treat frontier science models as dual-use surfaces, not only chatbots
2. Require synthesis-screening + capability eval for bio-capable models
3. Text-refusal ≠ physical-risk closure (wet-lab validation gap)

### Phase-0

| Verdict | **REFERENCE** — awareness; no attack-tool clone |

## Snippets

> "text-level safeguards and the risks posed by capable scientific models" — gap highlighted by near-saturated bio-risk ASR on several targets.
[Source: arxiv-2607.18056 abstract paraphrase]
