#!/usr/bin/env python3
import os
import json
import csv
import shutil
import hashlib
from datetime import datetime

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

def calculate_sha256(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def load_json_db():
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_json_db(db):
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

def save_csv_db(db):
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    headers = [
        "document_id", "title", "type", "issuing_authority", "department", 
        "state", "district", "date", "reference_no", "subject", "keywords", 
        "source_url", "status", "file_path",
        "prov_downloaded_from", "prov_download_date", "prov_downloaded_by", 
        "prov_sha256", "prov_original_filename", "prov_archive_url",
        "relationships_list"
    ]
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for entry in db:
            row = {k: v for k, v in entry.items() if k not in ["provenance", "relationships"]}
            
            # Flatten keywords
            if isinstance(row.get("keywords"), list):
                row["keywords"] = "; ".join(row["keywords"])
                
            # Flatten provenance fields
            prov = entry.get("provenance", {})
            row["prov_downloaded_from"] = prov.get("downloaded_from", "")
            row["prov_download_date"] = prov.get("download_date", "")
            row["prov_downloaded_by"] = prov.get("downloaded_by", "")
            row["prov_sha256"] = prov.get("sha256", "")
            row["prov_original_filename"] = prov.get("original_filename", "")
            row["prov_archive_url"] = prov.get("archive_url", "")
            
            # Flatten relationships
            rels = entry.get("relationships", [])
            rels_flat = []
            for rel in rels:
                rels_flat.append(f"{rel.get('target_id')}({rel.get('type')})")
            row["relationships_list"] = "; ".join(rels_flat)
            
            writer.writerow(row)

def get_next_sequence(db, territory, agency, year):
    prefix = f"{territory}-{agency}-{year}-"
    highest_seq = 0
    for entry in db:
        doc_id = entry.get("document_id", "")
        if doc_id.startswith(prefix):
            try:
                seq_part = doc_id.split("-")[-1]
                seq = int(seq_part)
                if seq > highest_seq:
                    highest_seq = seq
            except ValueError:
                continue
    return highest_seq + 1

def determine_target_dir(state, type_name, district=None):
    state_clean = state.strip().lower()
    type_clean = type_name.strip()
    
    # District Level
    if district:
        dist_slug = district.strip().lower().replace(" ", "-")
        if dist_slug not in DISTRICT_CODES:
            print(f"Warning: Unknown district '{district}'. Creating custom district directory.")
            os.makedirs(os.path.join(repo_root, "districts", dist_slug), exist_ok=True)
        
        territory = f"AP_{DISTRICT_CODES.get(dist_slug, 'DST')}"
        
        if type_clean in ["Proceeding", "Circular", "Instruction"]:
            sub = "dic"
            agency = "DIC"
        elif type_clean in ["Minutes", "Agenda"]:
            sub = "dlcc"
            agency = "DLCC"
        elif type_clean == "Report":
            sub = "lead-bank"
            agency = "LBO"
        else:
            sub = "collector"
            agency = "COLL"
            
        return f"districts/{dist_slug}/{sub}", territory, agency

    # State Level (Andhra Pradesh)
    if "andhra" in state_clean or "ap" == state_clean:
        territory = "AP"
        if "commissioner" in type_clean.lower() or "industries" in type_clean.lower() or type_clean == "Proceeding":
            agency = "COI"
            return "andhra-pradesh/commissioner-of-industries/proceedings", territory, agency
        elif "kvic" in type_clean.lower():
            agency = "KVIC"
            return "andhra-pradesh/kvic-state-office/letters", territory, agency
        elif type_clean == "GO":
            agency = "GOV"
            return "andhra-pradesh/government-orders", territory, agency
        else:
            agency = "GOV"
            return "andhra-pradesh/circulars", territory, agency

    # Central Government / National Level
    territory = "IN"
    if "kvic" in type_clean.lower() or "kvic" in state_clean:
        agency = "KVIC"
        return "central-government/kvic/circulars", territory, agency
    else:
        agency = "MSME"
        if type_clean == "Guidelines":
            return "central-government/msme/guidelines", territory, agency
        elif type_clean == "Notification":
            return "central-government/msme/notifications", territory, agency
        else:
            return "central-government/msme/circulars", territory, agency

def main():
    print("=" * 60)
    print("   PMEGP DOCUMENT ARCHIVE - METADATA CREATOR & REGISTER")
    print("=" * 60)
    
    db = load_json_db()
    
    # Check PDF local file first
    source_file_path = input("Local Path to Document PDF: ").strip()
    while not os.path.exists(source_file_path):
        source_file_path = input("File not found! Please provide correct local path: ").strip()
        
    # Calculate SHA-256 and detect duplicates
    file_sha256 = calculate_sha256(source_file_path)
    print(f"[+] Cryptographic SHA-256 check: {file_sha256}")
    
    for entry in db:
        existing_sha = entry.get("provenance", {}).get("sha256", "")
        if existing_sha == file_sha256:
            print(f"\n[-] ERROR: DUPLICATE DOCUMENT DETECTED!")
            print(f"This PDF has the identical SHA-256 hash as an existing document.")
            print(f"Duplicate Document ID: {entry.get('document_id')}")
            print(f"Existing Title       : {entry.get('title')}")
            print(f"Existing Path        : {entry.get('file_path')}")
            print("Aborting registration to prevent duplicates.")
            return
            
    # 1. Ask for metadata details
    title = input("\nDocument Title: ").strip()
    while not title:
        title = input("Title cannot be empty. Document Title: ").strip()
        
    print(f"\nValid Document Types: {', '.join(VALID_TYPES)}")
    doc_type = input("Document Type: ").strip()
    while doc_type not in VALID_TYPES:
        doc_type = input(f"Invalid type. Select from {VALID_TYPES}: ").strip()
        
    issuing_auth = input("\nIssuing Authority (e.g., Ministry of MSME): ").strip()
    dept = input("Department (e.g., MSME): ").strip()
    
    state_input = input("\nState / Level ('Central' or 'Andhra Pradesh'): ").strip()
    while not state_input:
        state_input = input("State cannot be empty: ").strip()
        
    district = None
    if "andhra" in state_input.lower() or "ap" == state_input.lower():
        is_district = input("Is this document specific to a district? (y/n): ").strip().lower()
        if is_district == 'y':
            print("\nDistricts list:")
            for d in sorted(DISTRICT_CODES.keys()):
                print(f" - {d}")
            district_input = input("Enter AP District Name: ").strip().lower().replace(" ", "-")
            while district_input not in DISTRICT_CODES:
                district_input = input("District not found. Select from the list: ").strip().lower().replace(" ", "-")
            district = district_input.replace("-", " ").title()

    date_str = input("\nDate issued (YYYY-MM-DD): ").strip()
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        year = dt.year
    except ValueError:
        print("Invalid date format. Using current date year for ID, but please correct date in metadata.")
        year = datetime.now().year
        
    ref_no = input("\nReference/Official Number (e.g., No. 01/2023-PMEGP): ").strip()
    subject = input("Concise Subject Summary: ").strip()
    
    keywords_raw = input("\nKeywords (comma-separated): ").strip()
    keywords = [kw.strip() for kw in keywords_raw.split(",") if kw.strip()]
    
    source_url = input("\nSource URL (where did you find it?): ").strip()
    if not source_url:
        source_url = None
        
    print(f"\nValid Statuses: {', '.join(VALID_STATUSES)}")
    status = input("Document Status (default 'Active'): ").strip()
    if not status or status not in VALID_STATUSES:
        status = "Active"
        
    collector = input("\nDownloaded By (your github username, default 'pavan53732'): ").strip()
    if not collector:
        collector = "pavan53732"
        
    archive_url = input("Permanent Web Archive URL (optional, press enter to skip): ").strip()
    if not archive_url:
        archive_url = None

    # Relationship management
    relationships = []
    add_rel = input("\nDoes this document reference, supersede, or amend another document in the repository? (y/n): ").strip().lower()
    if add_rel == 'y':
        target_id = input("Enter Target Document ID: ").strip()
        print("Select Relationship Type:")
        print("1. supersedes\n2. superseded_by\n3. amends\n4. amended_by\n5. references")
        rel_choice = input("Choice (1-5): ").strip()
        rel_map = {"1": "supersedes", "2": "superseded_by", "3": "amends", "4": "amended_by", "5": "references"}
        rel_type = rel_map.get(rel_choice, "references")
        relationships.append({
            "target_id": target_id,
            "type": rel_type
        })
        
    # 2. Automatically determine category directory and construct Document ID
    target_dir, territory, agency = determine_target_dir(state_input, doc_type, district)
    seq = get_next_sequence(db, territory, agency, year)
    doc_id = f"{territory}-{agency}-{year}-{seq:04d}"
    
    file_ext = os.path.splitext(source_file_path)[1].lower()
    new_filename = f"{doc_id}{file_ext}"
    final_file_path = os.path.join(target_dir, new_filename)
    dest_absolute_path = os.path.join(repo_root, final_file_path)
    
    # 3. Create document record
    entry = {
        "document_id": doc_id,
        "title": title,
        "type": doc_type,
        "issuing_authority": issuing_auth,
        "department": dept,
        "state": "Central" if state_input.lower() == "central" else "Andhra Pradesh",
        "district": district,
        "date": date_str,
        "reference_no": ref_no,
        "subject": subject,
        "keywords": keywords,
        "source_url": source_url,
        "status": status,
        "file_path": final_file_path,
        "provenance": {
            "downloaded_from": source_url,
            "download_date": datetime.today().strftime("%Y-%m-%d"),
            "downloaded_by": collector,
            "sha256": file_sha256,
            "original_filename": os.path.basename(source_file_path),
            "archive_url": archive_url
        },
        "relationships": relationships
    }
    
    # 4. Copy and Rename file
    print(f"\nCopying file to: {final_file_path}...")
    os.makedirs(os.path.dirname(dest_absolute_path), exist_ok=True)
    shutil.copy2(source_file_path, dest_absolute_path)
    
    # 5. Append to DB and save
    db.append(entry)
    save_json_db(db)
    save_csv_db(db)
    
    print("\n" + "="*50)
    print("✓ DOCUMENT REGISTERED SUCCESSFULLY!")
    print(f"Generated Document ID : {doc_id}")
    print(f"Saved File Path       : {final_file_path}")
    print("=" * 50)

if __name__ == "__main__":
    main()
