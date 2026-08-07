# Contributing to the PMEGP Data Archive

Thank you for your interest in building this archive. Every document you contribute helps make the Prime Minister's Employment Generation Programme (PMEGP) more transparent, auditable, and accessible to researchers, journalists, and administrators across Andhra Pradesh.

---

## 1. Quick Start

1. **Fork** this repository and clone your fork locally.
2. **Read** [`docs/collection_policy.md`](docs/collection_policy.md) to confirm your document is in scope, and [`docs/document_classification.md`](docs/document_classification.md) to learn the naming conventions.
3. **Pick a source** from [`docs/SOURCE_REGISTRY.md`](docs/SOURCE_REGISTRY.md) — start with high-priority portals (Ministry of MSME, KVIC, AP Industries, SLBC AP).
4. **Collect** the document using one of the methods described in [`docs/collection_guide.md`](docs/collection_guide.md).
5. **Register** the document using the interactive CLI:
   ```bash
   python3 scripts/metadata/generate_metadata.py
   ```
   This will compute the SHA-256 hash, detect duplicates, assign the next sequential Document ID, copy the file to the correct folder, and update both `metadata/documents.json` and `metadata/documents.csv`.
6. **Validate** the integrity of the database:
   ```bash
   python3 scripts/validate/validate_metadata.py
   ```
7. **Refresh** the README status table:
   ```bash
   python3 scripts/validate/update_readme.py
   ```
8. **Commit** with a descriptive message (see §5 below) and open a Pull Request against `main`.

---

## 2. What to Contribute

### Documents (highest priority)
- Government Orders, Circulars, Proceedings, Letters, Notifications, and Reports related to PMEGP in **Andhra Pradesh** or issued by the **Central Government** for AP implementation.
- Any district, state, or national-level document that **directly references** PMEGP, margin money subsidy, KVIC targets, DIC proceedings, or SLBC reviews.

### Metadata corrections
- Fix errors in existing metadata entries (typos in titles, wrong dates, broken source URLs).
- Add missing `relationships` links when you discover that one document supersedes, amends, or references another.
- Upgrade `quality_metadata` grades from `C` → `B` → `A` by enriching keywords and provenance fields.

### New sources
- If you discover a new official URL or access method for a government portal, add it to [`docs/SOURCE_REGISTRY.md`](docs/SOURCE_REGISTRY.md).

---

## 3. Document Upload Rules

### Mandatory for every document:

1. **One PDF per document** — do not merge multiple circulars/proceedings into a single PDF.
2. **One entry in `metadata/documents.json`** — every PDF must have a corresponding JSON record conforming to [`schemas/document_metadata_schema.json`](schemas/document_metadata_schema.json).
3. **Unique `document_id`** — the interactive generator (`generate_metadata.py`) handles this automatically; never reuse or guess an ID manually.
4. **No PII** — redact all Aadhaar numbers, bank account numbers, IFSC codes, phone numbers, and personal addresses before committing. See [`docs/collection_policy.md`](docs/collection_policy.md) §3 for the redaction protocol.
5. **File size under 10 MB** — compress with `ghostscript` if necessary.
6. **Filename matches the Document ID exactly** — see §4 below.

### Filename convention

The filename **must** be the Document ID followed by the `.pdf` extension. Do **not** append descriptive slugs, dates, or extra suffixes — the Document ID is the canonical key and any extra text breaks the validator's path check.

```
✅ AP-COI-2024-0012.pdf
✅ IN-MSME-2023-0001.pdf
✅ AP_ANA-DIC-2024-0002.pdf

❌ AP-COI-2024-0012_subsidy_revision.pdf        (extra slug — not allowed)
❌ pmegp_ap_coi_2024_0012.pdf                    (wrong case + underscores)
❌ AP-COI-2024-12.pdf                            (sequence must be 4 digits)
❌ AP-COI-24-0012.pdf                            (year must be 4 digits)
```

---

## 4. Document ID Scheme

The Document ID is the unique primary key across the entire archive. It is structured as:

```
[TERRITORY]-[AGENCY_CODE]-[YEAR]-[SEQUENCE]
```

| Element | Description | Examples |
|---|---|---|
| **Territory** | `IN` for Central / National, `AP` for Andhra Pradesh state level, `AP_<DIST>` for district level (e.g. `AP_ANA` for Anakapalli) | `IN`, `AP`, `AP_ANA`, `AP_VSP` |
| **Agency Code** | The issuing agency — see [`docs/document_classification.md`](docs/document_classification.md) §3 for the full list | `MSME`, `KVIC`, `GOV`, `COI`, `SLBC`, `COLL`, `DIC`, `DLCC`, `DLRC`, `LBO`, `BNK` |
| **Year** | 4-digit year of issue | `2024`, `2025` |
| **Sequence** | 4-digit sequential integer starting at `0001`, scoped per `(territory, agency, year)` | `0001`, `0042`, `0153` |

**Examples:**
- `IN-MSME-2023-0001` — 1st document from Central Ministry of MSME in 2023.
- `AP-COI-2024-0012` — 12th document from AP Commissioner of Industries in 2024.
- `AP_ANA-DIC-2024-0002` — 2nd document from Anakapalli District DIC in 2024.

The interactive generator (`scripts/metadata/generate_metadata.py`) determines the next sequence automatically by scanning existing IDs in the database. You should never compute or assign an ID manually.

---

## 5. Folder Placement

Files are organized by issuing authority. The generator (`generate_metadata.py`) determines the target folder automatically based on `state`, `type`, and `district` fields:

| Source | Folder Path |
|---|---|
| Central MSME Guidelines | `central-government/msme/guidelines/` |
| Central MSME Notifications | `central-government/msme/notifications/` |
| Central MSME Circulars | `central-government/msme/circulars/` |
| Central KVIC Circulars | `central-government/kvic/circulars/` |
| Central KVIC Advisories | `central-government/kvic/advisories/` |
| Central KVIC EDP Guidelines | `central-government/kvic/edp/` |
| Central KVIC Portal Advisories | `central-government/kvic/portal/` |
| AP Government Orders | `andhra-pradesh/government-orders/` |
| AP State Circulars & Memos | `andhra-pradesh/circulars/` |
| AP Commissioner Proceedings | `andhra-pradesh/commissioner-of-industries/proceedings/` |
| AP Commissioner Circulars | `andhra-pradesh/commissioner-of-industries/circulars/` |
| AP Commissioner Instructions | `andhra-pradesh/commissioner-of-industries/instructions/` |
| AP KVIC State Circulars | `andhra-pradesh/kvic-state-office/circulars/` |
| AP KVIC State Letters | `andhra-pradesh/kvic-state-office/letters/` |
| AP KVIC Review Meetings | `andhra-pradesh/kvic-state-office/review-meetings/` |
| SLBC Agendas / Minutes / Reports | `slbc/agendas/`, `slbc/minutes/`, `slbc/reports/` |
| District Collector / DIC / DLCC / DLRC / Lead Bank | `districts/<district-slug>/<sub-folder>/` |
| Commercial Banks Circulars | `banks/` |

The full district slug list (26 districts) is in [`docs/document_classification.md`](docs/document_classification.md) §4.

---

## 6. Metadata Requirements

Every document MUST have an entry in `metadata/documents.json` with the following minimum fields. The full schema is defined in [`schemas/document_metadata_schema.json`](schemas/document_metadata_schema.json) and the canonical spec is in [`docs/metadata_schema.md`](docs/metadata_schema.md).

```json
{
  "document_id": "AP-COI-2024-0012",
  "title": "Revised Margin Money Subsidy Rates under PMEGP for FY 2024-25",
  "type": "Proceeding",
  "issuing_authority": "Commissioner of Industries, Government of Andhra Pradesh",
  "department": "Industries",
  "state": "Andhra Pradesh",
  "district": null,
  "date": "2024-04-15",
  "reference_no": "Rc.No. 12/PMEGP/2024",
  "subject": "Revises margin money subsidy rates from 25% to 30% for general category in rural areas",
  "keywords": ["PMEGP", "Subsidy", "Margin Money", "Rate Revision", "FY 2024-25"],
  "source_url": "https://industries.ap.gov.in/proceedings/2024/pmegp-subsidy-revision",
  "status": "Active",
  "source_authority_level": "PRIMARY",
  "quality_authenticity": "A",
  "quality_document": "A",
  "quality_metadata": "A",
  "file_path": "andhra-pradesh/commissioner-of-industries/proceedings/AP-COI-2024-0012.pdf",
  "provenance": {
    "downloaded_from": "https://industries.ap.gov.in/proceedings/2024/pmegp-subsidy-revision",
    "download_date": "2026-08-08",
    "downloaded_by": "your-github-username",
    "sha256": "a7ff0868274fef902c67830fd442c34dec5488ee9547cb47352e87fe954e2f7a",
    "original_filename": "pmegp-subsidy-revision.pdf",
    "archive_url": null
  },
  "relationships": []
}
```

See [`schemas/document_metadata_example.json`](schemas/document_metadata_example.json) for a real-world example pulled from the archive.

---

## 7. Pull Request Guidelines

### PR Title Format

```
[<Category>] Add N document(s) from <source>
```

Where `<Category>` is one of: `Central-MSME`, `Central-KVIC`, `AP-GOV`, `AP-COI`, `AP-KVIC`, `SLBC`, `District-<Slug>`, `Banks`.

**Examples:**
```
[AP-GOV] Add 3 Government Orders from AP Finance portal
[Central-MSME] Add 2 PMEGP guideline notifications from Ministry of MSME
[District-Anantapur] Add 5 DIC proceedings from Anantapur DIC office
```

### PR Description must include:

1. **List of documents added** — title + Document ID for each.
2. **Source of the documents** — direct URL or collection method (RTI / physical visit).
3. **PII redactions performed** — confirm any redactions or state "No PII present".
4. **Quality scores assigned** — justify any `B` or `C` grades.
5. **Validation result** — paste the output of `python3 scripts/validate/validate_metadata.py` confirming "Validation Succeeded".
6. **Issues or notes** — e.g. "Page 3 of AP-COI-2024-0012 is partially illegible", or "Source URL returned 404, used Wayback Machine snapshot instead".

---

## 8. Code of Conduct

- **Accuracy over speed** — a verified document is worth more than ten unverified ones.
- **Respect privacy** — never upload documents containing unredacted PII.
- **Cite sources** — always record where you obtained each document; never strip the `provenance` block.
- **Be descriptive** — thorough metadata helps everyone find what they need.
- **Ask questions** — if you're unsure whether a document belongs here, open a GitHub Issue with the `question` label first.

---

## 9. Questions?

Open a GitHub Issue with the `question` label and a maintainer will respond. For deeper architectural discussions about the schema, source policy, or quality scoring rubric, please consult the documents under [`docs/`](docs/) first — most decisions are formally recorded in [`docs/ACQUISITION_DECISIONS.md`](docs/ACQUISITION_DECISIONS.md).
