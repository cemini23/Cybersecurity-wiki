---
title: "AIRGuard: Guarding Agent Actions with Runtime Authority Control (arXiv:2605.28914)"
type: source
tags: [arxiv, agent-security, runtime-guard, authority-confusion, mcp, research-paper]
keywords: [airguard, authority confusion, least privilege, agenttrap, dtap-150, runtime authorization]
related:
  - concepts/agent-runtime-guardrails.md
  - entities/tools/airguard.md
  - concepts/llm-adversarial-fuzzing.md
  - entities/tools/nvidia-skillspector.md
  - sources/arxiv-2606-02240-agentredbench.md
  - sources/arxiv-2606-20023-over-privileged-tool-selection-toolprivbench.md
  - concepts/agent-least-privilege-tool-selection.md
maturity: draft
read_status: read
created: 2026-06-01
updated: 2026-06-19
---

## Relations

- @concepts/agent-runtime-guardrails.md — authority-confusion failure mode + runtime guard pattern
- @entities/tools/airguard.md — open-source implementation (MIT)
- @concepts/llm-adversarial-fuzzing.md — distinct from jailbreaks; agent side-effect attacks
- @entities/tools/nvidia-skillspector.md — pre-install skill audit vs AIRGuard action-time enforcement

## Raw Concept

- **Title**: AIRGuard: Guarding Agent Actions with Runtime Authority Control
- **Authors**: Suliu Qin, Haomin Zhuang, Yujun Zhou, Yufei Han, Xiangliang Zhang
- **Type**: arXiv preprint
- **Location**: `raw-sources/arxiv-2605.28914-airguard-guarding-agent-actions-with-runtime-aut.pdf`
- **URL**: https://arxiv.org/abs/2605.28914
- **Code**: https://github.com/Sophie508/AIRGuard
- **Retrieved**: 2026-06-01
- **Read-status**: read

## Narrative

Identifies **authority confusion**: untrusted content may inform reasoning but must not authorize side effects. AIRGuard enforces least privilege at **action time** — normalizes tool calls, derives step-level authority from task authority, tracks source/target trust, simulates sensitive effects, audits cross-step sequences. AgentTrap: Sonnet 4.6 ASR 36.3% → 5.5%. DTAP-150: 76.0% benign utility (Haiku 4.5) vs ARGUS 52.0% / MELON 42.0%. Ablation: prompt-only policy helps modestly; runtime authority layer is the main gain.

## Snippets

> "Data can inform; only authority can authorize."

> "Evidence is not authority: an argument can be well grounded while the resulting operation is still outside the user's authorized scope."
