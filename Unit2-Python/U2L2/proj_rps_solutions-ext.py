'''
proj_rps_solutions-ext.py
Description: Project solution file for rock paper scissors for U2L2. 
Project objective will explore variables, conditionals, and while loops.

This solutions files contains all extensions to the project except for extensions #5

Author: GWC Curriculum Team
Date Created: May 2020
'''

import random

#Part 1: Introduction and Start of the Game
#TODO: Write the opening introduction of your game
print("Welcome to the automated Rock, Paper, Scissors Game!")
print("The typical rules of the game is as follows:")
print("You will choose either rock, paper, or scissors (remember that spelling counts!)")
print("Rock beats Scissors")
print("Paper beats Rock")
print("Scissors beats Paper")
print("You will be battling the computer in this game")
print("In the event of a tie, no one wins the round")

#TODO: Add variables to use throughout the program in this section
choices = ["rock", "paper", "scissors"]
round = 0
player_win = 0
comp_win = 0
round_max = input("How many rounds should we play? ")
if (round_max.isdigit() == True):
    round_max = int(round_max)
else:
    print("Sorry, that's not a valid round amount")


#Part 2: Running Each Round
#TODO: Update while loop to loop through as many rounds as you want for your game!
while (round < round_max):
    #TODO: Ask for player's choice
    player = input("Pick rock, paper, or scissors: ")
    player = player.lower()

    #Randomly chooses the computer's choice from the choices list.
    #The computer's choice will either be "rock", "paper", or "scissors"
    comp = random.choice(choices)
    print ("The computer chose " + comp)

    #TODO: Add rules of game
    if (player == "rock"):
        if (comp == "rock"):
            print("It's a tie")
        elif (comp == "paper"):
            print("You lose!")
            comp_win+=1
        else:
            print("You win!")
            player_win+=1
    elif (player == "scissors"):
        if (comp == "scissors"):
            print("It's a tie")
        elif (comp == "rock"):
            print("You lose!")
            comp_win+=1
        else:
            print("You win!")
            player_win+=1
    elif (player == "paper"):
        if (comp == "paper"):
            print("It's a tie")
        elif (comp == "scissors"):
            print("You lose!")
            comp_win+=1
        else:
            print("You win!")
            player_win+=1
    else:
        print("I'm sorry, that is not a valid choice. Remember spelling counts!")

    #TODO: Increment the round variable
    round+=1
    print("SCORE: Player - " + str(player_win) + " Computer - " + str(comp_win))
    
#Part 3: Finishing Results and End of the Game
#TODO: Determine the overall winner
if (comp_win > player_win):
    print("Sorry, you lost this time. The computer is the overall winner")
elif (comp_win < player_win):
    print("You are the overall winner! Congratulations")
else:
    print("Both you and the computer tied!")

#TODO: Add a statement here to let your player know the game has ended!
print("The game has ended. Thank you for playing.")
print("Rerun the program to play again!")