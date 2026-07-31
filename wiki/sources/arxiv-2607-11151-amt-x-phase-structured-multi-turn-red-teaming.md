---
title: AMT-X — phase-structured multi-turn red-teaming (arXiv 2607.11151)
type: source
tags: [source, arxiv, llm-security, multi-turn, red-teaming, jailbreak, evaluation]
keywords: [2607.11151, amt-x, adaptive multi-turn exploitation, checklist-gated, full asr, overall asr, vulcan]
related:
  - concepts/amt-x-phase-structured-multi-turn-red-teaming.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/pair-prompt-pattern.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/layer-paradigm-agent-red-teaming.md
  - concepts/ai-for-cybersecurity.md
  - entities/tools/fuzzyai.md
maturity: draft
read_status: read
created: 2026-07-16
updated: 2026-07-31
phase_0_verdict: "REFERENCE 2026-07-16 — methodology paper; no public attack harness repo in abstract; steal dual-metric ASR + phase state machine"
wire_status: wont_wire
wire_target: "REFERENCE — no public harness"
---

**Briefs:** `briefs/2026-07-16_amt-x-checklist-gated-asr-handoff.md`, `briefs/2026-07-16_k175-amt-x-checklist-gated-asr-prod.md`

## Relations

- @concepts/amt-x-phase-structured-multi-turn-red-teaming.md — synthesis
- @concepts/crescendo-multi-turn-jailbreak.md — prior multi-turn escalation baseline AMT-X cites
- @concepts/pair-prompt-pattern.md — single-turn iterative baseline AMT-X contrasts

## Raw Concept

| Field | Value |
|-------|-------|
| Title | AMT-X: A Phase-Structured Multi-Turn Red-Teaming Framework with Checklist-Gated Dual-Metric Evaluation for LLM Safety |
| Authors | Yi Ting Shen, Kentaroh Toyoda, Alex Leung |
| Affiliation | Vulcan Research, AIFT, Singapore |
| arXiv | 2607.11151 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.11151-amt-x-phase-structured-multi-turn-red-teaming-wi.pdf` |
| Retrieved | 2026-07-16 |
| Read status | **read** (framework + dual ASR + phase machine; 35 pp) |

## Narrative

AMT-X (Adaptive Multi-Turn Exploitation) treats multi-turn jailbreaks as an explicit **multi-phase state machine** (P0–P4) with a library of **31 techniques**, semantic-simulation before each attacker turn, and a **multi-role jury** with phase-conditioned checklists.

### Dual ASR [CONFIRMED from paper]

| Metric | Gate | Reported range (6 frontier victims × 7 Moderation categories) |
|--------|------|--------------------------------------------------------------|
| **Overall ASR** | ≥1 critical actionability item | **97.6–100%** |
| **Full ASR** | all critical items (complete, real, operational detail) | **66.7–78.6%** (mean **71.4%**) |

Gap up to **33 pp** between partially and fully actionable harm — single-number ASR hides this. [Source: arXiv 2607.11151 abstract]

### Steal for Cemini

1. Always report **overall vs full** ASR on jailbreak / agent red-team evals
2. Prefer **phase-structured** attack plans over free-form Crescendo-style improvisation when reproducibility matters
3. Jury + checklist gates beat single LLM judge for production triage

### Phase-0 (2026-07-16)

| Gate | Status |
|------|--------|
| Public code | **NONE found** in paper front matter |
| Domain fit | Core LLM safety + agent chat eval |
| Verdict | **REFERENCE** — methodology steal only |

## Snippets

> "AMT-X attains overall attack success rates of 97.6–100% under a lenient score threshold, but 66.7–78.6% under a stricter gate requiring complete, real, and operational detail: a gap of up to 33 percentage points."
[Source: arxiv-2607.11151 abstract]
