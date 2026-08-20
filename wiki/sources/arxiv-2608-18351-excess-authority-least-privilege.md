---
title: "Task-conditioned least-privilege learning — excess authority (arXiv 2608.18351)"
type: source
tags: [source, arxiv, agent-security, least-privilege, ccc-k290]
keywords: [2608.18351, excess authority, least-privilege learning, MCP, terminal agents]
related:
  - concepts/task-conditioned-excess-authority.md
  - concepts/agent-least-privilege-tool-selection.md
  - concepts/mcp-security-posture.md
  - concepts/counterfactual-simulatability-llm-explanations.md
maturity: draft
read_status: read
created: 2026-08-20
updated: 2026-08-20
phase_0_verdict: "REFERENCE 2026-08-20 — no public code. CCC K290 (≠ Cybersec K290 CHIVE 2608.16747). Policy wire only."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (CCC K290 excess-authority axis)"
---

**Briefs:** `briefs/2026-08-20_k290-excess-authority-from-ccc.md`

## Relations

- @concepts/task-conditioned-excess-authority.md
- @concepts/agent-least-privilege-tool-selection.md
- @concepts/mcp-security-posture.md
- @concepts/counterfactual-simulatability-llm-explanations.md — **Dual-ID:** Cybersec K290 = CHIVE, not this paper

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Task-Conditioned Least-Privilege Learning for Executable Terminal and MCP Agents |
| Authors | Alexander Tu, Michael Tu |
| arXiv | 2608.18351 (cs.CR, v1 18 Aug 2026) |
| Code | none public |
| Retrieved | 2026-08-20 via CCC inbound brief (no new PDF in cyber inbox) |
| Read status | read (abstract + inbound brief) |

## Narrative

Tool-using agents can complete a task while exercising authority the user did not grant or the task does not need (**excess-authority errors**). Permission gates alone are insufficient. The paper post-trains a 4B model (Qwen3.5-4B, 1,500 tasks) to choose **task-conditioned** authority: each action is audited pre-execution and from observed effects along a **six-dimensional deterministic** risk vector; trajectories are scored against a per-task sufficient-authority envelope. Held-out: 98.48% safe success vs 64.36% base; excess-authority events 4.56% → 0.79% (2,896 episodes / 500 tasks). Learned restraint **complements** gates, signed mandates (CCC Mandato K285), and sandboxing — it does not replace them. [TENTATIVE] single paper; no public artifact.

**Dual-ID (mandatory):** CCC **K290** = this paper. Cybersec **K290** = CHIVE (2608.16747). Never reuse Cybersec K290 for excess-authority.

## Snippets

> Learned restraint through least-privilege aware post-training is therefore useful as an additional control layer … but it does not replace permission gates and sandboxing. [Source: arXiv 2608.18351 abstract]
