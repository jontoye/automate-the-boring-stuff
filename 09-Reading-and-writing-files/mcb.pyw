#!/usr/bin/env python
"""mcb.pyw - Saves and loads pieces of text to the clipboard.

Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
       py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
       py.exe mcb.pyw list - Loads all keywords to clipboard.
       py.exe mcb.pyw delete <keyword> - Deletes keyword from shelf.
       py.exe mcb.pyw delete - Deletes all keywords"""

import shelve
import sys
import pyperclip

mcb_shelf = shelve.open("mcb")


if len(sys.argv) == 3:
    if sys.argv[1].lower() == "save":
        # Save clipboard content to keyword
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == "delete":
        # Delete keyword data
        del mcb_shelf[sys.argv[2]]

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == "delete":
        # Delete all data
        for key in mcb_shelf:
            del mcb_shelf[key]
    elif sys.argv[1].lower() == "list":
        # Copy list of keywords to clipboard
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        # Load keyword content to clipboard
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
