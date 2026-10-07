---
title: "MemTensor / MemoryOS agent-memory supply-chain compromise"
type: source
tags: [source, routed, agent-security]
keywords: [WuBlock / SlowMist report 2026-10-06]
related:
  - concepts/agent-memory-supply-chain-compromise.md
  - concepts/coding-agent-supply-chain-install-gap.md
  - concepts/agent-skill-injection.md
maturity: draft
read_status: read (routed brief)
created: 2026-10-07
updated: 2026-10-07
phase_0_verdict: "REFERENCE 2026-10-07 — routed brief, no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (inbound brief)"
---

## Relations

- @concepts/agent-memory-supply-chain-compromise.md
- @concepts/coding-agent-supply-chain-install-gap.md
- @concepts/agent-skill-injection.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | MemTensor / MemoryOS agent-memory supply-chain compromise |
| Identifier | WuBlock / SlowMist report 2026-10-06 |
| Type | newsletter report (routed by OSINT K283) |
| Location | not held locally — routed brief only |
| Retrieved | 2026-10-07 |
| Read status | read (routed brief) |

## Narrative

**The agent's own memory layer was the payload.** `MemoryOS` **2.0.34** on **PyPI**, and the npm plugin `memtensor/memos-cloud-openclaw-plugin` (versions 0.1.21, 0.1.23, 0.1.25) used with the OpenClaw runtime, shipped a **cross-platform Go binary that executed on load/import**. The npm plugin may also **leak prompt content**.

**Why this is a different class from a poisoned tool.** The wiki already tracks the **setup-instruction supply chain** — docs that become install-time code. This extends it to the **memory package**: compromising it does not leak one tool call, it leaks the agent's **entire context**, because that is what a memory layer holds. Install-time execution plus full-context access is the worst combination available in an agent stack.

**Mitigation as reported (SlowMist):** uninstall or downgrade, kill running processes, review network activity, and **rotate exposed credentials**. **No payload, no binary, no PoC in wiki.**

## Snippets

> Routed brief, not a first-hand read of the source. [Source: `briefs/` inbound route (2026-10-07)]
