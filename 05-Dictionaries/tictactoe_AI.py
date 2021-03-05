# Tic Tac Toe with AI

import random

# --------------------------- MAIN ------------------------------
def main():

    print("Welcome to Tic Tac Toe!")

    while True:
        # Reset the board
        game_board = [" "] * 10
        player_letter, computer_letter = input_player_letter()
        turn = who_goes_first()
        print(f"The {turn} will go first.")
        game_is_playing = True

        while game_is_playing:
            if turn == "player":
                # Player's turn.
                draw_board(game_board)
                move = get_player_move(game_board)
                make_move(game_board, player_letter, move)

                if is_winner(game_board, player_letter):
                    draw_board(game_board)
                    print("Hooray! You have won the game!")
                    game_is_playing = False
                else:
                    if is_board_full(game_board):
                        print("The game is a tie!")
                        break
                    else:
                        turn = "computer"

            else:
                # Computer's turn.
                move = get_computer_move(game_board, computer_letter)
                make_move(game_board, computer_letter, move)

                if is_winner(game_board, computer_letter):
                    draw_board(game_board)
                    print("The computer has beaten you! You lose.")
                    game_is_playing = False
                else:
                    if is_board_full(game_board):
                        draw_board(game_board)
                        print("The game is a tie!")
                        break
                    else:
                        turn = "player"

        if not play_again():
            break


# -------------------------- FUNCTIONS ---------------------------
def draw_board(board):
    """Prints out the board to screen;
    'board' is a list of 10 strings representing the board (ignore index 0)"""
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[1] + "|" + board[2] + "|" + board[3])


def input_player_letter():
    """Lets the player type which letter they want to be;
    Returns a list with the player's letter as first item, computer's as second"""
    letter = ""
    while not (letter == "X" or letter == "O"):
        print("Do you want to be X or O?")
        letter = input().upper()
    if letter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]


def who_goes_first():
    """Randomly choose the player who goes first"""
    if random.randint(0, 1) == 0:
        return "computer"
    else:
        return "player"


def play_again():
    """Returns True if player chooses to play again, otherwise returns False"""
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")


def make_move(board, letter, move):
    board[move] = letter


def is_winner(b, l):
    """Returns True if the player whose letter was passed has won the game"""
    return (
        (b[7] == l and b[8] == l and b[9] == l)  # top row
        or (b[4] == l and b[5] == l and b[6] == l)  # middle row
        or (b[1] == l and b[2] == l and b[3] == l)  # bot row
        or (b[7] == l and b[4] == l and b[1] == l)  # left col
        or (b[8] == l and b[5] == l and b[2] == l)  # middle col
        or (b[9] == l and b[6] == l and b[3] == l)  # right col
        or (b[7] == l and b[5] == l and b[3] == l)  # diagonal 1
        or (b[9] == l and b[5] == l and b[1] == l)  # diagonal 2
    )


def get_board_copy(board):
    """Make a duplicate of the board list for use in AI simulations"""
    dupe_board = []

    for i in board:
        dupe_board.append(i)

    return dupe_board


def is_space_free(board, move):
    """Return True if 'move' is empty on 'board'"""
    return board[move] == " "


def get_player_move(board):
    """Let the player type in their move."""
    move = " "
    while move not in "1 2 3 4 5 6 7 8 9".split() or not is_space_free(
        board, int(move)
    ):
        print("What is your next move? (1-9)")
        move = input()
    return int(move)


def choose_random_move_from_list(board, moves_list):
    """Returns a valid move from the passed list; Returns None if no valid move"""
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computer_letter):
    """Determine computer's move and return that move"""
    if computer_letter == "X":
        player_letter = "O"
    else:
        player_letter = "X"

    # -------------- Algorithm for Tic Tac Toe AI --------------
    # First, check if we can win in next move
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, computer_letter, i)
            if is_winner(copy, computer_letter):
                return i
    # Check if the player could win on next move, and block them
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, player_letter, i)
            if is_winner(copy, player_letter):
                return i
    # Try to take one of the corners, if they are free
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move != None:
        return move
    # Try to take the center
    if is_space_free(board, 5):
        return 5
    # Move on one of the side spaces
    return choose_random_move_from_list(board, [2, 4, 6, 8])


def is_board_full(board):
    """Return True if every space on the board has been taken; otherwise return False"""
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


if __name__ == "__main__":
    main()