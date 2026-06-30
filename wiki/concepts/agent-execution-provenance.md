---
title: Agent execution provenance and evidence tracing
type: concept
tags: [concept, agent-security, provenance, observability, evaluation, audit, methodology]
keywords: [evidence tracing, execution provenance, agent traces, W3C PROV, claim attribution, trace completeness, process accountability]
related:
  - sources/arxiv-2606-04990-agent-traces-evidence-provenance.md
  - concepts/agent-runtime-guardrails.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/mcp-security-posture.md
  - concepts/agent-skill-injection.md
  - concepts/agent-vm-sandboxing.md
  - concepts/siem.md
  - concepts/neuro-symbolic-auditable-reasoning.md
  - concepts/ai-for-cybersecurity.md
  - sources/arxiv-2606-02302-seclaw-spec-driven-agent-security.md
  - sources/arxiv-2606-02240-agentredbench.md
  - sources/arxiv-mcp-description-code-inconsistency-2606.04769-2026-06-05.md
  - sources/arxiv-2606-05252-bas-to-siem-detection-as-code-synthesis.md
  - sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md
  - entities/tools/cua.md
  - entities/tools/defenseclaw.md
  - sources/arxiv-2606-07943-poise-position-aware-skill-injection.md
  - sources/arxiv-2606-09084-context-fractured-decomposition-attacks.md
  - sources/arxiv-2606-10749-toward-secure-llm-agents-survey.md
  - concepts/internet-of-agentic-ai-ioai.md
  - sources/arxiv-2606-12835-internet-of-agentic-ai-communication-coordination.md
  - concepts/context-fractured-decomposition-attacks.md
  - concepts/agentic-containment-principles.md
  - concepts/trajectory-context-control.md
  - sources/arxiv-2606-12797-agentic-containment-gap-framework-audit-2026-06-13.md
maturity: draft
created: 2026-06-07
updated: 2026-06-30
---

## Relations

- @sources/arxiv-2606-04990-agent-traces-evidence-provenance.md — survey anchor (arXiv 2606.04990)
- @concepts/agent-runtime-guardrails.md — runtime guards as provenance trust function (safety enforcement)
- @concepts/seclaw-agent-security-evaluation.md — trajectory eval > final-answer correctness
- @concepts/mcp-security-posture.md — admission/DCI/SPI/MSTI as provenance blind spots
- @concepts/agent-skill-injection.md — untracked skill/memory lineage
- @concepts/agent-vm-sandboxing.md — cua tracing as execution-unit capture
- @concepts/neuro-symbolic-auditable-reasoning.md — symbolic audit chains (NeuroLog) vs runtime traces
- @concepts/ai-for-cybersecurity.md — LLM agent accountability in blue/red workflows
- @sources/arxiv-2606-02302-seclaw-spec-driven-agent-security.md — unsafe intermediate steps in trajectories
- @sources/arxiv-2606-05252-bas-to-siem-detection-as-code-synthesis.md — defensive probe→rule traceback analog
- @sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md — SPI survives reset without provenance record
- @entities/tools/cua.md — screenshot + a11y-tree action traces
- @entities/tools/defenseclaw.md — scan/admission logs (partial provenance)

## Raw Concept

Daily digest ingest (2026-06-07): arXiv:2606.04990 survey synthesizing **evidence tracing** + **execution provenance** as the accountability layer for tool-using LLM agents — when final answers are insufficient for trust, audit, or incident response.

## Narrative

Tool-using agents compose retrieval, MCP/tool calls, memory, environment observations, and multi-agent messages. **Process-level accountability** asks: for each claim or action, what evidence supported it, what execution step caused it, and can an operator replay or dispute the chain?

### Two complementary views

| View | Question | Example artifacts |
|------|----------|-------------------|
| **Evidence tracing** | What supported/contradicted this claim? | Citations, atomic facts (FActScore), source supportiveness (SourceCheckup) |
| **Execution provenance** | What happened, in what order, with what dependencies? | ReAct traces, tool params, memory R/W, PROV-style graphs |

Structured logs make behavior **observable**; execution/evidence graphs make **influence explicit** (TRAIL failure localization).

### Taxonomy axes (operational checklist)

When scoping agent copilots (pentest, SOC, Cemini lazy-tool):

1. **Trace sources covered?** — tool + memory + inter-agent, not chat-only
2. **Granularity** — claim-level vs run-level only
3. **Timing** — runtime enforcement (CaMeL, FIDES, AIRGuard-class) vs post-hoc audit
4. **Trust function** — attribution vs safety vs recovery

### Mapping to this wiki's K95–K100 stack

| Provenance gap | Wiki control |
|----------------|------------|
| Tool description ≠ code | @concepts/mcp-security-posture.md DCI (2606.04769) |
| Cross-session poison | SPI checklist (2606.04425) + skill vetting |
| Mid-session tool surface | WebMCP MSTI (2606.06387) |
| Unsafe trajectory hidden by polite answer | @concepts/seclaw-agent-security-evaluation.md |
| Detection gap without traceback | @sources/arxiv-2606-05252-bas-to-siem-detection-as-code-synthesis.md |
| Symbolic vuln chain audit | @concepts/neuro-symbolic-auditable-reasoning.md |
| Artifact provenance gap (CFD) | @concepts/context-fractured-decomposition-attacks.md — lineage tagging (2606.09084) |

### Evaluation hygiene [CONFIRMED per survey]

Report at least one metric from each family when claiming "agent is secure":

- Evidence attribution (faithfulness / claim support)
- Execution provenance (trace completeness)
- Safety under tool/memory influence (AgentDojo-class)
- Debugging (failure localization — TRAIL, MAST)

Single **task success rate** is explicitly insufficient for trustworthy agents.

### Pentest / SOC implications

- Engagement reports: attach **provenance graph** or trace export for agent-assisted steps (cua traces, OpenTelemetry spans, defenseclaw scan logs).
- Red-team: test whether poisoned tool output/memory appears in final answer **without** appearing in operator-visible trace (provenance bypass).
- Blue-team: SIEM rules from BAS (2606.05252) provide defensive traceback; agent provenance provides **offensive-side** evidence chain for purple-team replay.

## Snippets

Provenance relations (survey): *support, derive, depend-on, contradict, invalidate, trigger, update, use, generate* — [Source: arxiv-2606.04990 Table 2, retrieved 2026-06-07]

Representative observability: AgentOps, AgentTrace, TRAIL — [Source: arxiv-2606.04990 Table 4, retrieved 2026-06-07]

## Dead Ends

- **Citation-only RAG eval** — ALCE/RAGAS do not cover tool-parameter or memory-lineage provenance.
- **Full trace retention on prod** — survey flags privacy-aware audit as open; redact secrets before centralizing traces.
- **Unified schema today** — fragmented; no single W3C-PROV-for-agents standard shipped [NEEDS VERIFICATION 2026-06-07].

### Fleet shared memory (CCC K125 — MemClaw)

Governed multi-agent memory (arXiv:2606.24535) raises **scope-tag + provenance-on-write** requirements for any fleet store agents read. Pre-trial checklist: `briefs/2026-06-25_k125-memclaw-fleet-memory-governance-handoff.md` (CCC primary; `@ccc-wiki/concepts/governed-fleet-shared-memory.md`).
