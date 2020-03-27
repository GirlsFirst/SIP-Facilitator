'''
proj_rps_solutions.py
Description: Project solution file for rock paper scissors for U2L2. 
Project objective will explore variables, conditionals, and while loops.

Author: GWC Curriculum Team
Date Created: May 2020
'''

import random


choices = ["rock", "paper", "scissors"]
round = 1
to_win = 3
comp_wins = 0
play_wins = 0

while (comp_wins<3 and play_wins<3):
    print("Round "+str(round))
    player = input("Pick rock, paper, or scissors: ")
    comp = random.choice(choices)
    print ("The computer chose "+comp)
    
    if (player=='rock'):
        #print ("here in rock")
        if (comp=='rock'):
            print("It's a tie!")
        elif (comp == 'scissors'):
            print ("You win!")
            play_wins+=1
        else:
            print ("You lose...")
            comp_wins+=1
    elif (player == "paper"):
        if (comp=='paper'):
            print("It's a tie!")
        elif (comp == 'rock'):
            print ("You win!")
            play_wins+=1
        else:
            print ("You lose...")
            comp_wins+=1
    elif (player == "scissors"):
        if (comp=='scissors'):
            print("It's a tie!")
        elif (comp == 'paper'):
            print ("You win!")
            play_wins+=1
        else:
            print ("You lose...")
            comp_wins+=1
    else:
        print ("I'm sorry, that is not a valid choice. Remember, spelling counts!")
    
    round+=1
    
    print("The score is now \tyou: "+str(play_wins)+ "\tcomp: "+str(comp_wins))
    print("***********")


if (play_wins==3):
    print ("Congratulations! You beat the computer")
else:
    print("The computer beat you this time, but try again!")



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




#Part 2: Running Each Round
#TODO: Update while loop to loop through as many rounds as you want for your game!
while (round < round_max):            ):
    #TODO: Ask for player's choice


    #Randomly chooses the computer's choice from the choices list.
    #The computer's choice will either be "rock", "paper", or "scissors"
    comp = random.choice(choices)
    print ("The computer chose" + comp)

    #TODO: Add rules of game








    #TODO: Increment the round variable
    
    
    
#Part 3: Finishing Results and End of the Game
#TODO: Determine the overall winner





#TODO: Add a statement here to let your player know the game has ended!