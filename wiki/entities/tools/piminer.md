---
title: PIMiner
type: entity
category: tool
tags: [entity, tool, agent-security, mit, conditional-go, lab]
keywords: [PIMiner, prompt injection, red team, Claude Code]
related:
  - sources/arxiv-2608-05108-piminer-prompt-injection-redteam.md
  - concepts/piminer-agentic-prompt-injection-redteam.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/ai-for-cybersecurity.md
  - concepts/prompt-injection-detector-calibration.md
  - concepts/local-abliterated-llm-pentest-stack.md
maturity: draft
created: 2026-08-06
updated: 2026-08-06
phase_0_verdict: "CONDITIONAL-GO 2026-08-06 — MIT; ~28MB; github.com/Wang-Yanting/PIMiner"
wire_status: deferred
wire_target: "owned lab only — Claude Code CLI required; no LIVE"
---

## Relations

- @sources/arxiv-2608-05108-piminer-prompt-injection-redteam.md
- @concepts/piminer-agentic-prompt-injection-redteam.md
- @concepts/llm-adversarial-fuzzing.md
- @concepts/ai-for-cybersecurity.md

**Local clone:** `raw-sources/repos/PIMiner` (~28MB)
- @concepts/prompt-injection-detector-calibration.md
- @concepts/local-abliterated-llm-pentest-stack.md

## Narrative

### Phase-0 (2026-08-06): CONDITIONAL-GO

| Gate | Status |
|------|--------|
| License | **PASS** — MIT |
| Size | **PASS** — ~28MB shallow |
| Contents | strategy library + iterative attack orchestrator; dual-use red-team |
| Prereq | Claude Code CLI (attacker/router); target API keys in `.env` |
| Verdict | **CONDITIONAL-GO** — clone for lab REFERENCE/run; **do not** `npm i -g` Claude Code or run against LIVE without operator OK |

Human gate: written lab scope + no third-party production agents.
