
### Update SSF2 Replays Repo Script

# Start message
clear
echo -e "\n### Welcome to SSF2 Repo Updater (WINDOWS)"
### CHANGED


### Update README
# Notify
echo -e "\nUpdating README..."

# Run script silently
python3 updateREADME.py > /dev/null



### Check new README
# DISABLED BECAUSE IT IS WORKING PERFECTLY
# Notify
# echo -e "\nNew README:"

# Print readme
# cat README.md

# New line
# echo -e "\n"

# Wait for check
# read -p "If the README looks correct, press any key to continue ..."



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

### CHANGED
git commit -m "Windows LEGION: <Player>"

# Check and/or amend commit (add more to message)
git commit --amend

# Push
echo -e "\n"
git push



### Open repo
# DISABLED
# Notify
# echo -e "\nOpening repo site..."

# Open repo link quietly
# bash -c "xdg-open https://github.com/DavoDC/SSF2Replays" 2> /dev/null > /dev/null



### Finish message
echo -e "\n\nFinished!\n"




