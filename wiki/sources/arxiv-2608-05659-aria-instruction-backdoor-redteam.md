---
title: ARIA instruction-backdoor red teaming for customized coding LLMs (arXiv 2608.05659)
type: source
tags: [source, arxiv, llm-security, red-teaming, backdoor, coding-agents, lab]
keywords: [2608.05659, ARIA, instruction backdoor, customized LLM, code intelligence]
related:
  - concepts/aria-instruction-backdoor-redteam.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/piminer-agentic-prompt-injection-redteam.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-08-07
updated: 2026-08-07
phase_0_verdict: "REFERENCE 2026-08-07 — no public ARIA code/LICENSE found; lab methodology only"
wire_status: wont_wire
wire_target: "policy pattern only — no runtime"
---

**Briefs:** `briefs/2026-08-07_k249-aria-prod.md`

## Relations

- @concepts/aria-instruction-backdoor-redteam.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/piminer-agentic-prompt-injection-redteam.md
- @concepts/local-abliterated-llm-pentest-stack.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Breaking Customized LLMs for Coding: Automated Red Teaming for Instruction Backdoor Attacks |
| Authors | Yuchen Chen, Wei Cheng, Yuan Xiao, Weisong Sun, Chunrong Fang, Yang Liu, Zhenyu Chen, Baowen Xu |
| arXiv | 2608.05659 |
| Code | none found (Phase-0 2026-08-07) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.05659-breaking-customized-llms-for-coding-automated-re.pdf` |
| Retrieved | 2026-08-07 |

## Narrative

Customized coding LLMs (system-prompt / instruction embedding without weight change) are an **instruction-backdoor** surface. **ARIA** automates covert backdoored instructions via an attacker LLM with multi-axis feedback (stealth, clean utility, backdoor ASR). Reports ASR up to 0.945, strong detection evasion (FNR up to 1.0), robustness across languages/temperature. [CONFIRMED abstract]

### Steal

1. Red-team customized coding assistants for instruction backdoors — not only weight-poison / PI
2. Score **stealth + clean utility + ASR** together; single-metric ASR is insufficient
3. Lab / written-scope only; do not implant backdoors in third-party platforms

## Snippets

> "we propose ARIA, an automated red-teaming framework for crafting covert and effective backdoored instructions against customized LLMs."
[Source: arXiv 2608.05659 abstract]
