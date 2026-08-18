---
title: "ESTI — state-semantic injection in LLM-driven embodied agents (arXiv 2608.16806)"
type: source
tags: [source, arxiv, agent-security, embodied, planner-integrity, k288]
keywords: [2608.16806, ESTI, ESTI-Bench, state-semantic injection, P-ASR, E-ASR, schema-preserving]
related:
  - "@ccc-wiki/concepts/planner-state-semantic-integrity-attack-surface.md"
  - "@ccc-wiki/sources/arxiv-esti-state-semantic-injection-2608.16806.md"
  - concepts/agent-runtime-guardrails.md
  - concepts/esti-state-semantic-injection-stub.md
  - concepts/mcp-security-posture.md
  - concepts/physical-vs-content-danger-embodied-agents.md
  - concepts/planner-state-integrity-embodied-agents.md
  - concepts/prompt-injection-detector-calibration.md
  - entities/tools/esti-bench.md
maturity: draft
read_status: read
created: 2026-08-18
updated: 2026-08-18
phase_0_verdict: "REFERENCE 2026-08-18 — no public repo at retrieval. Cyber-primary (same paper as CCC K288). Dual-ID: Cybersec K288 = CCC K288 ESTI (same paper); ≠ CCC K282/K283."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc + cemini-cybersec-mcp-tool-control.mdc (K288 ESTI)"
---

**Briefs:** `briefs/2026-08-18_k288-esti-state-injection.md`

## Relations

- @ccc-wiki/concepts/planner-state-semantic-integrity-attack-surface.md
- @ccc-wiki/sources/arxiv-esti-state-semantic-injection-2608.16806.md
- @concepts/agent-runtime-guardrails.md
- @concepts/esti-state-semantic-injection-stub.md
- @concepts/mcp-security-posture.md
- @concepts/physical-vs-content-danger-embodied-agents.md
- @concepts/planner-state-integrity-embodied-agents.md
- @concepts/prompt-injection-detector-calibration.md
- @entities/tools/esti-bench.md


## Raw Concept

| Field | Value |
|-------|-------|
| Title | When State Becomes an Attack Surface: State-Semantic Injection in LLM-Driven Embodied Agents |
| Authors | Jiawei Liu, Jiacheng Guo, Tian Zhang, Yiwei Xu, Juan Wang, Jinlin Fan, Bowen Xiao, Chi Guo (Wuhan Univ.); Hongxin Hu, Keyan Guo (Univ. at Buffalo) |
| arXiv | 2608.16806 (cs.RO, v1 17 Aug 2026) |
| Code | none at retrieval |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.16806-when-state-becomes-an-attack-surface-state-seman.pdf` |
| Retrieved | 2026-08-18 |
| Read status | read (full extract) |

## Narrative

ESTI asks a **conditional** downstream question: if exactly one planner-facing state producer is compromised, can a **schema-preserving false record** be adopted and realized as a targeted final-state consequence? User instruction, planner, and executor stay unchanged. False evidence is written over existing/interactable objects, relations, affordances, task-stage constraints, or execution feedback — not as an explicit competing command.

ESTI-Bench vs Vanilla IPI / EIRAD / BADROBOT in ProgPrompt/VirtualHome, VoxPoser/RLBench, AI2-THOR. Reported lifts vs strongest baseline: planning-level ASR up to **+89.32 pp**, execution-level ASR up to **+43.69 pp**. Ablation: removing runtime re-grounding changes P-ASR/E-ASR only **1.92 / 3.85 pp**; carrier compatibility + representation consistency dominate. **P-ASR ≠ E-ASR**. Results do not estimate the probability of obtaining write access. [TENTATIVE] single source.

**Cybersec K288 = CCC K288** (same paper; cyber-primary). Authorized embodied/sim lab only. No injection payloads in this wiki.

## Snippets

> Thus, our results characterize downstream consequences conditional on successful state delivery; they neither estimate the probability of obtaining write access nor treat planning deviation as equivalent to physical attack success. [Source: arXiv 2608.16806 abstract]
