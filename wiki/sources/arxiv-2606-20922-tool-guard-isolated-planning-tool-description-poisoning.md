---
title: Tool-Guard — isolated planning against cross-tool description poisoning (arXiv 2606.20922)
type: source
tags: [source, arxiv, agent-security, mcp, tool-poisoning, tool-guard]
keywords: [2606.20922, tool-guard, cross-tool description poisoning, isolated planning, influenced list, agentdojo]
related:
  - concepts/cross-tool-description-poisoning.md
  - entities/tools/tool-guard.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-for-cybersecurity.md
  - sources/arxiv-2606-06387-webmcp-tool-surface-poisoning.md
  - sources/arxiv-mcp-description-code-inconsistency-2606.04769-2026-06-05.md
maturity: draft
read_status: read
created: 2026-06-24
updated: 2026-06-24
phase_0_verdict: "CONDITIONAL-GO 2026-06-24 — github.com/shishishi123/Tool-Guard MIT, 0★, ICML 2026 artifact; lab-validate on prod-mcp before enforcement"
---

## Relations

- @concepts/cross-tool-description-poisoning.md — cross-tool metadata steering synthesis
- @entities/tools/tool-guard.md — Tool-Guard implementation + Phase-0 gate

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Think Twice Before You Act: Protecting LLM Agents Against Tool Description Poisoning via Isolated Planning |
| Authors | Shanghao Shi, Xiao Wang, Chaoyu Zhang, Hao Li, Wenjing Lou, Thomas Hou, Yevgeniy Vorobeychik, Chongjie Zhang, Ning Zhang |
| Affiliations | Washington University in St. Louis; Virginia Tech |
| arXiv | 2606.20922 (ICML 2026) |
| Code | [github.com/shishishi123/Tool-Guard](https://github.com/shishishi123/Tool-Guard) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2606.20922-think-twice-before-you-act-protecting-llm-agents.pdf` |
| Retrieved | 2026-06-24 |
| Read status | **read** (abstract, threat model, Tool-Guard design, AgentDojo/ASB tables) |

## Narrative

Introduces **cross-tool description poisoning**: corrupting one tool's MCP-visible metadata can steer the planner toward malicious actions involving **other** tools — even when the poisoned tool is never invoked. Standard prompt-injection defenses transfer poorly because poisoned descriptions **persist in planning context** across steps.

**Tool-Guard** implements **isolated planning**: after alignment/suspiciousness checks flag a tool, it moves to an **influenced list** — its description is excluded from subsequent planning context while the tool may still execute if needed. This breaks continuous metadata influence without blanket tool filtering.

### Headline results (AgentDojo, GPT-4o)

| Metric | No defense | Tool-Guard |
|--------|------------|------------|
| Benign utility | 76.29% | 72.16% |
| Attack utility (under attack) | 54.64% | 58.76% |
| ASR | 43.30% | **2.06%** |

Cross-model average ASR under defense: **0.00–4.76%** (Claude-3.5-Haiku 4.12% → 1.03%). Semantic-adaptive attacks: ASR **0%** on most variants; PAIR optimization raises defended ASR but remains low.

**Cost:** ~1.45×/1.39× token vs no-defense; ~3.7× wall-clock vs no-defense (less than Drift's 7.3×).

### Wiki relevance

Complements DCI (description≠code) and MSTI (mid-session registry) — this is **persistent cross-tool metadata influence** in static catalogs. Pair with @concepts/mcp-security-posture.md admission + re-scan cadence.

`[TENTATIVE]` — eval on AgentDojo/ASB; prod-mcp harness validation pending.

## Snippets

> "Cross-tool description poisoning can manipulate planner-visible tool metadata to steer an agent's trajectory, even if the poisoned tool itself is never chosen."

> "Tool-Guard substantially reduces attack success while maintaining high task utility."

[Source: arxiv-2606.20922-think-twice-before-you-act-protecting-llm-agents.pdf]
