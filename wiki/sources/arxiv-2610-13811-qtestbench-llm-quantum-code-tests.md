---
title: "QTestBench: a test framework for evaluating LLM-generated quantum code"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.13811, k422]
related:
  - concepts/llm-generated-test-discrimination.md
  - concepts/llm-generated-dependency-breaking-tests.md
  - concepts/code-monitor-red-teaming-public-tests.md
  - concepts/llm-vuln-repair-metrics-audit.md
  - concepts/verification-generation-gap.md
maturity: draft
read_status: read
created: 2026-10-12
updated: 2026-10-12
phase_0_verdict: "REFERENCE 2026-10-12 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K422)"
---

## Relations

## Relations

- @concepts/llm-generated-test-discrimination.md
- @concepts/llm-generated-dependency-breaking-tests.md
- @concepts/code-monitor-red-teaming-public-tests.md
- @concepts/llm-vuln-repair-metrics-audit.md
- @concepts/verification-generation-gap.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | QTestBench: a test framework for evaluating LLM-generated quantum code |
| arXiv | 2610.13811 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.13811-qtestbench-a-test-framework-for-evaluating-llm-g.pdf |
| Retrieved | 2026-10-12 |
| Read status | read |

## Narrative

**K422 — a generated test that passes is not a test that discriminates.** LLMs now write the unit tests that guard code, but a suite that **accepts incorrect code is worse than no test at all** — and on quantum software, where outputs are probabilistic, tolerances matter, and correctness is defined by **domain-specific checkers**, a well-formed test can still disagree with the benchmark's own verdict. **QTestBench** prompts models to produce syntactic, semantic, and behavioral tests, injects candidate solutions at runtime, and scores each test **against an independent benchmark checker — never against the tests themselves.**

Over five LLMs, eight **PennyLane QHack** challenges and ten **Qiskit HumanEval** tasks: generated suites **almost always execute**, but **discrimination lags** — best test quality **0.71** on QHack and **0.34** on Qiskit HumanEval, so **executability alone overstates quality**. Two failure modes are named: **too weak** (checks only that the entry point exists, passes a wrong solution) and **too strict** (a 1e-4 tolerance fails a correct implementation). **Oracle-verified synthetic mutants** stabilise bug-detection estimates when natural faulty solutions are scarce — on three of ten Qiskit tasks there are **none**. Repo `github.com/eBrain4Everyone/QTestBench`; licence not stated. Operator steal: **score generated tests against an independent oracle, measure accept-correct AND reject-incorrect, and use synthetic mutants when negatives are rare.** Pairs K300 and K413.

## Snippets

> See arXiv 2610.13811 abstract. [Source: arXiv 2610.13811 (retrieved 2026-10-12)]
