# complete code for Tic Tac Toe game
# tic tac toe game
player1 = input("Player 1, choose X or O: ")
if player1 == "x" or player1 == "X":
    player2 = "O"
    player1 = "X"
else:
    player2 = "X"
    player1 = "O"

print(f"Player 1 is {player1} and Player 2 is {player2}")


# board array
board = [" " for x in range(9)]

def printBoard():
    print("     |     |      ")
    print("  " + board[0] + "  |  " + board[1] + "  |  " + board[2] + " ")
    print("_____|_____|_____    1 | 2 | 3 ")
    print("     |     |       -------------")
    print("  " + board[3] + "  |  " + board[4] + "  |  " + board[5] + "      4 | 5 | 6 ")
    print("_____|_____|_____  -------------")
    print("     |     |         7 | 8 | 9 ")
    print("  " + board[6] + "  |  " + board[7] + "  |  " + board[8] + "  ")
    print("     |     |     ")