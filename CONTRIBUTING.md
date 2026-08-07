# Contributing to PMEGP Data Archive

Thank you for your interest in building this archive. Every document you contribute helps make PMEGP more transparent and accessible.

---

## Quick Start

1. **Fork** this repository
2. **Clone** your fork locally
3. **Pick a category** (01–07) that you have access to documents for
4. **Follow the collection guide** in [`docs/collection_guide.md`](docs/collection_guide.md)
5. **Add documents + metadata** to the appropriate category folder
6. **Submit a Pull Request** with a clear description of what you've added

---

## What to Contribute

### Documents (highest priority)
- Government Orders, Circulars, Proceedings, Letters related to PMEGP in Andhra Pradesh
- Any district, state, or national-level document that directly references PMEGP

### Metadata corrections
- Fix errors in existing metadata files
- Add missing `related_document_ids` links
- Update `verification_status` after cross-checking with original sources

### New sources
- If you discover a new URL or access method for a government portal, update the relevant category README

---

## Document Upload Rules

### Mandatory for every document:

1. **One PDF per document** — do not merge multiple documents into one PDF
2. **One JSON metadata file per document** — following the schema in `schemas/document_metadata_schema.json`
3. **Unique document_id** — check existing IDs to avoid duplicates
4. **No PII** — redact all personal information before uploading
5. **File size under 10 MB** — compress if necessary
6. **Descriptive filename** — use the format `PMEGP-AP-YYYY-NNN_descriptive_slug.pdf`

### File naming examples:
```
✅ PMEGP-AP-2024-001_subsidy_rate_revision.pdf
✅ PMEGP-AP-2024-001_subsidy_rate_revision.metadata.json
✅ PMEGP-AP-2024-015_ANT_edp_training_schedule_q2.pdf

❌ go_42_2024.pdf (no document_id, not descriptive)
❌ PMEGP_document.pdf (not descriptive)
❌ scanned_page_1.jpg + scanned_page_2.jpg (should be a single PDF)
```

---

## Metadata Requirements

Every document MUST have a `.metadata.json` file with at minimum these fields:

```json
{
  "document_id": "PMEGP-AP-YYYY-NNN",
  "title": "Full title of the document",
  "date_issued": "YYYY-MM-DD",
  "issuing_authority": "Full name of issuing body",
  "category": "01",
  "sub_category": "GO",
  "district": null,
  "subject_keywords": ["keyword1", "keyword2"],
  "source_url": "https://...",
  "file_path": "01_ap_government_gos_and_circulars/PMEGP-AP-YYYY-NNN_title.pdf",
  "language": "en",
  "pages": 5,
  "file_format": "pdf",
  "ocr_status": "original"
}
```

See [`schemas/document_metadata_example.json`](schemas/document_metadata_example.json) for a complete example.

---

## Getting a Document ID

Document IDs follow the format `PMEGP-AP-YYYY-NNN`:
- **YYYY** = year the document was issued
- **NNN** = sequential number (001, 002, 003...)

### How to find the next available ID:
1. Search the repository for all existing `document_id` values
2. Find the highest NNN for the relevant year
3. Increment by 1

**Example:** If the existing IDs for 2024 go up to `PMEGP-AP-2024-023`, your next document from 2024 gets `PMEGP-AP-2024-024`.

---

## Pull Request Guidelines

### PR Title Format:
```
[Category] Add N document(s) from [source/district]
```

Examples:
```
[01] Add 3 GOs from AP Industries Dept website
[04] Add 5 DIC proceedings from Anantapur district
[07] Add 2 MoMSME notifications on PMEGP guidelines
```

### PR Description must include:
1. List of documents added (title + document_id for each)
2. Source of the documents (URL or collection method)
3. Any PII redactions performed
4. Any issues or notes (e.g., "Page 3 of document 045 is partially illegible")

---

## Code of Conduct

- **Accuracy over speed** — a verified document is worth more than ten unverified ones
- **Respect privacy** — never upload documents containing unredacted personal information
- **Cite sources** — always record where you obtained each document
- **Be descriptive** — thorough metadata helps everyone find what they need
- **Ask questions** — if you're unsure whether a document belongs here, open an issue first

---

## Questions?

Open a GitHub Issue with the tag `question` and someone from the maintainers will respond.
