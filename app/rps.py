# this is my ROCK PAPER SCISSORS GAME

print("welcome to my game")

player_choice=input("Please select and option from rock, paper scissors")
print("User Chose:",player_choice)

import random

VALID_OPTIONS= ["rock","paper","scissors"]

computer_choice = random.choice(VALID_OPTIONS)
print("COMPUTER CHOSE:", computer_choice)

# bottom of the app/rps.py file:

if player_choice == computer_choice:
    result = "TIE GAME"
elif player_choice == "rock" and computer_choice == "scissors":
    result = "USER WINS"
elif player_choice == "rock" and computer_choice == "paper":
    result = "COMP WINS"
elif player_choice == "scissors" and computer_choice == "rock":
    result = "COMP WINS"
elif player_choice == "scissors" and computer_choice == "paper":
    result = "USER WINS"
elif player_choice == "paper" and computer_choice == "rock":
    result = "COMP WINS"
elif player_choice == "paper" and computer_choice == "scissors":
    result = "COMP WINS"

print(result)