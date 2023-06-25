#!/usr/bin/env bash

############ Update SSF2 Replays Repo Script ############


###### Global Variables

# Helper script path
SCRIPT_FOLDER="Helper_Scripts"

# README updater script path
README_SCRIPT="$SCRIPT_FOLDER/updateREADME.py"

# Constants for README script exit codes
README_SUCCESS=0
README_ERROR=1
README_UP_TO_DATE=2

# Commit script path
COMMIT_SCRIPT="$SCRIPT_FOLDER/commitToGit.sh"



###### Main Script Execution

# Clear terminal and print start message
clear
echo -e "\n### Welcome to SSF2 Repo Updater ###"


# Notify
echo -e "\n# Checking files..."


# Run README script and capture its output
readme_output=$(python3 "$README_SCRIPT") 
python_exit_code=$?


# Act based on README script exit code
if [ $python_exit_code -eq $README_SUCCESS ]; then

    # If README was updated, we assume replays need updating too.
    echo -e "New files detected!"
    echo -e "\n# Updated README replay count!"
    echo "$readme_output"
    echo -e "\n# Starting commit sequence!"
    ./$COMMIT_SCRIPT

elif [ $python_exit_code -eq $README_UP_TO_DATE ]; then

    # If README is up-to-date, we assume replays are too.
    echo -e "\nAlready up to date!"
    exit $README_UP_TO_DATE

else
    # If README update fails, re-run README script verbosely and exit
    echo -e "\nError! Re-running with output..."
    python3 "$README_SCRIPT" "verbose"
    exit $README_ERROR
fi


# Finish message
echo -e "\n# Finished!"