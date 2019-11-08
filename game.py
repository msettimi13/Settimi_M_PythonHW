# import the random package so we can generate a random AI choice
from random import randint
from gameFunctions import winlose, gameVars, playerOptions 

while gameVars.player is False:
	print("==================================================")
	print("Computer Lives", gameVars.computer_lives, "/", gameVars.total_lives)
	print("player Lives", gameVars.player_lives, "/", gameVars.total_lives)
	print("==================================================")
	print("choose your weapon!\n")
	player=input("choose rock, paper or scissors: \n")

	# this is where you would do the compare stuff
	# compare player and computer lives


	if gameVars.player_lives is 0:
		winlose.winorlose("lost")

	elif gameVars.computer_lives is 0:
		winlose.winorlose("won")

	else:
		player =False
		gameVars.computer = gameVars.weapons[randint(0,2)]



