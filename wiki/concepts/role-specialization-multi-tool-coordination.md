---
title: "Role specialization for multi-tool LLM coordination — RSM and explicit tool responsibility domains"
type: concept
tags: [methodology, agentic-se, multi-agent, tool-coordination, mcp, coding-agent, prompt-hardening, orchestration]
keywords: [role specialization, RSM, multi-tool coordination, Architect/Analyst/Specialist, scope boundaries, role drift, workflow inertia, prompt hardening, model routing, ISO 25010, constraint-density]
related:
  - sources/arxiv-2608-12311-rsm-role-specialization.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-security-posture.md
  - concepts/coding-agent-context-pruning.md
  - concepts/multi-tool-threshold-mcp-poisoning.md
  - concepts/agent-skill-injection.md
  - sources/arxiv-2608-13476-marc-v1-clinical-multi-agent.md
  - entities/tools/marc-v1.md
  - concepts/deterministic-multi-agent-orchestration-failure-attribution.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-mcp-tool-control.mdc (K277)"
---

# Role specialization for multi-tool LLM coordination — RSM and explicit tool responsibility domains

## Relations

- @sources/arxiv-2608-12311-rsm-role-specialization.md — the source case study
- @concepts/agent-runtime-guardrails.md — role boundaries are a runtime-coordination guardrail; drift is a guardrail failure
- @concepts/mcp-security-posture.md — MCP admission + tool-allowlist terms; RSM assigns each admitted tool a distinct responsibility domain
- @concepts/coding-agent-context-pruning.md — context management is a named RSM challenge (project-state handoffs)
- @concepts/multi-tool-threshold-mcp-poisoning.md — more tools = more surface; specialization bounds how much authority any one tool silently accumulates
- @concepts/agent-skill-injection.md — a drifted/overlapping role is an injection amplifier (untrusted input routed to a tool doing a job it was not scoped for)

## Raw Concept

The question this page answers: when several LLM tools with different capabilities are available in one workflow, how do you keep each one doing what it is best at, and catch the drift when one tool silently absorbs another's role? Answer pattern: assign explicit, capability-matched responsibility domains (Architect/Analyst/Specialist), enforce scope boundaries between phases, treat role drift as a measured coordination failure, and keep human verification of agent outputs.

## Narrative

### The RSM pattern

Separation-of-concerns applied to tools instead of code: each tool gets a distinct responsibility domain based on its actual capability profile, execution modality, and privacy properties. The reference case: Antigravity (agentic IDE, cloud) = **Architect** (multi-file generation, macro vision), Gemini CLI (terminal, cloud) = **Analyst** (bulk processing, docs, architectural audit), Qwen Code (local Ollama) = **Specialist** (validation, unit tests, sensitive-data privacy from local execution).

### Why role drift is the core failure mode

The main observed deviation was one tool spontaneously assuming another's refactoring role. Three compounding factors:
1. **Absent scope boundaries** — no explicit boundary between phases, so the tool implemented improvements it was not asked for.
2. **Functional overlap** — two tools with overlapping capabilities (both Gemini-backed here) blur the boundary; model homogeneity reduces cognitive diversity and makes overlap more likely.
3. **Workflow inertia** — once a tool has the context, switching costs (re-establishing project state, describing completed work, verifying cross-tool consistency) outweigh the benefit of restoring the planned distribution.

The lesson generalizes to MCP-heavy harnesses: **do not let one tool absorb all roles silently.** If the coding agent also does the audit, the review, and the config edit, you lose the separation that makes failures attributable — and you widen the injection blast radius, because untrusted input can be routed to a tool doing a job it was never scoped for.

### Supporting findings that transfer

- **Constraint-density degradation** (AGENTIF): agents fail more as simultaneous instruction count grows; explicit *negative* constraints ("DO NOT run commands, use tools, or create the file") are the prompt-hardening technique that pinned the CSV-generation task.
- **CoT reasoning paradox**: explicit chain-of-thought can degrade simple instruction-following by redirecting attention — the agent deprioritized a date-format constraint while focused on structural reasoning. Separating format-constraint prompts from task-generation prompts is the suggested mitigation.
- **Failure-backed instructions** (ETH AGENTS.MD eval): overly detailed project-rule files reduce success rates and raise inference cost; add rules only when a recurrent error is demonstrated without them.
- **LLMOps patterns**: prompts-as-code (versioned in Git), deterministic-plan/probabilistic-execution separation, and intelligent model routing (small local models for routine tasks, cloud for architectural change).

### Authorized-use framing

Role specialization is an orchestration/coordination principle for agent harnesses — directly applicable to this wiki's own MCP/tool-control posture (which tool may do what, under what scope). It is also a defensive evaluation lens: in a multi-tool agent pentest, role drift is a signal that scope boundaries are weak. Nothing here is a live-attack capability; it's harness design and evaluation (K277).

## Snippets

> The role distribution among LLM agents tends to adapt dynamically, placing on the human orchestrator the responsibility of actively intervening when the planned distribution is deemed important. [Source: arXiv:2608.12311 p.12]

> The most relevant patterns... are: (a) prompts as code; (b) separation between deterministic planning and probabilistic execution; (c) intelligent model routing: delegating routine tasks to small local models while reserving powerful cloud models for global architectural changes. [Source: arXiv:2608.12311 p.15]

## Dead Ends

- The paper is a single exploratory case — no controlled replication; role-drift generalizability is not established.
- Qualitative ISO/IEC 25010 ratings are author judgment, not tool-supported measurement; the 2023 edition (with Safety) is recommended for future replication.
- Two of three tools shared the Gemini backend — the observed overlap may partly be a model-homogeneity artifact rather than a general RSM property.
