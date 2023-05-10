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

#A QUICK COUNTDOWN BEFORE ROUND BEGINS

def countdown():
    
    time.sleep(0.5)
    print("GET READY TO GUESS WORD!")
    for count in ['3', '2', '1']:
        time.sleep(1)
        print(count)

    print("GO!\n")

#/****************************************************************/

def line_printer():
    print("-----------------------------------")

#/****************************************************************/

#Print out information for each round of game:
def info_printer(round_score, streak, round_, score, player_number):
    
    #Print info for just singleplayer
    if player_number == 1:
        line_printer()
        print(f"Score for Round: {round_score[0]}")
        print(f"Streak: {streak[0]}")         
        print(f"TOTAL SCORE FOR ROUND {round_}: {score[0]}")
        line_printer()

    #Print info for both players, using for loop
    else:
        line_printer()
        for player in range(player_number):
            print(f"Player {player + 1} score for Round: {round_score[player]}")
            print(f"Player {player + 1} streak: {streak[player]}")         
            print(f"PLAYER {player + 1} TOTAL SCORE FOR ROUND {round_}: {score[player]}")
            line_printer()
    
    #Have some delay to allow player(s) to view scores
    time.sleep(3)

#/****************************************************************/

def main_game(player_number):

    score = [0,0]
    round_score = [0,0]
    streak = [0,0]

    #generate list of all lengths to be used
    #Start at length 4, as going smaller has lots of acronyms
    #End at 14, as English words longer than this aren't common
    all_word_lens = list(range(4,14))

    for word_len in all_word_lens:
        for player in range(player_number):
            print("\n****************************************")
            round_ = word_len-3
            if player_number == 1:
                print(f"\nROUND {round_}\n")
            else:
                print(f"\nROUND {round_} FOR PLAYER {player+1}\n")
            countdown()
            duration, guesses_left = gameloop(word_len)

            #Determine round didn't fail, if so, add to score
            if guesses_left > 0:

                #Do score such that faster time gets more score
                round_score[player] = round(100 / duration) 

                #Times by word length, so that longer words score better
                round_score[player] *= word_len

                #Players get rewarded with 'streak' system,
                #where more succesful games in a row also increases score
                streak[player] += 1
                round_score[player] *= streak[player]
                score[player] += round_score[player]

            #Score should be nothing for failed round
            else:
                round_score[player] = 0
                streak[player] = 0
            
        info_printer(round_score, streak, round_, score, player_number)
        

#/****************************************************************/

#SET UP BEGINNING OF GAME

def begin_game():

    #Print out main information
    line_printer()
    print("\nWELCOME TO HANGMAN!\n")
    line_printer()
    print("Press ... to quit.")

    #Figure out number of players
    player_number = ""
    valid_player_numbers = ['1', '2']

    #Check that '1' or '2' is inputted, and nothing else
    while player_number not in valid_player_numbers:
        player_number = input("Enter '1' for singleplayer, enter '2' for multiplayer: ")

        if player_number not in valid_player_numbers:
            print("\nNot a valid response.")
            print("Press ... to quit.")

    #Print out relevant message to response
    player_number = int(player_number)
    if player_number == 1:
        print("You have chosen singleplayer.")
    else:
        print("You have chosen multiplayer.")
    
    
    main_game(player_number)

#/****************************************************************/

begin_game()