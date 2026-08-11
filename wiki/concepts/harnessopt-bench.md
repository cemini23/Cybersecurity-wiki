---
title: HarnessOpt-Bench — evaluating LLMs at harness optimization
type: concept
tags: [concept, agent-harness, evaluation]
keywords: [HarnessOpt-Bench, harness optimization, 2608.06301, Scale]
related:
  - sources/arxiv-2608-06301-harnessopt-bench.md
  - concepts/llm-pentest-automation.md
  - concepts/self-evolving-agent-security.md
  - concepts/ai-for-cybersecurity.md
  - concepts/blast-radius-reversible-context-eviction.md
  - sources/arxiv-2608-09885-she-safety-harness-evolution.md
  - concepts/safety-harness-evolution.md
  - entities/tools/she-safety-harness-evolution.md
maturity: draft
created: 2026-08-07
updated: 2026-08-11
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc"
---

## Relations

- @sources/arxiv-2608-06301-harnessopt-bench.md
- @concepts/llm-pentest-automation.md
- @concepts/self-evolving-agent-security.md
- @concepts/ai-for-cybersecurity.md
- @concepts/blast-radius-reversible-context-eviction.md
- @sources/arxiv-2608-09885-she-safety-harness-evolution.md — safety-flavored harness optimization with validity check + safety-utility selection
- @concepts/safety-harness-evolution.md — SHE is the safety instance of the harness-opt protocol
- @entities/tools/she-safety-harness-evolution.md — local Apache-2.0 adopt (lab shelf)

## Raw Concept

Protocol for measuring how well an LLM-as-optimizer improves another agent’s harness under budgeted, held-out evaluation.

## Narrative

Relevant to Cemini/Cursor harness tuning and self-improving agent risk. Prefer explicit eval boundaries + version audit over unbounded self-modify. No public bench to wire — steal the protocol. [CONFIRMED]
