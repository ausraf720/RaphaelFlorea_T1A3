#/****************************************************************/

#Import all necessary functions/classes variables
#This will be done to build guessing mechanic of game

import random
import string

from hangman import stages, hangman_stage
from wordlist_builder import grand_list

#/****************************************************************/

#INITIALISE GUESSING FUNCTION

#to be changed depending on word length desired
word_len = 5


guesses_left = 10
current_word_list = grand_list[word_len - 1]
word_count = len(current_word_list)

#generate blank state for word to be shown, eg. '____'
word_shown = []
for i in range(word_len):
    word_shown.append('_')

#find random word, using randit:
random.seed()
word_index = random.randint(0, word_count - 1)
guess_word = current_word_list[word_index]
guess_word = list(guess_word.upper())
print(guess_word)

upper_letters = string.ascii_uppercase
guesses = []
incorrect_guesses = []

#/****************************************************************/

#get a letter guess
def letter_validator(guesses_left, guesses):
    
    letter_guess = input("Guess a letter: ")
    letter_guess = letter_guess.upper()
    while (letter_guess not in upper_letters) and (letter_guess not in guesses):

        #check if guess is valid letter
        if letter_guess in guesses:
            print("You have already guessed that letter.")
        elif letter_guess not in upper_letters:
            print("That's not a valid guess.")

        print(f"Guesses remaining: {guesses_left}")
        print("Press ... to quit.\n")

        #keep prompting for guess until quit or valid guess given
        letter_guess = input("Guess a letter: ")
        letter_guess = letter_guess.upper()

    return letter_guess

#/****************************************************************/

while guesses_left > 0:

    #First, check letter is valid, and obtain letter
    letter = letter_validator(guesses_left, guesses)

    #Check if letter in word
    if letter in guess_word:
        print("That is a correct letter!")

        #If letter is correct, add the letter to 'word_shown'
        #Thus, displayed word will be updated with guess
        for itr in range(word_len):
            if letter == guess_word[itr]:
                word_shown[itr] = letter
    
    #If guess wrong, guesses left reduces by one
    else:
        print("That is not correct!")
        guesses_left -= 1
        incorrect_guesses.append(letter)

    guesses.append(letter)

    #print word shown as string, not list
    str = ""
    word_joined = str.join(word_shown) 
    print(word_joined)

    #print actual hangman and other relevant info
    stages[guesses_left].printer()
    print(f"Incorrect guesses: {incorrect_guesses}")
    print(f"Guesses remaining: {guesses_left}")
    print("Press ... to quit.\n")
    
#/****************************************************************/
    




