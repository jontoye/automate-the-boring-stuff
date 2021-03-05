""" Chess Board Validator"""
# Checks wheter a given chess board is valid (correct squares and pieces)
# Does not check if pieces are located on valid locations within a game

# This dict stores all valid pieces with their current count, and max number allowed
piece_count = {
    "bking": {"cur": 0, "max": 1},
    "bqueen": {"cur": 0, "max": 1},
    "brook": {"cur": 0, "max": 2},
    "bknight": {"cur": 0, "max": 2},
    "bbishop": {"cur": 0, "max": 2},
    "bpawn": {"cur": 0, "max": 8},
    "wking": {"cur": 0, "max": 1},
    "wqueen": {"cur": 0, "max": 1},
    "wrook": {"cur": 0, "max": 2},
    "wknight": {"cur": 0, "max": 2},
    "wbishop": {"cur": 0, "max": 2},
    "wpawn": {"cur": 0, "max": 8},
}


def main():
    board = {
        "1h": "bking",
        "6c": "wqueen",
        "2g": "bbishop",
        "5h": "bqueen",
        "3e": "wking",
        "4d": "bbishop",
    }

    if is_valid_chess_board(board):
        print("This is a valid chess board")
    else:
        print("This is not a valid chess board")


def is_valid_chess_board(board):
    # A list to store taken squares
    taken_squares = []

    # Loop through each key, value pair in board dict
    for square, piece in board.items():
        # Check if square is valid:
        if square[0] not in "12345678" or square[1] not in "abcdefgh":
            return False

        # Check if square is already occupied
        if square in taken_squares:
            return False
        else:
            taken_squares.append(square)

        # Update piece_count and check that max has not been exceeded
        piece_count[piece]["cur"] += 1
        if piece_count[piece]["cur"] > piece_count[piece]["max"]:
            return False

    # Check that each player has extactly one king
    if piece_count["wking"]["cur"] != 1 or piece_count["bking"]["cur"] != 1:
        return False

    # If all tests pass, the board is valid
    return True


if __name__ == "__main__":
    main()