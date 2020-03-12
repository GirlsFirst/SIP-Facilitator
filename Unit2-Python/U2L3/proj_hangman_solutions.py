import random

wordBank = ["sisterhood", "girls", "first", "code"]

word = random.choice(wordBank)

guessedWord = []

for i in range(len(word)):
    guessedWord.append('-')

done = False

rounds = len(word)+3

while (not done):
    letter = input("guess a letter! ")

    if letter.isalpha():
        round-=1
        if (letter in word):
            for i in range(len(word)):
                if word[i]==letter:
                    guessedWord[i]=letter    
        
        if ('-' not in guessedWord):
            done = True

    else:
        print ("that isn't a letter! Try again!")
    