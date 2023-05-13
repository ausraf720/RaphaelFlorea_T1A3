#!/bin/bash

#Check if Python 3 is installed
if [[ -x "$(command -v python3)" ]]; then
    echo "Python 3 is installed. Able to run program."
else
    echo "Python 3 is not installed. Install before running."
    exit 1
fi

#Create virtual environment
python3 -m venv hangman_venv
source hangman_venv/bin/activate

echo "Enter 't' to run test, enter anything else to run program."
read input
if [[ "$input" == "t" ]] ; then
	
    # Install pytest, then run program
    pip install pytest
    pytest testing.py

else
    python3 run_game.py
fi

deactivate

#Remove virtual environment
rm -r hangman_venv