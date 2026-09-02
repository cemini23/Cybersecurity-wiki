---
title: "Psychological multi-turn jailbreaks — persuasion as an attack surface (K302)"
type: concept
tags: [concept, llm-safety, jailbreak, persuasion, multi-turn, k302, red-team, lab-only]
keywords: [PsychJail, psychological jailbreak, multi-turn persuasion, PAP, PKM, change-of-meaning, crescendo, susceptibility fingerprint, social engineering]
related:
  - sources/arxiv-2608-23028-psychjail.md
  - concepts/crescendo-multi-turn-jailbreak.md
  - concepts/system-prompt-leakage.md
  - concepts/agent-runtime-guardrails.md
  - concepts/logit-tilting-rare-behaviour-audit.md
  - concepts/evoflint-multi-turn-redteam-atlas.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/decoy-hardening-open-weight-abliteration.md
  - concepts/local-abliterated-llm-pentest-stack.md
maturity: draft
created: 2026-08-25
updated: 2026-09-02
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K302)"
---

## Relations

- @sources/arxiv-2608-23028-psychjail.md
- @concepts/crescendo-multi-turn-jailbreak.md — adjacent multi-turn tactic (escalation/reframing) — psychological persuasion is a distinct, theory-grounded layer on top
- @concepts/system-prompt-leakage.md — interactive deployments leak policy surface; persuasion works on that surface
- @concepts/agent-runtime-guardrails.md — enforcement-layer context: refusal is not stable across turns
- @concepts/ai-redteam-evidential-ceiling.md — fingerprint claims are empirical, labeled conjecture — keep evidence standards
- @concepts/decoy-hardening-open-weight-abliteration.md — defense contrast: decoys vs persuasion resilience
- @concepts/local-abliterated-llm-pentest-stack.md — lab context for authorized adversarial testing (authorization floor)

## Raw Concept

Question this page answers: **how do multi-turn, psychology-grounded interactions erode LLM policy adherence, and how should authorized red teams scope that surface without producing weaponized persuasion material?**

## Narrative

Single-turn jailbreak research frames the problem as prompt optimization against an adversarially exploitable system. **Multi-turn persuasion** is a different threat model: the attacker is a *sustained social interlocutor* who negotiates harmful intent across turns, exploiting how aligned policies respond to framing, credibility, narrative, and belief updates — the same levers as human social engineering. PsychJail (K302, 2608.23028) operationalizes this with a PKM-based factorization of each turn (change-of-meaning analysis → tactic → victim-visible message) trained with a PKM-gated trajectory reward; it reports the highest average ASR (87.3%) across four aligned victim models and four per-model **susceptibility fingerprints** (rationalist / credibility-driven / narrative-monoculture / broadly persuadable — explicitly labeled conjecture).

**Why it matters for this wiki:**
- **Interactive LLM deployments are social-engineering surfaces.** If a system is deployed as a sustained interlocutor (support, health, policy advising, agent front-ends), multi-turn persuasion is in scope for authorized red-team evals — not just single-shot injection tests.
- **Refusal is not turn-stable.** A policy that refuses directly can be persuaded over multiple turns; guardrail/refusal testing should include multi-turn scripts, not one-shot.
- **Fingerprints ≠ stable identity.** The four profiles are empirical patterns + interpretation conjecture; do not harden against "profiles" as if they were confirmed victim-model categories ([TENTATIVE], [NEEDS VERIFICATION] until replication).

**Scope rules (hard):** this page documents the *threat model and evaluation framing only*. **No persuasion recipes, attack prompts, jailbreak scripts, or PoCs are filed in this wiki** (NEVER list). PsychJail's repo is NO-GO (null SPDX, ~2GB). Authorized-lab / owned-deployment eval only — same authorization floor as every technique page here.

**Defender reading:** treat sustained high-stakes interactions as needing HITL or escalation paths; monitor for persuasion-tactic markers (authority framing, incremental normalization, false-consensus appeals) the way you would monitor phishing lures; and validate that guardrail verdicts hold across turns, not just per-message.

## Snippets

> PsychJail maps established persuasion techniques from social psychology into a tactic-conditioned attack policy … operationalizing the Persuasion Knowledge Model (PKM). [Source: arXiv 2608.23028 abstract]

> The analysis recovers four empirically distinct per-model susceptibility fingerprints … We interpret them as four candidate psychological profiles … while treating that interpretation as a conjecture. [Source: arXiv 2608.23028 abstract]
