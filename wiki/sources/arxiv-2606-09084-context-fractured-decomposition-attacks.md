---
title: Context-Fractured Decomposition — artifact provenance gap attacks (arXiv 2606.09084)
type: source
tags: [source, arxiv, agent-security, jailbreak, provenance, multi-step, icml-workshop]
keywords: [2606.09084, cfd, context-fractured decomposition, provenance gap, artifact-mediated, cross-session]
related:
  - concepts/context-fractured-decomposition-attacks.md
  - concepts/agent-execution-provenance.md
  - concepts/agent-runtime-guardrails.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/mcp-security-posture.md
  - concepts/agent-skill-injection.md
  - sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md
  - sources/arxiv-2606-04990-agent-traces-evidence-provenance.md
  - sources/arxiv-2606-07943-poise-position-aware-skill-injection.md
  - sources/arxiv-2606-10749-toward-secure-llm-agents-survey.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-06-11
updated: 2026-06-11
---

## Relations

- @concepts/context-fractured-decomposition-attacks.md — attack class synthesis
- @concepts/agent-execution-provenance.md — artifact lineage as missing trust function
- @concepts/crescendo-multi-turn-jailbreak.md — contiguous-trace assumption contrast
- @sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md — cross-session state without provenance record

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Context-Fractured Decomposition Attacks on Tool-Using LLM Agents: Exploiting Artifact Provenance Gaps |
| Authors | Xiaofeng Lin, Yukai Yang, Daniel Guo, et al. (UCLA, Texas A&M, Cisco) |
| arXiv | 2606.09084 |
| Venue | ICML 2026 Workshop on Failure Modes in Agentic AI (FAGEN) |
| Location | `raw-sources/arxiv-2606.09084-context-fractured-decomposition-attacks-on-tool.pdf` |
| Retrieved | 2026-06-11 |
| Read status | **read** |

## Narrative

Operationalizes the **provenance gap**: defenders assume contiguous interaction traces, but real agent pipelines fracture context across tools, sessions, and instances while **persistent artifacts** (files, logs, tickets) carry state. **Context-Fractured Decomposition (CFD)** decomposes disallowed objectives into individually plausible tool steps whose harm emerges only under delayed artifact-mediated composition [CONFIRMED].

### Attack model

1. Early step writes benign-looking artifact (intent-bearing, locally acceptable)
2. Later step — possibly different agent instance — reads artifact and executes harmful action
3. Final executor is an **innocent executor**: no semantic access to earlier intent

Contrasts with Crescendo/Tree-of-Attacks: those assume escalating intent visible in one conversational window.

### Results [CONFIRMED]

- Up to **+28.14 percentage points ASR** vs SOTA baselines (Crescendo, Tree-of-Attacks, role-play) on agent-system jailbreak benchmarks
- Strong single-turn judges fail — cannot observe across provenance gap
- Context removal ablation: dropping early turns cuts ASR **58% → 44%** (−14 pp); confirms delayed composition dependency
- Proposed mitigation direction: **provenance lineage tagging** at policy layer

### Cemini relevance

Extends K100 SPI + skill-poisoning story: audit **who wrote what artifact, under what policy, readable by which downstream tool** — not only install-time skill scan.

## Snippets

> "Each step can appear benign in isolation, yet the risk arises from cross-step composition through artifacts."
> — [Source: arxiv-2606.09084 §1, retrieved 2026-06-11]

> "CFD achieves up to 28.14 percentage points higher ASR than advanced jailbreaking baselines."
> — [Source: arxiv-2606.09084 abstract/results, retrieved 2026-06-11]

## Dead Ends

- **Crescendo-only red-team eval** on multi-agent prod pipelines — overstates defense when artifacts bridge sessions.
- **Final-turn LLM judge as sole guard** — observability gap is structural, not model weakness alone.
