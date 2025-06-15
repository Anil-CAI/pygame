def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True

    for col in zip(*board):
        if all(s == player for s in col):
            return True

    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Player {current}, enter row (0-2): "))
            col = int(input(f"Player {current}, enter col (0-2): "))
        except ValueError:
            print("Please enter a number.")
            continue

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = current
            if check_winner(board, current):
                print_board(board)
                print(f"Player {current} wins!")
                break
            elif is_full(board):
                print_board(board)
                print("It's a draw!")
                break
            current = "O" if current == "X" else "X"
        else:
            print("Invalid move. Try again.")

play_tic_tac_toe()
