'''
Generate a random integer between 1 – 1000.  Also ask the user to enter how many guesses are allowed.  The game will ask the user to guess the randomly generated number.  
If the guess is lower than the number, the game will say:  “go higher”.  If the guess is higher than the number, the game will say:  “go lower”
Every time a guess is made, the number of tries go down.  
The game ends when the correct number is guessed or the number of tries run out.
'''

import random

hiddenNumber = random.randint(1, 1000) #secretly generated number

guesses = int(input('Enter number of guesses given: '))

guess = -1

while guess != hiddenNumber and guesses > 0:
    guess = int(input('Enter your guess: '))
    if guess > hiddenNumber:
        print('Go lower\n')
    elif guess < hiddenNumber:
        print('Go Higher\n')
    else:
        print('That is the correct guess')
    guesses -= 1
    
    
if guesses == 0:
    print('You ran out of tries')
    print('The correct number was', hiddenNumber)

    
    
