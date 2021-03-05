"""Takes a list of strings and displays it in a well organized table
with each column right-justified"""

table_data = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]


def print_table(table):
    # Create list containing column widths
    col_widths = [0] * len(table)

    # Store widths of each lists' longest string
    for i, word_list in enumerate(table):
        col_widths[i] = len(max(word_list, key=len))

    # Print each row of table using col_width for justification
    for row in range(len(table[0])):
        for col in range(len(table)):
            print(table[col][row].rjust(col_widths[col]), end=" ")
        print()


print_table(table_data)
