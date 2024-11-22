# plays game and alternates turns
def alternate_turns():
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    player_X_choice = True
    while True:
        print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
        print(f"--+---+--")
        print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
        print(f"--+---+--")
        print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
        while True:
            try:
                if player_X_choice:
                    player_choice = int(input("Player 1: Choose a spot 1-9: "))
                else:
                    player_choice = int(input("Player 2: Choose a spot 1-9: "))
                if player_choice not in range(1, 10):
                    print("Invalid input, please put another spot in")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if not check_spot(board, player_choice):
                break
            else:
                print("Please choose a different spot.")
        row = (player_choice - 1) // 3
        col = (player_choice - 1) % 3
        if player_X_choice:
            board[row][col] = "X"
        else:
            board[row][col] = "O"
        if check_win(board):
            if player_X_choice:
                print("Player 1 Wins!")
                replay_game()
            else:
                print("Player 2 Wins!")
                replay_game()
            break
        if check_tie(board):
            print("Tie game, no winner")
            replay_game()
            break
        player_X_choice = not player_X_choice

#checks to see if someone won
def check_win(board):
    for row in board:
        if row[0] == row[1] == row[2]:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            return True
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] == board[1][1] == board[2][0]:
        return True
    return False

#checks for a tie
def check_tie(board):
    for row in board:
        for spot in row:
            if isinstance(spot, int):
                return False
    return True

#check if spot is already filled
def check_spot(board, player_choice):
    row = (player_choice - 1) // 3
    col = (player_choice - 1) % 3
    if board[row][col] == "X" or board[row][col] == "O":
        return True
    return False

def replay_game():
    while True:
        replay = str(input("Play Again? (Y/N): "))
        if replay == "Y":
            alternate_turns()
        elif replay == "N":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

def instruction_page():
    print("This is Tic Tac Toe, play against your friend and see who can get 3 in a row first!")
    print("Player 1 is X and player 2 is O, on your turn enter the number on the board that you want.")
    print("Good luck and have fun!")
    str(input("Press any key to continue: "))
    alternate_turns()

instruction_page()