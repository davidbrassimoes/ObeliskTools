import os
import shutil
import sys

def rename_files_safe(directory, new_name):
    file_list = os.listdir(directory)
    out_directory = os.path.join(directory, "out")
    os.makedirs(out_directory, exist_ok=True)

    for i, file_name in enumerate(file_list):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):  # Check if it's a file
            file_extension = os.path.splitext(file_name)[1]
            new_file_name = f"{new_name}{i+1}{file_extension}"
            new_file_path = os.path.join(out_directory, new_file_name)
            shutil.copy(file_path, new_file_path)

def rename_files(directory, new_name):
    file_list = os.listdir(directory)
    for i, file_name in enumerate(file_list):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):  # Check if it's a file
            file_extension = os.path.splitext(file_name)[1]
            new_file_name = f"{new_name}{i+1}{file_extension}"
            new_file_path = os.path.join(directory, new_file_name)
            os.rename(file_path, new_file_path)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python rename.py <backup> <directory> <new_name>")
        sys.exit(1)

    backup = sys.argv[1]
    directory = sys.argv[2]
    new_name = sys.argv[3]

    if backup.lower() == "y":
        rename_files_safe(directory, new_name)
    elif backup.lower() == "n":
        rename_files(directory, new_name)
    else:
        print("Invalid backup option. Please enter either 'y' or 'n'.")
        sys.exit(1)
