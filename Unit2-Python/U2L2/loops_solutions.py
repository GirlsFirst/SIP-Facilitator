'''
loops_solutions.py
Description: Intro Python Loops Solutions File for you to practice writing loops 
and explore variable operations

Author: GWC Curriculum Team
Date Created: May 2020
'''

#TODO: Create an integer variable and set it equal to 0
num = 0

#TODO: Write a while loop that prints out the value of your integer variable and repeats for 25 iterations
while (num < 25):
    print(num)
    num += 1

#TODO: Write a while loop that prints out all the odd numbers starting from 25 and ending at 1
num = 0

while (num > 0):
    print(num)
    num -= 2

#TODO: Write a while loop that prints out the powers of 2 up to 1024: 2, 4, 8, 16, 32, ...
num = 2
while (num <= 1024):
    print (num)
    num *= 2

#TODO: Write a while loop that start from 0 to 20 (inclusive) and increments the variable by 1 but only prints out the variable 
# if it is a multiple of 4
num = 0
while (num <= 20):
    if (num % 4 == 0):
        print (num)
    num+=1


#Extensions

