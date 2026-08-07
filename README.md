# PMEGP Circular, GO & Proceedings Data Archive

## Overview

This repository is a **highly structured, curated, and searchable digital archive** of all official documents related to the **Prime Minister's Employment Generation Programme (PMEGP)** in **Andhra Pradesh**, India.

PMEGP is a flagship credit-linked subsidy scheme launched by the Government of India, implemented through the **Ministry of MSME**, **KVIC (Khadi and Village Industries Commission)**, State **KVIBs (Khadi and Village Industries Boards)**, and **District Industries Centres (DICs)**. Since local decisions, fund releases, subsidy rates, and procedural updates are issued by multiple independent entities, this archive compiles, standardizes, and makes these critical documents fully accessible.

This project goes beyond a simple PDF storage dump by compiling a unified database of document metadata, enabling direct searches, programmatic audits, and structured research.

---

## 1. Repository Structure

The repository is structured hierarchically to match official federal and state administrative channels:

```
PMEGP-CIRCULAR-AND-GOS-AND-PROCEEDINGS-DATA/
├── README.md                          # This file
├── CHANGELOG.md                       # Chronological record of schema & curation changes
├── CONTRIBUTING.md                    # How to add documents and open PRs
├── LICENSE                            # MIT License for compilation
├── docs/                              # Detailed documentation guidelines
│   ├── collection_policy.md           # Permitted sources and privacy / PII rules
│   ├── collection_guide.md            # Practical step-by-step collection methodology
│   ├── document_classification.md     # Directory structure, Document ID scheme, district codes
│   ├── metadata_schema.md             # Production-frozen JSON & CSV metadata spec
│   ├── SOURCE_REGISTRY.md             # Index of every official source portal
│   ├── MISSING_DOCUMENTS.md           # Gap registry of known missing documents
│   └── ACQUISITION_DECISIONS.md        # Architecture & curation decision records (ADL)
├── schemas/                           # Machine-readable JSON Schema definitions
│   ├── document_metadata_schema.json  # Canonical metadata schema (v2.0.0)
│   └── document_metadata_example.json # Real-world example entry
├── central-government/                # Central / National-level guidelines
│   ├── msme/                          # Ministry of MSME guidelines, circulars, notifications
│   └── kvic/                          # KVIC Head Office circulars, advisories, EDP training norms
├── andhra-pradesh/                    # Andhra Pradesh State-level policy files
│   ├── government-orders/             # AP Government Orders (G.O.Ms / G.O.Rt)
│   ├── circulars/                     # Chief Secretariat circulars & memos
│   ├── commissioner-of-industries/    # Commissioner of Industries proceedings & instructions
│   └── kvic-state-office/             # AP KVIC State Office letters & meeting minutes
├── slbc/                              # State Level Bankers' Committee records
│   ├── agendas/                       # Meeting agenda notes
│   ├── minutes/                       # Official committee meeting minutes
│   └── reports/                       # Credit performance and subsidy disbursal reports
├── districts/                         # District-specific records for all 26 AP Districts
│   ├── anakapalli/                    # (e.g. Anakapalli District)
│   │   ├── collector/                 # District Collector proceedings
│   │   ├── dic/                       # District Industries Centre files
│   │   ├── dlcc/                      # District Level Consultative Committee minutes
│   │   ├── dlrc/                      # District Level Review Committee reports
│   │   └── lead-bank/                 # District Lead Bank directives
│   ├── visakhapatnam/                 # Visakhapatnam District records
│   └── ...                            # (Subdirectories for all 26 AP districts)
├── banks/                             # Standard lending terms and commercial banks directives
├── metadata/                          # Complete search indices
│   ├── documents.json                 # Searchable Master JSON database
│   ├── documents.csv                  # Master Spreadsheet database for Excel/Pandas
│   └── collection_status.json         # Per-category expected/collected counts
├── scripts/                           # Python administration scripts
│   ├── download/                      # Document scrapers and crawlers (planned)
│   ├── validate/                      # Schema validators and integrity checkers
│   ├── metadata/                      # Interactive metadata generation CLI tool
│   └── setup_repository.py            # One-shot scaffolder for the full directory tree
├── .github/                           # GitHub Issue & PR templates
└── index/                             # Local query indexes and cache files
```

---

## 2. Document Collection Status

The status table below is automatically compiled and updated from the master database by running `python3 scripts/validate/update_readme.py`:

<!-- STATUS_TABLE_START -->

### Archive Collection Completeness
**Completeness Score: `0.38%`** *(Progress is measured against verified totals where confirmed, or planning estimates by default)*
```text
[░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 10 / 2665 documents collected
```

#### Completeness Breakdown by Official Source

| Authority / Source | Expected (Planning) | Verified Total | Collected | Status | Progress |
|---|---|---|---|---|---|
| Central MSME Guidelines | 15 | Pending Audit | 2 | 🟡 In Progress | `[█░░░░░░░░░]` (13.3%) |
| Central MSME Circulars | 50 | Pending Audit | 0 | ⏳ Pending | `[░░░░░░░░░░]` (0.0%) |
| Central MSME Notifications | 40 | Pending Audit | 1 | 🟡 In Progress | `[░░░░░░░░░░]` (2.5%) |
| Central KVIC Circulars | 110 | Pending Audit | 0 | ⏳ Pending | `[░░░░░░░░░░]` (0.0%) |
| Central KVIC Advisories | 30 | Pending Audit | 0 | ⏳ Pending | `[░░░░░░░░░░]` (0.0%) |
| Central KVIC EDP Guidelines | 25 | Pending Audit | 0 | ⏳ Pending | `[░░░░░░░░░░]` (0.0%) |
| Central KVIC Portal Advisories | 20 | Pending Audit | 0 | ⏳ Pending | `[░░░░░░░░░░]` (0.0%) |
| AP Government Orders (GOs) | 120 | Pending Audit | 4 | 🟡 In Progress | `[░░░░░░░░░░]` (3.3%) |
| AP State Circulars & Memos | 80 | Pending Audit | 1 | 🟡 In Progress | `[░░░░░░░░░░]` (1.2%) |
| AP Commissioner Proceedings | 450 | Pending Audit | 0 | ⏳ Pending | `[░░░░░░░░░░]` (0.0%) |
| AP Commissioner Circulars | 150 | Pending Audit | 0 | ⏳ Pending | `[░░░░░░░░░░]` (0.0%) |
| AP Commissioner Instructions | 100 | Pending Audit | 1 | 🟡 In Progress | `[░░░░░░░░░░]` (1.0%) |
| AP KVIC State Circulars | 95 | Pending Audit | 0 | ⏳ Pending | `[░░░░░░░░░░]` (0.0%) |
| AP KVIC State Letters | 180 | Pending Audit | 0 | ⏳ Pending | `[░░░░░░░░░░]` (0.0%) |
| AP KVIC Review Agendas/Minutes | 60 | Pending Audit | 0 | ⏳ Pending | `[░░░░░░░░░░]` (0.0%) |
| SLBC Meeting Agendas | 40 | Pending Audit | 0 | ⏳ Pending | `[░░░░░░░░░░]` (0.0%) |
| SLBC Meeting Minutes | 40 | Pending Audit | 0 | ⏳ Pending | `[░░░░░░░░░░]` (0.0%) |
| SLBC Monitoring Reports | 50 | Pending Audit | 1 | 🟡 In Progress | `[░░░░░░░░░░]` (2.0%) |
| District Collector Proceedings | 130 | Pending Audit | 0 | ⏳ Pending | `[░░░░░░░░░░]` (0.0%) |
| District DIC Proceedings | 260 | Pending Audit | 0 | ⏳ Pending | `[░░░░░░░░░░]` (0.0%) |
| District DLCC Meeting Minutes | 260 | Pending Audit | 0 | ⏳ Pending | `[░░░░░░░░░░]` (0.0%) |
| District DLRC Meeting Reports | 130 | Pending Audit | 0 | ⏳ Pending | `[░░░░░░░░░░]` (0.0%) |
| District Lead Bank Guidelines | 130 | Pending Audit | 0 | ⏳ Pending | `[░░░░░░░░░░]` (0.0%) |
| Commercial Banks Circulars | 100 | Pending Audit | 0 | ⏳ Pending | `[░░░░░░░░░░]` (0.0%) |
| **TOTAL ARCHIVE** | **2665** | **Audit Underway** | **10** | **🟡 Curation Phase** | `[░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]` (0.38%) |

<!-- STATUS_TABLE_END -->

---

## 3. Document Metadata Schema

Every document in this archive includes corresponding master metadata properties. The fields are defined as follows:

| Field | Description / Format |
|---|---|
| **Document ID** | Unique string (e.g. `AP_ANA-DIC-2024-0001` or `AP-COI-2024-0012`) |
| **Title** | Full official title as it appears on the cover page |
| **Type** | Document type (e.g. `GO`, `Circular`, `Proceeding`, `Guidelines`, `Minutes`) |
| **Issuing Authority** | Name of the issuing agency (e.g., `Commissioner of Industries`) |
| **Department** | Administrative division (e.g., `Industries`, `Finance`, `Lead Bank`) |
| **State** | `Andhra Pradesh`, `Central` or `National` |
| **District** | Name of district if specific (or `null` if State/National level) |
| **Date** | Official date issued in `YYYY-MM-DD` format |
| **Reference No** | Reference/File number (e.g., `Rc.No. 12/PMEGP/2024`) |
| **Subject** | One-sentence summary of content |
| **Keywords** | Comma-separated search keywords |
| **Source URL** | Direct URL to original download site (or `null` if collected offline/RTI) |
| **Status** | Implementation status (`Active`, `Superseded`, `Obsolete`) |
| **File Path** | Relative path to document PDF in this repository |

---

## 4. Key Scripts & Automation

We maintain a set of administrative automation scripts under the `scripts/` folder:

### A. Run Integrity Checker
To validate the metadata schema, ensure sync between CSV and JSON, and verify that no files are missing or orphaned:
```bash
python3 scripts/validate/validate_metadata.py
```

### B. Add a New Document Interactively
To easily register a document, copy it to the correct hierarchical subfolder, assign a unique sequential ID, and update both JSON and CSV files automatically:
```bash
python3 scripts/metadata/generate_metadata.py
```

### C. Update README Status Stats
To compile counts from the database and refresh the status table above:
```bash
python3 scripts/validate/update_readme.py
```

---

## 5. Collection Rules

1. **Official Channels Only:** Only include documents sourced from official government portals (e.g., KVIC, Ministry of MSME, AP Industries, SLBC AP, or District administrations). Secondary sources must be explicitly declared as such in the metadata notes.
2. **Redact Personally Identifiable Information (PII):** Beneficiary name lists must be checked. Block out Aadhaar cards, bank details, and personal phone numbers before committing files.
3. **Naming Consistency:** Keep files named exactly matching their Document ID, e.g., `AP-COI-2024-0012.pdf`.

---

## 6. Documentation Index

| Document | Purpose |
|---|---|
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to add documents, the standard contribution workflow, and PR guidelines. |
| [CHANGELOG.md](CHANGELOG.md) | Chronological record of schema versions, structural changes, and document acquisitions. |
| [docs/collection_policy.md](docs/collection_policy.md) | Scope of collection, permitted sources, and the PII redaction protocol. |
| [docs/collection_guide.md](docs/collection_guide.md) | Practical step-by-step methodology for collecting documents (web, RTI, physical). |
| [docs/document_classification.md](docs/document_classification.md) | Directory structure mapping, Document ID scheme, and the 26 AP district slugs/codes. |
| [docs/metadata_schema.md](docs/metadata_schema.md) | Production-frozen metadata spec: status taxonomy, provenance, relationships, quality scores. |
| [docs/SOURCE_REGISTRY.md](docs/SOURCE_REGISTRY.md) | Registry of every official source portal (Central, AP State, 26 district portals). |
| [docs/MISSING_DOCUMENTS.md](docs/MISSING_DOCUMENTS.md) | Gap registry of known missing documents and target collection dates. |
| [docs/ACQUISITION_DECISIONS.md](docs/ACQUISITION_DECISIONS.md) | Architecture & Curation Decision Records (AD-0001 onwards). |
| [schemas/document_metadata_schema.json](schemas/document_metadata_schema.json) | Machine-readable JSON Schema (v2.0.0) — enforced by the validator. |
| [schemas/document_metadata_example.json](schemas/document_metadata_example.json) | Real-world example entry pulled from the archive. |

---

## 7. License

This curated archive database structure, search indexing files, and administrative scripts are licensed under the [MIT License](LICENSE). Individual government documents are subject to administrative public domain copyright standards of India.
