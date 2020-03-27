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
num = 25

while (num > 0):
    print(num)
    num -= 2

#TODO: Write a while loop that prints out the multiples of 5 starting from 5 up to 100

num = 5
while (num >= 100):
    print (num)
    num+=5

#TODO: Write a while loop that prints out the powers of 2 up to 1024: 2, 4, 8, 16, 32, ...
num = 2
while (num <= 1024):
    print (num)
    num *= 2

#Extensions (Optional)
#TODO: Write a while loop that executes 20 iterations but prints out numbers between 5-10

num = 0

while (num < 20):
    if (num >= 5 and num <= 10):
        print (num)
    num+=1

#TODO: Write a while loop that calculates the factorial of 4 or noted as 4!
prod = 1
index = 4

while (index > 0):
    prod*=index
    index-=1

print (prod)

#TODO: Print out the first 10 fibonacci numbers: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

fib1 = 1
fib2 = 1
print (fib1)
print (fib2)
index = 3

while (index <=10):
    nextFib = fib1+fib2
    print(fib1+fib2)
    fib1 = fib2
    fib2 = nextFib
    index+=1
