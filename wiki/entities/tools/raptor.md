---
title: "raptor — Claude Code offensive/defensive security agent (Semgrep + CodeQL)"
type: entity
tags: [tool, llm-automation, static-analysis, claude-code, semgrep, codeql, offensive, defensive, steal-from]
keywords: [raptor, gadievron, claude code agent, semgrep, codeql, static analysis, vuln validation, exploit generation, prompt chaining, sub-agent architecture]
related:
  - concepts/llm-pentest-automation.md
  - concepts/ai-for-cybersecurity.md
  - concepts/bug-bounty.md
  - entities/tools/pentest-ai-agents.md
maturity: draft
created: 2026-05-21
updated: 2026-05-21
cross-wiki-source: @osint-wiki/sources/multi-wiki-tool-eval-prompt-2026-05-18.md
---

# raptor — Claude Code offensive/defensive security agent

## Relations

- @concepts/llm-pentest-automation.md — prompt-chaining + sub-agent architecture reference
- @concepts/ai-for-cybersecurity.md — LLM-driven static analysis pattern
- @concepts/bug-bounty.md — autonomous vuln validation workflow
- @entities/tools/pentest-ai-agents.md — complementary Claude Code agent framework

## Raw Concept

Routed from K51 OSINT-wiki tool eval (2026-05-18). Claude Code wrapper with Semgrep + CodeQL for autonomous static analysis, vuln validation, and exploit generation. Steal-from tier (no license found).

## Narrative

`gadievron/raptor` wraps Claude Code with Semgrep + CodeQL for autonomous static analysis, vulnerability validation, and exploit generation. Self-described as "held together with enthusiasm and duct tape" — high capability, low production readiness.

**Steal-from only** — no license found, so study the architecture (prompt-chaining, sub-agent orchestration, hook wiring) but do not execute on proprietary code. The architectural patterns are the extractable value: how raptor chains Semgrep findings → CodeQL deep-dive → Claude Code exploit generation is a reusable prompt-engineering blueprint.

Also cross-routes to CCC wiki as an apex Claude-Code-orchestration exemplar.
