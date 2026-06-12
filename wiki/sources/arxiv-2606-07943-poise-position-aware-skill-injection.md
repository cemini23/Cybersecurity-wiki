---
title: POISE — position-aware undetectable skill injection (arXiv 2606.07943)
type: source
tags: [source, arxiv, skill-injection, agent-skills, stealth, prompt-injection]
keywords: [2606.07943, poise, skill poisoning, attack success rate, skill-inject, skillsbench]
related:
  - concepts/agent-skill-injection.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-security-posture.md
  - concepts/agent-execution-provenance.md
  - entities/tools/nvidia-skillspector.md
  - entities/tools/malskillbench.md
  - sources/arxiv-2606-07131-malskillbench-runtime-verified-malicious-skills.md
  - sources/arxiv-2606-01567-skill-injection-defenses-enablers.md
  - sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md
  - sources/arxiv-2606-09084-context-fractured-decomposition-attacks.md
  - concepts/context-fractured-decomposition-attacks.md
  - "@ccc-wiki/concepts/skill-vetting.md"
maturity: draft
read_status: read
created: 2026-06-09
updated: 2026-06-11
---

## Relations

- @concepts/agent-skill-injection.md — stealth body injection vs YAML-header poisoning
- @concepts/agent-runtime-guardrails.md — static LLM scanners fail on blended body lines
- @sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md — persistent skill state vs single-session POISE
- @entities/tools/malskillbench.md — runtime-verified PI benchmark complement
- @entities/tools/nvidia-skillspector.md — 74.6% false-positive rate on clean skills cited in paper context

## Raw Concept

| Field | Value |
|-------|-------|
| Title | POISE: Position-Aware Undetectable Skill Injection on LLM Agents |
| arXiv | 2606.07943 |
| Location | `raw-sources/arxiv-2606.07943-poise-position-aware-undetectable-skill-injectio.pdf` |
| Retrieved | 2026-06-09 |
| Read status | **read** |

## Narrative

Skill-poisoning attack optimizing **reliability × stealth** under a stricter success metric than raw payload execution.

### Attack Success Rate (ASR)

ASR counts success only when:
1. Injected payload (canary) **executes**, and
2. User's legitimate task **passes verifier** in the same trial

This models the dangerous regime: compromise hidden behind successful task completion.

### POISE mechanism

- Catalogues three SKILL.md injection positions: YAML `description` append, numbered-step insert, install-section append
- Places **one benign-looking body line** at a **feasible position** via context-aware generator (blends with setup/prerequisite steps)
- Avoids YAML-header exposure (easy to inspect) and scattered explicit malicious prose (agent suspicion)

### Results [CONFIRMED]

| Benchmark | Agent | POISE ASR | Notes |
|-----------|-------|-----------|-------|
| Skill-Inject | codex+gpt-5.2 | **89.3%** | +28.0 pts vs random body B@k=2 (61.3%); verifier 97.3% vs clean 96.0% |
| Skill-Inject | multi (4 configs) | **86.7–90.7%** | YAML-only 86.7% |
| SkillsBench | — | **16.0% ASR** | Clean verifier ceiling 25.9%; beats YAML-only (11.1%) |

**Stealth:** four-judge LLM scanner panel — only **5.6%** of poisoned variants gain new high-risk alert over clean baseline (blends into 74.6% FP on benign skills).

### Defensive implication

Static skill scanners and human YAML review miss single-line body injections that preserve task success. Pair install-time review with **runtime canary + task verifier** tests (authorized lab).

## Snippets

> "Attack Success Rate … requires the injected payload to execute and the user's task to still pass its verifier in the same trial."
> — [Source: arxiv-2606.07943 abstract, retrieved 2026-06-09]

> "POISE achieves an 89.3% ASR … while retaining the stealth advantage of body placement."
> — [Source: arxiv-2606.07943 abstract, retrieved 2026-06-09]

## Dead Ends

- **YAML-only vetting** — 86.7% ASR still high; header inspection insufficient alone.
- **LLM scanner as block gate** — saturated false positives on legitimate privileged skill prose; POISE hides in noise.
