---
title: Safety in self-evolving LLM agent systems — MLAS (arXiv 2606.23075)
type: source
tags: [source, arxiv, agent-security, self-evolution, openclaw, mlas, k114]
keywords: [2606.23075, mlas, self-evolving agents, openclaw, hermes-agent, attack persistence, optimizer optimizee collapse]
related:
  - concepts/ai-for-cybersecurity.md
  - concepts/self-evolving-agent-security.md
  - concepts/agentic-containment-principles.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-security-posture.md
  - concepts/agent-skill-injection.md
  - sources/arxiv-2606-01494-clawhub-security-signals.md
  - sources/openreview-openclaw-real-world-safety-analysis.md
  - entities/tools/defenseclaw.md
  - entities/tools/nvidia-skillspector.md
  - concepts/safeclawbench-staged-agent-security.md
maturity: draft
read_status: read
created: 2026-06-23
updated: 2026-06-23
phase_0_verdict: "Reference 2026-06-23 — framework analysis paper; case studies cite github.com/openclaw/openclaw + github.com/NousResearch/hermes-agent (separate Phase-0 on those repos)"
---

## Relations

- @concepts/self-evolving-agent-security.md — MLAS matrix + amplification effects synthesis
- @sources/arxiv-2606-01494-clawhub-security-signals.md — OpenClaw skill scanner disagreement context

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Safety in Self-Evolving LLM Agent Systems: Threats, Amplification, and Case Studies |
| Authors | Ruixiao Lin et al. (ZJU, Ant Group, Tsinghua, NTU, Fudan) |
| arXiv | 2606.23075 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2606.23075-pdf-safety-in-self-evolving-llm-agent-systems-ar.pdf` |
| Retrieved | 2026-06-23 |
| Read status | **read** (abstract, MLAS overview, Table 1, OpenClaw/Hermes case studies) |

## Narrative

Self-evolving agents that update **weights, memory, tools, and architecture** convert session-scoped attacks into **heritable, compounding threats**.

### MLAS matrix (5 modules × 5 lifecycle stages)

| Module | Scope |
|--------|--------|
| Brain | Core reasoning / policy |
| Cognitive Resource | Memory, RAG, knowledge bases |
| Execution | Tools, APIs, actuators |
| Self-Design | Optimizer modifying own architecture |
| Collective | Multi-agent propagation |

| Stage | Scope |
|-------|--------|
| Bootstrap → Propose → Evaluate → Commit → Serve |

**25 cells:** 17 **critical** (no effective defense), 7 **high** (insufficient defenses), 1 partial mitigation. **Self-Design uniformly critical** (optimizer–optimizee collapse).

### Seven amplification effects

Generational accumulation, selective amplification, deceptive evolution, Lamarckian propagation, capability ratchet, emergent unpredictability, **optimizer–optimizee collapse** (meta-effect disabling other defenses).

### OpenClaw vs Hermes case studies

| Framework | Design | Attack surface | Persistence |
|-----------|--------|----------------|-------------|
| OpenClaw | Evolution-augmented | Lower MLAS activation | — |
| Hermes | Evolution-native | **3.5×** more MLAS cells | **100%** (40/40 payloads, all CIA+Privacy) |

Co-located security scanner blocked **2.5%** of attacks on evolution pathway — install-time scan ≠ runtime evolution risk.

### Cybersecurity relevance

- **Do not deploy self-evolving agents** on prod-mcp / lazy-tool without treating every commit stage as untrusted
- Skill scanners (SkillSpector, DefenseClaw) address **static** install surface only
- Extends K114 containment gap (@concepts/agentic-containment-principles.md) — P3 memory integrity + new **immutable-anchor loss**

## Snippets

> "Self-evolution converts every known attack category from session-bounded incidents into persistent, heritable threat vectors."

> "Evolution-native design activates 3.5× more attack surface cells and achieves a 100% attack persistence rate (40/40 payloads)."

[Source: arxiv-2606.23075-self-evolving-llm-agent-safety-mlas.pdf]
