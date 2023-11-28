import os
import shutil

backup = input("Do you want to keep your files and make new ones? (y/n): ")
while backup.lower() not in ['y', 'n']:
    backup = input("Please enter either 'y' or 'n': ")

def rename_files_safe():
    directory = input("Enter the directory path: ")
    new_name = input("Enter the new name: ")

    file_list = os.listdir(directory)
    out_directory = os.path.join(directory, "out")
    os.makedirs(out_directory, exist_ok=True)

    for i, file_name in enumerate(file_list):
        file_path = os.path.join(directory, file_name)
        file_extension = os.path.splitext(file_name)[1]
        new_file_name = f"{new_name}{i+1}{file_extension}"
        new_file_path = os.path.join(out_directory, new_file_name)
        shutil.copy(file_path, new_file_path)

def rename_files():
    directory = input("Enter the directory path: ")
    new_name = input("Enter the new name: ")

    file_list = os.listdir(directory)
    for i, file_name in enumerate(file_list):
        file_path = os.path.join(directory, file_name)
        file_extension = os.path.splitext(file_name)[1]
        new_file_name = f"{new_name}{i+1}{file_extension}"
        new_file_path = os.path.join(directory, new_file_name)
        os.rename(file_path, new_file_path)

if backup.lower() == "y":
    rename_files_safe()
elif backup.lower() == "n":
    rename_files()