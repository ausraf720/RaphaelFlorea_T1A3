#/****************************************************************/

"""import subprocess

# use pip to install the package
subprocess.check_call(["pip", "install", 'numpy'])"""

#/****************************************************************/

from hangman_gameloop import word_generator, hangman_loop
from wordlist_builder import grand_list
from hangman_classes import stages

import time
import numpy as np

#/****************************************************************/

#Function to control entire game loop for a single round
def gameloop(word_len):
    time_start = time.time()

    #Run functions to generate word, then ask to guess word
    guess_word = word_generator(word_len, grand_list)
    guesses_left = hangman_loop(guess_word, stages, word_len)

    time_finish = time.time()
    duration = time_finish - time_start

    if guesses_left == 0:
        print("FAILURE!")
    else:
        print("GUESSED WORD CORRECTLY!")
    return duration, guesses_left

#/****************************************************************/

score = 0

streak = 0

#generate list of all lengths to be used
#Start at length 4, as going smaller has lots of acronyms
#End at 14, as English words longer than this aren't common
all_word_lens = list(range(4,14))

for word_len in all_word_lens:
    print("\n****************************************")
    round_ = word_len-3
    print(f"\nROUND {round_}\n")
    duration, guesses_left = gameloop(word_len)

    #Determine round didn't fail, if so, add to score
    if guesses_left > 0:

        #Do score based on inverse of time taken,
        #Thus faster has more score
        round_score = round(100 / duration) 

        #Times by word length, so that longer words score better
        round_score *= word_len

        #Players get rewarded with 'streak' system,
        #where more succesful games in a row also increases score
        streak += 1
        round_score *= streak
        score += round_score

    #Score should be nothing for failed round
    else:
        round_score = 0
        streak = 0
    print("-----------------------------------")
    print(f"Score for Round: {round_score}")
    print(f"Streak: {streak}")
    
    print(f"TOTAL SCORE FOR ROUND {round_}: {score}")
    print("-----------------------------------")

#/****************************************************************/