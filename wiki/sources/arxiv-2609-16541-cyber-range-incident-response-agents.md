---
title: "Cyber range evaluation of autonomous network incident response agents (arXiv 2609.16541)"
type: source
tags: [source, arxiv, agent-security, blue-team, soc, cyber-range, eval, k340]
keywords: [2609.16541, cyber range, incident response agents, SIEM, autonomous defense]
related:
  - concepts/cyber-range-autonomous-incident-response-agents.md
maturity: draft
read_status: read
created: 2026-09-16
updated: 2026-09-16
phase_0_verdict: "REFERENCE 2026-09-16 — cyber-range IR agent eval; no clone until SPDX verified."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K340)"
---

## Relations

- @concepts/cyber-range-autonomous-incident-response-agents.md — K340 concept

## Raw Concept

| Field | Value |
|-------|-------|
| Title | A Cyber Range Evaluation of Autonomous Network Incident Response Agents |
| arXiv | 2609.16541 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.16541-a-cyber-range-evaluation-of-autonomous-network-i.pdf |
| Retrieved | 2026-09-16 |
| Read status | read (abstract + triage) |

## Narrative

Autonomous **network incident response** agents are increasingly evaluated outside single-host sandboxes. **K340** tests defensive agents in a **cyber range** with variable topology, red-team emulation, simulated users, and SIEM-mapped alerts. Success requires blocking red-team host access while **minimizing availability cost** from defensive actions. **Audit steal:** report containment outcomes with availability tradeoffs and evidence path — alert closure ≠ verified containment (pairs K278/K330). Authorized lab / cyber-range scope only.

## Snippets

> Cyber-range eval of autonomous IR agents balancing intrusion prevention vs defensive availability cost. [Source: arXiv 2609.16541 abstract]
