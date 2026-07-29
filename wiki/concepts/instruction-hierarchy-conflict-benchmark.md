---
title: Instruction-hierarchy conflict robustness (IH-B)
type: concept
tags: [concept, instruction-hierarchy, mcp, agent-security]
keywords: [IH-Benchmark, S≻U, U≻T, tool output override, 2607.25987]
related:
  - sources/arxiv-2607-25987-ih-benchmark-instruction-hierarchy.md
  - concepts/system-prompt-leakage.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-07-29
updated: 2026-07-29
---

## Relations

- @sources/arxiv-2607-25987-ih-benchmark-instruction-hierarchy.md
- @concepts/system-prompt-leakage.md
- @concepts/mcp-security-posture.md
- @concepts/agent-runtime-guardrails.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

SYSTEM ≻ USER is not the same skill as USER ≻ TOOL when tool outputs inject conflicting instructions.

## Narrative

IH-B stress-tests both edges with 2,336 conflict scenarios. Models that hold system constraints under user pressure often collapse when the conflict arrives via tool output. Subtle injections (disclaimers, small factual lies) are often more successful than overt policy violations. For MCP/agent stacks: eval U≻T separately; never treat S≻U leaderboard as tool-robustness. [CONFIRMED abstract; harness pending public release]
