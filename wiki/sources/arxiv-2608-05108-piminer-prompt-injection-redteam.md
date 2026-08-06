---
title: PIMiner agentic prompt-injection red teaming (arXiv 2608.05108)
type: source
tags: [source, arxiv, agent-security, prompt-injection, red-teaming, lab]
keywords: [2608.05108, PIMiner, prompt injection, IPIArena, AgentDojo, strategy library]
related:
  - concepts/piminer-agentic-prompt-injection-redteam.md
  - entities/tools/piminer.md
  - concepts/prompt-injection-detector-calibration.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/openart-environment-evolution-agent-redteam.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-08-06
updated: 2026-08-06
phase_0_verdict: "CONDITIONAL-GO 2026-08-06 — MIT; ~28MB; lab red-team only; Claude Code CLI required"
wire_status: deferred
wire_target: "lab sandbox only — no Cursor alwaysApply / no LIVE"
---

**Briefs:** `briefs/2026-08-06_k248-piminer-prod.md`

## Relations

- @concepts/piminer-agentic-prompt-injection-redteam.md
- @entities/tools/piminer.md
- @concepts/prompt-injection-detector-calibration.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/openart-environment-evolution-agent-redteam.md
- @concepts/crescendo-multi-turn-jailbreak.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Agent Against Agent: An Agentic System for Automatic Prompt Injection Red Teaming |
| Authors | Yanting Wang, Chenlong Yin, Runpeng Geng, Jinyuan Jia |
| arXiv | 2608.05108 |
| Code | https://github.com/Wang-Yanting/PIMiner (MIT) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.05108-agent-against-agent-an-agentic-system-for-automa.pdf` |
| Retrieved | 2026-08-06 |

## Narrative

RL-trained prompt-injection attackers often fail to transfer to new target LLMs. **PIMiner** trains an agentic attacker that builds a **strategy library** across (dataset, target) pairs and transfers the library at test time without retraining; ~10 queries/sample. Reports strong ASR on IPIArena and AgentDojo vs Gemini-2.5-Pro / GPT-5.1 / Claude-Sonnet-4.5. Implementation drives attacker via **Claude Code** sessions. [CONFIRMED abstract + README]

### Steal

1. Prefer transferable strategy libraries over single-target RL attackers
2. Lab-only against owned agents; written scope; dual metrics (overall vs full ASR)
3. Human gate: Claude Code CLI + target API keys — do not host-install until asked

## Snippets

> "At test time, the learned strategy library can be directly transferred to a previously unseen target LLM without additional training."
[Source: arXiv 2608.05108 abstract]
