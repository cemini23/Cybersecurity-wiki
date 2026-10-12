---
title: "A passing generated test is not a discriminating test (K422)"
type: concept
tags: [concept, agent-security, k422]
keywords: [2610.13811, K422]
related:
  - sources/arxiv-2610-13811-qtestbench-llm-quantum-code-tests.md
  - concepts/llm-generated-dependency-breaking-tests.md
  - concepts/code-monitor-red-teaming-public-tests.md
  - concepts/llm-vuln-repair-metrics-audit.md
  - concepts/verification-generation-gap.md
maturity: draft
created: 2026-10-12
updated: 2026-10-12
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K422)"
---

## Relations

- @sources/arxiv-2610-13811-qtestbench-llm-quantum-code-tests.md
- @concepts/llm-generated-dependency-breaking-tests.md
- @concepts/code-monitor-red-teaming-public-tests.md
- @concepts/llm-vuln-repair-metrics-audit.md
- @concepts/verification-generation-gap.md

## Raw Concept

Question: **A passing generated test is not a discriminating test** — operator steal from arXiv 2610.13811?

## Narrative

An LLM-written test suite that runs and passes tells you almost nothing: the question is whether it **separates a correct implementation from a faulty one**. QTestBench makes that the metric — inject candidate solutions, compare each test's verdict to an **independent oracle's** label, and never treat the generated tests as ground truth. The gap is large: suites **almost always execute**, yet the best model reaches test quality **0.71** on one benchmark and **0.34** on another, so **executability overstates quality**.

Two concrete failure modes to check for: a **too-weak** test that only verifies the entry point and so passes a wrong solution, and a **too-strict** test whose tolerance (e.g. 1e-4) fails a correct one. When natural faulty solutions are rare — true for three of ten Qiskit tasks — **oracle-verified synthetic mutants** restore a stable bug-detection estimate. Operator rule: for any agent that writes its own tests, **score the tests against an external oracle and report accept-correct and reject-incorrect separately**. Pairs K300 (dependency-breaking tests) and K413 (the verification-generation gap).

## Snippets

> See arXiv 2610.13811 abstract. [Source: arXiv 2610.13811 (retrieved 2026-10-12)]
