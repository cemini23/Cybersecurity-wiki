---
title: "rea — agent-first reverse-engineering toolkit and MCP server"
type: entity
tags: [entity, tool, agent-security]
keywords: [github.com/morluto/rea, K285-b]
related:
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/llm-vulnerability-discovery.md
maturity: draft
created: 2026-10-09
updated: 2026-10-09
phase_0_verdict: "EXTRACT K285 — MIT, high-star, technique mature. Requires local Hopper + authorized scope. No clone this batch."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K285-b)"
---

## Relations

- @concepts/local-abliterated-llm-pentest-stack.md — K408-K417 ingest / 2026-10-09
- @concepts/llm-vulnerability-discovery.md — K408-K417 ingest / 2026-10-09

## Raw Concept

rea — agent-first reverse-engineering toolkit and MCP server — evaluated from the inbound routed brief (github.com/morluto/rea).

## Narrative

**MIT, 19,363 stars.** 'Reverse engineer anything with agents, from app behaviour down to native binaries.' An **agent-first reverse-engineering toolkit and MCP server** that bridges Claude / Cursor into **Hopper disassembly and execution tracing**.

**Why it is notable here.** This was a **Pass in K283** and is an **Extract here** — a re-evaluation, because the technique it names (MCP-mediated decompilation) is now mature enough to be routine. **Hard gate:** it needs a **local Hopper Disassembler** and must stay inside a **whitehat authorized scope**. The pattern is filed; **no PoC, no exploit steps, no payloads.**

## Snippets

> Verified from the routed brief, not a first-hand repo audit. [Source: `briefs/` inbound route (2026-10-09)]
