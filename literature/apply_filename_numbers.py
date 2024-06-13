import os
import shutil
import json
import re

invalid_file_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*', '\'']

def get_valid_filename(name):
    for char in invalid_file_chars:
        name = name.replace(char, "")
    return name

original_folder = "annotated"
destination_folder = "../abgabe/literatur"

json_file_path = "rename_map.json"

os.makedirs(destination_folder, exist_ok=True)

# if result folder is not empty, delete all files
for file in os.listdir(destination_folder):
    file_path = os.path.join(destination_folder, file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)

with open(json_file_path, 'r', encoding='utf-8') as file:
    rename_map = json.load(file)

# copy/rename files from original folder to destination folder
for original_name, new_name in rename_map.items():
    original_path = os.path.join(original_folder, original_name)
    destination_path = os.path.join(destination_folder, get_valid_filename(new_name))
    if os.path.exists(original_path):
        shutil.copy2(original_path, destination_path)
    else:
        print(f"File not found: {original_name} --> {new_name}")

# Sanity check
pattern = re.compile(r'\[(\d+)\]')
numbers = []

for file in os.listdir(destination_folder):
    match = pattern.search(file)
    if match:
        numbers.append(int(match.group(1)))

if numbers:
    max_number = max(numbers)
    missing_numbers = [num for num in range(1, max_number + 1) if num not in numbers]
    if missing_numbers:
        print(f"Missing numbers: {missing_numbers}")
    else:
        print("No numbers are missing.")
else:
    print("No valid numbers found in filenames.")
