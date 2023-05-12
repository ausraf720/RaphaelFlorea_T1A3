#!/bin/bash

#Check if Python 3 is installed
if which python3 >/dev/null 2>&1; then
    echo "Python 3 is installed. This program will now run."
else
    echo "Python 3 is not installed. Install before running."
fi

#Create virtual environment
python3 -m venv hangman_venv

# Install pytest
pip install pytest

#Run file
pytest testing.py

#Remove virtual environment
rm -r hangman_venv