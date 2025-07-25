# this is my ROCK PAPER SCISSORS GAME

print("welcome to my game")

player_choice=input("Please select and option from rock, paper scissors")
print("User Chose:",player_choice)

import random

VALID_OPTIONS= ["rock","paper,scissors"]

computer_choice = random.choice(VALID_OPTIONS)
print("COMPUTER CHOSE:", computer_choice)

# todo: determine the winner

print("WINNER: TODO")