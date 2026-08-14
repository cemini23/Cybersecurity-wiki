---
title: "Deterministic multi-agent orchestration + stage-wise failure attribution (MARC pattern)"
type: concept
tags: [concept, multi-agent, orchestration, llm, architecture, attribution, k279]
keywords: [deterministic orchestration, stage-wise failure attribution, MARC, Decomposer, YAML agents, explicit context passing, Level-2 autonomy, role coordination, clinical AI]
related:
  - sources/arxiv-2608-13476-marc-v1-clinical-multi-agent.md
  - entities/tools/marc-v1.md
  - concepts/role-specialization-multi-tool-coordination.md
  - concepts/agent-runtime-guardrails.md
  - concepts/llm-pentest-automation.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-mcp-tool-control.mdc (K279) — clinical runtime wont_wire"
---

## Relations

- @sources/arxiv-2608-13476-marc-v1-clinical-multi-agent.md — source paper + MIT repo (GO clone)
- @entities/tools/marc-v1.md — entity page
- @concepts/role-specialization-multi-tool-coordination.md — RSM (K277); roles across tools vs deterministic stages within one harness
- @concepts/agent-runtime-guardrails.md — stage-wise attribution is itself a guardrail: it localizes failures and injection effects
- @concepts/llm-pentest-automation.md — pentest-agent harnesses need the same auditable-stage property

## Raw Concept

When a multi-agent run fails, who is to blame? Monolithic single-prompt LLM systems conflate extraction, reasoning, and answer generation, so a failure anywhere looks like a failure everywhere. MARC's pattern: **deterministic sequential orchestration of role-specialized agents with explicit context passing**, so each stage's output is inspectable and failures are attributable to a stage.

## Narrative

### The pattern

1. **Decompose the task into role-specialized stages** — extraction, reasoning, answer generation, evaluation (clinical example; the principle is domain-agnostic).
2. **Declare agents in YAML** (name, model, prompt file, optional RAG context) — reordering/adding agents needs no code.
3. **Explicit context passing** — each agent receives the original input + the preceding agent's output. No hidden state.
4. **Stage-wise failure attribution** — because outputs are traceable intermediates, an error localizes to the stage that produced it.
5. **Automated prompt generation (Decomposer)** — an LLM decomposes a plain-language task into a validated 3-agent pipeline spec (JSON), removing manual prompt engineering while enforcing structural constraints (`{input}`, `{previous_agent_output}` bindings, VERDICT formatting).
6. **Determinism** — greedy decoding (temperature 0) for repeatable runs.

### Why it matters for Cemini harnesses

- **Auditability** — a pentest or agent-security harness that traces evidence needs stage-level provenance; deterministic stages give you that for free.
- **Injection localization** — if one stage's output is poisoned, explicit context passing shows exactly which stage consumed it (pairs with `agent-runtime-guardrails`).
- **Complements RSM (K277)** — RSM assigns *roles across separate tools*; MARC assigns *stages within one orchestration*. Together they cover the two failure axes: cross-tool role drift + within-harness stage attribution.

### Boundaries

- MARC is clinically validated; **clinical runtime wont_wire** (no patient data in scope).
- It is a **clone-for-reference** (MIT, 20MB shallow) — pattern source, not a runtime dependency. Do not wire `marc` into preflight as a service.

## Snippets

> MARC runs a sequence of role-specialized agents that pass context explicitly, so each stage of the reasoning process can be inspected on its own. [Source: README, github.com/Penn-RAIL/MARC-v1]
