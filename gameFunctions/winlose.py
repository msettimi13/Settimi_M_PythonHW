from random import randint
from gameFunctions import winlose, gameVars, playerOptions 

def winorlose(status):
	print("\n\n")
	print("called win or lose", status, "\n")
	print("You", status, "! Would you like to play again")
	choice = input ("Y / N? ")

	if choice == "Y" or choice == "y":
  		#reset the game and start all over again
		gameVars.player_lives = gameVars.total_lives
		gameVars.computer_lives = gameVars.total_lives
		gameVars.player = False
		gameVars.computer = gameVars.weapons[randint(0,2)]

	elif choice == "N" or choice == "n":
		print("You chose to quit.")
		exit()
	else:
		print("Make a vaild Choice. Yes or No!!")
		# recursion => calling a function from inside itself
		winorlose(status)