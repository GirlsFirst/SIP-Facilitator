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
print("Welcome to the automated Rock, Paper, Scissors Game!")
print("The typical rules of the game is as follows:")
print("You will choose either rock, paper, or scissors (remember that spelling counts!)")
print("Rock beats Scissors")
print("Paper beats Rock")
print("Scissors beats Paper")
print("You will be battling the computer in this game")
print("In the event of a tie, no one wins the round")

choices = ["rock", "paper", "scissors"]
round = 0
player_win = 0
comp_win = 0

#Extensions #3-4: Allow user to determine number of rounds and check for invalid responses
round_max = input("How many rounds should we play? ")
if (round_max.isdigit() == True):
    round_max = int(round_max)
else:
    print("Sorry, that's not a valid round amount")


#Part 2: Running Each Round
while (round < round_max):
    player = input("Pick rock, paper, or scissors: ")
    
    #Extensions #1: Accept responses regardless of case
    player = player.lower()

    comp = random.choice(choices)
    print ("The computer chose " + comp)

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

    round+=1
    #Extension #2: Adding current score at the end of each round
    print("SCORE: Player - " + str(player_win) + " Computer - " + str(comp_win))
    
#Part 3: Finishing Results and End of the Game
if (comp_win > player_win):
    print("Sorry, you lost this time. The computer is the overall winner")
elif (comp_win < player_win):
    print("You are the overall winner! Congratulations")
else:
    print("Both you and the computer tied!")

print("The game has ended. Thank you for playing.")
print("Rerun the program to play again!")