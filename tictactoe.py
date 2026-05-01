def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]}")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(b):
    #all winning combos
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], #horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], #vertical
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combinations:
        if b[combo[0]] == b[combo[1]] == b[combo[2]] != " ":
            return b[combo[0]]
        if " " not in b:
            return "Tie"
        return None
    
def run():
    print("--- Tic Tac Toe---")
    board = [" "] * 9
    current_player = "X"

    while True:
        print_board(board)
        try:
            move = input(f"Player {current_player}, choose a spot (1-9) or 'q' to quit: ")
            if move.lower() == 'q': break

            index = int(move) - 1

            if board[index] == " ":
                board[index] = current_player
                winner = check_winner(board)

                if winner:
                    print_board(board)
                    if winner == "Tie":
                        print("It's a tie")
                    else:
                        print(f"Player {winner} wins!")
                    break

                current_player = "O" if current_player == "X" else "X"
            else:
                print("That spot is taken!")
        except (ValueError, IndexError):
            print("Invalid input! Enter a number between 1 and 9.")

    input("\nPress Enter to return to the Main Menu...")