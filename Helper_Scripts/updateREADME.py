#!/usr/bin/env python3

# Name: Update README
# Author: David
# Requirements: Python 3.8
# Run using: clear && python3 updateREADME.py 'verbose'

# Imports
import os
import sys
from ReplayLine import ReplayLine

# Exit codes
SUCCESS = 0
ERROR = 1
UP_TO_DATE = 2

# Readme file path
README_FILE_PATH = "README.md"


def main():
    # Start message
    printV("###### Update README by David ######")

    # Get new replay line
    newReplayLine = getNewReplayLine()

    # Update current replay count line
    updateReplayCountLine(newReplayLine)


def getNewReplayLine():
    # Get parent folder of script folder
    scriptPath = os.path.abspath(os.path.dirname(__file__))
    replayPath = os.path.dirname(scriptPath)

    # Get all file paths with the .ssfrec extension
    # in the current directory and its subdirectories,
    # excluding the .git folder
    replayFiles = [
        os.path.join(root, file)
        for root, dirs, files in os.walk(replayPath)
        if '.git' not in root
        for file in files
        if file.endswith('.ssfrec')
    ]

    # The replay count is the number of .ssfrec paths
    replayCount = len(replayFiles)

    # If none found, notify and stop
    if replayCount == 0:
        printV("\nERROR! No replays found!")
        sys.exit(ERROR)
    
    # Create ReplayLine and return
    newReplayLine = ReplayLine(replayCount=replayCount)
    printV("\nGenerated new line: " + newReplayLine.to_string())
    return newReplayLine


def updateReplayCountLine(newReplayLine):
    # New content holder
    updatedContent = ""

    # Flag to track if the replay line is found
    replayLineFound = False

    # Open README file in read mode
    with open(README_FILE_PATH, "r") as readmeFile:

        # Iterate over lines, processing each
        for line in readmeFile:
            replayLineFound, updatedContent = processReadmeLine(line, newReplayLine, replayLineFound, updatedContent)

    # If the replay line is found
    if replayLineFound:

        # Open README file in write mode and write new content
        with open(README_FILE_PATH, "w") as readmeFile:
            readmeFile.write(updatedContent)

        # Notify about success and exit with success code
        printV("\nSuccessfully updated README!")
        sys.exit(SUCCESS)
    else:
        # Else if not found, notify and exit with error code
        printV("\nERROR! Replay line not found in README.")
        sys.exit(ERROR)


def processReadmeLine(line, newReplayLine, replayLineFound, updatedContent):

    # If the given line is the replay line of the README file
    if ReplayLine.isReplayLine(line):

        # If the replay line matches the new one
        if ReplayLine(line) == newReplayLine:

            # Notify and exit with up-to-date code
            printV("\nReplay line is already up to date!")
            sys.exit(UP_TO_DATE)
        else:
            # Else if replay line needs updating:
            # Convert new line to string
            newReplayLineS = newReplayLine.to_string()

            # Always print out new line
            print("New line: " + newReplayLineS)

            # Append new line to content instead of old line
            updatedContent += newReplayLineS + "\n"

            # Set the flag to indicate that the replay line is found
            replayLineFound = True
    else:
        # For normal lines, just append as-is
        updatedContent += line

    return replayLineFound, updatedContent


# Helper function to print message if 'verbose' is given as an argument
def printV(message):
    if 'verbose' in sys.argv:
        print(message)


# If file is run from the command line:
if __name__ == '__main__':
    # Run main and exit
    sys.exit(main())