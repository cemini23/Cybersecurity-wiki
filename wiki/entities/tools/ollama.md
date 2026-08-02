---
title: "Ollama — local LLM runtime (simple pull/run + API)"
type: entity
tags: [entity, tool, llm, local-llm, ollama, inference, pentest-assist]
keywords: [ollama, local llm, OpenAI-compatible API, GGUF, Apple Silicon, NVIDIA, model server]
related:
  - concepts/local-abliterated-llm-pentest-stack.md
  - entities/tools/vllm.md
  - concepts/llm-pentest-automation.md
  - concepts/ai-for-cybersecurity.md
  - concepts/agent-vm-sandboxing.md
  - concepts/operator-lab-playbook.md
maturity: draft
created: 2026-08-02
updated: 2026-08-02
---

## Relations

- @concepts/operator-lab-playbook.md — start-here operator lab hub (local AI → owned lab → product → bounty)

- @concepts/local-abliterated-llm-pentest-stack.md — primary methodology: when/why to run low-refusal open weights for authorized pentest assist; VRAM tiers; host hardening
- @entities/tools/vllm.md — sibling runtime: prefer vLLM when you need higher concurrent throughput on NVIDIA
- @concepts/llm-pentest-automation.md — Tier-1 first; Tier-2 only with declared scope when agents call tools
- @concepts/ai-for-cybersecurity.md — LLM × security context
- @concepts/agent-vm-sandboxing.md — keep tool-using agents isolated even when inference is local

## Raw Concept

Stub entity created 2026-08-02 alongside @concepts/local-abliterated-llm-pentest-stack.md. Ollama is the **simple** local runtime path in that stack (Linux + NVIDIA primary, Apple Silicon secondary). No Phase-0 clone/install stamp on this page yet — do not invent local paths or star counts here; see the concept for operational doctrine.

## Narrative

**Ollama** is a local large-language-model runtime that makes open-weight models easy to pull, run, and serve via a local HTTP API (including OpenAI-compatible style clients depending on version/config). In this wiki it is documented as the low-friction option for **authorized pentest assist** with abliterated / low-refusal text models — not as a general chat desktop app page.

**Role in the stack**

| Concern | Ollama stance |
|---------|----------------|
| Operator UX | Fastest path: install → pull model → query |
| Hardware | Works on Linux NVIDIA and Apple Silicon; quant selection matters for VRAM/unified memory |
| Throughput | Fine for solo / light concurrent use; prefer @entities/tools/vllm.md for multi-agent load on a GPU box |
| Security | **Bind loopback by default**; never expose a public Ollama endpoint; isolate from bounty egress — full rules on @concepts/local-abliterated-llm-pentest-stack.md |

**Cemini fit**

- **Cybersec (primary)** — local dual-use technical assist when cloud models refuse in-scope content; feed Tier-1 (and carefully scoped Tier-2) agents.
- **Not a substitute for authorization** — low-refusal models still require written scope for anything that touches live systems.

For VRAM → model size class, host hardening, ethics, and Tier-1/Tier-2 wiring, use the concept page — this entity stays thin by design.
