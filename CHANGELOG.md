# Changelog

All notable changes to the **PMEGP Circular, GO & Proceedings Data Archive** are documented in this file.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) for the metadata schema version (`schemas/document_metadata_schema.json` → `_schema_info.version`).

---

## [Unreleased]

### Added — Data Acquisition Phase (2026-08-08)

#### Document Acquisitions (25 new documents, 7 → 32 entries)

**Tier 1 — Central MSME PMEGP Guidelines (8 documents):**
- `IN-MSME-2008-0001` — Original 2008 PMEGP Guidelines (KVI Policy Section, 24 pages).
- `IN-MSME-2014-0001` — O.M. PMEGP/Policy/3/2014 dated 20.09.2014 (interest on margin money plough-back). OCR'd.
- `IN-MSME-2015-0001` — O.M. PMEGP/Policy/3/2014 dated 06.05.2015 (negative list clarification, Khadi units permitted). OCR'd.
- `IN-MSME-2018-0002` — 2nd Loan Guidelines for PMEGP/MUDRA unit upgradation.
- `IN-MSME-2022-0001` — **🎯 May 13, 2022 O.M.** (PMEGP/Policy/09/2021) approving PMEGP continuation for 2021-22 to 2025-26 with Rs. 13,554.42 Crore outlay. Foundational Tier 1 document.
- `IN-MSME-2022-0002` — MSME Schemes Booklet 2022-23 (PMEGP is scheme #1).

**Tier 1 — Udyam Registration O.M.s (6 documents):**
- `IN-MSME-2020-0001` — **🎯 O.M. 5/2(1)/2020-P&G/Policy dated 17.07.2020** substituting UAM with Udyam Registration Certificate. Foundational Tier 1 priority #2 document.
- `IN-MSME-2020-0002` — RBI Circular RBI/2020-2021/10 (02.07.2020) on new MSME classification.
- `IN-MSME-2020-0003` — RBI Notification RBI/2020-2021/26 (21.08.2020) with MSME definition clarifications.
- `IN-MSME-2020-0004` — O.M. on NIC Codes not covered under MSMED Act for Udyam (01.12.2020).
- `IN-MSME-2020-0005` — O.M. 2/1(5)/2019-P&G/Policy (pt. IV) on EM/UAM transition (06.08.2020).
- `IN-MSME-2021-0001` — O.M. including retail/wholesale traders in MSME classification (02.07.2021).

**Tier 1 — KVIC PMEGP e-portal Circulars (8 documents):**
- `IN-KVIC-2022-0001` — PMEGP Scheme Guidelines (Certified Copy 2022-23) published by KVIC (43 pages, 145 PMEGP mentions).
- `IN-KVIC-2015-0001` — Circular adopting Udyog Aadhaar Memorandum for PMEGP unit registration (23.11.2015). OCR'd.
- `IN-KVIC-2019-0001` — EDP Training Circular (15.11.2019). OCR'd. Filed under `central-government/kvic/edp/`.
- `IN-KVIC-2019-0002` — Online EDP Training introduction (23.10.2019). OCR'd. Filed under `kvic/edp/`.
- `IN-KVIC-2019-0003` — Transgender special subsidy rate circular (19.12.2019). OCR'd.
- `IN-KVIC-2020-0001` — Simplification of PMEGP procedure during COVID-19 (06.05.2020). OCR'd.
- `IN-KVIC-2020-0002` — Diversification of products by REGP/PMEGP units (06.07.2020). OCR'd.
- `IN-KVIC-2022-0002` — Physical verification via geo-tagging (10.02.2022). OCR'd.

**Tier 2 — AP Budget Volume III-16 (Industries & Commerce Dept) (5 documents):**
- `AP-GOV-2022-0001` through `AP-GOV-2026-0002` — 5-year continuous series covering the entire 15th Finance Commission PMEGP cycle (2021-22 to 2025-26). Each volume allocates funds to Major Head 105 Khadi & Village Industries (KVIB) and MSME development programmes.

#### Documentation Enhancements
- **`docs/DISTRICT_PMEGP_PROGRESS_FY2024_25.md`** — New comprehensive reference document extracted from the AP Socio-Economic Survey 2024-25 (Annexure 6.4). Contains the complete 26-district PMEGP progress table (target/sanctioned/claimed/dischursed for each district), the tripartite KVIC/KVIB/DIC implementation model, priority district targets, per-district acquisition checklist, and key findings (Visakhapatnam underperformance, Anakapalli 65% disbursement gap, state-wide 53% disbursement gap).
- **`docs/MISSING_DOCUMENTS.md`** — Fully rewritten with the tripartite KVIC/KVIB/DIC targeting model. Reorganised into: National Level (MSME/KVIC/RBI), AP State Level (GOs/CoI/KVIB/KVIC State Office), SLBC AP, District-Level (Tier A/B/C with per-district checklists for Visakhapatnam and Anakapalli), Banks, and an RTI Filing Priority Queue. All previously-missing items that have now been acquired are marked as `- [x] ~~...~~ **ACQUIRED** as <document_id>`.

#### OCR Pipeline
- Implemented a 2-stage OCR pipeline (`scripts/pmegp_acquisition/ocr_scanned_docs.py`): pdftoppm (300 DPI) → tesseract 5.5.0 (eng+tel) → pdfunite. Downloaded `tel.traineddata` from tesseract-ocr/tessdata_fast GitHub and set up a user-controlled tessdata directory (no root needed).
- OCR'd 9 scanned PDFs total (2 MSME circulars + 7 KVIC circulars). Each has a `_ocr.pdf` companion alongside the original scan, and the corresponding `.evidence.json` file includes `ocr_processed`, `ocr_engine`, `ocr_languages`, `ocr_pipeline`, `ocr_quality`, `ocr_stats`, and `ocr_text_preview` fields.
- The OCR'd text revealed the actual O.M. numbers and dates for the two scanned MSME circulars, allowing metadata corrections: `IN-MSME-2014-0001` reference_no corrected to "O.M. No. PMEGP/Policy/3/2014" and date to 20.09.2014; `IN-MSME-2015-0001` reference_no corrected to "O.M. No. PMEGP/Policy/3/2014" and date to 06.05.2015.

#### Completeness Progress
- **Starting point:** 7 documents, 0.26% completeness.
- **Ending point:** 32 documents, 1.20% completeness.
- **Tier 1 status:** All three Tier 1 priorities from the acquisition roadmap are now COMPLETE (Revised 2022 Guidelines, Udyam Registration O.M.s, KVIC National Circulars — though state-wise target allocation matrices still pending RTI).

---

## [Unreleased] — Framework Freeze (2026-08-08)

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
