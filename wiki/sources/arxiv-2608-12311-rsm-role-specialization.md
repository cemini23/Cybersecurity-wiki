---
title: "RSM — Role Specialization Model for coordinating LLM tools in agentic software engineering (arXiv 2608.12311)"
type: source
tags: [source, arxiv, agentic-se, multi-agent, tool-coordination, mcp, coding-agent, prompt-hardening]
keywords: [2608.12311, RSM, role specialization, multi-tool, agentic software engineering, SE 3.0, Antigravity, Gemini CLI, Qwen Code, Ollama, vibe coding, ISO 25010, constraint-density degradation]
related:
  - concepts/role-specialization-multi-tool-coordination.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-security-posture.md
  - concepts/coding-agent-context-pruning.md
  - concepts/multi-tool-threshold-mcp-poisoning.md
maturity: draft
read_status: read
created: 2026-08-13
updated: 2026-08-13
phase_0_verdict: "REFERENCE 2026-08-13 — Zenodo DOI (10.5281/zenodo.21076890) not registered at retrieval; code available from corresponding author on request; no public SPDX artifact. Framework steal-from for multi-tool role coordination. K277 policy wire."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-mcp-tool-control.mdc (K277)"
---

**Briefs:** `briefs/2026-08-13_k277-rsm-role-specialization.md`

## Relations

- @concepts/role-specialization-multi-tool-coordination.md
- @concepts/agent-runtime-guardrails.md — role boundaries are a runtime-coordination guardrail; unplanned role drift is the failure mode
- @concepts/mcp-security-posture.md — multi-tool admission/coordination in MCP terms; RSM assigns each tool a distinct responsibility domain
- @concepts/coding-agent-context-pruning.md — context management was a recurring RSM challenge (project-state descriptions fed to agents)
- @concepts/multi-tool-threshold-mcp-poisoning.md — the more tools in the loop, the more surface; role specialization reduces silent role-absorption by any one tool

## Raw Concept

| Field | Value |
|-------|-------|
| Title | The Role Specialization Model (RSM): Coordinating LLM-Based Tools in Agentic Software Development — An Exploratory Case Study |
| Authors | Carlos Alberto Fernández-y-Fernández (UTM, México); Jorge R. Aguilar Cisneros (UPAEP, México) |
| arXiv | 2608.12311 |
| Code | Zenodo DOI 10.5281/zenodo.21076890 (not registered at retrieval 2026-08-13); otherwise available from corresponding author on request |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.12311-the-role-specialization-model-rsm-coordinating-l.pdf` |
| Retrieved | 2026-08-13 |
| Read status | read (28 pp, full text extracted) |

## Narrative

The paper proposes and applies the **Role Specialization Model (RSM)**: coordinate multiple LLM-based development tools by assigning each a distinct, capability-matched responsibility domain (separation-of-concerns applied to tools rather than code), with the human developer as orchestrator. Exploratory single-case study on a Python desktop app (Climate Data Visualizer, Tkinter/Pandas/Matplotlib).

**Roles:** Antigravity (agentic IDE, Gemini backend) = **Architect** — multi-file generation, macro vision, iterative refinement; Gemini CLI = **Analyst** — bulk processing, documentation, architectural audit; Qwen Code (local via Ollama) = **Specialist** — validation, unit testing, sensitive-data privacy (local execution).

**Findings by research question:**
- **RQ1 (coordination):** RSM provided a structured basis; Antigravity generated 6 coherent project files from one natural-language prompt; Gemini CLI drove dataset generation, architectural audit (led to a DataModel MVC refactor), and docs; Qwen Code produced a date-format validator + 10 passing unit tests.
- **RQ2 (deviations):** the main deviation was Gemini CLI spontaneously assuming the refactoring task assigned to Qwen Code. Three factors: absent scope boundaries between phases, functional overlap between tools, and **workflow inertia** — the cognitive cost of context-switching (re-establishing full project context in another tool) outweighed staying in the drifted role. Also: Antigravity ignored the specified date format (CoT reasoning paradox: deprioritized a formatting constraint while focused on structural reasoning).
- **RQ3 (quality, ISO/IEC 25010:2011 qualitative):** High functional suitability, maintainability (MVC, type hints), interaction capability, flexibility (run.sh env fallback); Moderate reliability (venv corruption fragility). 2023 edition adds Safety — directly relevant to §5.5 security discussion.

**Prompt hardening:** CSV generation needed 3 iterations with explicit negative constraints — the agent tried to invoke unavailable internal tools and mixed metadata into output before "DO NOT run commands / use tools / create the file" pinned it. Consistent with AGENTIF constraint-density degradation.

**Security (§5.5.3):** indirect prompt injection from trusted data (web pages, external CSV) is flagged as the most significant threat for agents with file-system write + terminal access; the study's benign incidents (attempted tool invocation, venv corruption) illustrate the escalation potential. Calls for strict sandboxing + resource controls in agentic dev environments. Recommends LLMOps patterns: prompts-as-code, deterministic-plan/probabilistic-execution separation, and intelligent model routing (small local models for routine tasks, cloud models for architectural changes).

**Cyber relevance:** this is the multi-tool role-coordination side of agent harness design. For MCP-heavy harnesses, RSM's lesson is: assign explicit responsibility domains per tool, enforce scope boundaries, and treat unplanned role-absorption by one tool (e.g., a coding agent silently doing the audit) as a coordination failure to be caught — matching this wiki's multi-tool MCP poisoning axis.

## Snippets

> Explicit role coordination can support development cycle organization and architectural quality, but requires deliberate coordination strategies, context management, and human verification of agent-generated outputs. [Source: arXiv:2608.12311 abstract]

> The main deviation observed was Gemini CLI assuming the architectural refactoring task originally assigned to Qwen Code. Three concurrent factors account for this: the absence of an explicit scope boundary between Phase 2 and Phase 3; functional overlap between both tools; and workflow inertia. [Source: arXiv:2608.12311 p.11]

> Indirect prompt injections represent the most significant threat: malicious instructions hidden in trusted data (web pages, external CSV files) that the agent reads and executes without prior validation. [Source: arXiv:2608.12311 p.15]

## Dead Ends

- Zenodo DOI 10.5281/zenodo.21076890 returned 404 at retrieval (2026-08-13) — re-check after publication before attempting local repro.
- Threats to validity: single case, single researcher (observer bias), two of three tools share the same Gemini backend (reduces cognitive diversity — may partly explain role overlap), qualitative ISO 25010 ratings are author judgment.
- The RSM framework itself is backend-agnostic; the paper explicitly proposes a future heterogeneous-toolset test (Anthropic/Meta local model + Google agentic IDE).
