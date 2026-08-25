---
title: "PsychJail — Psychological Jailbreaks via Multi-Turn Persuasion of LLM Policies (arXiv 2608.23028)"
type: source
tags: [source, arxiv, llm-safety, jailbreak, persuasion, multi-turn, k302, lab-only]
keywords: [2608.23028, PsychJail, psychological jailbreak, multi-turn persuasion, PKM, change-of-meaning, susceptibility fingerprint, GRPO]
related:
  - concepts/psychological-multiturn-jailbreaks.md
maturity: draft
read_status: read
created: 2026-08-25
updated: 2026-08-25
phase_0_verdict: "LAB-ONLY 2026-08-25 — FengZeyugit/PsychJail GitHub repo null SPDX + ~2GB → NO-GO clone. No persuasion recipes / attack prompts / PoCs in wiki. Authorized-lab red-team framing only."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K302)"
---

## Relations

- @concepts/psychological-multiturn-jailbreaks.md — primary steal (multi-turn persuasion threat model; lab-only framing)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | PsychJail: Exploring Psychological Jailbreaks via Multi-Turn Persuasion of LLM Policies |
| Authors | Zeyu Feng, Qingyu Wu, Yuzhe Luo, Hua Cheng (Defense Innovation Institute, Academy of Military Sciences, Beijing) |
| arXiv | 2608.23028 (21 pp) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.23028-psychjail-exploring-psychological-jailbreaks-via.pdf` |
| Retrieved | 2026-08-25 |
| Read status | read (abstract + method + results sections) |
| Public code | `github.com/FengZeyugit/PsychJail` — **null SPDX license, ~2GB → NO-GO clone** (hunt 2026-08-25) |

## Narrative

**PsychJail** red-teams aligned LLMs through **theory-grounded, multi-turn persuasion** rather than single-turn prompt optimization. It maps established social-psychology persuasion techniques (a 40-tactic taxonomy, PAP-derived) into a **tactic-conditioned attack policy**, factorizing each attacker action into (1) a **Change-of-Meaning** analysis, (2) a **tactic selection**, and (3) a victim-visible message — operationalizing the **Persuasion Knowledge Model (PKM)**. The policy is refined with trajectory-level RL under a **PKM-gated reward**: early jailbreak success is credited only when *every* turn carries a well-formed change-of-meaning analysis (STRIT-PARSE gate; GRPO update).

**Setup:** attacker initialized from Qwen2.5-3B-Instruct (SFT 3 epochs, 8×H100); victims = Qwen2.5-7B-Instruct, Gemma-2-9B-IT, Llama-3.1-8B-Instruct, Mistral-7B-Instruct-v0.3; train on 520 AdvBench prompts; eval on HarmBench standard subset (200) + StrongREJECT; judge = HarmBench classifier.

**Key results (paper-reported, [TENTATIVE]):**
- Highest average attack success rate across the four victims: **87.3%**, beating strong single-turn and multi-turn baselines (incl. TROJail) on all four models.
- Breaking-action analysis recovers **four empirically distinct per-model susceptibility fingerprints** — which persuasion levers open which model, and how broadly — explaining cross-model transfer asymmetry. The authors label the interpretive profiles (rationalist / credibility-driven / narrative-monoculture / broadly persuadable) as **conjecture** for future validation.

**Why filed (K302):** multi-turn social-engineering-style interaction is the attack surface for increasingly interactive LLM deployments (education, healthcare, policy advising). **Lab only; no persuasion scripts, attack prompts, or PoCs in the wiki**; NO-GO clone (null SPDX + 2GB). [Source: arXiv 2608.23028 PDF]

## Snippets

> PsychJail maps established persuasion techniques from social psychology into a tactic-conditioned attack policy … operationalizing the Persuasion Knowledge Model (PKM) — and refines this policy with trajectory-level reinforcement learning under a PKM-gated reward. [Source: arxiv-2608.23028-psychjail PDF, abstract]

> Across four aligned victim models, PsychJail attains the highest average attack success rate (87.3%), surpassing strong single-turn and multi-turn baselines across all four models. [Source: arxiv-2608.23028-psychjail PDF, abstract]

> We interpret them as four candidate psychological profiles (rationalist, credibility-driven, narrative-monoculture, and broadly persuadable), while treating that interpretation as a conjecture for future validation. [Source: arxiv-2608.23028-psychjail PDF, abstract]
