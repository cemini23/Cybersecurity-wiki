---
title: "GFlowNet automated LLM attack generation (Turkcell) — arXiv 2608.10171"
type: source
tags: [source, arxiv, llm-security, red-team, gflownet, automated-red-teaming]
keywords: [2608.10171, GFlowNet, red-teaming, attacker-victim-evaluator, Turkish, SFT, MLE, attack diversity, Qwen3, Gemma3]
related:
  - concepts/gflownet-automated-redteam-attack-generation.md
  - concepts/gflowrl-distribution-matching-attacker-rl.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-08-12
updated: 2026-08-12
phase_0_verdict: "REFERENCE 2026-08-12 — no public code/repo at Phase-0 (4-page workshop paper; builds on Lee et al. ICLR 2025). K270 lab-redteam policy wire."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K270)"
---

**Briefs:** `briefs/2026-08-12_k270-gflownet-llm-attacks.md`

## Relations

- @concepts/gflownet-automated-redteam-attack-generation.md
- @concepts/gflowrl-distribution-matching-attacker-rl.md — sibling GFlowNet-attacker line (Microsoft GFlowRL); do not conflate
- @concepts/llm-adversarial-fuzzing.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Generating Attacks for LLMs with GFlowNets |
| Authors | Berkay Ozcam, Irem Onen, Emin Islam Tatli (Turkcell Cybersecurity R&D); Mehmet Fatih Amasyali (Yıldız Technical Univ) |
| arXiv | 2608.10171 |
| Code | None found at Phase-0 (no public repo) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.10171-generating-attacks-for-llms-with-gflownets.pdf` |
| Retrieved | 2026-08-12 |
| Read status | read (4 pp workshop) |

## Narrative

Trains a GFlowNet-based **attacker LLM** to generate diverse, high-success adversarial prompts against a victim LLM, using a third model as evaluator (attacker → victim → evaluator reward loop). Pipeline = dataset construction → SFT into an "attack specialist" persona → GFlowNet diversity-seeking sampling → MLE smoothing toward high-reward samples.

| Dataset | Size |
|---------|------|
| Lee et al. (ICLR 2025) source | combined open-source |
| Turkish translation | direct translation |
| Expanded | cosine-similarity dedup → 2,500 disjoint + 600 self-built manipulations = 3,100 |
| Turkish translation of expanded | — |

Key result (attacker Qwen3-1.7b, victim Gemma3-4b, classifier Qwen3Guard-8b):

| Config | Similarity ↓ | Toxicity | Success Rate |
|--------|-------------|----------|--------------|
| SFT only | 0.62 | 0.14 | 0.08 |
| SFT + GFN + MLE | 0.54 | 0.71 | 0.79 |

- **Transferability:** English attacks keep high success when the victim scales Gemma3-4b → Gemma3-12b; Turkish attacks lose substantially (lower diversity in the Turkish attack set → higher similarity).
- **Evaluator choice:** in Turkish, LlamaGuard3-8b-trained attacker is more successful but less creative; in English, Qwen3Guard-trained attacker is more successful, LlamaGuard-trained is more creative.
- **Novelty:** first reported Turkish-language GFlowNet attack-generation model.

`[TENTATIVE]` — single workshop paper, small models (1.7b attacker / 4b victim), no public code; numbers are paper-reported.

## Snippets

> Existing automated methods suffer from limited creativity due to their inherent dependency on fixed datasets. ... this research aims to generate more effective adversarial attacks in English compared to existing benchmarks and, as a novel contribution to the literature, introduces a model capable of generating attack inputs in the Turkish language. [Source: arXiv:2608.10171 abstract]

> (SFT only → SFT+GFN+MLE): Similarity 0.62→0.54, Toxicity 0.14→0.71, Success Rate 0.08→0.79. [Source: arXiv:2608.10171 Table I]

## Dead Ends

- No public code / weights at Phase-0 → **REFERENCE** only; cannot reproduce Table I in-lab without re-implementing the Lee et al. base method.
- Small-model setup (Qwen3-1.7b attacker, Gemma3-4b victim) — headline numbers are a lower bound for what a larger attacker would achieve; do not extrapolate to frontier models.
- Evaluator-model quality directly bounds measured success rate — treat ASR as co-determined by the classifier, not just the attacker.
