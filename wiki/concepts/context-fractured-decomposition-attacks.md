---
title: Context-Fractured Decomposition (CFD) — cross-session artifact jailbreaks
type: concept
tags: [concept, agent-security, jailbreak, provenance, multi-step, artifact-mediated]
keywords: [cfd, context fracture, provenance gap, innocent executor, cross-context jailbreak, lineage tagging]
related:
  - sources/arxiv-2606-09084-context-fractured-decomposition-attacks.md
  - concepts/agent-execution-provenance.md
  - concepts/agent-runtime-guardrails.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/mcp-security-posture.md
  - concepts/agent-skill-injection.md
  - sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md
  - sources/arxiv-2606-04990-agent-traces-evidence-provenance.md
  - sources/arxiv-2606-10749-toward-secure-llm-agents-survey.md
  - sources/arxiv-2606-07943-poise-position-aware-skill-injection.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-06-11
updated: 2026-06-11
---

## Relations

- @sources/arxiv-2606-09084-context-fractured-decomposition-attacks.md — primary source (ICML 2026 FAGEN)
- @concepts/crescendo-multi-turn-jailbreak.md — contiguous-trace multi-turn class (CFD breaks its defender assumptions)
- @concepts/agent-execution-provenance.md — artifact lineage as accountability layer
- @sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md — cross-session poison without trace linkage

## Raw Concept

Daily digest ingest (2026-06-11): arXiv:2606.09084 — **Context-Fractured Decomposition** exploits the **provenance gap** when agent pipelines split enforcement across tools, time, and instances while artifacts persist state.

## Narrative

**Context fracture** = relevant history split across planner/executor, sessions (hours/days apart), and fresh agent instances, with filesystem/logs/tickets carrying state **without provenance surfaced to policy**.

### CFD attack pattern [CONFIRMED]

| Phase | Behavior |
|-------|----------|
| Write | Early step stores benign-looking artifact (snippet, config, attachment) |
| Persist | Artifact survives across session/instance boundary |
| Compose | Later step reads artifact; individually innocuous tool call completes harmful objective |
| Executor | Final agent is **innocent executor** — no access to intent-bearing earlier context |

Harm is **artifact-mediated composition**, not linguistic escalation in one chat.

### vs adjacent classes

| Class | Assumption CFD breaks |
|-------|----------------------|
| Crescendo / ToA | Contiguous conversation; intent increasingly visible |
| POISE skill injection | SKILL.md body poison at install; CFD uses runtime artifacts |
| SPI (2606.04425) | Persistent prompt state; CFD generalizes to any artifact store |

### Empirical note [CONFIRMED]

Up to **+28.14 pp ASR** vs Crescendo/ToA baselines on agent jailbreak benchmarks; strong single-turn judges fail structurally.

### Defensive direction [TENTATIVE]

**Provenance lineage tagging**: policy layer sees who wrote artifact, under what constraints, which downstream tools may consume it. Aligns with @concepts/agent-execution-provenance.md and 2606.10749 survey prescription.

### Authorized lab eval

Test multi-stage pipelines (writer agent → scheduled job → mail/file tool) with artifact inspection at run completion, not final-turn chat politeness alone.

## Snippets

Example chain: draft snippet → save shared file → later agent emails file to contact list — each step locally reasonable.

## Dead Ends

- **Per-turn refusal filters only** — miss delayed composition through artifacts.
- **Treating multi-turn jailbreak eval as sufficient** for production agent orchestration without artifact provenance controls.
