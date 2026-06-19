---
title: Over-privileged tool selection in LLM agents — TOOLPRIVBENCH (arXiv 2606.20023)
type: source
tags: [source, arxiv, agent-security, least-privilege, tool-selection, toolprivbench, mcp]
keywords: [2606.20023, toolprivbench, opur, over-privileged tool selection, premature escalation, ped]
related:
  - concepts/agent-least-privilege-tool-selection.md
  - entities/tools/toolprivbench.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-skill-injection.md
  - concepts/agentic-containment-principles.md
  - concepts/ai-for-cybersecurity.md
  - concepts/zero-trust.md
  - entities/tools/airguard.md
  - entities/tools/chaincaps.md
  - sources/arxiv-2605-28914-airguard-guarding-agent-actions.md
  - sources/arxiv-2606-03024-skillguard-permission-framework.md
maturity: draft
read_status: read
created: 2026-06-19
updated: 2026-06-19
phase_0_verdict: "Reference 2026-06-19 — TOOLPRIVBENCH repo AISafetyHub/agent-tool-selection-bias: README claims MIT, gh api LICENSE null/404; benchmark methodology only until SPDX filed"
---

## Relations

- @concepts/agent-least-privilege-tool-selection.md — synthesized OPUR/PED framework + mitigation ladder
- @entities/tools/toolprivbench.md — benchmark entity + Phase-0 gate
- @concepts/mcp-security-posture.md — least-privilege tool choice complements admission/DCI/SPI stack

## Raw Concept

| Field | Value |
|-------|-------|
| Title | When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents |
| Authors | Kaiyue Yang, Yuyan Bu, Jingwei Yi, Yuchi Wang, Biyu Zhou, Juntao Dai, Songlin Hu, Yaodong Yang |
| Affiliations | CAS IIE, BAAI, CUHK, PKU |
| arXiv | 2606.20023v1 [cs.SE] |
| Code | [github.com/AISafetyHub/agent-tool-selection-bias](https://github.com/AISafetyHub/agent-tool-selection-bias) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2606.20023-when-lower-privileges-suffice-investigating-over.pdf` |
| Retrieved | 2026-06-19 |
| Read status | **read** (abstract, §3–5, mitigation §5, results tables) |

## Narrative

Identifies **over-privileged tool selection** — agents choosing or escalating to higher-privilege tools when lower-privilege alternatives are **functionally sufficient** (orthogonal to external enforcement like SkillGuard/AIRGuard: this is **internal agent behavior** among authorized tools).

### Behavioral modes

| Mode | PED | Definition |
|------|-----|------------|
| **Aggressive selection** | 0 | First tool choice is higher-privilege despite untried lower-privilege sufficient tools |
| **Premature escalation** | ≥1 | After transient, privilege-unrelated failures (e.g. HTTP 503), agent escalates before exhausting lower-privilege alternatives |

Formal criterion: at step *i*, selecting tool *t_h* is over-privileged if ∃ *t_ℓ* ∈ untried sufficient tools with *p(t_ℓ) < p(t_h)*.

### TOOLPRIVBENCH

- **544** validated scenarios; **8 domains** (Database, Business, Education, Coding, Gov, Health, Media, Infra); **5 risk types** (Authority Escalation, Scope Expansion, Temporal Persistence, Safety Bypass, Data Over-Exposure)
- Each case: user task + **6 tools** (3 lower-privilege + 3 higher-privilege), all independently sufficient under non-error conditions
- Multi-turn eval (k=5); transient failures injected into lower-privilege calls to test escalation under friction
- Tool sufficiency validated via dual-judge consensus (Gemini 2.5 Pro + GPT-5.2) + human expert audit
- Risk taxonomy derived from APIGen tool clusters (L1–L5 exposure scale); synthetic tools to control privilege contrast

### Key empirical findings

1. **OPUR is widespread:** 6/11 models >30% OPUR; open-weight small models worst (Qwen3-8B **64.9%**, LLaMA-3.1-8B **55.9%**); frontier aligned models lower (Claude 4.6 Sonnet ~**2.6%** total OPUR in Figure 4, GPT-5.2 **9.7%**, GLM-5 **8.6%**)
2. **Transient failures amplify escalation:** models shift OPUR mass from PED=0 to PED=1/2 after privilege-unrelated errors — "capability uncertainty" drives over-provisioning
3. **Domain/risk asymmetry:** Infra/K8s debugging highest OPUR for many models; Authority Escalation + Safety Bypass dominate risk types; Scope Expansion lower
4. **General safety alignment ≠ least privilege:** AgentAlign cuts AgentHarm harmful score (67.4→10.5% Ministral) but OPUR barely moves (68.8→62.5%) or **increases** (Qwen 50.4→60.7%)
5. **Prompt SECURITY PRINCIPLE block:** modest OPUR reduction; weakens after failed lower-privilege attempts
6. **Privilege-aware post-training (SFT + GRPO):** strongest mitigation — Qwen3-8B OPUR 64.9→**27.0%**; Qwen3-4B-think 66.0→**18.9%**; general capability largely stable (MMLU/GSM8K/MetaTool retain >95%)

### Cybersecurity relevance

- **MCP / prod-mcp:** exposing admin/write tools alongside read-scoped alternatives creates the exact sufficient-alternative confound TOOLPRIVBENCH isolates — agents may pick `run_shell` when `read_file` suffices
- **Red team:** test HTTP 503 / timeout on narrow tools → observe privilege escalation to broad MCP servers
- **Blue team:** runtime authority narrowing (AIRGuard) + closed allowlists address **external** bounds; this paper shows **model-internal** preference for broader tools still fires inside authorized sets
- **Vibe-coding / agent-built apps:** anecdotal over-permissive backend patterns may stem from agent path preference, not inability to build secure configs

## Snippets

[Source: arxiv-2606.20023 abstract]

> We refer to this behavior as over-privileged tool selection. … General safety alignment does not reliably transfer to least-privilege tool choice, while prompt-level controls provide only limited mitigation under transient failures.

[Source: arxiv-2606.20023 §3.1 Eq. 1]

> If the agent selects a_i = t_h such that ∃ t_ℓ ∈ U_i(x) with p(t_ℓ) < p(t_h), then the choice at step i is over-privileged.

[Source: arxiv-2606.20023 Table 2 — AgentAlign mismatch]

> Learning to refuse explicitly harmful agent requests does not automatically teach an agent to prefer the minimally privileged sufficient tool among authorized options.

## Dead Ends

- **Treating OPUR as injection ASR** — all tools are authorized; failure is privilege preference not unauthorized access
- **Installing TOOLPRIVBENCH repo without LICENSE** — README MIT badge but no LICENSE file on GitHub API (2026-06-19); Reference until SPDX verified
- **Prompt-only least-privilege on prod agents under flaky tools** — paper shows PE degrades when lower-privilege tools return transient errors; need runtime narrowing or retry policy in harness
