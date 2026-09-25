---
title: "Coding agents for generalized task and motion planning (OOD)"
type: source
tags: [source, ood]
keywords: [2609.30233, ood]
related:
  - "@ccc-wiki/sources/arxiv-2609-30233-coding-agents-tamp-ood-2026-09-25.md"
maturity: draft
read_status: deep-read
created: 2026-09-25
updated: 2026-09-25
phase_0_verdict: "REFERENCE 2026-09-25 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (OOD)"
cross-wiki-source: "@ccc-wiki/sources/arxiv-2609-30233-coding-agents-tamp-ood-2026-09-25.md"
---

## Relations

- @ccc-wiki/sources/arxiv-2609-30233-coding-agents-tamp-ood-2026-09-25.md — CCC wiki **primary steal** (generalized TAMP / coding agents).

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Coding agents for generalized task and motion planning (OOD) |
| arXiv | 2609.30233 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609-30233-coding-agents-for-generalized-task-and-motion-pl.pdf |
| Retrieved | 2026-09-25 |
| Read status | deep-read (2026-09-25) |

## Narrative

**OOD (2609.30233)** — **Generalized TAMP** via **coding agents** (Claude Code **Opus 5**, Codex **GPT-5.6 Sol**, **GPT-6 Astra**) synthesizing programs in a **network-isolated Docker** sandbox (NumPy/SciPy only). **28** KinDER + PDDLStream environments; **980** programs evaluated on **100** held-out instances each (**98k** episodes). Mean success **56–95%** vs **~47%** hand-engineered planners where available; agents used simulator interaction to calibrate physics. Primary home: **@ccc-wiki** robotics/planning steal — cyber wiki keeps cross-link + egress PDF pointer only.
## Snippets

> "980 generated programs on 100 held-out instances each, 98,000 evaluation episodes in total." [Source: arXiv 2609.30233 abstract]

> "Coding agents integrate frontier LLMs with harnesses that enable them to read files, write programs, and execute arbitrary commands … sandboxed Docker container … no network access." [Source: arXiv 2609.30233]