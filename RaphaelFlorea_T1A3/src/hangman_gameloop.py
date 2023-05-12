#/****************************************************************/

#Import all necessary functions/classes variables
#This will be done to build guessing mechanic of game

import random
import string

from hangman_classes import hangman_stage

#/****************************************************************/

#Random word generator, to find word for game
def word_generator(word_len, grand_list):

    current_word_list = grand_list[word_len - 1]
    word_count = len(current_word_list)

    #find random word, using randit:
    random.seed()
    word_index = random.randint(0, word_count - 1)
    guess_word = current_word_list[word_index]
    guess_word = list(guess_word.upper())

    print(guess_word)
    return guess_word
    
#/****************************************************************/

#Function used to control all inputs
def inputter(text):
    print("Press '3' to quit.")
    input_val = input(text)

    #Uses '3' to exit program at anytime
    if input_val == '3':
        raise KeyboardInterrupt
    else:
        return input_val

#/****************************************************************/

#Validate the letter to be guessed based on input
def letter_validator(guesses_left, guesses):
    
    #First, get input
    letter_guess = inputter("Guess a letter: ")
    
    #Generate list of all uppercase letters in alphabet
    upper_letters = string.ascii_uppercase
    letter_guess = letter_guess.upper()

    while (letter_guess not in upper_letters) or (letter_guess in guesses):

        #Check if guess is valid letter
        if letter_guess in guesses:
            print("You have already guessed that letter.")
        elif letter_guess not in upper_letters:
            print("That's not a valid guess.")

        print(f"Guesses remaining: {guesses_left}")

        #Keep prompting for guess until quit or valid guess given
        letter_guess = inputter("\nGuess a letter: ")
        letter_guess = letter_guess.upper()

    return letter_guess

#/****************************************************************/

def hint_system(guess_word, guesses):

    #Use sets to easily find remaining letters to guess
    guess_word = set(guess_word)
    guesses = set(guesses)
    guesses_left = guess_word - guesses

    #Choose random letter and give it to player
    random_letter = random.choice(list(guesses_left))
    print("You're struggling with this word...")
    print(f"Try the letter: {random_letter}\n")

#/****************************************************************/

#Main hangman gameplay loop
def hangman_loop(guess_word, stages, word_len):

    #Initialise list and variables needed for function
    guesses = []
    incorrect_guesses = []
    guesses_left = 10
    hint_given = False

    #generate blank state for word to be shown, eg. '____'
    word_shown = []
    for i in range(word_len):
        word_shown.append('_')

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
        print(f"\n{word_joined}")

        #print actual hangman and other relevant info
        stages[guesses_left].printer()
        print(f"\nIncorrect guesses: {incorrect_guesses}")
        print(f"Guesses remaining: {guesses_left}")

        #finally check if whole word is guessed correctly
        if word_shown == guess_word:
            break
        
        #activate hint system if running out of guesses
        if guesses_left == 1 and not hint_given:
            hint_system(guess_word, guesses)
            
            #Use this variable so hint only given once
            hint_given = True

    return guesses_left

#/****************************************************************/






