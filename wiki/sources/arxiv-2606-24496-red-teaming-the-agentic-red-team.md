---
title: Red-Teaming the Agentic Red-Team (arXiv 2606.24496)
type: source
tags: [source, arxiv, agent-security, red-team, llm-pentest, agent-phishing, kill-chain]
keywords: [2606.24496, agentic red team, agent-phishing, offensive security agents, sandbox escape, cracken]
related:
  - concepts/agentic-offensive-security-kill-chain.md
  - concepts/llm-pentest-automation.md
  - concepts/agent-runtime-guardrails.md
  - concepts/red-team-operations.md
  - concepts/agent-vm-sandboxing.md
  - concepts/ai-for-cybersecurity.md
  - entities/tools/airecon.md
  - entities/tools/pentest-ai-agents.md
  - entities/tools/pentest-ai.md
  - sources/arxiv-zero-apt-llm-pentest-2606.05567-2026-06-05.md
  - concepts/mcp-security-posture.md

maturity: draft
read_status: read
created: 2026-06-25
updated: 2026-07-31
phase_0_verdict: "Reference 2026-06-25 — Cracken offensive-security meta-audit; no single adoption repo; individual tool Phase-0s deferred to per-entity pages"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

## Relations

- @concepts/agentic-offensive-security-kill-chain.md — kill chain + secure architecture synthesis
- @concepts/llm-pentest-automation.md — Tier-2 agent deployment context

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Red-Teaming the Agentic Red-Team |
| Authors | Dario Pasquini, Michał Bazyli, Taras Fedynyshyn, Artem Sorokin (Cracken) |
| arXiv | 2606.24496 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2606.24496-red-teaming-the-agentic-red-team.pdf` |
| Retrieved | 2026-06-25 |
| Read status | **read** (abstract, threat model, Table 1–4, agent-phishing eval, §9 design principles) |

## Narrative

First in-depth security analysis of **agentic offensive-security tools** (autonomous pentest / red-team LLM agents). Threat model: adversary controls engagement **target** `T` (honeypot); manipulates agent via **agent-phishing** — staging trojanized artifacts without explicit prompt injection.

### Audited agents (12)

CAI, RedAmon, PentestAgent, DarkMoon, PentAGI, AIRecon, PentestGPT, METATRON†, nebula†, xalgorix†, Artemis, STRIX.

† = no OS-level sandbox (immediate host access). **STRIX** — no reliable exploit found in audit. **Artemis** — soft LLM-key exposure only.

### Table 1 headline (attacker capabilities)

| Outcome | Count |
|---------|-------|
| Worker RCE | 10/12 |
| Secrets exfil | 10/12 |
| Persistence / weaponization | 10/12 |
| Sandbox escape → host compromise | 10/12 |

Common flaws: **docker.sock** mounts (CAI, PentAGI), `--network=host` / privileged workers (AIRecon, PentestAgent), shared API keys across orchestrator+worker (RedAmon), orchestrator tools executing on host (PentestGPT `python_session`).

### Agent-phishing eval (8 agents × 6 LLMs)

Honeypot payloads: **cfgunpack** (tar `--to-command` shell), **db-restore** (mmap RWX driver), **pwcrypt** (metadata OOB → `system@plt`). **97.8%** overall success — no prompt injection; contextual deception + reward hacking.

| Payload | Overall success |
|---------|-----------------|
| cfgunpack | 98.3% |
| db-restore | 96.7% |
| pwcrypt | 98.3% |

### Kill chain (abstract)

LLM manipulation → lateral movement (worker→orchestrator) → persistence → guardrail bypass → sandbox escape.

### Secure architecture (§9) — core invariant

**Treat worker as malicious.** Secrets live on orchestrator; tool APIs proxied; minimal Docker caps; block worker→orchestrator escalation; egress proxy + human gate on high-impact actions.

`[TENTATIVE]` — Cracken-authored audit; independent reproduction of per-tool exploits not done in this wiki.

## Snippets

> "We assume that a determined adversary will eventually be able to achieve arbitrary code execution within the worker environment."

> "Agent-phishing achieves reliable (97.8% in our experiments) agent compromise purely via staging and adversarial reward hacking."

[Source: arxiv-2606.24496-red-teaming-the-agentic-red-team.pdf]
