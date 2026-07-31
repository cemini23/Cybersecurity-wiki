---
title: "AIRecon — autonomous pentest agent"
type: entity
tags: [tool, autonomous-pentest, ai-agent, recon, mit, offensive-security]
keywords: [airecon, autonomous pentest, ai recon, pentest-state pattern, mit]
related:
  - "@osint-wiki/entities/tools/airecon.md"
  - "@osint-wiki/sources/evaluating-project-links-systems-2-2026-05-12.md"
  - concepts/llm-vulnerability-discovery.md
  - sources/arxiv-2606-24496-red-teaming-the-agentic-red-team.md
  - concepts/agentic-offensive-security-kill-chain.md
  - concepts/llm-pentest-automation.md
maturity: draft
created: 2026-05-12
updated: 2026-07-31
phase_0_verdict: "CONDITIONAL-GO 2026-06-25 — 2606.24496 flags --network=host worker + orchestrator API abuse; re-audit before Tier-2 adoption"
osint_eval_origin: doc2-url-6 (cross-routed from OSINT eval as cybersec-primary)
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-containment.mdc"
---

## Relations

- `@osint-wiki/entities/tools/airecon.md` — OSINT cross-route stub
- `@osint-wiki/sources/evaluating-project-links-systems-2-2026-05-12.md` — origin Gemini eval (URL 6)
- `@concepts/llm-vulnerability-discovery.md` — methodology synthesis

## Raw Concept

- **License**: MIT
- **Tier**: Steal-from candidate (pentest-state pattern)
- **Origin**: Cross-routed from OSINT wiki Gemini eval as cybersec-primary

## Narrative

Autonomous pentest agent — LLM orchestrates recon + scan + exploit + post-exploit phases with a persistent state machine tracking discoveries. The **pentest-state pattern** is the methodologically interesting bit: explicit state transitions gate next-action selection, preventing the random-step LLM behavior common in early autonomous-agent attempts.

**2606.24496 audit:** AIRecon worker granted `--network=host` among other caps — sandbox escape via orchestrator API (`/api/chat` + host-executed `python_session` pattern). See @concepts/agentic-offensive-security-kill-chain.md before Tier-2 deployment.

### Phase-0 audit pending

Verify maturity (stars, commits, recency), supported recon targets, integration with existing scanner toolchain. File deeper eval after Phase-0.
