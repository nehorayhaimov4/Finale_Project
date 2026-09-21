# START

# Stage 1

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def print_board(board):
    """
    Prints the current state of the board in a clean grid format.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Stage 2.1

def get_valid_move(board, player):
    """
    Prompts the player for a move between 1-9, validates the input,
    and returns the corresponding row and column indices.
    """
    while True:
        try:
            choice = input(f"Player {player}, choose a square (1-9): ")
            move = int(choice)

            if move < 1 or move > 9:
                print("Invalid range! Please choose a number between 1 and 9.")
                continue

            row = (move - 1) // 3
            col = (move - 1) % 3

            if board[row][col] != " ":
                print("This square is already taken! Choose another one.")
                continue

            return row, col

        except ValueError:
            print("Invalid input! Please enter numbers only.")

# Stage


