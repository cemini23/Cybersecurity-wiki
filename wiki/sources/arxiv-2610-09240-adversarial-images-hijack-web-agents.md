---
title: "Adversarial images hijack web agents from visual grounding to browser execution"
type: source
tags: [source, arxiv, agent-security]
keywords: [2610.09240, k408]
related:
  - concepts/adversarial-images-hijack-web-agents.md
  - concepts/model-is-not-a-security-boundary-kubernetes-agents.md
  - concepts/prompt-injection-detector-calibration.md
maturity: draft
read_status: read
created: 2026-10-09
updated: 2026-10-09
phase_0_verdict: "REFERENCE 2026-10-09 — no attack payloads in wiki."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K408)"
---

## Relations

## Relations

- @concepts/adversarial-images-hijack-web-agents.md
- @concepts/model-is-not-a-security-boundary-kubernetes-agents.md
- @concepts/prompt-injection-detector-calibration.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Adversarial images hijack web agents from visual grounding to browser execution |
| arXiv | 2610.09240 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.09240-adversarial-images-hijack-web-agents-from-visual.pdf |
| Retrieved | 2026-10-09 |
| Read status | read (deep-read) |

## Narrative

**K408** — a modern **web agent is a vision-language model that both perceives and acts**, so a perturbed *image* on a page is not just visual noise: the agent reads it as grounding evidence and then **executes** on it in the browser. The attack therefore crosses two stages — it hijacks **visual grounding** and carries through to **browser execution** — which is why a screenshot-level guard is not enough. Repo `github.com/MoonTea0416/WebMirage`; licence not stated. Operator steal: **an image on a page an agent browses is untrusted input on the same footing as a tool description** — the K421 data/control collapse, in the browser rather than the cluster. Treat any agent that reads pixels and holds browser credentials as needing a **least-privilege browser context**, not a better prompt. Authorized lab only. **No perturbation recipes or attack code in wiki.**

## Snippets

> See arXiv 2610.09240 abstract. [Source: arXiv 2610.09240 (retrieved 2026-10-09)]
