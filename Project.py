# START

# Stage 1

def init_board():
    """
    Builds a fresh 3x3 board of empty squares and returns it.
    """
    return [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]


def print_board(board):
    """
    Prints the board row by row with clean separators.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


# Stage 2.1 + 2.2

def get_move(board, mark):
    """
    Asks the player for a square (1-9), validates it,
    and directly writes the mark to the board once a valid empty square is found.
    """
    while True:
        try:
            choice = input(f"Player {mark}, choose a square (1-9): ")
            move = int(choice)

            if move < 1 or move > 9:
                print("Number out of range! Please choose between 1 and 9.")
                continue

            row = (move - 1) // 3
            col = (move - 1) % 3

            if board[row][col] != " ":
                print("This square is already taken! Choose another one.")
                continue

            board[row][col] = mark
            return

        except ValueError:
            print("Invalid input! Please enter numbers only.")


# Stage 2.3 + 2.4

def check_winner(board, mark):
    """
    Checks the status of the game.
    First, checks if the current mark won
    If not, checks if the board is full resulting in a draw
    Returns "win", "draw", or None if the game continues.
    """

    lines = [
        # 3 Rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # 3 Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # 2 Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]

    target = [mark, mark, mark]
    if target in lines:
        return "win"

    for row in board:
        if " " in row:
            return None

    return "draw"
