#!/usr/bin/env python3
import os
import json

# Path references
repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_path = os.path.join(repo_root, "metadata", "documents.json")
readme_path = os.path.join(repo_root, "README.md")

def update_readme():
    print("=" * 60)
    print("   PMEGP ARCHIVE - README STATUS TABLE AUTO-UPDATER")
    print("=" * 60)
    
    if not os.path.exists(json_path):
        print(f"[-] Error: JSON Database not found at {json_path}")
        return False
        
    if not os.path.exists(readme_path):
        print(f"[-] Error: README.md not found at {readme_path}")
        return False
        
    # Load database
    with open(json_path, 'r', encoding='utf-8') as f:
        db = json.load(f)
        
    # Categories counts
    counts = {
        "central_msme": 0,
        "central_kvic": 0,
        "ap_state_govt": 0,
        "ap_coi": 0,
        "ap_kvic": 0,
        "slbc": 0,
        "districts": 0,
        "banks": 0
    }
    
    for entry in db:
        path = entry.get("file_path", "")
        if path.startswith("central-government/msme"):
            counts["central_msme"] += 1
        elif path.startswith("central-government/kvic"):
            counts["central_kvic"] += 1
        elif path.startswith("andhra-pradesh/commissioner-of-industries"):
            counts["ap_coi"] += 1
        elif path.startswith("andhra-pradesh/kvic-state-office"):
            counts["ap_kvic"] += 1
        elif path.startswith("andhra-pradesh/"):
            counts["ap_state_govt"] += 1
        elif path.startswith("slbc"):
            counts["slbc"] += 1
        elif path.startswith("districts"):
            counts["districts"] += 1
        elif path.startswith("banks"):
            counts["banks"] += 1

    total_docs = len(db)
    
    # Generate Markdown Table
    table_lines = [
        "| Section / Category | Folder Path | Count | Status |",
        "|---|---|---|---|",
        f"| **Central Govt (MSME)** | `central-government/msme/` | {counts['central_msme']} | {'🟢 Active' if counts['central_msme'] > 0 else '⏳ Pending'} |",
        f"| **Central Govt (KVIC)** | `central-government/kvic/` | {counts['central_kvic']} | {'🟢 Active' if counts['central_kvic'] > 0 else '⏳ Pending'} |",
        f"| **AP State Govt Orders** | `andhra-pradesh/government-orders/` | {counts['ap_state_govt']} | {'🟢 Active' if counts['ap_state_govt'] > 0 else '⏳ Pending'} |",
        f"| **AP Commissioner of Industries** | `andhra-pradesh/commissioner-of-industries/` | {counts['ap_coi']} | {'🟢 Active' if counts['ap_coi'] > 0 else '⏳ Pending'} |",
        f"| **AP KVIC State Office** | `andhra-pradesh/kvic-state-office/` | {counts['ap_kvic']} | {'🟢 Active' if counts['ap_kvic'] > 0 else '⏳ Pending'} |",
        f"| **SLBC AP Records** | `slbc/` | {counts['slbc']} | {'🟢 Active' if counts['slbc'] > 0 else '⏳ Pending'} |",
        f"| **District Level (26 Districts)** | `districts/` | {counts['districts']} | {'🟢 Active' if counts['districts'] > 0 else '⏳ Pending'} |",
        f"| **Banks Rules & Guidelines** | `banks/` | {counts['banks']} | {'🟢 Active' if counts['banks'] > 0 else '⏳ Pending'} |",
        f"| **Total Curated Documents** | **-** | **{total_docs}** | **🟢 Active Curation** |"
    ]
    table_content = "\n".join(table_lines)
    
    # Read README
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()
        
    start_tag = "<!-- STATUS_TABLE_START -->"
    end_tag = "<!-- STATUS_TABLE_END -->"
    
    if start_tag not in readme_content or end_tag not in readme_content:
        print("[-] Error: README.md does not contain STATUS_TABLE comment anchors!")
        return False
        
    # Replace content between anchors
    pattern = re.compile(rf"{re.escape(start_tag)}.*?{re.escape(end_tag)}", re.DOTALL)
    replacement = f"{start_tag}\n\n{table_content}\n\n{end_tag}"
    new_readme_content = pattern.sub(replacement, readme_content)
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_readme_content)
        
    print(f"[+] Successfully updated README.md statistics with {total_docs} total documents!")
    return True

if __name__ == "__main__":
    import re
    update_readme()
