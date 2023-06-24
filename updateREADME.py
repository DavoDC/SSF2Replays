#!/usr/bin/env python3

# Name: Update README
# Author: David
# Last Update: 24 JUNE 2023
# Requirements: Python 3.8
# Run using: clear && python3 updateREADME.py
# Run in: SSF2Replays repo folder

import os
import sys
import datetime

# String constants
REPLAY_COUNT_PLACEHOLDER = "NUM"
DATE_PLACEHOLDER = "DATE"
TEMPLATE_STRING = f"### Replay Count = {REPLAY_COUNT_PLACEHOLDER} (as of {DATE_PLACEHOLDER})"
README_FILE_PATH = "README.md"

def main():
    print("###### Update README by David ######")
    updateReplayCountLine(getNewReplayCountLine())

def getNewReplayCountLine():
    # Initialize template
    newReplayLine = TEMPLATE_STRING

    # Get replay count
    # Get the directory that script is running in
    runPath = os.path.abspath(os.path.dirname(__file__))

    # Get all file paths with the .ssfrec extension
    # in the current directory and its subdirectories,
    # excluding the .git folder
    replayFiles = [
        os.path.join(root, file)
        for root, dirs, files in os.walk(runPath)
        if '.git' not in root
        for file in files
        if file.endswith('.ssfrec')
    ]

    # The replay count is the number of .ssfrec paths
    replayCount = len(replayFiles)

    # Replace replay count
    newReplayLine = newReplayLine.replace(REPLAY_COUNT_PLACEHOLDER, str(replayCount))

    # Replace date
    dateS = datetime.datetime.today().strftime('%d/%m/%y')
    newReplayLine = newReplayLine.replace(DATE_PLACEHOLDER, str(dateS))

    # Notify and return
    print("\nGenerated new line: \n" + newReplayLine)
    return newReplayLine

def updateReplayCountLine(newReplayLine):
    # New content holder
    updatedContent = ""
    
    # Flag to track if the replay line is found
    replayLineFound = False
    
    # Open README file in read mode and iterate over lines
    with open(README_FILE_PATH, "r") as readmeFile:
        for line in readmeFile:

            # If the line starts with part of the template
            if line.startswith(TEMPLATE_STRING.split(" = ")[0]):

                # Append the new replay line instead
                updatedContent += newReplayLine + "\n"

                # Set the flag to indicate that the replay line is found
                replayLineFound = True
            else:
                # For normal lines, just append
                updatedContent += line

    # If the replay line is found
    if replayLineFound:

        # Open README file in write mode
        with open(README_FILE_PATH, "w") as readmeFile:

            # Write the updated content to the file
            readmeFile.write(updatedContent)
        
        # Display a success message
        print("\nSuccessfully updated README!")
    else:
        # Display an error message if the replay line is not found
        print("\nERROR! Replay line not found in README.")

# If file is run from the command line:
if __name__ == '__main__':
    # Run main and exit
    sys.exit(main())