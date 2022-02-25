
### Update SSF2 Replays Repo Script

# Start message
clear
echo -e "\n### Welcome to SSF2 Repo Updater"


### Update README
# Notify
echo -e "\nUpdating README..."

# Run script silently
python3 updateREADME.py > /dev/null


### Check new README
# Notify
echo -e "\nNew README:"

# Print readme
cat README.md

# New line
echo -e "\n"

# Wait for check
read -p "If the README looks correct, press any key to continue ..."


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
read -p "If [up to date with 'origin/main'], press any key to continue ..."


### Upload to GitHub
# Notify
echo -e "\nUploading to GitHub..."

# Add
echo -e "\n"
git add .

# Commit
echo -e "\n"
git commit -m "New replays from Wine Linux X230"

# Check and/or amend commit
git commit --amend

# Push
echo -e "\n"
git push



### Open repo
# Notify
echo -e "\nOpening repo site..."

# Open repo link quietly
bash -c "xdg-open https://github.com/DavoDC/SSF2Replays" 2> /dev/null > /dev/null



### Finish message
echo -e "\n\nFinished!\n"




