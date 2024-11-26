# complete code for Tic Tac Toe game
# tic tac toe game
player1 = input("Player 1, choose X or O: ")
if player1 == "x":
    player2 = "O"
    player1 = "X"
else:
    player2 = "X"
    player1 = "O"

print(f"Player 1 is {player1} and Player 2 is {player2}")
