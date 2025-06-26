import math

# Initialize the board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to print the current board
def print_board():
    print("-------------")
    for row in board:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print("\n-------------")

# Function to check if the board is full
def is_draw():
    for row in board:
        if ' ' in row:
            return False
    return True

# Function to check for a win
def is_winner(player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Column
            return True
    if all([board[i][i] == player for i in range(3)]):  # Main diagonal
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Anti diagonal
        return True
    return False

# Minimax algorithm
def minimax(depth, is_maximizing):
    if is_winner('O'):
        return 1
    if is_winner('X'):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# Find the best move for AI
def find_best_move():
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X' and AI is 'O'")
    print_board()

    while True:
        # Human move
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    break
                else:
                    print("Cell already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter numbers between 0 and 2.")

        print_board()

        if is_winner('X'):
            print("You win! 🎉")
            break
        if is_draw():
            print("It's a draw!")
            break

        # AI move
        print("AI is thinking...")
        ai_move = find_best_move()
        board[ai_move[0]][ai_move[1]] = 'O'

        print_board()

        if is_winner('O'):
            print("AI wins! 😢")
            break
        if is_draw():
            print("It's a draw!")
            break

# Start the game
play_game()
