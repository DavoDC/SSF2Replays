#!/usr/bin/env bash

# Detected operating system
detected_os=""

echo -e "\nHello from commit to git!"


# ### Determine operating system
# if [[ "$OSTYPE" == "linux-gnu"* ]]; then
#     detected_os="Linux X230"
#     echo -e "\nOS Detected: Ubuntu"

# elif [[ "$OSTYPE" == "msys" ]]; then
#     detected_os="Windows LEGION"
#     echo -e "\nOS Detected: Windows"

# else
#     echo -e "\nSystem Detection Error!"
#     exit
# fi



# ### Check connection

# # TODO



# ### Check if repo is up-to-date
# # Notify
# echo -e "\nChecking repo..."

# # New line
# echo -e "\n"

# # Check against remote quietly
# git fetch > /dev/null

# # Get first part status
# git status | head -n 3

# # Wait for check
# echo -e "\n"
# read -p "If [up to date with 'origin/main'], press any key to continue ..."



# ### Upload to GitHub
# # Notify
# echo -e "\nUploading to GitHub..."

# # Add all files
# echo -e "\n"
# git add .

# # Commit with message
# echo -e "\n"
# git commit -m "$detected_os: <Player(s)>"

# # Add commit description via text editor
# git commit --amend

# # Push to remote
# echo -e "\n"
# git push
