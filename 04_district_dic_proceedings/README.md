# 04 - District DIC Proceedings

## What goes here

Proceedings from **District Industries Centres (DICs)** across all 26 districts of Andhra Pradesh. DICs are the **primary implementing agencies** for PMEGP at the district level.

## Why this is the largest category

There are **26 districts**, each with an active DIC that issues proceedings related to:
- District-level PMEGP target allocation and utilization
- Application scrutiny and recommendation decisions
- EDP (Entrepreneurship Development Programme) training schedules
- Monthly/quarterly review meetings
- Subsidy disbursement tracking
- Coordination with banks and district administration

## All 26 AP Districts

| # | District | DIC Code | Status |
|---|----------|----------|--------|
| 1 | Anakapalli | DIC-ANP | ⏳ Pending |
| 2 | Anantapur | DIC-ANT | ⏳ Pending |
| 3 | Annamayya | DIC-ANY | ⏳ Pending |
| 4 | Bapatla | DIC-BPT | ⏳ Pending |
| 5 | Chittoor | DIC-CTR | ⏳ Pending |
| 6 | Dr. B.R. Ambedkar Konaseema | DIC-BRK | ⏳ Pending |
| 7 | East Godavari | DIC-EGV | ⏳ Pending |
| 8 | Eluru | DIC-ELU | ⏳ Pending |
| 9 | Guntur | DIC-GNT | ⏳ Pending |
| 10 | Kakinada | DIC-KKD | ⏳ Pending |
| 11 | Kurnool | DIC-KNL | ⏳ Pending |
| 12 | Kuppam | DIC-KPM | ⏳ Pending |
| 13 | Nandyal | DIC-NDL | ⏳ Pending |
| 14 | NTR | DIC-NTR | ⏳ Pending |
| 15 | Narasaraopet | DIC-NRT | ⏳ Pending |
| 16 | Palnadu | DIC-PLD | ⏳ Pending |
| 17 | Parvathipuram Manyam | DIC-PVM | ⏳ Pending |
| 18 | Prakasam | DIC-PKM | ⏳ Pending |
| 19 | SPSR Nellore | DIC-NLR | ⏳ Pending |
| 20 | Sri Sathya Sai | DIC-SSA | ⏳ Pending |
| 21 | Tirupati | DIC-TPT | ⏳ Pending |
| 22 | Alluri Sitharama Raju | DIC-ASR | ⏳ Pending |
| 23 | Vishakapatnam | DIC-VSK | ⏳ Pending |
| 24 | Vizianagaram | DIC-VZM | ⏳ Pending |
| 25 | West Godavari | DIC-WGV | ⏳ Pending |
| 26 | YSR Kadapa | DIC-KDP | ⏳ Pending |

## Collection strategy

**Do NOT try to collect all 26 districts at once.** Prioritize based on:
1. **Districts with functional websites** (Vishakapatnam, Guntur, Chittoor, Anantapur typically have better online presence)
2. **High PMEGP application volume** districts
3. **RTI requests** for districts with no online presence

## Folder structure within this category

```
04_district_dic_proceedings/
├── README.md
├── anantapur/
├── chittoor/
├── guntur/
├── ... (one subfolder per district)
└── vishakapatnam/
```

## Naming convention

```
PMEGP-AP-YYYY-NNN_districtcode_descriptive_slug.pdf
PMEGP-AP-YYYY-NNN_districtcode_descriptive_slug.metadata.json
```

Example: `PMEGP-AP-2024-015_ANT_edp_training_schedule_q2.pdf`

## Notes

- Many DICs do **not** have functional websites — RTI and physical visits are often necessary
- DIC proceedings may contain **PII** (applicant names, addresses) — **redact before uploading**
- Some DICs issue proceedings in **Telugu only** — flag with `"language": "te"`