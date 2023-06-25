#!/usr/bin/env bash


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


### Fetch from remote quietly, notifying if fails
fetch_output=$(git fetch origin 2>&1)
fetch_exit_code=$?
if [[ $fetch_exit_code -ne 0 ]]; then
    echo -e "\nFailed to connect to GitHub!"
    echo -e "$fetch_output"
    exit 1
fi


### Check local repo against remote
# Get the latest hashes of local and remote commits
latest_local_commit_hash=$(git rev-parse HEAD)
latest_remote_commit_hash=$(git rev-parse origin/main)
# If they don't match
if [ "$latest_local_commit_hash" != "$latest_remote_commit_hash" ]; then
    # Notify, pull, and exit
    echo -e "\nThe local repo is not up-to-date with the remote!"
    echo -e "Updating from the remote and exiting. Please check results and try again.\n"
    git pull
    exit 1
fi


### Check if local repo has uncommitted changes
# Get porcelain git status output
status_output=$(git status --porcelain)
# If output empty
if [[ -z "$status_output" ]]; then
    # Notify
    echo -e "\nThe local repo has no new changes!"
    exit 1
fi


### Upload to GitHub
# Notify
echo -e "\nRepo passed checks!"
echo -e "\nStarting GitHub update..."

# Add all new files
git add .

# Commit with message
git commit -m "$detected_os: <Player(s)>"

# Add commit description via text editor
git commit --amend

# Push to remote
git push