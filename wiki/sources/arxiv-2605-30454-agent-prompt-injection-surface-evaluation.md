---
title: "The Surface You Test Is Not the Surface That Breaks (arXiv:2605.30454)"
type: source
tags: [arxiv, agent-security, prompt-injection, evaluation, mcp, research-paper]
keywords: [adaptive attack rate, tool description injection, tool output injection, per-surface asr, emnlp]
related:
  - concepts/agent-runtime-guardrails.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/llm-pentest-automation.md
  - sources/arxiv-2606-00485-confused-chatgpt-cross-app-context-poisoning.md
  - sources/arxiv-2606-02240-agentredbench.md
  - sources/arxiv-2606-02302-seclaw-spec-driven-agent-security.md
  - sources/arxiv-2606-02822-owasp-llm-defense-attribution.md
  - entities/tools/llm-defense-lattice.md
maturity: draft
read_status: read
created: 2026-06-01
updated: 2026-06-04
---

## Relations

- @concepts/agent-runtime-guardrails.md — dual-surface injection + Adaptive Attack Rate evaluation method
- @concepts/llm-adversarial-fuzzing.md — fixed-channel eval overstates robustness
- @concepts/llm-pentest-automation.md — agent eval methodology for pentest copilots

## Raw Concept

- **Title**: The Surface You Test Is Not the Surface That Breaks
- **Authors**: Shifat E Arman et al. (University of Dhaka)
- **Type**: arXiv preprint (EMNLP under review)
- **Location**: `raw-sources/arxiv-2605.30454-the-surface-you-test-is-not-the-surface-that-bre.pdf`
- **URL**: https://arxiv.org/abs/2605.30454
- **Retrieved**: 2026-06-01
- **Read-status**: read

## Narrative

Tool-augmented agents have (at least) two injection surfaces: **tool outputs** (data) and **tool descriptions** (schema read every turn). Same payload byte-identical inverts ASR across models (e.g. GPT-4.1 96% output vs 4% description; Gemini-3-Flash mirror). Variance decomposition (6,830 attempts): model×surface interaction 16.7%; surface alone 0%. **Adaptive Attack Rate (AAR)** = per-cell max over surfaces; beats best fixed surface by +9.1 pp on average. Standard defenses reduce output ASR but leave description channel >54%.

## Snippets

> "Vulnerability is a property of the pairing, not the channel."

> "Both attack and defense evaluation must report per-surface vulnerability."
