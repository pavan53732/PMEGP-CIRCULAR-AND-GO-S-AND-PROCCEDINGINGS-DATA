# RTI Application — Priority 1: Commissioner of Industries, AP

**Target PIO**: Public Information Officer, Office of the Commissioner of Industries, Government of Andhra Pradesh, Vijayawada.

**Priority**: 1 (Highest) — State-level tripartite allocation documents.

**Estimated Fee**: ₹50 (general) / ₹10 (BPL with certificate)

**Expected Response Time**: 30 days from filing

---

## Application Text

```
To: The Public Information Officer
    Office of the Commissioner of Industries
    Government of Andhra Pradesh
    Vijayawada, Andhra Pradesh

Subject: Application under Section 6(1) of the Right to Information Act, 2005

Sir/Madam,

I, [APPLICANT_NAME], citizen of India, hereby request the following
information under the Right to Information Act, 2005, related to the
implementation of the Prime Minister's Employment Generation Programme
(PMEGP) in Andhra Pradesh:

1. Certified copies of the annual target allocation proceedings issued by
   the Commissioner of Industries, AP, for the following financial years,
   showing the district-wise and category-wise (KVIC / KVIB / DIC)
   distribution of PMEGP physical and financial targets:
   (a) FY 2024-25
   (b) FY 2025-26
   (c) FY 2026-27 (if issued)

2. Certified copies of the quarterly monitoring instructions issued by
   the Commissioner of Industries, AP, to the General Managers of all
   26 District Industries Centres (DICs) during the period
   01 April 2024 to [DATE_OF_FILING], with specific reference to:
   (a) Physical verification of PMEGP-assisted units (including geo-tagging)
   (b) Margin money claim and disbursement tracking
   (c) EDP training compliance

3. Certified copies of the minutes of the State Level Task Force Committee
   meetings (chaired by the Principal Secretary, Industries / Commissioner
   of Industries) held during the period 01 April 2024 to [DATE_OF_FILING],
   in which private sector scheduled commercial banks were approved for
   PMEGP lending.

4. A list of all proceedings, circulars, and instructions issued by the
   Commissioner of Industries, AP, on PMEGP during the period
   01 April 2024 to [DATE_OF_FILING], with their reference numbers,
   dates, and subject lines.

I request that the information be provided in the form of certified
photocopies of the original documents. I am enclosing the prescribed RTI
fee of ₹50 (Rupees Fifty Only) via [PAYMENT_MODE: IPO / Demand Draft /
Online Payment Reference Number: XXXXXXXXXX].

If the requested information is exempt under Section 8 or 9 of the RTI Act,
please provide the specific exemption clause and the reasons for invoking it,
along with the details of the First Appellate Authority for filing an appeal.

[APPLICANT_NAME]
[APPLICANT_ADDRESS]
[APPLICANT_PHONE]
[APPLICANT_EMAIL]
[DATE_OF_FILING]

Place: [CITY]
```

---

## Filing Instructions

1. **Online filing** (preferred): Visit <https://rtionline.gov.in>
   - Select "Andhra Pradesh" as the State
   - Select "Commissioner of Industries" as the Public Authority
   - Paste the application text above
   - Pay ₹50 via UPI / net banking / credit card
   - Save the registration number

2. **Physical filing** (if online is unavailable):
   - Print the application
   - Attach a ₹50 Indian Postal Order (IPO) marked "Commissioner of Industries, AP"
   - Send via Speed Post / Registered Post to:
     ```
     The Public Information Officer
     Office of the Commissioner of Industries
     Government of Andhra Pradesh
     [ADDRESS_LINE_1]
     Vijayawada, Andhra Pradesh - [PINCODE]
     ```

3. **First Appeal** (if no response in 30 days):
   - File with the First Appellate Authority (FAA) at the same office
   - Use the first appeal template at <https://rtionline.gov.in>

---

## What to Do with the Response

When the PIO responds with the requested documents:

1. **Scan** all pages at 300 DPI to PDF.
2. **Check for PII** — redact any Aadhaar / bank account / phone numbers per [`docs/collection_policy.md`](../collection_policy.md) §3.
3. **Register** each received document in the archive via:
   ```bash
   python3 scripts/metadata/generate_metadata.py
   ```
4. **Tag** the document with `source_authority_level = ARCHIVED` and add the RTI application number in the `provenance.notes` field.
5. **Cross-reference** the received documents against the gaps in [`docs/MISSING_DOCUMENTS.md`](../MISSING_DOCUMENTS.md) and mark them as ACQUIRED.
6. **Commit and push** to the repository.

---

## Expected Documents

Based on the requested information, expect to receive:

| Document Type | Expected Count | Document ID Range |
|---|---|---|
| Annual target allocation proceedings | 3 (one per FY) | `AP-COI-2024-NNNN`, `AP-COI-2025-NNNN`, `AP-COI-2026-NNNN` |
| Quarterly monitoring instructions | ~8 (2 per FY x 2 years + 2 for FY 26-27) | `AP-COI-YYYY-NNNN` |
| State Level Task Force minutes | ~4-8 (quarterly) | `AP-COI-YYYY-NNNN` |
| Reference list of all PMEGP proceedings | 1 (the list itself) | Not registered (use as a discovery index) |

Total expected new documents: **~15-20 entries**.
