# import the random package so we can generate a random AI choice
from random import randint

# set up some variables for player and AI lives
player_lives = 5
computer_lives = 5

# "basket" of choices
choices=["rock","paper","scissors"]

# let the AI make a choice
computer=choices[randint(0,2)]

# set up a game loop here so we don't have to keep restarting
player = False

while player is False:
	# set plater to True
	print("***************************\n")
	print("computer lives: ", computer_lives, "/5\n")
	print("player lives: ", player_lives, "/5\n")
	print("Choose your weapon!\n")
	print("***************************\n")

	player = input("choose rock, paper or scissors:")
	player = player.lower()

	print("computer chose ", computer, "\n")
	print("player chose ", player, "\n")

	if player.lower() == "quit":
		exit()
	elif computer == player:
		print("tie! no one wins, play again")
	elif player.lower() == "rock":
		if computer == "paper":
			print("You lose!", computer, "covers", player, "\n")
			player_lives = player_lives - 1
		else:
			print("You win!", player, "smashes", computer, "\n")
			computer_lives = computer_lives - 1

	elif player.lower() == "paper":
		if computer == "scissors":
			print("You lose!", computer, "cuts", player, "\n")
			player_lives = player_lives - 1
		else:
			print("You win!", player, "covers", computer, "\n")
			computer_lives = computer_lives - 1

	elif player.lower() == "scissors":
		if computer == "rock":
			print("You lose!", computer, "smashes", player, "\n")
			player_lives = player_lives - 1
		else:
			print("You win!", player, "cuts", computer, "\n")
			computer_lives = computer_lives - 1

	else: 
		print("That's not a valid choice, try again")

	# handle all lives lost for player or AI
	if player_lives is 0: 
		print("Out of lives! you suck at this game. Would you like to play again?\n")
		choice = input("Y / N")
		print(choice)

		if (choice is "N") or (choice is "n"): 
			print("You chose to quit.")
			exit()

		elif (choice is "Y") or (choice is "y"):
		# reset the game so that we can start all over again
			player_lives = 5
			computer_lives = 5 
			player = False
			computer = choices[randint(0,2)]

	elif computer_lives is 0: 
		print("Computer is out of lives! you rock at this game. Would you like to play again?\n")
		choice = input("Y / N")
		print(choice)

		if (choice is "N") or (choice is "n"): 
			print("You chose to quit.")
			exit()

		elif (choice is "Y") or (choice is "y"):
		# reset the game so that we can start all over again
			player_lives = 5
			computer_lives = 5 
			player = False
			computer = choices[randint(0,2)]
	else:
		player = False
		computer = choices[randint(0,2)]

