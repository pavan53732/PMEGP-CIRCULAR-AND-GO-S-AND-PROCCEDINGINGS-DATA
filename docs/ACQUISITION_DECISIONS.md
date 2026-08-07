# PMEGP Archive Acquisition Decision Log (ADL)

This document functions as an Architecture and Curation Decision Record (ADR) for the Prime Minister's Employment Generation Programme (PMEGP) Document Archive. Every significant policy decision, scoping boundary, or collection exception must be formally logged here to preserve the repository's intellectual integrity over time.

---

## AD-0001: Jurisdictional Scoping Constraints

*   **Decision**: The repository scope is strictly restricted to **Central Government (National)** and **Andhra Pradesh State** PMEGP documents. Any documents from other states (e.g., Karnataka, Telangana, Tamil Nadu, Odisha) are outside the repository's collection scope.
*   **Reason**: To maintain a tight, complete, and highly authoritative dataset for PMEGP implementation in Andhra Pradesh without distracting contributors or diluting progress metrics with unrelated local rules.
*   **Decision Date**: 2026-08-07
*   **Status**: **ACCEPTED** (Enforced immediately via deletion of Karnataka SLBC reports)

---

## AD-0002: Acceptance of Official Secondary Mirrors

*   **Decision**: Documents may be sourced and downloaded from official secondary government or bank mirrors (such as State Level Bankers' Committees of neighboring states, or academic archives) **only** if the primary government issuing portal is offline, permanently relocated, or geoblocked/firewalled.
*   **Reason**: Outbound HTTP requests from server hosting ranges are frequently geoblocked by `.nic.in` or specific Indian state subnets. Using certified secondary mirrors prevents collection blockages while still ensuring text authenticity.
*   **Decision Date**: 2026-08-07
*   **Status**: **ACCEPTED**

---

## AD-0003: Multi-Dimensional Quality Auditing

*   **Decision**: Replace single-metric quality scales with a three-dimensional matrix assessing Authenticity, Document Format, and Metadata Completeness independently.
*   **Reason**: A single score fails to convey situations where a document is fully authentic (A) but suffers from poor scan legibility (C), or where metadata is incomplete (C) despite a pristine digital native source (A).
*   **Decision Date**: 2026-08-07
*   **Status**: **ACCEPTED**

---

## AD-0004: Formalization of Acquisition States

*   **Decision**: Establish a formal document acquisition state workflow (`DISCOVERED` -> `DOWNLOADED` -> `VERIFIED` -> `CURATED` -> `REJECTED` -> `REPLACED`) that operates separately from a document's legal status (`Active`, `Superseded`).
*   **Reason**: To separate the legal and administrative life-cycle of a government policy from the operational workflow of our curation queue.
*   **Decision Date**: 2026-08-07
*   **Status**: **ACCEPTED**
