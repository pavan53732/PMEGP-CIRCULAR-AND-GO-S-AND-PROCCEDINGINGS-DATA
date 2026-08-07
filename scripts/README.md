# Scripts

This folder contains automation scripts for collecting, processing, and managing PMEGP documents.

## Planned Scripts

| Script | Purpose | Status |
|--------|---------|--------|
| `scrape_ap_govt_gos.py` | Scrape GOs from AP Industries Dept portal | ⏳ Planned |
| `scrape_momsme.py` | Scrape MoMSME PMEGP notifications | ⏳ Planned |
| `generate_metadata.py` | Generate metadata JSON template for a new document | ⏳ Planned |
| `validate_metadata.py` | Validate metadata files against the schema | ⏳ Planned |
| `ocr_documents.py` | Batch OCR processing for scanned PDFs | ⏳ Planned |
| `compress_pdfs.py` | Compress large PDFs to meet size limits | ⏳ Planned |
| `check_pii.py` | Basic PII detection in documents (regex-based) | ⏳ Planned |
| `update_readme_status.py` | Auto-update the status table in README.md | ⏳ Planned |

## Usage Notes

- All Python scripts require Python 3.8+
- Dependencies are listed in each script's header
- Never run scrapers aggressively — respect rate limits and server load
- Always review scraped documents manually before committing
