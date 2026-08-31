---
title: "Step-level agent guardrails — pre-execution tool checks (K307)"
type: concept
tags: [concept, agent-security, guardrail, mcp, tool-use, k307, defensive]
keywords: [StepGuard, step-level guard, pre-execution, trajectory guard, safety-utility balance, defense bias, tool action audit]
related:
  - sources/arxiv-2608-24777-stepguard.md
  - entities/tools/stepguard.md
  - concepts/agent-runtime-guardrails.md
  - concepts/nl-security-rules-vs-builtin-deny.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/mcp-security-posture.md
  - concepts/non-decaying-loop-safety-state.md
  - concepts/recognition-enforcement-gap-instruction-arbitration.md
maturity: draft
created: 2026-08-26
updated: 2026-08-26
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc + mcp-tool-control.mdc (K307)"
---

## Relations

- @sources/arxiv-2608-24777-stepguard.md
- @entities/tools/stepguard.md — StepGuard repo/model pointer (CONDITIONAL-GO pending LICENSE)
- @concepts/agent-runtime-guardrails.md — guard placement in agent stack
- @concepts/nl-security-rules-vs-builtin-deny.md — prose rules ≠ pre-execution deny
- @concepts/faithful-agent-asr-measurement.md — report ASR + utility jointly, not guard accuracy alone
- @concepts/mcp-security-posture.md — tool admission vs per-step action gate

## Raw Concept

Question: **where should an agent guard intercept unsafe tool use — after the trajectory completes, or before each tool action executes?**

## Narrative

Trajectory-level guards diagnose harm **after** side effects may already exist (file writes, messages, transactions). Step-level guards treat **each candidate tool call** as a decision point: allow, block, or escalate before the executor runs.

StepGuard (K307, 2608.24777) trains a 4B guard with **StepGen** (matched safe/unsafe prefixes at the risky step) and **Balance-GRPO** (reweight safe vs unsafe learning from observed accuracy gaps). Paper evidence: large ASR reduction on AgentDojo/AgentDyn with small utility cost — but **AgentHarm** still trades completion for malicious-score reduction; highly adversarial harm settings remain open.

**Operator steal (authorized lab / product pentest harness):**
1. **Prefer pre-execution gates for irreversible MCP/tool effects** (pairs K239). Trajectory audit is complementary, not a substitute.
2. **Measure safety–utility together** — a guard that blocks everything has ASR≈0 and utility≈0. Report ASR, benign-task utility, and over-block rate.
3. **Defense bias is a product bug** — calibrate guards on held-out benign tool chains from your harness, not only attack packs.
4. **No LICENSE → no default clone/wire** — `zheng977/StepGuard` had no LICENSE file at Phase-0 hunt; steal patterns only until SPDX verified.
5. Guards monitor agents; they do not replace sandboxing, mandate chains (K285), or deterministic deny hooks (K303).

## Snippets

> A guard must block unsafe actions while preserving benign tasks. However, existing guards often exhibit defense bias. [Source: arXiv 2608.24777 §1]

> StepGuard checks candidate tool actions before execution and also audits completed trajectories. [Source: arXiv 2608.24777 abstract]
