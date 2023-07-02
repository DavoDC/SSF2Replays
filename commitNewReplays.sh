#!/usr/bin/env bash

############ SSF2 Replays Repo Updater ############

###### Global Variables

# Helper script path
SCRIPT_FOLDER="Helper_Scripts"

# README updater script path
README_SCRIPT="$SCRIPT_FOLDER/update_readme.py"

# README updater script exit codes (Must match those defind in python!)
README_SUCCESS=0
README_ERROR=1
README_UP_TO_DATE=2

# Commit script path
COMMIT_SCRIPT="$SCRIPT_FOLDER/commitToGit.sh"


###### Main Script Execution

# Clear terminal and print start message
clear
echo -e "\n### SSF2 Replays Repo Updater ###"

# Check Python 3 installation
if ! command -v python3 &> /dev/null; then
    echo -e "Error: Python 3 is required but not found."
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
    echo -e "\nError!"
    exit $README_ERROR
fi