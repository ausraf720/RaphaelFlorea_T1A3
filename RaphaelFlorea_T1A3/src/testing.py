import pytest
from main import score_calc
from hangman_gameloop import hangman_loop, letter_validator

#/***********************************************************************************************/
#/***********************************************************************************************/

#INITALISE VARIABLES FOR TESTING SCORE SYSTEM

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