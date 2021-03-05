"""English to Pit Latin Translator"""

print("Enter the English message to translate into Pig Latin: ")
message = input()

VOWELS = ("a", "e", "i", "o", "u", "y")

# A list of the words in Pig Latin
pig_latin = []

for word in message.split():

    # Seperate the non-letters at the start of this word
    prefix_non_letters = ""
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letters += word[0]
        word = word[1:]
    if len(word) == 0:
        pig_latin.append(prefix_non_letters)
        continue

    # Seperate the non-letters at the end of this word
    suffix_non_letters = ""
    while not word[-1].isalpha():
        suffix_non_letters += word[-1]
        word = word[:-1]

    # Remember if the word was in uppercase or title case
    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower()  # Make the word lowercase for translation

    # Separate the consonants at the start of this word
    prefix_consonants = ""
    while len(word) > 0 and not word[0] in VOWELS:
        prefix_consonants += word[0]
        word = word[1:]

    # Add the pig latin ending to the word
    if prefix_consonants != "":
        word += prefix_consonants + "ay"
    else:
        word += "yay"

    # Convert word back to its original case
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()

    # Add the non-letters back to the start or end of the word
    pig_latin.append(prefix_non_letters + word + suffix_non_letters)

# Join all the words back together into a single string
print(" ".join(pig_latin))