#!/usr/bin/env bash

############ SSF2 Replays Repo Updater ############

###### Global Variables

# Helper script paths
SCRIPT_FOLDER="Helper_Scripts"
README_SCRIPT="$SCRIPT_FOLDER/update_readme.py"
COMMIT_SCRIPT="$SCRIPT_FOLDER/commitToGit.sh"

# README updater script exit codes (Must match those defined in python!)
README_SUCCESS=0
README_ERROR=1
README_UP_TO_DATE=2

###### Main Script Execution

# Clear terminal and print start message
clear
echo -e "\n### SSF2 Replays Repo Updater ###"

# Check if the scripts can be found
if [ ! -f "$README_SCRIPT" ] || [ ! -f "$COMMIT_SCRIPT" ]; then
    echo -e "\nError: Could not locate helper script(s)!"
    exit $README_ERROR
fi

# Check Python 3 installation
if ! command -v python3 &> /dev/null; then
    echo -e "\nError: Python 3 is required but was not found!"
    exit $README_ERROR
fi

# Run README script and capture its output
echo -e "\n# Checking files..."
readme_output=$(python3 "$README_SCRIPT") 
readme_exit_code=$?

# Act based on README script exit code
if [ $readme_exit_code -eq $README_SUCCESS ]; then

    # If README was updated, we assume replays need updating too.
    # This works because we are comparing
    # the current replay count to the count previously committed.
    echo -e "New files detected!"
    
    echo -e "\n# Updated README replay count!"
    echo "$readme_output"

    echo -e "\n# Starting commit sequence!"
    ./$COMMIT_SCRIPT

    # Finish and exit
    echo -e "\n# Finished!"
    exit $README_SUCCESS

elif [ $readme_exit_code -eq $README_UP_TO_DATE ]; then

    # If README is up-to-date, we assume replays are too.
    echo -e "\nAlready up to date!"
    exit $README_UP_TO_DATE

else
    # If README update fails, notify and exit
    echo -e "\nError: README script failed!"
    exit $README_ERROR
fi