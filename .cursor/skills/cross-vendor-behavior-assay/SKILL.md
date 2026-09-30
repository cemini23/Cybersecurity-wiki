---
name: cross-vendor-behavior-assay
description: >-
  K392 cross-vendor/release behavior assay gate. Validate frozen pins and cheap assay pass ratio before model comparisons.
  Use when operator says vendor assay / release behavior probe / cross-vendor eval.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# Cross-vendor behavior assay (K392)

Helper: `scripts/cross_vendor_behavior_assay.py`. Canon: `@wiki/concepts/low-cost-cross-vendor-behavior-assays.md`.

```bash
python3 scripts/cross_vendor_behavior_assay.py checklist
python3 scripts/cross_vendor_behavior_assay.py json --json config/cross_vendor_behavior_assay.example.json
python3 scripts/cross_vendor_behavior_assay.py selftest
```

## NEVER

- Not a substitute for full EnterpriseVal/K373 scale gate.
