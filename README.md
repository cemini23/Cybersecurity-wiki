# Cybersecurity Wiki

> A local knowledge hub for **cybersecurity research, training, and offensive/defensive operations** — LLM-managed, human-read. Welcome in.

## What this is

This workspace is a **librarian** for cybersecurity knowledge. It:

- **Manages** raw sources (PDFs, slide decks, video transcripts, repo snapshots) you drop into `research to be indexed/`
- **Curates** them into an interlinked wiki under `wiki/` — certifications, tools, frameworks, threat actors, platforms, people, vendors, programming languages, and concepts
- **Applies** them as briefs in `briefs/` that you paste into claude.ai / Claude Desktop or hands-on workflows (engagement notes, SOC runbooks, CTF write-ups, certification cram sheets)

Everything for this wiki lives on your laptop. No remote wiki servers, no team distribution, and no automation that posts to third-party platforms without you.

The **seed corpus** (~227 PDFs) was contributed by [Joas A Santos](wiki/entities/people/joas-a-santos.md), a Brazilian cybersecurity educator with deep coverage of offensive security, red team operations, certification prep, SOC tooling, and youth cyber safety. Later shared-folder ingests added a **Redteam Kit** and a **BlueTeam Kit**, plus a Kali Linux video course. Ongoing research ingests (labs, papers, FOSS audits) have grown the catalog to **~436 source pages**, alongside entity and concept coverage that now also includes **agent-security / local whitehat lab** patterns.

## Quick start

1. Read `CLAUDE.md` — the schema the LLM follows each session (you only need it once as a human).
2. Skim `ROADMAP.md` — active workstreams and open decisions.
3. Copy `.env.example` to `.env` and fill in what you have. Most fields can stay blank at first.
4. (Optional) Copy `claude_desktop_config.json.example` into Claude Desktop’s config path and replace the placeholders.
5. Drop a source into `research to be indexed/` and ask your LLM assistant to ingest it.

## Folder layout

```
Cybersecurity-wiki/
  CLAUDE.md                          # schema the LLM reads each session
  README.md                          # this file
  LESSONS.md                         # meta-lessons (how we work)
  ROADMAP.md                         # active work + decisions + done log
  hot.md                             # session-state cache (gitignored)
  .env.example                       # env-var + intake template
  claude_desktop_config.json.example # Claude Desktop MCP config template
  research to be indexed/            # drop zone for new sources (gitignored)
  raw-sources/                       # local raw corpus / clones (gitignored)
  briefs/                            # staged deliverables (mostly gitignored)
  wiki/                              # the wiki proper
    index.md                         # catalog of all pages
    log.md                           # append-only operations log
    entities/                        # certs, tools, frameworks, threat-actors, …
    concepts/                        # red-team-ops, SOC, agent-security, …
    sources/                         # one page per ingested source
  scripts/                           # wiki_lint.py + helpers
  prompts/                           # reusable prompt templates
```

## Operations

The full operations spec lives in `CLAUDE.md`. Quick reference:

- **Ingest** — drop a source into `research to be indexed/`, ask the LLM to ingest it. It creates a source page, updates entity/concept pages, appends `wiki/log.md`, and archives the raw file (canon: egress bulk store via the OSINT archive helper; see `CLAUDE.md`).
- **Query** — ask a question; the LLM searches `wiki/index.md` first, then pages, then external MCP tools if needed.
- **Lint** — periodically run `python3 scripts/wiki_lint.py` to catch orphans, broken links, and stale claims.
- **Distribute** — a brief lands in `briefs/`; you copy/paste into the target surface.

## Cemini wiki federation

**Eight** wikis + private **Cemini Financial Suite**. Cross-links use `@<alias>/path/to/page.md` (see `CLAUDE.md` → Related Wikis).

| Alias | Repository | Visibility | Focus |
|-------|------------|------------|--------|
| **`cybersecurity-wiki`** | **This repo** ([Cybersecurity-wiki](https://github.com/cemini23/Cybersecurity-wiki)) | **Public** | Pentest, red team, SOC, certifications, agent-security lab |
| `gambling-wiki` | [Gambling-wiki](https://github.com/cemini23/Gambling-wiki) | **Public** | Sports betting, casino, poker, DFS |
| `game-dev-wiki` | [Game-Dev-wiki](https://github.com/cemini23/Game-Dev-wiki) | **Public** | Hobby game dev — castle/RTS, Godot evals |
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

- `.env`, `raw-sources/`, most of `briefs/`, `hot.md`, and `.claude/` are gitignored
- Commit schema + wiki content only (`CLAUDE.md`, `README.md`, `LESSONS.md`, `ROADMAP.md`, `wiki/`, `scripts/`, `prompts/`, examples, license)
- Never commit API keys or PII
- Techniques on these pages assume **written authorization** for the target. Operating outside scope is a crime in most jurisdictions.

## Related

- Methodology newsletter: [Outlier Weekly](https://outlierweekly.substack.com)
- YouTube: [@Cemini23](https://www.youtube.com/@Cemini23)
- Products: [Atto](https://youratto.com) · [GuruWatcher](https://guruwatcher.com)
- Wiki federation hub: [cemini-claude-code-CCC](https://github.com/cemini23/cemini-claude-code-CCC)
- Agent toolkit: [wikilint](https://github.com/cemini23/wikilint) · [vet](https://github.com/cemini23/vet) · [ara-schema](https://github.com/cemini23/ara-schema)
- Sibling wikis: [SEO/GEO](https://github.com/cemini23/SEO-GEO-B-M-Wiki) · [3D Printing](https://github.com/cemini23/3D-Printing-Wiki) · [Image Gen](https://github.com/cemini23/uncensored-image-gen-wiki) · [Gambling](https://github.com/cemini23/Gambling-wiki) · [Game Dev](https://github.com/cemini23/Game-Dev-wiki)
- Canonical donation wallets: [SUPPORT.md](https://github.com/cemini23/cemini-claude-code-CCC/blob/main/SUPPORT.md) (CCC)

## Support

Thank you for your interest — and for any support, large or small. Tips and kind words both help keep the public research and tooling open.

Voluntary tips fund open research and tooling. **Donation-only addresses** — not trading or production wallets.

| Chain family | Address |
|--------------|---------|
| **X Money** (fiat, US) | Request [@Cemini23](https://x.com/Cemini23) in the X app — scan the Request QR |
| **EVM** (Ethereum, Polygon, Base, Arbitrum, …) | `0x444C5C2eC439E0382aa5a17F70313c536BcC5D58` |
| **Solana / SVM** | `J4zNn4hK9jTrKBFY8sbAGJHLoZvXvQf4B9pQSbSrocZE` |
| **Polymarket** (referral) | [polymarket.com/?r=Cemini23](https://polymarket.com/?r=Cemini23) |
| **Hyperliquid** (referral) | [app.hyperliquid.xyz/join/CEMINI23](https://app.hyperliquid.xyz/join/CEMINI23) |

If you’d rather follow along or try something we ship:

- Newsletter — [Outlier Weekly](https://outlierweekly.substack.com) (Substack)
- Genealogy kit — [youratto.com](https://youratto.com)
- Newsletter parameter alerts — [guruwatcher.com](https://guruwatcher.com)
- YouTube — [@Cemini23](https://www.youtube.com/@Cemini23)

We’re grateful you’re here. Thank you for your support.

## License

MIT — see `LICENSE`.
