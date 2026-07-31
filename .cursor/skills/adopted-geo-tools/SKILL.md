---
name: adopted-geo-tools
description: >-
  Use Cemini-adopted GEO/website tools (E-GEO rewrite prompts, geo-optimizer CLI,
  wondelai CRO skills) owned by the SEO/GEO wiki. Trigger from ANY Cursor workspace
  when rewriting local-business service pages for AI citation, auditing a site for
  GEO/AEO readiness, diagnosing why a brick-and-mortar site does not convert/book,
  or the user mentions E-GEO / geo-optimizer / wondelai CRO.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
---

# Adopted GEO / website tools (federation)

Canon + on-disk clones live in the **SEO/GEO wiki**. This skill is synced to
`~/.cursor/skills/` and all Cemini Cursor workspaces via CCC
`scripts/sync_federation_cursor_skills.sh` — use it from any open folder.

```bash
SEO_ROOT="/Users/claudiobarone/Projects/SEO:GEO B&M Business"
```

Always `cd "$SEO_ROOT"` (or pass absolute paths) before running helpers — do not
assume the current workspace root is the SEO wiki.

## E-GEO service-page rewrite

```bash
cd "$SEO_ROOT"
python3 scripts/e_geo_rewrite_service_page.py --list
python3 scripts/e_geo_rewrite_service_page.py --style competitive --file path/to/copy.md
```

1. Run the printed prompt in-session with **only factual** shop copy.
2. Stage before/after under `"$SEO_ROOT/briefs/"`.
3. Measure with `@seo-wiki/concepts/geo-visibility-vector-protocol.md` (or open that file under `$SEO_ROOT/wiki/…`).

Recommended styles: `competitive`, `FAQ`, `authoritative`, `format`.

Prompts on disk: `$SEO_ROOT/raw-sources/tools/E-GEO/src/optimized_prompts.json`

## geo-optimizer-skill audit

```bash
cd "$SEO_ROOT"
bash scripts/run_geo_audit.sh https://THE-SHOP-SITE
```

- Needs a real shop URL — fill `$SEO_ROOT/wiki/entities/companies/shop-1.md` if blank.
- Citation scores are **directional**; pair with bootstrap CIs (geo-visibility-measurement).
- **Ignore** `/llms.txt` recommendations for Google Search (first-party mythbust).

Local clone: `$SEO_ROOT/raw-sources/tools/geo-optimizer-skill`

## wondelai CRO / website journeys

Read from disk (do not re-invent):

- `$SEO_ROOT/raw-sources/tools/wondelai-skills/cro-methodology/SKILL.md`
- `$SEO_ROOT/raw-sources/tools/wondelai-skills/improve-website/SKILL.md`
- `$SEO_ROOT/raw-sources/tools/wondelai-skills/ux-heuristics/SKILL.md`

Big-5 objections for local B&M: Trust, Price, Fit, Timing, Effort — mine reviews/GBP for voice-of-customer language.

### Operator (optional Claude Code plugin install)

```bash
npx skills add wondelai/skills/cro-methodology --global
npx skills add wondelai/skills/improve-website --global
npx skills add wondelai/skills/ux-heuristics --global
```

Agents can read the local clones without that install.

## Re-deploy this skill after edits

```bash
bash "/Users/claudiobarone/Projects/Cemini claude code CCC/scripts/sync_federation_cursor_skills.sh"
```
