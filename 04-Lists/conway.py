# Conway's Game of Life

# If a living square has 2 or 3 living neighbors, it continues to live
# If a dead square has 3 living neighbors, it comes alive on next step
# Every other square dies or remains dead

import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create a list of lists for the cells
next_cells = []
for x in range(WIDTH):
    column = [] # create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append("#") # add a living cell
        else:
            column.append(" ") # add a dead cell
    next_cells.append(column)

# Main program loop
while True:
    print("\n\n\n\n\n")
    current_cells = copy.deepcopy(next_cells)

    # Print current_cells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end='')
        print()

    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates
            # '% WIDTH' ensures left_coord is always between 0 and WIDTH - 1
            left_coord = (x - 1) % WIDTH
            right_coord = (x + 1) % WIDTH
            above_coord = (y - 1) % HEIGHT
            below_coord = (y + 1) % HEIGHT

            # Count number of living neighbors
            num_neighbors = 0
            if current_cells[left_coord][above_coord] == '#':
                num_neighbors += 1 # Top-left neighbor is alive
            if current_cells[x][above_coord] == '#':
                num_neighbors += 1 # Top neighbor is alive
            if current_cells[right_coord][above_coord] == '#':
                num_neighbors += 1 # Top-right neighbor is alive
            if current_cells[left_coord][y] == '#':
                num_neighbors += 1 # Left neighbor is alive
            if current_cells[right_coord][y] == '#':
                num_neighbors += 1 # Right neighbor is alive
            if current_cells[left_coord][below_coord] == '#':
                num_neighbors += 1 # Bottom-left neighbor is alive
            if current_cells[x][below_coord] == '#':
                num_neighbors += 1 # Bottom neighbor is alive
            if current_cells[right_coord][below_coord] == '#':
                num_neighbors += 1 # Bottom-right neighbor is alive

            # Set cell based on Conway's Game of Life rule
            if current_cells[x][y] == '#' and (num_neighbors == 2 or num_neighbors == 3):
                next_cells[x][y] = '#'
            elif current_cells[x][y] == ' ' and num_neighbors == 3:
                next_cells[x][y] = '#'
            else:
                next_cells[x][y] = ' '
    
    time.sleep(1) # Add a 1 second pause to reduce flickering           

