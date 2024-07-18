# Initialize a 2D array for the Connect 4 board
rows = 6  # Connect 4 has 6 rows
columns = 7  # Connect 4 has 7 columns
global player1_sign
global player2_sign
player1_sign = "R"
player2_sign = "A"
# Create the board as a list of lists, initially filled with empty spaces
board = [[' ' for _ in range(columns)] for _ in range(rows)]

# ANSI escape codes for colors
RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m'

# Function to print the board in a readable format with a grid
def print_board(board):
    print("  " + "   ".join(map(str, range(columns))))
    print("+---" * columns + "+")
    for row in board:
        print("| " + " | ".join([color_piece(cell) for cell in row]) + " |")
        print("+---" * columns + "+")

# Function to color the pieces
def color_piece(piece):
    if piece == player1_sign:
        return f"{RED}{piece}{RESET}"
    elif piece == player2_sign:
        return f"{BLUE}{piece}{RESET}"
    return piece

# Function to drop a piece into the board
def drop_piece(board, column, piece):
    for row in reversed(board):
        if row[column] == ' ':
            row[column] = piece
            return True
    return False

# Function to check for a win (horizontally, vertically, or diagonally)
def check_for_win(board, piece):
    # Check horizontal locations for a win
    for r in range(rows):
        for c in range(columns - 3):
            if all(board[r][c + i] == piece for i in range(4)):
                return True

    # Check vertical locations for a win
    for r in range(rows - 3):
        for c in range(columns):
            if all(board[r + i][c] == piece for i in range(4)):
                return True

    # Check positively sloped diagonals
    for r in range(rows - 3):
        for c in range(columns - 3):
            if all(board[r + i][c + i] == piece for i in range(4)):
                return True

    # Check negatively sloped diagonals
    for r in range(3, rows):
        for c in range(columns - 3):
            if all(board[r - i][c + i] == piece for i in range(4)):
                return True

    return False

# Main game loop
def play_game():
    turn = 0
    game_over = False
        
    global player1_sign
    global player2_sign

    player1_sign = str(input("Enter one character to represent player 1: "))
    player2_sign = str(input("Enter one character to represent player 2: "))
    player1_sign = player1_sign.upper()
    player1_sign = player1_sign[0]
    player2_sign = player2_sign.upper()
    player2_sign = player2_sign[0]
        
    pieces = [player1_sign, player2_sign]  # X for Player 1, O for Player 2
    print_board(board)

    while not game_over:
        # Get player input
        column = int(input(f"Player {turn % 2 + 1} ({pieces[turn % 2]}), choose a column (0-{columns - 1}): "))

        # Drop the piece in the selected column
        if drop_piece(board, column, pieces[turn % 2]):
            print_board(board)

            # Check for a win
            if check_for_win(board, pieces[turn % 2]):
                print(f"Player {turn % 2 + 1} ({pieces[turn % 2]}) wins!")
                game_over = True
            else:
                turn += 1
        else:
            print("Column full. Try again.")

# Start the game
play_game()