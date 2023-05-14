# Coder Academy Assignment T1A3 - Raphael Florea

## Important links:

[Github](https://github.com/ausraf720/RaphaelFlorea_T1A3) 
<br>

[Presentation](https://www.youtube.com/watch?v=MnlbGMgQAEI) 
<br>

[Trello board](https://trello.com/b/gKbjakpR/project-management) 
<br>

[List of English words for usage in game](https://github.com/first20hours/google-10000-english) 
<br>

## Overview of project

This project aims to simulate the game 'hangman' in a computer program. It is also designed to incorporate additional features, such as having a timing system for scoring, multiplayer, using words of longer lengths as the game progresses, and giving hints.

## Styling of Code

### Code styled to use some PEP 8 guidelines:

* Each line has no more than 79 lines
* Indentation uses 4 spaces
* Appropriate use of white space in expressions and statements
* Variable names use lowercase_with_underscores
* Continuation lines start at opening delimiter in previous line, applies to some functions and print statements

[Link to PEP 8 styling](https://peps.python.org/pep-0008/)

## Implementation plan

### Features to be included, in order of priority:

1. Random word selection feature, where the player then has to guess the letters in that word, and has 10 guesses to guess the word.
2. Hangman pictures to be displayed, and the one that displays depends on the number of guesses left where less guesses causes hangman to be closer to being hanged.
3. Different word levels, where a game starts off with short words but gradually introduces longer words which can give more points.
4. Competitive multiplayer feature, which requires a scoring system where players score better if they can guess the word faster.
5. Hint system, where if a player is almost out of guesses, game will give a single letter hint to help player.

##### Screenshots of project management software usage at bottom of this readme.

### Checklist:

1. **Random word selection:**
- [x] Find large English word list and import into python to be used for random word selection 
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
- [x] Then implement score system based off timings, as well as word levels, where faster times result in better scores 
- [x] More words guessed successfully consecutively also result in better scores
- [x] Finally implement multiplayer system to allow for competitive play

6. **Additional features:**
- [x] Assign key that can end game at any time
- [x] Bash script that can run program
- [x] Same script can also run program tests if so desired

## Instructions to run program

### OS/System requirements

Program should run on any system with Python 3 installed. Bash scripts will open up Python 3 download page if not installed on system, but this only works for Mac and Windows users (not Linux). Users of other OSs need to manually locate the download page themselves. Bash scripts will install necessary dependencies into virtual environment.

### Opening the program:
1. In terminal, change current working directory to the src folder.

2. Run bash script with: 
```
bash index.sh
```
3. Bash script will firstly determine if Python 3 is installed and can run, if not installed then [download Python 3 here](https://www.python.org/downloads/). Otheriwse, 1st bash script will load 2nd bash script that contains Python files.

4. Virtual environment is created and activated (then deactivated and deleted at end of everything).

5. Bash script will then ask if want to run tests, run game with cheats, or run tests. Running tests can be done by entering just letter 't'.

6. If test is chosen, pip will install pytest in venv and tests will be run.

7. If 'c' is entered, program will run but with cheats, meaning whenever a round of hangman starts, the word to be guessed will be shown. This is used mainly for testing purposes.

8. If neither of the above option is selected, program will run normally and game will begin.

### Game start instructions:
1. Firstly note, at any input, enter '3' to close the game.

2. At start of game, press '1' for single player, or '2' for multiplayer.

3. Game has 10 rounds of hangman for each player:
* ##### For single player, 10 rounds carry out normally, and player must attempt to guess each word with 10 spare guesses per round. 
* ##### For multiplayer, player1 has a go at a 1st round, then player2 1st round, then back to player1 for 2nd round, etc. with each player having 10 spare guesses for each of their rounds.

4. For every round, player gets 10 spare guesses. They must guess all the letters in a hidden word. Everytime they make a wrong guess, they lose a spare guess. If they reach 0 guesses, they fail the round and don't score any points for that round.

5. For first round for the player(s), the length of the word is 4 letters (repeated letters are allowed). For each successive round, the length of the word increases by 1 letter, until the last round (round 10), where words are of length 13.

6. Once all 10 rounds are finished, scores are summmed up. For multiplayer, whoever has highest score wins, and if both players have same score, it is a tie.

### Scoring system explanation:
1. Score for a round is firstly determined by time to guess the entire word, using the formula below (note, the score is rounded to the nearest integer):
```
score for round = 100/seconds
```
2. Another factor in scoring is 'streaks'. Streaks occur when a player has successfully guessed words consecutive times. For the 1st round, if the player gets a word correct, they get a streak of 1, then if they get the next word, they're on a streak of 2, then 3 etc. until they fail to guess a word. Then the streak goes back to 0, and they have to start building up the streak again. This streak is then accounted for in the final formula:
```
score for round = streak * (100/seconds)
```
 3. The final score is the sum of all the scores of the individual rounds using the above formula.

## Testing information

Automatic tests can be found when running bash scripts and entering 't', but can also be found [here](src/testing.py). They test 2 things:

1. Score system

2. Letter guess system

Manual testing can be done by running bash scripts and entering 'c', which allows the game to play with cheats, so that the word needed to be guessed can be viewed. 

The streak system was manually tested, and the results can be replicated by playing the game with cheats and in singleplayer mode. [Here](./docs/Manual%20testing%20screenshots/Streak%20manual%20testing.pdf) is a link to the spreadhsheet for the manual test.

Below are images as proof for the tests:

1. Test 1:

![Test 1 pic 1](./docs/Manual%20testing%20screenshots/Test%201%20pic%201.png)

2. Test 2:

![Test 2 pic 1](./docs/Manual%20testing%20screenshots/Test%202%20pic%201.png)
![Test 2 pic 2](./docs/Manual%20testing%20screenshots/Test%202%20pic%202.png)

3. Test 3:

![Test 3 pic 1](./docs/Manual%20testing%20screenshots/Test%203%20pic%201.png)
![Test 3 pic 2](./docs/Manual%20testing%20screenshots/Test%203%20pic%202.png)
![Test 3 pic 3](./docs/Manual%20testing%20screenshots/Test%203%20pic%203.png)



## Trello project management screenshots (in chronological order)

![Trello screenshot 1](./docs/Trello%20screenshots/Trello%201.png)
![Trello screenshot 2](./docs/Trello%20screenshots/Trello%202.png)
![Trello screenshot 3](./docs/Trello%20screenshots/Trello%203.png)
![Trello screenshot 4](./docs/Trello%20screenshots/Trello%204.png)
![Trello screenshot 5](./docs/Trello%20screenshots/Trello%205.png)
![Trello screenshot 6](./docs/Trello%20screenshots/Trello%206.png)
![Trello screenshot 7](./docs/Trello%20screenshots/Trello%207.png)
![Trello screenshot 8](./docs/Trello%20screenshots/Trello%208.png)
![Trello screenshot 9](./docs/Trello%20screenshots/Trello%209.png)
![Trello screenshot 10](./docs/Trello%20screenshots/Trello%2010.png)
![Trello screenshot 11](./docs/Trello%20screenshots/Trello%2011.png)
![Trello screenshot 12](./docs/Trello%20screenshots/Trello%2012.png)
![Trello screenshot 13](./docs/Trello%20screenshots/Trello%2013.png)
![Trello screenshot 14](./docs/Trello%20screenshots/Trello%2014.png)
![Trello screenshot 15](./docs/Trello%20screenshots/Trello%2015.png)
![Trello screenshot 16](./docs/Trello%20screenshots/Trello%2016.png)
![Trello screenshot 17](./docs/Trello%20screenshots/Trello%2017.png)
![Trello screenshot 18](./docs/Trello%20screenshots/Trello%2018.png)
![Trello screenshot 19](./docs/Trello%20screenshots/Trello%2019.png)