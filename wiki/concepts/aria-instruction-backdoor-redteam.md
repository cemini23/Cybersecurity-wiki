---
title: ARIA — instruction-backdoor red teaming for customized coding LLMs
type: concept
tags: [concept, llm-security, red-teaming, backdoor, coding-agents, lab]
keywords: [ARIA, instruction backdoor, customized LLM, 2608.05659]
related:
  - sources/arxiv-2608-05659-aria-instruction-backdoor-redteam.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/piminer-agentic-prompt-injection-redteam.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-08-07
updated: 2026-08-07
---

## Relations

- @sources/arxiv-2608-05659-aria-instruction-backdoor-redteam.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/piminer-agentic-prompt-injection-redteam.md
- @concepts/local-abliterated-llm-pentest-stack.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

Automated red team for **instruction-level backdoors** in customized coding LLMs (system-prompt customization platforms), not weight poisoning.

## Narrative

Complements PIMiner (prompt-injection) and DataShield/Gradient Immunity (fine-tune poisoning). Threat model: malicious or compromised custom instructions that preserve clean-task utility while triggering harmful code behaviors. Eval needs dual/triple metrics (ASR, utility, stealth). Authorized labs only — no LIVE third-party customization platforms. [CONFIRMED]
