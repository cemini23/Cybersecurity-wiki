---
title: Agent runtime guardrails — attack surfaces + enforcement paradigms
type: concept
tags: [methodology, agent-security, guardrail, mcp, prompt-injection, runtime-enforcement, formal-methods]
keywords: [agent guardrail, authority confusion, permission laundering, sleeper attack, epca, airguard, chaincaps, adaptive attack rate, tool composition safety]
related:
  - concepts/ai-for-cybersecurity.md
  - concepts/llm-adversarial-fuzzing.md
  - concepts/llm-pentest-automation.md
  - concepts/agent-vm-sandboxing.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/responsible-disclosure.md
  - entities/tools/airguard.md
  - entities/tools/chaincaps.md
  - entities/tools/defenseclaw.md
  - entities/tools/nvidia-skillspector.md
  - entities/tools/iron-proxy.md
  - sources/arxiv-2605-29251-provably-secure-agent-guardrail.md
  - sources/arxiv-2605-28914-airguard-guarding-agent-actions.md
  - sources/arxiv-2605-26542-chaincaps-composition-safe-tool-using-agents.md
  - sources/arxiv-2605-28201-plant-persist-trigger-sleeper-attack.md
  - sources/arxiv-2605-30454-agent-prompt-injection-surface-evaluation.md
maturity: draft
created: 2026-06-01
updated: 2026-06-01
---

# Agent runtime guardrails — attack surfaces + enforcement paradigms

## Relations

- @concepts/ai-for-cybersecurity.md — LLM agents in offensive/defensive workflows
- @concepts/llm-adversarial-fuzzing.md — jailbreak/refusal testing vs agent side-effect attacks
- @concepts/llm-pentest-automation.md — Tier-2 agents with MCP tools need runtime guards
- @concepts/agent-vm-sandboxing.md — VM isolation complements but does not replace authority control
- @concepts/crescendo-multi-turn-jailbreak.md — multi-turn jailbreak vs sleeper persist-and-trigger
- @concepts/responsible-disclosure.md — agent guardrail bypass findings follow CVD timelines
- @entities/tools/airguard.md — MIT runtime authority guard (AgentTrap / DTAP-150)
- @entities/tools/chaincaps.md — MCP proxy for composition-safe tool chains
- @entities/tools/defenseclaw.md — enterprise agent governance + MCP scanner
- @entities/tools/nvidia-skillspector.md — skill supply-chain preflight
- @entities/tools/iron-proxy.md — egress firewall for agent workloads
- @sources/arxiv-2605-29251-provably-secure-agent-guardrail.md — ePCA / formal guardrail anchor
- @sources/arxiv-2605-28914-airguard-guarding-agent-actions.md — authority confusion
- @sources/arxiv-2605-26542-chaincaps-composition-safe-tool-using-agents.md — permission laundering
- @sources/arxiv-2605-28201-plant-persist-trigger-sleeper-attack.md — sleeper attack
- @sources/arxiv-2605-30454-agent-prompt-injection-surface-evaluation.md — per-surface eval

## Raw Concept

Synthesized from daily-digest inbox cluster (2026-06-01): five arXiv papers on tool-using agent security — defensive guardrails (ePCA, AIRGuard, ChainCaps) and attack/eval advances (sleeper attack, dual-surface injection).

## Narrative

Tool-using agents (MCP, shell, APIs, email) shift the security problem from **refusal robustness** to **side-effect authorization**. A step can look benign in isolation yet violate policy in composition or across time. This page clusters 2026 research into failure modes, defenses, and evaluation hygiene for pentest/SOC copilot deployments.

### Failure modes (offensive / red-team lens)

| Mode | Mechanism | Source |
|------|-----------|--------|
| **Authority confusion** | Untrusted docs/MCP/skills *inform* reasoning but must not *authorize* writes, sends, or exec | AIRGuard |
| **Permission laundering** | Each tool call passes local ACL; composed workflow exfiltrates (read → summarize → send) | ChainCaps |
| **Sleeper attack** | Payload persists in session/memory/skills; benign later query triggers harm | PLANT |
| **Dual-surface injection** | Same bytes succeed on tool *output* or tool *description* depending on model | Surface paper |
| **Semantic decoupling** | Natural-language intent hides unsafe tool args from LLM-as-Judge guards | ePCA motivation |

These are **not jailbreaks** in the classic sense — the model may comply with user intent while attacker-controlled context steers authorized access off-scope. [CONFIRMED] across AIRGuard + sleeper paper framing.

### Defense paradigms (defensive / blue-team lens)

1. **Formal pre-action verification (ePCA)** — SMT/formal constraints on intended actions before execution; maps unsafe transitions to UNSAT deadlocks. Aims for deterministic lower bound under explicit assumptions. `[TENTATIVE]` — lab validation pending; complements not replaces semantic alignment.

2. **Runtime authority control (AIRGuard)** — Action-time least privilege: task authority → step authority (narrow-only), source/target trust, side-effect simulation, cross-step audit. Prompt-only policy insufficient in paper ablation.

3. **Composition-safe IFC (ChainCaps)** — MCP proxy; sink-specific capability budgets propagate by intersection (monotonic attenuation). Requires **trusted manifests** — naive manifests block only ~27% of attacks in paper.

4. **Stack with existing wiki tools** — @entities/tools/nvidia-skillspector.md (skill preflight), @entities/tools/defenseclaw.md (enterprise governance), @entities/tools/iron-proxy.md (egress), @concepts/agent-vm-sandboxing.md (substrate isolation).

### Evaluation hygiene

- Report **per-surface** ASR (tool output vs tool description), not single-channel headline numbers. [Source: arXiv:2605.30454]
- Use **Adaptive Attack Rate (AAR)** = max ASR over surfaces for the model×task cell.
- Test **multi-session** persist targets (memory, skills), not only single-interaction injection. [Source: arXiv:2605.28201]
- Test **multi-tool compositions**, not isolated tool permissions. [Source: arXiv:2605.26542]

### Pentest / engagement implications

When assessing client agent copilots: poison both MCP tool descriptions and return payloads; attempt persist-via-memory/skill; chain read+transform+external-send; measure whether guards sit **before** tool execution (AIRGuard/ChainCaps pattern) or only in system prompt.

## Snippets

Defense layering (recommended order for authorized lab):

1. Skill/MCP supply-chain scan (SkillSpector)
2. Egress policy (iron-proxy / VM sandbox)
3. Runtime authority or composition proxy (AIRGuard / ChainCaps-class)
4. Formal constraint layer where policy is machine-expressible (ePCA-class) `[NEEDS VERIFICATION 2026-06-01]`

## Dead Ends

- **LLM-as-Judge alone** for high-privilege agents — paper consensus: probabilistic semantic guards lack verifiable lower bound under decoupling attacks.
- **Single-surface ASR** as pass/fail metric — systematically overstates defense and understates attack (Surface paper).
- **Per-tool ACL only** — does not stop permission laundering across composed MCP chains.
