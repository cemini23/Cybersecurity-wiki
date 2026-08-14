---
title: "MARC v1 — open-source multi-agent framework for clinical AI reasoning (arXiv 2608.13476)"
type: source
tags: [source, arxiv, multi-agent, orchestration, clinical-ai, llm, k279]
keywords: [2608.13476, MARC, Multi-Agent Reasoning and Coordination, Decomposer, stage-wise failure attribution, clinical reasoning, LangChain, Ollama, Gemini, Penn-RAIL]
related:
  - entities/tools/marc-v1.md
  - concepts/deterministic-multi-agent-orchestration-failure-attribution.md
  - concepts/role-specialization-multi-tool-coordination.md
  - concepts/agent-runtime-guardrails.md
maturity: draft
read_status: read
created: 2026-08-14
updated: 2026-08-14
phase_0_verdict: "GO clone 2026-08-14 — github.com/Penn-RAIL/MARC-v1 MIT, ~31MB (20MB shallow), 2 stars, Python 3.10-3.13. Steal: deterministic sequential multi-agent orchestration + Decomposer + stage-wise failure attribution. Clinical runtime wont_wire; orchestration pattern K279 policy wire."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-mcp-tool-control.mdc (K279) — clinical runtime wont_wire"
---

**Briefs:** `briefs/2026-08-14_k279-marc-orchestration-steal.md`

## Relations

- @entities/tools/marc-v1.md — the entity page (GO clone)
- @concepts/deterministic-multi-agent-orchestration-failure-attribution.md — the synthesized orchestration steal
- @concepts/role-specialization-multi-tool-coordination.md — RSM (K277); MARC is the deterministic-pipeline implementation of role coordination
- @concepts/agent-runtime-guardrails.md — stage-wise failure attribution as a guardrail mechanism

## Raw Concept

| Field | Value |
|-------|-------|
| Title | MARC v1: An Open-Source Multi-Agent Framework for Clinical AI Reasoning and Coordination |
| Authors | Saisha Shetty, Satvik Tripathi (co-first), Austin Lin, Colin Zhao, Theodore Kim, Don Enwerem, Jacinta Arnold, Shahriar Faghani, Tessa S. Cook (UC Davis / UPenn / Drexel) |
| arXiv | 2608.13476 (13 pp, v1 13 Aug 2026) |
| Code | `github.com/Penn-RAIL/MARC-v1` — MIT, ~31MB (20MB shallow), 2 stars |
| Location | `raw-sources/repos/MARC-v1/` (shallow clone, 2026-08-14) + `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.13476-marc-v1-an-open-source-multi-agent-framework-for.pdf` |
| Retrieved | 2026-08-14 |
| Read status | read (13 pp full text) + repo README/source inspected |

## Narrative

MARC replaces **monolithic LLM prompting** with **deterministic multi-agent orchestration** for clinical reasoning. Coordinates role-specialized agents (extraction → reasoning → answer generation → evaluation) with **explicit context passing** and **traceable intermediate outputs**, enabling **stage-wise failure attribution**.

**Architecture (all implemented in the repo):**
- **YAML-declared agents** — name, model, prompt file, optional RAG context files; no code changes to add/reorder/remove agents. Default pipeline: 3 agents (extraction, reasoning, answer), each receiving original input + preceding agent's output.
- **Decomposer module** — takes a plain-language task description, uses Gemma 4B (via Ollama) to emit a structured JSON 3-agent pipeline spec (names, roles, full prompt templates), validated against structural constraints (variable bindings `{input}`/`{previous_agent_output}`, VERDICT formatting, length limits) before writing to disk.
- **Two backends** — Google Gemini API or local Ollama (CPU-compatible); greedy decoding (temperature 0) by default for repeatable runs.
- **Per-agent RAG** — optional Chroma retrieval over local text files.

**Steal for Cemini harnesses (non-clinical):** the deterministic sequential pipeline with explicit context passing + stage-wise failure attribution is exactly the pattern that makes multi-agent runs auditable. Pairs with RSM (K277): RSM assigns *roles across tools*, MARC implements *deterministic stage-wise execution with attribution*.

**Clinical domain note:** the framework is validated on biomedical QA, radiology report generation, and task-adaptive pipeline construction. **wont_wire** for clinical runtime — no patient data in Cemini scope; the orchestration *pattern* is what transfers.

## Snippets

> MARC runs a sequence of role-specialized agents that pass context explicitly, so each stage of the reasoning process can be inspected on its own. [Source: README, github.com/Penn-RAIL/MARC-v1]

> Adding, removing, or reordering agents requires no code changes. [Source: README]
