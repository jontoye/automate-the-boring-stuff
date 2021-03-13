"""
filling-gaps.py

Write a program that finds all files with a given prefix in a single folder and locates any gaps in the numbering. Rename all the later files to close this gap.
"""

from pathlib import Path
import re
import shutil

PREFIX = "spam"
FOLDER = Path()

number_pattern = re.compile(r"[1-9]\d*")  # Matches any number without leading zeroes

# Build array of files to be sorted and renamed
files = []
for filepath in FOLDER.iterdir():
    if filepath.name.startswith(PREFIX):
        files.append(filepath.name)

# Sort array of files and loop through each one, starting at the second array item
files = sorted(files)
for i in range(1, len(files)):

    # Obtain fileno's of current and previous file
    current_fileno = number_pattern.search(files[i]).group()
    previous_fileno = int(number_pattern.search(files[i - 1]).group())

    # If there is a gap in the numbering, rename the current file
    if int(current_fileno) != previous_fileno + 1:
        orig_filename = files[i]
        new_fileno = str(previous_fileno + 1)

        # Add leading zeros if new_fileno contains fewer digits than current_fileno
        while len(new_fileno) != len(current_fileno):
            new_fileno = "0" + new_fileno

        new_filename = orig_filename.replace(current_fileno, new_fileno)
        print(f"Renaming {orig_filename} to {new_filename}")
        shutil.move(orig_filename, new_filename)

        # Update files array
        files[i] = new_filename
