"""Asks users for their sandwich preferences"""

import pyinputplus as pyip

# Store the cost data in a dictionary
COST = {
    "bread": {"whole wheat": 1.00, "white": 0.75, "sourdough": 1.25},
    "protein": {"chicken": 3.50, "turkey": 3.25, "ham": 4.00, "tofu": 3.00},
    "cheese": {"cheddar": 1.00, "swiss": 1.25, "mozzarella": 1.25},
}


def main():
    sandwich_cost = 0.00

    print("Let's make a sandwich!\n")

    # Ask user to select type of bread and add appropriate cost to the total
    bread_type = pyip.inputMenu(
        ["whole wheat", "white", "sourdough"],
        prompt="Choose your bread\n",
        numbered=True,
    )
    sandwich_cost += COST["bread"][bread_type]

    # Ask user to select type of protein and add appropriate cost to the total
    protein_type = pyip.inputMenu(
        ["chicken", "turkey", "ham", "tofu"],
        prompt="Choose your protein\n",
        numbered=True,
    )
    sandwich_cost += COST["protein"][protein_type]

    # Ask if the user would like cheese, and if so, which kind
    cheese = pyip.inputYesNo(prompt="Would you like cheese?\n")
    if cheese == "yes":
        cheese_type = pyip.inputMenu(
            ["cheddar", "swiss", "mozzarella"],
            prompt="What kind of cheese\n",
            numbered=True,
        )
        sandwich_cost += COST["cheese"][cheese_type]

    # Additional toppings, no extra charge
    mayo = pyip.inputYesNo(prompt="Would you like mayo?\n")
    mustard = pyip.inputYesNo(prompt="Would you like mustard?\n")
    lettuce = pyip.inputYesNo(prompt="Would you like lettuce?\n")
    tomato = pyip.inputYesNo(prompt="Would you like tomato?\n")

    # Ask user how many sandwiches they would like
    num_sandwiches = pyip.inputInt(
        prompt="How many sandwiches would you like?\n", min=1
    )

    # Print out the total amount due and a thank you message
    print(f"Your total amount due: ${sandwich_cost * num_sandwiches:.2f}")
    print(f"Thanks for your order! Enjoy your {protein_type} sandwich(es)!")


if __name__ == "__main__":
    main()