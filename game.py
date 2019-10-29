# import the random package so we can generate a random AI choice
from random import randint

# "basket" of choices
choices=["rock","paper","scissors"]

# let the AI make a choice
computer=choices[randint(0,2)]

# set up a game loop here so we don't have to keep restarting
player = False

while player is False:
	# set plater to True
	print("***************************\n\n")
	print("Choose your weapon!\n\n")
	print("***************************\n\n")

	player = input("choose rock, paper or scissors:")

	print("computer chose ", computer, "\n")
	print("player chose ", player, "\n")

	if player.lower() == "quit":
		exit()
	elif computer == player:
		print("tie! no one wins, play again")
	elif player.lower() == "rock":
		if computer == "paper":
			print("You lose!", computer, "covers", player, "\n")
		else:
			print("You win!", player, "smashes", computer, "\n")

	elif player.lower() == "paper":
		if computer == "scissors":
			print("You lose!", computer, "cuts", player, "\n")
		else:
			print("You win!", player, "covers", computer, "\n")

	elif player.lower() == "scissors":
		if computer == "rock":
			print("You lose!", computer, "smashes", player, "\n")
		else:
			print("You win!", player, "cuts", computer, "\n")

	else: 
		print("That's not a valid choice, try again")



	
	player = False
	computer = choices[randint(0,2)]

