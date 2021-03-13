"""
delete_unneeded.py

Write a program that walks through a folder tree and searches for files larger than 100MB. Print these files with their absolute path to the screen.

1 MB = 2^20 bytes

Usage: python delete_unneeded.py folder

arguments:
folder      the absolute or relative path of a folder to walk through
"""

import os
from pathlib import Path
import sys


def main():

    if len(sys.argv) != 2:
        print("Usage: python delete_unneeded.py folder")
        sys.exit(1)
    folder_path = Path(sys.argv[1])

    # If relative path provided, convert to absolute
    if not folder_path.is_absolute():
        folder_path = folder_path.resolve()

    # Exit program if folder does not exist
    if not folder_path.exists():
        print(f"{folder_path} does not exist")
        sys.exit(1)

    for foldername, subfolders, filenames in os.walk(folder_path):
        for file in filenames:
            file_path = Path(foldername).joinpath(file)
            if (
                not file_path.is_symlink()  # ignore paths that point to symbolic links
                and os.path.getsize(file_path) > pow(2, 20) * 100
            ):
                print(file_path)


if __name__ == "__main__":
    main()
