# Rock, paper, scissors game

import random, sys

print("ROCK, PAPER, SCISSORS")

# Variables to track wins, losses, ties
wins = 0
losses = 0
ties = 0

# main game loop
while True:
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    while True: # Player input loop
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        player_move = input()
        if player_move == 'q':
            sys.exit() # Quit game
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break # Break out of player input loop
        print("Type one of r, p, s, or q")

    # Display player's move
    if player_move == 'r':
        print("ROCK versus...")
    elif player_move == 'p':
        print("PAPER versus...")
    elif player_move == 's':
        print("SCISSORS versus...")

    # Display computer's move
    computer_move = random.choice(['r', 'p', 's'])
    if computer_move == 'r':
        print("ROCK")
    elif computer_move == 'p':
        print("PAPER")
    elif computer_move == 's':
        print("SCISSORS")

    # Determine winner, display and record outcome
    if player_move == computer_move:
        print("It's a tie!")
        ties += 1
    elif player_move == 'r':
        if computer_move == 's':
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1
    elif player_move == 'p':
        if computer_move == 'r':
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1
    elif player_move == 's':
        if computer_move == 'p':
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1


    



