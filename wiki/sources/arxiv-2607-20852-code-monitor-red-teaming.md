---
title: Code Monitor Red Teaming for public-test-passing code (arXiv 2607.20852)
type: source
tags: [source, arxiv, code-security, red-team, llm-verifier]
keywords: [2607.20852, CodeMonitorBench, public tests, hidden bugs, weak-to-strong]
related:
  - concepts/code-monitor-red-teaming-public-tests.md
  - concepts/llm-code-review-agent-security.md
  - concepts/llm-vulnerability-discovery.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-24
updated: 2026-07-24
phase_0_verdict: "REFERENCE 2026-07-24 — CodeMonitorBench protocol; no public code located"
---

**Briefs:** `briefs/2026-07-24_k216-code-monitor-red-teaming-prod.md`

## Relations

- @concepts/code-monitor-red-teaming-public-tests.md
- @concepts/llm-code-review-agent-security.md
- @concepts/llm-vulnerability-discovery.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Code Monitor Red Teaming for Public-Test-Passing Code |
| Authors | Liao, Deng, Ren (UESTC) |
| arXiv | 2607.20852 |
| Code | none located |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.20852-code-monitor-red-teaming-for-public-test-passing.pdf` |
| Retrieved | 2026-07-24 |

## Narrative

Passing **public tests ≠ specification correctness**. Protocol: after public-test pass, can a **weaker LLM verifier** catch residual hidden bugs? **CodeMonitorBench** (function / data-science / workflow).

### Headline [CONFIRMED abstract]

| Stat | Value |
|------|-------|
| Candidates | 71,000 |
| Pass public | 43,677 |
| Of those, fail hidden | 23,810 |
| Weak verifiers @ 5% FPR | still miss **most** hidden bugs |
| Adversarial public-test-overfit | lowers AUROC / raises low-FPR miss |

### Steal

1. Merge gates that only run public tests are insufficient — need hidden/spec oracles or stronger monitors
2. Weak-to-strong monitor eval with fixed public-check information boundary
3. Stress with public-test-overfit generators

## Snippets

> "Across 71,000 generated candidates, 43,677 pass public tests and 23,810 of those fail hidden tests. Weak verifiers… still miss most hidden bugs at 5% false-positive rate."
[Source: arxiv-2607.20852 abstract]
