# PMEGP Circular, GO & Proceedings Data Archive

## Overview

This repository serves as a **structured, searchable archive** of all official documents related to the **Prime Minister's Employment Generation Programme (PMEGP)** in **Andhra Pradesh**, India.

PMEGP is a credit-linked subsidy scheme launched by the Government of India, implemented through **KVIC (Khadi and Village Industries Commission)**, **KVIB (State Khadi and Village Industries Boards)**, and **DICs (District Industries Centres)**. Operational decisions, fund allocations, eligibility clarifications, and procedural changes are communicated through various official documents — Government Orders (GOs), Circulars, Proceedings, and Letters — issued by different authorities at the state, district, and national level.

This archive aims to:
- **Consolidate** all PMEGP-related documents from disparate sources into one organized repository
- **Standardize** metadata for every document (source, date, subject, category, district)
- **Enable** searchability and analysis for researchers, applicants, and PMEGP Assistants
- **Preserve** documents that are frequently moved, renamed, or removed from government portals

## Repository Structure

```
①②③④⑤⑥⑦⑧⑨/
├── 01_ap_government_gos_and_circulars/    # AP State Government Orders & Circulars
├── 02_kvic_andhra_pradesh_letters/       # KVIC AP regional office letters & directives
├── 03_commissioner_of_industries_proceedings/ # Commissioner of Industries office proceedings
├── 04_district_dic_proceedings/           # District Industries Centre proceedings (all 26 districts)
├── 05_collector_proceedings/               # District Collector proceedings related to PMEGP
├── 06_slbc_dlcc_records/                  # SLBC/DLCC meeting records & banking guidelines
├── 07_miscellaneous/                       # Other relevant documents ( RBI, MoMSME, press notes )
├── data_raw/                               # Unprocessed raw downloads (PDFs, scans, HTML dumps)
├── data_processed/                         # OCR’d, cleaned, and structured versions
├── schemas/                               # JSON schema definitions for metadata
├── scripts/                               # Scrapers, OCR pipelines, metadata generators
├── docs/                                  # Collection guides, source documentation, methodology
├── CONTRIBUTING.md                        # How to contribute documents & metadata
└── README.md                              # This file
```

## Document Categories Explained

### 01 - AP Government GOs & Circulars

Government Orders (GOs) issued by the Andhra Pradesh state government departments (Industries, Finance, Rural Development) that directly or indirectly affect PMEGP implementation. These include policy amendments, subsidy rate changes, budget allocations, and administrative restructuring orders.

**Typical sources:** `ap.gov.in`, `industries.ap.gov.in`, AP Gazette

### 02 - KVIC Andhra Pradesh Letters

Official letters, directives, and communications from the KVIC regional/district offices in Andhra Pradesh. These often contain operational guidelines, target allocations, application processing instructions, and clarification on scheme norms.

**Typical sources:** KVIC regional office, RTI responses, physical records

### 03 - Commissioner of Industries Proceedings

Proceedings issued by the Commissioner/Director of Industries, Andhra Pradesh. These are mid-level administrative directives that translate state GOs into actionable instructions for DICs and field offices.

**Typical sources:** `industries.ap.gov.in`, Commissioner’s office

### 04 - District DIC Proceedings

Proceedings from all 26 District Industries Centres in Andhra Pradesh. DICs are the primary implementing agencies for PMEGP at the district level. Their proceedings contain district-specific targets, applicant scrutiny decisions, and training schedules.

**AP has 26 districts:** Anakapalli, Anantapur, Bapatla, Eluru, Guntur, Kakinada, Kurnool, Nandyal, NTR, Palnadu, Parvathipuram Manyam, Prakasam, SPSR Nellore, Sri Sathya Sai, Tirupati, Vishakapatnam, Vizianagaram, West Godavari, East Godavari, YSR Kadapa, Annamayya, Chittoor, Kuppam, Dr. B.R. Ambedkar Konaseema, Alluri Sitharama Raju, and Narasaraopet.

### 05 - Collector Proceedings

Proceedings issued by District Collectors that relate to PMEGP — typically district-level coordination meetings, land allotment for industrial estates, and monitoring committee decisions.

### 06 - SLBC/DLCC Records

State Level Bankers’ Committee (SLBC) and District Level Consultative Committee (DLCC) records that contain banking-related PMEGP guidelines, credit flow data, and subsidy disbursement instructions.

### 07 - Miscellaneous

Documents from other relevant authorities: RBI circulars on credit-linked subsidies, MoMSME notifications, press information bureau releases, NABARD guidelines, and court orders affecting PMEGP.

## Document Metadata Schema

Every document in this archive must include a corresponding JSON metadata file. See [`schemas/document_metadata_schema.json`](schemas/document_metadata_schema.json) for the full schema definition.

**Required fields for every document:**

| Field | Type | Description |
|-------|------|-------------|
| `document_id` | string | Unique identifier (format: `PMEGP-AP-YYYY-NNN`)|
| `title` | string | Full title of the document |
| `date_issued` | string | Date in `YYYY-MM-DD` format |
| `issuing_authority` | string | Name of the issuing body |
| `category` | string | One of the 7 category codes (01–07) |
| `sub_category` | string | Specific sub-type (GO, Circular, Letter, Proceeding, etc.) |
| `district` | string or null | Relevant district name, or `null` for state/national level |
| `subject_keywords` | array | Searchable keywords |
| `source_url` | string or null | Original URL where the document was found |
| `file_path` | string | Relative path to the document file in this repo |
| `language` | string | `en` (English), `te` (Telugu), or `bilingual` |
| `pages` | integer | Number of pages |
| `file_format` | string | `pdf`, `jpg`, `png`, or `html` |
| `ocr_status` | string | `original`, `ocr_done`, `needs_manual_review` |
| `notes` | string | Any additional notes or context |

## Data Collection Status

| Category | Status | Count | Last Updated |
|----------|--------|-------|-------------|
| 01 - AP Govt GOs & Circulars | ⏳ Pending | 0 | - |
| 02 - KVIC AP Letters | ⏳ Pending | 0 | - |
| 03 - Commissioner Proceedings | ⏳ Pending | 0 | - |
| 04 - District DIC Proceedings | ⏳ Pending | 0 | - |
| 05 - Collector Proceedings | ⏳ Pending | 0 | - |
| 06 - SLBC/DLCC Records | ⏳ Pending | 0 | - |
| 07 - Miscellaneous | ⏳ Pending | 0 | - |

## Important Notes

- **Copyright:** Government of India and Andhra Pradesh government documents are generally in the public domain. However, always verify before redistribution.
- **PII:** Some proceedings may contain personal information (applicant names, Aadhaar references). These must be redacted before uploading.
- **File sizes:** Prefer compressed/optimized PDFs. If a single PDF exceeds 10 MB, consider splitting or compressing.
- **Naming convention:** Use the `document_id` as the filename prefix, e.g., `PMEGP-AP-2024-001_subsidy_rate_revision.pdf`

## License

This archive is maintained for research and public information purposes. Individual documents retain their original government copyright status.

## Contact

For questions, corrections, or to contribute documents, please open an issue or refer to [CONTRIBUTING.md](CONTRIBUTING.md).
