---
title: PATS — policy-aware training scaffolding for agentic RL (arXiv 2607.21419)
type: source
tags: [source, arxiv, agent-rl, scaffolding, training]
keywords: [2607.21419, PATS, ALFWorld, WebShop, evidence cards, RLVR]
related:
  - concepts/pats-policy-aware-agent-rl-scaffold.md
  - concepts/experiential-abstraction-memory.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-24
updated: 2026-07-31
phase_0_verdict: "REFERENCE 2026-07-24 — Tencent/PKU training method; no public code located"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

**Briefs:** `briefs/2026-07-24_k217-pats-agentic-rl-scaffold-prod.md`

## Relations

- @concepts/pats-policy-aware-agent-rl-scaffold.md
- @concepts/experiential-abstraction-memory.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | PATS: Policy-Aware Training Scaffolding for Agentic Reinforcement Learning |
| Authors | Shi, Ma, Wang, Tan, Li, Chen, Zhu (PKU / Tencent) |
| arXiv | 2607.21419 |
| Code | none located |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.21419-pats-policy-aware-training-scaffolding-for-agent.pdf` |
| Retrieved | 2026-07-24 |

## Narrative

Weak agent policies repeat failures → uninformative rollouts. **PATS** reframes skills as a **dynamic training scaffold**: rollout groups → evidence cards → adjust next-rollout context. Guidance for weak policies; fade/remove as policy improves. Scaffold discarded at deploy. ALFWorld/WebShop: **up to +18.6%** vs strong baselines; search-QA competitive with **32.1% fewer prompts**.

### Steal

1. Training-time scaffolds ≠ deploy-time crutches — fade explicit guidance
2. Convert failure clusters into evidence cards for next rollouts (pairs with experiential abstractions)
3. Cyber agent training: scaffold scope/tool policy hints then remove

## Snippets

> "On ALFWorld and WebShop, Pats improves over strong baselines by up to 18.6%… using 32.1% fewer prompts"
[Source: arxiv-2607.21419 abstract/body]
