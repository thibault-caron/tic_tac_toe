# Function to print Tic Tac Toe
def print_tic_tac_toe(values):
	print("\n")
	print("\t     |     |")
	print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
	print('\t_____|_____|_____')

	print("\t     |     |")
	print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
	print('\t_____|_____|_____')

	print("\t     |     |")

	print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
	print("\t     |     |")
	print("\n")


# Function to print the score-board
def print_scoreboard(score_board):
	print("\t--------------------------------")
	print("\t       	   SCOREBOARD       ")
	print("\t--------------------------------")

	players = list(score_board.keys())
	print("\t   ", players[0], "\t    ", score_board[players[0]])
	print("\t   ", players[1], "\t    ", score_board[players[1]])

	print("\t--------------------------------\n")