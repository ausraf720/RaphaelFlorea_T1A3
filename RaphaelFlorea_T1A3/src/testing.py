#/***********************************************************************************************/

import pytest
from main import score_calc
from hangman_gameloop import guess_checker

#/***********************************************************************************************/
#/***********************************************************************************************/

#TESTING FOR SCORE SYSTEM - TEST IF SCORES OUTPUTTED ARE CORRECT

#Initialise variables
#Player1 is index 0, only testing player1
player1 = 0
#Overall_score always at 0 for both players, doesn't affect result
overall_score_0 = [0,0]
#Round_score always at 0 for both players, doesn't affect result
round_score_0 = [0,0]

#Streaks start at 1 for both players (but will be changed later)
streak_1 = [1,1]

#/***********************************************************************************************/

#FIRST AND SECOND TEST
"""Want to test if given a short duration or 0 duration,
    scoring system will give player max score of 1000 for that round
"""
large_result = 1000
duration_0 = 0
duration_small = 0.00000001
test1 = (duration_0, player1, overall_score_0, round_score_0, streak_1, large_result)
test2 = (duration_small, player1, overall_score_0, round_score_0, streak_1, large_result)

#THIRD TEST
"""Want to test if given a very large duration of time, like an hour,
    scoring system will give player score 0 for that round
"""
duration_hour = 60 * 60
small_result = 0
test3 = (duration_hour, player1, overall_score_0, round_score_0, streak_1, small_result)

#FOURTH TEST
"""Want to test if player 1 has streak of 5, 
    and duration of 50 seconds for turn
    their score should be (100 / 50) * 5 = 10
"""
duration_50 = 50
streak_5 = [5,0]
result_10 = 10
test4 = (duration_50, player1, overall_score_0, round_score_0, streak_5, result_10)

#FIFTH TEST
"""Want to test if player 1 has streak of 7, 
    and duration of 5 seconds for turn
    their score should be (100 / 5) * 7 = 140
"""
duration_5 = 5
streak_7 = [7,0]
result_140 = 140
test5 = (duration_5, player1, overall_score_0, round_score_0, streak_7, result_140)

#/***********************************************************************************************/

#NOW RUN ALL TESTS TOGETHER
@pytest.mark.parametrize(('duration', 'player', 'score', 'round_score', 'streak', 'result'), 
                         [test1, test2, test3, test4, test5])
def test_scorer(duration, player, score, round_score, streak, result):

    player_round_score = score_calc(duration, player, score, round_score, streak)
    assert player_round_score[0] == result

#/***********************************************************************************************/
#/***********************************************************************************************/

#TESTING FOR CHECKING IF LETTER IN WORD - TEST IF FUNCTION DETERMINES IF GUESSED LEFT REDUCES

#Initialise variables, for these tests word length will be length 5
#Word shown is blank, doesn't affect test result
word_shown = ['_', '_', '_', '_', '_']
#No incorrect guesses to start with, doesn't affect test result
incorrect_guesses = []

#Start with guesses left as 10, but will change later
guesses_left_10 = 10
#Start with word 'snake', but will change later
guess_word_snake = ['s', 'n', 'a', 'k', 'e']

#/***********************************************************************************************/

#If 10 guesses left, and 'e' is guessed, 'e' is in snake, so guesses should stay 10
letter_e = 'e'
result_10 = 10
test6 = (letter_e, guess_word_snake, word_shown, incorrect_guesses, guesses_left_10, result_10)

#If 10 guesses left, and 'f' is guessed, 'f' is not in snake, so guesses should go down to 9
letter_f = 'f'
result_9 = 9
test7 = (letter_f, guess_word_snake, word_shown, incorrect_guesses, guesses_left_10, result_9)

#Test with double-letter words
#If 5 guesses left, and 'o' is guessed, 'o' is in books, so guesses should stay at 5
letter_o = 'o'
guesses_left_5 = 5
result_5 = 5
guess_word_books = ['b', 'o', 'o', 'k', 's']
test8 = (letter_o, guess_word_books, word_shown, incorrect_guesses, guesses_left_5, result_5)

#If 7 guesses left, and 'z' is guessed, 'z' is not in snake, so guesses should go down to 6
letter_z = 'z'
guesses_left_7 = 7
result_6 = 6
test9 = (letter_z, guess_word_books, word_shown, incorrect_guesses, guesses_left_7, result_6)

#If 1 guess left, and 's' is guessed, 's' is in books, so guesses should stay at 1
letter_s = 's'
guesses_left_1 = 1
result_1 = 1
test10 = (letter_s, guess_word_books, word_shown, incorrect_guesses, guesses_left_1, result_1)


#/***********************************************************************************************/

#NOW RUN ALL TESTS TOGETHER
@pytest.mark.parametrize(('letter', 'guess_word', 'word_shown', \
                          'incorrect_guesses', 'guesses_left', 'result'), 
                         [test6, test7, test8, test9, test10])
def test_guess_checker(letter, guess_word, word_shown, incorrect_guesses, guesses_left, result):

    guesses_left = guess_checker(letter, guess_word, word_shown, incorrect_guesses, guesses_left)
    assert guesses_left == result

#/***********************************************************************************************/