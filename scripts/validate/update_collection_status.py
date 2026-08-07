#!/usr/bin/env python3
import os
import json

# Path references
repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_path = os.path.join(repo_root, "metadata", "documents.json")
status_path = os.path.join(repo_root, "metadata", "collection_status.json")

def get_category_key(path):
    """
    Maps relative file path to collection_status key
    """
    if not path:
        return None
        
    path = path.replace("\\", "/") # cross-platform normalization
    
    # Central Government
    if path.startswith("central-government/msme/guidelines"):
        return "msme_guidelines"
    elif path.startswith("central-government/msme/circulars"):
        return "msme_circulars"
    elif path.startswith("central-government/msme/notifications"):
        return "msme_notifications"
    elif path.startswith("central-government/kvic/circulars"):
        return "kvic_circulars"
    elif path.startswith("central-government/kvic/advisories"):
        return "kvic_advisories"
    elif path.startswith("central-government/kvic/edp"):
        return "kvic_edp"
    elif path.startswith("central-government/kvic/portal"):
        return "kvic_portal"
        
    # State Government (Andhra Pradesh)
    elif path.startswith("andhra-pradesh/government-orders"):
        return "ap_government_orders"
    elif path.startswith("andhra-pradesh/circulars"):
        return "ap_state_circulars"
    elif path.startswith("andhra-pradesh/commissioner-of-industries/proceedings"):
        return "ap_coi_proceedings"
    elif path.startswith("andhra-pradesh/commissioner-of-industries/circulars"):
        return "ap_coi_circulars"
    elif path.startswith("andhra-pradesh/commissioner-of-industries/instructions"):
        return "ap_coi_instructions"
    elif path.startswith("andhra-pradesh/kvic-state-office/circulars"):
        return "kvic_state_circulars"
    elif path.startswith("andhra-pradesh/kvic-state-office/letters"):
        return "kvic_state_letters"
    elif path.startswith("andhra-pradesh/kvic-state-office/review-meetings"):
        return "kvic_state_review_meetings"
        
    # SLBC AP
    elif path.startswith("slbc/agendas"):
        return "slbc_agendas"
    elif path.startswith("slbc/minutes"):
        return "slbc_minutes"
    elif path.startswith("slbc/reports"):
        return "slbc_reports"
        
    # Districts
    elif path.startswith("districts/"):
        parts = path.split("/")
        if len(parts) >= 3:
            sub = parts[2]
            if sub == "collector":
                return "districts_collector"
            elif sub == "dic":
                return "districts_dic"
            elif sub == "dlcc":
                return "districts_dlcc"
            elif sub == "dlrc":
                return "districts_dlrc"
            elif sub == "lead-bank":
                return "districts_lead_bank"
                
    # Banks
    elif path.startswith("banks"):
        return "banks"
        
    return None

def update_status():
    print("=" * 60)
    print("   PMEGP ARCHIVE - COLLECTION COMPLETENESS CALCULATOR")
    print("=" * 60)
    
    if not os.path.exists(json_path):
        print(f"[-] Error: JSON Database not found at {json_path}")
        return False
        
    if not os.path.exists(status_path):
        print(f"[-] Error: collection_status.json not found at {status_path}")
        return False
        
    # Load DB
    with open(json_path, 'r', encoding='utf-8') as f:
        db = json.load(f)
        
    # Load Status Template
    with open(status_path, 'r', encoding='utf-8') as f:
        status_db = json.load(f)
        
    # Reset counts to zero first
    for key in status_db:
        status_db[key]["collected"] = 0
        
    # Count collected documents
    unmapped = 0
    for entry in db:
        file_path = entry.get("file_path", "")
        key = get_category_key(file_path)
        if key and key in status_db:
            status_db[key]["collected"] += 1
        else:
            print(f"[!] Warning: File path could not be mapped to status key: {file_path}")
            unmapped += 1
            
    # Calculate totals
    total_estimated = sum(item["estimated"] for item in status_db.values())
    total_collected = sum(item["collected"] for item in status_db.values())
    
    completeness_percentage = (total_collected / total_estimated) * 100 if total_estimated > 0 else 0
    
    # Write back
    with open(status_path, 'w', encoding='utf-8') as f:
        json.dump(status_db, f, indent=2, ensure_ascii=False)
        
    print(f"[+] Completeness status updated: {total_collected} collected / {total_estimated} estimated.")
    print(f"[+] Total completeness: {completeness_percentage:.2f}%")
    if unmapped > 0:
        print(f"[!] Warnings: {unmapped} unmapped file entries.")
        
    return True

if __name__ == "__main__":
    update_status()
