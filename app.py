#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import random
from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")


# Rock beats scissors, paper beats rock, scissors beats paper
# User can select only rock, paper or scissors
def playGame(userChoice):
    validChoices = ["rock", "paper", "scissors"]
    if userChoice not in validChoices:
        return "Invalid input. Please choose rock, paper, or scissors."
    
    computerChoice = random.choice(validChoices)
    if userChoice == computerChoice:
        return "It's a tie!"
    elif userChoice == "rock" and computerChoice == "scissors":
        return "You win!"
    elif userChoice == "paper" and computerChoice == "rock":
        return "You win!"
    elif userChoice == "scissors" and computerChoice == "paper":
        return "You win!"
    else:
        return "You lose!"
    
# Computer picks a random choice
# User picks a choice
# User choice to play again or not
def playAgain():
    while True:
        playAgain = input("Do you want to play again? (y/n): ")
        if playAgain == "y":
            return True
        elif playAgain == "n":
            return False
        else:
            print("Invalid input. Enter y or n.")
# User must to be advise if he entry an incorrect option
# User can see all the score at the end of the game wins, loses and ties
def main():
    userWins = 0
    computerWins = 0
    ties = 0
    while True:
        userChoice = input("rock, paper, or scissors? ").lower()
        result = playGame(userChoice)
        print(result)
        if result == "You win!":
            userWins += 1
        elif result == "You lose!":
            computerWins += 1
        else:
            if result != "Invalid input. Please choose rock, paper, or scissors.":
                ties += 1
        print("You have {} wins, {} losses, and {} ties.".format(userWins, computerWins, ties))
        if not playAgain():
            print("You have {} wins, {} losses, and {} ties.".format(userWins, computerWins, ties))
            break
# Each match, user can see if he wins, loses or ties
# The game convert capital letters to minus to avoid errors

# At the end of each match, user can select if he wants to play again or not

# Start the game 
main()







