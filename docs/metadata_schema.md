# PMEGP Archive Metadata Schema & Provenance Standards

To ensure that the archive acts as a trustworthy, academic, and administrative resource, every document must be systematically indexed and fully validated. This file specifies the advanced JSON and CSV schemas, which track relationships, status progression, and file provenance.

---

## 1. Advanced Status Taxonomy

A document's administrative lifespan must be precisely recorded under the `status` field:

*   **`Active`**: Currently in force and represents the active guideline, target, or procedure.
*   **`Superseded`**: Replaced by a newer document (which must be linked under `relationships`).
*   **`Withdrawn`**: Revoked by the issuing authority without a direct replacement.
*   **`Cancelled`**: Declared void or invalid.
*   **`Merged`**: Combined with another document to form a new policy.
*   **`Amended`**: Modified by a subsequent circular or amendment order.

---

## 2. Provenance Tracking

To prove the authenticity of each PDF and avoid any accidental duplication or fabrication, every record must trace its origin using cryptographic and metadata checkpoints under the `provenance` sub-object:

*   **`downloaded_from`**: The exact live URL of the official source portal.
*   **`download_date`**: The date the file was fetched (`YYYY-MM-DD`).
*   **`downloaded_by`**: The username or identity of the collector.
*   **`sha256`**: The SHA-256 cryptographic hash of the PDF file. (Serves as a tamper-evident seal and duplicate detector).
*   **`original_filename`**: The file name as originally served by the portal.
*   **`archive_url`**: A link to a permanent web archive (such as the Wayback Machine) if available.

---

## 3. Document Relationship Indexing

Administrative policies are deeply interconnected. To capture relationships, each document metadata can include a list under `relationships` containing:

*   `target_id`: The ID of the related document (e.g., `IN-MSME-2018-0001`).
*   `type`: The relationship type:
    *   `superseded_by` (this document was replaced by the target)
    *   `supersedes` (this document replaces the target)
    *   `amends` (this document amends the target)
    *   `amended_by` (this document is amended by the target)
    *   `references` / `referenced_by` (citation links)

---

## 4. Master Schema Specification

The following table defines the final, production-ready schema:

| Field | JSON Key | CSV Header | Type | Required | Format & Constraints |
|---|---|---|---|---|---|
| **Document ID** | `document_id` | `document_id` | String | **Yes** | e.g. `IN-MSME-2018-0001` |
| **Title** | `title` | `title` | String | **Yes** | Full official title |
| **Type** | `type` | `type` | String | **Yes** | `GO`, `Circular`, `Notification`, `Proceeding`, `Advisory`, `Letter`, `Minutes`, `Agenda`, `Report`, `Guidelines`, `Instruction`, `Other` |
| **Issuing Authority** | `issuing_authority` | `issuing_authority` | String | **Yes** | e.g., `Ministry of MSME` |
| **Department** | `department` | `department` | String | **Yes** | e.g., `MSME`, `Industries`, `Lead Bank` |
| **State** | `state` | `state` | String | **Yes** | `Central`, `Andhra Pradesh` |
| **District** | `district` | `district` | String/Null | **Yes** | Official district name (or `null`) |
| **Date** | `date` | `date` | String | **Yes** | `YYYY-MM-DD` |
| **Reference No** | `reference_no` | `reference_no` | String | **Yes** | e.g., `No. 01/2023-PMEGP` |
| **Subject** | `subject` | `subject` | String | **Yes** | One-sentence summary |
| **Keywords** | `keywords` | `keywords` | Array/String | **Yes** | Tags |
| **Source URL** | `source_url` | `source_url` | String/Null | **Yes** | Verified download link |
| **Status** | `status` | `status` | String | **Yes** | `Active`, `Superseded`, `Withdrawn`, `Cancelled`, `Merged`, `Amended` |
| **File Path** | `file_path` | `file_path` | String | **Yes** | Relative path in repo |
| **Provenance** | `provenance` | *(Nested/Prefix)* | Object | **Yes** | Source, Date, Collector, Hash, Original Name |
| **Relationships** | `relationships` | *N/A* | Array | **Yes** | Direct policy relations |

---

## 5. Production Examples

### JSON Representation:
```json
[
  {
    "document_id": "IN-MSME-2018-0001",
    "title": "Guidelines on Prime Minister's Employment Generation Programme (PMEGP)",
    "type": "Guidelines",
    "issuing_authority": "Ministry of Micro, Small and Medium Enterprises",
    "department": "MSME",
    "state": "Central",
    "district": null,
    "date": "2018-09-14",
    "reference_no": "Regp6/desk/new sch.pmegp/guide",
    "subject": "Operational guidelines detailing project subsidies, bank accounts operation, EDP training, and monitoring of PMEGP",
    "keywords": [
      "PMEGP",
      "Guidelines",
      "Subsidy",
      "EDP Training",
      "Bank Accounts"
    ],
    "source_url": "https://slbcorissa.com/wp-content/uploads/2018/09/PMEGP-Scheme-Guidelines.pdf",
    "status": "Superseded",
    "file_path": "central-government/msme/guidelines/IN-MSME-2018-0001.pdf",
    "provenance": {
      "downloaded_from": "https://slbcorissa.com/wp-content/uploads/2018/09/PMEGP-Scheme-Guidelines.pdf",
      "download_date": "2026-08-07",
      "downloaded_by": "pavan53732",
      "sha256": "73dc70f88b63ebf4f488f6a31c146d7b248ef4e52e0d54214378820df0f3de04",
      "original_filename": "PMEGP-Scheme-Guidelines.pdf",
      "archive_url": null
    },
    "relationships": [
      {
        "target_id": "IN-MSME-2023-0001",
        "type": "superseded_by"
      }
    ]
  }
]
```
