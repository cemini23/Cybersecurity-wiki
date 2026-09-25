#!/usr/bin/env python3
"""Write federation precheck skills for K371/K373 (idempotent)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".cursor" / "skills"

SPECS = {
    "instrumental-monitor-evasion-precheck": (
        "K371 instrumental runtime monitor evasion eval checklist before authorized-lab runs. No evasion recipes in wiki.",
        "k371_instrumental_monitor_evasion_precheck.py",
        "instrumental-monitor-evasion-evaluation",
        "2609.30217",
        "Report **attempt vs success** separately; external step gates still required (K307/K314).",
        "No evasion recipes, monitor-bypass prompts, or PoCs in wiki.",
    ),
    "agent-trace-tampering-precheck": (
        "K373 agent execution trace tampering audit checklist. Plan out-of-band append-only logging. No tamper PoCs in wiki.",
        "k373_agent_trace_tampering_precheck.py",
        "agent-execution-trace-tampering-audit",
        "2609.30266",
        "Trajectory self-report is not verification (pairs K271/K278).",
        "No trace-deletion playbooks or tamper PoCs in wiki.",
    ),
}


def main() -> int:
    for name, (desc, script, canon, arxiv, body_note, never) in SPECS.items():
        d = SKILLS / name
        d.mkdir(parents=True, exist_ok=True)
        title = name.replace("-", " ").title()
        kid = "K371" if "371" in script else "K373"
        (d / "SKILL.md").write_text(
            f"""---
name: {name}
description: >-
  {desc}
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
disable-model-invocation: true
---

# {title} ({kid})

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/{script} checklist
python3 scripts/{script} selftest
```

Canon: `@cybersecurity-wiki/concepts/{canon}.md` (arXiv **{arxiv}**).

{body_note}

## NEVER

- {never}
- No LIVE third-party eval without written scope.
""",
            encoding="utf-8",
        )
        print("wrote", d / "SKILL.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
