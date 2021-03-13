"""
selective_copy.py 

Write a program that walks through a folder tree and searches for 
files with a certain file extension. Copy these files from whatever
location they are in to a new folder.

Usage: python selective_copy.py extension folder

arguments:
extension         file extension of files to be copied
folder            destination folder name 

example:
python selective_copy.py pdf new_folder  --> copies all .pdf files into new_folder
OR
python selective_copy.py .pdf new_folder
"""

import os
from pathlib import Path
import shutil
import sys

# Set the directory this program will search through to current working directory
FOLDER = Path().cwd()


def main():

    # Check proper program usage
    if len(sys.argv) != 3:
        print("Usage: python selective_copy.py <file extension> <new folder>")
        sys.exit(1)

    # Assign command-line arguments to these variables
    file_extension = sys.argv[1]
    new_folder = sys.argv[2]

    # If new_folder doesn't already exist, create it
    if not Path(FOLDER / new_folder).exists():
        Path(FOLDER / new_folder).mkdir()

    # Add period ('.') to file extension if not provided in command-line
    if not file_extension.startswith("."):
        file_extension = "." + file_extension

    print(f"Ok, copying all {file_extension} files in:\n  {FOLDER}")

    # Walk through folder tree, copying files ending with file_extension into new_folder
    for foldername, subfolders, filenames in os.walk(FOLDER):

        # Skip new_folder
        if foldername.endswith(new_folder):
            continue

        for file in filenames:
            if file.endswith(file_extension):
                shutil.copy(
                    Path(foldername).joinpath(file),
                    FOLDER / new_folder,
                )

    print(f"Done. Files copied to:\n  {FOLDER / new_folder}")


if __name__ == "__main__":
    main()
