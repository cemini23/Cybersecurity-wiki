---
title: "GitHub — CyberStrikeus/CyberStrike (AI offensive harness)"
type: source
tags: [source, github, pentest, llm-automation, agpl]
keywords: [CyberStrike, CyberStrikeus, OpenCode fork, AGPL-3.0, Bolt, scope_check]
related:
  - entities/tools/cyberstrike.md
  - concepts/llm-pentest-automation.md
  - concepts/operator-lab-playbook.md
  - concepts/agent-vm-sandboxing.md
  - concepts/ai-pentest-harness-landscape.md
  - sources/github-strix.md
maturity: draft
created: 2026-08-02
updated: 2026-08-02
read_status: read
---

## Relations
- @sources/github-strix.md — Strix upstream source stub
- @entities/tools/cyberstrike.md — Phase-0 entity + adoption stamp
- @concepts/llm-pentest-automation.md — methodology comparison surface
- @concepts/operator-lab-playbook.md — operator path that may consume this tool in lab
- @concepts/agent-vm-sandboxing.md — required isolation (upstream no-sandbox)
- @concepts/ai-pentest-harness-landscape.md — AI pentest harness landscape (CyberStrike as one AGPL entry)

## Raw Concept

| Field | Value |
|-------|--------|
| Title | CyberStrike — open-source AI agent for offensive security |
| Author / org | CyberStrikeus (fork of anomalyco/opencode) |
| Type | GitHub repository + npm package |
| URL | https://github.com/CyberStrikeus/CyberStrike |
| Homepage | https://cyberstrike.io |
| Docs | https://docs.cyberstrike.io |
| License | AGPL-3.0 |
| Retrieved | 2026-08-02 |
| Local location | `raw-sources/repos/CyberStrike` (shallow, branch `dev` @ `93a51658`, ~219MB) |
| Read-status | read (README, LICENSE, SECURITY.md, CHANGELOG provenance, scope-check.ts, methodology context, package.json, containers README) |

## Narrative

Phase-0 source page for the CyberStrike harness. Key verified claims: AGPL-3.0; OpenCode fork; no sandbox (SECURITY.md); advisory `scope_check` tool; Ollama/LM Studio offline path; Bolt remote execution; ~7.6k skill markdown files in-tree. Full synthesis and verdict live on @entities/tools/cyberstrike.md.

## Snippets

```text
# SECURITY.md — No Sandbox
CyberStrike does not sandbox the agent. The permission system exists as a UX
feature … If you need true isolation, run CyberStrike inside a Docker
container or VM.
```

```text
# CHANGELOG provenance
Fork of opencode (anomalyco/opencode) with offensive security focus
Rebrand: OpenCode → CyberStrike
```

[Source: github.com/CyberStrikeus/CyberStrike @ 93a51658]
