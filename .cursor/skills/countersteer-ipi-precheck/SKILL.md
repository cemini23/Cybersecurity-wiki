---
name: countersteer-ipi-precheck
description: >-
  K383 CounterSteer inference-time IPI steering checklist. White-box serving +
  span tags; causal and capability gates. Parameter manipulation stays open.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
federation_owner: cybersecurity-wiki
disable-model-invocation: true
---

# CounterSteer Precheck (K383)

From **Cybersecurity Wiki** WorkDir:

```bash
python3 scripts/k383_countersteer_ipi_precheck.py checklist
python3 scripts/k383_countersteer_ipi_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/countersteer-activation-steering-ipi-defense.md` (arXiv **2609.36570**).

Suppression beats detection for indirect prompt injection on white-box-served agents — but steering does
**not** remove **parameter manipulation**; add argument-provenance controls.

## NEVER

- No injection payloads, steering vectors, or fitted directions in wiki.
- Do not clone `github.com/markrussinovich/countersteer-satml27-artifact` (license not stated; ships attack drivers).
- No LIVE third-party eval without written scope.

## Related

- `@cybersecurity-wiki/concepts/piminer-agentic-prompt-injection-redteam.md`
- `@cybersecurity-wiki/concepts/prompt-injection-detector-calibration.md`
