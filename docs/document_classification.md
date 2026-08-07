# PMEGP Document Classification and Naming Standards

To keep the repository cleanly organized and fully searchable, every document must follow strict folder placement rules and naming conventions.

---

## 1. Directory Structure Mapping

The repository has been restructured into logical folders reflecting the administrative hierarchy of PMEGP implementation:

| Category | Folder Path | Description |
|---|---|---|
| **Central MSME** | `central-government/msme/` | Policy guidelines, circulars, and notifications from the Ministry of MSME |
| **Central KVIC** | `central-government/kvic/` | Circulars, advisories, EDP training norms, and portal updates from KVIC HO |
| **AP State Govt** | `andhra-pradesh/` | State-level GOs and circulars from Andhra Pradesh Secretariats |
| **AP Commissioner** | `andhra-pradesh/commissioner-of-industries/` | Proceedings, circulars, and administrative instructions from the CoI AP |
| **AP KVIC State** | `andhra-pradesh/kvic-state-office/` | Circulars, review meeting logs, and letters from the KVIC State Office, AP |
| **SLBC AP** | `slbc/` | Agendas, minutes, and performance reports of the State Level Bankers' Committee |
| **Districts** | `districts/[district-name]/` | All local records (Collector, DIC, DLCC, DLRC, Lead Bank) for AP's 26 districts |
| **Banks** | `banks/` | Standard circulars, lending norms, and targets from individual commercial/rural banks |

---

## 2. Document Naming Convention

Every file added to the repository must be named exactly according to its unique **Document ID** to maintain clean path references:

### Format:
`[DOCUMENT_ID].[EXTENSION]`

### Example:
- PDF document: `AP-COI-2024-0012.pdf`
- Metadata record (if saved alongside): `AP-COI-2024-0012.metadata.json`

---

## 3. Document ID Scheme

The Document ID acts as the unique primary key across the entire archive. It is structured as:

`[TERRITORY]-[AGENCY_CODE]-[YEAR]-[SEQUENCE]`

### Elements:
1. **Territory:**
   - `IN` = Central Government or National Level
   - `AP` = Andhra Pradesh State Level
   - `AP_[DISTRICT_SLUG]` = District Level (e.g. `AP_ANA` for Anakapalli)
2. **Agency Code:**
   - `MSME` = Ministry of MSME
   - `KVIC` = Khadi & Village Industries Commission
   - `GOV` = State Government (Chief Secretariat)
   - `COI` = Commissioner of Industries
   - `SLBC` = State Level Bankers' Committee
   - `COLL` = District Collector
   - `DIC` = District Industries Centre
   - `DLCC` = District Level Consultative Committee
   - `DLRC` = District Level Review Committee
   - `LBO` = Lead Bank Office
   - `BNK` = Individual Bank
3. **Year:** 4-digit year of issuance (e.g., `2024`)
4. **Sequence:** 4-digit sequential integer starting at `0001` per agency per year.

### Examples:
- **AP-COI-2024-0012:** The 12th document registered issued by the AP Commissioner of Industries in the year 2024.
- **IN-MSME-2023-0005:** The 5th document registered issued by the Central Ministry of MSME in 2023.
- **AP_ANA-DIC-2024-0002:** The 2nd document registered issued by the Anakapalli District DIC in 2024.

---

## 4. AP District Slugs

For District Territory codes and directory structures, use these uniform lowercase slugs and 3-letter codes for IDs:

| District Name | Folder Slug | District ID Code |
|---|---|---|
| Alluri Sitharama Raju | `alluri-sitharama-raju` | `ASR` |
| Anakapalli | `anakapalli` | `ANA` |
| Anantapur | `anantapur` | `ATP` |
| Annamayya | `annamayya` | `AMY` |
| Bapatla | `bapatla` | `BPT` |
| Chittoor | `chittoor` | `CTR` |
| Dr. B.R. Ambedkar Konaseema | `dr-br-ambedkar-konaseema` | `KSM` |
| East Godavari | `east-godavari` | `EG` |
| Eluru | `eluru` | `ELR` |
| Guntur | `guntur` | `GNT` |
| Kakinada | `kakinada` | `KKD` |
| Krishna | `krishna` | `KRI` |
| Kurnool | `kurnool` | `KNL` |
| Nandyal | `nandyal` | `NDL` |
| NTR | `ntr` | `NTR` |
| Palnadu | `palnadu` | `PLN` |
| Parvathipuram Manyam | `parvathipuram-manyam` | `PVM` |
| Prakasam | `prakasam` | `PKM` |
| SPS Nellore | `sps-nellore` | `NLR` |
| Srikakulam | `srikakulam` | `SKL` |
| Sri Sathya Sai | `sri-sathya-sai` | `SSS` |
| Tirupati | `tirupati` | `TPT` |
| Visakhapatnam | `visakhapatnam` | `VSP` |
| Vizianagaram | `vizianagaram` | `VZM` |
| West Godavari | `west-godavari` | `WG` |
| YSR Kadapa | `ysr-kadapa` | `KDP` |
