from random import randint
from gameFunctions import winlose, gameVars, playerOptions 

# "basket" of choices
weapons=["rock", "paper", "scissors"]

player_lives = 5
computer_lives = 5

total_lives = 5
#start doing some logic and condition checking
computer=weapons[randint(0,2)]
player = False