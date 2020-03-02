#conditional_solution.py:
#This is the solution file for conditional.py: an intro python file to get you familiar 
#with writing conditionals in python!
#
#@author: <Insert Your Name Here!>
#

#Here at the top we include any libraries. We will discuss this later in the unit!
import random

#These next lines of codes generate a random number from 1 to 9
random.seed(1)
num = random.randint(1,9)

#Uncomment the line #15 and comment line #12 when facilitating the debugging activity.
#num = 5

#TODO: write a line of code below that prints out the value of num
print (num)

#TODO: Write a conditional statement that checks if num is less than 5. 
# If it is, print out a statement that reads the number is less than 5


if (num < 5):
    print ("The number is less than 5")

#TODO: Update your conditional statement so that if the number is not less than 5 
# it prints out “The number is greater than 5”.
if (num < 5):
    print ("The number is less than 5")
else:
    print ("The number is greater than 5!")

#TODO: Update the conditional once more that checks if num = 5 and 
# prints out “The number is 5!”
if (num < 5):
    print ("The number is less than 5")
elif (num == 5):
    print ("The number is 5!")
else:
    print ("The number is greater than 5!")


'''Alternatice solutions
Note that students will check if their solutions are correct in the next section

if (num < 5):
    print ("The number is less than 5!)
elif (num > 5):
    print("The number is greater than 5)
else:
    print("The number is 5!)

if (num < 5):
    print ("The number is less than 5)
else:
    if (num == 5):
        print("The number is 5!)
    else:
        print ("the number is greater than 5)

if num(<=4):
    print("The number is less than 5!)
elif (num == 5):
    print ("The number is 5!)
else:
    print ("The number is greater than 5!)

'''
#Sample Faulty Instructions for Class Debugging Activity.
#Uncomment out line #13 at after discussion of this activity
if (num < 5):
    print ("The number is less than 5")
else: 
    if (num == 5):
        print ("The number is 5!")
    print ("The number is greater than 5")

'''
Possible fixes to Sample Faulty Instructions

if (num < 5):
    print ("The number is less than 5")
else: 
    if (num == 5):
        print ("The number is 5!")
    else:
        print ("The number is greater than 5")

if (num < 5):
    print ("The number is less than 5")
else: 
    if (num == 5):
        print ("The number is 5!")
    if (num > 5):
        print ("The number is greater than 5")

if (num < 5):
    print ("The number is less than 5")
elif (num == 5):
    print ("The number is 5!")
else:
    print ("The number is greater than 5")
'''

#Extension Practice
#TODO: Write a conditional that checks if the number is between 1 and 3 or not. 
if (num<4):
    print ("The number is between 1 and 3")

#TODO: Write a conditional that checks if the number is in the beginning part of the range (1-3), 
# middle half (4-6), or latter part (7-9) of the range.
if (num <= 3):
    print ("The number is in the beginning of the range")
elif (num <= 6):
    print ("The number is in the middle of the range")
else:
    print ("The number is in the end of the range")

#TODO: Write a conditional that checks if a number is either 1 or 9 or not.
if (num == 1 or num == 9):
    print ("the number is either 1 or 9")

#TODO: Write a conditional that checks if the number is a multiple of 3
if (num == 3 or num == 6 or num == 9):
    print ("the number is a multiple of 3")

#TODO: Write a conditional that checks if the number is a multiple of 2. 
# If it is a multiple 2 check if the number is also a multiple of 4. 
if (num == 2 or num == 4 or num == 6 or num == 8):
    if (num == 4 or num == 8):
        print ("the number is a multiple of 2 and 4")
