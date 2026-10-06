---
title: "FrugalEvo: towards cost-aware LLM-guided program evolution"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.03675, k397]
related:
  - concepts/budget-aware-agentic-search-cost.md
  - concepts/fragtoken-inference-cost-amplification-lab.md
  - concepts/reliable-inference-procurement-routing.md
maturity: draft
read_status: read
created: 2026-10-06
updated: 2026-10-06
phase_0_verdict: "REFERENCE 2026-10-06 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K397)"
---

## Relations

## Relations

- @concepts/budget-aware-agentic-search-cost.md
- @concepts/fragtoken-inference-cost-amplification-lab.md
- @concepts/reliable-inference-procurement-routing.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | FrugalEvo: towards cost-aware LLM-guided program evolution |
| arXiv | 2610.03675 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.03675-frugalevo-towards-cost-aware-llm-guided-program.pdf |
| Retrieved | 2026-10-06 |
| Read status | read (deep-read) |

## Narrative

**K397** — LLM-guided evolutionary search (AlphaEvolve-style) is usually scored as gain per *iteration*. This argues for **gain per unit cost** instead, and introduces **BA-AUC** (Budget-Aware Area Under the Curve): the area under the best-so-far score curve plotted against **cumulative LLM cost**, up to a budget. The framework splits the loop — a **strong, expensive LLM explores** strategies while a **cheap LLM implements and refines** the code — and the harness and prompts are built to **maximise prefix sharing** across evolution steps for cache reuse. Over 10 math and systems optimisation tasks it matches or beats OpenEvolve / ShinkaEvolve / AdaEvolve / EvoX on final quality and BA-AUC, at **$1.68** (Terra + Luna) and **$0.55** (GLM-5.3 + Flash) against roughly **$50** for multi-agent baselines (CORAL, SwarmResearch). Operator steal: **budget the loop, not the iteration count**, and split strategist from implementer. Tangential to security — it is a harness-cost pattern, useful for the wiki's cost thread (K376 FragToken, K366 inference procurement), not a security technique. Repo `github.com/chchenhui/frugalevo` **Apache-2.0** but **305 MB** — REFERENCE, no clone.

## Snippets

> See arXiv 2610.03675 abstract. [Source: arXiv 2610.03675 (retrieved 2026-10-06)]
