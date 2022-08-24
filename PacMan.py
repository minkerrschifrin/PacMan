import random
print()
print("Welcome to Pac-Man!")
print()
print("Use your A, W, S, and D keys to move!")
print ("Collect the fruit (F) for extra points!")
print()
print("Watch out for the number ghosts!")

#game boards

def game_board():
	board = [["F", "X", "o", "o", "X", "o", "o", "o", "1"],
			 ["o", "o", "o", "o", "X", "o", "X", "o", "2"],
			 ["X", "o", "o", "o", "o", "o", "X", "o", "o"],
			 ["o", "o", "o", "o", "o", "o", "X", "X", "o"],
			 ["o", "X", "X", "o", "X", "o", "o", "o", "o"],
			 ["o", "X", "o", "o", "X", "X", "o", "o", "o"],
			 ["o", "o", "o", "o", "X", "o", "o", "X", "o"],
			 ["X", "o", "X", "X", "o", "o", "X", "X", "o"],
			 ["X", "o", "o", "X", "o", "o", "o", "X", "o"],
			 ["o", "o", "o", "X", "o", "X", "o", "o", "o"],
			 ["p", "o", "o", "o", "o", "X", "o", "X", "F"]]
	return board
			 
def print_board(board):
	for line in board:
		print(line)

print_board(game_board())

board = [["F", "X", "o", "o", "X", "o", "o", "o", "1"],
		 ["o", "o", "o", "o", "X", "o", "X", "o", "2"],
		 ["X", "o", "o", "o", "o", "o", "X", "o", "o"],
		 ["o", "o", "o", "o", "o", "o", "X", "X", "o"],
		 ["o", "X", "X", "o", "X", "o", "o", "o", "o"],
		 ["o", "X", "o", "o", "X", "X", "o", "o", "o"],
		 ["o", "o", "o", "o", "X", "o", "o", "X", "o"],
		 ["X", "o", "X", "X", "o", "o", "X", "X", "o"],
		 ["X", "o", "o", "X", "o", "o", "o", "X", "o"],
		 ["o", "o", "o", "X", "o", "X", "o", "o", "o"],
		 ["p", "o", "o", "o", "o", "X", "o", "X", "F"]]

food_board = [["F", "-", "o", "o", "-", "o", "o", "o", "_"],
			  ["o", "o", "o", "o", "-", "o", "-", "o", "_"], 
			  ["-", "o", "o", "o", "o", "o", "-", "o", "o"], 
			  ["o", "o", "o", "o", "o", "o", "-", "-", "o"],
			  ["o", "-", "-", "o", "-", "o", "o", "o", "o"],
			  ["o", "-", "o", "o", "-", "-", "o", "o", "o"],
			  ["o", "o", "o", "o", "-", "o", "o", "-", "o"],
			  ["-", "o", "-", "-", "o", "o", "-", "-", "o"],
			  ["-", "o", "o", "-", "o", "o", "o", "-", "o"],
			  ["o", "o", "o", "-", "o", "-", "o", "o", "o"],
			  ["-", "o", "o", "o", "o", "-", "o", "-", "F"]]	 

#(see above) This food_board indicates where the dots and fruit (food) are on the board that can ONLY be affected by Pac-Man's movements, 
#and not the ghosts. In this way, Dania and I could guarantee that whenever the ghosts move, they do not affect the board in anyway.
#For example, when 1 or 2 (ghosts) randomly move, the original board is restored behind them whether it was an "o", an "_", or an "F".

#starting locations for Pac-Man and ghosts

pac_row = 10
pac_col = 0

ghost_location = {1:[8,0], 2:[8,1]}

ghost1_row = 0
ghost1_col = 8

ghost2_row = 1
ghost2_col = 8

game_over = False

#ghost movement(s)

def ghost1_movement():
	global game_over, pac_row, pac_col
	valid_moves = []
	possible_moves = [[ghost1_row-1,ghost1_col],
					  [ghost1_row+1,ghost1_col],
				   	  [ghost1_row,ghost1_col-1],
					  [ghost1_row,ghost1_col+1]]
	for i in possible_moves:
		if i[0] >= 0 and i[0] <= 10:
			if i[1] >= 0 and i[1] <= 8:
				if board[i[0]][i[1]] != "X":
					valid_moves.append(i)
	if len(valid_moves)==0:
		print("No Moves Left")
	move = random.choice(valid_moves)
	if move == [pac_row, pac_col]:
		game_over = True
		print("Game Over! You Lose!")
		print("Watch out for those ghosts!")	
		print("Final Score: " + str(score))
		print()
		print("TRY AGAIN: exit and reset your program!")
	return move		  

def ghost2_movement():
	global game_over, pac_row, pac_col
	valid_moves = []
	possible_moves = [[ghost2_row-1,ghost2_col],
					  [ghost2_row+1,ghost2_col],
				   	  [ghost2_row,ghost2_col-1],
					  [ghost2_row,ghost2_col+1]]
	for i in possible_moves:
		if i[0] >= 0 and i[0] <= 10:
			if i[1] >= 0 and i[1] <= 8:
				if board[i[0]][i[1]] != "X":
					valid_moves.append(i)	
	if len(valid_moves)==0:
		print("No Moves Left")
	move = random.choice(valid_moves)
	if move == [pac_row, pac_col]:
		game_over = True
		print("Game Over! You Lose!")
		print("Watch out for those ghosts!")	
		print("Final Score: " + str(score))
		print()	
		print("TRY AGAIN: exit and reset your program!")		
	return move

#(see above) Our two ghosts, 1 and 2, can choose any random movement (up, down, left, or right) as long as it's not into a wall ("X"). 
#The possible moves are added to an empty list and then one of those moves are chosen.
#If one of the ghost's movements equals the location of Pac-Man's current locations then the game ends. 
#In other words, if the ghost eats Pac-Man, the game ends.
#These functions will later be applied under the while statement (see below).

#pac-man movement

score = 0

while game_over == False:
	command = input("What's your next move?")
	if command == 'w':
		if board[pac_row-1][pac_col] != "X":

			if board[pac_row-1][pac_col] == "o":
				score = score+1
			if board[pac_row-1][pac_col] == "F":
				score = score+2	
			if board[pac_row-1][pac_col] == "1" or board[pac_row-1][pac_col] == "2":
				game_over = True
				print("Game Over! You Lose!")
				print("Watch out for those ghosts!")	
				print("Final Score: " + str(score))
				print()
				print("TRY AGAIN: exit and reset your program!")
				break	

			food_board[pac_row-1][pac_col] = "_"
			board[pac_row][pac_col] = "_"
			board[pac_row-1][pac_col] = "p"
			pac_row = pac_row-1
			print_board(board)

			if not game_over:
				print("Score: " + str(score))
		else:
			print("Invalid Move!")	

	elif command == 's':
		if board[pac_row+1][pac_col] != "X":

			if board[pac_row+1][pac_col] == "o":
				score = score+1
			if board[pac_row+1][pac_col] == "F":
				score = score+2	
			if board[pac_row+1][pac_col] == "1" or board[pac_row+1][pac_col] == "2":
				game_over = True
				print("Game Over! You Lose!")
				print("Watch out for those ghosts!")	
				print("Final Score: " + str(score))
				print()
				print("TRY AGAIN: exit and reset your program!")
				break

			food_board[pac_row+1][pac_col] = "_"
			board[pac_row][pac_col] = "_"
			board[pac_row+1][pac_col] = "p"
			pac_row = pac_row+1
			print_board(board)

			if not game_over:
				print("Score: " + str(score))
		else:
			print("Invalid Move!")

	elif command == 'a':
		if board[pac_row][pac_col-1] != "X":

			if board[pac_row][pac_col-1] == "o":
				score = score+1
			if board[pac_row][pac_col-1] == "F":
				score = score+2	
			if board[pac_row][pac_col-1] == "1" or board[pac_row][pac_col-1] == "1":
				game_over = True
				print("Game Over! You Lose!")
				print("Watch out for those ghosts!")	
				print("Final Score: " + str(score))
				print()
				print("TRY AGAIN: exit and reset your program!")
				break

			food_board[pac_row][pac_col-1] = "_"
			board[pac_row][pac_col] = "_"
			board[pac_row][pac_col-1] = "p"
			pac_col = pac_col-1
			print_board(board)

			if not game_over:
				print("Score: " + str(score))
		else:
			print("Invalid Move!")

	elif command == 'd':	
		if board[pac_row][pac_col+1] != "X":

			if board[pac_row][pac_col+1] == "o":
				score = score+1
			if board[pac_row][pac_col+1] == "F":
				score = score+2	
			if board[pac_row][pac_col+1] == "1" or board[pac_row][pac_col+1] == "2":
				game_over = True
				print("Game Over! You Lose!")
				print("Watch out for those ghosts!")	
				print("Final Score: " + str(score))
				print()
				print("TRY AGAIN: exit and reset your program!")
				break

			food_board[pac_row][pac_col+1] = "_"
			board[pac_row][pac_col] = "_"
			board[pac_row][pac_col+1] = "p"
			pac_col = pac_col+1
			print_board(board)

			if not game_over:
				print("Score: " + str(score))
		else:
			print("Invalid Move!")

#(see above) For each possible move (using the A, W, S, and D keys) Pac-Man can move in one of four directions, as long as it is not into a wall ("X"). 
#Running into a wall results in "Invalid Move!"
#If Pac-Man's location is the same as a ghosts's the game ends. 
#And with every one of Pac-Man's move, it affects the food board.
#For example, if Pac-Man collects "o"s or "F"s, the food board is updated. 
#Collecting an "o" adds 1 point to the score, and collecting an "F" adds 2 points.

	print()
	next_ghost1_move = ghost1_movement()		
	board[ghost1_row][ghost1_col] = food_board[ghost1_row][ghost1_col]
	board[next_ghost1_move[0]][next_ghost1_move[1]] = "1"
	ghost1_row = next_ghost1_move[0] 
	ghost1_col = next_ghost1_move[1]	

	next_ghost2_move = ghost2_movement()
	board[ghost2_row][ghost2_col] = food_board[ghost2_row][ghost2_col]
	board[next_ghost2_move[0]][next_ghost2_move[1]] = "2"
	ghost2_row = next_ghost2_move[0] 
	ghost2_col = next_ghost2_move[1]	

#(see above) This puts the ghost1_movement() and ghost2_movement() functions into action. 
#After choosing a random move, this executes it.

	if score == 70:
		game_over = True
		print ("Game Over! You Win!")
		print("Final Score: " + str(score))
		print()
		print("PLAY AGAIN: exit and reset your program!")

#(see above) If you collect all the food, you win!		


