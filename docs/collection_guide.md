# PMEGP Data Collection Guide

## Purpose

This guide provides a **practical, step-by-step methodology** for collecting PMEGP-related documents from government sources in Andhra Pradesh. It is designed for contributors who want to help build this archive.

> **Note:** This guide assumes you have already read [`collection_policy.md`](collection_policy.md) (scope & privacy rules), [`document_classification.md`](document_classification.md) (folder & ID conventions), and [`metadata_schema.md`](metadata_schema.md) (the production metadata spec).

---

## 1. Collection Methods (by priority)

### Method 1: Web Scraping / Manual Download

**Best for:** Central MSME, AP Government Orders, AP Commissioner of Industries, SLBC AP reports.

**Steps:**
1. Identify the target website from [`SOURCE_REGISTRY.md`](SOURCE_REGISTRY.md).
2. Navigate to the GOs / Circulars / Proceedings section.
3. Search for `"PMEGP"`, `"Prime Minister's Employment Generation Programme"`, or `"Margin Money Subsidy"`.
4. Download the document and **copy the source URL** — you will need it for the `provenance.downloaded_from` field.
5. If the site has no search function, browse by year and department.

**Tools:**
- Manual browser download (recommended for small batches).
- `wget` / `curl` for direct PDF links (verify `Content-Type: application/pdf` in the response headers).
- Python + `requests` / `BeautifulSoup` for structured scraping (place scrapers under `scripts/download/`).

### Method 2: RTI (Right to Information) Requests

**Best for:** KVIC state-office letters, DIC proceedings, Collector proceedings.

**Steps:**
1. File RTI online via <https://rtionline.gov.in>.
2. Target the specific PIO (Public Information Officer):
   - KVIC Regional Office → KVIC PIO
   - DIC proceedings → District Industries Manager / Commissioner of Industries PIO
   - Collector proceedings → District Collector's office PIO
3. Draft the RTI query specifically (see template below).
4. Pay the RTI fee (₹10 for BPL, ₹50 otherwise).
5. Follow up if no response within 30 days.

**RTI Query Template for PMEGP Documents:**
```
To: [PIO Name and Designation]
    [Office Name and Address]

Subject: RTI Application under Section 6(1) of RTI Act, 2005

Sir/Madam,

I kindly request the following information related to PMEGP implementation:

1. Copies of all proceedings/letters/circulars issued by your office
   related to PMEGP during the period [start_date] to [end_date].

2. If the documents are too numerous, please provide a list of all
   such documents with their reference numbers, dates, and subjects.

3. Information on the total number of PMEGP applications received,
   sanctioned, and subsidy disbursed by your office during the above period.

[Applicant Details as per RTI format]
```

> When registering an RTI-sourced document with `generate_metadata.py`, leave `source_url` blank and set `source_authority_level` to `ARCHIVED`. Record the RTI application number in the `provenance.notes` field (free text — the script currently stores this in the relationships array, see AD-0002 in [`ACQUISITION_DECISIONS.md`](ACQUISITION_DECISIONS.md)).

### Method 3: Physical Collection

**Best for:** KVIC letters, DIC proceedings, Collector proceedings — when online/RTI routes fail.

**Steps:**
1. Visit the relevant office (DIC, KVIC, Collector).
2. Meet the clerk / section officer handling PMEGP files.
3. Request permission to photocopy or photograph specific proceedings.
4. Carry a formal request letter on letterhead (if representing an organization).
5. Take photographs using a document scanner app (CamScanner, Adobe Scan, vFlat).

### Method 4: DIC Forwarded Copies

**Best for:** KVIC letters that were forwarded to DICs as part of their regular correspondence. These can often be obtained from the DIC itself rather than the KVIC office.

---

## 2. Recommended Collection Order

Based on **effort vs. yield**, collect in this order:

| Priority | Source | Method | Effort | Folder |
|---|---|---|---|---|
| 1 | AP Government Orders | Web download | Low | `andhra-pradesh/government-orders/` |
| 2 | AP Socio-Economic Survey & Budget | Web download | Low | `andhra-pradesh/circulars/`, `andhra-pradesh/government-orders/` |
| 3 | Central MSME Guidelines & Notifications | Web download | Low | `central-government/msme/guidelines/`, `central-government/msme/notifications/` |
| 4 | AP Commissioner of Industries Proceedings | Web + RTI | Medium | `andhra-pradesh/commissioner-of-industries/proceedings/` |
| 5 | SLBC Agendas / Minutes / Reports | Web + RTI | Medium | `slbc/agendas/`, `slbc/minutes/`, `slbc/reports/` |
| 6 | District DIC / Collector / DLCC / DLRC | RTI + Physical | High | `districts/<slug>/<sub>/` |
| 7 | KVIC Letters (State Office) | RTI + Physical | High | `andhra-pradesh/kvic-state-office/letters/` |

---

## 3. Document Processing Workflow

After collecting a document, run the interactive metadata generator — it handles most of the workflow automatically:

```bash
python3 scripts/metadata/generate_metadata.py
```

The script will:

1. **Compute the SHA-256 hash** of the source PDF and detect duplicates against the existing database.
2. **Prompt for metadata fields** (title, type, issuing authority, date, reference number, subject, keywords, source URL, status, quality scores).
3. **Determine the target folder** automatically based on `state`, `type`, and `district`.
4. **Assign the next sequential Document ID** scoped to `(territory, agency, year)`.
5. **Copy and rename** the file to `<document_id>.pdf` in the correct folder.
6. **Append** the entry to `metadata/documents.json` and regenerate `metadata/documents.csv`.

### Manual post-registration steps:

1. **Check for PII** — open the PDF and verify no Aadhaar / bank account / phone numbers are exposed. If found, redact with a PDF editor (e.g. `pdf-redact-tools`, `Obsidian`, or Adobe Acrobat), recalculate the SHA-256, and re-register.
2. **Compress the PDF** if file size exceeds 5 MB:
   ```bash
   ghostscript -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
       -dNOPAUSE -dQUIET -dBATCH -sOutputFile=compressed.pdf input.pdf
   ```
3. **Add relationships** if the document supersedes / amends / references another document already in the archive. The generator prompts for this; you can also edit `metadata/documents.json` directly and add an entry to the `relationships` array.
4. **Refresh the README status table**:
   ```bash
   python3 scripts/validate/update_readme.py
   ```
5. **Run the validator** to confirm everything is healthy:
   ```bash
   python3 scripts/validate/validate_metadata.py
   ```

---

## 4. Quality Checklist

Before committing any document, verify:

- [ ] File is not corrupted (opens correctly in a PDF reader).
- [ ] All pages are captured (check page count against the source).
- [ ] Metadata entry exists in `metadata/documents.json` and conforms to [`schemas/document_metadata_schema.json`](../schemas/document_metadata_schema.json).
- [ ] `metadata/documents.csv` is regenerated and synced (the generator does this automatically).
- [ ] No PII is exposed (or has been redacted).
- [ ] File is under 10 MB.
- [ ] Document is relevant to PMEGP (not a general government document).
- [ ] `source_url` is recorded (or `null` if collected via RTI / physical).
- [ ] Filename matches the Document ID exactly (`<document_id>.pdf`).
- [ ] `python3 scripts/validate/validate_metadata.py` returns "Validation Succeeded".

---

## 5. OCR Processing (for scanned documents)

For scanned documents where text is not selectable:

1. Use **Tesseract OCR** with Telugu + English language support:
   ```bash
   tesseract input.pdf output -l eng+tel pdf
   ```
2. Save the OCR'd PDF **alongside** the original under the same Document ID — do not register it as a separate document. Instead, add an `ocr_status` note to `provenance.notes` (free text field on the JSON entry, or via the generator's interactive prompt).
3. If OCR quality is poor, set the `quality_document` grade to `C` and add a note describing the legibility issue.

**Installing Tesseract on Ubuntu/Debian:**
```bash
sudo apt-get install tesseract-ocr tesseract-ocr-eng tesseract-ocr-tel
```

---

## 6. Handling Dead / Geoblocked Source URLs

Per [AD-0002](ACQUISITION_DECISIONS.md) in the Acquisition Decision Log, outbound HTTP requests from server hosting ranges are frequently geoblocked by `.nic.in` or specific Indian state subnets. When the primary portal is unreachable:

1. **Try an official secondary mirror** — e.g. another state's SLBC portal that hosts the same central circular.
2. **Use the Wayback Machine** — fetch from <https://web.archive.org> and record the snapshot URL in `provenance.archive_url`.
3. **Set `source_authority_level` to `SECONDARY`** (or `MIRROR` if from a third-party platform), and document the substitution in `provenance.notes`.

Never strip the original `source_url` — it must always point to the canonical issuing portal, even if you fetched the bytes from elsewhere.
