---
title: AI-Infra-Guard Technical Report — multi-layer agent red teaming (arXiv 2606.31227)
type: source
tags: [source, arxiv, agent-security, mcp, ai-red-team, tencent, layer-paradigm]
keywords: [2606.31227, ai-infra-guard, layer-paradigm, mcp-scan, agent-scan, infra-scan, jailbreak]
related:
  - entities/tools/ai-infra-guard.md
  - concepts/layer-paradigm-agent-red-teaming.md
  - concepts/mcp-security-posture.md
  - concepts/agent-skill-injection.md
  - concepts/local-agent-runtime-audit.md
  - concepts/llm-pentest-automation.md
  - entities/tools/nvidia-skillspector.md
  - entities/tools/defenseclaw.md
  - entities/tools/clawaudit.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agentic-containment-principles.md
maturity: draft
read_status: read
created: 2026-07-01
updated: 2026-07-31
phase_0_verdict: "CONDITIONAL-GO 2026-07-01 — Apache-2.0 + NOTICE §4(d); external Docker only; github.com/Tencent/AI-Infra-Guard ~4018★"
wire_status: deferred
wire_target: "External Docker only — ask before runtime"
---

## Relations

- @entities/tools/ai-infra-guard.md — artifact + Phase-0 entity (K44 + refresh)
- @concepts/layer-paradigm-agent-red-teaming.md — layer-paradigm matching synthesis

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Securing the AI Agent: A Unified Framework for Multi-Layer Agent Red Teaming |
| Authors | Yong Yang, Xing Zheng, Huiyu Wu, Huangsheng Cheng, Xiaorong Shi, Jing Guo, Bo Yang, Yi Zhou, Xiangfan Wu, Zonghao Ying (Tencent Zhuque Lab) |
| arXiv | 2606.31227 |
| Code | `github.com/Tencent/AI-Infra-Guard` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2606.31227-ai-infra-guard-technical-report.pdf` |
| Retrieved | 2026-07-01 |
| Read status | **read** (abstract, layer model, four modules, supply-chain motivation, ClawScan adoption note) |

## Narrative

Tencent Zhuque Lab's **technical report** formalizes **AI-Infra-Guard** as a unified open-source agent red-team framework organized around **layer-paradigm matching**: the AI agent attack surface is **stratified** (infrastructure → protocol/tool → agent behavior → model), and each layer needs a **different detection paradigm** — deterministic rules, LLM-driven auditing, black-box runtime probing, or statistical jailbreak evaluation.

### Four layers × modules

| Layer | Paradigm | Module | Mechanism |
|-------|----------|--------|-----------|
| Infrastructure | Deterministic rule matching | **M1 Infra-Scan** | **75+** AI components, **1,400+** vulnerability rules (vLLM, Ollama, ComfyUI, agent platforms, etc.) |
| Protocol / tool | LLM-driven agentic audit | **M2 MCP-Scan** | Static + agentic analysis of MCP servers and tool surfaces |
| Agent behavior | Black-box runtime exposure | **M3 Agent-Scan** | Multi-turn adversarial probing; **agent-skill package** supply-chain auditing |
| Model | Alignment robustness stats | **M4 jailbreak harness** | **26+** attack operators across **sixteen** datasets |

Authors claim this is the only open-source framework spanning **all four** layers including **installable agent skills** as a supply-chain surface — complementary to runtime-only audits (@concepts/local-agent-runtime-audit.md) and admission-layer MCP posture (@concepts/mcp-security-posture.md).

### Positioning vs wiki stack

- **External scanner only** for Cemini IP — Apache-2.0 with **Mandatory Attribution NOTICE (§4(d))** still contaminates vendored derivatives (@entities/tools/ai-infra-guard.md Phase-0).
- **Skill supply chain** — M3 Agent-Scan overlaps SkillGuard / SkillSpector / MalSkillBench eval lanes; use as **breadth scanner**, not sole gate.
- **MCP-Scan** — aligns with DCI/SPI/MSTI layers in @concepts/mcp-security-posture.md; does not replace attested admission or closed allowlists.
- **ClawScan** — paper notes OpenClaw ecosystem **ClawScan** adopted AIG components for agent-skill scanning [TENTATIVE — verify repo linkage on next ClawAudit re-audit].

### Phase-0 (2026-07-01 refresh)

| Gate | Status |
|------|--------|
| License | Apache-2.0 + NOTICE §4(d) mandatory attribution — **external Docker only** |
| Maturity | **~4,018★**, pushed 2026-07-01 |
| Report ↔ code | Technical report documents M1–M4 modules matching public repo layout |
| Verdict | **CONDITIONAL-GO** — landscape entity + lab external scanner; **DO NOT VENDOR** |

## Snippets

> "The framework therefore matches a paradigm to each layer, from deterministic rule matching over 75+ AI components and 1,400+ vulnerability rules, through LLM-driven agentic auditing of MCP servers and agent-skill packages and multi-turn black-box agent red teaming, to a jailbreak harness with 26+ attack operators over sixteen datasets."
[Source: arxiv-2606.31227-ai-infra-guard-technical-report.pdf abstract]

> "To our knowledge it is the only open-source framework to span all of these, including supply-chain auditing of the agent skills that increasingly extend AI agents."
[Source: arxiv-2606.31227-ai-infra-guard-technical-report.pdf abstract]
