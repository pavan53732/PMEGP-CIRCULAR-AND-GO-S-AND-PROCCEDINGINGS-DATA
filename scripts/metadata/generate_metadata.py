#!/usr/bin/env python3
import os
import json
import csv
import shutil
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
        "source_url", "status", "file_path"
    ]
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for entry in db:
            row = entry.copy()
            # Flatten keywords list to semi-colon separated string for CSV compatibility
            if isinstance(row["keywords"], list):
                row["keywords"] = "; ".join(row["keywords"])
            writer.writerow(row)

def get_next_sequence(db, territory, agency, year):
    # ID pattern: AP_ANA-DIC-2024-0001
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
    """
    Returns relative directory path in repo and territory/agency parts for Document ID
    """
    state_clean = state.strip().lower()
    type_clean = type_name.strip()
    
    # District Level
    if district:
        dist_slug = district.strip().lower().replace(" ", "-")
        if dist_slug not in DISTRICT_CODES:
            print(f"Warning: Unknown district '{district}'. Creating custom district directory.")
            os.makedirs(os.path.join(repo_root, "districts", dist_slug), exist_ok=True)
        
        territory = f"AP_{DISTRICT_CODES.get(dist_slug, 'DST')}"
        
        # Mapping type to folder
        if type_clean == "Proceeding" or type_clean == "Circular":
            sub = "dic"
            agency = "DIC"
        elif type_clean == "Minutes" or type_clean == "Agenda":
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
        return "central-government/msme/circulars", territory, agency

def main():
    print("=" * 60)
    print("   PMEGP DOCUMENT ARCHIVE - METADATA CREATOR & REGISTER")
    print("=" * 60)
    
    db = load_json_db()
    
    # 1. Ask for metadata details
    title = input("Document Title: ").strip()
    while not title:
        title = input("Title cannot be empty. Document Title: ").strip()
        
    print(f"\nValid Document Types: {', '.join(VALID_TYPES)}")
    doc_type = input("Document Type (e.g., GO, Circular, Proceeding, Guidelines): ").strip()
    while doc_type not in VALID_TYPES:
        doc_type = input(f"Invalid type. Select from {VALID_TYPES}: ").strip()
        
    issuing_auth = input("\nIssuing Authority (e.g., Commissioner of Industries): ").strip()
    dept = input("Department (e.g., Industries & Commerce): ").strip()
    
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
        
    ref_no = input("\nReference/Official Number (e.g., Rc.No.123/PMEGP/2024): ").strip()
    subject = input("Concise Subject Summary: ").strip()
    
    keywords_raw = input("\nKeywords (comma-separated): ").strip()
    keywords = [kw.strip() for kw in keywords_raw.split(",") if kw.strip()]
    
    source_url = input("\nSource URL (optional, press enter to skip): ").strip()
    if not source_url:
        source_url = None
        
    status = input("Document Status ('Active', 'Superseded', 'Obsolete'): ").strip()
    if not status:
        status = "Active"
        
    source_file_path = input("\nLocal Path to Document PDF: ").strip()
    while not os.path.exists(source_file_path):
        source_file_path = input("File not found! Please provide correct local path: ").strip()
        
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
        "file_path": final_file_path
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
