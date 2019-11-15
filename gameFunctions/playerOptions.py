from random import randint
from gameFunctions import gameVars 

def compareChoices(status):

	if gameVars.player == gameVars.computer:
		print("\n")
		print("***************************")
		print("tie, no one wins! try again")
		print("***************************")

	elif gameVars.player == "quit":
		print("\n")
		print("****************************")
		print("you choose to quit, quitter.")
		print("****************************")
		exit()

	elif gameVars.player == "rock":
		if gameVars.computer == "paper":
			print("||||||||||||||||||||||||||||||||||||||||||||||||||")
			print("\n")
			print("You lose!", gameVars.computer, "covers", gameVars.player, "\n")
			print("\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("||||||||||||||||||||||||||||||||||||||||||||||||||")
			print("\n")
			print("You win!", gameVars.player, "smashes", gameVars.computer, "\n")
			print("\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif gameVars.player == "paper":
		if gameVars.computer == "scissors":
			print("||||||||||||||||||||||||||||||||||||||||||||||||||")
			print("\n")
			print("You lose!", gameVars.computer, "cuts", gameVars.player, "\n")
			print("\n")
			gameVars.player_lives = gameVars.player_lives -1

		else:
			print("||||||||||||||||||||||||||||||||||||||||||||||||||")
			print("\n")
			print("You win!", gameVars.player, "covers", gameVars.computer, "\n")
			print("\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif gameVars.player == "scissors":
		if gameVars.computer == "rock":
			print("||||||||||||||||||||||||||||||||||||||||||||||||||")
			print("\n")
			print("You lose!", gameVars.computer, "smashes", gameVars.player, "\n")
			print("\n")
			gameVars.player_lives = gameVars.player_lives -1

		else:
			print("||||||||||||||||||||||||||||||||||||||||||||||||||")
			print("\n")
			print("You win!", gameVars.player, "cuts", gameVars.computer, "\n")
			print("\n")
			gameVars.computer_lives = gameVars.computer_lives -1
