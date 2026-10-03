---
name: wpa3-sae-dos-precheck
description: >-
  K392 WPA3-SAE availability (DoS) posture checklist. Measure AP-side cost under
  repeated failed attempts; do not shorten the slow path for speed.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
federation_owner: cybersecurity-wiki
disable-model-invocation: true
---

# WPA3-SAE DoS Precheck (K392)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k392_wpa3_sae_dos_precheck.py checklist
python3 scripts/k392_wpa3_sae_dos_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/wpa3-sae-dos-cost-asymmetry.md` (arXiv **2609.31519**).

SAE is expensive by design — that is both its strength and its availability weakness. Assess an AP by
**measuring per-authentication AP CPU cost under repeated failed attempts**, and report the client-side
cost with it. Shortening the slow path (PBKDF2 / Argon2 work, PE derivation) is a **security** change,
not a performance tweak: it is what preserves offline-dictionary resistance.

## NEVER

- Authorized wireless lab or owned AP only.
- No flood rates, tool commands, or DoS recipes in wiki.
- Treat stateless tickets as a new surface — require replay handling and revocation.
