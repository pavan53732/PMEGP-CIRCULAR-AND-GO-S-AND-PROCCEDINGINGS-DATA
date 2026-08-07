#!/usr/bin/env python3
import os
import shutil

# Root path of the repository
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(f"Target repository root: {repo_root}")

# List of old directories to remove
old_dirs = [
    "01_ap_government_gos_and_circulars",
    "02_kvic_andhra_pradesh_letters",
    "03_commissioner_of_industries_proceedings",
    "04_district_dic_proceedings",
    "05_collector_proceedings",
    "06_slbc_dlcc_records",
    "07_miscellaneous",
    "data_raw",
    "data_processed"
]

# Standard 26 districts of Andhra Pradesh
districts = [
    "alluri-sitharama-raju",
    "anakapalli",
    "anantapur",
    "annamayya",
    "bapatla",
    "chittoor",
    "dr-br-ambedkar-konaseema",
    "east-godavari",
    "eluru",
    "guntur",
    "kakinada",
    "krishna",
    "kurnool",
    "nandyal",
    "ntr",
    "palnadu",
    "parvathipuram-manyam",
    "prakasam",
    "sps-nellore",
    "srikakulam",
    "sri-sathya-sai",
    "tirupati",
    "visakhapatnam",
    "vizianagaram",
    "west-godavari",
    "ysr-kadapa"
]

# Core directories in the new recommended structure
new_dirs = [
    # Documentation
    "docs",
    
    # Central Government
    "central-government/msme/guidelines",
    "central-government/msme/circulars",
    "central-government/msme/notifications",
    "central-government/kvic/circulars",
    "central-government/kvic/advisories",
    "central-government/kvic/edp",
    "central-government/kvic/portal",
    
    # State Government of Andhra Pradesh
    "andhra-pradesh/government-orders",
    "andhra-pradesh/circulars",
    "andhra-pradesh/commissioner-of-industries/proceedings",
    "andhra-pradesh/commissioner-of-industries/circulars",
    "andhra-pradesh/commissioner-of-industries/instructions",
    "andhra-pradesh/kvic-state-office/circulars",
    "andhra-pradesh/kvic-state-office/letters",
    "andhra-pradesh/kvic-state-office/review-meetings",
    
    # State Level Bankers Committee
    "slbc/agendas",
    "slbc/minutes",
    "slbc/reports",
    
    # Banks
    "banks",
    
    # Metadata & Indices
    "metadata",
    "index",
    
    # Scripts
    "scripts/download",
    "scripts/validate",
    "scripts/metadata"
]

# Add district directories
for district in districts:
    new_dirs.extend([
        f"districts/{district}/collector",
        f"districts/{district}/dic",
        f"districts/{district}/dlcc",
        f"districts/{district}/dlrc",
        f"districts/{district}/lead-bank"
    ])

# 1. Clean up old directories
print("Cleaning up old directories...")
for old_dir in old_dirs:
    path = os.path.join(repo_root, old_dir)
    if os.path.exists(path):
        print(f"Removing old directory: {old_dir}")
        shutil.rmtree(path)

# 2. Create new directory structure
print("Creating new directory structure...")
for new_dir in new_dirs:
    path = os.path.join(repo_root, new_dir)
    os.makedirs(path, exist_ok=True)
    
    # Add .gitkeep to each leaf directory to ensure Git tracks empty directories
    gitkeep_path = os.path.join(path, ".gitkeep")
    if not os.path.exists(gitkeep_path):
        with open(gitkeep_path, 'w') as f:
            pass

print("New directory structure created successfully!")
