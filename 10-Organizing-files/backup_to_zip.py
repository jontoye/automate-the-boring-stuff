"""backup_to_zip.py - Copies an entire folder and its contents into
a zip file whose filename increments with each new save."""

import os
from pathlib import Path
import zipfile


def main():
    # Backup current working directory
    backup_to_zip(Path().cwd())


def backup_to_zip(folder):
    """Back up the entire contents of 'folder' into a ZIP file."""

    folder = Path(folder).resolve()  # make sure folder is absolute

    # Figure out the filename this code should use based on
    # what files already exist
    number = 1
    while True:
        zip_filename = f"{folder.name}_{number}.zip"
        if not Path(zip_filename).exists():
            break
        number += 1

    # Create the ZIP file
    print(f"Creating {zip_filename}...")
    backup_zip = zipfile.ZipFile(zip_filename, "w")

    # Walk the entire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print(f"Adding files in {foldername}...")

        # Add the current folder to the ZIP file
        backup_zip.write(foldername)

        # Add all the files in this folder to the ZIP file
        for filename in filenames:
            new_base = folder.name + "_"
            if filename.startswith(new_base) and filename.endswith(".zip"):
                continue
            backup_zip.write(Path(foldername).joinpath(filename))

    backup_zip.close()
    print("Done.")


if __name__ == "__main__":
    main()