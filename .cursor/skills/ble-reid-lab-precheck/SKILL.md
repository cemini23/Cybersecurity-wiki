---
name: ble-reid-lab-precheck
description: >-
  K365 BLE MAC randomization re-identification lab checklist before owned-device wireless eval. Authorized lab only. No probe payloads in wiki.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
federation: true
disable-model-invocation: true
---

# PIR sandbagging precheck (K365)

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k365_ble_reid_lab_precheck.py checklist
python3 scripts/k365_ble_reid_lab_precheck.py selftest
```

Canon: `@cybersecurity-wiki/concepts/ble-mac-randomization-reidentification-lab.md` (arXiv **2609.26079**).

Owned devices only. Separate pairing from linkability; test service authorization (K305).

## NEVER

- No tracking recipes or fingerprint playbooks in wiki.
- No LIVE third-party model probing without written scope.
