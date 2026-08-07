# Changelog

All notable changes to the **PMEGP Circular, GO & Proceedings Data Archive** are documented in this file.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) for the metadata schema version (`schemas/document_metadata_schema.json` → `_schema_info.version`).

---

## [Unreleased]

### Changed
- **`schemas/document_metadata_schema.json`** — bumped to **v2.0.0**. Replaced the legacy `PMEGP-AP-YYYY-NNN` ID pattern and the `category` / `sub_category` / `language` / `pages` / `file_format` / `ocr_status` / `verification_status` field set with the production field set (`document_id`, `type`, `issuing_authority`, `department`, `state`, `district`, `date`, `reference_no`, `subject`, `keywords`, `source_url`, `status`, `source_authority_level`, `quality_authenticity`, `quality_document`, `quality_metadata`, `file_path`, `provenance`, `relationships`). Added independent multi-dimensional quality scoring (A/B/C) and a tamper-evident provenance block with SHA-256 hashing. Marked `additionalProperties: false` so stale fields fail validation.
- **`schemas/document_metadata_example.json`** — replaced the synthetic placeholder example with a real entry pulled from `metadata/documents.json` (`IN-MSME-2023-0001`), so contributors have an accurate reference.
- **`CONTRIBUTING.md`** — fully rewritten. Removed references to the deleted `01_ap_government_gos_and_circulars`-style category folders and the legacy `PMEGP-AP-YYYY-NNN_descriptive_slug.pdf` filename pattern. Documented the canonical `[TERRITORY]-[AGENCY]-[YEAR]-[SEQUENCE]` Document ID scheme, the folder mapping from [`docs/document_classification.md`](docs/document_classification.md), the production metadata schema, and the standard contribution workflow (`generate_metadata.py` → `validate_metadata.py` → `update_readme.py`).
- **`docs/collection_guide.md`** — rewrote to align with the current folder structure and naming conventions. Updated the recommended collection order to reference real folder paths (`andhra-pradesh/government-orders/`, `slbc/reports/`, etc.) instead of the legacy `01_ap_government_gos_and_circulars` categories. Documented the interactive registration workflow and the manual post-registration steps (PII check, compression, relationships, README refresh, validation).
- **`scripts/README.md`** — restructured into "Implemented Scripts" (✅) and "Planned Scripts" (⏳) sections. Documented the four implemented scripts (`generate_metadata.py`, `validate_metadata.py`, `update_collection_status.py`, `update_readme.py`) plus `setup_repository.py`. Listed planned scrapers and utilities (`scrape_ap_govt_gos.py`, `check_pii.py`, `compress_pdfs.py`, `ocr_documents.py`) under a roadmap.

### Added
- **`scripts/download/`** — directory created with `.gitkeep` and a `README.md` describing scraper guidelines (robots.txt, User-Agent, rate limiting, caching, manual review) and the suggested Python stack (`requests`, `beautifulsoup4`, `pdfminer.six`).
- **`CHANGELOG.md`** — this file. Provides a chronological record of schema versions, structural changes, and document acquisitions for contributors and downstream consumers.
- **`.github/ISSUE_TEMPLATE/`** — added Issue templates for `bug_report`, `document_request`, and `new_source` to streamline community contributions.
- **`.github/PULL_REQUEST_TEMPLATE.md`** — added a PR template that mirrors the contribution checklist in [`CONTRIBUTING.md`](CONTRIBUTING.md) §7.

---

## [2026-08-07] — Initial Curation Phase

### Added
- Established the **Acquisition Decision Log** ([`docs/ACQUISITION_DECISIONS.md`](docs/ACQUISITION_DECISIONS.md)) with four formal records:
  - **AD-0001** — Jurisdictional scoping restricted to Central Government and Andhra Pradesh; Karnataka SLBC reports deleted.
  - **AD-0002** — Acceptance of official secondary mirrors when primary portals are geoblocked or offline.
  - **AD-0003** — Multi-dimensional quality scoring (Authenticity, Document, Metadata) replaces the single-metric scale.
  - **AD-0004** — Formal acquisition state workflow (`DISCOVERED → DOWNLOADED → VERIFIED → CURATED → REJECTED / REPLACED`).
- Ingested the first **7 curated documents** with `.evidence.json` provenance records:
  - `IN-MSME-2018-0001` — 2018 PMEGP Scheme Guidelines (superseded).
  - `IN-MSME-2023-0001` — 2023 PMEGP Scheme Guidelines (active, supersedes 2018).
  - `IN-MSME-2026-0001` — MoMSME Annual Report 2025-26 PMEGP targets.
  - `AP-GOV-2025-0001` — AP Socio Economic Survey 2024-25.
  - `AP-GOV-2026-0001` — AP Demands for Grants (Supplementary Estimates) 2025-26.
  - `AP-SLBC-2015-0001` — SLBC AP directory of certified private ITIs.
  - `AP-COI-2020-0001` — AP Industries Department technical cadre & DRDA coordination guidelines.
- Implemented the **metadata validation pipeline**:
  - `scripts/validate/validate_metadata.py` — schema validator with cross-reference checks and SHA-256 duplicate detection.
  - `scripts/validate/update_collection_status.py` — recomputes `collected` counts from `documents.json`.
  - `scripts/validate/update_readme.py` — regenerates the README status table between `<!-- STATUS_TABLE_START -->` / `<!-- STATUS_TABLE_END -->` anchors.
- Implemented `scripts/metadata/generate_metadata.py` — interactive CLI that registers a new document end-to-end (hash → duplicate check → metadata prompt → ID assignment → file copy → JSON/CSV update).
- Implemented `scripts/setup_repository.py` — one-shot scaffolder that creates the full directory tree (central-government, andhra-pradesh, slbc, districts/&lt;slug&gt;/{collector,dic,dlcc,dlrc,lead-bank}, banks, etc.) and seeds each leaf with a `.gitkeep`.
- Authored comprehensive documentation:
  - [`docs/metadata_schema.md`](docs/metadata_schema.md) — production-frozen metadata spec with status taxonomy, provenance, relationships, source authority classification, multi-dimensional quality scores, and acquisition states.
  - [`docs/document_classification.md`](docs/document_classification.md) — directory structure mapping, Document ID scheme, and the 26 AP district slug/code table.
  - [`docs/collection_policy.md`](docs/collection_policy.md) — scope of collection, permitted sources, PII redaction protocol, verification standards, and licensing.
  - [`docs/SOURCE_REGISTRY.md`](docs/SOURCE_REGISTRY.md) — registry of every official source portal (Central MSME, KVIC, AP Govt, AP Industries, SLBC AP, 26 district portals) with priority ratings.
  - [`docs/MISSING_DOCUMENTS.md`](docs/MISSING_DOCUMENTS.md) — gap registry of known missing documents and target collection dates.

### Removed
- Deleted the legacy `01_ap_government_gos_and_circulars` through `07_miscellaneous` category folders (along with `data_raw/` and `data_processed/`) per the restructuring in commit `3746029`.
- Deleted Karnataka SLBC reports per AD-0001 (jurisdictional scope enforcement).

---

## Schema Versioning Policy

The metadata schema version follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html):

- **MAJOR** — breaking changes to required fields, ID pattern, or enum values. Existing entries in `metadata/documents.json` will need migration.
- **MINOR** — additive changes (new optional fields, new enum values, new relationship types). Existing entries remain valid.
- **PATCH** — documentation-only changes, clarifications, and typo fixes.

The current production version is **v2.0.0** (recorded in `schemas/document_metadata_schema.json` → `_schema_info.version`). The validator (`scripts/validate/validate_metadata.py`) does not yet enforce a minimum schema version, but contributors should always reference the latest schema in `schemas/`.
