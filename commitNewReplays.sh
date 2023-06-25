#!/usr/bin/env bash

############ Update SSF2 Replays Repo Script ############

###### Global Variables

# Name of helper script folder
SCRIPT_FOLDER="Helper_Scripts"

# Name of README updater script
UPDATE_SCRIPT="$SCRIPT_FOLDER/updateREADME.py"

# Constants for README script exit codes
README_SUCCESS=0
README_ERROR=1
README_UP_TO_DATE=2

# Name of commit script
COMMIT_SCRIPT="$SCRIPT_FOLDER/commitToGit.sh"



###### Main Script Execution

### Clear terminal and print start message
clear
echo -e "\n### Welcome to SSF2 Repo Updater ###"

# TEST!!!
./$COMMIT_SCRIPT




# # Notify
# echo -e "\nUpdating README..."

# # Run script quietly but capture exit code
# python3 "$UPDATE_SCRIPT" > /dev/null 2>&1
# python_exit_code=$?

# # Check exit code and perform actions
# if [ $python_exit_code -eq $README_SUCCESS ]; then
#     # Notify README_SUCCESS
#     echo -e "\n$UPDATE_SCRIPT: README updated README_SUCCESSfully!"

#     # Commit to GitHub
#     # commit_to_github

# elif [ $python_exit_code -eq $UP_TO_DATE ]; then
#     # Notify already up to date and exit
#     echo -e "\n$UPDATE_SCRIPT: README is already up to date!"
#     exit $UP_TO_DATE

# else
#     # Notify error and exit
#     echo -e "\n$UPDATE_SCRIPT: Error! Re-running with output..."
#     python3 "$UPDATE_SCRIPT"
#     exit $ERROR
# fi

# ### Finish message
# echo -e "\nFinished!\n"