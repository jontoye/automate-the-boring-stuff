"""Regex version of the strip() method"""

import re


def main():

    print("Test example results:")
    # Tests for one argument
    regex_strip("      strip this     ")
    regex_strip("             AND this...        ")
    regex_strip("maybe this?")

    # Tests for two arguments
    regex_strip("xxxxxxHello Worldxxxxxxxx", "x")
    regex_strip("abbbccaabcDo you know your abc's?abcabcabbbccc", "abc")
    regex_strip("101000119984674636630001111010", "01")

    # Allow user to enter a string and characters to be stripped
    print()
    string = input("Enter a string to be stripped: ")
    chars = input(
        "Enter characters to be stripped, or press Enter to strip whitespace: "
    )
    regex_strip(string, chars)


def regex_strip(string, chars=""):
    """Removes leading and trailing characters from a string. Default characters are whitespace"""
    # If no chars argument provided, remove whitespace
    if chars == "":
        match = re.search(r"\S+.*\S+", string)
        if match:
            print(match.group())

    # If chars argument provided, remove these characters from beginning and end of string
    else:
        match = re.search(rf"[^{chars}].*[^{chars}]", string)
        if match:
            print(match.group())


if __name__ == "__main__":
    main()