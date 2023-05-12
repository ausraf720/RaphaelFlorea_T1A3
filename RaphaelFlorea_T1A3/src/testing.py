import pytest
from main import score_calc
from hangman_gameloop import hangman_loop, letter_validator



def score_test_1():

    #first check for divide by zero
    #check duration 0 doesn't cause issue

    duration = 0.0
    player = 0
    score = [0,0]
    round_score = [0,0]
    streak = [0,0]
    player_round_score = score_calc(duration, player, score, round_score, streak)


    assert player_round_score[0] == 1000

def score_test_2():
    pass

    #check extremely small duration still only goes up to 1000 score
    duration = 0.000000001
    player = 0
    score = [0,0]
    round_score = [0,0]
    streak = [0,0]
    player_round_score = score_calc(duration, player, score, round_score, streak)

    assert player_round_score[0] == 1000


