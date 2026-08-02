---
title: "GitHub — usestrix/strix"
type: source
tags: [github, strix, ai-pentest, harness, apache, phase0]
keywords: [usestrix/strix, Strix, Apache-2.0, Docker sandbox, PoC validation, strix-agent, OmniSecure]
related:
  - entities/tools/strix.md
  - concepts/ai-pentest-harness-landscape.md
  - entities/tools/cyberstrike.md
  - sources/github-cyberstrike.md
  - concepts/llm-pentest-automation.md
  - concepts/agent-vm-sandboxing.md
  - sources/github-strix-omlx.md
  - entities/tools/strix-omlx.md
maturity: draft
created: 2026-08-02
updated: 2026-08-02
read_status: skimmed
---

## Relations
- @entities/tools/strix-omlx.md

- @entities/tools/strix.md — tool entity (CONDITIONAL-GO; clone done)
- @concepts/ai-pentest-harness-landscape.md — landscape synthesis citing this source
- @entities/tools/cyberstrike.md — sibling harness for contrast
- @sources/github-cyberstrike.md — CyberStrike Phase-0 source snapshot
- @concepts/llm-pentest-automation.md — methodology umbrella
- @concepts/agent-vm-sandboxing.md — containment context for sandbox claims
- @sources/github-strix-omlx.md — Apple MLX/Ollama wrapper peer

## Raw Concept

| Field | Value |
|-------|--------|
| Title | usestrix/strix |
| Author / org | usestrix (OmniSecure Inc. copyright in LICENSE) |
| Type | GitHub repository |
| Location | https://github.com/usestrix/strix · local `raw-sources/repos/strix` |
| Retrieved | 2026-08-02 |
| SHA | `dbc427d8162008edd9e175224b6d1156577fb094` (shallow `main`) |
| Pages | n/a (repo) |
| Read-status | skimmed |

## Narrative

Phase-0 source snapshot for the Strix AI pentest harness. Shallow clone completed 2026-08-02 under `raw-sources/repos/strix` (~11MB). Verified **Apache-2.0**, Docker sandbox runtime (`strix/runtime/docker_client.py`, Kali image via `STRIX_IMAGE`), soft instruction-based scope, and **telemetry default-on** (PostHog + Scarf; `STRIX_TELEMETRY=0` opt-out). Install docs include curl\|bash — not used; PyPI package `strix-agent` noted for operator pipx/uv later.

Host CLI was **not** installed during Phase-0. See entity for verdict + human gates; brief `briefs/2026-08-02_strix-phase0.md` (gitignored) for checklist.

## Snippets

```text
URL: https://github.com/usestrix/strix
SPDX: Apache-2.0
Local: raw-sources/repos/strix @ dbc427d (main, depth=1)
Package: strix-agent==1.4.1
Default image: ghcr.io/usestrix/strix-sandbox:1.2.0
```

```bash
# Telemetry off (lab default)
export STRIX_TELEMETRY=0

# Optional: attach sandbox to a lab-only Docker network
export STRIX_DOCKER_SANDBOX_NETWORK=lab-net
```

## Dead Ends

- **Desk-only claims without clone** — superseded by this Phase-0.
- **curl\|sh install** — rejected by federation policy; use pipx/uv after operator OK.
