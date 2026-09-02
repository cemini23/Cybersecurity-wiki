---
name: firmware-rehost-lab-precheck
description: >-
  K322 advisory checklist before authorized embedded firmware rehosting / peripheral
  modeling lab work. Use when operator says firmware rehost / peripheral fidelity /
  K322 precheck / IoT dynamic analysis lab. Owned hardware only.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# Firmware rehost lab — K322 advisory checklist

Canon: `@wiki/concepts/firmware-rehosting-peripheral-fidelity.md` (arXiv **2608.29737**). Helper: `scripts/k322_firmware_rehost_precheck.py`. **Authorized owned-hardware lab only.**

## Procedure

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k322_firmware_rehost_precheck.py checklist
python3 scripts/k322_firmware_rehost_precheck.py selftest
```

Document **rehost fidelity acceptance criteria** before analysis. Reactive peripheral modeling from firmware I/O. Pair `@wiki/concepts/secure-boot-vs-device-ownership.md`.

## NEVER

- No exploit payloads or PoCs in wiki or briefs.
- Do not equate emulator success with on-device behavior.
