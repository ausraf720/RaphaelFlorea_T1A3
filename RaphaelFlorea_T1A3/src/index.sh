#!/bin/bash

#Check if Python 3 is installed, exit if not
if [[ -x "$(command -v python3)" ]]; then
    echo "Python 3 is installed. Able to run program."
else
    echo "Python 3 is not installed. Install before running."
    exit 1
fi

#Create virtual environment, then activate
python3 -m venv hangman_venv
source hangman_venv/bin/activate

#Have option to either run test, or run program
echo "Enter 't' to run test, enter anything else to run program."
read input
if [[ "$input" == "t" ]] ; then
	
    # Install pytest, then run program
    pip install pytest
    pytest testing.py

else
    #Run program, no dependencies needed to be installed
    python3 run_game.py
fi

#Deactivate then remove virtual environment after finishing
deactivate
rm -r hangman_venv