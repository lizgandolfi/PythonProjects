
'''
A hidden word will be chosen from a large list.  This will not be revealed.  The number of tries allowed will be double the size of the hidden word.  You will write a program that allows the user to guess a character or letter.  
If the letter guessed is inside the word, you will reveal what location that letter exists in.  If the letter is not inside the word, the number of tries goes down by 1.  
The player can also guess the word instead.  If the guess is correct, the game is won.  If the guess is not correct, the number of tries goes down by 1.
If the number of tries reaches 0, the game is lost.
All words will be lower case.
'''
import math
import random


# Master word list
wordList = ['wilderness', 'dependence', 'distributor', 'fireplace', 'difference', 'straighten', 'franchise', 'integrity' ,'television',
    'literature', 'fashionable', 'empirical', 'chemistry', 'memorandum', 'countryside', 'undertake', 'chimpanzee', 'legislation', 'population',
    'negligence', 'credibility', 'partnership', 'ghostwriter', 'defendant', 'confusion', 'eavesdrop', 'demonstration', 'battlefield', 'expectation',
    'houseplant', 'captivate', 'resolution', 'presidential', 'transition', 'constituency', 'reference', 'consolidate', 'recording', 'acceptable',
    'shareholder', 'catalogue', 'projection', 'acquaintance', 'interference', 'environment', 'invisible', 'electronics', 'operation', 'butterfly']
    
hiddenWord = random.choice(wordList)  # a random word is chosen from the list above


hiddenWordLenght = len(hiddenWord)
guesses =(hiddenWordLenght * 2)
triesRemaining = (guesses -1)
guess = ' '


print('Welcome to Hangman. A hidden word has been chosen')
print('The lenght of this word is ', hiddenWordLenght)

while guesses > 0 and guess != hiddenWord:
    print('\nWhat would you like to do?')
    print('1:\tGuess a letter')
    print('2:\tGuess the word')
    
    choice = int(input())
    
    if choice == 1:
        letter = input('\nEnter your letter: ')
        getLetterCount = hiddenWord.count(letter)
        
        if getLetterCount == 0:
            print('That letter does not exist.')
            print(triesRemaining, 'tries remaining.\n')
        
        else:   
            for i in range(hiddenWordLenght):
                if hiddenWord[i:i+1] == letter:
                    print('This letter exists in positions: ')
                    print(i + 1)
                
    if choice == 2:
        guess = input('\nEnter your word: ')
        
        if guess == hiddenWord:
            print('That is correct. You have won!)')
        else:
            print('That is incorrect.')
            print(triesRemaining, 'tries remaining.\n')
            
if triesRemaining == 0:
    print('You have run out of tries. HANGMAN! The secret word was', hiddenWord)





