# CodTech Task 1 - Automated File Organizer
# Intern ID: CITS9786
import os
import shutil
def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isdir(file_path):
            continue
        ext = filename.split('.')[-1].lower() if '.' in filename else "others"
        ext_folder = os.path.join(folder_path, ext)
        if not os.path.exists(ext_folder):
            os.mkdir(ext_folder)
        shutil.move(file_path, os.path.join(ext_folder, filename))
        print(f"Moved {filename} -> {ext}/")
folder = input("Enter folder path: ")
organize_files(folder)
print("Task 1 Completed - CITS9786")
