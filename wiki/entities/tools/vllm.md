---
title: "vLLM — high-throughput OpenAI-compatible LLM serving"
type: entity
tags: [entity, tool, llm, local-llm, vllm, inference, nvidia, pentest-assist]
keywords: [vllm, continuous batching, OpenAI-compatible API, PagedAttention, NVIDIA, model server, throughput]
related:
  - concepts/local-abliterated-llm-pentest-stack.md
  - entities/tools/ollama.md
  - concepts/llm-pentest-automation.md
  - concepts/ai-for-cybersecurity.md
  - concepts/agent-vm-sandboxing.md
  - entities/tools/iron-proxy.md
  - concepts/operator-lab-playbook.md
  - concepts/toktier-exact-stateful-tokenization.md
  - sources/arxiv-2607-29678-toktier-stateful-tokenization.md
maturity: draft
created: 2026-08-02
updated: 2026-08-03
---

## Relations

- @concepts/operator-lab-playbook.md — start-here operator lab hub (local AI → owned lab → product → bounty)

- @concepts/local-abliterated-llm-pentest-stack.md — primary methodology: local low-refusal stack, VRAM tiers, host hardening, ethics
- @entities/tools/ollama.md — sibling runtime: prefer Ollama for simple solo pull/run; vLLM for throughput
- @concepts/llm-pentest-automation.md — multi-agent concurrency still obeys Tier-1 / Tier-2 scope gates
- @concepts/ai-for-cybersecurity.md — LLM × security context
- @concepts/agent-vm-sandboxing.md — isolate tool-using agents from the inference host when possible
- @entities/tools/iron-proxy.md — egress control if the serving host is shared with untrusted agent workloads
- @concepts/toktier-exact-stateful-tokenization.md
- @sources/arxiv-2607-29678-toktier-stateful-tokenization.md

## Raw Concept

Stub entity created 2026-08-02 alongside @concepts/local-abliterated-llm-pentest-stack.md. vLLM is the **throughput-oriented** OpenAI-compatible serving path (Linux + NVIDIA primary) in that stack. No Phase-0 clone/install stamp or invented metrics on this page — operational doctrine lives on the concept.

## Narrative

**vLLM** is a high-performance inference engine for large language models, known for efficient GPU memory use (e.g. PagedAttention-class techniques) and **continuous batching** so multiple concurrent clients share a single GPU more effectively than naive one-request-per-process serving. Clients typically talk to an **OpenAI-compatible HTTP API**, which makes it a drop-in `base_url` target for agent frameworks already written against cloud APIs.

**Role in the stack**

| Concern | vLLM stance |
|---------|-------------|
| Operator UX | More setup than Ollama; better when the host is a dedicated GPU lab box |
| Hardware | NVIDIA-first; match model class to VRAM per @concepts/local-abliterated-llm-pentest-stack.md |
| Throughput | Prefer when several Tier-1 agents or parallel lab jobs hit the same model |
| Security | Loopback or isolated lab VLAN only; auth if any non-localhost client; never public internet; pair with egress policy (@entities/tools/iron-proxy.md) if agents co-reside |

**Cemini fit**

- **Cybersec (primary)** — serving abliterated / low-refusal open weights for authorized multi-agent or multi-session pentest assist.
- **vs Ollama** — Ollama for simplicity; vLLM when concurrency and stable OpenAI-compat serving matter more than one-command pull.

For ethics, Tier-1-first wiring, and AI-host hardening, defer entirely to @concepts/local-abliterated-llm-pentest-stack.md.
