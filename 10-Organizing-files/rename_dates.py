"""rename_dates.py - Renames filenames with American MM-DD-YYY date formate
to European DD-MM-YYY."""

import os
import re
import shutil


# Create a regex that matches files with the American date formate.
date_pattern = re.compile(
    r"""^(.*?)          # all text before the date
    ((0|1)?\d)-         # one or two digits for the month
    ((0|1|2|3)?\d)-     # on or two digits for the day
    ((19|20)\d\d)       # four digits for the year
    (.*?)$              # all text after the date
    """,
    re.VERBOSE,
)

# Loop over the files in the working directory
for amer_filename in os.listdir("."):
    match = date_pattern.search(amer_filename)

    # Skip files without a date
    if match == None:
        continue

    # Get the different parts of the filename
    before_part = match.group(1)
    month_part = match.group(2)
    day_part = match.group(4)
    year_part = match.group(6)
    after_part = match.group(8)

    # Form the European-style filename
    euro_filename = f"{before_part}{day_part}-{month_part}-{year_part}{after_part}"
    print(f"Renaming '{amer_filename}' to '{euro_filename}'...")

    # Get the full, absolute file paths
    abs_working_dir = os.path.abspath(".")
    amer_filename = os.path.join(abs_working_dir, amer_filename)
    euro_filename = os.path.join(abs_working_dir, euro_filename)

    # Rename the files
    shutil.move(amer_filename, euro_filename)