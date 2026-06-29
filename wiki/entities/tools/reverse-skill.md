---
title: reverse-skill — security research skill router pack
type: entity
tags: [tool, offensive, skills, pentest, skill-router, mit, k129]
keywords: [reverse-skill, zhaoxuya520, skill router, penetration testing, claude code, cursor]
related:
  - concepts/llm-pentest-automation.md
  - concepts/red-team-operations.md
  - entities/tools/offensive-claude.md
  - entities/claude-red-offensive-skills.md
  - entities/tools/pentest-ai-agents.md
  - concepts/agent-skill-injection.md
  - concepts/mcp-security-posture.md
  - "@osint-wiki/entities/tools/reverse-skill.md"
maturity: draft
created: 2026-06-27
updated: 2026-06-27
phase_0_verdict: "GO 2026-06-25 — github.com/zhaoxuya520/reverse-skill MIT, ~6.2k★; authorized pentest skill routing before MCP tool invocation"
---

## Relations

- @concepts/llm-pentest-automation.md — Tier-2 methodology; router sits above tool execution
- @entities/tools/offensive-claude.md — sibling Claude Code offensive workstation pattern
- @osint-wiki/entities/tools/reverse-skill.md — OSINT cross-route stub (K129 eval provenance)

## Raw Concept

K129 Adopt (`briefs/2026-06-25_k129-reverse-skill-adopt.md`, 2026-06-25). Repo: [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill), **MIT**, ~6.2k★.

## Narrative

**reverse-skill** is a **skill router pack** for authorized penetration testing and reverse-engineering workflows. Classifies offensive tasks and routes to optimal AI methodology (RULES.md → Skill Router → MCP execution) before broad tool invocation.

### Phase-0 summary

| Check | Result |
|-------|--------|
| License | MIT `[CONFIRMED]` |
| Maturity | ~6.2k★; active 2026-06 |
| vs pentest-ai-agents | Router taxonomy vs composable agent framework — complementary |
| vs offensive-claude | Curated skill modules vs monolithic workstation install |

**Verdict: GO** for authorized Tier-2 pentest stacks — install only on scoped engagement machines; pair with @concepts/mcp-security-posture.md allowlist + SkillSpector pre-scan.

See `briefs/2026-06-25_k129-reverse-skill-adopt.md`.

## Snippets

[Source: github.com/zhaoxuya520/reverse-skill README]
