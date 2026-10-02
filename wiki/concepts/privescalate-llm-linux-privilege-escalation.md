---
title: "PrivEscalate — LLM Linux priv-esc measurement (K331)"
type: concept
tags: [concept, offensive-security, linux, priv-esc, agent, lab-only, k331]
keywords: [2609.09087, PrivEscalate, Linux privilege escalation, LLM agents, executable verification]
related:
  - concepts/kalibench-nl-to-cli-tool-use-eval.md
  - sources/arxiv-2610-02206-kalibench-nl-to-cli-cybersecurity-tool-use.md
  - sources/arxiv-2609-09087-privescalate-llm-linux-privesc.md
  - concepts/privilege-escalation.md
  - concepts/linux-pentest.md
  - concepts/llm-pentest-automation.md
  - concepts/faithful-agent-asr-measurement.md
maturity: draft
created: 2026-09-11
updated: 2026-10-02
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K331)"
---

## Relations

- @concepts/kalibench-nl-to-cli-tool-use-eval.md — K387-K391 cross-link
- @sources/arxiv-2610-02206-kalibench-nl-to-cli-cybersecurity-tool-use.md — K387-K391 ingest source page
- @sources/arxiv-2609-09087-privescalate-llm-linux-privesc.md — PrivEscalate: Measuring and Augmenting the Threat of LLM-Automated Linux Privilege Escalation (2609.09087)

## Raw Concept

Question: **PrivEscalate — LLM Linux priv-esc measurement** — what should operators steal from this paper?

## Narrative

LLM agents are increasingly used across the kill chain, but **Linux privilege escalation** evaluations have been limited to small scenario sets. **K331 (PrivEscalate)** scales measurement with **executable verification** and augmentation of the threat model. **Authorized lab / owned targets only** — no priv-esc exploit recipes in wiki. Report ASR with scenario count, verification mode, and model/agent harness; pairs K271 faithful ASR.

## Snippets

> Large-scale Linux priv-esc benchmark with executable verification for LLM-automated post-exploitation. [Source: arXiv 2609.09087 abstract]
