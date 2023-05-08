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

guess_count = 0
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

#/****************************************************************/

upper_letters = string.ascii_uppercase
guesses = ['A']

#get a letter guess
letter_guess = input("Guess a letter: ")
while (letter_guess not in upper_letters) and (letter_guess not in guesses):
    letter_guess = letter_guess.upper()

    #check if guess is valid letter
    if letter_guess in guesses:
        print("You have already guessed that letter.")
        print("Press ... to quit.")
    elif letter_guess not in upper_letters:
        print("That's not a valid guess.")
        print("Press ... to quit.")

    #keep prompting for guess until quit or valid guess given
    letter_guess = input("Guess a letter: ")




