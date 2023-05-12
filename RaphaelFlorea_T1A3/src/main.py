#/***********************************************************************************************/

from hangman_gameloop import word_generator, hangman_loop, inputter
from wordlist_builder import grand_list_builder, wordlist_opener
from hangman_classes import stages_initialiser, stage_builder

import time
import numpy as np

#/***********************************************************************************************/

#Function to control entire game loop for a single round
def gameloop(word_len):
    time_start = time.time()

    #Run functions to generate word, then ask to guess word
    word_list = grand_list_builder(wordlist_opener())
    guess_word = word_generator(word_len, word_list)
    stages = stage_builder(stages_initialiser())
    guesses_left = hangman_loop(guess_word, stages, word_len)

    time_finish = time.time()
    duration = time_finish - time_start

    if guesses_left == 0:
        print("FAILURE!")
    else:
        print("GUESSED WORD CORRECTLY!")
    return duration, guesses_left

#/***********************************************************************************************/

#A QUICK COUNTDOWN BEFORE ROUND BEGINS

def countdown():
    
    time.sleep(0.5)
    print("GET READY TO GUESS WORD!")
    for count in ['3', '2', '1']:
        time.sleep(1)
        print(count)

    print("GO!\n")

#/***********************************************************************************************/

def line_printer():
    print("-----------------------------------")

#/***********************************************************************************************/

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

#/***********************************************************************************************/

def score_calc(duration, player, score, round_score, streak):
    
    #Do score such that faster time gets more score, cap at 1000
    try:
        round_score[player] = min([round(100 / duration), 1000])
    except ZeroDivisionError:
        round_score[player] = 1000
    finally:
        #Players get rewarded with 'streak' system,
        #where more succesful games in a row also increases score
        round_score[player] *= streak[player]
        score[player] += round_score[player]

    #Return score for testing
    return round_score

#/***********************************************************************************************/

def main_game(player_number):

    #Initialise scoring, for both 1 and 2 players
    score = [0,0]
    round_score = [0,0]
    streak = [0,0]

    """Generate list of all lengths to be used:
        - Start at length 4, as going smaller has lots of acronyms
        - End at 14, as English words longer than this aren't common
    """
    all_word_lens = list(range(4,14))

    #Do 10 rounds, each round the word gets longer by 1 letter
    for word_len in all_word_lens:
        for player in range(player_number):
            print("\n****************************************")
            
            #Print out information about round
            round_ = word_len-3
            if player_number == 1:
                print(f"\nROUND {round_}\n")
            else:
                print(f"\nROUND {round_} FOR PLAYER {player+1}\n")
            countdown()

            #Run core game loop
            duration, guesses_left = gameloop(word_len)

            #Determine round didn't fail, if so, add to score
            if guesses_left > 0:
                streak[player] += 1
                score_calc(duration, player, score, round_score, streak)
            else:
                round_score[player] = 0
                streak[player] = 0
            
        info_printer(round_score, streak, round_, score, player_number)
    return score
        
#/***********************************************************************************************/

#SET UP BEGINNING OF GAME

def begin_game():

    #Print out main information
    line_printer()
    print("\nWELCOME TO HANGMAN!\n")
    line_printer()

    #Figure out number of players

    player_number = 0
    #Check that '1' or '2' is inputted, and nothing else
    valid_player_numbers = [1,2]
    while player_number not in valid_player_numbers:

        player_number = inputter("Enter '1' for singleplayer, enter '2' for multiplayer: ") 

        #Try to find if input is valid number
        try:
            player_number = int(player_number)
        except ValueError:
            print("\nNot a number.")
        else:
            if player_number not in valid_player_numbers:
                print("\nNot a valid number.")

    #Print out relevant message to response
    player_number = int(player_number)
    if player_number == 1:
        print("You have chosen singleplayer.")
    else:
        print("You have chosen multiplayer.")
    
    #Return scores to be shown at end of game
    total_scores = main_game(player_number)
    if player_number == 2:
        return total_scores
    else:
        return [total_scores[0]]

#/***********************************************************************************************/

#Function for contolling entire game

def whole_game():

    try:
        #Start game, get final scores at end
        scores = begin_game()

        #Print final scores
        if len(scores) == 1:
            print(f"OVERALL SCORE: {scores}")
        else:
            print(f"OVERALL SCORE FOR PLAYER 1: {scores[0]}")
            print(f"OVERALL SCORE FOR PLAYER 2: {scores[1]}\n")

            #Determine who won, or if there was a tie
            if scores[0] > scores[1]:
                print("PLAYER 1 WINS!")
            elif scores[1] > scores[0]:
                print("PLAYER 2 WINS!")
            else:
                print("PLAYER 1 AND 2 ARE TIED!")
        
        #Give final information
        
        inputter("Otherwise, press enter to continue.") 

    except KeyboardInterrupt:
        print("Bye bye!")      

#/***********************************************************************************************/

