---
title: "AIRecon — autonomous pentest agent"
type: entity
tags: [tool, autonomous-pentest, ai-agent, recon, mit, offensive-security]
keywords: [airecon, autonomous pentest, ai recon, pentest-state pattern, mit]
related:
  - "@osint-wiki/entities/tools/airecon.md"
  - "@osint-wiki/sources/evaluating-project-links-systems-2-2026-05-12.md"
  - concepts/llm-vulnerability-discovery.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
osint_eval_origin: doc2-url-6 (cross-routed from OSINT eval as cybersec-primary)
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

### Phase-0 audit pending

Verify maturity (stars, commits, recency), supported recon targets, integration with existing scanner toolchain. File deeper eval after Phase-0.
