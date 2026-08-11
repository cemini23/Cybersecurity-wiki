---
title: "SHE: Trajectory-driven Safety Harness Evolution for LLM Agents (arXiv 2608.09885)"
type: source
tags: [source, arxiv, agent-security, harness-evolution, guardrail]
keywords: [2608.09885, SHE, safety harness, Agent-SafetyBench, AgentHarm, Rule Bank, Safety Memory, Tool Policy]
related:
  - concepts/safety-harness-evolution.md
  - entities/tools/she-safety-harness-evolution.md
  - concepts/agent-runtime-guardrails.md
  - concepts/harnessopt-bench.md
  - concepts/self-evolving-agent-security.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-08-11
updated: 2026-08-11
phase_0_verdict: "GO 2026-08-11 — Apache-2.0, shallow clone ~4.7MB (raw-sources/repos/SHE). K268 policy wire + lab adopt."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc + cemin-cybersec-lab-redteam.mdc (K268)"
---

**Briefs:** `briefs/2026-08-11_k268-she-harness-evolution.md`

## Relations

- @concepts/safety-harness-evolution.md
- @entities/tools/she-safety-harness-evolution.md
- @concepts/agent-runtime-guardrails.md
- @concepts/harnessopt-bench.md
- @concepts/self-evolving-agent-security.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | SHE: Trajectory-driven Safety Harness Evolution for LLM Agents |
| Authors | Qu, Mao (Shanghai AI Lab / SJTU); Li, Liu, Zhang, Guo, Zhu, Liu, Yuan, Lin, Zhu, Fu, Shao, Hu, Liu (AgentDoG Team) |
| arXiv | 2608.09885 |
| Code | https://github.com/RainbowQTT/SHE @ `0c656460` · Apache-2.0 · local `raw-sources/repos/SHE` (~4.7MB) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.09885-she-trajectory-driven-safety-harness-evolution-f.pdf` |
| Retrieved | 2026-08-11 |
| Read status | read (15 pp) |

## Narrative

SHE treats the **agent harness** (context, memory, tools, permissions, runtime control) as an evolvable safety object rather than a fixed deployment artifact. It decomposes the harness into four artifacts with explicit safety responsibilities:

| Artifact | Responsibility |
|----------|----------------|
| **System Prompt** | Global behavioral contract: source hierarchy, capability grounding, trust-boundary commitments |
| **Rule Bank** | Structured safety rules for risk classification + intervention (allow/warn/block/sanitize/judge) |
| **Safety Memory** | Experience from failure cases unresolved after repeated evolution attempts |
| **Tool Policy** | Tool authority + runtime enforcement for calls, observations, blocked actions, final-response recovery |

**Attribution-guided evolution loop** (Algorithm 1): per round → rollout under current best harness → `RiskRelevant` cases → structured diagnosis along three axes (harm domain · attack surface · failure mode) → artifact routing → bounded local edit → validity check (rejects reward-hacking/evaluator-specific shortcuts) → safety–utility selection `S(Ĥ)>S(Hbest) ∧ U(Ĥ)≥U(Hbest)` → rejection feedback `Frej` for later rounds.

Results:
- Agent-SafetyBench: ASR 8.6%→5.5%, Clean UBR 25.7%→19.8%, UA 33.5%→47.6% (evolved).
- vs static SafeHarness: 3.1× lower ASR (17.1%→5.5%) and +50.6% UA (31.6%→47.6%).
- Held-out AgentHarm: Harm Score 19.8%→9.8%, Harm Refusal 78.4%→86.4%.
- Cross-agent transfer: evolved on DeepSeek-V3.2, applied to Kimi K2.6 / GLM-5.2 / MiniMax M2.7 without re-evolution.
- Evolution-model ablation: GPT-5.5, DeepSeek-V3.2, GLM-5.2 all improve the seed; GPT-5.5 is the most utility-preserving.

Setup: 20 evolution rounds over a 15-task split (90 task-condition instances, 180 trajectories/round); the other 185 tasks held out. Component replacement ablation (⋆ rows) confirms each learned artifact matters.

`[CONFIRMED]` — results from paper tables + repo smoke tests consistent with README; independent lab repro of the 3.1× ASR claim not yet run.

## Snippets

> SHE evolves an explicit safety harness for tool-using LLM agents from execution trajectories. Rather than treating safety as a single monolithic prompt, it separates the harness into a System Prompt, Rule Bank, Safety Memory, and Tool Policy. [Source: github.com/RainbowQTT/SHE README]

> Compared with the static SafeHarness baseline, SHE lowers ASR from 17.1% to 5.5% and improves average UA from 31.6% to 47.6%. [Source: arXiv:2608.09885 abstract]

## Dead Ends

- SHE is a harness/artifact evolution loop, **not** a model-weight trainer and **not** an attack generator — do not treat it as a red-teaming tool.
- Evolution relies on an LLM judge/diagnosis model (GPT-5.5 in paper) — the validity check mitigates reward-hacking, but judge quality still bounds evolution.
- Repo smoke tests exist but no end-to-end benchmark rerun yet in this workspace; treat headline ASR as paper-reported `[CONFIRMED]` pending local reproduction.
