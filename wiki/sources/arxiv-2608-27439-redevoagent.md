---
title: "RedEvoAgent — experience-driven red-team skill evolution (arXiv 2608.27439)"
type: source
tags: [source, arxiv, agent-security, offensive, red-team, skill-evolution, lab-only, k313]
keywords: [2608.27439, RedEvoAgent, skill evolution, red-team agent, tool-effectiveness profiling, Deciding-Tool Attribution, validation ratchet, jailbreak skill, black-box]
related:
  - concepts/experience-driven-redteam-skill-evolution.md
maturity: draft
read_status: read
created: 2026-08-28
updated: 2026-08-28
phase_0_verdict: "REFERENCE 2026-08-28 — lab-only eval primitive. No public paper repo at hunt. Do NOT copy evolved skills into `.cursor/skills`; no attack-skill bodies in wiki. Authorized-lab targets only."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K313)"
---

## Relations

- @concepts/experience-driven-redteam-skill-evolution.md — primary steal (evolve skills with a validation ratchet; lab-only)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | RedEvoAgent: Automatic Red-Teaming Agent with Experience-Driven Skill Evolution |
| Authors | Junjie Zhang, Hui Liu, Kecheng Chen (CityU HK); Xianbo Mo, Changsheng Chen (Shenzhen MSU-BIT); Haoliang Li (CityU HK) |
| arXiv | 2608.27439 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.27439-redevoagent-automatic-red-teaming-agent-with-exp.pdf` |
| Retrieved | 2026-08-28 |
| Read status | read (abstract + method) |
| Public code | **none at hunt** — no matching repo; no clone |

## Narrative

**Problem:** LLM agents now run in product-level execution harnesses (Claude Code / Codex class) where a jailbreak can trigger **harmful tool use and persistent state changes** — higher risk than unsafe text alone. Existing automatic red-teaming uses **fixed attacks**, while recent agentic attackers coordinate multiple jailbreak tools with **trajectory-based retrieval**. That retrieval suffers **retrieval bias** and **unclear tool credit**, and full trajectories cost context and interpretability.

**RedEvoAgent (K313)** is a **black-box red-teaming agent** that **distills cross-case attack trajectories into a concise, human-readable attack skill**, which adaptively evolves through:

- **Tool-effectiveness profiling** + **Deciding-Tool Attribution** — attribute success/failure to specific tools for skill updates.
- **Validation ratchet** — retain only updates that **improve validation** performance.

**Result (paper claim):** outperforms fixed and agentic baselines, improves tool efficiency, and **transfers across attacker models and target execution harnesses** (Claude Code / Codex class).

**Why filed (K313):** this is the **offense-side** counterpart to K283 JailbreakSkill (evolving attack-skill libraries) and **skill misevolution** (defense side — practice can make a skill library unsafe). The key steal is the **validation ratchet** — the evaluation update gate that prevents skill drift. **Authorized lab only**: no `.cursor/skills` evolution from attack runs; no attack-skill bodies or PoCs in wiki; no LIVE third-party targets. No public repo at hunt → REFERENCE only.

## Snippets

> RedEvoAgent, a black-box red-teaming agent that distills cross-case attack trajectories into a concise, human-readable attack skill … adaptively evolves through tool-effectiveness profiling and Deciding-Tool Attribution for skill updates, and a validation ratchet that retains only updates improving validation performance. [Source: arXiv 2608.27439 abstract]

> Experiments on multiple benchmarks, target models, and target execution harnesses show that RedEvoAgent outperforms fixed and agentic baselines, improves tool efficiency, and transfers across attacker models and target execution harnesses. [Source: arXiv 2608.27439 abstract]
