---
title: "src-hunter-skill — Claude Code bug-bounty / pentest skill (305 payloads, 19 playbooks)"
type: entity
tags: [tool, bug-bounty, pentest, claude-code, skill, waf-bypass, jshookmcp, mit, adopt]
keywords: [src-hunter-skill, myurikanao, claude code skill, src, bug bounty, waf bypass, jshookmcp, frida, wasm reverse engineering, payload library]
related:
  - concepts/bug-bounty.md
  - concepts/web-pentest-methodology.md
  - entities/tools/pentest-ai-agents.md
  - concepts/ai-for-cybersecurity.md
  - entities/tools/nvidia-skillspector.md
maturity: draft
created: 2026-05-21
updated: 2026-05-31
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-19url-2026-05-20.md"
---

# src-hunter-skill — Claude Code bug-bounty / pentest skill

## Relations

- @concepts/bug-bounty.md — SRC / bug-bounty workflow integration
- @concepts/web-pentest-methodology.md — WAF bypass variants for web-app testing
- @entities/tools/pentest-ai-agents.md — complementary Claude Code skill framework
- @concepts/ai-for-cybersecurity.md — LLM-driven offensive tooling
- @entities/tools/nvidia-skillspector.md — vet third-party skills before install (K88)

## Raw Concept

Routed from K55 OSINT-wiki tool eval (2026-05-20). Comprehensive Claude Code skill for SRC/bug-bounty/penetration testing. Adopt-tier, MIT.

## Narrative

`MyuriKanao/src-hunter-skill` (MIT) packages 305 structured payloads, 19 attack playbooks, and 263 WAF bypass variants as a Claude Code skill. Integrates `jshookmcp` MCP server for browser manipulation, Frida memory validation, and WASM reverse engineering.

Per K55 eval: "directly implements the offensive operations, red-teaming, and exploit development methodologies documented in the Cybersec wiki." MIT license enables immediate adoption.

**Action item**: clone and audit `jshookmcp` (the embedded MCP server) for execution integrity before integrating into any workflow. The payload library and WAF bypass catalog are safe to reference immediately.
