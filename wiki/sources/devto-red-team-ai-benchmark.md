---
title: "DEV — Red Team AI Benchmark (uncensored LLMs)"
type: source
tags: [source, llm, red-team, benchmark, ollama]
keywords: [red team AI benchmark, uncensored LLM, Ollama, ADCS, EDR, refusal]
related:
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-08-02
updated: 2026-08-02
read_status: skimmed
---

## Relations

- @concepts/local-abliterated-llm-pentest-stack.md — benchmark caution (refusal-free ≠ accurate)
- @concepts/ai-for-cybersecurity.md — LLM × security context

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Red Team AI Benchmark: Evaluating Uncensored LLMs for Offensive Security |
| Author | toxy4ny (DEV Community) |
| URL | https://dev.to/toxy4ny/red-team-ai-benchmark-evaluating-uncensored-llms-for-offensive-security-1fol |
| Retrieved | 2026-08-02 |
| Read-status | skimmed |

## Narrative

Fixed 12-question offensive-security quiz (ADCS, NTLM relay, EDR, shellcode, etc.) run via Ollama/LM Studio. Shows wide score variance across “uncensored” models — supports the wiki claim that low refusal does not imply lab-validated accuracy. Scores are volatile; treat as methodology, not leaderboard truth.
