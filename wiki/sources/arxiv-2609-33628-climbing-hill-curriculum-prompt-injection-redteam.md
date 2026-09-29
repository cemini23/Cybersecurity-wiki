---
title: "Climbing the hill: prompt injection red-teaming against frontier models with curriculum reinforcement learning"
type: source
tags: [source, arxiv, agent-security]
keywords: [2609.33628, k379]
related:
  - concepts/curriculum-prompt-injection-redteam-frontier-models.md
  - concepts/black-box-agentic-redteam-taxonomy.md
maturity: draft
read_status: read
created: 2026-09-29
updated: 2026-09-29
phase_0_verdict: "REFERENCE 2026-09-29 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K379)"
---

## Relations

- @concepts/curriculum-prompt-injection-redteam-frontier-models.md
- @concepts/black-box-agentic-redteam-taxonomy.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Climbing the hill: prompt injection red-teaming against frontier models with curriculum reinforcement learning |
| arXiv | 2609.33628 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.33628-climbing-the-hill-prompt-injection-red-teaming-a.pdf |
| Retrieved | 2026-09-29 |
| Read status | read (abstract + triage) |

## Narrative

**K379** — RL attacker LLMs for prompt injection hit a **cold-start** wall on frontier targets: every attempt fails, reward stays zero, and learning stalls. **Curriculum** training walks the attacker through a sequence of **increasingly robust** targets, with each stage warm-starting from the prior attacker; after each stage the attacker must **partially succeed** on the next target so learning signals continue. Paper reports AgentDyn ASR@10 of **93.8%** / **45.0%** on named frontier pairs where single-shot RL baselines stay at **0%**. Operator steal: document the curriculum and cold-start, use **owned / written-scope frontier lab only**, report harness + judge. **No injection payloads in wiki.** **Runtime:** `scripts/k379_curriculum_pi_redteam_precheck.py`. Pairs K327 black-box agentic red-team taxonomy.

## Snippets

> See arXiv 2609.33628 abstract. [Source: arXiv 2609.33628 (retrieved 2026-09-29)]
