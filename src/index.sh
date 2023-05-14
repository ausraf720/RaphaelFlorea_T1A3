#!/bin/bash

#Check if Python 3 is installed, exit if not
if  [[ -x "$(command -v python3)" ]]; then
    echo "Python 3 is installed. Able to run program."
    bash file_opener.sh
else
    echo "Python 3 is not installed. Install before running."

    #Now open up web browser for python3 depending on OS:
    website="https://www.python.org/downloads/"
    if [[ "$OSTYPE" == "darwin"* ]]; then
        open "$website"
    elif [[ "$OSTYPE" == "msys"* ]]; then
	    start "$website"
    fi
    exit 1

    #NOTE: Will not open on Linux or other OSs, 
    # however program will still work normally if Python3 installed
fi