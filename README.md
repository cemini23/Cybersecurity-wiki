# Cybersecurity Wiki

> Local knowledge hub for **cybersecurity research, training, and offensive/defensive operations**. LLM-managed, human-read.

## What this is

This workspace is a **librarian** for cybersecurity knowledge. It:

- **Manages** raw sources (PDFs, slide decks, video transcripts, repo snapshots) you drop into `research to be indexed/`
- **Curates** them into an interlinked wiki under `wiki/` — pages on certifications, tools, frameworks, threat actors, platforms, people, vendors, programming languages, and concepts
- **Applies** them by producing briefs in `briefs/` that you paste into claude.ai / Claude Desktop / hands-on workflows (engagement notes, SOC runbooks, CTF write-ups, certification cram sheets)

Everything lives on locally. No remote servers, no team distribution, no automation that touches third-party platforms.

The seed corpus (~227 PDFs) was contributed by [Joas A Santos](wiki/entities/people/joas-a-santos.md), a Brazilian cybersecurity educator with deep coverage of offensive security, red team operations, certification prep, SOC tooling, and youth cyber safety. Public release.

## Quick start

1. Read `CLAUDE.md` — that's the schema the LLM follows. (You'll only need to read it once; the LLM reads it every session.)
2. Read `ROADMAP.md` — current workstreams + open decisions.
3. Copy `.env.example` to `.env` and fill in whatever you have. Most fields can stay blank initially.
4. Copy `claude_desktop_config.json.example` to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) and replace the placeholders.
5. Drop a source into `research to be indexed/` and ask Claude to ingest it.

## Folder layout

```
Cybersecurity-wiki/
  CLAUDE.md                         # the schema the LLM reads each session
  README.md                         # this file
  LESSONS.md                        # meta-lessons (how we work)
  ROADMAP.md                        # active work + decisions + done log
  hot.md                            # session-state cache (gitignored)
  .env.example                      # env-var + intake template
  claude_desktop_config.json.example # Claude Desktop MCP config template
  research to be indexed/           # drop zone for new sources (gitignored)
  raw-sources/                      # archived sources after ingest (gitignored)
  briefs/                           # staged deliverables (gitignored)
  wiki/                             # the wiki proper
    index.md                        # catalog of all pages
    log.md                          # append-only operations log
    entities/                       # certifications, tools, frameworks, threat-actors, platforms, people, vendors, programming-languages
    concepts/                       # red-team-operations, av-edr-bypass, osint-for-pentest, soc-operations, etc.
    sources/                        # one page per ingested source
  scripts/                          # wiki_lint.py + helpers
  prompts/                          # reusable prompt templates
```

## Operations

The full operations spec lives in `CLAUDE.md`. Quick reference:

- **Ingest** — drop a source into `research to be indexed/`, ask Claude to ingest it. Claude creates a source page, updates entity/concept pages, appends to `log.md`, moves the file to `raw-sources/`.
- **Query** — ask Claude any question; it searches `wiki/index.md` first, then pages, then external MCP tools if needed.
- **Lint** — periodically run `python3 scripts/wiki_lint.py` to catch orphans, broken links, stale claims.
- **Distribute** — Claude produces a brief in `briefs/`; you copy/paste into the target surface.

## Sister wikis

This wiki is part of a four-wiki constellation. Cross-wiki links use `@<alias>/path/to/page.md` syntax. Aliases + paths in `CLAUDE.md` under "Related Wikis":

- `osint-wiki` — financial / quant / prediction-market research
- `image-gen-wiki` — uncensored image generation, ComfyUI, LoRA
- `seo-wiki` — local SEO, GBP, GEO/AEO, web design
- `3d-printing-wiki` — FDM/FFF, Bambu, slicers, print farms

Cybersecurity intersects all four: OSINT tradecraft (osint-wiki), deepfakes + adversarial-image attacks (image-gen-wiki), web-app security for client sites + spam-policy attacks (seo-wiki), physical-pentest tooling + RFID jigs (3d-printing-wiki).

## Privacy + safety

- `.env`, `raw-sources/`, `briefs/`, `hot.md`, `.claude/` are gitignored
- Only commit `CLAUDE.md`, `README.md`, `LESSONS.md`, `ROADMAP.md`, `wiki/`, `scripts/`, `prompts/`, `.gitignore`, `.env.example`, `claude_desktop_config.json.example`
- Never commit API keys or PII
- All techniques on these pages assume written authorization for the target. Operating outside scope is a crime in most jurisdictions.

## License

MIT — see `LICENSE`.
