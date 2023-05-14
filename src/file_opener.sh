#!/bin/bash

#Create virtual environment, then activate
python3 -m venv hangman_venv
source hangman_venv/bin/activate

#Have option to either run test, or run program
echo "Enter 't' to run test, enter 'c' to run program with cheats."
echo "Enter anything else to run program normally."
read input
if [[ "$input" == "t" ]] ; then
	
    # Install pytest, then run program
    pip install pytest
    pytest testing.py

elif [[ "$input" == "c" ]] ; then

    #Run program file that enables cheats, no dependencies needed to be installed
    python3 run_game_cheats.py    

else
    #Run program, no dependencies needed to be installed
    python3 run_game.py
fi

#Deactivate then remove virtual environment after finishing
deactivate
rm -r hangman_venv