---
title: "Confused ChatGPT — cross-app context poisoning via first-party APIs (arXiv:2606.00485)"
type: source
tags: [arxiv, agent-security, prompt-injection, chatgpt-apps, context-poisoning, confused-deputy, research-paper]
keywords: [cross-app context poisoning, ChatGPT Apps, sendFollowUpMessage, systemPrompt, isVisible, confused deputy, OpenAI]
related:
  - concepts/agent-skill-injection.md
  - concepts/agent-runtime-guardrails.md
  - concepts/llm-pentest-automation.md
  - concepts/ai-for-cybersecurity.md
  - sources/arxiv-2605-30454-agent-prompt-injection-surface-evaluation.md
  - sources/arxiv-2606-02240-agentredbench.md
  - sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md
maturity: draft
read_status: read
created: 2026-06-03
updated: 2026-06-03
---

## Relations

- @concepts/agent-skill-injection.md — cross-app context poisoning as platform-level IPI variant
- @concepts/agent-runtime-guardrails.md — architectural isolation gap vs runtime authority guards
- @concepts/llm-pentest-automation.md — multi-app copilot threat model for pentest engagements
- @concepts/ai-for-cybersecurity.md — commercial LLM platform security research
- @sources/arxiv-2605-30454-agent-prompt-injection-surface-evaluation.md — per-surface eval hygiene
- @sources/arxiv-2606-02240-agentredbench.md — integration read→write attacks on enterprise copilots

## Raw Concept

- **Title**: Confused ChatGPT: Cross-App Context Poisoning via First-Party APIs
- **Authors**: Chao Wang, Somesh Jha, Zhiqiang Lin (Ohio State / Wisconsin)
- **Type**: arXiv preprint
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/arxiv-2606.00485-confused-chatgpt-cross-app-context-poisoning-via.pdf`
- **URL**: https://arxiv.org/abs/2606.00485
- **Retrieved**: 2026-06-03
- **Read-status**: read (abstract + threat model + attack sections via arXiv HTML)

## Narrative

Names **cross-app context poisoning** — indirect prompt injection on ChatGPT Apps (888 apps by May 2026) where: (i) poison persists in shared chat context across turns; (ii) harm surfaces through a **different** co-resident app the user later invokes; (iii) delivery uses **first-party APIs** every connected app can call.

**sendFollowUpMessage** is the primary write channel; undocumented params **systemPrompt** (elevates to system priority) and **isVisible:false** (hides injection from UI) enable silent, system-priority poisoning. Demonstrated **confused-deputy** attacks: conditional payloads (redirect benign hotel search) and imperative payloads (force victim-app tool calls). Validated on six ChatGPT models (GPT o3 through GPT 5.5 Thinking).

Root cause is **architectural**: flat, unpartitioned shared context with no provenance — not patchable without context partitioning or capability model. OpenAI disclosure made; undocumented params still accessible at publication `[TENTATIVE]`.

Relevant to cybersec wiki as red-team methodology for multi-app LLM copilots and as contrast to skill-file injection (terminal agents) in the same K95 cluster.

## Snippets

> "The LLM's context is a persistent, flat, untagged data store shared by user and apps, with no isolation."

> "A malicious app poisons the context so that the LLM, consulting that context, enables manipulation against benign co-resident apps."
