#!/usr/bin/env bash
# obsidian-setup.sh — Initialize an Obsidian vault for the SEO/GEO/B&M wiki
#
# What this does:
#   1. Creates an Obsidian vault folder (defaults: ~/Documents/SEO-GEO-B-M-Vault)
#   2. Symlinks the wiki/ folder so edits stay in sync with the repo
#   3. Writes recommended Obsidian settings (core plugins, new-link format)
#   4. Generates a starter .obsidian/plugins.json recommending community plugins
#
# Usage:
#   bash scripts/obsidian-setup.sh                  # defaults
#   bash scripts/obsidian-setup.sh --vault ~/custom # custom vault path
#   bash scripts/obsidian-setup.sh --dry-run        # preview without writing
#
# Requirements: Obsidian installed (checks for it). macOS primary; Linux supported.
# This script does NOT launch Obsidian — that's the operator's step.

set -euo pipefail

# ── Defaults ────────────────────────────────────────────────────────────────

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VAULT_ROOT="${VAULT_ROOT:-$HOME/Documents/SEO-GEO-B-M-Vault}"
DRY_RUN=false

while [[ $# -gt 0 ]]; do
    case "$1" in
        --vault) VAULT_ROOT="$2"; shift 2 ;;
        --dry-run) DRY_RUN=true; shift ;;
        --help|-h)
            echo "Usage: $0 [--vault PATH] [--dry-run]"
            echo ""
            echo "Options:"
            echo "  --vault PATH   Vault directory (default: \$HOME/Documents/SEO-GEO-B-M-Vault)"
            echo "  --dry-run      Show what would happen without writing anything"
            echo "  --help         This message"
            exit 0
            ;;
        *) echo "Unknown option: $1" >&2; exit 1 ;;
    esac
done

# ── Preflight checks ───────────────────────────────────────────────────────

echo "=== Obsidian Vault Setup for SEO/GEO/B&M Wiki ==="
echo ""

# Check Obsidian is installed
OBSIDIAN_PATH=""
for candidate in \
    "/Applications/Obsidian.app/Contents/MacOS/Obsidian" \
    "$HOME/Applications/Obsidian.app/Contents/MacOS/Obsidian" \
    "$(which obsidian 2>/dev/null || true)"; do
    if [[ -x "$candidate" ]]; then
        OBSIDIAN_PATH="$candidate"
        break
    fi
done

if [[ -z "$OBSIDIAN_PATH" ]]; then
    echo "⚠️  Obsidian not found in standard locations."
    echo "   Install it from: https://obsidian.md"
    echo "   Re-run this script after installing."
    # Continue anyway — we can still set up the vault folder
fi

# Check repo structure
if [[ ! -d "$REPO_ROOT/wiki" ]]; then
    echo "❌ Wiki directory not found at $REPO_ROOT/wiki"
    echo "   Are you running from the repo root?"
    exit 1
fi

echo "  Repo root:    $REPO_ROOT"
echo "  Vault target: $VAULT_ROOT"
echo ""

# ── Phase 1: Create vault structure ────────────────────────────────────────

if [[ "$DRY_RUN" == "true" ]]; then
    echo "[DRY RUN] Would create vault at: $VAULT_ROOT"
else
    mkdir -p "$VAULT_ROOT"
    echo "✅ Created vault directory: $VAULT_ROOT"
fi

# Symlink wiki/ → vault root (so Obsidian sees the full folder tree)
# We symlink individual top-level items so the vault root IS the repo root
# for reading purposes, but we don't symlink .git, .github, .env, etc.
LINK_ITEMS=(
    "wiki"
    "CLAUDE.md"
    "README.md"
    "LESSONS.md"
    "ROADMAP.md"
    "hot.md"
    "briefs"
    "prompts"
    "scripts"
    "raw-sources"
    "research to be indexed"
)

for item in "${LINK_ITEMS[@]}"; do
    src="$REPO_ROOT/$item"
    dst="$VAULT_ROOT/$item"

    # Skip items that don't exist in the repo
    [[ -e "$src" ]] || continue

    if [[ "$DRY_RUN" == "true" ]]; then
        echo "[DRY RUN] Would symlink: $item"
        continue
    fi

    if [[ -L "$dst" ]]; then
        echo "  ↻ Symlink already exists: $item"
    elif [[ -e "$dst" ]]; then
        echo "  ⚠️  Conflict (not a symlink): $item — skipping"
    else
        ln -s "$src" "$dst"
        echo "  ✅ Symlinked: $item"
    fi
done

echo ""

# ── Phase 2: Obsidian config files ─────────────────────────────────────────

OBSIDIAN_DIR="$VAULT_ROOT/.obsidian"

if [[ "$DRY_RUN" == "true" ]]; then
    echo "[DRY RUN] Would create/update: $OBSIDIAN_DIR/"
else
    mkdir -p "$OBSIDIAN_DIR"
fi

# app.json — recommended core settings
APP_JSON='{
  "attachmentFolderPath": "",
  "newFileLocation": "folder",
  "newFileFolderPath": "wiki",
  "newFileFormat": "markdown",
  "newLinkFormat": "relative-path",
  "useWikilinks": true,
  "showLineCount": true,
  "showLineNumber": true,
  "userIgnoreFragmentTestPattern": ""
}'

if [[ "$DRY_RUN" == "true" ]]; then
    echo "[DRY RUN] Would write: .obsidian/app.json"
else
    echo "$APP_JSON" > "$OBSIDIAN_DIR/app.json"
    echo "  ✅ Written: .obsidian/app.json"
fi

# core-plugins.json — enable core plugins
CORE_PLUGINS='{
  "file-explorer": true,
  "global-search": true,
  "switcher": true,
  "graph": true,
  "backlink": true,
  "outgoing-link": true,
  "tag-pane": true,
  "page-preview": true,
  "daily-notes": false,
  "templates": false,
  "command-palette": true,
  "editor-status": true,
  "starred": true,
  "outline": true,
  "word-count": false,
  "file-recovery": true
}'

if [[ "$DRY_RUN" == "true" ]]; then
    echo "[DRY RUN] Would write: .obsidian/core-plugins.json"
else
    echo "$CORE_PLUGINS" > "$OBSIDIAN_DIR/core-plugins.json"
    echo "  ✅ Written: .obsidian/core-plugins.json"
fi

# community-plugins.json — recommended community plugins to install
# (These can't be auto-installed; this file serves as a shopping list.)
COMMUNITY_PLUGINS='[
  {
    "id": "dataview",
    "name": "Dataview",
    "reason": "Query YAML frontmatter like a database (e.g. all draft sources, all entities by type)"
  },
  {
    "id": "obsidian-tag-wrangler",
    "name": "Tag Wrangler",
    "reason": "Bulk rename and merge tags as the wiki grows"
  },
  {
    "id": "obsidian-local-rest-api",
    "name": "Local REST API",
    "reason": "Programmatic access to vault (useful for automation scripts)"
  },
  {
    "id": "obsidian-file-explorer-note-count-plugin",
    "name": "File Explorer Note Count",
    "reason": "See paragraph/word counts in the file explorer sidebar"
  },
  {
    "id": "obsidian-minimal",
    "name": "Minimal Theme",
    "reason": "Clean, distraction-free reading for long wiki sessions"
  },
  {
    "id": "things",
    "name": "Things",
    "reason": "Style Obsidian as a Things-like task manager (optional aesthetic)"
  }
]'

if [[ "$DRY_RUN" == "true" ]]; then
    echo "[DRY RUN] Would write: .obsidian/community-plugins.json"
else
    echo "$COMMUNITY_PLUGINS" > "$OBSIDIAN_DIR/community-plugins.json"
    echo "  ✅ Written: .obsidian/community-plugins.json"
fi

# ── Phase 3: Convenience symlinks for repo-side tooling ────────────────────

# Also symlink the repo root into the vault so scripts that reference
# repo-relative paths (e.g., scripts/wiki_lint.py) work from inside the vault
if [[ "$DRY_RUN" == "true" ]]; then
    echo "[DRY RUN] Would symlink repo root for script compatibility"
else
    REPO_LINK="$VAULT_ROOT/_repo-root"
    if [[ -L "$REPO_LINK" ]]; then
        echo "  ↻ Repo root symlink already exists"
    else
        ln -s "$REPO_ROOT" "$REPO_LINK"
        echo "  ✅ Symlinked repo root → _repo-root"
    fi
fi

# ── Summary ─────────────────────────────────────────────────────────────────

echo ""
echo "=== Setup ${DRY_RUN:+DRY RUN }Complete ==="
echo ""
echo "Next steps:"
echo "  1. Open Obsidian → 'Open folder as vault' → select: $VAULT_ROOT"
echo "  2. Install recommended community plugins:"
echo "       - Dataview (query YAML frontmatter)"
echo "       - Tag Wrangler (tag management)"
echo "       - Local REST API (automation)"
echo "  3. Start reading: open wiki/index.md"
echo "  4. For cross-link navigation, see: concepts/obsidian-navigation.md"
echo ""
echo "Note: .obsidian/ contains your personal vault preferences."
echo "      These are gitignored — your settings stay on your machine."
echo ""

if [[ -n "$OBSIDIAN_PATH" ]]; then
    echo "Found Obsidian at: $OBSIDIAN_PATH"
    echo "To launch now: open '$VAULT_ROOT' in Obsidian"
else
    echo "Obsidian not found — install it first, then open the vault manually."
fi