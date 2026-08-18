---
title: Faithful agent ASR measurement — exposure / execution / observation / adjudication
type: concept
tags: [concept, agent-security, red-team, evaluation, faithful-measurement]
keywords: [ASR, exposure, execution, observation, adjudication, Recognition-Execution Gap, REG, trajectory vs state judge, harness-dependent, evaluation cue]
related:
  - sources/arxiv-2608-10669-redagentbench-faithful-agent-asr.md
  - entities/tools/redagentbench.md
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/agent-data-injection-attacks.md
  - concepts/safety-harness-evolution.md
  - concepts/ai-for-cybersecurity.md
  - sources/arxiv-2608-12996-atobench-deceptive-observations.md
  - concepts/atobench-verification-chain-deception.md
  - sources/arxiv-2608-12880-labels-not-endpoints.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - sources/arxiv-2608-15578-arena-audio-lalm-redteam.md
  - concepts/audio-grounded-lalm-redteaming.md
  - sources/arxiv-2608-16747-chive-counterfactual-explanations.md
  - concepts/counterfactual-simulatability-llm-explanations.md
  - sources/arxiv-2608-16795-ood-historical-backtesting-astronomy.md
maturity: draft
created: 2026-08-12
updated: 2026-08-15
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc + cemin-cybersec-agent-audit.mdc (K271)"
---

## Relations

- @sources/arxiv-2608-10669-redagentbench-faithful-agent-asr.md
- @entities/tools/redagentbench.md
- @concepts/agent-runtime-guardrails.md
- @concepts/ai-redteam-evidential-ceiling.md
- @concepts/agent-data-injection-attacks.md
- @concepts/safety-harness-evolution.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

A single attack-success-rate (ASR) number for tool-using LLM agents is meaningless without its measurement conditions. REDAgentBench 2608.10669 formalizes reported ASR as an **exposure → execution → observation → adjudication** pipeline and shows that changing the harness, the evidence view, or the evaluation cue can reverse model rankings or flip verdicts on the *same* rollout.

## Narrative

**Cybersec takeaway:** whenever you red-team an agent system, report ASR as a **tuple**, not a scalar — `(harness, judging configuration, evaluation cue, judge backbone)` — and prefer **state-grounded** verification (service receipts / final-state diffs) over trajectory self-report. Trajectory-only judging systematically misses durable harm: an agent can *say* "I will not merge" and then *click merge* (the Recognition–Execution Gap), or leak a key that only shows up in service records.

Three failure modes REDAgentBench pins down:
1. **Harness-dependence:** the same model+case can swing from ~40% to ~95% ASR purely from the agent harness (tool mediation, turn construction, runtime control). Never compare agent safety across papers without the harness.
2. **Evidence-view bias:** state judging runs 7.7–11.7 pp higher than trajectory judging and re-labels 13–21% of paired rollouts. The trajectory transcript is a *claim*; the service receipt is a *record*.
3. **Evaluation-awareness leak:** telling the agent it is being evaluated in a mock sandbox lowers ASR by ~5–7 pp on average (not uniformly) — evaluation cues are an experimental variable, not a constant.

**Diagnostic + defense:** the Recognition–Execution Gap (agent states the constraint, then violates it) motivates an **action-time policy reminder** — restating the applicable safety rule at the action boundary. Paper reports a 74-pp confirmed-violation reduction in matched replay; a cheap, training-free intervention worth stealing into lab harnesses (`agent-runtime-guardrails`).

Do not adopt REDAgentBench as a runtime gate; it is an **evaluation/instrumentation pattern** (REFERENCE until the benchmark ships). Authorized lab only when running executable agent red-teaming.

## Snippets

> An ASR number is meaningful only with its measurement conditions. ... this turns cross-paper comparisons into structured statements — "harness A under judging configuration B and cue C, using backbone D, scores X". [Source: arXiv:2608.10669 §5]

## Dead Ends

- Cannot reproduce locally yet (benchmark unreleased). Treat the 65.69% macro-ASR and the 74-pp reminder effect as paper-reported pending independent rerun.
- Recognition labels require the "resolved action anchor" sub-cohort; 331 unresolved executions were excluded — REG percentages are for the resolved subset, with conservative full-cohort lower bounds (16.05% / 4.91%).
