---
title: "The agent memory layer is a supply-chain target (K283-b)"
type: concept
tags: [concept, agent-security, k283-b]
keywords: [WuBlock/SlowMist 2026-10-06, K283-b]
related:
  - concepts/coding-agent-supply-chain-install-gap.md
  - sources/wublock-2026-10-06-memtensor-agent-memory-supply-chain.md
  - concepts/agent-skill-injection.md
maturity: draft
created: 2026-10-07
updated: 2026-10-09
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K283-b)"
---

## Relations

- @concepts/coding-agent-supply-chain-install-gap.md — K408-K417 ingest / 2026-10-09
- @sources/wublock-2026-10-06-memtensor-agent-memory-supply-chain.md
- @concepts/agent-skill-injection.md

## Raw Concept

Question: **The agent memory layer is a supply-chain target** — operator steal from the inbound brief (WuBlock/SlowMist 2026-10-06)?

## Narrative

A poisoned **tool** leaks what that tool can reach. A poisoned **memory package** leaks the agent's **entire context** — that is what a memory layer is for. Add install-time execution (the MemoryOS PyPI/npm case shipped a Go binary that ran on import) and you have the worst combination in an agent stack: **code that runs on install, holding the full context.**

Operator rules: treat the memory package as **privileged**, not as a library; pin versions and review diffs; and know that on compromise the response is **uninstall/downgrade, kill processes, review egress, rotate exposed credentials** — rotating credentials is the step people skip, and it is the one that matters because the context has already left. This is the memory-layer instance of the install-gap pattern.

## Snippets

> Synthesised from the routed inbound brief. [Source: `briefs/` inbound route (2026-10-07)]
