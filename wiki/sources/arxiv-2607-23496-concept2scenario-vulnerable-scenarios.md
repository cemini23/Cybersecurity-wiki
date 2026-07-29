---
title: Do LLMs know their vulnerable scenarios / Concept2Scenario (arXiv 2607.23496)
type: source
tags: [source, arxiv, jailbreak, interpretability, red-teaming]
keywords: [2607.23496, Concept2Scenario, SAE, refusal direction, scenario framing]
related:
  - concepts/concept2scenario-refusal-suppression.md
  - concepts/pair-prompt-pattern.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-29
updated: 2026-07-29
phase_0_verdict: "REFERENCE 2026-07-29 — no public code located; ACM preprint"
---

**Briefs:** `briefs/2026-07-29_k221-concept2scenario-prod.md`

## Relations

- @concepts/concept2scenario-refusal-suppression.md
- @concepts/pair-prompt-pattern.md
- @concepts/crescendo-multi-turn-jailbreak.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Do LLMs Know Their Vulnerable Scenarios? |
| Authors | Peng, Deng, Jin, Rong, Han, Teng, Wang, Zou, Hu |
| arXiv | 2607.23496 |
| Code | none located (preprint) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.23496-do-llms-know-their-vulnerable-scenarios.pdf` |
| Retrieved | 2026-07-29 |

## Narrative

Scenario-wrapped harmful requests activate internal **scenario directions** that causally reduce refusal. **Concept2Scenario**: SAE concept space → attribute refusal suppression → NL scenarios → interaction attribution for synergistic combinations. Up to **+18.2 pp ASR** on open models; transfers to GPT-5 / Claude-Haiku-4.5 / Gemini-3-Flash; combinations beat singles and shrink multi-turn attack budgets (PAIR etc.).

### Steal

1. Treat scenario framing as a first-class jailbreak prior — not just prompt mutators
2. Test synergistic scenario pairs, not only single wrappers
3. Reuse discovered scenarios as black-box priors against closed models

## Snippets

> "the discovered scenarios serve as reusable priors that improve average attack success rates by up to 18.2 percentage points."
[Source: arxiv-2607.23496 abstract]
