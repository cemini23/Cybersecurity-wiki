---
title: "PrivEscalate — LLM-automated Linux privilege escalation eval (arXiv 2609.09087)"
type: source
tags: [source, arxiv, offensive-security, linux, priv-esc, agent, lab-only, k331]
keywords: [2609.09087, PrivEscalate, Linux privilege escalation, LLM agents, executable verification]
related:
  - concepts/privescalate-llm-linux-privilege-escalation.md
maturity: draft
read_status: read
created: 2026-09-11
updated: 2026-09-11
phase_0_verdict: "REFERENCE 2026-09-11 — LLM priv-esc eval bench; authorized lab only; no exploit bodies in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K331)"
---

## Relations

- @concepts/privescalate-llm-linux-privilege-escalation.md — K331 concept

## Raw Concept

| Field | Value |
|-------|-------|
| Title | PrivEscalate: Measuring and Augmenting the Threat of LLM-Automated Linux Privilege Escalation |
| arXiv | 2609.09087 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609.09087-privescalate-measuring-and-augmenting-the-threat.pdf |
| Retrieved | 2026-09-11 |
| Read status | read (abstract + triage) |

## Narrative

LLM agents are increasingly used across the kill chain, but **Linux privilege escalation** evaluations have been limited to small scenario sets. **K331 (PrivEscalate)** scales measurement with **executable verification** and augmentation of the threat model. **Authorized lab / owned targets only** — no priv-esc exploit recipes in wiki. Report ASR with scenario count, verification mode, and model/agent harness; pairs K271 faithful ASR.

## Snippets

> Large-scale Linux priv-esc benchmark with executable verification for LLM-automated post-exploitation. [Source: arXiv 2609.09087 abstract]
