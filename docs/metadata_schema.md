# PMEGP Archive Metadata Schema

To ensure that the archive acts as a searchable, programmatic database, every single document must have an associated metadata record. These records are compiled into two central files located in the `metadata/` directory:

1. **`metadata/documents.json`** — Standardized JSON array containing deep objects.
2. **`metadata/documents.csv`** — Flattened CSV spreadsheet suitable for Excel, Pandas, or database imports.

---

## 1. Metadata Fields Specification

The following table defines the schema requirements for every document record:

| Field | JSON Key | CSV Header | Type | Required | Description / Format |
|---|---|---|---|---|---|
| **Document ID** | `document_id` | `document_id` | String | **Yes** | e.g. `AP-COI-2024-0012` (Matches name of file) |
| **Title** | `title` | `title` | String | **Yes** | Full official title of the document |
| **Type** | `type` | `type` | String | **Yes** | One of: `GO`, `Circular`, `Notification`, `Proceeding`, `Advisory`, `Letter`, `Minutes`, `Agenda`, `Report`, `Guidelines`, `Instruction`, `Other` |
| **Issuing Authority** | `issuing_authority` | `issuing_authority` | String | **Yes** | e.g. `Commissioner of Industries` |
| **Department** | `department` | `department` | String | **Yes** | e.g. `Industries & Commerce`, `Finance`, `Lead Bank` |
| **State** | `state` | `state` | String | **Yes** | `Andhra Pradesh`, `Central`, or `National` |
| **District** | `district` | `district` | String/Null | **Yes** | AP District name (or `null` if State/National level) |
| **Date** | `date` | `date` | String | **Yes** | `YYYY-MM-DD` format |
| **Reference No** | `reference_no` | `reference_no` | String | **Yes** | Official number (e.g., `G.O.Ms.No. 42`, `Rc.No. 12/PMEGP/2024`) |
| **Subject** | `subject` | `subject` | String | **Yes** | Concise single-sentence subject |
| **Keywords** | `keywords` | `keywords` | Array/String | **Yes** | Comma-separated or array of tags (e.g. `subsidy, margin_money`) |
| **Source URL** | `source_url` | `source_url` | String/Null | **Yes** | Verified download link (or `null` if obtained offline/RTI) |
| **Status** | `status` | `status` | String | **Yes** | `Active`, `Superseded`, `Obsolete`, `Draft` |
| **File Path** | `file_path` | `file_path` | String | **Yes** | Relative path in repo (e.g. `andhra-pradesh/government-orders/AP-GOV-2024-0001.pdf`) |

---

## 2. Example Metadata Entry

### JSON Representation:
```json
{
  "document_id": "AP-COI-2024-0012",
  "title": "PMEGP Review Meeting Proceedings on Subsidy Disbursal",
  "type": "Proceeding",
  "issuing_authority": "Commissioner of Industries",
  "department": "Industries",
  "state": "Andhra Pradesh",
  "district": "Anakapalli",
  "date": "2024-03-14",
  "reference_no": "Rc.No.123/PMEGP/2024",
  "subject": "Review of pending margin money claims and subsidy release targets for Q4 2023-24",
  "keywords": ["PMEGP", "Subsidy", "DIC", "Margin Money"],
  "source_url": "https://industries.ap.gov.in/downloads/pmegp_proceedings_14032024.pdf",
  "status": "Active",
  "file_path": "districts/anakapalli/dic/AP-COI-2024-0012.pdf"
}
```

### CSV Representation:
```csv
document_id,title,type,issuing_authority,department,state,district,date,reference_no,subject,keywords,source_url,status,file_path
AP-COI-2024-0012,PMEGP Review Meeting Proceedings on Subsidy Disbursal,Proceeding,Commissioner of Industries,Industries,Andhra Pradesh,Anakapalli,2024-03-14,Rc.No.123/PMEGP/2024,Review of pending margin money claims and subsidy release targets for Q4 2023-24,"PMEGP, Subsidy, DIC, Margin Money",https://industries.ap.gov.in/downloads/pmegp_proceedings_14032024.pdf,Active,districts/anakapalli/dic/AP-COI-2024-0012.pdf
```
