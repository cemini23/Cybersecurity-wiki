---
title: "Experience-driven red-team skill evolution — validation ratchet (K313)"
type: concept
tags: [concept, agent-security, offensive, red-team, skill-evolution, lab-only, k313]
keywords: [RedEvoAgent, skill evolution, validation ratchet, tool-effectiveness, Deciding-Tool Attribution, attack skill, black-box red team, lab eval]
related:
  - sources/arxiv-2608-27439-redevoagent.md
  - concepts/evolving-attack-skill-libraries.md
  - concepts/skill-misevolution.md
  - concepts/evoskill-injection-self-evolving-agents.md
  - sources/arxiv-2608-30429-evoskill-injection.md
maturity: draft
created: 2026-08-28
updated: 2026-09-01
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K313)"
---

## Relations

- @sources/arxiv-2608-27439-redevoagent.md — source paper (black-box skill-evolution red team)
- @concepts/evolving-attack-skill-libraries.md — offense-side evolving skill library (K283 JailbreakSkill)
- @concepts/skill-misevolution.md — defense side: practice can make a skill library unsafe

## Raw Concept

Question: **can a red-team agent learn from prior runs, and how do you evolve its "attack skill" without it drifting into junk that merely looks effective?**

## Narrative

Agentic attackers that retrieve full trajectories reuse **misleading experiences** (retrieval bias) and cannot attribute credit to a specific tool — while also paying full-trajectory context cost. **RedEvoAgent (K313)** compresses cross-case trajectories into a concise, **human-readable attack skill** and evolves it with two mechanisms:

- **Tool-effectiveness profiling + Deciding-Tool Attribution** — decides which tool actually produced the success/failure, so the skill update targets the right capability.
- **Validation ratchet** — keep an update **only if it improves validation**. This is the essential gate: it stops the skill from drifting toward superficially-plausible-but-worse behavior.

It **transfers across attacker models and target harnesses** (Claude Code / Codex class), outperforming fixed and agentic baselines.

**Operator steal (authorized lab / product pentest harness):**
1. **Evolving attack skills are a lab eval primitive, not a prod capability.** Never auto-evolve `.cursor/skills` from an attack-run (pairs K283 / misevolution — retrieval-time harm is not covered by a HITL write).
2. **Always gate a skill update on validation** — the ratchet. An update that does not strictly improve held-out validation is rejected. Never let "it worked on the last run" push a change.
3. **Attribute credit to the tool, not the trajectory** — per-tool effectiveness lets the skill stay concise and interpretable; full-trajectory retrieval waters down credit and costs context.
4. **No attack-skill bodies, prompts, or PoCs in the wiki** — document the *mechanism* (distill + attribute + ratchet), not the payloads. Authorized-lab targets only; no LIVE third-party.
5. **Report double-sided** — dual ASR, tool efficiency, and generalization/transfer, not just a headline ASR.

## Snippets

> The attack skill adaptively evolves through tool-effectiveness profiling and Deciding-Tool Attribution for skill updates, and a validation ratchet that retains only updates improving validation performance. [Source: arXiv 2608.27439 abstract]
