#!/usr/bin/env python3
import os
import json
import csv
import re

# Path references
repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_path = os.path.join(repo_root, "metadata", "documents.json")
csv_path = os.path.join(repo_root, "metadata", "documents.csv")

# Standard districts mapping
DISTRICT_CODES = {
    "alluri-sitharama-raju": "ASR",
    "anakapalli": "ANA",
    "anantapur": "ATP",
    "annamayya": "AMY",
    "bapatla": "BPT",
    "chittoor": "CTR",
    "dr-br-ambedkar-konaseema": "KSM",
    "east-godavari": "EG",
    "eluru": "ELR",
    "guntur": "GNT",
    "kakinada": "KKD",
    "krishna": "KRI",
    "kurnool": "KNL",
    "nandyal": "NDL",
    "ntr": "NTR",
    "palnadu": "PLN",
    "parvathipuram-manyam": "PVM",
    "prakasam": "PKM",
    "sps-nellore": "NLR",
    "srikakulam": "SKL",
    "sri-sathya-sai": "SSS",
    "tirupati": "TPT",
    "visakhapatnam": "VSP",
    "vizianagaram": "VZM",
    "west-godavari": "WG",
    "ysr-kadapa": "KDP"
}

VALID_TYPES = [
    "GO", "Circular", "Notification", "Proceeding", "Advisory", 
    "Letter", "Minutes", "Agenda", "Report", "Guidelines", "Instruction", "Other"
]

VALID_STATUSES = ["Active", "Superseded", "Withdrawn", "Cancelled", "Merged", "Amended"]

VALID_QUALITY_SCORES = ["A", "B", "C", "D", "X"]

def validate():
    print("=" * 60)
    print("   PMEGP ARCHIVE - METADATA INTEGRITY VALIDATOR")
    print("=" * 60)
    
    errors = []
    warnings = []
    
    # 1. Verify files exist
    if not os.path.exists(json_path):
        print("[-] Error: metadata/documents.json is missing!")
        return False
    if not os.path.exists(csv_path):
        print("[-] Error: metadata/documents.csv is missing!")
        return False
        
    # 2. Parse JSON Database
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            json_db = json.load(f)
        print(f"[+] Loaded JSON database: {len(json_db)} entries.")
    except Exception as e:
        print(f"[-] Error: Failed to parse metadata/documents.json: {e}")
        return False
        
    # 3. Parse CSV Database
    csv_entries = []
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                csv_entries.append(row)
        print(f"[+] Loaded CSV database: {len(csv_entries)} entries.")
    except Exception as e:
        print(f"[-] Error: Failed to parse metadata/documents.csv: {e}")
        return False
        
    # 4. Cross-Reference Databases
    json_ids = {entry.get("document_id") for entry in json_db}
    csv_ids = {entry.get("document_id") for entry in csv_entries}
    
    extra_in_json = json_ids - csv_ids
    extra_in_csv = csv_ids - json_ids
    
    if extra_in_json:
        errors.append(f"Document IDs found in JSON but missing from CSV: {extra_in_json}")
    if extra_in_csv:
        errors.append(f"Document IDs found in CSV but missing from JSON: {extra_in_csv}")
        
    # 5. Detail validation for each entry
    id_pattern = re.compile(r"^[A-Z_]+-[A-Z]+-\d{4}-\d{4}$")
    sha_hashes = {} # To detect duplicate hashes
    
    for idx, entry in enumerate(json_db):
        doc_id = entry.get("document_id", f"ENTRY_INDEX_{idx}")
        
        # Check ID format
        if not id_pattern.match(doc_id):
            errors.append(f"[{doc_id}] Document ID format is invalid. Expected [TERRITORY]-[AGENCY]-[YEAR]-[SEQUENCE] (e.g. AP-COI-2024-0012)")
            
        # Check required fields
        required_fields = ["title", "type", "issuing_authority", "department", "state", "date", "reference_no", "subject", "keywords", "status", "quality_score", "file_path", "provenance"]
        for field in required_fields:
            val = entry.get(field)
            if val is None or val == "" or (isinstance(val, list) and not val):
                errors.append(f"[{doc_id}] Missing or empty required field: '{field}'")
                
        # Validate Type
        doc_type = entry.get("type")
        if doc_type and doc_type not in VALID_TYPES:
            errors.append(f"[{doc_id}] Invalid type '{doc_type}'. Must be one of {VALID_TYPES}")
            
        # Validate Status
        status = entry.get("status")
        if status and status not in VALID_STATUSES:
            errors.append(f"[{doc_id}] Invalid status '{status}'. Must be one of {VALID_STATUSES}")
            
        # Validate Quality Score
        quality = entry.get("quality_score")
        if quality and quality not in VALID_QUALITY_SCORES:
            errors.append(f"[{doc_id}] Invalid quality_score '{quality}'. Must be one of {VALID_QUALITY_SCORES}")
            
        # Validate State & District mapping
        state = entry.get("state")
        district = entry.get("district")
        if district:
            dist_slug = district.lower().replace(" ", "-")
            if dist_slug not in DISTRICT_CODES:
                errors.append(f"[{doc_id}] District '{district}' is not in the official 26 AP districts list.")
            elif not doc_id.startswith(f"AP_{DISTRICT_CODES[dist_slug]}"):
                warnings.append(f"[{doc_id}] District Specific ID prefix doesn't match district code (expected prefix 'AP_{DISTRICT_CODES[dist_slug]}')")
                
        # Validate File Path Existence
        file_path = entry.get("file_path")
        if file_path:
            abs_file_path = os.path.join(repo_root, file_path)
            if not os.path.exists(abs_file_path):
                errors.append(f"[{doc_id}] File does not exist at specified path: '{file_path}'")
            elif not os.path.isfile(abs_file_path):
                errors.append(f"[{doc_id}] Path is not a file: '{file_path}'")
                
        # Validate Provenance Block
        prov = entry.get("provenance")
        if isinstance(prov, dict):
            prov_req = ["download_date", "downloaded_by", "sha256", "original_filename"]
            for pr_f in prov_req:
                if not prov.get(pr_f):
                    errors.append(f"[{doc_id}] Provenance missing subfield: '{pr_f}'")
            
            # Duplication Hash Check
            sha = prov.get("sha256")
            if sha:
                if sha in sha_hashes:
                    errors.append(f"[{doc_id}] Duplicate file hash detected! Shares identical SHA-256 hash with '{sha_hashes[sha]}'.")
                else:
                    sha_hashes[sha] = doc_id
        else:
            if "provenance" in entry:
                errors.append(f"[{doc_id}] Provenance block is invalid (expected a JSON object).")
                
    # 6. Report Summary
    print("\n" + "="*50)
    print("   INTEGRITY SUMMARY REPORT")
    print("="*50)
    print(f"Total Entries Checked : {len(json_db)}")
    print(f"Errors Found          : {len(errors)}")
    print(f"Warnings Found        : {len(warnings)}")
    print("="*50)
    
    if warnings:
        print("\n[!] Warnings:")
        for warning in warnings:
            print(f"  - {warning}")
            
    if errors:
        print("\n[-] Critical Validation Failures:")
        for error in errors:
            print(f"  - {error}")
        print("\n[❌] Validation Failed. Please resolve all errors before pushing changes.")
        return False
    else:
        print("\n[✓] Validation Succeeded! Metadata database is healthy and synced.")
        return True

if __name__ == "__main__":
    import sys
    success = validate()
    sys.exit(0 if success else 1)
