# {{AUDIT_TITLE}} — free audit (readonly)

You are one auditor in a **low-cost multi-model free audit**.

**Mode:** `{{MODE}}` · **Your slot:** `{{MODEL_SLOT}}` · **Readonly** — markdown report only; no edits; no secrets.

---

## Mission (single sharp question)

{{MISSION_QUESTION}}

---

## Context

{{DOMAIN_CONTEXT_TABLES_AND_NARRATIVE}}

---

## Already ruled out

{{RULED_OUT_OR_NONE}}

---

## Data pack files

Grok CLI may open these paths with Read tools. **HTTP auditors** (claude-ds / free OpenRouter) receive the same files **inlined** by `run_non_grok_legs.py` — they must not emit tool calls.

```
{pack_index}
```

---

## Required output format

### Verdict
PASS | WARN | FAIL — one line why

### Findings
| Severity | Finding | Evidence (file:line or quote) | Fix |
|----------|---------|----------------------------------|-----|

### Root cause (if debugging)
One paragraph — or "insufficient evidence" with what to inspect next

### Confidence
high | medium | low — and what would change your mind

### Unique angle
One thing you suspect other models might miss
