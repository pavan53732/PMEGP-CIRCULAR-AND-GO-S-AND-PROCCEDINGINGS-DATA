# Pull Request

## Description

<!-- Brief description of what this PR does and why. Reference any related Issues with "Closes #NN" or "Ref #NN". -->

Closes #

## Type of Change

- [ ] **New document(s) added** — PDF + metadata entry registered via `generate_metadata.py`.
- [ ] **Metadata correction** — fixed a typo, broken URL, missing relationship, or upgraded a quality grade on an existing entry.
- [ ] **Schema / script change** — modified `schemas/`, `scripts/`, or the validator.
- [ ] **Documentation improvement** — updated `README.md`, `docs/`, `CONTRIBUTING.md`, or `CHANGELOG.md`.
- [ ] **New source** — added a portal to `docs/SOURCE_REGISTRY.md`.
- [ ] **Other**: <!-- specify -->

## Documents Added / Modified

<!-- If this PR adds or modifies document entries, list them here. One row per document. -->

| Document ID | Title | Source | Status |
|---|---|---|---|
| <!-- AP-COI-2024-0012 --> | <!-- Revised Margin Money Subsidy Rates --> | <!-- industries.ap.gov.in --> | <!-- New / Updated --> |

## PII Redaction

- [ ] I have opened every PDF in this PR and verified that no Aadhaar numbers, bank account numbers, IFSC codes, phone numbers, or personal addresses are exposed.
- [ ] PII was found and has been redacted prior to commit.
- [ ] No PII was present in any of the source documents.

<!-- If redactions were performed, briefly describe what was redacted and on which document. -->

## Quality Scores Justification

<!-- For each new document, justify any B or C grades. A-grade entries do not require justification. -->

- `quality_authenticity`: <!-- e.g. "B — unsigned but complete official publication on industries.ap.gov.in" -->
- `quality_document`: <!-- e.g. "A — digital-native PDF with selectable text" -->
- `quality_metadata`: <!-- e.g. "A — all fields populated, keywords enriched, relationships mapped" -->

## Validation

I have run the following commands locally and they all succeed:

```bash
python3 scripts/validate/validate_metadata.py
python3 scripts/validate/update_readme.py
```

- [ ] `validate_metadata.py` returns "Validation Succeeded".
- [ ] `update_readme.py` has run and the README status table reflects the new counts.
- [ ] No new warnings or errors were introduced.

<!-- Paste the final lines of the validator output here for the reviewer's convenience. -->

```
[✓] Validation Succeeded! Metadata database is healthy and synced.
```

## Notes for Reviewers

<!-- Anything the reviewer should pay special attention to: source substitutions per AD-0002, low-quality scans, disputed authenticity, etc. -->
