game_board = {
    "top-L": " ",
    "top-M": " ",
    "top-R": " ",
    "mid-L": " ",
    "mid-M": " ",
    "mid-R": " ",
    "bot-L": " ",
    "bot-M": " ",
    "bot-R": " ",
}


def main():
    display_board(game_board)
    player = "X"
    for i in range(9):
        print(f"Turn for {player}. Move on which space?")
        move = input()
        game_board[move] = player
        if player == "X":
            player = "O"
        else:
            player = "X"
        display_board(game_board)


def display_board(board):
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")
    print(board["bot-L"] + "|" + board["bot-M"] + "|" + board["bot-R"])


if __name__ == "__main__":
    main()
