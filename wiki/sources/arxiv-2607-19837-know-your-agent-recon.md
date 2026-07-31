---
title: Know Your Agent — reconnaissance-driven agent pentesting (arXiv 2607.19837)
type: source
tags: [source, arxiv, agent-security, ipi, pentesting, reconnaissance]
keywords: [2607.19837, KYA, Know Your Agent, agent reconnaissance, AgentDojo, OpenHands, Mirsky]
related:
  - concepts/agent-reconnaissance-ipi-pentesting.md
  - entities/tools/know-your-agent.md
  - concepts/agent-data-injection-attacks.md
  - concepts/llm-pentest-automation.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-23
updated: 2026-07-31
phase_0_verdict: "CONDITIONAL-GO 2026-07-23 — paper promises open-source KYA + baselines; public GitHub not found yet; REFERENCE until release"
wire_status: deferred
wire_target: "Await public KYA repo"
---

**Briefs:** `briefs/2026-07-23_k210-know-your-agent-recon-prod.md`

## Relations

- @concepts/agent-reconnaissance-ipi-pentesting.md
- @entities/tools/know-your-agent.md
- @concepts/agent-data-injection-attacks.md
- @concepts/llm-pentest-automation.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/agent-runtime-guardrails.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Know Your Agent: Reconnaissance-Driven Pentesting of AI Agents |
| Authors | Or Zion Eliav, Eyal Lenga, Shir Bernstien, Yisroel Mirsky (BGU) |
| arXiv | 2607.19837 |
| Code | Promised open-source KYA + prior baselines — **not yet located on GitHub** (2026-07-23) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.19837-know-your-agent-reconnaissance-driven-pentesting.pdf` |
| Retrieved | 2026-07-23 |

## Narrative

Traditional pentest uses recon between steps; authors argue **AI agents need the same**. Formalize **agent reconnaissance** — extract knowledge assets (tools, policies, permissions, task context, defenses, environment) to drive stronger **indirect prompt injection (IPI)** attacks. Instantiate as **Know Your Agent (KYA)**: black-box probe → target profile → tailored attacks.

### Headline results [CONFIRMED from abstract]

| Finding | Detail |
|---------|--------|
| ASR lift | KYA surpasses baselines by **up to 67 percentage points** ASR on agent-security benchmarks |
| Real agent | Validated on **OpenHands** coding agent (beyond synthetic suites / AgentDojo) |
| Artifact | Will release KYA + two previously unavailable baselines |

### Steal

1. Treat agent IPI eval as **recon→exploit loops**, not single-shot payload mutation
2. Profile tool/policy/defense surface before crafting injections
3. Track KYA release for lab harness adopt

### Phase-0

| Gate | Status |
|------|--------|
| License | **WAIT** — code not public |
| Size | n/a |
| Verdict | **CONDITIONAL-GO / REFERENCE** until GitHub lands |

## Snippets

> "Across a range of models and scenarios on established agent-security benchmarks, KYA surpasses all baselines by up to 67 percentage points in attack success rate."
[Source: arxiv-2607.19837 abstract]
