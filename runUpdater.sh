#!/usr/bin/env bash

############ Update SSF2 Replays Repo Script ############

###### Global Variables

# Detected operating system
detected_os=""

# Constants for exit codes
SUCCESS=0
ERROR=1
UP_TO_DATE=2

# Name of README updater script
UPDATE_SCRIPT="updateREADME.py"

# Global variable for replay line prefix
REPLAY_LINE_PREFIX="### Replay Count"


###### Helper Functions

### Helper function to determine OS type
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        detected_os="Linux X230"
        echo -e "\nOS Detected: Ubuntu"

    elif [[ "$OSTYPE" == "msys" ]]; then
        detected_os="Windows LEGION"
        echo -e "\nOS Detected: Windows"

    else
        echo -e "\nSystem Detection Error!"
        exit $ERROR
    fi
}

### Function to commit to GitHub
commit_to_github() {
    ### Check repo
    # Notify
    echo -e "\nChecking repo..."

    # New line
    echo -e "\n"

    # Check against remote quietly
    git fetch > /dev/null

    # Get first part status
    git status | head -n 3

    # Wait for check
    echo -e "\n"
    read -p "If [up to date with 'origin/main'], press any key to continue ..."

    ### Upload to GitHub
    # Notify
    echo -e "\nUploading to GitHub..."

    # Add
    echo -e "\n"
    git add .

    # Commit
    echo -e "\n"
    git commit -m "$detected_os: <Player(s)>"

    # Add more info to commit
    git commit --amend

    # Push
    echo -e "\n"
    git push
}

### Function to find the line index with the replay count prefix
find_replay_line_index() {
    local line_index=0
    while IFS= read -r line; do
        line_index=$((line_index + 1))
        if [[ "$line" == "$REPLAY_LINE_PREFIX"* ]]; then
            echo "$line_index"
            return
        fi
    done < README.md
}

### Function to print the new replay count line
print_new_replay_line() {
    line_index=$(find_replay_line_index)
    if [[ -n "$line_index" ]]; then
        sed "${line_index}q;d" README.md
    fi
}



###### Main script execution

### Start message
clear
echo -e "\n### Welcome to SSF2 Repo Updater ###"

### Determine OS type
detect_os

# Notify
echo -e "\nUpdating README..."

# Run script quietly but capture exit code
python3 "$UPDATE_SCRIPT" > /dev/null 2>&1
python_exit_code=$?

# Check exit code and perform actions
if [ $python_exit_code -eq $SUCCESS ]; then
    # Notify success
    echo -e "\n$UPDATE_SCRIPT: README updated successfully!"

    # Commit to GitHub
    # commit_to_github

    # Print new replay line
    print_new_replay_line

elif [ $python_exit_code -eq $UP_TO_DATE ]; then
    # Notify already up to date and exit
    echo -e "\n$UPDATE_SCRIPT: README is already up to date!"
    exit $UP_TO_DATE

else
    # Notify error and exit
    echo -e "\n$UPDATE_SCRIPT: Error! Re-running with output..."
    python3 "$UPDATE_SCRIPT"
    exit $ERROR
fi

### Finish message
echo -e "\nFinished!\n"