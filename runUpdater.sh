#!/bin/sh

###### Update SSF2 Replays Repo Script ######


### Start message
clear
echo -e "\n### Welcome to SSF2 Repo Updater ###"


### Determine OS type

# System booleans - True if running on that system
ubuntu=false     
windows=false

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # If on Linux, we are on Ubuntu:
    ubuntu=true
    echo -e "\nSystem Detected: Ubuntu"

elif [[ "$OSTYPE" == "msys" ]]; then
    # If on MinGW, we are on Git-Bash/Windows:
    windows=true
    echo -e "\nSystem Detected: Windows"

else
    echo -e "\nSystem Detection Error!"
    exit
fi



### Update README
# Notify
echo -e "\nUpdating README..."

# Run script silently
python3 updateREADME.py > /dev/null




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

# Set commit heading depending on system type
commit_heading=""
if [ "$ubuntu" = true ]; then
	commit_heading="Linux X230: <Player(s)>"
elif [ "$windows" = true ]; then
	commit_heading="Windows LEGION: <Player(s)>"
fi

# Commit
echo -e "\n"
git commit -m "$commit_heading"

# Add more info to commit
git commit --amend

# Push
echo -e "\n"
git push





### Print last line of README (the new Replay count)
echo -e "\n"
tail -1 README.md


### Finish message
echo -e "\n\nFinished!\n"




