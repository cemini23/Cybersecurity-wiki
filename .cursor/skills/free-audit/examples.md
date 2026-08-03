# Free audit — examples

## Example A — code-debug (default)

**User:** `/free-audit why does setup_cursor_github_mcp.sh fail on missing token?`

**Cursor does:**

1. Mode `code-debug`
2. Tailors prompt + artifacts (script + error log)
3. `prepare_free_audit.py` → handoff
4. `handoff-to-grok.ps1 -PromptFile …/GROK_HANDOFF.md`
5. Pastes: `reports/audit/free-github-mcp/SYNTHESIS.md`

**Grok does:** auditor-grok.md → `run_non_grok_legs.py` → SYNTHESIS.md

## Example B — quick-triage

**User:** `free audit quick on .cursor/mcp.json`

Narrow pack (mcp.json only). Free OR still ≥2 distinct families. Synthesis top-3 findings only.

## Example C — brief-plan

**User:** `/free-audit mode: brief-plan is this Phase-0 ADOPT brief shippable?`

Pack includes brief path. No secrets. Overall SHIP/REWORK/REJECT in SYNTHESIS.md; Cursor only pastes the path.
