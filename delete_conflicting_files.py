#!/usr/bin/env python
import os
import glob

# List of files to delete
files_to_delete = [
    "havo-ifloslanishi.html",
    "o'rmonlar-kesilishi.html", 
    "plastik-ifloslanish.html",
    "suv-ifloslanishi.html",
    "yovvyi-tabiat.html",
]

# Files that are conflicting with Django's auth templates
html_files_to_remove = [
    "login.html",
    "register.html",
]

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Delete the specific files
for filename in files_to_delete + html_files_to_remove:
    filepath = os.path.join(".", filename)
    if os.path.exists(filepath):
        try:
            os.remove(filepath)
            print(f"✓ Deleted: {filename}")
        except Exception as e:
            print(f"✗ Failed to delete {filename}: {e}")
    else:
        print(f"- File not found: {filename}")

print("\nDone! Conflicting files have been removed.")
