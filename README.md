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
├── LICENSE                            # MIT License for compilation
├── docs/                              # Detailed documentation guidelines
│   ├── COLLECTION_POLICY.md           # Permitted sources and privacy guidelines
│   ├── DOCUMENT_CLASSIFICATION.md     # Directory structures and naming guidelines
│   └── METADATA_SCHEMA.md             # Detailed metadata JSON & CSV schemas
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
│   └── documents.csv                  # Master Spreadsheet database for Excel/Pandas
├── scripts/                           # Python administration scripts
│   ├── download/                      # Document scrapers and crawlers
│   ├── validate/                      # Schema validators and integrity checkers
│   └── metadata/                      # Interactive metadata generation CLI tools
└── index/                             # Local query indexes and cache files
```

---

## 2. Document Collection Status

The status table below is automatically compiled and updated from the master database by running `python3 scripts/validate/update_readme.py`:

<!-- STATUS_TABLE_START -->

| Section / Category | Folder Path | Count | Status |
|---|---|---|---|
| **Central Govt (MSME)** | `central-government/msme/` | 1 | 🟢 Active |
| **Central Govt (KVIC)** | `central-government/kvic/` | 0 | ⏳ Pending |
| **AP State Govt Orders** | `andhra-pradesh/government-orders/` | 1 | 🟢 Active |
| **AP Commissioner of Industries** | `andhra-pradesh/commissioner-of-industries/` | 0 | ⏳ Pending |
| **AP KVIC State Office** | `andhra-pradesh/kvic-state-office/` | 0 | ⏳ Pending |
| **SLBC AP Records** | `slbc/` | 0 | ⏳ Pending |
| **District Level (26 Districts)** | `districts/` | 0 | ⏳ Pending |
| **Banks Rules & Guidelines** | `banks/` | 0 | ⏳ Pending |
| **Total Curated Documents** | **-** | **2** | **🟢 Active Curation** |

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

## 6. License

This curated archive database structure, search indexing files, and administrative scripts are licensed under the [MIT License](LICENSE). Individual government documents are subject to administrative public domain copyright standards of India.
