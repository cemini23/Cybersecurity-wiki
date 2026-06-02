# Cybersecurity Wiki

> Local knowledge hub for **cybersecurity research, training, and offensive/defensive operations**. LLM-managed, human-read.

## What this is

This workspace is a **librarian** for cybersecurity knowledge. It:

- **Manages** raw sources (PDFs, slide decks, video transcripts, repo snapshots) you drop into `research to be indexed/`
- **Curates** them into an interlinked wiki under `wiki/` — pages on certifications, tools, frameworks, threat actors, platforms, people, vendors, programming languages, and concepts
- **Applies** them by producing briefs in `briefs/` that you paste into claude.ai / Claude Desktop / hands-on workflows (engagement notes, SOC runbooks, CTF write-ups, certification cram sheets)

Everything lives locally. No remote servers, no team distribution, no automation that touches third-party platforms.

The **seed corpus** (~226 PDFs) was contributed by [Joas A Santos](wiki/entities/people/joas-a-santos.md), a Brazilian cybersecurity educator with deep coverage of offensive security, red team operations, certification prep, SOC tooling, and youth cyber safety. Public release. Since then the wiki has grown through additional shared-folder ingests — a **Redteam Kit** (22 English-language pentest references) and a **BlueTeam Kit** (26 SOC / defensive PDFs — SIEM, threat hunting, incident response, EDR), plus a 50-chapter Kali Linux video course — for **275 source pages** in total.

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

## Cemini wiki federation

**Seven** wikis + private **Cemini Financial Suite**. Cross-links: `@<alias>/path/to/page.md` (`CLAUDE.md` → Related Wikis).

| Alias | Repository | Visibility | Focus |
|-------|------------|------------|--------|
| **`cybersecurity-wiki`** | **This repo** ([Cybersecurity-wiki](https://github.com/cemini23/Cybersecurity-wiki)) | **Public** | Pentest, red team, SOC, certifications |
| `gambling-wiki` | [Gambling-wiki](https://github.com/cemini23/Gambling-wiki) | **Public** | Sports betting, casino, poker, DFS |
| `ccc-wiki` | [cemini-claude-code-CCC](https://github.com/cemini23/cemini-claude-code-CCC) | **Public** | Agent orchestration, MCP, skill security patterns |
| `osint-wiki` | `llm-wiki-by-cemini` *(private)* | **Private** | OSINT tradecraft overlap |
| `image-gen-wiki` | [uncensored-image-gen-wiki](https://github.com/cemini23/uncensored-image-gen-wiki) | Public | Deepfakes, adversarial-image attacks |
| `seo-wiki` | [SEO-GEO-B-M-Wiki](https://github.com/cemini23/SEO-GEO-B-M-Wiki) | Public | Web-app security, spam-policy attacks |
| `3d-printing-wiki` | [3D-Printing-Wiki](https://github.com/cemini23/3D-Printing-Wiki) | Public | Physical pentest tooling, RFID jigs |
| *Cemini Financial Suite* | `Cemini-Financial-Suite` *(private)* | **Private** | Trading stack (not a wiki) |

**Privacy:** **`ccc-wiki` is public.** **`osint-wiki`** and **Cemini Financial Suite** are private.

```bash
git clone https://github.com/cemini23/Cybersecurity-wiki.git
```

## Privacy + safety

- `.env`, `raw-sources/`, `briefs/`, `hot.md`, `.claude/` are gitignored
- Only commit `CLAUDE.md`, `README.md`, `LESSONS.md`, `ROADMAP.md`, `wiki/`, `scripts/`, `prompts/`, `.gitignore`, `.env.example`, `claude_desktop_config.json.example`
- Never commit API keys or PII
- All techniques on these pages assume written authorization for the target. Operating outside scope is a crime in most jurisdictions.

## Related

- Methodology newsletter: [Outlier Weekly](https://outlierweekly.substack.com)
- YouTube: [@Cemini23](https://www.youtube.com/@Cemini23)
- Wiki federation hub: [cemini-claude-code-CCC](https://github.com/cemini23/cemini-claude-code-CCC)
- Agent toolkit: [wikilint](https://github.com/cemini23/wikilint) · [vet](https://github.com/cemini23/vet) · [ara-schema](https://github.com/cemini23/ara-schema)
- Sibling wikis: [SEO/GEO](https://github.com/cemini23/SEO-GEO-B-M-Wiki) · [3D Printing](https://github.com/cemini23/3D-Printing-Wiki) · [Image Gen](https://github.com/cemini23/uncensored-image-gen-wiki)


## Support

Voluntary tips fund open research and tooling. **Donation-only addresses** — not trading or production wallets.

| Chain family | Address |
|--------------|---------|
| **EVM** (Ethereum, Polygon, Base, Arbitrum, …) | `0x444C5C2eC439E0382aa5a17F70313c536BcC5D58` |
| **Solana / SVM** | `J4zNn4hK9jTrKBFY8sbAGJHLoZvXvQf4B9pQSbSrocZE` |


## License

MIT — see `LICENSE`.
