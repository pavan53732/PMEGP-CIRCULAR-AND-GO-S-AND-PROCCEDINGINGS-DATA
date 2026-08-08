# PMEGP Administrative Hierarchy in Andhra Pradesh

This document codifies the **three-layer administrative hierarchy** through which every PMEGP directive flows in Andhra Pradesh. It is the definitive operational reference for understanding who issues what type of document, and how state-level G.O.s and KVIC guidelines get translated into local field action.

This hierarchy is the targeting model for all district-level and state-level document acquisition in this archive. Every missing document in [`docs/MISSING_DOCUMENTS.md`](MISSING_DOCUMENTS.md) is classified by which of these three layers issued it.

---

## 1. The Three Administrative Layers

PMEGP is never run in isolation. Every state G.O. and KVIC guideline has to be translated into local action. This translation happens through a strict hierarchy involving three key authorities:

### Layer 1: The State Commissioners (Mid-Level Bridge)

**Role**: The Commissioner acts as the mid-level bridge between the State Cabinet and the field. When the Government of AP issues a G.O. (like `AP-GOV-2024-0001` or `AP-GOV-2026-0001` in this archive), the Commissioner of Industries immediately translates it into a "Proceeding" or "Circular Instruction" directing all 26 DICs how to process applications and what social targets (SC/ST/Women) must be prioritised.

**Key Officials**:
- **Commissioner of Industries, AP** (Vijayawada) — the primary PMEGP commissioner
- **Principal Secretary, Industries & Commerce Dept** — the commissioner's reporting authority
- **Vice Chairman & CEO, Andhra Pradesh Industrial Infrastructure Corporation (APIIC)** — for PMEGP infrastructure
- **Director of Industries** — operational head under the Commissioner

**Key Document Types Issued**:
| Document Type | Typical Format | Frequency | Target Folder |
|---|---|---|---|
| Commissioner Proceedings | `Rc.No. XX/PMEGP/YYYY` dated DD.MM.YYYY | Quarterly + ad-hoc | `andhra-pradesh/commissioner-of-industries/proceedings/` |
| State-level Implementation Circulars | `Cir.Memo.No. XX/PMEGP/YYYY` | Monthly | `andhra-pradesh/commissioner-of-industries/circulars/` |
| Target Allocation Proceedings | `Rc.No. A2/PMEGP/Targets/YYYY` | Annual (April) | `andhra-pradesh/commissioner-of-industries/proceedings/` |
| Quarterly Monitoring Instructions | `Rc.No. B1/PMEGP/Monitoring/YYYY` | Quarterly | `andhra-pradesh/commissioner-of-industries/instructions/` |
| State Level Task Force Committee minutes | `STFC/PMEGP/YYYY` | Quarterly | `andhra-pradesh/commissioner-of-industries/proceedings/` |
| Review Meeting Minutes (with DIC GMs) | `Rc.No. C3/PMEGP/Review/YYYY` | Monthly | `andhra-pradesh/commissioner-of-industries/proceedings/` |

**Current Status in Archive**: 1 document acquired (`AP-COI-2020-0001`). **Highest-priority gap** — see RTI template [`01_coI_ap_state_targets.md`](rti_templates/01_coI_ap_state_targets.md).

---

### Layer 2: The District Collectors (Collectorate Memos & DLMC Orders)

**Role**: The District Collector is the **supreme administrative head of PMEGP at the local level**. By law, the Collector chairs two critical committees that govern PMEGP implementation in every district:

1. **The District Level Consultative Committee (DLCC)** — reviews banking disbursements
2. **The District Level Monitoring Committee (DLMC)** — meets quarterly to monitor unit physical verifications and track delayed margin money

The Collector's role is explicitly documented in the AP Outcome Budget 2020-21 (`AP-GOV-2020-0002`):
> *"Identification of beneficiaries will be made by the District Level Task Force Committee in all Districts constituted under the Chairman of the District Collector for extending the financial benefits under the Prime Ministers Employment Generation Programme (PMEGP). All applications identified by the committee will be sent to the concerned banks for sanction of loans under the Scheme."*

**Key Officials (per district)**:
- **District Collector** — Chairman of DLCC and DLMC
- **Joint Collector** — alternate chair in some districts
- **District Revenue Officer (DRO)** — supports the Collector in PMEGP coordination

**Key Document Types Issued (per district)**:
| Document Type | Typical Format | Frequency | Target Folder |
|---|---|---|---|
| Collectorate Proceedings (PMEGP) | `Rc.No. XX/PMEGP/YYYY` | Monthly | `districts/<slug>/collector/` |
| DLMC Review Memos | `DLMC/PMEGP/QX-YYYY` | Quarterly | `districts/<slug>/collector/` |
| DLCC Agenda & Minutes | `DLCC/PMEGP/QX-YYYY` | Quarterly | `districts/<slug>/dlcc/` |
| District Target Allocation Order | `Rc.No. XX/PMEGP/Targets/YYYY` | Annual | `districts/<slug>/collector/` |
| Beneficiary Identification List | `DLTC/Beneficiary/YYYY` | Rolling | `districts/<slug>/collector/` (with PII redaction) |
| Bank-wise Sponsoring Letter | `Rc.No. XX/Banks/YYYY` | Rolling | `districts/<slug>/collector/` |

**Current Status in Archive**: 0 documents acquired for any district. **Critical gap** for Visakhapatnam (SBI Lead Bank) and Anakapalli (Union Bank Lead Bank) — see RTI template [`04_district_collector.md`](rti_templates/04_district_collector.md).

---

### Layer 3: The Project Directors / General Managers (PDs of DRDA / GMs of DICs)

**Role**: The General Manager of the DIC and the Project Director (PD) of the District Rural Development Agency (DRDA) act as the **"Member-Conveners"** of the district committees. They do the heavy lifting:
- Validating applications
- Forwarding files directly to financing banks
- Managing local Entrepreneurship Development Programmes (EDP)
- Handling the geo-tagged unit verifications (per `IN-KVIC-2022-0002`)
- Coordinating with MEPMA (Mission for Elimination of Poverty in Municipal Areas) for urban beneficiaries

**Key Officials (per district)**:
- **General Manager, District Industries Centre (DIC)** — Member-Convener of DLCC/DLMC; primary PMEGP field officer
- **Project Director, District Rural Development Agency (DRDA)** — coordinates rural PMEGP mobilisation
- **District Coordinator, MEPMA** — coordinates urban PMEGP mobilisation
- **Lead Bank Manager** (SBI in Visakhapatnam, Union Bank in Anakapalli) — banking channel lead

**Key Document Types Issued (per district)**:
| Document Type | Typical Format | Frequency | Target Folder |
|---|---|---|---|
| DIC Sponsoring Letters (to banks) | `GM/PMEGP/Sponsor/YYYY/NNN` | Rolling | `districts/<slug>/dic/` |
| DIC Annual Target Allocation | `GM/PMEGP/Targets/YYYY` | Annual | `districts/<slug>/dic/` |
| DIC Physical Verification Reports | `GM/PMEGP/PV/YYYY/NNN` | Per-unit | `districts/<slug>/dic/` |
| DIC EDP Training Schedule | `GM/PMEGP/EDP/YYYY` | Quarterly | `districts/<slug>/dic/` |
| DRDA Joint Mobilization Circular | `PD/DRDA/PMEGP/YYYY` | Annual | `districts/<slug>/lead-bank/` or `districts/<slug>/dic/` |
| MEPMA Joint Mobilization Circular | `DC/MEPMA/PMEGP/YYYY` | Annual | `districts/<slug>/dic/` |
| PD Implementation Instructions | `PD/DRDA/PMEGP/Instr/YYYY` | Quarterly | `districts/<slug>/lead-bank/` |
| Lead Bank Credit Plan (with PMEGP sub-targets) | `LBP/CreditPlan/YYYY` | Annual | `districts/<slug>/lead-bank/` |
| Lead Bank Handholding / RSETI Setup | `LBP/RSETI/YYYY` | Annual | `districts/<slug>/lead-bank/` |

**Current Status in Archive**: 0 documents acquired for any district. **Largest volume gap** — these are the highest-volume document types in PMEGP administration.

---

## 2. Document Flow: From G.O. to Bank Disbursement

The following diagram shows how a single state-level G.O. flows through the three layers and ultimately results in a bank-level loan sanction and margin money disbursement:

```
┌─────────────────────────────────────────────────────────────────┐
│ STATE CABINET (Government of Andhra Pradesh)                    │
│   Issues: G.O.Ms No. XX/Industries/YYYY                         │
│   Example in archive: AP-GOV-2024-0001, AP-GOV-2026-0001        │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│ LAYER 1: COMMISSIONER OF INDUSTRIES, AP                         │
│   Issues: Commissioner Proceedings (Rc.No. XX/PMEGP/YYYY)       │
│   Action: Translates G.O. into target allocations for 26 DICs  │
│           Issues quarterly monitoring instructions              │
│   Example in archive: AP-COI-2020-0001                          │
│   Gap: Target Allocation Proceedings for FY 2024-25/2025-26/26 │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│ LAYER 2: DISTRICT COLLECTOR (per district)                      │
│   Issues: Collectorate Proceedings, DLMC Review Memos           │
│   Action: Chairs DLCC (banking review) and DLMC (monitoring)   │
│           Constitutes District Level Task Force Committee       │
│           Identifies beneficiaries (with PII redaction)         │
│   Gap: 0 documents acquired for any district                    │
└─────────────┬───────────────────────────────────┬───────────────┘
              │                                   │
              ▼                                   ▼
┌─────────────────────────────────┐  ┌─────────────────────────────┐
│ LAYER 3: GM of DIC              │  │ LAYER 3: PD of DRDA         │
│   (Member-Convener)             │  │   (Member-Convener)         │
│   Issues: DIC Sponsoring        │  │   Issues: Joint Mobilization│
│           Letters to banks      │  │           Circulars         │
│           Physical Verification │  │           (with MEPMA)      │
│           Reports (geo-tagged)  │  │                             │
│           EDP Training Schedule │  │   Urban mobilisation        │
│                                 │  │                             │
│   Gap: 0 documents acquired     │  │   Gap: 0 documents acquired │
└─────────────┬───────────────────┘  └─────────────┬───────────────┘
              │                                    │
              └─────────────┬──────────────────────┘
                            │
                            ▼
              ┌─────────────────────────────────┐
              │ FINANCING BANKS                 │
              │   (SBI in Vizag, Union Bank     │
              │    in Anakapalli)               │
              │   Action: Loan sanction         │
              │           Margin Money claim     │
              │           Margin Money disbursal│
              │                                 │
              │   Lead Bank: Annual Credit Plan │
              │   Gap: 0 documents acquired     │
              └─────────────────────────────────┘
```

---

## 3. Per-District Authority Matrix

### Focus District: Visakhapatnam

| Authority | Office | Documents Targeted |
|---|---|---|
| District Collector | Collectorate, Mahatma Gandhi Marg, Visakhapatnam - 530001 | DLMC memos, DLCC minutes, Collectorate proceedings |
| Joint Collector | Collectorate Complex, Vizag | Alternate chair for DLMC/DLCC |
| GM, DIC Visakhapatnam | Industrial Estate, Autonagar, Visakhapatnam - 530012 | Sponsoring letters, PV reports, EDP schedules |
| PD, DRDA Visakhapatnam | Collectorate Complex, Vizag | Joint mobilisation circulars, rural mobilisation |
| Lead Bank Manager (SBI) | SBI Main Branch, Vizag | Annual credit plan, PMEGP sub-targets, handholding |
| District Coordinator, MEPMA | Municipal Corporation, Vizag | Urban PMEGP mobilisation |

**Visakhapatnam PMEGP Activity (FY 2024-25)**:
- Target: 26 projects / ₹78.50 Lakh MM
- Sanctioned: 27 projects / ₹124.36 Lakh MM
- Claimed: 35 projects / ₹193.72 Lakh MM
- Disbursed: 14 projects / ₹80.70 Lakh MM
- **Anomaly**: Lowest project target of all 26 districts — investigate whether PMEGP activity shifted to Anakapalli post-district reorganisation (2022)

### Focus District: Anakapalli

| Authority | Office | Documents Targeted |
|---|---|---|
| District Collector | Collectorate, Anakapalli - 531001 | DLMC memos, DLCC minutes, Collectorate proceedings |
| Joint Collector | Collectorate Complex, Anakapalli | Alternate chair for DLMC/DLCC |
| GM, DIC Anakapalli | DIC Office, Anakapalli (newly formed 2022) | Sponsoring letters, PV reports, EDP schedules, Task Force setup |
| PD, DRDA Anakapalli | DRDA Office, Anakapalli | Joint mobilisation circulars, rural mobilisation |
| Lead Bank Manager (Union Bank) | Union Bank Lead Bank Office, Anakapalli | Annual credit plan, PMEGP sub-targets, handholding, RSETI setup |
| District Coordinator, MEPMA | Municipal Corporation, Anakapalli | Urban PMEGP mobilisation |

**Anakapalli PMEGP Activity (FY 2024-25)**:
- Target: 55 projects / ₹157.96 Lakh MM
- Sanctioned: 159 projects / ₹277.89 Lakh MM (289% of target)
- Claimed: 196 projects / ₹289.81 Lakh MM
- Disbursed: 26 projects / ₹100.96 Lakh MM
- **Anomaly**: 65% claim-to-disbursement gap — investigate bank-level MM release delays via DLCC minutes and KVIC State Office review letters

---

## 4. State-Level Authorities Above the Commissioner

| Authority | Role | Document Types | Archive Status |
|---|---|---|---|
| **Hon'ble Chief Minister, AP** | Approves PMEGP state outlay via Cabinet | Cabinet decisions (not public) | N/A |
| **Hon'ble Minister for Industries, AP** | Political head; reviews PMEGP quarterly | Ministerial review minutes | Not acquired |
| **Chief Secretary, AP** | Topmost civil servant; chairs State Level Task Force | SLTF minutes | Not acquired |
| **Principal Secretary, Industries & Commerce Dept** | Administrative head of the department | Departmental proceedings | Not acquired |
| **Commissioner of Industries, AP** | Operational head; issues PMEGP proceedings to all DICs | Commissioner Proceedings | 1 acquired (`AP-COI-2020-0001`) |
| **Director of Industries, AP** | Operational support to Commissioner | Director-level circulars | Not acquired |
| **Vice Chairman & CEO, APIIC** | Manages PMEGP industrial infrastructure | APIIC land allotment circulars | Not acquired |
| **Secretary, Finance Dept** | Approves state matching subsidy budget releases | Budget Release Orders (BROs) | Not acquired (referenced in `AP-GOV-2026-0001`) |

---

## 5. Document Acquisition Status by Layer

| Layer | Total Target Documents | Acquired | Gap | Acquisition Method |
|---|---|---|---|---|
| **Central (MSME/KVIC/RBI)** | ~300 | 115 | ~185 | Wayback Machine (mostly done) |
| **State Cabinet (AP GOs)** | ~120 | 23 | ~97 | apfinance.gov.in S3 (active) |
| **Layer 1: Commissioner of Industries** | ~450 | 1 | ~449 | RTI Priority 1 (offline) |
| **Layer 2: District Collectors (26 districts)** | ~130 × 26 = 3,380 | 0 | 3,380 | RTI Priority 4 (offline) |
| **Layer 3: GMs of DICs (26 districts)** | ~260 × 26 = 6,760 | 0 | 6,760 | RTI Priority 4 (offline) |
| **Layer 3: PDs of DRDAs (26 districts)** | ~130 × 26 = 3,380 | 0 | 3,380 | RTI (offline) |
| **Layer 3: Lead Banks (26 districts)** | ~130 × 26 = 3,380 | 0 | 3,380 | RTI to bank CPIOs (offline) |
| **SLBC AP** | ~50 | 1 | ~49 | RTI Priority 2 (offline) |
| **AP KVIB** | ~95 | 0 | ~95 | RTI (offline) |
| **TOTAL ARCHIVE** | ~2,665 (planning estimate) | 150 | ~2,515 | Mixed |

The Commissioner/Collector/PD layers account for the **vast majority of the remaining gap**. This confirms the strategic insight: these three layers are the **absolute highest-value targets** for making this a definitive, reference-grade archive.

---

## 6. Online Accessibility Assessment

| Authority | Online Portal | Wayback Coverage | Online Documents Accessible? | RTI Required? |
|---|---|---|---|---|
| Commissioner of Industries, AP | `industries.ap.gov.in` | No snapshots | None | **Yes** |
| AP e-Gazette | `egazette.ap.gov.in` | No snapshots | None | **Yes** |
| AP GOIR (GO Repository) | `goir.ap.gov.in` | Splash page only | None | **Yes** |
| District Collectors (26) | `<district>.ap.gov.in` | Limited splash pages | None | **Yes** |
| Vizag Collectorate | `vizagcollectorate.in` | Limited | None | **Yes** |
| DRDA AP | No central portal | N/A | None | **Yes** |
| MEPMA | `mepma.ap.gov.in` | Not probed | TBD | TBD |
| DIC AP | No central portal | N/A | None | **Yes** |
| MSME-DI Visakhapatnam | `msmedivisakhapatnam.ap.nic.in` | DNS fails | None | **Yes** |
| KVIC AP State Office | No portal | N/A | None | **Yes** |
| AP KVIB | `apkvib.org.in` | 2016 splash only | None | **Yes** |
| SLBC AP | `slbcap.nic.in` | Splash only | None | **Yes** |

**Conclusion**: All three target layers (Commissioner, Collector, PD) require RTI filings. The RTI templates in [`docs/rti_templates/`](rti_templates/) are the primary acquisition channel.

---

## 7. How This Hierarchy Informs the RTI Strategy

The four RTI templates in `docs/rti_templates/` map directly to this hierarchy:

| RTI Template | Target Authority | Layer | Expected Documents |
|---|---|---|---|
| `01_coI_ap_state_targets.md` | Commissioner of Industries, AP | Layer 1 | ~15-20 proceedings, instructions, SLTF minutes |
| `02_slbc_ap_quarterly.md` | SLBC AP Convenor Bank | Cross-layer (banking) | ~25-35 agendas, minutes, district reviews |
| `03_kvic_state_office.md` | KVIC State Director, AP | Central-state bridge | ~25-40 review letters, action plans, EDP calendars |
| `04_district_collector.md` | District Collectors (Vizag + Anakapalli) | Layer 2 + Layer 3 | ~70-80 DIC/DLCC/DLRC/Lead Bank/Collector docs |

**Filing all four RTIs simultaneously** will give us the most comprehensive coverage of the three-layer hierarchy in the shortest time. Each RTI has a 30-day response deadline, so filing them in parallel is critical.

---

## 8. Cross-References

- [`docs/MISSING_DOCUMENTS.md`](MISSING_DOCUMENTS.md) — gap registry organised by this hierarchy
- [`docs/DISTRICT_PMEGP_PROGRESS_FY2024_25.md`](DISTRICT_PMEGP_PROGRESS_FY2024_25.md) — district-wise PMEGP progress baseline
- [`docs/rti_templates/`](rti_templates/) — 4 ready-to-file RTI applications
- [`docs/collection_policy.md`](collection_policy.md) — scope and PII rules
- [`docs/collection_guide.md`](collection_guide.md) — practical collection methodology
- [`docs/SOURCE_REGISTRY.md`](SOURCE_REGISTRY.md) — registry of all official source portals
- [`docs/ACQUISITION_DECISIONS.md`](ACQUISITION_DECISIONS.md) — architectural decision records
