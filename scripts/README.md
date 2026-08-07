# Scripts

This folder contains automation scripts for collecting, processing, validating, and managing PMEGP documents in the archive.

---

## 1. Implemented Scripts

These scripts are production-ready and used in the standard contribution workflow.

| Script | Purpose | Status |
|---|---|---|
| [`metadata/generate_metadata.py`](metadata/generate_metadata.py) | Interactive CLI that registers a new document: computes SHA-256, detects duplicates, prompts for metadata, assigns the next Document ID, copies the PDF to the correct folder, and updates both `documents.json` and `documents.csv`. | ✅ Implemented |
| [`validate/validate_metadata.py`](validate/validate_metadata.py) | Validates the metadata database against the production schema. Checks ID format, required fields, enum values, file existence, and duplicate SHA-256 hashes. Cross-references JSON and CSV for sync. | ✅ Implemented |
| [`validate/update_collection_status.py`](validate/update_collection_status.py) | Recomputes the `collected` counts in `metadata/collection_status.json` by scanning `documents.json` and mapping each `file_path` to its category key. | ✅ Implemented |
| [`validate/update_readme.py`](validate/update_readme.py) | Regenerates the status table inside `README.md` between the `<!-- STATUS_TABLE_START -->` / `<!-- STATUS_TABLE_END -->` anchors. Calls `update_collection_status.py` first. | ✅ Implemented |
| [`setup_repository.py`](setup_repository.py) | One-shot scaffolder that creates the full directory tree (central-government, andhra-pradesh, slbc, districts/&lt;slug&gt;/{collector,dic,dlcc,dlrc,lead-bank}, banks, etc.) and seeds each leaf with a `.gitkeep`. Run once when bootstrapping a fresh fork. | ✅ Implemented |

### Standard Contribution Workflow

```bash
# 1. Register a new document (interactive)
python3 scripts/metadata/generate_metadata.py

# 2. Validate the database
python3 scripts/validate/validate_metadata.py

# 3. Refresh the README status table
python3 scripts/validate/update_readme.py
```

---

## 2. Planned Scripts (Not Yet Implemented)

The following scripts are planned for future development. If you'd like to contribute one, please open an Issue first to discuss the design.

| Script | Purpose | Status |
|---|---|---|
| `download/scrape_ap_govt_gos.py` | Scrape Government Orders from the AP Industries Dept portal (`ap.gov.in`). Should respect `robots.txt` and rate limits. | ⏳ Planned |
| `download/scrape_momsme.py` | Scrape MoMSME PMEGP notifications from `msme.gov.in`. | ⏳ Planned |
| `download/scrape_slbc_ap.py` | Scrape SLBC AP agendas / minutes / reports from `slbcap.nic.in`. | ⏳ Planned |
| `validate/check_pii.py` | Regex-based PII detector — flags Aadhaar numbers, bank account numbers, IFSC codes, phone numbers, and email addresses inside committed PDFs. | ⏳ Planned |
| `validate/compress_pdfs.py` | Batch-compress PDFs that exceed the 10 MB limit using `ghostscript`. | ⏳ Planned |
| `validate/ocr_documents.py` | Batch OCR processing for scanned PDFs using Tesseract (`eng+tel`). Saves OCR'd copy alongside the original. | ⏳ Planned |

---

## 3. Usage Notes

- All Python scripts require **Python 3.8+**.
- The scripts use only the Python standard library (`os`, `json`, `csv`, `hashlib`, `re`, `shutil`, `datetime`) — no `pip install` is required for the implemented scripts.
- The planned scraper scripts will likely need `requests`, `beautifulsoup4`, and `pdfminer.six` — add them to a `requirements.txt` when implementing.
- **Never run scrapers aggressively** — respect rate limits, set a `User-Agent` identifying the archive, and add at least a 1-second delay between requests.
- **Always review scraped documents manually** before committing — automated downloads can fetch the wrong file, an outdated revision, or a document with PII.
- All scripts determine the repository root via `os.path.dirname(os.path.dirname(os.path.abspath(__file__)))` — they can be run from any working directory inside the repo.
