---
title: "Bug-Bounty-Agents — 43 offensive-security agent personas"
type: entity
tags: [tool, bug-bounty, offensive-agents, persona-patterns, mit, offensive-security]
keywords: [bug-bounty-agents, 43 personas, offensive agents, mit, persona prompting]
related:
  - concepts/bug-bounty.md
  - concepts/llm-pentest-automation.md
  - "@osint-wiki/entities/tools/bug-bounty-agents.md"
  - "@osint-wiki/sources/evaluating-project-links-systems-2-2026-05-12.md"
maturity: draft
created: 2026-05-12
updated: 2026-05-15
osint_eval_origin: doc2-url-22 (cross-routed; cybersec primary)
---

## Relations

- @concepts/bug-bounty.md — primary deployment context for the 43 offensive-security personas
- @concepts/llm-pentest-automation.md — methodology umbrella; persona-prompting variant of LLM-pentest automation
- `@osint-wiki/entities/tools/bug-bounty-agents.md` — OSINT cross-route stub
- `@osint-wiki/sources/evaluating-project-links-systems-2-2026-05-12.md` — origin eval (URL 22)

## Raw Concept

- **License**: MIT
- **Tier**: Steal-from / Adopt-candidate

## Narrative

43-persona offensive-security agent library. Personas are pre-defined prompt configurations specialized by attack class (SQLi-focused, XSS-focused, business-logic-focused, etc.). Each persona is a constrained agent role — they don't fight, they coordinate via task assignment.

### Phase-0 audit pending

Verify persona quality (are they actually specialized or just renamed copies of the same prompt?), MIT compliance, install/run experience, supported LLM backends.
