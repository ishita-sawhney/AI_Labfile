import os

# Initialize the board
board = {
    1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "
}
game_on = True
turn = "p1"
# Initialize scores
p1_score = 0
p2_score = 0

def print_board():
    print("")
    print(f"  {board[7]} |  {board[8]}  | {board[9]}")
    print("---------------")
    print(f"  {board[4]} |  {board[5]}  | {board[6]}")
    print("---------------")
    print(f"  {board[1]} |  {board[2]}  | {board[3]}")
    print("")
    print("")

# Function to set player symbols
def set_player():
    p1 = ""
    while p1 != "X" and p1 != "O":
        p1 = input("Player 1: Choose 'X' or 'O' and type it down on the "
                   "keyboard: ")
        if p1 == "X":
            p2 = "O"
        elif p1 == "O":
            p2 = "X"
    print("Ready! \n \nPlayer 1 =", p1, ", Player 2 =", p2)
    return p1, p2

# Function to handle player turns
def players_turn(p1, p2, turn):
    valid_position = False
    while valid_position is False:
        if turn == "p1":
            pos = int(input("Player 1: It's your turn. "
                            "Choose the position to play (1-9): "))
            valid_position = validate_open_position_on_board(board, pos)
            if valid_position:
                board[pos] = p1
                turn = "p2"
        else:
            pos = int(input("Player 2: It's your turn. "
                            "Choose the position to play (1-9): "))
            valid_position = validate_open_position_on_board(board, pos)
            if valid_position:
                board[pos] = p2
                turn = "p1"
    return board, turn

# Function to validate if someone has won
def validate_win(board):
    # Horizontal validation
    if (((board[7] == board[8] and board[8] == board[9]) and
        (board[7] == "X" or board[7] == "O")) or
        ((board[4] == board[5] and board[5] == board[6]) and
        (board[4] == "X" or board[4] == "O")) or
        ((board[1] == board[2] and board[2] == board[3]) and
       (board[2] == "X" or board[2] == "O"))):
        horizontal_validation = True
    else:
        horizontal_validation = False

    # Vertical validation
    if (((board[7] == board[4] and board[4] == board[1]) and
        (board[7] == "X" or board[7] == "O")) or
        ((board[8] == board[5] and board[5] == board[2]) and
        (board[8] == "X" or board[8] == "O")) or
        ((board[9] == board[6] and board[6] == board[3]) and
       (board[9] == "X" or board[9] == "O"))):
        vertical_validation = True
    else:
        vertical_validation = False

    # Diagonal validation
    if (((board[7] == board[5] and board[5] == board[3]) and
        (board[7] == "X" or board[7] == "O")) or
        ((board[1] == board[5] and board[5] == board[9]) and
       (board[1] == "X" or board[1] == "O"))):
        diagonal_validation = True
    else:
        diagonal_validation = False

    return horizontal_validation or vertical_validation or diagonal_validation

# Function to validate if the game is a tie
def validate_tie(board):
    return " " not in board.values()

# Function to validate if a position is open
def validate_open_position_on_board(board, pos):
    return True if board[pos] == " " else False

# Main game loop
while game_on:
    os.system('cls')
    print("Welcome to Tic Tac Toe!")
    p1, p2 = set_player()
    while not validate_win(board) and not validate_tie(board):
        print_board()
        board, turn = players_turn(p1, p2, turn)
    print_board()

    # Check for a tie
    if validate_tie(board):
        print("It's a tie!")
    else:
        # Determine the winner and update scores
        if turn == "p1":
            print("Congratulations, Player 2! You are the winner! \n")
            p2_score += 1
        else:
            print("Congratulations, Player 1! You are the winner! \n")
            p1_score += 1

    # Display scores
    print(f"Player 1: {p1_score} wins | Player 2: {p2_score} wins")

    # Reset the board for a new game
    board = {
        1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "
    }

    # Ask if players want to play again
    end_response = input("Do you want to play again? (y/n): ")
    if end_response.lower() != "y":
        game_on = False

print("\nBye!")