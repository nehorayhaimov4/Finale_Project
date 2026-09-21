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
    # 1. Check Rows
    for row in board:
        if all(cell == mark for cell in row):
            return True

    # 2. Check Columns
    for col in range(3):
        if all(board[row][col] == mark for row in range(3)):
            return True

    # 3. Check Diagonals
    if all(board[i][i] == mark for i in range(3)):
        return True
    if all(board[i][2 - i] == mark for i in range(3)):
        return True

    return False
# Stage 3.4: Check if the board is full
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