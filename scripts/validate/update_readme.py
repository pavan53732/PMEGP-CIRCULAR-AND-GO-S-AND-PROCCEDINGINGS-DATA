#!/usr/bin/env python3
import os
import json
import re

# Path references
repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_path = os.path.join(repo_root, "metadata", "documents.json")
status_path = os.path.join(repo_root, "metadata", "collection_status.json")
readme_path = os.path.join(repo_root, "README.md")

def make_progress_bar(percentage, width=30):
    completed_chars = int((percentage / 100) * width)
    remaining_chars = width - completed_chars
    return "[" + "█" * completed_chars + "░" * remaining_chars + "]"

def update_readme():
    print("=" * 60)
    print("   PMEGP ARCHIVE - README STATUS TABLE AUTO-UPDATER")
    print("=" * 60)
    
    # 1. Run collection status calculator first
    status_script = os.path.join(repo_root, "scripts", "validate", "update_collection_status.py")
    if os.path.exists(status_script):
        print("[+] Syncing collection status counts first...")
        os.system(f"python3 {status_script}")
        
    if not os.path.exists(status_path):
        print(f"[-] Error: collection_status.json not found at {status_path}")
        return False
        
    if not os.path.exists(readme_path):
        print(f"[-] Error: README.md not found at {readme_path}")
        return False
        
    # Load status data
    with open(status_path, 'r', encoding='utf-8') as f:
        status_db = json.load(f)
        
    total_estimated = sum(item["estimated"] for item in status_db.values())
    total_collected = sum(item["collected"] for item in status_db.values())
    completeness = (total_collected / total_estimated) * 100 if total_estimated > 0 else 0
    
    progress_bar = make_progress_bar(completeness)
    
    # Generate Markdown status block
    lines = []
    lines.append("### Archive Collection Completeness")
    lines.append(f"**Completeness Score: `{completeness:.2f}%`**")
    lines.append(f"```text\n{progress_bar} {total_collected} / {total_estimated} documents collected\n```")
    lines.append("")
    lines.append("#### Completeness Breakdown by Official Source")
    lines.append("")
    lines.append("| Authority / Source | Estimated | Collected | Status | Progress |")
    lines.append("|---|---|---|---|---|")
    
    # Sort or iterate through status sections
    for key, data in status_db.items():
        label = data["label"]
        est = data["estimated"]
        col = data["collected"]
        pct = (col / est) * 100 if est > 0 else 0
        
        status_icon = "⏳ Pending"
        if col > 0:
            status_icon = "🟢 Active" if pct >= 100 else "🟡 In Progress"
            
        short_bar = make_progress_bar(pct, width=10)
        lines.append(f"| {label} | {est} | {col} | {status_icon} | `{short_bar}` ({pct:.1f}%) |")
        
    lines.append(f"| **TOTAL ARCHIVE** | **{total_estimated}** | **{total_collected}** | **{'🟡 Curation Phase' if total_collected > 0 else '⏳ Pending'}** | `{progress_bar}` ({completeness:.2f}%) |")
    
    table_content = "\n".join(lines)
    
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
        
    print(f"[+] Successfully updated README.md statistics with {total_collected}/{total_estimated} completeness status!")
    return True

if __name__ == "__main__":
    update_readme()
