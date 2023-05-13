# Coder Academy Assignment T1A3 - Raphael Florea

## Important links:

[Github](https://github.com/ausraf720/RaphaelFlorea_T1A3) 
<br>

[Presentation (Not yet done)](https://www.youtube.com/) 
<br>

[Trello board](https://trello.com/b/gKbjakpR/project-management) 
<br>

## Overview of project

This project aims to simulate the game 'hangman' in a computer program. It is also designed to incorporate additional features, such as 

## Styling of Code

### Code styled to use some PEP 8 guidelines:

* Each line has no more than 79 lines
* Indentation uses 4 spaces
* Appropriate use of white space in expressions and statements
* Variable names use lowercase_with_underscores
* Continuation lines start at opening delimiter, applies to some functions and print statements

[Link to PEP 8 styling](https://peps.python.org/pep-0008/)

## Implementation plan:

### Features to be included, in order of priority:

1. Random word selection feature, where the player then has to guess the letters in that word, and has 10 guesses to guess the word
2. Hangman pictures to be displayed, and the one that displays depends on the number of guesses left where less guesses causes hangman to be closer to being hanged
3. Different word levels, where a game starts off with short words but gradually introduces longer words which can give more points
4. Competitive multiplayer feature, which requires a scoring system where players score better if they can guess the word faster
5. Hint system, where if a player is almost out of guesses, game will give a single letter hint to help player

### Checklist:

1. **Random word selection:**
- [x] Make word list and import into python to be used for random word selection 
- [x] Prompt user for input letter
- [x] Only allow user for 10 guesses

2. **Hangman pictures:**
- [x] Create hangman class to be displayed for each guess
- [x] Write necessary code to print out each instance of class when necessary

3. **Different word levels:**
- [x] Allow for program that incorporates different word levels

4. **Hint system:**
- [x] First implement for when player only has 1 guess left
- [x] Then make sure it only gets implemented once, so players don't get multiple hints

5. **Competitive system:**
- [x] Implement timing system so that times to guess words are recorded
- [x] Then implement score system based off timings, as well as word levels
- [x] Finally implement multiplayer system to allow for competitive play

6. **Additional features:**
- [x] Assign key that can end game at any time
- [x] Bash script that can run program
- [x] Same script can also run program tests if so desired

## How to run program:

### Opening the program:
1. In terminal, change directory to src/ folder.

2. Run bash script with: 
```
bash index.sh
```
3. Bash script will firstly determine if Python3 is installed and can run, if not installed [download Python3 here](https://www.python.org/downloads/).

4. Virtual environment is created and activated, then deactivated and deleted at end.

5. Bash script will then ask if want to run tests or run game, run tests can be done by entering just letter 't', run game can be done by entering anything else.

5. If test is chosen, pip will install pytest in venv and tests will be run.

6. If test is not chosen, program will run normally and game will begin.

### Game start instructions:
1. Firstly note, at any input, enter '3' to close the game.

2. At start of game, press '1' for single player, or '2' for multiplayer.

3. Game has 10 rounds of hangman for each player:
* ##### For single player, 10 rounds carry out normally, and player must attempt to guess each word within 10 spare guesses. 
* ##### For multiplayer, player1 has a go at a 1st round, then player2 1st round, then back to player1 for 2nd round, etc. with each round having 10 spare guesses.

4. For every round, player gets 10 spare guesses. They must guess all the letters in a hidden word. Everytime they make a wrong guess, they lose a spare guess. If they reach 0 guesses, they lose and don't score any points for that round.

5. For first round for the player(s), the length of the word is 4 letters (repeated letters are allowed). For each successive round, the length of the word increases by 1 letter, until the last round (round 10), where words are of length 13.

6. Once all 10 rounds are finished, scores are summmed up. For multiplayer, whoever has highest score wins, and if they have same score, it is a tie.

### Scoring system explanation:
1. Score for a round is firstly determined by time to guess the entire word, using the formula below (note, the score is rounded to the nearest integer):
```
score for round = 100/seconds
```
2. Another factor in scoring is 'streaks'. Streaks occur when a player has successfully guessed words consecutive times. For the 1st round, if the player gets a word correct, they get a streak of 1, then if they get the next word, they're on a streak of 2, then 3 etc. until they fail to guess a word. Then the streak goes back to 0. This streak is then accounted for in the final formula:
```
score for round = streak * (100/seconds)
```
 3. The final score is the sum of all the scores of the individual rounds using the above formula.