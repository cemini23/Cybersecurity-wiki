---
title: "ChainCaps — MCP proxy for composition-safe tool chains"
type: entity
tags: [tool, ai-security, mcp, information-flow, composition-safety, research, reference]
keywords: [chaincaps, permission laundering, monotonic capability attenuation, mcp proxy, sink-specific budget]
related:
  - concepts/agent-runtime-guardrails.md
  - concepts/llm-pentest-automation.md
  - entities/tools/airguard.md
  - entities/tools/nvidia-skillspector.md
  - entities/tools/defenseclaw.md
  - sources/arxiv-2605-26542-chaincaps-composition-safe-tool-using-agents.md
  - concepts/mcp-security-posture.md
  - sources/arxiv-attested-tool-server-admission-2605.24248-2026-06-05.md
  - sources/arxiv-2606-06387-webmcp-tool-surface-poisoning.md
maturity: draft
created: 2026-06-01
updated: 2026-05-31
phase_0_verdict: "Reference 2026-06-01 — workshop paper + MCP proxy pattern; no canonical public repo in source; adopt pattern after manifest linter + lab replay."
---

# ChainCaps — MCP proxy for composition-safe tool chains

## Relations

- @concepts/agent-runtime-guardrails.md — permission laundering + monotonic budget propagation
- @concepts/llm-pentest-automation.md — MCP tool chains in pentest automation
- @entities/tools/airguard.md — authority control at action time vs flow budgets across composition
- @entities/tools/nvidia-skillspector.md — static skill audit vs runtime value-level IFC
- @entities/tools/defenseclaw.md — enterprise governance complement
- @sources/arxiv-2605-26542-chaincaps-composition-safe-tool-using-agents.md — paper provenance

## Raw Concept

Ingested from arXiv:2605.26542 (2026-06-01). ChainCaps — transparent **MCP proxy** enforcing sink-specific capability budgets with intersection on compose.

## Narrative

Addresses **permission laundering**: individually authorized tool calls compose into policy-violating end-to-end effects. Values carry sink-specific budgets; composition uses intersection — authority only attenuates.

**Deployment bottleneck**: manifest quality (expert vs naive manifests: 100% vs 27.3% block in paper). Scope: explicit-flow composition under trusted manifests and proxy-visible movement — not covert channels or hidden model state.

**Import boundary**: reference architecture for MCP hardening labs; implement or vendor-wrap only after manifest authoring workflow exists.

## Snippets

Paper-reported: ASR 25–68% → 0–4.8% on 82-task suite; 96–100% benign completion. `[TENTATIVE]`

## Dead Ends

- **Per-tool server ACL alone** — cannot prevent safe-looking compositions from reaching forbidden sinks.
- **Naive auto-generated manifests** — paper shows majority of attack traces slip through.
