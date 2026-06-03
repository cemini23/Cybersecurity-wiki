---
title: Agent skill injection — attack surface and defenses (K95 cluster)
type: concept
tags: [concept, agent-security, skill-injection, mcp, k95]
keywords: [skill injection, SkillGuard, context poisoning, confused deputy, agent skills]
related:
  - sources/arxiv-2606-00485-confused-chatgpt-cross-app-context-poisoning.md
  - sources/arxiv-2606-01567-skill-injection-defenses-enablers.md
  - sources/arxiv-2606-03024-skillguard-permission-framework.md
  - concepts/agent-runtime-guardrails.md
  - "@ccc-wiki/concepts/skill-vetting.md"
maturity: draft
created: 2026-06-03
updated: 2026-06-03
---

## Relations

- @sources/arxiv-2606-00485-confused-chatgpt-cross-app-context-poisoning.md — cross-app context poisoning
- @sources/arxiv-2606-01567-skill-injection-defenses-enablers.md — defense/enabler taxonomy
- @sources/arxiv-2606-03024-skillguard-permission-framework.md — SkillGuard permissions
- @ccc-wiki/concepts/skill-vetting.md — Cemini Phase-0 skill audit (steal permission model)

## Narrative

K95 cluster (2026-06-03 daily digest): three papers on **agent skill / context injection** — platform-level confused-deputy poisoning (ChatGPT Apps), skill-file attack surfaces on coding agents, and **SkillGuard** permission framework.

| Paper | arXiv | Takeaway |
|-------|-------|----------|
| Confused ChatGPT | 2606.00485 | Flat shared context + first-party APIs → cross-app poisoning |
| Defenses & enablers | 2606.01567 | Taxonomy of mitigations vs attack enablers on skill injection |
| SkillGuard | 2606.03024 | Permission framework for agent skills — steal-for skill_audit |

**Cemini relevance:** extend `skill-vetting.md` + prod MCP governance (K94 brief) with permission metadata; no SkillGuard vendor install without Phase-0.
