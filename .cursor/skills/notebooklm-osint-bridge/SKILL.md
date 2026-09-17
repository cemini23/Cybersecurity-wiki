---
name: notebooklm-osint-bridge
description: >-
  Cemini OSINT workflow for NotebookLM via notebooklm-py (K69). Use when exporting
  wiki/briefs to Google NotebookLM for audio overview, Q&A, or study artifacts;
  after /notebooklm or "turn this brief into a podcast". Requires laptop auth
  (notebooklm login). Never upload prod secrets or credentials.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
---

# NotebookLM bridge (OSINT / Cemini)

Laptop-only operator tool. Canonical upstream skill: `notebooklm` (installed via `notebooklm skill install`). Wiki: `@ccc-wiki/concepts/claude-obsidian-notebooklm-bridge.md`, `@ccc-wiki/entities/tools/notebooklm-py.md`.

## Prerequisites

```bash
notebooklm auth check --test --json   # require "status": "ok" and token_fetch true
```

If not ok: `notebooklm login` then re-check.

## When to use

- User wants **audio overview**, quiz, infographic, or chat over a **curated export** of wiki pages or a brief
- Reviewing a **redacted** ingest summary before prod brief sign-off
- **Not** for librarian RAG, prod-mcp, or replacing kb-server

## Cemini redaction (mandatory before upload)

Strip or never include:

- `.local/server.md`, SSH configs, API keys, `.env`, `~/.cemini/*` tokens
- Raw wallet keys, Polymarket signing material, prod connection strings
- Unredacted `briefs/` destined for prod if they contain operator secrets

Prefer: exported markdown from `wiki/` concept/source pages, or a **sanitized** brief copy in `/tmp/`.

## Typical workflow

1. **Curate** — pick 1–15 markdown files (single topic); write a one-paragraph export manifest for the user if ambiguous.
2. **Create notebook** — `notebooklm create "OSINT <topic> <YYYY-MM-DD>"`
3. **Add sources** — URLs, PDFs, or local files per upstream `notebooklm` skill (use explicit notebook ID in automation: `-n` / `--notebook`).
4. **Generate** — audio overview / ask / artifact per user request.
5. **Download** — save artifacts under `briefs/` or user-specified path; cite NotebookLM as synthesis layer, not `[CONFIRMED]` market fact.

## Parallel agents

Use a dedicated profile when multiple chats might run NotebookLM:

```bash
export NOTEBOOKLM_PROFILE=osint-$(date +%Y%m%d)
notebooklm -p "$NOTEBOOKLM_PROFILE" login   # once per profile
```

Or pass explicit notebook IDs on every command (preferred).

## Full API surface

Read and follow the installed **`notebooklm`** skill (`.claude/skills/notebooklm/SKILL.md` or `notebooklm skill show`) for all CLI flags, artifact types, and autonomy rules.
