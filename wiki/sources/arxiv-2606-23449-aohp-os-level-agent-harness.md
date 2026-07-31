---
title: AOHP — OS-level agent harness on AOSP (arXiv 2606.23449)
type: source
tags: [source, arxiv, agent-harness, android, aosp, os-level]
keywords: [2606.23449, aohp, android open harness project, agent-native os, information flow]
related:
  - entities/tools/aohp.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-vm-sandboxing.md
  - concepts/mcp-security-posture.md
  - concepts/ai-for-cybersecurity.md
  - concepts/mobile-pentest.md
  - sources/arxiv-2606-21071-clawaudit-local-agent-runtime-audit.md
maturity: draft
read_status: read
created: 2026-06-27
updated: 2026-07-31
phase_0_verdict: "CONDITIONAL-GO 2026-06-27 — github.com/aohp-os/aohp Apache-2.0, ~93★; AOSP fork — lab-validate security-policy hooks before production agent deployment"
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-containment.mdc"
---

## Relations

- @entities/tools/aohp.md — AOHP implementation + Phase-0 gate
- @concepts/agent-runtime-guardrails.md — OS-level information-flow controls for agents

## Raw Concept

| Field | Value |
|-------|-------|
| Title | AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction |
| Authors | Shanhui Zhao, Jiacheng Liu, Guohong Liu, et al. |
| Affiliations | Tsinghua University; Peking University; HKU |
| arXiv | 2606.23449 |
| Code | [github.com/aohp-os/aohp](https://github.com/aohp-os/aohp) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2606.23449-2606-23449v1-aohp-an-open-source-os-level-agent.pdf` |
| Retrieved | 2026-06-27 |
| Read status | **read** (architecture, three OS mechanisms, preliminary eval vs stock Android / OpenClaw) |

## Narrative

**AOHP** (Android Open Harness Project) is an AOSP-based **agent-native OS harness** treating agents as first-class actors — not app wrappers. Addresses app-centric OS mismatch: fixed GUIs, single-app lifecycle assumptions, permission boundaries that fail to track sensitive data across agent tool chains.

### Three agent-oriented mechanisms

1. **Personalized service composition** — adaptive UI / capability surfacing for agent consumption
2. **Efficient agent interfaces** — reduced token/execution overhead vs conventional Android agent stacks
3. **Secure information flow** — OS-level policy tracking across agent context + tool calls

### Headline results (preliminary, challenging OS-agent tasks)

| Metric | AOHP vs baseline |
|--------|------------------|
| Task completion | **+21.12%** |
| Token cost | **−51.55%** |
| Security-policy compliance | improved (vs stock Android; OpenClaw comparison cited) |

Compared against stock Android and OpenClaw on overlapping task subset.

### Wiki relevance

Complements harness-layer controls in @concepts/agent-runtime-guardrails.md and sandbox posture in @concepts/agent-vm-sandboxing.md — AOHP moves enforcement **into the OS** rather than app-level guardrails alone. Distinct from MCP transport security (@concepts/mcp-security-posture.md) but relevant for mobile agent pentest labs (@concepts/mobile-pentest.md).

`[TENTATIVE]` — technical report; long-horizon production validation pending.

## Snippets

> "AOHP preserves the mature Android software and hardware ecosystem while introducing three agent-oriented system mechanisms: personalized service composition, efficient agent interfaces, and secure information flow."

> "+21.12% completion rate), execution cost (-51.55% token cost), and security-policy compliance."

[Source: arxiv-2606.23449-2606-23449v1-aohp-an-open-source-os-level-agent.pdf]
