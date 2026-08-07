# PMEGP Data Collection Guide

## Purpose

This guide provides a **practical, step-by-step methodology** for collecting PMEGP-related documents from government sources in Andhra Pradesh. It is designed for contributors who want to help build this archive.

---

## Collection Methods (by priority)

### Method 1: Web Scraping / Manual Download

**Best for:** Categories 01, 07 (AP Govt portal, MoMSME, RBI, PIB)

**Steps:**
1. Identify the target website (see category-specific READMEs for URLs)
2. Navigate to the GOs/Circulars/Proceedings section
3. Search for "PMEGP", "Prime Minister's Employment Generation Programme", "margin money subsidy"
4. Download the document and note the source URL
5. If the site has no search function, browse by year and department

**Tools:**
- Manual browser download (recommended for small batches)
- `wget` / `curl` for bulk downloads (if direct PDF links are available)
- Python + BeautifulSoup/Scrapy for structured scraping (see `scripts/` folder)

### Method 2: RTI (Right to Information) Requests

**Best for:** Categories 02, 04, 05 (KVIC letters, DIC proceedings, Collector proceedings)

**Steps:**
1. File RTI online via `https://rtionline.gov.in`
2. Target the specific PIO (Public Information Officer):
   - KVIC Regional Office → KVIC PIO
   - DIC proceedings → District Industries Manager / Commissioner of Industries PIO
   - Collector proceedings → District Collector's office PIO
3. Draft the RTI query specifically (see template below)
4. Pay the RTI fee (₹10 for BPL, ₹50 otherwise)
5. Follow up if no response within 30 days

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

### Method 3: Physical Collection

**Best for:** Categories 02, 04, 05 (when online/RTI routes fail)

**Steps:**
1. Visit the relevant office (DIC, KVIC, Collector)
2. Meet the clerk/section officer handling PMEGP files
3. Request permission to photocopy or photograph specific proceedings
4. Carry a formal request letter on letterhead (if representing an organization)
5. Take photographs using a document scanner app (CamScanner, Adobe Scan)

### Method 4: DIC Forwarded Copies

**Best for:** Category 02 (KVIC letters often forwarded to DICs)

Many KVIC communications are received by DICs as part of their regular correspondence. These can often be obtained from the DIC itself rather than the KVIC office.

---

## Recommended Collection Order

Based on **effort vs. yield**, collect in this order:

| Priority | Category | Method | Estimated Effort |
|----------|----------|--------|-----------------|
| 1 | 01 - AP Govt GOs | Web download | Low |
| 2 | 07 - Miscellaneous | Web download | Low |
| 3 | 03 - Commissioner Proceedings | Web + RTI | Medium |
| 4 | 06 - SLBC/DLCC | Web + RTI | Medium |
| 5 | 04 - DIC Proceedings | RTI + Physical | High |
| 6 | 02 - KVIC Letters | RTI + Physical | High |
| 7 | 05 - Collector Proceedings | RTI + Physical | High |

---

## Document Processing Workflow

### After collecting a document:

1. **Rename** the file to match the naming convention: `PMEGP-AP-YYYY-NNN_descriptive_slug.pdf`
2. **Determine the next document_id** by checking the highest existing ID and incrementing
3. **Create the metadata JSON file** following the schema in `schemas/document_metadata_schema.json`
4. **Place the document** in the correct category folder
5. **Check for PII** — redact any personal information (names, addresses, Aadhaar, bank account numbers)
6. **Optimize the PDF** — compress if file size exceeds 5 MB (use `ghostscript` or online tools)
7. **Update the status table** in the main README.md

---

## Quality Checklist

Before uploading any document, verify:

- [ ] File is not corrupted (opens correctly)
- [ ] All pages are captured (check page count against source)
- [ ] Metadata JSON is complete and follows the schema
- [ ] No PII is exposed (or has been redacted)
- [ ] File is under 10 MB
- [ ] Document is relevant to PMEGP (not a general government document)
- [ ] Source URL is recorded (if applicable)
- [ ] Language is correctly tagged (en/te/bilingual)

---

## OCR Processing

For scanned documents (non-selectable text):

1. Use **Tesseract OCR** with Telugu + English language support
2. Save the OCR output alongside the original: `PMEGP-AP-YYYY-NNN_descriptive_slug_ocr.pdf`
3. Set `ocr_status` to `"ocr_done"` in metadata
4. If OCR quality is poor, set `ocr_status` to `"needs_manual_review"`

**Tesseract command:**
```bash
tesseract input.pdf output -l eng+tel pdf
```
