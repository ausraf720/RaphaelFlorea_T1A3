#/***********************************************************************************************/

import random
import string

from hangman_classes import hangman_stage

#/***********************************************************************************************/

#A lot of words in program appears as list of characters, so use this to convert back into word
def word_joiner(word):
    str = ""
    word_joined = str.join(word) 
    return word_joined

#/***********************************************************************************************/

#MAIN MANUAL TESTING FEATURE
"""Used for testing purposes, to print actual word to be guessed at start of game,
    that way user can test if by putting in correct inputs,
    program can be tested to see if it recognises correct guesses or not"""

def optional_print_word(print_option, guess_word):
    if print_option == True:
        print(word_joiner(guess_word))

#/***********************************************************************************************/

#Random word generator, to find word for game
def word_generator(word_len, grand_list):

    #Word is selected only from portion of grand_list that has matching word_len
    current_word_list = grand_list[word_len - 1]
    word_count = len(current_word_list)

    #Find random word by generating seed, then use randit:
    random.seed()
    word_index = random.randint(0, word_count - 1)
    guess_word = current_word_list[word_index]
    guess_word = list(guess_word.upper())

    #Here, select if want to print guess word for testing purposes
    print_guess_word = True
    optional_print_word(print_guess_word, guess_word)

    return guess_word
    
#/***********************************************************************************************/

#Function used to control all inputs
def inputter(text):

    #Give option to quit at any time
    print("Press '3' to quit.")
    input_val = input(text)

    #Uses '3' to exit program at any time
    if input_val == '3':
        raise KeyboardInterrupt
    else:
        return input_val

#/***********************************************************************************************/

#Validate the letter to be guessed based on input
def letter_validator(guesses_left, guesses):
        
    #Generate list of all uppercase letters in alphabet
    upper_letters = string.ascii_uppercase

    while True:

        #First, get input
        letter_guess = inputter("Guess a letter: ")
        letter_guess = letter_guess.upper()

        #Check if already made guess before
        if letter_guess in guesses:
            print("\nYou have already guessed that letter.")
        
        #Make sure letter is valid single alphabet character, and also is not nothing
        elif letter_guess not in upper_letters or not letter_guess:
            print("\nThat's not a valid guess.")
        
        #If letter guess is valid, get out of loop
        else:
            break

        print(f"Guesses remaining: {guesses_left}")

    return letter_guess

#/***********************************************************************************************/

#This function gives a single hint if called
def hint_system(guess_word, guesses):

    """Use sets to easily find remaining letters to guess,
        by finding letters that are in the guess word, but not already guessed"""
    guess_word = set(guess_word)
    guesses = set(guesses)
    guesses_left = guess_word - guesses

    #Choose random letter from available letters and give it to player
    random_letter = random.choice(list(guesses_left))
    print("You're struggling with this word...")
    print(f"Try the letter: {random_letter}\n")

#/***********************************************************************************************/

#This function determines if letter is in word or not, and prints out remarks accordingly
def guess_checker(letter, guess_word, word_shown, incorrect_guesses, guesses_left):

    #Check if letter in word
    if letter in guess_word:
        print("That is a correct letter!")

        #If letter is correct, add the letter to 'word_shown', so word displayed is updated
        for itr in range(len(guess_word)):
            if letter == guess_word[itr]:
                word_shown[itr] = letter
    
    #If guess is wrong, guesses left reduces by one
    else:
        print("That is not correct!")
        guesses_left -= 1
        incorrect_guesses.append(letter)

    return guesses_left

#/***********************************************************************************************/

#Main hangman gameplay loop
def hangman_loop(guess_word, stages, word_len):

    #Initialise list and variables needed for function
    guesses = []
    incorrect_guesses = []
    guesses_left = 10
    hint_given = False

    #generate blank state for word to be displayed, eg. '____'
    word_shown = []
    for i in range(word_len):
        word_shown.append('_')

    #Keep looping until no available guesses left
    while guesses_left > 0:

        #First, check letter is valid, and obtain letter
        letter = letter_validator(guesses_left, guesses)
        guesses.append(letter)

        #Figure out if number of guesses are reduced
        guesses_left = \
            guess_checker(letter, guess_word, word_shown, incorrect_guesses, guesses_left)

        #Print word shown as string, not list
        print(f"\n{word_joiner(word_shown)}")

        #Print actual hangman and other relevant info
        stages[guesses_left].printer()
        print(f"\nIncorrect guesses: {incorrect_guesses}")
        print(f"Guesses remaining: {guesses_left}")

        #Finally check if whole word is guessed correctly
        if word_shown == guess_word:
            break
        
        #Activate hint system if running out of guesses, provided hint not yet given
        if guesses_left == 1 and not hint_given:
            hint_system(guess_word, guesses)
            
            #Use this variable to show program hint has been given, so it can't be given again
            hint_given = True

    return guesses_left

#/***********************************************************************************************/






