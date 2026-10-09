---
title: "Adversarial images hijack web agents (K408)"
type: concept
tags: [concept, agent-security, k408]
keywords: [2610.09240, K408]
related:
  - sources/arxiv-2610-09240-adversarial-images-hijack-web-agents.md
  - concepts/model-is-not-a-security-boundary-kubernetes-agents.md
  - concepts/prompt-injection-detector-calibration.md
maturity: draft
created: 2026-10-09
updated: 2026-10-09
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K408)"
---

## Relations

- @sources/arxiv-2610-09240-adversarial-images-hijack-web-agents.md
- @concepts/model-is-not-a-security-boundary-kubernetes-agents.md
- @concepts/prompt-injection-detector-calibration.md

## Raw Concept

Question: **Adversarial images hijack web agents** — operator steal from arXiv 2610.09240?

## Narrative

An agent that **reads pixels and then acts** collapses the boundary between content and command. A page image the agent merely *looks at* can steer its **visual grounding**, and because the same agent holds browser execution, that steer becomes an **action** — the attack crosses from perception into the execution stage rather than stopping at mis-description.

The operator consequence: screencast or OCR filtering is a **perception** control, and the failure here is **downstream of it**. What helps is bounding what the browser context can *do* once grounding is wrong — least-privilege sessions, action confirmation for credentialed steps, and treating any rendered image as untrusted input. Same shape as K421's 'the model is not a security boundary', applied to the browser.

## Snippets

> See arXiv 2610.09240 abstract. [Source: arXiv 2610.09240 (retrieved 2026-10-09)]
