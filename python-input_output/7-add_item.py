#!/usr/bin/python3
"""
Script that adds arguments to a Python list and saves them to a JSON file.
"""

import sys
import os

# Import your own functions from previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing list if file exists, else start with empty list
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add all new command-line arguments (skip the script name)
items.extend(sys.argv[1:])

# Save updated list to JSON file
save_to_json_file(items, filename)
