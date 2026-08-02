---
title: "GitHub — tcpiplab/AblitaFuzzer (abliterated attacker LLM)"
type: source
tags: [source, github, llm, abliteration, pentest, ollama]
keywords: [AblitaFuzzer, abliterated, Ollama, LLM pentest, attacker model]
related:
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/llm-adversarial-fuzzing.md
  - entities/tools/ollama.md
maturity: draft
created: 2026-08-02
updated: 2026-08-02
read_status: skimmed
---

## Relations

- @concepts/local-abliterated-llm-pentest-stack.md — local abliterated attacker-model pattern
- @concepts/llm-adversarial-fuzzing.md — adversarial LLM testing methodology
- @entities/tools/ollama.md — typical local host for the attacker model

## Raw Concept

| Field | Value |
|-------|--------|
| Title | AblitaFuzzer — abliterated local LLM for generating attack prompts against target LLM APIs |
| URL | https://github.com/tcpiplab/AblitaFuzzer |
| Retrieved | 2026-08-02 |
| Read-status | skimmed |

## Narrative

Uses a local Ollama-hosted abliterated model as the **attacker** to generate novel prompts, then probes a remote **target** LLM API. Relevant as a consumer pattern for @concepts/local-abliterated-llm-pentest-stack.md (authorized LLM engagements only — not a general web pentest scanner).
