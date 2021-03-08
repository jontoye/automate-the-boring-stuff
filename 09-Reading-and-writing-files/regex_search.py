"""Regex Search - Open all .txt files in a folder and search for 
any line that matches a user-supplied regular expression.
The results should be printed to the screen.

Usage: python regex_search.py              --> searches within current working directory 
       python regex_search.py <directory>  --> searches within <directory>
"""

from pathlib import Path
import re
import sys

# Search current working directory
if len(sys.argv) == 1:
    folder_to_search = Path(".")

# Search user-supplied directory
elif len(sys.argv) == 2:
    folder_to_search = Path(sys.argv[1])
    if not folder_to_search.is_dir():
        print(f"{sys.argv[1]} is not a directory")
        sys.exit(1)

# Obtain regular expression from user
user_string = input("Enter a regular expression: ")

# user_regex will match any line of text that contains the
# regular expression entered by the user
user_regex = re.compile(rf".*{user_string}.*[^\n]")

# Iterate over all .txt files in folder
for textfile in folder_to_search.glob("**/*.txt"):
    f = open(textfile)
    text = f.read()
    matches = user_regex.findall(text)
    for match in matches:
        print(f"In {textfile} found: {match}")
    f.close()
