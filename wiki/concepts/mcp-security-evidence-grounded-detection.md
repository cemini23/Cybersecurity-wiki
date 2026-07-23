---
title: MCP security — evidence-grounded detection
type: concept
tags: [concept, mcp, security, dynamic-analysis]
keywords: [2607.14754, FlowGuard, runtime evidence]
related:
  - sources/arxiv-flowguard-mcp-security-evidence-2607.14754.md
  - concepts/mcp-security-posture.md
  - concepts/mcp-taint-style-vulnerabilities.md
  - "@ccc-wiki/concepts/mcp-security-signals-vs-runtime-evidence.md"
  - concepts/chainwatch-mcp-kill-chain-detection.md
maturity: draft
created: 2026-07-18
updated: 2026-07-23
---

## Relations

- @sources/arxiv-flowguard-mcp-security-evidence-2607.14754.md — FlowGuard paper
- @concepts/mcp-security-posture.md — MCP admission umbrella
- @ccc-wiki/concepts/mcp-security-signals-vs-runtime-evidence.md — CCC K189 harness checklist

## Raw Concept

When is an MCP “finding” a confirmed execution-path vuln vs semantic suspicion?

## Narrative

Do not equate semantic suspiciousness with confirmed MCP vulnerability when the risk is execution-path. Prefer runtime probes with schema-valid payloads; adjudicate placeholders. CCC owns harness mapping (K189); cybersec keeps detector/ops steal.
