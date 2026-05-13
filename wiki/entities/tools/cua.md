---
title: cua — Computer Use Agent (agent-VM sandbox)
type: entity
tags: [agent-vm, sandbox, tracing, lume, apple-virtualization, red-team, mcp, foss]
keywords: [cua, computer use agent, lume, apple virtualization, agent sandbox, tracing, m-series mac, mcp server]
related:
  - concepts/agent-vm-sandboxing.md
  - concepts/red-team-operations.md
  - concepts/exploit-development.md
  - concepts/incident-response.md
  - concepts/malware-analysis.md
  - concepts/av-edr-bypass.md
  - entities/tools/fuzzyai.md
  - entities/tools/pentest-ai-agents.md
  - "@osint-wiki/entities/tools/cua.md"
maturity: validated
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- @concepts/agent-vm-sandboxing.md — the methodology pattern this tool implements
- @concepts/red-team-operations.md — primary use case (LLM-driven exploit testing in isolated VMs)
- @concepts/exploit-development.md — sandboxed PoC detonation
- @concepts/incident-response.md — tracing-replay for post-incident analysis
- @concepts/malware-analysis.md — detonation chamber for unknown samples
- @concepts/av-edr-bypass.md — testing payload behavior in clean-image VMs without contaminating host telemetry
- @entities/tools/fuzzyai.md — sibling tool; pair LLM-adversarial fuzzing with cua-tracing for replayable jailbreak campaigns
- @entities/tools/pentest-ai-agents.md — sibling tool; pentest-ai-agents orchestrates the pentest toolchain, cua provides the isolation chamber for execution
- @osint-wiki/entities/tools/cua.md — sibling-wiki Phase-0 audit notes; cross-wiki context for the Cemini Conductor (REFERENCE-ONLY there)

## Raw Concept

Phase-0 audit completed 2026-05-13 via `briefs/2026-05-13_cua-adoption.md` (gitignored). Verdict: **GO** for cybersec-wiki primary adoption. Source repo: [github.com/trycua/cua](https://github.com/trycua/cua), MIT, 16,381 stars, 60 contributors.

## Narrative

cua (`trycua/cua`) is an agent-VM-sandbox framework purpose-built for M-series Macs. Architecture: **Lume** (a thin wrapper around Apple's Virtualization.Framework — no QEMU overhead) provides the VM substrate, the Python SDK + `cuabot` CLI orchestrate agent execution, and an MCP server exposes the whole stack to any MCP-compatible client (Claude Desktop, Claude Code, etc.). [CONFIRMED]

**The single most important cybersec feature** is the tracing API: every agent action emits a screenshot + accessibility tree + API-call log, which makes post-mortem replay possible. For red-team work this is the difference between "the agent owned the box" and "here is the exact sequence of clicks, payloads, and API calls that owned the box, replayable into a report" — invaluable for engagement deliverables and for IR-side analysis of attacker behavior. [CONFIRMED]

### Cybersec use cases [CONFIRMED]

- **LLM-driven exploit testing** — generate a PoC in a Lume VM with a clean OS image, detonate, capture trace. Host OS stays untouched.
- **Phishing-page detonation** — open suspicious URLs inside the VM, capture screenshots + DOM at every state transition.
- **Red-team agent reconnaissance** — drive a Claude-Code-style agent through `nmap → enumeration → exploit-suggestion` loops while the VM isolates everything that gets launched.
- **IR replay** — feed an attacker's recovered command stream into a matched VM image, capture what they would have seen, what the host EDR would have caught.

### Hardware floor [CONFIRMED]

- macOS Ventura (13.0)+ on Apple Silicon (M1 and later). Intel Macs are **out of scope** — Lume relies on Virtualization.Framework's M-series-specific paths.
- ~2-5 GB per VM image (macOS guest) or ~1-2 GB (Linux guest).
- Tracing payloads are GB-scale on long runs — see Dead Ends below.

### Integration footprint

- **MCP server** exposes cua to Claude Code / Claude Desktop / any MCP client. Standard skill-style integration; no custom protocol.
- **Python SDK** suits programmatic batches (CI-integrated red-team test suites).
- **cuabot CLI** suits ad-hoc interactive sessions.

### Pairings inside this wiki

- @entities/tools/pentest-ai-agents.md — natural complement; pentest-ai-agents orchestrates the 80+ pentest tools, cua provides the isolation chamber for execution.
- @entities/tools/fuzzyai.md — pair the LLM-adversarial fuzzer with cua-tracing to capture exactly what the jailbreak attempts looked like at each turn.

## Snippets

```bash
# canonical install (Apple Silicon, macOS 13+)
pip install cua
# launch a fresh Linux VM via Lume
lume run --image ubuntu-22.04-arm64 --cpu 4 --memory 8G
# drive an agent with tracing on
cuabot --tracing-dir ./traces/engagement-2026-05/ "enumerate the local network"
```

## Dead Ends

- **Tracing-payload disk pressure** — GB-scale full-screenshot+a11y traces will fill a default `~/cua-traces/` directory within a day of agentic work. Mitigation pattern documented at @concepts/agent-vm-sandboxing.md (rotation + S3 offload). [CONFIRMED]
- **Intel-Mac path** — Lume does not target x86_64 macOS. Teams running mixed-hardware fleets cannot standardize on cua across the team without provisioning M-series workstations. [CONFIRMED]
- **VM-escape attack surface is non-zero** — running adversarial LLM-generated exploits inside Lume does not eliminate the need for host-OS patching. Lume isolates, it does not absolve. [TENTATIVE — no published Lume escape as of 2026-05-13, but the framework is young enough that the absence-of-evidence caveat applies]
