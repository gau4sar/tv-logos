import os
import json

folder_path = r"C:\Users\heroi\OneDrive\Desktop\desktop4\projects\github\tv-logos\tv-logos\countries\all-countries"  # Replace with the actual path to your folder

# Get all files in the folder with a .png extension
png_files = [f for f in os.listdir(folder_path) if f.endswith(".png")]

# Create a list of dictionaries
file_entries = [{"name": png_file} for png_file in png_files]

# Write the list of dictionaries to a JSON file
with open("file_names.json", "w") as json_file:
    json.dump(file_entries, json_file, indent=2)

print(f"{len(png_files)} entries written to file_names.json")
