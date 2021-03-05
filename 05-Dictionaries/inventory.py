"""Fantasy Game Inventory"""
import time


def main():
    stuff = {
        "rope": 1,
        "torch": 6,
        "gold coin": 42,
        "dagger": 1,
        "arrow": 12,
        "hammer": 1,
        "potion": 3,
    }
    dragon_loot = ["gold coin", "dagger", "bread", "gold coin", "ruby", "ruby", "beer"]

    display_inventory(stuff)
    inv = add_to_inventory(stuff, dragon_loot)
    display_inventory(inv)


def display_inventory(inventory):
    """Prints out the inventory dict to the screen"""
    print("Inventory:")
    num_items = 0

    for k, v in inventory.items():
        print(f"{v} {k}")
        num_items += v

    print(f"Total number of items: {num_items}")
    print()


def add_to_inventory(inventory, loot_items):
    """Adds a list of items to an inventory dict"""
    for item in loot_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1

    return inventory


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Time elapsed: {end - start:f} seconds")