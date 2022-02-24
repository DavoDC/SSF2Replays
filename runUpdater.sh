
### Update SSF2 Replays Repo Script

# Start message
clear
echo -e "\n### Welcome to SSF2 Repo Updater"


### Update README
# Notify
echo -e "\nUpdating README..."

# Run script silently
python3 updateREADME.py > NUL


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
git fetch > NUL

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

# Push
echo -e "\n"
git push


### Finish message
echo -e "\n\nFinished!\n"
