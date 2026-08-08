# RTI Request Templates for PMEGP Document Acquisition

This directory contains **ready-to-file RTI (Right to Information) application templates** for acquiring PMEGP-related documents that are not available through online portals.

Per [`docs/ACQUISITION_DECISIONS.md`](../ACQUISITION_DECISIONS.md) AD-0002 and the geoblocking reality documented in [`docs/MISSING_DOCUMENTS.md`](../MISSING_DOCUMENTS.md) §7, the following portals are unreachable from online channels and require RTI filings:

- `slbcap.nic.in` (SLBC AP) — DNS does not resolve
- `industries.ap.gov.in` (AP Commissioner of Industries) — no Wayback snapshots
- `apkvib.org.in` (AP KVIB) — largely offline
- KVIC AP State Office — no online document repository
- District DIC / Collector / Lead Bank offices — offline-only

## How to Use These Templates

1. **Read the applicable template** below.
2. **Fill in the bracketed placeholders** (`[APPLICANT_NAME]`, `[DATE]`, etc.).
3. **File online** at <https://rtionline.gov.in> (preferred) or submit a physical copy to the PIO.
4. **Pay the RTI fee** — ₹10 for BPL applicants (with certificate), ₹50 otherwise. Online payment via UPI/net banking is supported on rtionline.gov.in.
5. **Track the application** — PIO must respond within 30 days (48 hours if life/liberty involved).
6. **First appeal** — if no response within 30 days, file a first appeal with the First Appellate Authority (FAA) within 30 days.
7. **Second appeal** — if the FAA also fails, approach the Central/State Information Commission.

## Templates

| # | File | Target PIO | Priority | Documents Requested |
|---|---|---|---|---|
| 1 | [`01_coI_ap_state_targets.md`](01_coI_ap_state_targets.md) | Commissioner of Industries, AP | **Priority 1** (Layer 1) | Annual target allocation proceedings (FY 2024-25, 2025-26, 2026-27), quarterly monitoring instructions, State Level Task Force minutes |
| 2 | [`02_slbc_ap_quarterly.md`](02_slbc_ap_quarterly.md) | SLBC AP Convenor Bank | **Priority 2** (Cross-layer banking) | Quarterly agenda books and minutes (last 8 quarters), district performance reviews for Visakhapatnam and Anakapalli |
| 3 | [`03_kvic_state_office.md`](03_kvic_state_office.md) | KVIC State Director, AP | **Priority 3** (Central-state bridge) | Review letters to banks on delayed MM releases, annual action plan, EDP training calendar, state-level target correspondence |
| 4 | [`04_district_collector.md`](04_district_collector.md) | District Collectors (Visakhapatnam & Anakapalli) | **Priority 4** (Layers 2 & 3) | DIC annual target allocations, DLCC/DLRC minutes, Lead Bank directives, Collector DLMC review logs |
| 5 | [`05_des_ap_dhbs.md`](05_des_ap_dhbs.md) | Directorate of Economics and Statistics, AP | **Priority 5** (Statistical channel) | District Handbooks for FY 2013-14 through 2024-25 for all 26 districts (especially Visakhapatnam and Anakapalli) |

## Legal Basis

- **Right to Information Act, 2005** — Section 6(1) allows any Indian citizen to request information from public authorities.
- **Section 7(1)** — PIO must respond within 30 days (48 hours if life/liberty involved).
- **Section 4(1)(b)** — Suo moto disclosure obligations; many of these documents should already be public but aren't.
- **Cost of copies** — ₹2 per page for A4/A3 (₹5 for larger), per RTI Rules 2012.

## Notes

- Always keep a printed copy of the filed RTI application and the receipt.
- PIOs sometimes reject requests citing "disproportionate diversion of resources" — appeal this; the bar is high.
- If documents contain beneficiary PII (Aadhaar, bank accounts), request **aggregated** versions or redacted copies per [`docs/collection_policy.md`](../collection_policy.md) §3.
- RTI responses are themselves valuable archival documents — once received, scan and register them in the archive under `IN-RTI-YYYY-NNNN` or `AP-RTI-YYYY-NNNN`.
