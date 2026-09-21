#!/usr/bin/env python3
"""One-shot hardening for ~/.claude — deny list, scoped SSH, local-only claude-mem MCP."""
from __future__ import annotations

import json
from pathlib import Path

HOME = Path.home()
CLAUDE = HOME / ".claude"

DENY = [
    "Read(.env)",
    "Read(.env.*)",
    "Read(**/.ssh/id_rsa)",
    "Read(**/.ssh/id_ed25519)",
    "Read(**/*.pem)",
    "Read(**/watches.json)",
    "Write(**/watches.json)",
    "Edit(**/watches.json)",
    "Bash(cat .env)",
    "Bash(cat .env.*)",
    "Bash(printenv *KEY*)",
    "Bash(printenv *TOKEN*)",
    "Bash(printenv *SECRET*)",
    "Bash(curl *|*sh*)",
    "Bash(curl *|*bash*)",
]

ALLOW = [
    "Bash(crontab *)",
    "Bash(chmod +x *)",
    'Bash("/Users/claudiobarone/Projects/OSINT WORKSPACE/scripts/cemini_prod_healthcheck.sh")',
    "Bash(git *)",
    'Bash(python3 "/Users/claudiobarone/Projects/OSINT WORKSPACE/scripts/wiki_lint.py")',
]


ASK = [
    "Bash(ssh cemini-prod *)",
    "Bash(ssh cemini-egress-fi *)",
    "Bash(ssh -J cemini-prod cemini-egress-fi *)",
]

def main() -> int:
    local_path = CLAUDE / "settings.local.json"
    local_data = json.loads(local_path.read_text())
    local_data["permissions"] = {"allow": ALLOW, "deny": DENY, "ask": ASK}
    local_data["enableAllProjectMcpServers"] = False
    local_path.write_text(json.dumps(local_data, indent=2) + "\n")
    print("OK settings.local.json")

    settings_path = CLAUDE / "settings.json"
    settings = json.loads(settings_path.read_text())
    settings["permissions"] = {"deny": DENY, "allow": [], "ask": ASK}
    hooks = settings.setdefault("hooks", {})
    pretool = local_data.get("hooks", {}).get("PreToolUse")
    if pretool and "PreToolUse" not in hooks:
        hooks["PreToolUse"] = pretool
    settings_path.write_text(json.dumps(settings, indent=2) + "\n")
    print("OK settings.json")

    mcp_files = [
        CLAUDE / "plugins/marketplaces/thedotmack/claude-mem-cursor/mcp.json",
        CLAUDE / "plugins/marketplaces/thedotmack/claude-mem-grok-bot/mcp.json",
        CLAUDE / "plugins/marketplaces/thedotmack.bak/claude-mem-cursor/mcp.json",
        CLAUDE / "plugins/marketplaces/thedotmack.bak/claude-mem-grok-bot/mcp.json",
    ]
    for mp in mcp_files:
        if not mp.is_file():
            print(f"SKIP missing {mp}")
            continue
        data = json.loads(mp.read_text())
        servers = data.get("mcpServers", {})
        if "claude-mem-remote" in servers:
            del servers["claude-mem-remote"]
            data["mcpServers"] = servers
            mp.write_text(json.dumps(data, indent=2) + "\n")
            print(f"OK removed claude-mem-remote from {mp.parent.name}/{mp.name}")

    sh_path = CLAUDE / "skills/obsidian-second-brain/hooks/obsidian-bg-agent.sh"
    sh = sh_path.read_text()
    sh = sh.replace(
        "# Logs: /tmp/obsidian-bg-agent.log",
        "# Logs: ~/.claude/logs/obsidian-bg-agent.log (private dir)",
    )
    old_tail = (
        'PROMPT=$(cat "$PROMPT_FILE")\n'
        'rm -f "$PROMPT_FILE"\n\n'
        "# Run headless agent in vault directory - async, logs to /tmp for debugging\n"
        "(\n"
        '  cd "$VAULT" && \\\n'
        '  claude -p "$PROMPT" \\\n'
        "    --allowed-tools Read Write Edit Glob Grep \\\n"
        "    >> /tmp/obsidian-bg-agent.log 2>&1\n"
        ") &\n\n"
        "exit 0"
    )
    new_tail = (
        'LOG_DIR="${CLAUDE_CONFIG_DIR:-$HOME/.claude}/logs"\n'
        'LOG_FILE="$LOG_DIR/obsidian-bg-agent.log"\n'
        'mkdir -p "$LOG_DIR"\n'
        'chmod 700 "$LOG_DIR" 2>/dev/null || true\n\n'
        'PROMPT=$(cat "$PROMPT_FILE")\n'
        'trap \'rm -f "$PROMPT_FILE"\' EXIT\n\n'
        "# PostCompact hook is async in settings.json — no background & here\n"
        'cd "$VAULT" && \\\n'
        '  claude -p "$PROMPT" \\\n'
        "    --allowed-tools Read Write Edit Glob Grep \\\n"
        '    >> "$LOG_FILE" 2>&1\n\n'
        "exit 0"
    )
    if old_tail in sh:
        sh_path.write_text(sh.replace(old_tail, new_tail))
        print("OK obsidian-bg-agent.sh")
    else:
        print("WARN obsidian hook tail not matched")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
