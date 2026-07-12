import os
import glob

# Search for any jsonl or log files in the gemini app data dir
base_dir = "/Users/amanyoonus/.gemini/antigravity-ide"
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".jsonl") or file.endswith(".log"):
            full_path = os.path.join(root, file)
            size_mb = os.path.getsize(full_path) / (1024 * 1024)
            print(f"Log file: {full_path} ({size_mb:.3f} MB)")
