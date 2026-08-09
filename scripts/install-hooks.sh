#!/usr/bin/env bash
# Install local git hooks for OSINT WORKSPACE.
#
# Hooks live in scripts/*.sh (versioned in the repo). This script symlinks
# them into .git/hooks/ so they fire on git operations. Idempotent —
# rerun safely after a fresh clone or if .git/hooks gets cleared.
#
# Usage:
#   bash scripts/install-hooks.sh

set -euo pipefail

# Resolve repo root from script location (scripts/ → repo root).
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HOOKS_DIR="$REPO_ROOT/.git/hooks"

if [[ ! -d "$HOOKS_DIR" ]]; then
    echo "Error: $HOOKS_DIR does not exist. Are you inside a git working tree?"
    exit 1
fi

install_hook() {
    local hook_name="$1"
    local script_name="$2"
    local target="$HOOKS_DIR/$hook_name"
    local source_path="$REPO_ROOT/scripts/$script_name"

    if [[ ! -f "$source_path" ]]; then
        echo "Error: $source_path does not exist"
        exit 1
    fi

    # Make sure the source is executable (idempotent).
    chmod +x "$source_path"

    # Use a relative symlink so the link survives if the workspace gets
    # moved. .git/hooks/pre-commit → ../../scripts/pre-commit.sh
    ln -sf "../../scripts/$script_name" "$target"
    echo "  installed: $hook_name → ../../scripts/$script_name"
}

echo "Installing git hooks..."
install_hook "pre-commit" "pre-commit.sh"
install_hook "post-commit" "post-commit.sh"
echo ""
echo "Done. Verify with:"
echo "  ls -la $HOOKS_DIR | grep -v sample"
