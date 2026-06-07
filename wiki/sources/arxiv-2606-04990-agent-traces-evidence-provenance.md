---
title: From Agent Traces to Trust — evidence tracing and execution provenance survey (arXiv 2606.04990)
type: source
tags: [source, arxiv, survey, agent-security, provenance, observability, evaluation]
keywords: [2606.04990, evidence tracing, execution provenance, agent traces, W3C PROV, TRAIL, AgentTrace]
related:
  - concepts/agent-execution-provenance.md
  - concepts/agent-runtime-guardrails.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/mcp-security-posture.md
  - concepts/agent-skill-injection.md
  - concepts/agent-vm-sandboxing.md
  - concepts/ai-for-cybersecurity.md
  - concepts/siem.md
  - concepts/neuro-symbolic-auditable-reasoning.md
  - entities/tools/cua.md
  - entities/tools/defenseclaw.md
  - sources/arxiv-2606-02302-seclaw-spec-driven-agent-security.md
  - sources/arxiv-2606-02240-agentredbench.md
  - sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md
  - sources/arxiv-2606-05252-bas-to-siem-detection-as-code-synthesis.md
  - sources/arxiv-mcp-description-code-inconsistency-2606.04769-2026-06-05.md
maturity: draft
read_status: read
created: 2026-06-07
updated: 2026-06-07
---

## Relations

- @concepts/agent-execution-provenance.md — synthesized taxonomy + eval framework from this survey
- @concepts/agent-runtime-guardrails.md — runtime guardrails as one provenance trust function
- @concepts/seclaw-agent-security-evaluation.md — trajectory eval vs final-answer metrics
- @concepts/mcp-security-posture.md — tool-call / DCI / SPI as provenance gaps
- @concepts/agent-skill-injection.md — memory lineage + cross-session poison as provenance failure
- @concepts/ai-for-cybersecurity.md — process-level accountability umbrella
- @sources/arxiv-2606-02302-seclaw-spec-driven-agent-security.md — trajectory scoring benchmark
- @sources/arxiv-2606-02240-agentredbench.md — integration-aware redteam traces
- @sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md — SPI as untracked memory provenance
- @sources/arxiv-2606-05252-bas-to-siem-detection-as-code-synthesis.md — probe-level SIEM traceback (defensive analog)
- @sources/arxiv-mcp-description-code-inconsistency-2606.04769-2026-06-05.md — description≠code as semantic provenance gap

## Raw Concept

| Field | Value |
|-------|-------|
| Title | From Agent Traces to Trust: Evidence Tracing and Execution Provenance in LLM Agents |
| Authors | Yiqi Wang et al. (Griffith, PKU, Nanjing, Macquarie, SUSTech, …) |
| arXiv | 2606.04990 |
| Type | Survey (33 pages) |
| Location | `raw-sources/arxiv-2606.04990-from-agent-traces-to-trust-evidence-tracing-and.pdf` |
| Retrieved | 2026-06-07 |
| Read status | **read** (abstract, taxonomy Tables 2–7, benchmark mapping, conclusion) |

## Narrative

Systematic survey framing **process-level accountability** for tool-using LLM agents. Final-answer accuracy cannot explain which evidence supported each claim, whether tool calls were justified, how memory influenced decisions, or which step caused failure [CONFIRMED].

### Core definitions

- **Evidence tracing** — record/connect evidence units (retrieval, tool outputs, memory, observations) that support, contradict, or influence claims and actions.
- **Execution provenance** — structured representation of full agent run: documents, tool calls + parameters, memory R/W, intermediate claims, inter-agent messages, final outputs. Informed by W3C PROV-DM and OpenTelemetry distributed traces.

### Taxonomy (Table 2) — seven dimensions

| Dimension | Examples |
|-----------|----------|
| Trace sources | Reasoning, retrieval, tool use, memory, environment, multi-agent |
| Evidence units | Passages, tool outputs, memory items, claims, policies |
| Execution units | Steps, tool invocations, parameters, memory ops, messages |
| Provenance relations | support, derive, depend-on, contradict, invalidate, trigger, update |
| Tracing granularity | run → step → tool-call → parameter → claim → token/span |
| Tracing timing | pre-execution, runtime, post-hoc, continuous |
| Trust functions | verification, attribution, debugging, safety enforcement, audit, recovery |

### Representation forms (Table 3)

Structured logs → execution graphs → evidence graphs → static schemas → runtime provenance (source-to-sink IFC).

### Tool-use provenance lines (Table 4)

Maps InjecAgent / AgentDojo / ToolEmu (risk eval) → CaMeL / StruQ / FIDES / NeuroTaint (IFC) → Agent-Sentry (argument provenance) → AgentSpec / AgentBound (execution boundaries) → AgentOps / AgentTrace / TRAIL / LADYBUG (trace debugging).

### Evaluation shift (Table 6–7)

Four metric families beyond task success:

1. **Evidence attribution** — claim grounding (FActScore, RAGChecker, SourceCheckup)
2. **Execution provenance** — trace completeness, dependency coverage
3. **Safety/robustness** — unsafe influence, policy violations (ToolEmu, AgentDojo)
4. **Debugging/recovery** — failure localization (TRAIL, MAST)

**Gap:** few benchmarks jointly ship evidence labels + tool calls + memory ops + multi-agent comms + safety perturbations + provenance-relation annotations.

### Cemini / wiki mapping

Complements existing cybersec-wiki stack: @concepts/seclaw-agent-security-evaluation.md (trajectory), @concepts/mcp-security-posture.md (tool trust), @sources/arxiv-2606-05252-bas-to-siem-detection-as-code-synthesis.md (deterministic defensive traceback). Survey argues unified trace schema should be **first-class infrastructure**, not post-hoc logging.

## Snippets

> "Final-answer accuracy alone cannot explain how an output was produced, which evidence supported each claim, whether tool calls were justified, how memory influenced later decisions, or where execution failures originated."
> — [Source: arxiv-2606.04990 abstract, retrieved 2026-06-07]

> "Evidence tracing and execution provenance should become a first-class infrastructure layer for reliable agent systems."
> — [Source: arxiv-2606.04990 §9 Conclusion, paraphrase, retrieved 2026-06-07]

## Dead Ends

- **Survey-only** — no single shipped unified schema; practitioners must compose AgentOps + guardrail + eval tools ad hoc [TENTATIVE].
- **Privacy-aware audit** — open challenge; full trace retention conflicts with credential redaction in pentest/SOC copilots.
