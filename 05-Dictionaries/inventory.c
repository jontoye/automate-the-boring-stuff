#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

#define SIZE(obj) sizeof(obj) / sizeof(obj[0])

typedef struct
{
    char *name;
    int count;
} Item;

int num_distinct_items = 0;
double start, end;

Item *add_to_inventory(Item *inventory, char *items[], size_t n_items);
void display_inventory(Item *inventory, size_t n);

int main(void)
{
    start = clock();

    // Initial inventory array
    Item stuff[] = {{"rope", 1}, {"torch", 6}, {"gold coin", 42}, {"dagger", 1}, {"arrow", 12}, {"hammer", 1}, {"potion", 3}};

    // Set num_distinct_items
    num_distinct_items = SIZE(stuff);

    // New items to be added
    char *dragon_loot[] = {"gold coin", "dagger", "bread", "gold coin", "ruby", "ruby", "beer"};

    // Display initial inventory list
    display_inventory(stuff, num_distinct_items);

    // Create new inventory list with new items added
    Item *new_stuff = add_to_inventory(stuff, dragon_loot, SIZE(dragon_loot));

    // Display new inventory list
    display_inventory(new_stuff, num_distinct_items);

    // Free memory allocated for new array
    free(new_stuff);

    end = clock();
    printf("Time elapsed: %f seconds\n", (end - start) / CLOCKS_PER_SEC);
    exit(EXIT_SUCCESS);
}

void display_inventory(Item *inventory, size_t n)
{
    int total_items = 0;
    Item *p = inventory;
    printf("Inventory:\n");

    for (p = inventory; p < inventory + n; p++)
    {
        printf("%d %s\n", p->count, p->name);
        total_items += p->count;
    }

    printf("Total number of items: %d\n\n", total_items);
}

Item *add_to_inventory(Item *inventory, char *items[], size_t n_items)
{
    int i;
    bool item_exists;
    Item *new_inventory;
    Item *new_p, *p;

    // Allocate memory for new array
    new_inventory = malloc(num_distinct_items * sizeof(Item));
    if (new_inventory == NULL)
    {
        printf("Error allocating space for new_inventory.\n");
        exit(EXIT_SUCCESS);
    }

    // Copy inventory array into new_inventory
    for (p = inventory, new_p = new_inventory;
         p < inventory + num_distinct_items;
         p++, new_p++)
    {
        new_p->count = p->count;
        new_p->name = p->name;
    }

    // Loop through each item in list of items to be added
    for (i = 0; i < n_items; i++)
    {
        item_exists = false;

        // Loop through inventory array
        for (new_p = new_inventory; new_p < new_inventory + num_distinct_items; new_p++)
        {

            // Compare item to be added with each existing item in the inventory
            if (strcmp(items[i], new_p->name) == 0)
            {
                item_exists = true;
                new_p->count += 1;
            }
        }

        // If item does not exist, add it to the inventory
        if (!item_exists)
        {
            // Resize the memory block of new_inventory
            new_inventory = realloc(new_inventory, num_distinct_items * sizeof(Item) + sizeof(Item));

            // Add new item
            new_inventory[num_distinct_items].name = items[i];
            new_inventory[num_distinct_items].count = 1;

            // Increment num_distinct_items
            num_distinct_items += 1;
        }
    }
    return new_inventory;
}