"""Mad Libs - Reads in a text file from the command-line and lets the 
user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or 
VERB appears.

Usage: python madlibs.py <file>
"""

import re
import sys

# Check command-line arguments
if len(sys.argv) != 2:
    print("Usage: python madlibs.py <file>")
    sys.exit(1)

# Create a regex object that matches the blanks to be filled in
blanks = re.compile(r"ADJECTIVE|NOUN|VERB|ADVERB")

# Read the text of the file into a string
with open(sys.argv[1]) as file:
    text = file.read()

# Loop through each blank found in the text
for blank in blanks.findall(text):
    if blank.lower() in ["adjective", "adverb"]:
        article = "an"
    else:
        article = "a"

    # Obtain a word from the user, and insert into blank
    user_word = input(f"Enter {article} {blank.lower()}:\n")
    text = text.replace(blank, user_word, 1)

# Display filled in text
print(text)
