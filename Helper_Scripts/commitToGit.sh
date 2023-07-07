#!/usr/bin/env bash


### Fetch from remote quietly, notifying if fails
fetch_output=$(git fetch origin 2>&1)
fetch_exit_code=$?
if [[ $fetch_exit_code -ne 0 ]]; then
    echo -e "\nFailed to connect to GitHub!"
    echo -e "$fetch_output"
    exit 1
fi


### Check local repo against remote
# Compare hashes of latest local and remote commits
latest_local_commit_hash=$(git rev-parse HEAD)
latest_remote_commit_hash=$(git rev-parse origin/main)
if [ "$latest_local_commit_hash" != "$latest_remote_commit_hash" ]; then

    # Notify, pull, and exit
    echo -e "\nThe local repo is not up-to-date with the remote!"
    echo -e "Updating from the remote and exiting. Please check results and try again.\n"
    git pull
    exit 1
fi


### Check the uncommitted changes to the local repo
# Save git status output to a variable
status_output=$(git status --porcelain --untracked-files=all)

# If output is empty, notify
if [[ -z "$status_output" ]]; then
    echo -e "\nThe local repo has no new changes!"
    exit 1
elif ! echo "$status_output" | grep -q ".ssfrec"; then
    # Else if there are changes, but none involving replays, notify and exit
    echo -e "\nNo new replays found!"
    exit 1
fi


### Detect operating system, notifying if fails
detected_os=""
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    detected_os="Linux X230"
elif [[ "$OSTYPE" == "msys" ]]; then
    detected_os="Windows LEGION"
else
    echo -e "\nOperating System Detection Error!"
    exit 1
fi


### Upload to GitHub

# Add all new files
git add .

# Commit with message
git commit -m "$detected_os: <Player(s)>"

# Add commit description via text editor
git commit --amend

# Push to remote
git push