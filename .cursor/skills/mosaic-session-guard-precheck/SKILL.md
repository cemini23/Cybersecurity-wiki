---
name: mosaic-session-guard-precheck
description: >-
  K400 multi-turn mosaic session-guard checklist. No fixed bounded window of
  recent turns is a defense. Require cross-turn state; no attack fragments.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
federation_owner: cybersecurity-wiki
disable-model-invocation: true
---

# Mosaic Session Guard Precheck (K400)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k400_mosaic_session_guard_precheck.py checklist
python3 scripts/k400_mosaic_session_guard_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/mosaic-attack-bounded-window-insufficiency.md` (arXiv **2610.05346**).

Before accepting a conversation guard as a defence: a **mosaic attack** splits harm across turns, each
fragment benign alone. The paper proves **no fixed bounded window of recent prompts is sufficient** —
the safety-relevant fragment can sit arbitrarily far back. Require an **online state mechanism** that
survives session boundaries.

## NEVER

- No attack fragments, prompt sequences, or payloads in wiki.
- Do not accept "we check the last N turns" as a defence.
- Do not treat self-play equilibrium as proof of usefulness.
