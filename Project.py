# START

# Stage 1: Creating the board
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


# Stage 2.1 + 2.2 + 3.1 + 3.2: Game turn
def get_move(board, mark):
    """
    Asks the player for a square (1-9), validates the input,
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


# Stage 2.3 + 2.4 + 3.3: Check who win
def check_winner(board, mark):
    """
    Checks all 8 possible lines. Returns True if the mark won, otherwise False.
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
    return target in lines


# Step 3.4: Check if the board is full
def is_board_full(board):
    """
    Returns True if every square on the board is already taken.
    """
    for row in board:
        if " " in row:
            return False
    return True


# Play again?
def ask_play_again():
    """
    Asks "play again?", returns True or False.
    """
    while True:
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice in ['yes']:
            return True
        if choice in ['no']:
            return False
        print("Invalid input! Please type 'yes' or 'no'.")


# Play
def play_round():
    board = init_board()
    print_board(board)

    while True:
        # Player X Turn
        get_move(board, "X")
        print_board(board)

        if check_winner(board, "X") == "win" or check_winner(board, "X") is True:
            print("Player X wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        # Player O Turn
        get_move(board, "O")
        print_board(board)

        if check_winner(board, "O") == "win" or check_winner(board, "O") is True:
            print("Player O wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break


# Main
while True:
    play_round()
    if not ask_play_again():
        print("Thanks for playing!")
        break

# STOP