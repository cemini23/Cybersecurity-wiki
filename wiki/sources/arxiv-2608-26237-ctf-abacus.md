---
title: "CTF-ABACUS — trace-level provenance for agentic offensive-security eval (arXiv 2608.26237)"
type: source
tags: [source, arxiv, agent-security, ctf, offensive, evaluation, evidence, k311]
keywords: [2608.26237, CTF-ABACUS, trace-based eval, agent auditing, solve profile, flag recovery, shortcut, evidence-grounded, penetration-testing phases]
related:
  - concepts/trace-verified-ctf-agent-eval.md
maturity: draft
read_status: read
created: 2026-08-28
updated: 2026-08-28
phase_0_verdict: "REFERENCE 2026-08-28 — audit/eval framework; no attack payloads. No matching SPDX repo (AbacusCTF is unrelated). Authorized-lab CTF eval only."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K311)"
---

## Relations

- @concepts/trace-verified-ctf-agent-eval.md — primary steal (flag ≠ demonstrated exploit)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | How Do LLM Agents Actually Get the Flag? Trace-Level Provenance for Agentic Offensive Security Evaluation |
| Authors | Kimberly Milner et al. (NYU Tandon / NYU Abu Dhabi / CISPA / IIIT Hyderabad / IIT Tirupati) |
| arXiv | 2608.26237 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.26237-how-do-llm-agents-actually-get-the-flag-trace-le.pdf` |
| Retrieved | 2026-08-28 |
| Read status | read (abstract + method + results) |
| Public code | **none matching at hunt** — `blessingcharles/AbacusCTF` is unrelated to this paper; no clone |

## Narrative

**Problem:** CTF benchmarks are the standard proxy for "agentic offensive capability." Most evaluations use a **shallow binary judgment** (did it reach the flag) or an aggregate score, and ignore the **trajectory** to the flag. That conflates real exploitation with several unrelated paths — **direct flag exposure, memorized recall, external lookup, guessing, and unsupported claims** — so CTF evals **overstate capability**.

**CTF-ABACUS (K311)** is a **trace-based agent auditing framework** that reconstructs each run as an **evidence-grounded solve profile**:

- Decomposes agent actions into **penetration-testing phases** and **categorical techniques**.
- Pinpoints where exploitation occurs, where the flag **first appears**, and whether the recovered flag is **supported by demonstrated behavior**.
- Aggregating profiles across agents yields **challenge signatures** that separate **intended-exploit success** from **shortcut pathways**.

**Result (paper claim):** across **1,435 CTF attempts**, **240 challenges**, **six models**, and **two judge lenses** — **trace-verified exploits account for only 62–87% of recovered flags**. Shortcut recoveries follow substantially shallower evidence chains.

**Why filed (K311):** this is the offensive-pentest-specific instance of **faithful capability measurement** — pairs K271 (REDAgentBench faithful ASR) and K278 (ATOBench verification-chain deception). **Flag ≠ demonstrated exploit.** Any pentest-agent eval that counts flags as wins without a trace check overstates capability. **No matching repo at hunt** → REFERENCE only; **authorized-lab CTF eval only**; no LIVE third-party targets.

## Snippets

> Evaluations rely on shallow binary judgments or aggregate scores, overlooking the agent's trajectory to the flag. Consequently, actual exploitation is conflated with direct flag exposure, memorized recall, external lookup, guessing, and unsupported claims, potentially overstating the agent's cybersecurity capability. [Source: arXiv 2608.26237 abstract]

> Trace-verified exploits account for only 62-87% of recovered flags across benchmarks, while shortcut recoveries follow substantially shallower evidence chains. [Source: arXiv 2608.26237 abstract]
