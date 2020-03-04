'''
proj_adventure_soln.py
Description: Sample Solutions for choose your own adventure project originally in Scratch
Sample Scratch Project: https://scratch.mit.edu/projects/277970837/

Author: GWC Curriculum Team
Date Created: May 2020

'''

#The code below displays the base requirements for the project
print ("What a beautiful jungle!")
print("I should go exploring!")
answer = input ("Should I go left or right? ")
if (answer == "left"):
    print("Go to the Jurassic scene")
    print("Ahhh, time to relax!")
else:
    print("Go to the Wetland scene")
    print("This place looks tropical!")
    print("Dino: BOO!")
    print("AHHH!")
    answer = input ("Should I be his friend? (Enter yes or no.) ")
    if (answer == "yes"):
        print("Hello! Want to be friends?")
        print("Dino: Yay! My very first friend! <3")
        answer = input("Should we go get food? ")
        if (answer == "yes"):
            print("I love tacos!")
        else:
            print("Okay we can just hang out here")
    else:
        print("Leave me alone!")
        print("Dino: Awww...:(")

'''
#The code below provides the solutions to ALL extensions

print ("What a beautiful jungle!")
print("I should go exploring!")
answer = input ("Should I go left, right, or straight? ")
if (answer == "left" or answer == "Left"):
    print("Go to the Jurassic scene")
    print("Ahhh, time to relax!")
elif (answer == "right" or answer == "Right"):
    print("Go to the Wetland scene")
    print("This place looks tropical!")
    print("Dino: BOO!")
    print("AHHH!")
    answer = input ("Should I be his friend? (Enter yes or no.) ")
    if (answer == "yes" or answer == "Yes"):
        print("Hello! Want to be friendds?")
        print("Dino: Yay! My very first friend! <3")
        answer = input("Should we go get food? ")
        if (answer == "yes" or answer == "Yes"):
            print("I love tacos!")

            tacoShell = input("Do you prefer hard or soft tacos?" )
            tacoSauce = input("Do you prefer mild or hot sauce?" )
            if ((tacoShell == "hard" or tacoShell == "Hard") and (tacoSauce == "spicy" or tacoSauce == "Spicy")):
                print("That is my favorite too!")
            elif ((tacoShell == "hard" or tacoShell == "Hard") and (tacoSauce == "mild" or tacoSauce == "Mild")):
                print("I love hard tacos too but I prefer hot sauce!")
            elif ((tacoShell == "soft" or tacoShell == "Soft") and (tacoSauce == "mild" or tacoSauce == "Mild")):
                print("Hm, I'm not sure about that!")
            elif ((tacoShell == "soft" or tacoShell == "Soft") and (tacoSauce == "spicy" or tacoSauce == "Spicy")):
                print("I love spicy sauce but I prefer hard tacos!")
            else:
                print("I'm sorry, this answer is invalid. Press play and try again.")

        elif (answer == "no" or answer == "No"):
            print("Okay we can just hang out here")
        else:
            print("I'm sorry, this answer is invalid. Press play and try again.")
    elif (answer == "no" or answer == "No"):
        print("Leave me alone!")
        print("Dino: Awww...:(")
    else:
        print("I'm sorry, this answer is invalid. Press play and try again.")
elif (answer == "straight" or answer == "Straight"):
    print("Go to the Dessert scene")
    print("It's so dry here! Where is all of the water?")
else:
    print("I'm sorry, this answer is invalid. Press play and try again.")
'''