"""Date Detection - write a regular expression that can detect dates
in the DD/MM/YYYY format. Then checks if date is valid"""

import re

# Date regex to match dates in DD/MM/YYYY format
date_regex = re.compile(
    r"""([0-2][0-9]|3[0-1])     # DD between 01 and 31
        /                       # /
        (0[1-9]|1[0-2])         # MM between 01 and 12
        /                       # /
        ([1-2][0-9]+)           # YYYY between 1000 and 2999
    """,
    re.VERBOSE,
)

# Text to search
text = [
    "This is the text that will be searched through.",
    "Dates such as 01/01/2021 should be detected by the regex.",
    "Invalid formats such as 01-01-2021 will not be detected.",
    "Out of range values such as 33/13/3333 or 21/14/1999 will also not be detected.",
    "Once all dates with valid formats have been detected, the program will check whether each date actually exists",
    "List of dates:",
    "01/01/1000",
    "31/04/2000",
    "31/05/2000",
    "30/02/1999",
    "29/02/2000",
    "29/02/2020",
    "29/02/2021",
    "29/02/2100",
]


def main():

    print("Matches found: ")
    for groups in date_regex.findall("\n".join(text)):
        day = groups[0]
        month = groups[1]
        year = groups[2]
        print(f"{day}/{month}/{year}  <-- ", end="")
        if date_exists(day, month, year):
            print("valid")
        else:
            print("DOES NOT EXIST")


def date_exists(day, month, year):
    """Returns True if date exists, False otherwise."""
    # Convert strings to integers
    day = int(day)
    month = int(month)
    year = int(year)

    # If month is in Apr, Jun, Sep, Nov check that num of days does not exceed 30
    if month in [4, 6, 9, 11] and day > 30:
        return False

    # If month is Feb, check if leap year to determine num of days
    if month == 2:
        if year % 400 == 0:  # Leap year
            return day <= 29
        else:
            if year % 100 == 0:  # Not a leap year
                return day <= 28
            elif year % 4 == 0:  # Leap year
                return day <= 29
            else:  # Not a leap year
                return day <= 28

    # Month is in Jan, Mar, May, Jul, Aug, Oct, Dec so is allowed 31 days
    return True


if __name__ == "__main__":
    main()