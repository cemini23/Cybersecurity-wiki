---
title: "Security-agent SLR — act but authority unbounded / behavior unauditable (K315)"
type: concept
tags: [concept, agent-security, survey, software-security, evaluation, k315]
keywords: [security agent survey, bounded authority, auditable behavior, trajectory metrics, assessment taxonomy, PentestGPT, CVE-Bench, RepoAudit]
related:
  - sources/arxiv-2608-28490-llm-security-agents-survey.md
  - concepts/agent-runtime-guardrails.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/llm-pentest-automation.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/trace-verified-ctf-agent-eval.md
  - concepts/recognition-enforcement-gap-instruction-arbitration.md
  - concepts/ai-pentest-harness-landscape.md
maturity: draft
created: 2026-08-31
updated: 2026-08-31
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K315)"
---

## Relations

- @sources/arxiv-2608-28490-llm-security-agents-survey.md — source SLR (100 papers, 2023–2026)
- @concepts/agent-runtime-guardrails.md — guard/enforcement stack context
- @concepts/faithful-agent-asr-measurement.md — faithful capability measurement (K271)
- @concepts/llm-pentest-automation.md — Tier-1/Tier-2 pentest agent patterns
- @concepts/ai-redteam-evidential-ceiling.md — what fixed-budget evals can prove
- @concepts/trace-verified-ctf-agent-eval.md — trace-level assessment complement (K311)

## Raw Concept

Question: **where is the LLM-based security-agent literature, and what does it still miss?**

## Narrative

The Nie et al. survey (K315, 2608.28490) organizes **100 papers** (Jan 2023 – Mar 2026) along **Approach / Application / Assessment**. Applications span vulnerability auditing, exploit workflows, red teaming, fuzzing, malware analysis, SOC support, and access-control review — with sharply different risk profiles that the literature often collapses under the label “agent.”

**Central observation:** researchers have demonstrated agents that **plan, use tools, and act over multi-step security workflows**, but have **not** consistently built agents with **bounded authority** or **auditable trajectories**. Reported end-task success does not establish faithful evidence use, scope compliance, permission respect, or reproducible cost.

**Operator steal:**
1. **Classify any security-agent claim on three axes** — how it is built (approach), what task it serves (application risk tier), and how it is measured (assessment: outcome vs trajectory vs safety).
2. **Demand trajectory- and safety-level metrics** for high-blast agents (exploit execution, prod patching, live scanning) — not flag/ASR alone. Pairs K271, K311 trace-verified eval.
3. **Treat “agent” labels as incomparable** until architecture + autonomy + tool scope are explicit — single tool-calling LLM ≠ multi-agent SOC pipeline.
4. **Future direction (paper):** evidence-centered architecture, risk-aware autonomy, reproducible executable benchmarks, accountable human–agent collaboration.

## Snippets

> Agents able to act but not yet agents whose authority is bounded or whose behavior is auditable. [Source: arXiv 2608.28490 abstract]

> Final task success is important, but it does not show whether an agent used evidence faithfully, stayed within scope, avoided hallucinations, respected tool permissions … [Source: arXiv 2608.28490 abstract]
