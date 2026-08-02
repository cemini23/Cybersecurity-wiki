---
title: "GitHub — sw30labs/strix-omlx (Strix → local MLX/Ollama)"
type: source
tags: [source, github, local-llm, apple-silicon, pentest, phase0]
keywords: [strix-omlx, OMLX, Heretic, Apple Silicon, abliterated, Apache-2.0]
related:
  - entities/tools/strix-omlx.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - entities/tools/strix.md
  - concepts/ai-pentest-harness-landscape.md
  - sources/github-strix.md
  - entities/tools/ollama.md
maturity: draft
created: 2026-08-02
updated: 2026-08-02
read_status: skimmed
---

## Relations

- @entities/tools/strix-omlx.md — Phase-0 entity (CONDITIONAL-GO clone)
- @concepts/local-abliterated-llm-pentest-stack.md — Apple Silicon / OMLX / abliterated model wiring pattern
- @entities/tools/strix.md — Strix harness (CONDITIONAL-GO Phase-0 clone)
- @concepts/ai-pentest-harness-landscape.md — harness landscape
- @sources/github-strix.md — upstream Strix Phase-0 source snapshot
- @entities/tools/ollama.md — Ollama backend path

## Raw Concept

| Field | Value |
|-------|--------|
| Title | strix-omlx — run Strix against local OMLX/Ollama/SGLang with abliterated models |
| Author / org | sw30labs |
| URL | https://github.com/sw30labs/strix-omlx |
| License | Apache-2.0 (SPDX) |
| Stars (audit) | 0 |
| Pushed at | 2026-07-05T18:02:00Z |
| Clone | `raw-sources/repos/strix-omlx` shallow `main` @ `b623b9f1c1a4b45c5ef96fe6e93beae5c0540bad` (~3.3MB) |
| Retrieved | 2026-08-02 |
| Read-status | skimmed (Phase-0: README + LICENSE + setup scripts) |

## Narrative

Thin wrapper (not a fork of Strix) that installs/configures `strix-agent` against a **local** OpenAI-compatible inference server:

- **OMLX** (MLX, Apple Silicon) — primary path; default model id `MiniMax-M2.7-ultra-uncensored-heretic-oQ4-MLX` (Heretic abliteration)
- **Ollama** — cross-platform local path
- **SGLang** — NVIDIA DGX path

Phase-0 2026-08-02: LICENSE verified Apache-2.0; clone under `raw-sources/repos/strix-omlx`; host setup scripts **not** executed. Entity verdict **CONDITIONAL-GO** (clone/docs only). See @entities/tools/strix-omlx.md for failure modes (Apple-primary OMLX, pip install side effect, missing `STRIX_TELEMETRY=0`, abliterated-weight ethics, soft scope).

Companion research repo (not Phase-0’d here): `sw30labs/strix-research`.

## Snippets

```text
Scripts: setup-strix-omlx.sh | setup-strix-ollama.sh | setup-strix-sglang-dgx.sh | run-strix.sh
Prerequisite: Docker running (Strix sandbox); Python ≥3.12; local model server up
Authorized use only language present in README
```

[Source: github.com/sw30labs/strix-omlx @ b623b9f]
