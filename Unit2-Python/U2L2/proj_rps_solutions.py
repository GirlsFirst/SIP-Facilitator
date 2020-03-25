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