---
title: Cross-tool description poisoning
type: concept
tags: [concept, agent-security, mcp, tool-poisoning, metadata, planner]
keywords: [cross-tool description poisoning, tool metadata, influenced list, isolated planning, 2606.20922]
related:
  - sources/arxiv-2606-20922-tool-guard-isolated-planning-tool-description-poisoning.md
  - entities/tools/tool-guard.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - sources/arxiv-mcp-description-code-inconsistency-2606.04769-2026-06-05.md
  - sources/arxiv-2606-06387-webmcp-tool-surface-poisoning.md
  - concepts/multi-tool-threshold-mcp-poisoning.md
  - sources/arxiv-2606-27027-sharelock-multi-tool-threshold-mcp-poisoning.md
  - concepts/ai-for-cybersecurity.md
  - sources/arxiv-2606-29073-hcp-mcp-execution-control-invariants.md
  - concepts/mcp-execution-control-invariants.md
  - entities/tools/handle-capability-protocol.md
  - sources/arxiv-2607-05120-agent-data-injection-attacks.md
  - concepts/agent-data-injection-attacks.md
  - sources/arxiv-2607-07461-spellsmith-mcp-taint-style-vulnerabilities.md
  - concepts/mcp-taint-style-vulnerabilities.md
  - entities/tools/spellsmith.md
maturity: draft
created: 2026-06-24
updated: 2026-07-09
---

## Relations

- @sources/arxiv-2606-20922-tool-guard-isolated-planning-tool-description-poisoning.md — Tool-Guard + isolated planning (2606.20922)
- @entities/tools/tool-guard.md — reference implementation
- @concepts/mcp-security-posture.md — DCI/MSTI layer model

## Raw Concept

Ingest 2026-06-24: arXiv:2606.20922 — attack class where **poisoned tool metadata** steers planner trajectories involving **other tools**, without invoking the poisoned tool.

## Narrative

### Attack progression

```
Preference poisoning → self-select poisoned tool
Cross-tool poisoning → corrupt metadata influences OTHER tool choices (poisoned tool never called)
Multi-tool threshold (ShareLock) → Shamir shares across {T1…Tn}; <t shares reveal nothing; trigger reconstructs payload
```

ShareLock (2606.27027) extends this class: average ASR **93.3%** vs monolithic TPA **75.3%**; per-tool review and entropy heuristics fail via **information-theoretic secrecy** + **entropy dilution**. See @concepts/multi-tool-threshold-mcp-poisoning.md.

Poisoned descriptions **persist in planning context** across steps — unlike one-shot tool-output injection. Prompt-injection defenses (repeat prompt, drift, Progent) transfer poorly; AgentDojo ASR stays **19–43%** under those defenses vs **2.06%** under Tool-Guard (GPT-4o).

### Defense pattern: isolated planning

1. Alignment + suspiciousness checks on tool descriptions
2. Flagged tools → **influenced list** (excluded from planning context)
3. Tool may still execute if task requires it — breaks metadata influence, not utility

### Distinction from related failures

| Failure | Layer |
|---------|-------|
| DCI (2606.04769) | Authorized tool's description ≠ code |
| MSTI (2606.06387) | Mid-session registry mutation |
| **Cross-tool poisoning** | Metadata on tool A steers selection of tool B |
| **Multi-tool threshold** | Payload split across tools; cooperative reconstruction (2606.27027) |
| SPI (2606.04425) | Poison persists in memory across sessions |

### prod-mcp checklist `[TENTATIVE]`

1. Re-scan MCP manifests on version bump (DCI + cross-tool eval)
2. Test poisoned description on **non-invoked** tool in allowlist
3. Consider influenced-list pattern before blanket tool filtering
4. Report per-surface ASR — not chat-only injection metrics

See `briefs/2026-06-24_tool-guard-isolated-planning-prod-mcp-handoff.md`.

## Snippets

| Setting | ASR no defense | ASR Tool-Guard (GPT-4o avg) |
|---------|----------------|----------------------------|
| AgentDojo | 43.30% | 2.06% |
| Critical-tool poison stress | 19.59% | 3.09% |

[Source: arxiv-2606.20922]
