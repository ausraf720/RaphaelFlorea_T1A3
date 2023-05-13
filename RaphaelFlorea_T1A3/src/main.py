#/****************************************************************************/

from hangman_gameloop import word_generator, hangman_loop, inputter, \
                             word_joiner, optional_print_word
from wordlist_builder import grand_list_builder, wordlist_opener
from hangman_classes import stages_initialiser, stage_builder

import time

#/****************************************************************************/


#Function to control entire game loop for a single round
def gameloop(word_len, word_list, cheats):

    #Record the time before running the whole round
    time_start = time.time()

    #Run functions to generate word, then ask to guess word
    guess_word = word_generator(word_len, word_list)

    #Here, select if want to print guess word for testing purposes


    optional_print_word(cheats, guess_word)

    stages = stage_builder(stages_initialiser())
    guesses_left = hangman_loop(guess_word, stages, word_len)

    #Calculate overall time for round, 
    # by finding difference between start and end times
    time_finish = time.time()
    duration = time_finish - time_start

    #Determine if guesses_left is 0, 
    # meaning hangman is hanged and round failed
    if guesses_left == 0:
        print("FAILURE!\n")

        #Show actual word
        print(f"Correct word was: {word_joiner(guess_word)}")
    
    #Notfiy player if they won round
    else:
        print("GUESSED WORD CORRECTLY!")
    return duration, guesses_left

#/****************************************************************************/

#A quick countdown function before round begins, 
# giving players time to get ready
def countdown():
    
    time.sleep(0.5)
    print("GET READY TO GUESS WORD!")

    #This just prints 3 2 1, with a second wait between each number
    for count in ['3', '2', '1']:
        time.sleep(1)
        print(count)

    print("GO!\n")

#/****************************************************************************/

#Often need to print out long character line, so this function handles that
def line_printer():
    print("-----------------------------------")

#/****************************************************************************/

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
            print(f"Player {player + 1} " +
                  f"score for Round: {round_score[player]}")
            print(f"Player {player + 1} " +
                  f"streak: {streak[player]}")         
            print(f"PLAYER {player + 1} " +
                  f"TOTAL SCORE FOR ROUND {round_}: {score[player]}")
            line_printer()
    
    #Have some delay to allow player(s) to view scores
    time.sleep(3)

#/****************************************************************************/

#Calculate score for each player for a single round, if round wasn't failure
def score_calc(duration, player, score, round_score, streak):
    
    #Do score such that faster time gets more score, cap at 1000
    try:
        round_score[player] = min([round(100 / duration), 1000])

    #Account for possibility of duration being 0
    except ZeroDivisionError:
        round_score[player] = 1000

    finally:
        """Players get rewarded with 'streak' system,
            each consective round they successfully guess word,
            their streak increases by one, helping to improve overall score,
            but streak ends and starts from zero if they fail at any point"""
        round_score[player] *= streak[player]
        score[player] += round_score[player]

        #Return score for testing purposes
        return round_score

#/****************************************************************************/

#Main function to run entire game
def main_game(player_number, cheats):

    #Initialise scoring, for both 1 and 2 players
    score = [0,0]
    round_score = [0,0]
    streak = [0,0]

    #Generate list of all words
    word_list = grand_list_builder(wordlist_opener())

    """Generate list of all lengths to be used:
        - Start at length 4, as going smaller has lots of acronyms
        - End at 14, as English words longer than this aren't common"""
    all_word_lens = list(range(4,6))

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

            #Start countdown for the round
            countdown()

            #Run core game loop for single round
            duration, guesses_left = gameloop(word_len, word_list, cheats)

            #Determine round didn't fail, if so, add to score
            if guesses_left > 0:
                streak[player] += 1
                score_calc(duration, player, score, round_score, streak)

            #Round score is always 0 and streak ends if fail to guess word
            else:
                round_score[player] = 0
                streak[player] = 0
        
        #Prints score info at end of round, for player (or both players)
        info_printer(round_score, streak, round_, score, player_number)
    return score
        
#/****************************************************************************/

#Set up pre-game information
def begin_game(cheats):

    #Print out main title
    line_printer()
    if cheats:
        print("\nWELCOME TO HANGMAN (with cheats)!\n")
    else:   
        print("\nWELCOME TO HANGMAN!\n")
    line_printer()

    #Next piece of code is to figure out number of players
    player_number = 0

    #Check that '1' or '2' is inputted, 
    # and nothing else ('3' still quits program)
    valid_player_numbers = [1,2]
    while True:

        player_number = inputter(
            "Enter '1' for singleplayer, enter '2' for multiplayer: ") 

        #Try to find if input is valid number
        try:
            player_number = int(player_number)
        except ValueError:
            print("\nNot a whole number.")
        else:
            if player_number not in valid_player_numbers:
                print("\nNot a valid number.")
            else:
                #If no problems occured, leave loop
                break

    #Print out relevant message to response
    if player_number == 1:
        print("You have chosen singleplayer.")
    else:
        print("You have chosen multiplayer.")
    
    #Return number of players
    return player_number

#/****************************************************************************/

#Function for contolling entire game, start to finish
def whole_game(cheats=False):

    try:
        #Start game, find number of players
        player_number = begin_game(cheats)

        #Get scores from main gameplay
        total_scores = main_game(player_number, cheats)
        if player_number == 2:
            scores = total_scores
        else:
            scores = total_scores[0]
        
        #Print final scores, easy for if there's one players
        if type(scores) == int:
            print(f"OVERALL SCORE: {scores}")

        #For two players, first print out both scores
        else:
            print(f"OVERALL SCORE FOR PLAYER 1: {scores[0]}")
            print(f"OVERALL SCORE FOR PLAYER 2: {scores[1]}\n")

            #Then determine who won, or if there was a tie
            if scores[0] > scores[1]:
                print("PLAYER 1 WINS!")
            elif scores[1] > scores[0]:
                print("PLAYER 2 WINS!")
            else:
                print("PLAYER 1 AND 2 ARE TIED!")

    #Terminate whole game if anytime '3' is entered
    except KeyboardInterrupt:
        print("Ended program early.")      
    
    #Always tell player(s) goodbye, 
    # give some time before program fully terminates
    finally:
        print("\nThanks for playing! Bye bye!\n")
        time.sleep(0.5)

#/****************************************************************************/

