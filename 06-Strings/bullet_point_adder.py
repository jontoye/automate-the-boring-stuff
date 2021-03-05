#!/usr/bin/env python
"""bullet_point_adder.py - Adds Wikipedia bullet points to the start 
of each line of text on the clipboard."""

import pyperclip

text = pyperclip.paste()

# Seperate lines and add stars
lines = text.split("\n")
for i, line in enumerate(lines):
    lines[i] = "*" + line
text = "\n".join(lines)


pyperclip.copy(text)
