"""Strong Password Detection"""

import re

program_description = """
Strong Password Detection Program

A strong password has the following properties:
    --> at least 8 characters long
    --> contains both uppercase and lowercase characters
    --> has at least one digit
    
This program will prompt you to enter a password, then tell you
whether it meets the above criteria or not."""

# Length regex
length_regex = re.compile(r".{8,}")

# Case regex
case_regex = re.compile(r".*[A-Z]+.*[a-z]+.*|.*[a-z]+.*[A-Z]+.*")

# Digit regex
digit_regex = re.compile(r".*\d.*")


def main():
    print(program_description)

    input("Press enter to begin...")

    while True:
        print("Enter a password")
        password = input("> ")

        # Get match objects, these will be None type if match not found
        length_match = length_regex.match(password)
        case_match = case_regex.match(password)
        digit_match = digit_regex.match(password)

        # If all match objects exist, the password meets requirements
        if length_match and case_match and digit_match:
            print("That is a strong password. Nice!")
            break
        # If any of the matches failed, user will be prompted to enter new password
        else:
            print("Password not strong enough. Try again.")


if __name__ == "__main__":
    main()
