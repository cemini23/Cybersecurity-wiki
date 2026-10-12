---
title: Code monitor red-teaming (public-test-passing code)
type: concept
tags: [concept, code-security, red-team, monitoring]
keywords: [CodeMonitorBench, public tests, hidden bugs, weak verifier, 2607.20852]
related:
  - concepts/llm-generated-test-discrimination.md
  - sources/arxiv-2610-13811-qtestbench-llm-quantum-code-tests.md
  - concepts/llm-vulnerability-discovery.md
  - sources/arxiv-2607-20852-code-monitor-red-teaming.md
  - concepts/llm-code-review-agent-security.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-07-24
updated: 2026-10-12
---

## Relations

- @concepts/llm-generated-test-discrimination.md — K418-K424 ingest / 2026-10-12
- @sources/arxiv-2610-13811-qtestbench-llm-quantum-code-tests.md — K418-K424 ingest / 2026-10-12
- @concepts/llm-vulnerability-discovery.md — K408-K417 ingest / 2026-10-09
- @sources/arxiv-2607-20852-code-monitor-red-teaming.md
- @concepts/llm-code-review-agent-security.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

Can a weaker monitor catch hidden bugs **after** public tests pass?

## Narrative

~55% of public-test-passers still fail hidden tests (23810/43677). Weak monitors miss most at 5% FPR; adversarial overfit pressure worsens AUROC. Merge-gate implication: public CI ≠ correctness. [CONFIRMED abstract]
